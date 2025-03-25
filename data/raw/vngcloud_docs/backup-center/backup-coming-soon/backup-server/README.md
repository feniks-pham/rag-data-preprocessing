# Backup Server

**Backup Server** là một dịch vụ chuyên biệt nhằm bảo vệ dữ liệu của hệ thống bằng cách tạo và lưu trữ các bản sao lưu (backup) một cách tự động và định kỳ. Dịch vụ này cung cấp một giải pháp toàn diện để bảo vệ dữ liệu khỏi những sự cố bất ngờ như hỏng hóc phần cứng, lỗi phần mềm, tấn công mạng, hoặc thiên tai.

## Cơ chế hoạt động

**1. Backup Location (Vị trí lưu trữ):**

* **Chức năng:** Đây là nơi lưu trữ các bản sao lưu (Backup Server Point) được tạo ra từ các Backup Server.
* **Tính năng:**
  * **Location Lock:** Ngăn chặn việc xóa các bản sao lưu một cách tùy tiện, đảm bảo tính toàn vẹn của dữ liệu.
  * **Soft Delete:** Khi một bản sao lưu bị xóa, nó sẽ được lưu trữ trong một khoảng thời gian nhất định (retention day) trước khi bị xóa vĩnh viễn, tạo cơ hội phục hồi dữ liệu nếu cần.

**2. Backup Server (Máy chủ sao lưu):**

* **Chức năng:** Đóng vai trò như một kế hoạch sao lưu (Backup Plan).
* **Hoạt động:** Để sao lưu một máy chủ, người dùng cần tạo một Backup Server tương ứng. Backup Server sẽ được cấu hình với các thông số như:
  * **Backup Policy:** Quy định lịch trình sao lưu tự động.
  * **Backup Location:** Chỉ định vị trí lưu trữ các bản sao lưu.
* **Mục tiêu:** Đảm bảo rằng dữ liệu của máy chủ được sao lưu một cách định kỳ và an toàn.

**3. Backup Policy (Chính sách sao lưu):**

* **Chức năng:** Quản lý và cài đặt lịch trình chạy tự động của các Backup Server.
* **Cấu hình:** Người dùng có thể tùy chỉnh lịch trình sao lưu theo nhu cầu, ví dụ: hàng ngày, hàng tuần, hàng tháng, hoặc theo một lịch trình tùy biến.

**4. History (Lịch sử):**

* **Chức năng:** Lưu trữ tất cả các hoạt động liên quan đến dịch vụ Backup Server, bao gồm:
  * **Lịch sử chạy Backup Server:** Ghi lại thời gian bắt đầu, kết thúc, kết quả của mỗi lần sao lưu.
  * **Lịch sử khôi phục:** Ghi lại các lần khôi phục dữ liệu từ bản sao lưu.
  * **Lịch sử chỉnh sửa Backup Location:** Ghi lại các thay đổi về cấu hình của vị trí lưu trữ.
* **Mục đích:** Cung cấp một bản ghi chi tiết về các hoạt động của hệ thống, giúp người dùng theo dõi và quản lý quá trình sao lưu một cách hiệu quả.

## Lợi ích từ Backup Server và Backup Location

Backup Server và các tính năng đi kèm như Backup Location, Lock, Soft Delete, và lưu trữ Cross-region là một giải pháp bảo vệ dữ liệu toàn diện, giúp doanh nghiệp giảm thiểu rủi ro mất mát dữ liệu, tăng cường tính sẵn sàng của hệ thống và đảm bảo tuân thủ các quy định về bảo mật.

**1. Bảo vệ dữ liệu toàn diện**

* **Phục hồi dữ liệu nhanh chóng:** Khi gặp sự cố mất dữ liệu, việc khôi phục từ bản sao lưu sẽ diễn ra nhanh chóng, giúp doanh nghiệp nhanh chóng trở lại hoạt động bình thường.
* **Ngăn chặn mất mát dữ liệu vĩnh viễn:** Các bản sao lưu được lưu trữ ở một vị trí khác biệt, giúp bảo vệ dữ liệu khỏi những rủi ro như hỏng hóc phần cứng, xóa nhầm, hoặc tấn công ransomware.
* **Tuân thủ quy định:** Đảm bảo tuân thủ các quy định về lưu trữ và bảo mật dữ liệu, đặc biệt là đối với các ngành có yêu cầu cao về bảo mật như tài chính, y tế.

**2. Tính năng Backup Location nâng cao**

* **Lưu trữ Cross-region:**
  * **Bảo vệ trước thảm họa:** Lưu trữ bản sao lưu ở nhiều vùng địa lý khác nhau giúp giảm thiểu rủi ro mất dữ liệu do thiên tai, sự cố cơ sở hạ tầng tại một khu vực.
  * **Tăng cường tính sẵn sàng:** Ngay cả khi một khu vực gặp sự cố, dữ liệu vẫn được bảo vệ an toàn ở các khu vực khác.
* **Tính năng Lock và Soft Delete:**
  * **Bảo vệ dữ liệu khỏi bị xóa nhầm:** Tính năng Lock ngăn chặn việc xóa các bản sao lưu quan trọng, đảm bảo tính toàn vẹn của dữ liệu.
  * **Khôi phục dữ liệu đã xóa:** Tính năng Soft Delete cho phép khôi phục lại các bản sao lưu đã bị xóa trong một khoảng thời gian nhất định, tránh mất mát dữ liệu không đáng có.
* **Phòng chống ransomware:**
  * **Ngăn chặn mã hóa dữ liệu:** Các bản sao lưu được lưu trữ ở một vị trí riêng biệt, không thể truy cập trực tiếp từ hệ thống đang bị tấn công, giúp ngăn chặn ransomware mã hóa toàn bộ dữ liệu.
  * **Khôi phục dữ liệu nhanh chóng:** Sau khi loại bỏ ransomware, doanh nghiệp có thể khôi phục dữ liệu từ bản sao lưu một cách nhanh chóng.

**3. Lợi ích chi phí và tính sẵn sàng cao**

* **Tăng tính sẵn sàng của hệ thống:** Việc có sẵn các bản sao lưu giúp giảm thiểu thời gian gián đoạn hoạt động của hệ thống khi xảy ra sự cố.
* **Giảm thiểu chi phí:** So với việc xây dựng một hệ thống sao lưu riêng, sử dụng dịch vụ Backup Server thường có chi phí thấp hơn và dễ quản lý hơn.
* **Tăng cường hiệu quả làm việc:** Nhân viên IT có thể tập trung vào các công việc khác thay vì phải quản lý hệ thống sao lưu.
