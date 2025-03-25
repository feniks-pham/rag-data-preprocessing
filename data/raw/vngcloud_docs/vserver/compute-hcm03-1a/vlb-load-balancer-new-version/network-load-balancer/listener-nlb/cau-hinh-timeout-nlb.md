# Cấu hình timeout (NLB)

Tính năng **cấu hình timeout** cho Load Balancer cho phép bạn định rõ thời gian tối đa mà một kết nối hoặc yêu cầu có thể tồn tại trước khi bị đóng. Điều này quan trọng để quản lý tài nguyên và đảm bảo hiệu suất ổn định của hệ thống.

**Cách hoạt động**

* Khi một kết nối hoặc yêu cầu được gửi đến Load Balancer, hệ thống bắt đầu tính toán thời gian cho phép kết nối đó tồn tại.
* Nếu kết nối không hoàn thành hoặc yêu cầu không được phản hồi trong khoảng thời gian này, nó sẽ bị đóng.
* Việc cấu hình Timeout giúp tránh tình trạng kết nối hoặc yêu cầu bị treo và tiêu tốn tài nguyên.

**Tại sao cần cấu hình Timeout cho Load Balancer**

* **Quản Lý Tài Nguyên**: Timeout cấu hình giúp quản lý hiệu quả tài nguyên hệ thống bằng cách đảm bảo rằng các kết nối hoặc yêu cầu không cần thiết không tiêu tốn tài nguyên.
* **Bảo Đảm Hiệu Suất**: Điều này giúp đảm bảo rằng Load Balancer luôn hoạt động hiệu quả và không bị kẹt trong các kết nối hoặc yêu cầu không đáp ứng.

#### Hướng dẫn cấu hình timeout cho Load Balancer <a href="#configtimeout-nlb-huongdancauhinhtimeoutcholoadbalancer" id="configtimeout-nlb-huongdancauhinhtimeoutcholoadbalancer"></a>

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn biểu tượng Edit tại Listener cần cấu hình Timeout.**
5. **Một cửa sổ giao diện sẽ hiện ra, tìm đến phần Cấu hình nâng cao ở phía dưới cùng của cửa sổ.**
6. **Tại phần Idle Timeout, người dùng có thể cấu hình Timeout dựa trên các thuộc tính sau**
   * **Client Timeout (Timeout của Khách hàng):**
     * **Giải thích**: Client Timeout là thời gian tối đa mà Load Balancer cho phép một khách hàng (client) duy trì kết nối đến nó mà không thực hiện bất kỳ yêu cầu (request) nào. Nếu trong khoảng thời gian này không có hoạt động nào từ phía khách hàng, kết nối sẽ bị đóng.
     * **Lợi ích**: Điều này giúp giải phóng tài nguyên máy chủ backend và Load Balancer, đảm bảo rằng không có kết nối không cần thiết tiêu tốn tài nguyên.
   * **Member Timeout (Timeout của Member):**
     * **Giải thích**: Member Timeout là thời gian tối đa mà Load Balancer cho phép một máy chủ thành viên (member) trong nhóm máy chủ backend duy trì một kết nối mở mà không nhận được dữ liệu từ nó. Nếu máy chủ thành viên không gửi dữ liệu trong khoảng thời gian này, kết nối sẽ bị đóng.
     * **Lợi ích**: Điều này giúp đảm bảo rằng máy chủ thành viên không tiêu tốn tài nguyên bằng cách duy trì các kết nối không hoạt động.
   * **Connection Timeout (Timeout Kết nối):**
     * **Giải thích**: Connection Timeout là thời gian tối đa mà Load Balancer cho phép một kết nối mạng giữa nó và một máy chủ backend tồn tại trước khi bị đóng. Thời gian này bắt đầu tính từ khi kết nối được thiết lập. Nếu trong khoảng thời gian này không có hoạt động gì trên kết nối (bao gồm cả truyền dữ liệu), kết nối sẽ bị đóng.
     * **Lợi ích**: Điều này giúp đảm bảo rằng kết nối không cần thiết sẽ bị đóng, giải phóng tài nguyên và đảm bảo hiệu suất mạng ổn định.
7. **Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.**
