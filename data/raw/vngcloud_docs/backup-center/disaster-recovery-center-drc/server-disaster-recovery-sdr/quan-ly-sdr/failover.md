# Failover

Chuyển đổi dự phòng (Failover) là một hành động quan trọng trong Disaster Recovery (DR), được thực hiện khi máy chủ chính (Main Server) gặp sự cố và không thể hoạt động bình thường. Việc chuyển đổi này đảm bảo tính liên tục cho hoạt động kinh doanh bằng cách chuyển hướng tất cả hoạt động sang máy chủ dự phòng (Shadow Server) đã được sao chép dữ liệu trước đó.

Làm theo hướng dẫn dưới đây để thực hiện chuyển đổi dự phòng khi cần thiết:

**Bước 1: Server Disaster Recovery tại đây:**&#x20;

**Bước 2: Chọn máy chủ cần chuyển đổi dự phòng**

* Trong danh sách các máy chủ đã được bảo vệ (Server Disaster Recovery), xác định máy chủ bạn muốn thực hiện chuyển đổi dự phòng.
* Nhấp vào **DR Pair ID** tương ứng với máy chủ đó để xem thông tin chi tiết.

**Bước 3: Bắt đầu Failover**

* Trong giao diện chi tiết của máy chủ, tìm và nhấp vào nút **"Failover"**.

**Bước 4: Chọn điểm khôi phục (Recovery Point)**

* Một cửa sổ bật lên sẽ xuất hiện, yêu cầu bạn chọn điểm thời gian để khôi phục dữ liệu.
* Chọn điểm khôi phục mong muốn từ danh sách các điểm khôi phục khả dụng.
* Nhấn nút **"Failover"** để bắt đầu quá trình chuyển đổi dự phòng.

**Bước 5: Theo dõi quá trình Failover**

* Trạng thái của máy chủ sẽ chuyển sang **"Failover Processing"** trong khi hệ thống đang xử lý yêu cầu của bạn.
* Quá trình sao chép dữ liệu (Replication) sẽ bị dừng lại hoàn toàn trong quá trình Failover.

**Bước 6: Xử lý lỗi (nếu có)**

* **Trường hợp Failover Error:** Nếu quá trình Failover gặp lỗi, bạn có thể:
  * **Restart Replication:** Khởi động lại quá trình sao chép từ đầu và thử Failover lại sau.
  * **Thực hiện Failover lại:** Chọn một Recovery Point khác và thử Failover lại.
  * **Liên hệ hỗ trợ:** Nếu không thể tự giải quyết, hãy liên hệ với đội ngũ hỗ trợ của VNG Cloud để được giúp đỡ.

**Bước 7: Kiểm tra và thay đổi Recovery Point (nếu cần)**

* **Trường hợp Failover thành công:**
  * Truy cập vào máy chủ Failover để kiểm tra xem dữ liệu đã được khôi phục đúng như mong muốn hay chưa.
  * Nếu cần thiết, bạn có thể thực hiện **"Change Recovery Point"** để khôi phục dữ liệu về một thời điểm khác.

**Bước 8: Xác nhận chuyển đổi dự phòng (Commit Failover)**

* Khi đã hoàn tất kiểm tra và hài lòng với kết quả, nhấn nút **"Commit Failover"** để hoàn tất quá trình chuyển đổi dự phòng.
* Đánh dấu/bỏ đánh dấu tùy chọn **"Delete all associated recovery points"** nếu bạn muốn xóa tất cả các điểm khôi phục liên quan.
* Nhấn nút **"Commit Failover"** để xác nhận.

**Lưu ý:**

* Sau khi Commit Failover, máy chủ dự phòng sẽ trở thành máy chủ chính và quá trình sao chép sẽ không còn hoạt động.
* Hãy cân nhắc kỹ trước khi thực hiện Commit Failover vì nó sẽ ảnh hưởng đến toàn bộ hệ thống của bạn.
