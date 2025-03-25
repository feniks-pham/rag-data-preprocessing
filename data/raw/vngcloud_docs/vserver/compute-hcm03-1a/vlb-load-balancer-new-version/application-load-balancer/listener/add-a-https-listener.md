# Add a HTTPS listener

Sử dụng hướng dẫn này để thêm mới một HTTPS Listener vào một Application Load Balancer có sẵn.

**Cách thêm mới HTTPS Listener**

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần thêm mới Listener.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn chọn nút "Thêm mới Listener", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Listener**
5. **Tại cửa sổ thêm mới, cấu hình các thông tin như:**
   * **Tên Listener:** Lưu ý rằng tên Listener không thể thay đổi sau khi khởi tạo
   * **Chọn Giao thức HTTPS và Port** (mặc định hiển thị Port 443 và tăng dần nếu các Port nhỏ hơn đã được sử dụng)
   * **Chọn Certificate mặc định**
   * **Chọn danh sách Certificate sử dụng như là SNI:** Lưu ý rằng bạn không thể gỡ bỏ/thay đổi các Certificate dùng cho tính năng SNI một khi hoàn tất khởi tạo HTTPS Listener
   * **Cấu hình request Header** tại phần cấu hình nâng cao: Mặc định điền sẵn X-Fowarded-For, X-Forwarded-Proto, X-Fowarded-Port, có thể bỏ chọn Header nếu không có nhu cầu.
   * **Bật tính năng Client Certificate Authentication:** Client CA là tính năng bảo mật nâng cao của Load Balancer, giúp xác thực ứng dụng khách bằng cách sử dụng Certificate. Tìm hiểu thêm về tính năng [Client Certificate Authentication](client-certificate-authentication.md)
   * **Cấu hình Pool mặc định và hành động:** Trong trường các request đến Listener nằm ngoài danh sách Policies được cấu hình, các request này sẽ được chuyển hướng đến Pool mặc định để xử lý.
   * **Cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
     * [Config timeout](config-timeout.md)
     * [Config IP whitelist to load balancer](config-ip-whitelist-to-load-balancer.md)

\
