# Deployment Mode

Trong môi trường điện toán đám mây của VNG Cloud, chúng tôi cung cấp hai loại Load Balancer riêng biệt: Application Load Balancer và Network Load Balancer. Các Load Balancer này đóng một vai trò quan trọng trong việc tối ưu hóa hiệu suất, tính khả dụng và khả năng mở rộng của ứng dụng của bằng cách phân phối lưu lượng mạng đến các máy chủ backend một cách hiệu quả. Mỗi loại Load Balancer được tùy chỉnh cho các tình huống sử dụng cụ thể, cung cấp các tính năng độc đáo để đáp ứng các yêu cầu đa dạng của kiến trúc IT hiện đại.

**Tổng quan mô hình triển khai Load Balancer tại VNG Cloud như sau**

<figure><img src="../../../.gitbook/assets/64553488 (1).png" alt=""><figcaption></figcaption></figure>

**Model quản lý Load Balancer bao gồm các component chính như sau**

* **Layer:** Hỗ trợ 2 loại chính, bao gồm:
  * _Application Load Balancer:_ Application layer Load Balancer định tuyến lưu lượng dựa trên yêu cầu HTTP/HTTPS, cho phép phân tích dữ liệu cấp ứng dụng như HTTP Header và Cookie. Lý tưởng cho các ứng dụng web có yêu cầu định tuyến phức tạp hoặc nhu cầu định tuyến dựa trên nội dung.
  * _Network Load Balancer:_ Một transport-layer Load Balancer sử dụng TCP và UDP để phân phối lưu lượng giữa nhiều Server dựa trên địa chỉ IP và số cổng, lý tưởng cho các ứng dụng cần độ đáng tin cậy và độ sẵn sàng cao.
* **Scheme:** Bao gồm 2 scheme chính
  * _Internet-facing:_ Internet-facing Load Balancer định tuyến trên Internet chuyển hướng các yêu cầu từ máy khách qua Internet đến các cụm máy chủ, cho phép truy cập vào các ứng dụng hoặc dịch vụ từ Internet.
  * _Internal:_ Internal Load Balancer định tuyến lưu lượng trong mạng nội bộ của máy khách đến các cụm máy chủ, giúp phân phối yêu cầu hiệu quả trong mạng nội bộ.
* **Load Balancer:** Hỗ trợ triển khai 2 mô hình Load Balancer bao gồm Application LB và Network LB, trong mỗi Load Balancer bao gồm các thành phần chính như:
  * **Listener:** Listener là thành phần giám sát và lắng nghe các yêu cầu kết nối đến. Nó có trách nhiệm nhận lưu lượng truy cập trên một cổng và giao thức cụ thể, sau đó chuyển tiếp hoặc định tuyến lưu lượng đó đến các máy chủ hợp lệ dựa trên các quy tắc và cấu hình đã được xác định.
    * **Policy**: Đối với Application Load Balancer, Policy hoạt động như một bộ quy chuẩn/điều kiện để phân phối các yêu cầu đến các máy chủ backend
  * **Pool**: Pool (cụm máy chủ) đại diện cho một nhóm các máy chủ và xử lý lưu lượng truy cập đến. Pool có trách nhiệm cân bằng tải các yêu cầu trên các thành viên của nó, đảm bảo phân phối và tận dụng tài nguyên một cách hiệu quả.
    * **Pool Member:** Một Pool Memeber hoạt động như một máy chủ thành viên trong Pool.
    * **Health Check:** Health Check setting là một bộ quy định, qua đó giúp Load Balancer giám sát sức khỏe của các Pool và Pool Member trực thuộc.

#### Chủ đề <a href="#deploymentmode-chude" id="deploymentmode-chude"></a>

Tìm hiểu thêm về Application Load Balancer và Network Load Balancer tại đây:

* [Application Load Balancer](application-load-balancer/)
* [Network Load Balancer](network-load-balancer/)
* [Feature Comparison](feature-comparison.md)
