# Thay đổi và xóa Listener (NLB)

Sử dụng hướng dẫn này để thay đổi thông tin/xóa Listener trong việc quản lý Load Balancer.

#### Thay đổi thông tin Listener <a href="#update-and-deletelistener-nlb-thaydoithongtinlistener" id="update-and-deletelistener-nlb-thaydoithongtinlistener"></a>

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần chỉnh sửa Listener.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Tại danh sách Listener, rê chuột đến Listener cần chỉnh sửa, một biểu tượng "Edit" sẽ hiện lên, nhấn vào biểu tượng đó để bắt đầu chỉnh sửa Listener.**
5. **Một cửa sổ giao diện chỉnh sửa xuất hiện, người dùng có thể chỉnh sửa các thông tin sau:**
   * **Thay đổi Pool mặc định:** Trong trường các request đến Load Balancer mà không phù hợp với bất kỳ pool cụ thể nào, NLB sẽ chuyển hướng lưu lượng đó đến pool mặc định.
   * **Thay đổi cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
     * [Config timeout](../../application-load-balancer/listener/config-timeout.md)
     * [Config IP whitelist to load balancer](../../application-load-balancer/listener/config-ip-whitelist-to-load-balancer.md)
6. **Nhấn nút "Lưu" để hoàn tất chỉnh sửa**

#### Xóa Listener <a href="#update-and-deletelistener-nlb-xoalistener" id="update-and-deletelistener-nlb-xoalistener"></a>

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần xóa Listener.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Tại danh sách Listener, nhấn chọn biểu tượng "Xóa" tại hàng Listener cần xóa.**
5. **Một cửa sổ giao diện sẽ xuất hiện để xác nhận xóa, nhấn nút "Xóa" để hoàn tất.**

\
