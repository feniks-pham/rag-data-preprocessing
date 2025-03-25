# Network GLB

**Network Global Load Balancer (NGLB)** là một giải pháp mạng giúp phân phối lưu lượng truy cập Internet đến nhiều máy chủ ở các vị trí địa lý khác nhau. NGLB hoạt động như một "người điều phối giao thông" trên Internet, đảm bảo rằng các yêu cầu từ người dùng được chuyển đến máy chủ phù hợp nhất, giúp tăng tốc độ truy cập, cải thiện độ tin cậy và mở rộng khả năng phục vụ của các ứng dụng.

#### Các tính năng chính của Network GLB:

* **Phân phối lưu lượng toàn cầu:** NGLB phân phối lưu lượng đến các máy chủ ở nhiều vị trí địa lý khác nhau, giúp giảm thiểu độ trễ và tăng tốc độ truy cập cho người dùng.
* **Cân bằng tải:** NGLB phân phối đều lưu lượng truy cập đến các máy chủ, giúp tránh tình trạng quá tải một máy chủ và đảm bảo hiệu suất ổn định.
* **Geolocation routing:** NGLB xác định vị trí địa lý của người dùng và chuyển hướng lưu lượng đến máy chủ gần nhất, giúp giảm thiểu độ trễ.
* **Health check:** NGLB liên tục kiểm tra tình trạng hoạt động của các máy chủ và tự động loại bỏ các máy chủ bị lỗi khỏi quá trình phân phối lưu lượng.
* **Failover:** Nếu một máy chủ gặp sự cố, NGLB sẽ tự động chuyển hướng lưu lượng đến các máy chủ còn lại, đảm bảo tính khả dụng của dịch vụ.
* **Tính linh hoạt:** NGLB cho phép cấu hình các thuật toán cân bằng tải khác nhau (ví dụ: Round Robin, Least Connections), tùy chỉnh các chính sách định tuyến và hỗ trợ nhiều giao thức mạng.
* **Tích hợp với DNS:** GSLB thường làm việc chặt chẽ với hệ thống DNS để định tuyến các yêu cầu đến địa chỉ IP của máy chủ phù hợp.
