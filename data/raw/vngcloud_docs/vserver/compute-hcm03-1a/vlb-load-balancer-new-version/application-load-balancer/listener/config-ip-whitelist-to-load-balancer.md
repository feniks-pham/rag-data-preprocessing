# Config IP whitelist to load balancer

Tính năng **cấu hình Whitelist IP Source** cho Load Balancer là một phần quan trọng của bảo mật mạng, cho phép bạn xác định các địa chỉ IP nguồn cụ thể mà Load Balancer sẽ chấp nhận lưu lượng từ. Các địa chỉ IP không nằm trong dải IP cho phép sẽ bị từ chối truy cập.

**Cách hoạt động**

* Khi một yêu cầu truy cập đến Load Balancer, hệ thống sẽ kiểm tra địa chỉ IP nguồn của yêu cầu.
* Nếu địa chỉ IP nguồn nằm trong dải CIDRs cho phép, yêu cầu sẽ được chấp nhận và tiếp tục đến máy chủ backend.
* Nếu địa chỉ IP nguồn không nằm trong dải CIDRs cho phép, yêu cầu sẽ bị từ chối và không được chuyển tiếp.

**Tại sao cần cấu hình IP Whitelist đến Load Balancer**

* **Bảo Mật Tăng Cao**: Tính năng này tăng cường bảo mật bằng cách kiểm soát chặt chẽ quyền truy cập từ các địa chỉ IP nguồn không xác định.
* **Phòng Chống Tấn Công**: Nó giúp ngăn chặn các tấn công từ các địa chỉ IP đáng ngờ hoặc không mong muốn.
* **Quản Lý Quyền Truy Cập**: Whitelist IP Source cho phép bạn quản lý quyền truy cập vào Load Balancer một cách chi tiết và hiệu quả.

#### Hướng dẫn cấu hình <a href="#configipwhitelisttoloadbalancer-huongdancauhinh" id="configipwhitelisttoloadbalancer-huongdancauhinh"></a>

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn biểu tượng Edit tại Listener cần cấu hình.**
5. **Một cửa sổ giao diện sẽ hiện ra, tìm đến phần Cấu hình nâng cao ở phía dưới cùng của cửa sổ.**
6. **Tại phần Allowed CIDRs (Cho phép CIDRs), người dùng có thể cấu hình dải IP được phép truy cập.**
   * Ví dụ người dùng nhâp **"192.168.0.0/24, 172.16.0.0/24"** có nghĩa là chỉ những địa chỉ IP thuộc 2 dải IP Range này mới có quyền truy cập.
7. **Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.**

\
