# vLB (Load Balancer) - New Version



Hướng dẫn này được thiết kế nhằm mục đích cung cấp cho người dùng cái nhìn toàn diện và hướng dẫn từng bước để hiệu quả hóa việc sử dụng tính năng Load Balancer và tối ưu hóa tài nguyên đám mây của bạn cũng như việc cải thiện tính khả dụng và hiệu suất của ứng dụng load balancer...



{% embed url="https://youtu.be/o4EOm0WCiJ0?si=GtDmJ_3-YqL8bIZ6" %}
Hướng dẫn khởi tạo và quản lý Load Balancer
{% endembed %}

### Tổng quan về VNG Cloud load balancer <a href="#vlb-loadbalancer-newversion-tongquanvevngcloudloadbalancer" id="vlb-loadbalancer-newversion-tongquanvevngcloudloadbalancer"></a>

#### Load Balancer là gì? <a href="#vlb-loadbalancer-newversion-loadbalancerlagi" id="vlb-loadbalancer-newversion-loadbalancerlagi"></a>

Load Balancer là một công cụ mạnh mẽ được thiết kế để phân phối đều lưu lượng mạng đến nhiều máy chủ backend, đảm bảo việc sử dụng tài nguyên hiệu quả và tăng khả năng khả dụng của ứng dụng. Bằng cách phân phối lưu lượng dựa trên các quy tắc và thuật toán đã xác định, Load Balancer cải thiện hiệu suất và là một công cụ đáng tin cậy cho ứng dụng của người dùng, ngăn chặn bất kỳ máy chủ thành viên đơn lẻ nào trở nên quá tải.

#### Các tính năng chính <a href="#vlb-loadbalancer-newversion-cactinhnangchinh" id="vlb-loadbalancer-newversion-cactinhnangchinh"></a>

Những tính năng chính dưới đây đóng góp vào tính ổn định, khả năng mở rộng và hoạt động hiệu quả của ứng dụng và dịch vụ bằng cách phân phối thông minh lưu lượng và đảm bảo khả dụng cao.

* **Phân phối Lưu lượng**

Load Balancer phân phối các yêu cầu đến máy chủ theo nhiều cách khác nhau, như round-robin (phân phối đều đặn) hoặc least connections (đến máy chủ ít kết nối nhất). Phân phối đồng đều này ngăn chặn một máy chủ duy nhất bị quá tải và đảm bảo sử dụng tài nguyên hiệu quả.

* **Cải thiện Hiệu suất**

Bằng cách chuyển hướng lưu lượng đến nhiều máy chủ, Load Balancer cải thiện thời gian phản hồi và ngăn chặn các điểm trở ngại, kết quả là cải thiện hiệu suất ứng dụng và trải nghiệm người dùng nhanh hơn.

* **Khả năng Mở rộng**

Load Balancer hỗ trợ mở rộng theo chiều ngang bằng cách thêm mới máy chủ thành viên vào nhóm máy chủ một cách mượt mà. Mở rộng linh hoạt này đảm bảo sử dụng tài nguyên hiệu quả trong thời kỳ đỉnh điểm.

* **Tính Khả dụng cao**

Load Balancer liên tục theo dõi tình trạng sức khỏe của máy chủ. Nếu một máy chủ không phản hồi, Load Balancer tự động chuyển hướng lưu lượng đến các máy chủ khỏe mạnh, đảm bảo dịch vụ không bị gián đoạn.

* **Kiểm tra Sức khỏe**

Load Balancer thực hiện kiểm tra sức khỏe định kỳ trên các máy chủ backend, xác minh tính sẵn sàng và khả năng phản hồi của chúng. Nếu một máy chủ không vượt qua kiểm tra này, nó sẽ tạm thời bị gỡ bỏ khỏi nhóm máy chủ.

* **Phân phối Dựa trên Thuật toán**

Load Balancer sử dụng các thuật toán như round-robin, least connections hoặc IP Source để phân phối lưu lượng một cách thông minh. Điều này tối ưu hóa việc phân chia tài nguyên dựa trên các yếu tố như khả năng máy chủ, thời gian phản hồi và tải máy chủ.

* **Duy trì Phiên**

Một số ứng dụng đòi hỏi trải nghiệm nhất quán của người dùng trong một phiên làm việc. Load Balancer có thể đảm bảo điều này bằng cách duy trì phiên của người dùng trên cùng một máy chủ trong suốt quá trình tương tác.

* **SSL/TLS Encryption**

Load Balancer có thể xử lý mã hóa và giải mã lưu lượng SSL/TLS, giảm bớt công việc tính toán từ các máy chủ backend và tăng cường hiệu suất tổng thể.

* **Chuyển hướng Nội dung (Host/Path-based routing)**

Load Balancer có thể chuyển hướng lưu lượng dựa trên Host, Path hoặc các tiêu chí khác cụ thể cho ứng dụng. Điều này đảm bảo rằng các yêu cầu được chuyển hướng đến máy chủ phù hợp nhất dựa trên tính chất của yêu cầu.

* **Quản lý Tập trung**

Dịch vụ Load Balancer cung cấp giao diện quản lý tập trung cho phép quản trị viên cấu hình và giám sát nhiều trường hợp Load Balancer từ một vị trí duy nhất, đơn giản hóa các nhiệm vụ quản lý.

* **Giám sát Lưu lượng và Phân tích**

Load Balancer cung cấp thông tin về mẫu lưu lượng, hiệu suất máy chủ và hành vi người dùng thông qua số liệu, nhật ký và phân tích, giúp quản trị viên tối ưu hóa phân bổ tài nguyên và khắc phục sự cố

#### Các chủ đề liên quan <a href="#vlb-loadbalancer-newversion-cacchudelienquan" id="vlb-loadbalancer-newversion-cacchudelienquan"></a>

Cùng tìm hiểu thêm về cách hoạt động của như các hướng dẫn sử dụng dịch vụ chi tiết thông qua các bài viết dưới đây

