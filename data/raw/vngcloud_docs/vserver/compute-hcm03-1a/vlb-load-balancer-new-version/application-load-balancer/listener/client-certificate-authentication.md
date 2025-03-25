# Client Certificate Authentication

Tính năng "**Client Certificate Authentication**" là một phần quan trọng của hệ thống bảo mật mạng và ứng dụng. Nó cho phép bạn đảm bảo rằng chỉ những khách hàng hoặc thiết bị nào có chứng chỉ xác thực hợp lệ mới có thể truy cập vào ứng dụng hoặc dịch vụ của bạn.

**Cơ chế hoạt động**

* Khi một khách hàng hoặc thiết bị truy cập vào ứng dụng của bạn, hệ thống yêu cầu họ cung cấp một chứng chỉ số học xác thực riêng biệt.
* Chứng chỉ này thường được tạo và quản lý bởi một tổ chức chứng thực hoặc PKI (Public Key Infrastructure).
* Hệ thống sau đó kiểm tra chứng chỉ này để đảm bảo rằng nó hợp lệ và có thể xác định khách hàng hoặc thiết bị.
* Nếu chứng chỉ hợp lệ, khách hàng hoặc thiết bị được cho phép truy cập vào ứng dụng hoặc dịch vụ.

**Lợi ích**

* **Bảo Mật Tăng Cao**: Xác thực chứng chỉ tạo ra một lớp bảo mật mạnh mẽ bằng cách đảm bảo rằng chỉ có những người dùng hoặc thiết bị được xác định và có quyền truy cập.
* **Quản Lý Truy Cập Chi Tiết**: Bạn có thể quản lý truy cập của từng khách hàng hoặc thiết bị dựa trên chứng chỉ riêng biệt.
* **Tuân Thủ Bảo Mật**: Nó giúp bạn tuân thủ các quy tắc và tiêu chuẩn bảo mật nghiêm ngặt.

#### Cách bật/tắt tính năng Client Certificate Authentication <a href="#clientcertificateauthentication-cachbat-tattinhnangclientcertificateauthentication" id="clientcertificateauthentication-cachbat-tattinhnangclientcertificateauthentication"></a>

Đối với HTTPS Listener, người dùng có thể chủ động bật/tắt tính năng Client Certificate bất kỳ lúc nào.

**Hướng dẫn bật/tắt Client Certificate Authentication**

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần chỉnh sửa.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn biểu tượng Edit tại HTTPS Listener cần bật/tắt tính năng Client CA.**
5. **Một cửa sổ giao diện sẽ hiện ra, tại phần thông tin Listener, tìm đến Cài đặt nâng cao.**
6. **Tại phần Cài đặt nâng cao, check/uncheck vào check box Bật Client CA. Trường hợp Bật Client CA, người dùng cần chọn một Certificate từ danh sách Certificate trên hệ thống.**
7. **Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.**

\


\
