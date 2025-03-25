# Import dữ liệu vào RDS Instance (MySQL/Mariadb) bằng MySQLDump

Để nạp dữ liệu (import) vào RDS Instance với datastore MySQL/Mariadb, bạn có thể sử dụng công cụ **mysqldump**.

Bạn có thể tự thực hiện thông qua các bước sau:

* [1. Dump dữ liệu từ MySQL server của bạn:](import-du-lieu-vao-rds-instance-mysql-mariadb-bang-mysqldump.md#importdulieuvaordsinstance-mysql-mariadb-bangmysqldump-1.dumpdulieutumysqlservercuaban)
* [2. Import dữ liệu vào RDS Instance.](import-du-lieu-vao-rds-instance-mysql-mariadb-bang-mysqldump.md#importdulieuvaordsinstance-mysql-mariadb-bangmysqldump-2.importdulieuvaordsinstance)

### 1. Dump dữ liệu từ MySQL server của bạn: <a href="#importdulieuvaordsinstance-mysql-mariadb-bangmysqldump-1.dumpdulieutumysqlservercuaban" id="importdulieuvaordsinstance-mysql-mariadb-bangmysqldump-1.dumpdulieutumysqlservercuaban"></a>

Trên MySQL server của bạn, bạn có thể lấy danh sách database mình hiện có bằng lệnh sau:

| `mysql> show databases;` |
| ------------------------ |

<figure><img src="https://docs.vngcloud.vn/download/thumbnails/10880027/Screenshot%20from%202019-10-30%2017-44-08.png?version=2&#x26;modificationDate=1572432342000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


\
Xác định các database cần import ví dụ như trong hình là: _mysql02, mysql03, mysql04_.

**Lưu ý:** RDS Instance không hỗ trợ import các database hệ thống như: **mysql, performance\_schema, information\_schema và sys**. Bạn vui lòng bỏ qua các database này.

Sau khi đã có danh sách các database cần chuyển, bạn có thể dump dữ liệu bằng mysqldump với format tham khảo sau:

| `mysqldump -h<Local_DB_IP> -P<Local_DB_Port> -u<Local_DB_User> -p \--single-transaction \--routines --triggers \--databases <Your_DB_List >> dump-database.sql` |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- |

trong đó:&#x20;

* Local\_DB\_IP: IP MySQL Server của bạn.
* Local\_DB\_Port: Port MYSQL Server của bạn
* Local\_DB\_User: User trên MySQL Server của bạn.
* Your\_DB\_LIst: danh sách các database bạn muốn dump cách nhau bởi dấu khoảng trắng. VD: _mysql02, mysql03, mysql04_

Kết quả bạn sẽ có một file **dump-database.sql** chứa dữ liệu sẽ import.

### 2. Import dữ liệu vào RDS Instance. <a href="#importdulieuvaordsinstance-mysql-mariadb-bangmysqldump-2.importdulieuvaordsinstance" id="importdulieuvaordsinstance-mysql-mariadb-bangmysqldump-2.importdulieuvaordsinstance"></a>

Để thực hiện import, bạn sử dụng Master User được cấp khi khởi tạo RDS Instance.

Bạn có thể dùng lệnh:

| `mysql -h<RDS Instance_IP> -P3306 -u<RDS Instance_Master_User> -p < dump-database.sql` |
| -------------------------------------------------------------------------------------- |

với:&#x20;

* RDS Instance\_IP: IP của RDS Instance
* RDS Instance\_Master\_User: Master User được cấp khi khởi tạo RDS Instance.\
  \


Tùy vào lượng dữ liệu của bạn mà thời gian import có thể kéo dài hay không.&#x20;

Trên đây là hướng dẫn Import dữ liệu vào RDS Instance datastore MySQL/Mariadb. Chúc bạn thực hiện thành công.

\
