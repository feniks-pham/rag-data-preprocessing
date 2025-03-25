# Khởi tạo Juniper vSRX

Để khởi tạo, bạn vào vMarketPlace theo đường dẫn sau: [https://marketplace.console.vngcloud.vn/app-package/detail/4/30/1284a184-2119-4950-bd1c-af9161c52c01](https://marketplace.console.vngcloud.vn/app-package/detail/4/30/1284a184-2119-4950-bd1c-af9161c52c01)

## Khởi tạo Juniper vSRX

* Bạn chọn **Launch on Compute Engine.**
* Nhập tên, loại image là vSRX, cấu hình VM (Flavor, Storage), chỉ định chính xác VPC & Subnet sẽ gắn với vSRX Instance này.

Lưu ý: các resource (vServer, vLB, vDB) trong Subnet muốn route traffic qua vSRX Instance cần add route với gateway qua Internal IP của vSRX Instance này.

* Sau khi lựa chọn thông tin thích hợp, bạn chọn **Next**.
* Check lại các thông tin và chọn **CREATE SERVER**.
* Sau khi tạo xong (Status ACTIVE), bạn chọn vào Instance để xem thông tin IP kết nối.

## Update Security Group

Mặc định vSRX Instance tạo ra chưa được gắn Security Group, làm theo hướng dẫn bên dưới để cập nhật:

* Truy cập vào server instance vừa khởi tạo.
* Tiếp theo, bạn chọn  ACTION > Update Security và chọn New security group thích hợp.
  * Bạn có thể Allow all INBOUND & OUTBOUND từ 0.0.0.0/0 để setup ban đầu và siết lại IP WhiteList thích hợp.
  * Bạn lưu ý là cũng cần check lại **Network ACL** (trong mục VPC) để cấu hình cho đồng bộ với Security group này.

**Tiếp theo bạn cần tiến hành setup ban đầu cho vSRX instance.**

* Bạn chọn **ACTION** > **Console** để mở console của instance.

Mặc định khi khởi tạo, instance chưa được setup root password & cấu hình interface, ip, route, security zone & security polices.  Bạn cần cấu hình các thông tin này.

Để setup password root, bạn vào console, đăng nhập bằng user root và cấu hình như sau.

```
#mở mode sử dùng cli.
cli
#vào mode config
configure
#cấu hình password root dạng plain-text-password
set system root-authentication plain-text-password
New password: your-super-password 
Retype new password: your-super-password 

#kiểm tra tính hợp lệ
commit check
configuration check succeeds

#commit cấu hình
commit
commit complete
```

Để cấu hình Interface & nhận IP Address, bạn cấu hình như sau:

Trong đó,

```
#ge-0/0/0.0 và ge-0/0/1.0 lần luợt là interface external (ra Internet) và internal của vsrx instance.
set interfaces ge-0/0/0 unit 0 family inet dhcp-client
set interfaces ge-0/0/1 unit 0 family inet dhcp-client

# Allow all traffic ban đầu để cấu hình, sau đó sẽ WhiteList IP/Application thích hợp.
set security zones security-zone untrust interfaces ge-0/0/0.0
set security zones security-zone untrust interfaces ge-0/0/0.0 host-inbound-traffic system-services all
set security zones security-zone untrust interfaces ge-0/0/0.0 host-inbound-traffic protocols all

# Allow all traffic ban đầu để cấu hình, sau đó sẽ WhiteList IP/Application thích hợp.
set security zones security-zone trust interfaces ge-0/0/1.0
set security zones security-zone trust interfaces ge-0/0/1.0 host-inbound-traffic system-services all
set security zones security-zone trust interfaces ge-0/0/1.0 host-inbound-traffic protocols all

# Allow all traffic ban đầu để cấu hình, sau đó sẽ WhiteList IP/Application thích hợp.
set security policies from-zone untrust to-zone trust policy default-permit match source-address any
set security policies from-zone untrust to-zone trust policy default-permit match destination-address any
set security policies from-zone untrust to-zone trust policy default-permit match application any
set security policies from-zone untrust to-zone trust policy default-permit then permit 

# Commit config.
commit check
commit
```

Sau khi cấu hình, bạn cần reboot lại instance này.

```
#thoát khỏi mode config

exit

#reboot

request system reboot
```

Quá trình reboot có thể mất từ 10-15'.

Sau khi reboot, tại console, bạn đăng nhập bằng user root và password vừa cấu hình ở trên.

```
cli

show route
```

bạn ghi nhận Gateway ra Internet của vSRX Instance này tại 0.0.0.0/0&#x20;

VD:

```
show route

inet.0: 10 destinations, 13 routes (10 active, 0 holddown, 0 hidden)
+ = Active Route, - = Last Active, * = Both

0.0.0.0/0 *[Access-internal/12] 2d 16:49:10
> to 10.0.10.1 via ge-0/0/1.0
[Access-internal/12] 2d 16:49:10
> to 61.28.239.193 via ge-0/0/0.0
10.0.10.0/24 *[Direct/0] 2d 16:49:11
> via ge-0/0/1.0
10.0.10.9/32 *[Local/0] 2d 16:49:11
Local via ge-0/0/1.0
61.28.239.192/26 *[Direct/0] 2d 16:49:12
> via ge-0/0/0.0
61.28.239.211/32 *[Local/0] 2d 16:49:12
Local via ge-0/0/0.0
```

với instance này thì gateway là 61.28.239.193.

Bạn cấu hình route ra internet như sau.

```
cli

configure

set routing-options static route 0.0.0.0/0 next-hop 61.28.239.193

commit check

commit
```

Sau bước này, bạn có thể ssh vào instance từ Internet (qua Public IP) hoặc Internal IP từ vServer bằng user root, port 22 và password cấu hình ở trên.

Ngoài ra, bạn có thể cấu hình ssh bằng public key bằng lệnh

| `set system root-authentication ssh-rsa "ssh-rsa XXXRSA-KEYXXXXX”` |
| ------------------------------------------------------------------ |

\
\
