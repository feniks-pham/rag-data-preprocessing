# Load Balancer trong vCloudStack

Nhằm phân phối lưu lượng mạng đến nhiều máy chủ VM, cũng như đảm bảo việc sử dụng tài nguyên hiệu quả và tăng khả năng khả dụng của ứng dụng. vCloudStack cung cấp dịch vụ Load Balancer bằng cách phân phối lưu lượng dựa trên các quy tắc và thuật toán đã xác định, Load Balancer cải thiện hiệu suất và là một công cụ đáng tin cậy cho ứng dụng của người dùng, ngăn chặn bất kỳ máy chủ thành viên đơn lẻ nào trở nên quá tải.

Mô hình để Load Balancer hoạt động trong vCloudStack bao gồm những thành phần như sau:

* <mark style="color:blue;">**Layer**</mark>**:** Hỗ trợ 2 loại chính, bao gồm:
  * _Application Load Balancer:_ Application layer Load Balancer định tuyến lưu lượng dựa trên yêu cầu HTTP/HTTPS, cho phép phân tích dữ liệu cấp ứng dụng như HTTP Header và Cookie. Lý tưởng cho các ứng dụng web có yêu cầu định tuyến phức tạp hoặc nhu cầu định tuyến dựa trên nội dung.
  * _Network Load Balancer:_ Một transport-layer Load Balancer sử dụng TCP và UDP để phân phối lưu lượng giữa nhiều Server dựa trên địa chỉ IP và số cổng, lý tưởng cho các ứng dụng cần độ đáng tin cậy và độ sẵn sàng cao.
* <mark style="color:blue;">**Scheme**</mark>: chỉ áp dụng scheme là Internal:
  * _Internal:_ Internal Load Balancer định tuyến lưu lượng trong mạng nội bộ của máy khách đến các cụm máy chủ, giúp phân phối yêu cầu hiệu quả trong mạng nội bộ.
* **Load Balancer:** Hỗ trợ triển khai 2 mô hình Load Balancer bao gồm Application LB và Network LB, trong mỗi Load Balancer bao gồm các thành phần chính như:
  * <mark style="color:blue;">**Listener:**</mark> Listener là thành phần giám sát và lắng nghe các yêu cầu kết nối đến. Nó có trách nhiệm nhận lưu lượng truy cập trên một cổng và giao thức cụ thể, sau đó chuyển tiếp hoặc định tuyến lưu lượng đó đến các máy chủ hợp lệ dựa trên các quy tắc và cấu hình đã được xác định.
    * **Policy**: Đối với Application Load Balancer, Policy hoạt động như một bộ quy chuẩn/điều kiện để phân phối các yêu cầu đến các máy chủ backend
  * <mark style="color:blue;">**Pool**</mark><mark style="color:blue;">:</mark> Pool (cụm máy chủ) đại diện cho một nhóm các máy chủ và xử lý lưu lượng truy cập đến. Pool có trách nhiệm cân bằng tải các yêu cầu trên các thành viên của nó, đảm bảo phân phối và tận dụng tài nguyên một cách hiệu quả.
    * **Pool Member:** Một Pool Memeber hoạt động như một máy chủ thành viên trong Pool.
    * **Health Check:** Health Check setting là một bộ quy định, qua đó giúp Load Balancer giám sát sức khỏe của các Pool và Pool Member trực thuộc.

