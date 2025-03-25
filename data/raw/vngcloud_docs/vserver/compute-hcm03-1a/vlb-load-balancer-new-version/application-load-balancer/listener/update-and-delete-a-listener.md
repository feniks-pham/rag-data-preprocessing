# Update & Delete a Listener

Sử dụng hướng dẫn này để thay đổi thông tin/xóa Listener trong việc quản lý Load Balancer.

**Thay đổi thông tin Listener**

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần chỉnh sửa Listener.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Tại danh sách Listener, nhấn chọn Listener cần chỉnh sửa, sau đó xem lại thông tin chi tiết Listener tại phía bên phải trước khi thực hiện chỉnh sửa. Phần thông tin chi tiết bao gồm:**
   * Thông tin Listener
   * Thông tin Policy
   * Thông tin Certificate (đối với HTTPS Listener)
5. **Nhấn vào biểu tượng Edit ở hàng Listener cần chỉnh sửa tại mục danh sách Listener**
6. **Một cửa sổ giao diện chỉnh sửa xuất hiện, người dùng có thể chỉnh sửa các thông tin sau:**
   * **Chỉnh sửa Request Headers**
   * **Bật/Tắt tính năng Client Certificate Authentication (đối với HTTPS Listener)**: Tham khảo thêm tính năng [Client Certificate Authentication](client-certificate-authentication.md)
   * **Thay đổi Certificate mặc định (đối với HTTPS Listener)**
   * **Thay đổi Pool mặc định:** Trong trường các request đến Listener nằm ngoài danh sách Policies được cấu hình, các request này sẽ được chuyển hướng đến Pool mặc định để xử lý.
   * **Thay đổi cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
     * [Config timeout](config-timeout.md)
     * [Config IP whitelist to load balancer](config-ip-whitelist-to-load-balancer.md)
7. Nhấn nút "Lưu" để hoàn tất chỉnh sửa

**Xóa Listener**

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần xóa Listener.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Tại danh sách Listener, nhấn chọn biểu tượng "Xóa" tại hàng Listener cần xóa.**
5. **Một cửa sổ giao diện sẽ xuất hiện để xác nhận xóa, nhấn nút "Xóa" để hoàn tất.**

\
