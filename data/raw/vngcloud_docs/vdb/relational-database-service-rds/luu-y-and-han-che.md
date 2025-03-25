# Lưu ý & hạn chế

## A. Master User Privileges: <a href="#luuy-and-hanche-a.masteruserprivileges" id="luuy-and-hanche-a.masteruserprivileges"></a>

Đối với vDB dạng relational database, khi khởi tạo vDB, bạn được cấp một Master User để truy cập vào vDB.

Master User này sẽ được cấp các quyền sau:

* MySQL/MariaDB:
  * Global Privileges: ALTER ROUTINE, ALTER, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, CREATE, DELETE, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, REPLICATION CLIENT, REPLICATION SLAVE, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE.
  * Database Privileges: Full Privileges.

**Lưu ý**: database privileges ngoại trừ các database hệ thống như: mysql, information\_schema, performance\_schema, sys. Khi bạn tạo một database mới, hệ thống sẽ tự grant all privileges cho master user. Nếu chưa có, bạn vui lòng chờ trong giây lát hoặc liên hệ VNG Cloud Support.

* Postgresql: Createrole, CreateDB, Replication.

## B. Service Users/Roles: <a href="#luuy-and-hanche-b.serviceusers-roles" id="luuy-and-hanche-b.serviceusers-roles"></a>

Đối với vDB dạng relational database, hệ thống sẽ tạo sẵn các service users/roles để thực hiện các tác vụ tự động. Bạn vui lòng không xóa các user/role này để tránh các tính năng tự động bị lỗi.

* MySQL/MariaDB: \`os\_admin\`@\`127.0.0.1\`, \`root\`@\`localhost\`
* Postgresql: os\_admin, postgres

## C. Import Database: <a href="#luuy-and-hanche-c.importdatabase" id="luuy-and-hanche-c.importdatabase"></a>

Đối với các vDB dạng Relational, khi tiến hành backup source DB, bạn chỉ cần backup các database chứa dữ liệu, tránh backup all-databases (bao gồm các database hệ thống như mysql, sys, performance\_schema, information\_schema) hoặc các stored procedure có definer là quyền root. Nếu trong file dump tồn tại stored procedure có definer=root, bạn vui lòng replace bằng Master User đã khai báo lúc khởi tạo vDB. VD: sed -i 's/definer=root/definer=\<master\_user>/g' dump.sql

## D. Failover khi vDB role Master down: <a href="#luuy-and-hanche-d.failoverkhivdbrolemasterdown" id="luuy-and-hanche-d.failoverkhivdbrolemasterdown"></a>

Hiện tại, vDB sẽ không tự động failover khi có sự cố đối với vDB role Master (Read/Write) trong mô hình Master/Read-Replica. Quyền quyết định việc Promote Read Replica thành Master mới sẽ thuộc về Khách hàng. Bạn lưu ý sau khi Promote, quá trình đồng bộ dữ liệu với Master trước sẽ bị ngắt và không thể rollback được. Để khôi phục tính High Avaibility cho hệ thống, bạn có thể create read-replica mới từ Standalone vDB này.

Để thực hiện việc này, bạn có thể làm theo [hướng dẫn sau](https://docs.vngcloud.vn/pages/viewpage.action?pageId=31555997). Quá trình này sẽ bao gồm các bước sau:

1. Bạn chọn instance có role Replica và thao tác Promote to Standalone.
2. Bạn update connection\_string trong application của mình để Read/Write data vào Master mới.
3. Sau khi kiểm tra application đã ổn định, bạn chọn vào Master mới và tiến hành create read-replica từ Master mới này.
4. Bạn có thể xóa Master cũ nếu không còn nhu cầu sử dụng.

\
