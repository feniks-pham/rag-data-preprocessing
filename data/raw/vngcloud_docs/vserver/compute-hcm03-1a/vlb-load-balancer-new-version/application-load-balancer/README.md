# Application Load Balancer

#### Application Load Balancer là gì? <a href="#applicationloadbalancer-applicationloadbalancerlagi" id="applicationloadbalancer-applicationloadbalancerlagi"></a>

* Application Load Balancer (ALB) là một công cụ trong hạ tầng mạng và máy chủ được sử dụng để phân phối lưu lượng mạng đến nhiều máy chủ hoặc máy ảo để cải thiện hiệu suất và khả năng sẵn sàng của các ứng dụng. ALB hoạt động ở tầng ứng dụng, cho phép phân phối lưu lượng dựa trên nhiều yếu tố như loại yêu cầu, trạng thái của máy chủ và thuật toán phân phối tải.
* ALB cung cấp khả năng định tuyến nâng cao, cho phép điều hướng lưu lượng dựa trên các Host hay Path Header. Nó cũng hỗ trợ tính năng duy trì phiên, giúp duy trì liên tục phiên của người dùng đối với cùng một máy chủ. Điều này rất hữu ích cho các ứng dụng yêu cầu sự nhất quán trong quá trình tương tác của người dùng.

Nhờ những tính năng độc đáo này, Application Load Balancer đóng một vai trò quan trọng trong việc cải thiện hiệu suất, khả năng mở rộng và sẵn sàng của các ứng dụng trực tuyến.

#### Các tính năng nổi bật <a href="#applicationloadbalancer-cactinhnangnoibat" id="applicationloadbalancer-cactinhnangnoibat"></a>

* **Advanced Routing**: ALB cho phép định tuyến dựa trên Host và Path Header. Điều này giúp bạn điều hướng các yêu cầu đến các mục tiêu cụ thể dựa trên nội dung yêu cầu, cung cấp khả năng điều chỉnh phân phối lưu lượng dựa Host và Path.
* **X-Forwarded Headers**: Hỗ trợ thêm các HTTP Header phổ biến vào yêu cầu trước khi phân phối xuống máy chủ backend. Các header này giúp máy chủ backend có thêm thông tin về client đang gửi yêu cầu đến hệ thống.
* **Session Persistence**: ALB hỗ trợ duy trì phiên, giúp đảm bảo rằng các yêu cầu từ cùng một người dùng sẽ luôn được chuyển hướng đến cùng một máy chủ backend. Điều này làm tăng tính nhất quán của trải nghiệm người dùng.
* **Health Checks**: ALB tự động kiểm tra sức khỏe của các máy chủ backend bằng cách gửi các yêu cầu kiểm tra định kỳ. Nếu một máy chủ không hoạt động đúng cách, ALB sẽ ngừng chuyển hướng lưu lượng đến máy chủ đó, đảm bảo hiệu suất cao hơn và sẵn sàng tốt hơn.
* **SSL/TLS Encryption**: ALB có thể xử lý mã hóa và giải mã lưu lượng SSL/TLS, giảm bớt công việc tính toán từ các máy chủ backend và tăng cường hiệu suất tổng thể.
* **Authentication and Authorization**: Tích hợp VNG Cloud IAM, hỗ trợ đầy đủ các tính năng về xác thực và phân quyền.
* **Monitor Loadbalance**r: Dễ dàng giám sát sức khỏe, lịch sử truy cập của client & lịch sử chỉnh sửa Loadbalancer.
* **Terraform**: Hỗ trợ khởi tạo và quản lý Load Balancer nhanh chóng và hiệu quả với Terraform

#### &#x20;<a href="#applicationloadbalancer-chude" id="applicationloadbalancer-chude"></a>
