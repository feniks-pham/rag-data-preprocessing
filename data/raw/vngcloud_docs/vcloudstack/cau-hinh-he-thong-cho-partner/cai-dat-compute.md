# Cài đặt Compute

## Sơ đồ hệ thống vCloudStack

vCloudStack sẽ cơ bản được triển khai với sơ đồ hệ thống như sau:

<figure><img src="../../.gitbook/assets/image (830).png" alt=""><figcaption></figcaption></figure>

* Thông qua bộ Controller,  giao diện tương tác của người dùng (portal) sẽ tương tác bằng API để có thể nắm các thông tin từ các compute và ceph cluster trong hạ tầng.
* Ngoài việc bộ Controller kết nối với các bộ comput và Ceph Cluster để theo dõi các thông số hoạt động thì bộ Controller cũng kết nối với bộ định tuyến mạng (Switch) cũng để theo dõi trạng thái mạng đang hoạt động trong hạ tầng nội bộ của doanh nghiệp.

***

## 1/ Các thành phần chính trên Compute

Các node compute sẽ có các service chính:

* nova\_compute;
* neutro\_network\_agent (OVS),
* monitoring (monasca-agent\_collector, telegraf);

## 2/ Cài đặt các thành phần chính trên Compute:

### Network Config

Network trên compute cần có 2 vlan (management,neutron vlan).

```
network:
  version: 2
  renderswer: networkd
  ethernets:
    eno2:
      match:
        name: eno2
      set-name: eno2
      addresses: []
      dhcp4: no
      #      type: networkd
      #      bootproto: none
      #      name: eno2
      #      onboot: yes
 
  vlans:
    eno2.3321:
      id: 3323
      link: eno2
      addresses:
        - 10.237.123.4/24
      gateway4: 10.237.123.254
      dhcp4: no
  vlans:
    eno2.3330:
      id: 3330
      link: eno2
      dhcp4: no
```

Trên terminal deployer run command để thực hiện install các service (nova, neutron agent)

```
ansible-playbook -i mutinode deploy -l $NEW_KVM
```

Cần thêm các cấu hình trong file globals.yml. File globals.yml là file cấu hình chính cho Kolla Ansible, mặt định sẽ nằm trong /etc/kolla/globla.yml.

```
workaround_ansible_issue_8743: yes
kolla_base_distro: "ubuntu"
node_custom_config: "~/kolla/config"
kolla_internal_vip_address: "xx.xx.xx.xx" # VIP được cấu hình ở controller
network_interface: "eno2.3321" # Management vlan
neutron_external_interface: "eno2.3330" #Neutron interface
enable_cinder: "yes"
ceph_cinder_keyring: "ceph.client.cinder.keyring"
ceph_cinder_user: "cinder"
ceph_cinder_pool_name: "volumes"
ceph_nova_keyring: "{{ ceph_cinder_keyring }}"
ceph_nova_user: "{{ ceph_cinder_user }}"
ceph_nova_pool_name: "vms"

```

### Nova Compute

Mặc định (default) sẽ cấu hình là:

```
[DEFAULT]
debug = False
log_dir = /var/log/kolla/nova
state_path = /var/lib/nova
allow_resize_to_same_host = true
compute_driver = libvirt.LibvirtDriver
my_ip = 10.237.123.4
transport_url = rabbit://openstack:PASSWORD@10.237.121.11:5672,openstack: PASSWORD@10.237.121.12:5672,openstack:PASSWORD@10.237.121.13:5672//
```

Để tạo được server với các OS mong muốn cần cấu hìn service Glance API cho compute:

```
[glance]
debug = False
api_servers = http://10.237.121.210:9292
cafile =
num_retries = 3
```

Mặc định, các server được khởi tạo từ image sẽ được tạo trên pool LAB-SSD-02

```
[libvirt]
connection_uri = qemu+tcp://10.237.123.4/system
live_migration_inbound_addr = 10.237.123.4
virt_type = kvm
num_pcie_ports = 16
images_type = rbd
images_rbd_pool = LAB-SSD-02
images_rbd_ceph_conf = /etc/ceph/ceph.conf
rbd_user = cinder
rbd_secret_uuid = <secret_uuid>
```

Khi tạo server sẽ có một ứng dụng cloud-inti để chạy các đoạn script truyền vào. Để thực hiện lấy được đoạn script này các server phải được gọi về datastore endpoint. Khi đó cần cấu hình cho cả nova và neutron để thực hiện kết nối.

```
[neutron]
metadata_proxy_shared_secret = <secret0-key>
service_metadata_proxy = true
```

Vault được dùng cho phần quản lý mã khóa của tính năng mã hóa volume. Để các hypervisor có thể đọc và ghi được các volume mã hóa, set các key dưới đây để gọi về Vault endpoint.

```
[vault]
root_token_id = <token>
vault_url = http://10.237.123.210:8200
kv_mountpoint = cinder
```

Barbican là dịch vụ quản lý khóa Openstack (Symmetric Keys, Asymmetric Keys, Certificates). Nó cung cấp lưu trữ, quản lý dữ liệu bảo mật.

```
[barbican]
auth_endpoint = http://10.237.121.210:5000
barbican_endpoint_type = internal
```

