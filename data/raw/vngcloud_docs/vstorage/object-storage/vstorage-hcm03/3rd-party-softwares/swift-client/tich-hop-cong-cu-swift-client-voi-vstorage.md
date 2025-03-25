# Tích hợp công cụ Swift Client với vStorage

Để xem hướng dẫn tích hợp công cụ SwiftClient với vStorage, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn thư mục **Tích hợp.**
3. Chọn biểu tượng **Swift Client**.
4. Tại mục **Cấp quyền**, bạn cần điền thông tin cần thiết để cấu hình Swift Client của bạn nhằm tích hợp với vStorage bao gồm:
   1. Chọn một **Region** chứa project mà bạn muốn thực hiện truy xuất dữ liệu tới trong danh sách các Region mà chúng tôi cung cấp.
   2. Chọn một **Project** trong danh sách các project đang tồn tại trong Region mà bạn chọn trước đó. Nếu danh sách project hiển thị chưa đầy đủ, bạn có thể chọn ,chúng tôi sẽ tải lại danh sách project mới nhất tại thời điểm bạn thực hiện hành động này.
   3. Chọn một **Tên người dùng** trong danh sách các Swift user đang tồn tại thuộc project mà bạn chọn trước đó.
   4. Nhập **Mật khẩu** tương ứng của **Tên người dùng** mà bạn vừa chọn. Cặp Swift user và mật khẩu được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Nhấn vào đây để vào vIAM và quản lý Swift user](https://hcm-3.console.vngcloud.vn/iam/vstorage-credentials/swift) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý Swift user. Để biết thêm thông tin về Swift user, hãy xem tại [Khởi tạo Swift user](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-swift-user.md).
5. Sau khi hoàn tất chọn cấu hình **Cấp quyền**, chọn **Cấu hình Swift Client** để chuyển tới màn hình **Cấu hình**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Cấu hình Swift Client** để cập nhật cách sử dụng theo thông số mới của bạn. Bạn có thể xem hướng dẫn cách cài đặt, cấu hình Swift Client ngay trên màn hình này. Chi tiết tham khảo thêm tại: [Tích hợp vStorage.](https://vstorage.console.vngcloud.vn/integration/integration)

<figure><img src="../../../../../.gitbook/assets/Tich_hop_Swift_Client.gif" alt=""><figcaption></figcaption></figure>
