# Quản lý truy cập

### Quản lý tài khoản truy cập vMonitor Platform

Bạn có thể sử dụng 3 loại tài khoản để truy cập vào vMonitor Platform. Chi tiết 3 loại này bao gồm:

* **Root user account:** Là tài khoản [khởi tạo đầu tiên](https://register.vngcloud.vn/signup) để truy cập vào VNG Cloud với đầy đủ quyền truy cập vào tất cả dịch vụ tài nguyên trên VNG Cloud.
* **IAM user account (User account):** Là tài khoản được tạo ra từ tài khoản Root user account duy nhất với những quyền truy cập phụ thuộc vào chính sách cho phép truy cập được thiết lập từ Root user account.
* **Service account:** Tài khoản được sử dụng bởi 1 ứng dụng/máy, thực hiện các lệnh gọi API được ủy quyền và truy cập các tài nguyên được chỉ định trên VNG Cloud.

Trước khi có thể sử dụng 2 loại tài khoản **IAM user account** và **Service Account**, bạn cần thực hiện theo các bước:&#x20;

* Khởi tạo tài khoản IAM user account/ Service Account.
* Khởi tạo policy&#x20;
* Liên kết policy vào tài khoản IAM user account/ Service Account.

Chi tiết tham khảo tại: [IAM cho vMonitor](../identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/iam-cho-vmonitor.md).



***

### Tài nguyên vMonitor Platform được hỗ trợ phân quyền truy cập

Chúng tôi cung cấp cho bạn các loại tài nguyên được phép phân quyền truy cập bao gồm:

* alarm
* api-key
* api-test
* app
* archive
* certificate
* dashboard
* host
* location
* log2metric-metric
* log-project
* metric-unit-mapping-user
* notification
* parser-rule
* pipeline
* processor
* processor-group
* refill
* resources
* saved-query
* vas-host
* vbackup-host
* vdb-host
* vlb-host
* vlb-log-mapping
* vserver-host
* vMonitor Platform-host
* vMonitor Platform-log-mapping
* widget

***

### Quản lý truy cập tài nguyên vMonitor Platform

Sau khi thực hiện khởi tạo tài khoản truy cập vào vMonitor Platform theo hướng dẫn bên trên. Để truy cập vào tài nguyên( Metric quota, Log project,...) của bạn, bạn có thể sử dụng các tài khoản vMonitor Platform bao gồm tài khoản người dùng Root (Root User Account), tài khoản người dùng IAM (IAM User Account) và tài khoản Service Account để truy cập tài nguyên qua các giao diện người dùng (kênh truy cập): vMonitor Platform Portal, API, 3rd party softwares.&#x20;

Chi tiết tham khảo tại: [IAM cho vMonitor](../identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/iam-cho-vmonitor.md).