## Neutron Agent

Sau khi chạy kolla ansible xong openvswitch\_agent sẽ được cấu hình như

```
[agent]
tunnel_types = vxlan
l2_population = true
arp_responder = true
 
[securitygroup]
firewall_driver = neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver
 
[ovs]
bridge_mappings = vlan:br-vlan
datapath_type = system
ovsdb_connection = tcp:127.0.0.1:6640
ovsdb_timeout = 10
local_ip = 10.237.123.4
```

## Monitoring

Đối với monitor hệ thống đang sử dụng monasca-agent\_collector để thu thập metric và sử dụng telegraf để forward metric về vmonitor.

Command để thực hiện cài đặt:

```
ansible-playbook -i inventory.ini mon.yaml -t step4
```

Để telegraf có thể gửi metric về vmonitor cần cấu hình thêm PLUGINS

```
[[outputs.vngcloud_vmonitor]]
  url = "https://{{ VMONITOR_SITE }}:443"
  insecure_skip_verify = false
  data_format = "vngcloud_vmonitor"
  timeout = "30s"
  http_proxy_url = "{{ http_proxy }}"
 
  client_id = "{{ IAM_CLIENT_ID }}"
  client_secret = "{{ IAM_CLIENT_SECRET }}"
  iam_url = "{{ IAM_URL }}"
```

\######

Để các node compute có thể kết nối được với cehp, trên các node compute cần phải có keyring của ceph

```
cat <<EOF> /etc/kolla/nova-compute/ceph.client.cinder.keyring
[client.cinder]
key = AQDR2T1maAcOOxAAZq6qcRzZnn+XxOmjcPNj4g==
EOF
 
cat <<EOF> /etc/kolla/nova-compute/ceph.conf 
[global]
fsid = 914558fc-0d1c-11ef-9945-65f3290d75db
mon_host = [v2:10.237.123.11:3300/0,v1:10.237.123.11:6789/0] [v2:10.237.123.12:3300/0,v1:10.237.123.12:6789/0] [v2:10.237.123.13:3300/0,v1:10.237.123.13:6789/0]
EOF
```

Để libvirt có thể kết nối được với ceph key:

```
docker exec -it nova_libvirt bash
 
cat <<EOF> /etc/libvirt/secrets/c6fef76a-8c3d-440f-9344-56d1a03c7f37.xml
<secret ephemeral='no' private='no'>
<uuid>c6fef76a-8c3d-440f-9344-56d1a03c7f37</uuid>
<usage type='ceph'>
<name>client.volumes secret</name>
</usage>
</secret>
EOF

virsh secret-define --file /etc/libvirt/secrets/c6fef76a-8c3d-440f-9344-56d1a03c7f37.xml
virsh secret-set-value --secret c6fef76a-8c3d-440f-9344-56d1a03c7f37 --base64 AQDR2T1maAcOOxAAZq6qcRzZnn+XxOmjcPNj4g==
```

Copy key ceph vào container:

```
docker cp /etc/kolla/nova-compute/ceph.conf nova_compute:/etc/ceph/ceph.conf
docker cp /etc/kolla/nova-compute/ceph.client.cinder.keyring nova_compute:/etc/ceph/ceph.client.cinder.keyring
docker exec -u root nova_compute chown -R nova. /etc/ceph
docker exec nova_compute ls -la /etc/ceph/ 
docker restart nova_compute
```

Thêm type br-vlan trên openvswitch\_agent

```
docker exec -u root -it neutron_openvswitch_agent bash
### network type vlan
ovs-vsctl add-br br-vlan
ovs-vsctl add-port br-vlan eno2
### Edit file: /etc/kolla/neutron-openvswitch-agent/openvswitch_agent.ini
[ovs]
bridge_mappings = vlan:br-vlan
```

## 3/ Kiểm tra sau khi cài đặt

Sau khi cài đặt các phần mềm, trên terminal openstack client có thể gõ lệnh để kiểm tra các compute:

```
openstack compute service list | grep nova-compute
```

<figure><img src="../../.gitbook/assets/image (829).png" alt=""><figcaption></figcaption></figure>

## 4/ Quản lý Compute

### Bật tắt compute:

Để ngăn chặn việc tạo vm vào 1 compute, sử dụng lệnh sau để disable compute:

```
openstack compute service set --disable <host> nova-compute
```

Để để cho phép việc tạo vm vào 1 compute, sử dụng lệnh sau để enable compute:

```
openstack compute service set --enable <host> nova-compute
```

### Nova aggregate

Nova aggregate (hostgroup) là tính năng cho phép tạo ra các hostgroup với cả nhu cầu khác nhau. Các aggregate sẽ chưa thông tin các compute. Khi một flavor được properties là với một hostgroup thì khi tạo server với flavor đó thì vm chỉ được tạo trên các compute đã được add vào aggregate trước đó.

Dùng lệnh để list các aggregate hiện có:

```
openstack aggregate list
```

Để add host vào aggregate

```
openstack aggregate add <compute_host> <aggregate_name> 
```

Để aggregate hoạt động trên flavor cần cấu hình thêm:

```
aggregate_instance_extra_specs:hostgroup=’aggregate_name’
```



