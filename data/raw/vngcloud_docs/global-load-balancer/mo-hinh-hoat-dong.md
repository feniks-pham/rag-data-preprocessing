# Mô hình hoạt động

GLB là một công cụ quan trọng để đảm bảo hiệu suất và độ sẵn sàng của các ứng dụng web trên quy mô toàn cầu. Bằng cách phân phối lưu lượng đến các máy chủ phù hợp, GLB giúp giảm thiểu độ trễ, tăng cường khả năng phục hồi và cải thiện trải nghiệm người dùng. Dưới đây là ví dụ về mô hình hoạt động của GLB.

<figure><img src="../.gitbook/assets/GLB-Overview.drawio (1).png" alt=""><figcaption><p>Mô hình hoạt động</p></figcaption></figure>

1. **Phân phối địa lý:** Bạn triển khai các máy chủ ứng dụng của mình ở nhiều vùng địa lý khác nhau (ví dụ: HCM-03, HAN-01)
2. **Cấu hình GLB:** Bạn cần thiết lập một GLB để quản lý việc phân phối lưu lượng đến các máy chủ này. GLB sẽ theo dõi tình trạng của từng máy chủ và tình hình mạng.
3. **Người dùng truy cập:** Khi một người dùng gõ địa chỉ website của bạn, yêu cầu sẽ được gửi đến GLB.
4. **Xác định vị trí:** GLB sẽ xác định vị trí địa lý của người dùng dựa trên địa chỉ IP.
5. **Chọn máy chủ:** Dựa trên vị trí của người dùng và các thông tin khác (như tải của máy chủ, tình trạng hoạt động), GLB sẽ chọn một máy chủ gần nhất và có khả năng xử lý yêu cầu tốt nhất.
6. **Chuyển hướng:** GLB sẽ chuyển hướng yêu cầu của người dùng đến máy chủ đã chọn.

**Các yếu tố quan trọng trong hoạt động của GLB:**

* **Geolocation:** Khả năng xác định vị trí địa lý của người dùng là yếu tố cốt lõi của GSLB.
* **Thuật toán cân bằng tải:** GLB sử dụng các thuật toán để phân phối tải một cách hiệu quả, đảm bảo không có máy chủ nào bị quá tải.
* **Health check:** GLB liên tục kiểm tra tình trạng hoạt động của các máy chủ để loại bỏ các máy chủ bị lỗi khỏi quá trình phân phối tải.
* **DNS:** GLB thường làm việc chặt chẽ với hệ thống DNS để định tuyến các yêu cầu đến địa chỉ IP của máy chủ phù hợp.
