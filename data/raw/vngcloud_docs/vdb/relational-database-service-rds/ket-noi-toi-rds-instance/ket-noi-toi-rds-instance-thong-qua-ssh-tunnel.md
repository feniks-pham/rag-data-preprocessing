# Kết nối tới RDS Instance thông qua SSH Tunnel

Để kết nối với RDS Instance bạn có thể sử dụng **Public Endpoint** (thông qua Internet). Tuy nhiên, cách này tìm ẩn rủi ro về an toàn thông tin. Để tăng cuờng bảo mật, bạn có thể tạo RDS Instance chỉ cho phép kết nối tới Private Endpoint, sau đó truy cập thông qua một vServer chung mạng với RDS Instance này và có Public IP (vServer đóng vai trò Terminal trung gian).

* [Bước 1. Xác định thông tin Endpoint & Port để truy cập: ](ket-noi-toi-rds-instance-thong-qua-ssh-tunnel.md#ketnoitoirdsinstancethongquasshtunnel-buoc1.xacdinhthongtinendpoint-and-portdetruycap)
* [Bước 2: Tùy chỉnh Security Group Rules chỉ cho phép truy cập từ nội bộ VPC:](ket-noi-toi-rds-instance-thong-qua-ssh-tunnel.md#ketnoitoirdsinstancethongquasshtunnel-buoc2-tuychinhsecuritygroupruleschichopheptruycaptunoibovpc)
* [Bước 3: Cấu hình SSH Tunnel: ](ket-noi-toi-rds-instance-thong-qua-ssh-tunnel.md#ketnoitoirdsinstancethongquasshtunnel-buoc3-cauhinhsshtunnel)

### Bước 1. Xác định thông tin Endpoint & Port để truy cập:  <a href="#ketnoitoirdsinstancethongquasshtunnel-buoc1.xacdinhthongtinendpoint-and-portdetruycap" id="ketnoitoirdsinstancethongquasshtunnel-buoc1.xacdinhthongtinendpoint-and-portdetruycap"></a>

Tại giao diện quản lý Database, bạn chọn vào RDS Instance muốn kết nối, chọn đến tab **Connectivity & Security**, xem tại mục **Endpoint & Port**.&#x20;

VD: RDS Instance có 2 endpoint như sau:

* Private (trong nội bộ VPC): 10.0.116.3
* Public (có thể kết nối tới thông qua Internet): 61.28.233.82

Để phân biệt **Public Endpoint** & **Private Endpoint**, bạn xem mục **Networking** để xác định **Network Subnet** của RDS Instance này.&#x20;

VD: RDS Instance trên có **Network Subnet** là 10.0.116.0/24 nên 10.0.116.3 sẽ là **Private Endpoint**.&#x20;

### Bước 2: Tùy chỉnh Security Group Rules chỉ cho phép truy cập từ nội bộ VPC: <a href="#ketnoitoirdsinstancethongquasshtunnel-buoc2-tuychinhsecuritygroupruleschichopheptruycaptunoibovpc" id="ketnoitoirdsinstancethongquasshtunnel-buoc2-tuychinhsecuritygroupruleschichopheptruycaptunoibovpc"></a>

Mục **Security Group Rules** cho phép bạn giới hạn những **Remote IP** nào được phép truy cập vào RDS Instance của bạn. Ở truờng hợp này, bạn có thể cấu hình lại **Remote IP Prefix** là **Network Subnet** của VPC này để chỉ những vServer hoặc vDB chung VPC mới có thể truy cập được.&#x20;

Sau khi hiệu chỉnh, nhấn **Save** và chờ một lát để thay đổi được lưu lại.

Để chắc chắn kết nối được thông suốt, bạn có thể truy cập vào vServer Terminal trên và dùng các công cụ kiểm tra như telnet để kiểm tra kết nối tới port của RDS Instance.

VD: từ vServer terminal, bạn gõ lệnh sau để kiểm tra kết nối từ vServer tới vDB (ví dụ port = 3306):&#x20;

| `$ telnet 10.0.116.3` `3306` |
| ---------------------------- |

Khi kết nối đã thông, bạn có thể tiến hành kết nối tới RDS Instance.

### Bước 3: Cấu hình SSH Tunnel:  <a href="#ketnoitoirdsinstancethongquasshtunnel-buoc3-cauhinhsshtunnel" id="ketnoitoirdsinstancethongquasshtunnel-buoc3-cauhinhsshtunnel"></a>

Nếu bạn dùng một Client tool **có hỗ trợ kết nối thông qua SSH Tunnel** như **MySQL Workbench**, bạn có thể bỏ qua đoạn sau và đến phần cấu hình trong **MySQL Workbench**.

Nếu sử dụng một client tool **không hỗ trợ cấu hình** **SSH Tunnel** (VD như **mysqlclient**), bạn phải cấu hình tay như sau.&#x20;

Tại thiết bị của mình, bạn thiết lập SSH Tunnel bằng câu lệnh sau:&#x20;

| `ssh -N -L localhost_port:private_endpoint:3306` `ssh_user@vServer_IP` `-p vServer_ssh_port &` |
| ---------------------------------------------------------------------------------------------- |

với:&#x20;

* **Localhost\_port**: Port tại Localhost (thiết bị của bạn).&#x20;
* **Private\_endpoint**: Private Endpoint RDS Instance của bạn&#x20;
* **SSH\_user**: user để bạn ssh đến vServer đóng vai trò terminal&#x20;
* **vServer\_iP:**  IP của vServer đóng vai trò terminal.&#x20;
* **vServer\_ssh\_port**: port ssh của vServer đóng vai trò terminal.&#x20;
* **&**: dấu & để chỉ định process ssh tunnel này sẽ chạy ngầm (background), nếu không có, process này sẽ chiếm dụng terminal hiện tại, bạn cần mở terminal khác trước khi tiếp tục đến bước truy cập.

Ngoài ra nếu bạn dùng chứng thực bằng **Public key** thì có thể thêm cờ **-i** và kèm đuờng dẫn đến **Private key** của bạn.  Sau khi cấu hình thành công, bạn sử dụng Master User vừa tạo để kết nối.&#x20;

VD: RDS Instance vừa tạo có **Master user**: dba, **Private Endpoint**: 10.0.116.3. Terminal vServer có **IP**: 61.28.224.201. **Port SSH**: 234, **User SSH**: stackops, đường dẫn Private Key (tại Localhost thiết bị của bạn) là \~/.ssh/id\_rsa. **Localhost Port** bạn chọn là: 3306.&#x20;

Bạn cấu hình **SSH Tunnel** bằng lệnh:&#x20;

| `ssh -N -L 3306:10.0.116.3:3306` `stackops@61.28.224.201` `-p 234` `-i ~/.ssh/id_rsa &` |
| --------------------------------------------------------------------------------------- |

Sau đó, bạn có thể sử dụng **Master User** dba để kết nối thông qua **mysqlclient** như sau:&#x20;

| `$ mysql -h 127.0.0.1` `-P 3306` `-u dba -p` `Password` `mysql>` |
| ---------------------------------------------------------------- |

Nếu sử dụng một client tool **có hỗ trợ SSH Tunnel** như **Workbench**, bạn có thể cấu hình ngay bên trong giao diện của tool.

VD: với **Workbench**, bạn có thể chọn **Connection Method** là **Standard TCP/IP over SSH** như sau:

* **SSH Hostname**: bạn nhập **IP:SSH\_Port**, ví dụ như ở đây là **61.28.224.201**, port **234**. Nếu không cấu hình thêm Port, mặc định sẽ nhận Port 22.
* **SSH Username**: username để bạn ssh, ở đây là **stackops**.
* **SSH Password, SSH Key File**: tùy vào thiết lập SSH của bạn mà bạn có thể chọn đường dẫn đến SSH Public key hoặc chọn nhập Password.
* **MySQL Hostname, Port, Username, Password**: tương tự như bài hướng dẫn trước, bạn có thể xem lại tại: [Kết nối tới RDS Instance](./)

sau đó bạn nhấn **Test Connection**.

Chúc bạn thành công. Nếu có vấn đề gì cần hỗ trợ, bạn vui lòng liên hệ **VNG Cloud Support Team**.
