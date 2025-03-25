# Bắt đầu với Backup Server

**Bảo vệ dữ liệu của bạn một cách toàn diện với dịch vụ Backup Server**

Bạn đang lo lắng về việc mất dữ liệu quan trọng do sự cố máy tính, tấn công mạng hoặc thiên tai? Dịch vụ Backup Server sẽ là giải pháp hoàn hảo giúp bạn bảo vệ dữ liệu một cách an toàn và hiệu quả.

Với dịch vụ Backup Server, bạn có thể tự động tạo và lưu trữ các bản sao lưu dữ liệu của mình tại một vị trí an toàn. Điều này giúp bạn yên tâm hơn khi làm việc và giảm thiểu rủi ro mất mát dữ liệu.

**Hướng dẫn này sẽ giúp bạn:**

* Hiểu rõ các khái niệm cơ bản về Backup Server.
* Tự mình thiết lập và sử dụng dịch vụ một cách đơn giản.
* Tối ưu hóa quá trình sao lưu để bảo vệ dữ liệu hiệu quả nhất.

**Bắt đầu ngay để bảo vệ dữ liệu của bạn**

### 1. Tạo vị trí lưu trữ backup (Backup Location)

* **Mục đích:** Thiết lập nơi lưu trữ an toàn cho các bản sao lưu.
* **Các bước:**
  * **Tên vị trí:** Đặt tên dễ nhớ và mô tả cho vị trí lưu trữ.
  * **Vùng lưu trữ (Backup region):** Chọn vùng địa lý nơi muốn lưu trữ bản sao lưu.
  * **Dung lượng tối đa (Max quota):** Xác định giới hạn dung lượng tối đa cho vị trí lưu trữ.
  * **Soft Delete:**
    * **Bật/tắt:** Quyết định có cho phép soft delete bản sao lưu hay không.
    * **Thời gian giữ dữ liệu (Retention day):** Nếu bật soft delete, nhập số ngày bản sao lưu sẽ được giữ trước khi xóa vĩnh viễn.
  * **Đặt làm vị trí mặc định:** Chọn backup location này làm vị trí lưu trữ mặc định cho các bản sao lưu mới.
  * **Location Lock:**
    * **Thời gian giữ dữ liệu tối thiểu (Min retention day):** Thời gian ngắn nhất mà bản sao lưu phải được giữ lại.
    * **Thời gian giữ dữ liệu tối đa (Max retention day):** Thời gian dài nhất mà bản sao lưu được giữ lại.
    * **Thời gian thay đổi (Change duration):** Trong thời gian này, người dùng có thể thay đổi các cấu hình về Min và Max retention day, cũng như tắt tính năng Lock. Khi vượt qua thời gian này, cấu hình trên tính năng Lock sẽ không thể thay đổi.

### 2. Tạo Chính Sách Sao Lưu (Backup Policy)

* **Mục đích:** Thiết lập lịch trình và quy tắc sao lưu.
* **Các bước:**
  * **Tên chính sách:** Đặt tên dễ nhớ và mô tả cho chính sách.
  * **Cấu hình thời gian:**
    * **Chọn thời gian:** Lựa chọn thời điểm bắt đầu sao lưu (giờ, phút).
    * **Múi giờ:** Chọn múi giờ phù hợp.
  * **Cấu hình giữ dữ liệu:**
    * **Hàng giờ, hàng ngày, hàng tuần, hàng tháng:** Chọn tần suất giữ lại bản sao lưu.
    * **Kết hợp nhiều quy tắc:** Có thể kết hợp nhiều quy tắc để tạo lịch trình linh hoạt.
  * **Bật bảo vệ máy chủ:** Tự động tạo bản sao lưu cho máy chủ ngay khi bật tính năng này, không cần chờ theo lịch.
  * **Thông báo:** Chọn nhận thông báo qua email khi quá trình sao lưu thành công hoặc thất bại.

### 3. Tạo Máy Chủ Sao Lưu (Backup Server)

* **Mục đích:** Liên kết máy chủ cần bảo vệ với chính sách và vị trí lưu trữ.
* **Các bước:**
  * **Chọn máy chủ:** Lựa chọn máy chủ cần sao lưu từ danh sách.
  * **Chọn chính sách:** Áp dụng chính sách sao lưu đã tạo.
  * **Chọn vị trí lưu trữ:** Chọn vị trí lưu trữ cho bản sao lưu của máy chủ.

### 4. Xem Lịch Sử Sao Lưu

* **Mục đích:** Theo dõi hoạt động sao lưu và khôi phục.
* **Các bước:**
  * Truy cập vào mục lịch sử.
  * Xem chi tiết các hoạt động sao lưu, khôi phục, lỗi (nếu có).
  * Lọc dữ liệu theo máy chủ, chính sách, thời gian để tìm kiếm thông tin cụ thể.
