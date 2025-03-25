# Kubernetes Cluster

### **Tổng quan** <a href="#kubernetescluster-tongquan" id="kubernetescluster-tongquan"></a>

Kubernetes Cluster là một hệ thống phân tán bao gồm nhiều Cluster làm việc cùng nhau để quản lý và triển khai các ứng dụng container sử dụng Kubernetes. Kubernetes là một nền tảng mã nguồn mở được phát triển bởi Google, được sử dụng rộng rãi để quản lý và triển khai các ứng dụng container trên môi trường phân tán.

Một Kubernetes Cluster bao gồm các thành phần chính sau:

1. **Master Node:** Master node là trung tâm điều khiển của Kubernetes cluster. Nó quản lý và giám sát toàn bộ hệ thống. Master node chứa các thành phần sau:
   * **API Server:** API Server là trung tâm giao tiếp của toàn bộ hệ thống. Nó cung cấp các giao diện API để tương tác với Kubernetes cluster, cho phép bạn thao tác bằng dòng lệnh kubectl hoặc các công cụ quản lý khác.
   * **Scheduler:** Scheduler là thành phần quản lý việc lập lịch triển khai các Pod (nhóm các container liên quan đến nhau) lên các node của cluster. Nhiệm vụ của nó là tìm node phù hợp và phân phối các Pod vào node đó.
   * **LoadBalancer Controller:** LoadBalancer Controller điều khiển các thành phần của hệ thống, đảm bảo trạng thái thực tế của cluster tương thích với trạng thái mong muốn. Ví dụ, Replication Controller đảm bảo số lượng Pod được định nghĩa của một ứng dụng luôn được duy trì.
   * **ETCD:** ETCD là cơ sở dữ liệu phân tán chịu trách nhiệm lưu trữ trạng thái của toàn bộ cluster, bao gồm cấu hình, trạng thái của các Pods và các đối tượng khác.
2. **Minion (Node/Worker Node):** Minion là các máy tính thành viên trong cluster, nơi các ứng dụng và dịch vụ Kubernetes thực sự được triển khai và chạy. Minion chứa các thành phần sau:
   * **Kubelet:** Kubelet là thành phần chạy trên mỗi minion, quản lý các container và Pod trên node đó. Nó liên lạc với API Server để báo cáo trạng thái của node và nhận các yêu cầu triển khai Pod.
   * **Kube-proxy:** Kube-proxy là proxy mạng chịu trách nhiệm cung cấp kết nối mạng đến các Pod. Nó hỗ trợ chia sẻ IP và cân bằng tải giữa các Pod.
   * **Container Runtime:** Container Runtime (ví dụ như Docker, containerd, CRI-O) là công cụ quản lý và chạy các container trên node. Nó được sử dụng để tạo và quản lý các container mà các Pod chạy trong đó.
3. **Pod**: Là đơn vị nhỏ nhất trong Kubernetes, chứa một hoặc nhiều container chia sẻ tài nguyên mạng và lưu trữ. Mỗi Pod có địa chỉ IP duy nhất và được lên lịch triển khai trên các Worker Node.
4. **Service**: Đại diện cho một tập hợp các Pod, cung cấp một địa chỉ IP và tên miền duy nhất cho việc truy cập từ bên ngoài vào các Pod. Service giúp đảm bảo khả năng mở rộng và quản lý các ứng dụng trong Kubernetes Cluster.
5. **Volume**: Lưu trữ dữ liệu cho các container trong Kubernetes. Cung cấp tính năng khối lượng dữ liệu độc lập với Pod, đảm bảo dữ liệu không bị mất khi Pod bị lỗi hoặc tái tạo.

Khi triển khai ứng dụng trong Kubernetes Cluster, người dùng chỉ cần tạo các đối tượng như Pod, Service và Volume thông qua trình giao diện điều khiển hoặc Terraform. Hệ thống Kubernetes sẽ tự động xác định và phân phối các Pod đến các Minion Node khả dụng, đảm bảo tính sẵn sàng và khả năng mở rộng của ứng dụng.

***

### **Cách sử dụng Kubernetes Cluster** <a href="#kubernetescluster-cachsudungkubernetescluster" id="kubernetescluster-cachsudungkubernetescluster"></a>

Để sử dụng Kubernetes cluster, bạn có thể làm như sau:

1. **Triển khai ứng dụng:** Kubernetes cluster cho phép bạn triển khai các ứng dụng và dịch vụ trong các container. Bằng cách sử dụng các tệp cấu hình và tài nguyên, bạn có thể định nghĩa và triển khai các ứng dụng của mình trên cluster.
2. **Quản lý tài nguyên:** Kubernetes cluster giúp quản lý và phân phối tài nguyên giữa các container trên các Minion Node. Bạn có thể xác định yêu cầu tài nguyên cho mỗi ứng dụng và Kubernetes sẽ đảm bảo rằng tài nguyên đó được phân phối và sử dụng hiệu quả.
3. **Tự động mở rộng:** Với Kubernetes cluster, bạn có thể tự động mở rộng các ứng dụng dựa trên tải công việc. Khi tải tăng lên, Kubernetes có thể tự động triển khai thêm các bản sao của ứng dụng trên các Worker Node để đáp ứng nhu cầu tải.
4. **Quản lý phiên bản:** Kubernetes cluster cho phép quản lý các phiên bản của ứng dụng dễ dàng. Bạn có thể cập nhật, triển khai và quản lý các phiên bản mới của ứng dụng một cách linh hoạt và không gây gián đoạn đến ứng dụng đang chạy.
5. **Giám sát và khắc phục sự cố:** Kubernetes cung cấp các công cụ giám sát tích hợp để theo dõi sức khỏe và hiệu suất của các ứng dụng trong cluster. Nó cũng hỗ trợ việc khắc phục sự cố tự động bằng cách tự động khởi động lại container hoặc triển khai lại ứng dụng khi cần thiết.

Sử dụng Kubernetes cluster giúp đơn giản hóa việc triển khai và quản lý các ứng dụng container, tăng tính sẵn sàng và khả năng mở rộng của hệ thống, và giảm thiểu thời gian và công sức trong việc quản lý các tác vụ liên quan đến việc triển khai ứng dụng. Ngoài ra, người dùng có thể tận dụng khả năng mở rộng linh hoạt, quản lý hiệu suất và tự động hóa trong triển khai và quản lý ứng dụng container phân tán.

_**Xem hướng dẫn khởi tạo Kubernetes Cluster nhanh chóng với vServer tại đây:**_

{% embed url="https://youtu.be/pbd25lc1H00" %}
