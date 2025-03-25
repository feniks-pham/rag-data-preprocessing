# Bước 3: Kết nối 3rd party softwares với vStorage

Sau khi bạn đã thực hiện khởi tạo project và khởi tạo S3 key thành công, lúc này bạn có thể sử dụng các 3rd party softwares để kết nối và làm việc với project của bạn. Các công cụ 3rd party softwares bạn có thể lựa chọn sử dụng có thể là S3cmd, Cyberduck, Rclone, S3 Browser, MinIO Client,...Trong phạm vi tài liệu này, chúng tôi sẽ hướng dẫn bạn kết nối S3 Browser với vStorage. S3 Browser là công cụ được tối ưu hóa cho phép bạn chia sẻ và tải lên tệp tin của mình. Công cụ này có giao diện tương đối đơn giản, dễ sử dụng và đã tương thích với API của dịch vụ lưu trữ vStorage.&#x20;

Để tích hợp công cụ S3 Browser với vStorage, bạn có thể thực hiện theo hướng dẫn bên dưới:

1. Tải công cụ người dùng S3 Browser tại đây [https://s3browser.com/download.aspx](https://s3browser.com/download.aspx).
2. Mở ứng dụng **S3 Browser.** Chọn thư mục **Account, sau đó chọn Add new account**

<figure><img src="../../../../.gitbook/assets/image (585).png" alt="" width="443"><figcaption></figcaption></figure>



3. Màn hình Add New Account hiển thị, lúc này bạn nhập các thông tin như sau:

* **Display name:** Tên hiển thị của account. Ví dụ: Demo\_HCM04
* **Account type**: Chọn **S3 Compatible Storage.**
* **REST Endpoint**: Đường dẫn đến vstorage, đối với Region HCM04 thì đường dẫn là [hcm04.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/)
* **Access Key ID & Secret Access Key:** Là cặp S3 key bạn đã thực hiện generate tại bước 2 trước đó.

4. Chọn option **Use Secure transfer (SSL/TLS)** vì vStorage chỉ hỗ trợ kênh truyền đã được mã hoá (HTTPS, port 443) để đảm bảo an toàn dữ liệu, vStorage hiện tại không hỗ trợ kênh truyền không mã hoá (HTTP, port 80).
5. Chọn **Add new account.**

<figure><img src="../../../../.gitbook/assets/image (587).png" alt=""><figcaption></figcaption></figure>

6. Khi kết nối thành công, màn hình S3 Browser sẽ hiển thị như sau:&#x20;

<figure><img src="../../../../.gitbook/assets/image (588).png" alt=""><figcaption></figcaption></figure>
