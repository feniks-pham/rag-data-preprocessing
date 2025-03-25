# Bật Ingress Control cho Cluster

**Ingress:** Ingress trong Kubernetes là một nguồn thông tin quy định cách dữ liệu từ bên ngoài được chuyển tiếp đến các dịch vụ (Service) bên trong cluster. Nó cung cấp một cách tiêu chuẩn để quản lý việc truy cập vào các dịch vụ của ứng dụng từ bên ngoài. Ingress định tuyến các yêu cầu HTTP và HTTPS đến các Service, giúp điều hướng lưu lượng mạng một cách hiệu quả trong cluster.

**LoadBalancer Controller:** LoadBalancer Controller là một thành phần của Kubernetes có nhiệm vụ thực hiện các quy tắc được định nghĩa trong Ingress và thực hiện việc chuyển tiếp các yêu cầu đến các Service tương ứng trong cluster. LoadBalancer Controller là một loại cụm (cluster) của riêng nó, chịu trách nhiệm quản lý và xử lý các yêu cầu từ bên ngoài và định tuyến chúng đến các Service thích hợp bên trong cụm.

"Ingress Control Clusters" là một kiến trúc hoặc cấu hình trong Kubernetes mà sử dụng một hoặc nhiều LoadBalancer Controllers để quản lý việc định tuyến và điều hướng lưu lượng mạng từ bên ngoài vào các dịch vụ trong cluster. Mục tiêu chính của Ingress Control Clusters là tạo một cơ chế tiêu chuẩn để điều hướng các yêu cầu HTTP/HTTPS đến các ứng dụng và dịch vụ trong môi trường Kubernetes một cách linh hoạt và hiệu quả.

Các đặc điểm và lợi ích của Ingress Control bao gồm:

1. **Quản lý định tuyến lưu lượng mạng:** Ingress Control Clusters cung cấp một cơ chế tiêu chuẩn để quản lý định tuyến lưu lượng mạng từ bên ngoài vào các dịch vụ và ứng dụng trong cluster Kubernetes. Thay vì mở cổng trực tiếp cho mỗi Service, Ingress cho phép bạn quản lý điều hướng yêu cầu HTTP và HTTPS một cách linh hoạt và dễ dàng.
2. **Tối ưu hóa việc truy cập ứng dụng:** Ingress Control Clusters cho phép bạn cấu hình các quy tắc định tuyến linh hoạt để điều hướng yêu cầu đến các dịch vụ và ứng dụng phù hợp bên trong cluster. Điều này giúp tối ưu hóa việc truy cập ứng dụng từ bên ngoài và cải thiện trải nghiệm người dùng.
3. **Hỗ trợ nhiều ứng dụng và miền:** Ingress Control Clusters cho phép bạn cấu hình nhiều Ingress để hỗ trợ nhiều ứng dụng và miền trong cùng một cluster Kubernetes. Bằng cách sử dụng một Ingress Controller duy nhất, bạn có thể quản lý các quy tắc điều hướng cho nhiều ứng dụng một cách hiệu quả.
4. **Tăng tính linh hoạt và thay đổi dễ dàng:** Ingress Control Clusters cho phép bạn thay đổi cấu hình định tuyến mà không cần thay đổi cấu hình của dịch vụ. Điều này giúp tăng tính linh hoạt và cho phép bạn thích ứng nhanh chóng với các yêu cầu mới.
5. **Bảo mật và quản lý truy cập:** Ingress Control Clusters cung cấp khả năng quản lý truy cập và bảo mật cho các ứng dụng và dịch vụ trong cluster. Bạn có thể cấu hình các quy tắc bảo mật, xác thực và kiểm soát truy cập để bảo vệ các ứng dụng và dịch vụ khỏi các cuộc tấn công.
6. **Khả năng tích hợp với các giải pháp bảo mật bên ngoài:** Ingress Control Clusters hỗ trợ tích hợp với các giải pháp bảo mật bên ngoài, như WAF (Web Application Firewall), để bảo vệ ứng dụng khỏi các cuộc tấn công web phức tạp và các lỗ hổng bảo mật.

\


***

### **Bật Ingress Control** <a href="#batingresscontrolchocluster-batingresscontrol" id="batingresscontrolchocluster-batingresscontrol"></a>

Để bật Ingress Control cho Kubernetes Cluster của bạn vui lòng chọn Bật Ingress Control ở mục Tùy chọn nâng cao tại màn hình tạo mới Kubernetes Cluster, bạn có thể xem quy trình khởi tạo Kubernetes Cluster tại [Bước 2: Khởi tạo dịch vụ K8S](../bat-dau-voi-kubernetes-cluster/buoc-2-khoi-tao-dich-vu-k8s.md)
