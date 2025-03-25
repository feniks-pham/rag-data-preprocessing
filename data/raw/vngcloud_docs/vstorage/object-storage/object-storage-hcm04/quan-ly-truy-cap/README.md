# Quản lý truy cập

Trên region HCM04, bạn có thể sử dụng 4 loại tài khoản để truy cập vào vStorage. Chi tiết 4 loại này bao gồm:

* **Root User Account:** Là tài khoản [khởi tạo đầu tiên](https://register.vngcloud.vn/signup) để truy cập vào VNG Cloud với đầy đủ quyền truy cập vào tất cả dịch vụ tài nguyên trên VNG Cloud.
* **IAM User Account, Service Account:** Là tài khoản được tạo ra từ tài khoản Root user account duy nhất với những quyền truy cập phụ thuộc vào chính sách cho phép truy cập được thiết lập từ Root user account.&#x20;

<figure><img src="../../../../.gitbook/assets/image (864).png" alt=""><figcaption></figcaption></figure>

* **S3 keys:** Là cặp s3 key có access key và secret key được vStorage tích hợp để có tính tương thích với các client tool của S3 như s3cmd, s3 SDK,...

Tham khảo bảng bên dưới để nắm được cách hoạt động tổng quan của các tài khoản trên vStorage:&#x20;

<table data-full-width="true"><thead><tr><th width="194">Loại tài khoản</th><th>Kênh truy cập</th><th>Nơi khởi tạo</th><th>Quyền hạn mặc định</th><th>Làm việc với project</th><th>Làm việc với bucket</th></tr></thead><tbody><tr><td>Root User Account</td><td>vStorage Portal</td><td>Khởi tạo lần đầu khi sử dụng dịch vụ trên VNG Cloud</td><td>Full quyền trên project và bucket</td><td>Có</td><td>Có</td></tr><tr><td>IAM User Account</td><td>vStorage Portal</td><td>IAM Portal</td><td>Chưa có quyền hạn truy cập vào bất kỳ tài nguyên nào</td><td>Có, phân quyền thông qua IAM Policy</td><td>Có, phân quyền thông qua Bucket Policy</td></tr><tr><td>Service Account</td><td>vStorage API</td><td>IAM Portal</td><td>Chưa có quyền hạn truy cập vào bất kỳ tài nguyên nào</td><td>Có, phân quyền thông qua IAM Policy</td><td>Có, phân quyền thông qua Bucket Policy</td></tr><tr><td>S3 keys</td><td>3rd party software</td><td>vStorage Portal</td><td>Tùy thuộc vào tài khoản khởi tạo</td><td>Không</td><td>Có, quyền hạn tùy thuộc vào loại user khởi tạo S3 key</td></tr></tbody></table>
