# Cấu hình Replication với RDS (MySQL/Mariadb)

Để dữ liệu giữa MySQL server và RDS Instance đồng bộ hoàn toàn với nhau, bạn có thể cấu hình MySQL Replication. Lúc này, MySQL server của bạn sẽ đóng vai trò **Master**, RDS Instance sẽ đóng vai trò **Slave Read-Only**. Sau khi cấu hình thành công, mọi sự thay đổi trên MySQL server của bạn sẽ được đồng bộ trên RDS Instance thông qua cơ chế **Mysql Asynchronous Replication**.

* [1. Tạo Replication User trên MySQL server của bạn:](cau-hinh-replication-voi-rds-mysql-mariadb.md#cauhinhreplicationvoirds-mysql-mariadb-1.taoreplicationusertrenmysqlservercuaban)
* [2. Kiểm tra trạng thái Binary Log trên DB Server của bạn:](cau-hinh-replication-voi-rds-mysql-mariadb.md#cauhinhreplicationvoirds-mysql-mariadb-2.kiemtratrangthaibinarylogtrendbservercuaban)
* [3. Dump dữ liệu từ MySQL server của bạn và Import dữ liệu vào RDS Instance:](cau-hinh-replication-voi-rds-mysql-mariadb.md#cauhinhreplicationvoirds-mysql-mariadb-3.dumpdulieutumysqlservercuabanvaimportdulieuvaordsinstance)
* [4. Ghi nhận Binary Log File và Position trên MySQL server:](cau-hinh-replication-voi-rds-mysql-mariadb.md#cauhinhreplicationvoirds-mysql-mariadb-4.ghinhanbinarylogfilevapositiontrenmysqlserver)
* [5. Cấu hình Replication trên RDS Instance:](cau-hinh-replication-voi-rds-mysql-mariadb.md#cauhinhreplicationvoirds-mysql-mariadb-5.cauhinhreplicationtrenrdsinstance)

\


### **1. Tạo Replication User trên MySQL server của bạn:** <a href="#cauhinhreplicationvoirds-mysql-mariadb-1.taoreplicationusertrenmysqlservercuaban" id="cauhinhreplicationvoirds-mysql-mariadb-1.taoreplicationusertrenmysqlservercuaban"></a>

Trên MySQL server của bạn, bạn khởi tạo một user để thực hiện Replication như sau:

VD: bạn tạo user 'rep'@'%' với password 'abcd1234' và gán Global Privileges là Replication Slave.

| `mysql> create user 'rep'@'%'` `identified by 'abcd1234';` `mysql> grant replication slave on *.* to 'rep'@'%';` `mysql> flush privileges;` |
| ------------------------------------------------------------------------------------------------------------------------------------------- |



### **2. Kiểm tra trạng thái Binary Log trên DB Server của bạn:** <a href="#cauhinhreplicationvoirds-mysql-mariadb-2.kiemtratrangthaibinarylogtrendbservercuaban" id="cauhinhreplicationvoirds-mysql-mariadb-2.kiemtratrangthaibinarylogtrendbservercuaban"></a>

Để cấu hình Replication, bạn cần **enable binary log** trên MySQL server của bạn.

Để kiểm tra xem MySQL server của bạn đã bật binary log hay chưa, bạn có thể sử dụng câu lệnh sau:

| `mysql> show variables like "log_bin";` |
| --------------------------------------- |

<figure><img src="https://docs.vngcloud.vn/download/attachments/10880120/Screenshot%20from%202019-11-08%2011-15-34.png?version=3&#x26;modificationDate=1573186809000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Nếu kết quả là **OFF**, bạn có thể bật **binary log** bằng cách thêm trong file cấu hình **my.cnf (**&#x111;uờng dẫn mặc định thuờng là **/etc/mysql/my.cnf)** các giá trị sau:

| `[mysqld]` `log-bin=bin.log` `log-bin-index=bin-log.index` `max_binlog_size=100M` `binlog_format=row` |
| ----------------------------------------------------------------------------------------------------- |

\


Sau đó, bạn cần restart lại dịch vụ MySQL/Mariadb.

Đối với Ubuntu, bạn có thể sử dụng lệnh:

| `systemctl restart mysql` |
| ------------------------- |

\


Kiểm tra lại bằng cách chạy lại câu lệnh trên:

| `mysql> show variables like "log_bin";` |
| --------------------------------------- |

Nếu kết quả là **ON**, chúc mừng bạn đã cấu hình Binary Log thành công.

\


### **3. Dump dữ liệu từ MySQL server của bạn và Import dữ liệu vào RDS Instance:** <a href="#cauhinhreplicationvoirds-mysql-mariadb-3.dumpdulieutumysqlservercuabanvaimportdulieuvaordsinstance" id="cauhinhreplicationvoirds-mysql-mariadb-3.dumpdulieutumysqlservercuabanvaimportdulieuvaordsinstance"></a>

Bạn có thể tham khảo hướng dẫn [Import dữ liệu vào RDS Instance datastore MySQL/Mariadb bằng MySQLDump](import-du-lieu-vao-rds-instance-mysql-mariadb-bang-mysqldump.md).

\


### **4. Ghi nhận Binary Log File và Position trên MySQL server:** <a href="#cauhinhreplicationvoirds-mysql-mariadb-4.ghinhanbinarylogfilevapositiontrenmysqlserver" id="cauhinhreplicationvoirds-mysql-mariadb-4.ghinhanbinarylogfilevapositiontrenmysqlserver"></a>

Trên MySQL server của bạn, bạn sử dụng lệnh sau để kiểm tra trạng thái Master:

| `mysql> show master status;` |
| ---------------------------- |

Kết quả:

<figure><img src="https://docs.vngcloud.vn/download/attachments/10880120/Screenshot%20from%202019-11-08%2011-16-05.png?version=1&#x26;modificationDate=1573186810000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Bạn ghi nhận giá trị **File** và **Postion** của bin\_log trên MySQL server của bạn để chuyển sang bước tiếp theo.



### **5. Cấu hình Replication trên RDS Instance:** <a href="#cauhinhreplicationvoirds-mysql-mariadb-5.cauhinhreplicationtrenrdsinstance" id="cauhinhreplicationvoirds-mysql-mariadb-5.cauhinhreplicationtrenrdsinstance"></a>

Trên RDS Instance, bạn đăng nhập bằng Master User.

Bạn gọi Stored Procedure **mysql.vdbaas\_changeMasterHost** với cú pháp:

| `mysql> call mysql.vdbaas_changeMasterHost('<Host>','<Replication User>','<Replication User Password>','<Binary Log File>',<Position>);` |
| ---------------------------------------------------------------------------------------------------------------------------------------- |

VD: MySQL server của bạn có thông tin như sau:

* **Host**: 18.139.18.\*
* **User**: dba
* **Password**: password
* **Bin\_log** **File**: mysql-bin-changelog.000054
* **Position**: 154

thì bạn sẽ có câu lệnh sau:

| `mysql> call mysql.vdbaas_changeMasterHost('18.139.18.*','dba','password','mysql-bin-changelog.000059',511);` |
| ------------------------------------------------------------------------------------------------------------- |

\


Để bắt đầu quá trình Replication, bạn gọi Stored Procedure **mysql.vdbaas\_startSlave**:

| `mysql> call mysql.vdbaas_startSlave();` |
| ---------------------------------------- |

\


Để kiểm tra kết quả, bạn gõ lệnh:

| `mysql> show slave status\G;` |
| ----------------------------- |

<figure><img src="https://docs.vngcloud.vn/download/attachments/10880120/Screenshot%20from%202019-11-08%2011-16-18.png?version=1&#x26;modificationDate=1573186810000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Bạn chú ý các truờng: **Seconds\_Behind\_Master** và **Slave\_SQL\_Running\_State**.

Nếu **Slave\_SQL\_Running\_State** có giá trị **Slave has read all relay log; waiting for more updates** và **Seconds\_Behind\_Master** là **0** có nghĩa là hai bên đều đã đồng bộ thành công.

Từ bậy giờ, bạn có thể tắt đồng bộ và sử dụng RDS Instance là MySQL server chính bằng lệnh:

| `mysql> call mysql.vdbaas_stopSlave();` |
| --------------------------------------- |

hoặc giữ nguyên và sử dụng RDS Instance như là một **Replication Slave.**

\
