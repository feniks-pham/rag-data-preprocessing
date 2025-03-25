# Enable TLS encryption

Tính năng **Enable TLS Encryption** là một yếu tố quan trọng của bảo mật mạng, cho phép bạn bảo vệ dữ liệu truyền tải từ Load Balancer đến máy chủ backend. Khi tính năng này được kích hoạt, dữ liệu truyền tải sẽ được mã hóa và bảo vệ trong suốt quá trình truyền tải.

**Cách hoạt động**

* Khi một máy khách kết nối đến Load Balancer và yêu cầu truy cập trang web hoặc ứng dụng của bạn, dữ liệu truyền tải giữa máy khách và Load Balancer sẽ được mã hóa bằng một giao thức bảo mật TLS (Transport Layer Security), trước khi nó được chuyển tiếp đến máy chủ backend.
* Máy chủ backend cũng cần hỗ trợ TLS để có thể giải mã dữ liệu được gửi từ Load Balancer.
* Quá trình này đảm bảo rằng dữ liệu truyền tải không thể bị đánh cắp hoặc hiểu được trong trường hợp nó bị bắt gặp trên đường truyền.

**Lợi ích khi bật tính năng TLS Encryption**

* **Bảo Mật Cao**: TLS Encryption đảm bảo mức độ bảo mật cao cho dữ liệu của bạn, giúp ngăn chặn các cuộc tấn công trung gian và đánh cắp dữ liệu.
* **Tích Hợp An Toàn**: Nó cho phép bạn cung cấp một trải nghiệm an toàn cho khách hàng của mình bằng cách bảo vệ thông tin cá nhân và tài khoản của họ khi dữ liệu được truyền đến Load Balancer.
* **Độ Tin Cậy**: TLS Encryption cung cấp độ tin cậy trong việc truyền tải dữ liệu trên mạng, giúp đảm bảo rằng dữ liệu không bị thất lạc hoặc bị sửa đổi trong quá trình truyền từ Load Balancer đến máy chủ backend.
* **Cho phép sử dụng Self-signed Certificate**: Tính năng TLS Encryption hỗ trợ cả HTTP và HTTPS. Đối với HTTPS, khi bật tính năng này, Load Balancer sẽ không xác minh tính đúng đắn của SSL/TLS Certificate. Việc này giúp bạn có thể sử dụng cả các self-signed certificate trên máy chủ thành viên.

#### Hướng dẫn bật tính năng TLS Encryption <a href="#enabletlsencryption-huongdanbattinhnangtlsencryption" id="enabletlsencryption-huongdanbattinhnangtlsencryption"></a>

1. Truy cập vào trang chủ Load Balancer tại đây: [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.
3. Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
4. Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.
5. Một cửa sổ bật lên cho phép chỉnh sửa Pool.
6. Tại phần thông tin Pool, tìm đến check box Bật mã hóa TLS/Enable TLS Encryption, check/uncheck để bật/tắt tính năng mã hóa TLS.
7. Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất chỉnh sửa.

\
