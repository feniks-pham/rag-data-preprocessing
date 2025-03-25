# Tích hợp công cụ Rclone với vStorage

Để xem hướng dẫn tích hợp công cụ Rclone với vStorage, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn thư mục **Integration.**
3. Chọn biểu tượng **Rclone**.
4. Tại mục **Authentication**, bạn cần điền thông tin cần thiết để cấu hình Rclone của bạn nhằm tích hợp với vStorage bao gồm:
   1. Chọn một **Project** trong danh sách các project đang tồn tại trong Region mà bạn chọn trước đó. Nếu danh sách project hiển thị chưa đầy đủ, bạn có thể chọn , chúng tôi sẽ tải lại danh sách project mới nhất tại thời điểm bạn thực hiện hành động này.
   2. Chọn một **Access key** trong danh sách các access key đang tồn tại thuộc project mà bạn chọn trước đó.
   3. Nhập **Secret key** tương ứng của **Access key** vừa chọn. Cặp access key và secret key được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Nhấn vào đây để vào vIAM và quản lý s3 keys](https://hcm-3.console.vngcloud.vn/iam/vstorage-credentials/s3) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý S3 keys. Để biết thêm thông tin về S3 keys, hãy xem tại [Khởi tạo vStorage Credentials](../../../vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/).
5. Sau khi hoàn tất chọn cấu hình **Authentication**, chọn **Confirm Rclone** để chuyển tới màn hình **Configuration**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Cấu hình Rclone** để cập nhật cách sử dụng theo thông số mới của bạn. Bạn có thể xem hướng dẫn cách cài đặt, cấu hình Rclone ngay trên màn hình này.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (866).png" alt=""><figcaption></figcaption></figure>
