# Add a HTTP listener

Sử dụng hướng dẫn này để thêm mới một HTTP Listener vào một Application Load Balancer có sẵn.

**Cách thêm mới HTTP Listener**

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần thêm mới Listener.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn chọn nút "Thêm mới Listener", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Listener**
5. **Tại cửa sổ thêm mới, cấu hình các thông tin như:**
   * **Tên Listener:** Lưu ý rằng tên Listener không thể thay đổi sau khi khởi tạo
   * **Chọn Giao thức HTTP và Port** (mặc định hiển thị Port 80 và tăng dần nếu các Port nhỏ hơn đã được sử dụng)
   * **Cấu hình request Header** tại phần cấu hình nâng cao: Mặc định điền sẵn X-Fowarded-For, X-Forwarded-Proto, X-Fowarded-Port, có thể bỏ chọn Header nếu không có nhu cầu.
   * **Cấu hình Pool mặc định và hành động:** Trong trường các request đến Listener nằm ngoài danh sách Policies được cấu hình, các request này sẽ được chuyển hướng đến Pool mặc định để xử lý.
   * **Cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
     * [Config timeout](config-timeout.md)
     * [Config IP whitelist to load balancer](config-ip-whitelist-to-load-balancer.md)

\
