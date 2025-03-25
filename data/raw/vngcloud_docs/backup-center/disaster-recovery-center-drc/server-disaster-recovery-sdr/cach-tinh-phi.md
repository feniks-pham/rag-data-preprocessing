---
description: Chi phí sử dụng Server Disaster Recovery
---

# Cách tính phí

Khi sử dụng dịch vụ Server Disaster Recovery (SDR), các khoản phí sau sẽ được tính:

* **Ổ đĩa dự phòng (Shadow Volume):** Phí sử dụng các ổ đĩa gắn liền với máy chủ dự phòng, tính theo dung lượng và loại ổ đĩa (SSD hoặc NVMe).
* **Máy chủ kiểm tra chuyển đổi dự phòng (Test Failover Server):** Khi thực hiện kiểm tra chuyển đổi dự phòng (Test Failover), một máy ảo mới sẽ được tạo ra tạm thời. Bạn sẽ phải trả các khoản phí tương tự như máy chủ dự phòng và ổ đĩa dự phòng cho máy ảo này trong thời gian kiểm tra.

**Đối với người dùng trả trước:**

* **Máy chủ dự phòng (Shadow Server):** Phí sử dụng máy chủ ảo (VM) được tạo ra để làm máy chủ dự phòng, bao gồm chi phí CPU, RAM, và các tài nguyên khác của máy chủ.
* **Credit:** Để có thể bắt đầu sao chép (Start Replication) và kiểm tra chuyển đổi dự phòng (Test Failover), bạn cần có đủ credit trong tài khoản của mình.
* **Thanh toán:** Các khoản phí trên sẽ được trừ trực tiếp từ số dư credit của bạn.

**Lưu ý:**

* Chi phí cụ thể có thể thay đổi tùy thuộc vào cấu hình máy chủ, loại ổ đĩa và lượng dữ liệu được sao chép.
* Bạn có thể xem chi tiết về giá dịch vụ SDR trên trang web của VNG Cloud hoặc liên hệ với đội ngũ hỗ trợ để được tư vấn cụ thể.

**Tóm tắt:**

* Các dịch vụ tại Server Disaster Recovery sẽ được tính phí dựa trên việc sử dụng ổ đĩa dự phòng.
* Khi thực hiện Test Failover, bạn cũng sẽ phải trả phí cho máy ảo tạm thời được tạo ra.
* Người dùng trả trước cần có đủ credit để sử dụng các tính năng Start Replication và Test Failover.
