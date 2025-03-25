---
hidden: true
---

# Những câu hỏi thường gặp (FAQ)

### <mark style="color:blue;">\[vCloudStack] Những tài nguyên vật lý của doanh nghiệp sẽ đặt ở đâu?</mark>

Với mô hình Private Cloud dành cho doanh nghiệp ưu tiên vấn đề bảo mật và an toàn thông tin, do đó toàn bộ hạ tầng vật lý sẽ được đặt tại cơ sở nội bộ của doanh nghiệp.

### <mark style="color:blue;">\[vCloudStack] Những doanh nghiệp nào phù hợp sử dụng dịch vụ vCloudStack của VNG Cloud?</mark>

Các doanh nghiệp tổ chức hoạt động trong các hoạt động tài chính, chăm sóc sức khỏe, cơ quan đoàn thể cung câp các dịch vụ mang thông tin nhạy cảm của khách hàng, cần lưu trữ an toàn toàn bộ dữ liệu cho khách hàng tại hệ thống nội bộ của doanh nghiệp và không được sử dụng các sản phẩm lưu trữ của public cloud.

### <mark style="color:blue;">\[vCloudStack] Khi một host vật lý bị sự cố thì dịch vụ vCloudStack xử lý thế nào?</mark>

...

### <mark style="color:blue;">\[vCloudStack] Việc sử dụng ảo hóa các tài nguyên vật lý sẽ có tỷ lệ ratio như thế nào?</mark>

Việc ảo hóa tài nguyên vật lý sẽ dự vào một chỉ số gọi là Tỉ lệ cấp phát vCPU (vCPU Allocation Ratio) với số lượng tài nguyên vật lý thì sẽ có thể tạo ra số lượng vCPU để sử dụng cho các máy ảo VM sử dụng. Ví dụ cụ thể, nếu ta có số lượng tài nguyên vật lý là 24, có tỉ lệ cấp phát là 4 thì số vCPU cấp phát được là 24 x 4 = 96 vCPU.

### <mark style="color:blue;">\[vCloudStack] Làm thế nào để theo dõi lịch sử hoạt động của máy ảo?</mark>

Việc theo dõi máy chủ ảo VM là hoàn toàn khả thi, người vận hành VM có thể theo dõi tình trạng hoạt động của máy chủ ảo trên portal User Site của hệ thống vCloudStack, bằng cách vào chi tiết của VM, tìm đến tab Monitor để xem chi tiết theo dõi tình trạng hoạt động theo lịch sử thời gian cụ thể.

### <mark style="color:blue;">\[vCloudStack] Làm thế nào để theo dõi lịch sử hoạt động của host vật lý?</mark>

...

### <mark style="color:blue;">\[vCloudStack] Có thể tùy chọn ngưỡng vận hành provisioning của tài nguyên được không? Nhưng nếu để ngưỡng quá cao thì ảnh hưởng gì hay không?</mark>

Dịch vụ vCloudStack có thể cấu hình ngưỡng cấp phất  provisioning, khuyên cáo ngưỡng nên vào khoảng 70%, nếu khách hàng có nhu cầu cấu hình đến 90% vẫn hoàn toàn có thể, tuy nhiên sẽ có những rủi ro mất kiểm soát hệ thống, khách hàng nên cân nhắc trước khi thay đổi ngưỡng.

### <mark style="color:blue;">\[vCloudStack] Để tránh những rủi ro khi vận hành, có thể tạo máy chủ VM ở những host khác nhau không?</mark>

Không chỉ dịch vụ vCloudStack mà Public Cloud của VNG Cloud cho phép người dùng có thể cấu hình tạo VM khác Host vật lý khác nhau. Tham khảo thêm ở bài viết Placement Group.





