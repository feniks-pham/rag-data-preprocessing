# Kết nối tới RDS Instance

Để kết nối với RDS Instance có **Database Engine** là **MySQL** hay **Mariadb**, bạn có thể sử dụng bất kì công cụ MySQL Client nào như mysql-client (CLI Client của MySQL phát triển), MySQL Workbench (GUI client của MySQL phát triển), Heidi,…&#x20;

Tương tự, đối với **Postgresql**, bạn có thể dùng các client như: psql (ClI Client do PostgreSQL phát triển), pgAdmin (GUI Client phổ biến),...

Bạn có thể tham khảo video sau:

{% embed url="https://youtu.be/1kvJi3Hg4wM" %}

Hoặc tham khảo bài viết hướng dẫn dưới đây. Bài viết này VNG Cloud sử dụng mysql-client, MySQL Workbench và psql:

* [Bước 0. Cài đặt client tool để kết nối:](./#ketnoitoirdsinstance-buoc0.caidatclienttooldeketnoi)
* [Bước 1. Xác định thông tin Endpoint & Port để truy cập:](./#ketnoitoirdsinstance-buoc1.xacdinhthongtinendpoint-and-portdetruycap)
* [Bước 2: Tùy chỉnh Security Group Rules để bảo vệ DB Instance (tùy chọn)](./#ketnoitoirdsinstance-buoc2-tuychinhsecuritygrouprulesdebaovedbinstance-tuychon)
* [Bước 3. Kết nối bằng các client tools:](./#ketnoitoirdsinstance-buoc3.ketnoibangcacclienttools)

### Bước 0. Cài đặt client tool để kết nối: <a href="#ketnoitoirdsinstance-buoc0.caidatclienttooldeketnoi" id="ketnoitoirdsinstance-buoc0.caidatclienttooldeketnoi"></a>

Để cài đặt MySQL Workbench (Windows/Linux), bạn có thể download theo hướng dẫn của MySQL:

[https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)

Để cài đặt MySQL-Client (Linux), bạn có thể cài đặt nhanh bằng:

Ubuntu:

| `sudo apt-get install mysql-client` |
| ----------------------------------- |

CentOS:

| `sudo yum install mysql` |
| ------------------------ |

Để cài đặt Psql (Linux/MacOS), bạn cài đặt như sau:

Ubuntu:

| `sudo apt-get install postgresql-client` |
| ---------------------------------------- |

CentOS:

| `sudo yum install https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/pgdg-redhat10-10-2.noarch.rpm` `sudo yum install postgresql10` |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |

MacOS:

| `brew install libpq` |
| -------------------- |

### Bước 1. Xác định thông tin Endpoint & Port để truy cập: <a href="#ketnoitoirdsinstance-buoc1.xacdinhthongtinendpoint-and-portdetruycap" id="ketnoitoirdsinstance-buoc1.xacdinhthongtinendpoint-and-portdetruycap"></a>

Tại giao diện quản lý Database, bạn chọn vào RDS Instance vừa tạo, chọn đến tab **Connectivity & Security**, xem tại mục **Endpoint & Port**.

Để phân biệt **Public Endpoint** & **Private Endpoint**, bạn xem mục **Networking** để xác định **Private Network** **Subnet** của RDS Instance này.

VD: DB Instance có **Private Network Subnet** là 10.0.116.0/24 thì 10.0.116.3 sẽ là **Private Endpoint**.

### Bước 2: Tùy chỉnh Security Group Rules để bảo vệ DB Instance (tùy chọn) <a href="#ketnoitoirdsinstance-buoc2-tuychinhsecuritygrouprulesdebaovedbinstance-tuychon" id="ketnoitoirdsinstance-buoc2-tuychinhsecuritygrouprulesdebaovedbinstance-tuychon"></a>

Mục **Security Group Rules** cho phép bạn giới hạn những **Remote IP** nào được phép truy cập vào RDS Instance của bạn. Để tiện lợi cho việc sử dụng, khi vừa khởi tạo, VNG Cloud cho phép bạn truy cập không hạn chế từ mọi nơi (0.0.0.0/0) vào RDS Instance. Tuy nhiên, VNG Cloud khuyến nghị bạn tùy chỉnh lại mục này sao cho chỉ những **Remote IP** tin cậy được truy cập vào.

* Để thay đổi, bạn chọn vào **EDIT** và điền IP (theo chuẩn CIDR) thích hợp.
* Sau khi hiệu chỉnh, nhấn **Save** và chờ một lát để thay đổi được lưu lại.

Để chắc chắn kết nối được thông suốt, bạn có thể dùng các công cụ kiểm tra như telnet.

Khi kết nối đã thông suốt, bạn có thể tiến hành kết nối tới RDS Instance.

### Bước 3. Kết nối bằng các client tools: <a href="#ketnoitoirdsinstance-buoc3.ketnoibangcacclienttools" id="ketnoitoirdsinstance-buoc3.ketnoibangcacclienttools"></a>

Sau khi có thông tin endpoint, bạn sử dụng **Master User** vừa tạo để kết nối.

Lưu ý: Master user chỉ được tạo một lần duy nhất, nếu quên password, bạn có thể chọn **Action** > **Edit Database** để tự thay đổi password. Nếu quên thông tin Master User, bạn có thể liên hệ **VNG Cloud Support** để được hỗ trợ.

VD: RDS Instance vừa tạo có master user là: dba, endpoint truy cập là public endpoint: 61.28.224.201, port: 3306, bạn kết nối như sau:

* Trên **Linux** (**Ubuntu**, **CentOS**), bạn có thể dùng ngay luôn **mysqlclient** (thường được cài đặt sẵn trong hệ điều hành):

| `$ mysql -h 61.28.224.201` `-P 3306` `-u dba –p` `Password` `mysql>` |
| -------------------------------------------------------------------- |

* Trên **Windows/Linux/MacOS** bạn có thể tải **MySQL Workbench** tại: [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)

#### Workbench

Workbench là client tool của chính MySQL phát triển, có giao diện đồ họa trực quan, dễ sử dụng. Trên các máy Linux (Ubuntu, Centos) bạn cũng có thể sử dụng Workbench.

Sau khi tải & cài đặt Workbench, tại giao diện khởi động, bạn chọn **Database** > **Connect to Database** và điền các thông tin cần thiết như:

* Connection Name: đặt một tên dễ nhớ cho kết nối này để bạn dễ phân biệt.
* Hostname: IP Endpoint của vDB, ở đây là **61.28.244.201**
* Port: giữ nguyên mặc định 3306.
* Username: Master User của bạn, ở đây là **dba**

sau khi chắc chắn các thông tin đã chính xác, bạn nhấn **Test Connection.** Một hộp thoại hiện ra để yêu cầu bạn nhập mật khẩu truy cập, bạn có thể tick chọn **Save Password in vault** để Workbench lưu lại password cho phiên kết nối sau.

Lưu ý, nếu bạn sử dụng Workbench kết nối đến MariaDB hoặc MySQL version cũ, sẽ có cảnh báo không hoàn toàn tương thích như sau, bạn có thể bỏ qua và chọn **Continue Anyway**.

Đối với **Postgresql**, bạn dùng psql với cú pháp sau và nhập password đã đăng kí lúc khởi tạo vDB:

| `psql -h<Endpoint_vDB> -U<master_user> -W -d<Database_Name>` `Password:` |
| ------------------------------------------------------------------------ |

trong đó:

* Endpoint\_vDB: là endpoint kết nối tới vDB.
* Master\_user: là master user bạn đăng kí lúc khởi tạo.
* Database\_Name: là Database Name bạn điền vào ở phần DB Options. (khác với DB Instance Name ở mục DB Settting lúc khởi tạo và hiển thị ở mục Database trên Portal). Nếu quên, bạn có thể liên hệ VNG Cloud Support để lấy lại thông tin này.&#x20;

Nếu có vấn đề gì cần hỗ trợ, bạn có thể liên hệ **VNG Cloud Support Team** ngay. Cảm ơn bạn đã xem hết bài hướng dẫn.
