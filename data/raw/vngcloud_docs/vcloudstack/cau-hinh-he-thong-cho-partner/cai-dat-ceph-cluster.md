# Cài đặt Ceph Cluster

Bước  1: Cần cái Cài đặt các chương trình tiên quyết:

* Python 3
* Systemd
* Podman or Docker for running containers
* Time synchronization (such as Chrony or the legacy ntpd)
* LVM2 for provisioning storage devices

Step2: Install Cephadm

·         In Ubuntu:

_apt install -y cephadm_\
\


·         In CentOS Stream:

_dnf search release-ceph_\
&#xNAN;_&#x64;nf install --assumeyes centos-release-ceph-quincy_\
&#xNAN;_&#x64;nf install --assumeyes cephadm_

Step3: Create cephadmin user, pull ceph component images

useradd -m cephadmin

ssh-keygen -t rsa -b 4096 -C "cephadm@yourhostname"

docker pull quay.io/ceph/ceph:v17

docker pull quay.io/prometheus/node-exporter:v1.5.0

&#x20;

Step4: Running the bootstrap Command (running on admin node)

cephadm --image quay.io/ceph/ceph:v17 bootstrap \\\
&#x20;\--cluster-network 10.237.123.0/24 \\\
&#x20;\--mon-ip 10.237.123.11 \\\
&#x20;\--ssh-user cephadmin \\\
&#x20;\--ssh-private-key /home/cephadmin/.ssh/id\_rsa \\\
&#x20;\--ssh-public-key /home/cephadmin/.ssh/authorized\_keys \\\
&#x20;\--initial-dashboard-user admin \\\
&#x20;\--initial-dashboard-password "admin@storage" --skip-pull

&#x20;

Step5: Enable CEPH CLI

apt install ceph-common

Confirm that the ceph command is accessible with:

_ceph -v_\
\


Confirm that the ceph command can connect to the cluster and also its status with:

_ceph status_

&#x20;

Step6: Adding host

&#x20;

ceph orch host add lab-vcloudstack-cehp012 10.237.123.12 mon mgr osd\
ceph orch host add lab-vcloudstack-cehp013 10.237.123.13 mon mgr osd

&#x20;

Step7: Adding OSD

·         Print a list of devices discovered by cephadm, run command:

ceph orch device ls

·         Check hardware support libstoragemgmt:

cephadm shell lsmcli ldl

&#x20;

![](file:///C:/Users/LAP14997-local/AppData/Local/Packages/oice_16_974fa576_32c1d314_195d/AC/Temp/msohtmlclip1/01/clip_image002.png)

&#x20;

·         Check disk rotation (SSD: rotate =0, HDD: rotate =1)\
&#x20;           _lsblk -o name,rota_

&#x20;

![](file:///C:/Users/LAP14997-local/AppData/Local/Packages/oice_16_974fa576_32c1d314_195d/AC/Temp/msohtmlclip1/01/clip_image004.png)

·         Apply osd spec

_ceph orch apply -i osd\_spec.yaml_

&#x20;

![](file:///C:/Users/LAP14997-local/AppData/Local/Packages/oice_16_974fa576_32c1d314_195d/AC/Temp/msohtmlclip1/01/clip_image005.png)

&#x20;

·         Add available device to cluster:

_ceph orch apply osd --all-available-devices_

&#x20;

Step8: Create and Configure Crush RULE

·         Create crush rule

_ceph osd crush add-bucket ssd-01 root_

_ceph osd crush add-bucket ssd-02 root_

_ceph osd crush move lab-vcloudstack-cehp013 root=ssd-01_

_ceph osd crush move lab-vcloudstack-cehp012 root=ssd-01_

&#x20;
