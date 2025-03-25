# Tự Động Redirect Từ HTTP Sang HTTPS

## Tổng quan

Tính năng **Tự động Redirect từ HTTP sang HTTPS** là một giải pháp bảo mật và tối ưu trải nghiệm người dùng, cho phép tự động chuyển đổi các yêu cầu HTTP sang HTTPS khi người dùng kết nối với website thông qua giao thức không an toàn HTTP. Tính năng này đảm bảo rằng toàn bộ lưu lượng truy cập đều được mã hóa và tuân thủ các tiêu chuẩn bảo mật hiện đại.

## Chi tiết

Khi khởi tạo một Web Accelerator, bạn có thể cấu hình tự động Redirect từ HTTP qua HTTPS thông qua:

<figure><img src="../../.gitbook/assets/image (17) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Trong đó:&#x20;

* **Always Use HTTPS:** Khi bật tùy chọn này, end-user truy cập vào website với giao thức HTTP sẽ được tự động chuyển hướng qua HTTPS.
* **Automatic HTTPS Rewrites**: Hỗ trợ đổi các link HTTP sang HTTPS trong source cod&#x65;**:** Hệ thống sẽ tự động nhận diện các nguồn http trong source code để chuyển thành HTTPS trước khi chuyển dữ liệu đến người dùng. Khách hàng có thể tùy chọn tính năng này khi khởi tạo CDN hoặc khi chỉnh sửa CDN đã tạo.
* **Minimum TLS Version**: Nếu website của bạn đang sử dụng giao thức HTTP và trong quá trình chuyển đổi sang HTTPS, trình duyệt sẽ cảnh báo khi trong website còn chứa các link HTTP. Tùy chọn này sẽ giúp thay thế tự động toàn bộ link HTTP thành HTTPS.
