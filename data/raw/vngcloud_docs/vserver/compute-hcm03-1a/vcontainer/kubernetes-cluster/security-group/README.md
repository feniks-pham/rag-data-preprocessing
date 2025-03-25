# Security Group

Bảo mật đám mây tại VNG là ưu tiên cao nhất. Là khách hàng của VNG, bạn được hưởng lợi từ trung tâm dữ liệu và kiến trúc mạng được xây dựng để đáp ứng yêu cầu của các tổ chức nhạy cảm nhất về bảo mật.

VNG Cloud chịu trách nhiệm bảo vệ cơ sở hạ tầng chạy các dịch vụ Kubernetes Cluster trong Đám mây VNG. Đối với Kubernetes Cluster, VNG Cloud chịu trách nhiệm về quản lý Kubernetes, bao gồm control plane node và cơ sở dữ liệu etcd. Kiểm toán viên bên thứ ba thường xuyên kiểm tra và xác minh tính hiệu quả của bảo mật của chúng tôi như một phần của chương trình tuân thủ VNG Cloud.

Bảo mật trong đám mây – Trách nhiệm của bạn bao gồm các lĩnh vực sau.

* Cấu hình bảo mật của mặt phẳng dữ liệu, bao gồm cấu hình của các nhóm bảo mật cho phép lưu lượng truyền từ mặt phẳng điều khiển Kubernetes Cluster vào VPC của khách hàng
* Bản thân cấu hình của các nút và vùng chứa
* Hệ điều hành của Node (bao gồm các bản cập nhật và bản vá bảo mật)
* Các phần mềm ứng dụng liên quan khác:
* Thiết lập và quản lý các điều khiển mạng, chẳng hạn như quy tắc tường lửa
* Quản lý danh tính cấp nền tảng và quản lý truy cập, có hoặc ngoài IAM
* Độ nhạy cảm của dữ liệu, yêu cầu của công ty bạn cũng như các luật và quy định hiện hành

Security Group được chia thành 2 loại: Bao gồm các Security được tạo mặc định bởi hệ thống khi bạn tạo mới Kubernetes Cluster và được tạo bởi người dùng, bạn có thể vào nhấn vào [Security Groups](https://docs.vngcloud.vn/display/vServer/Security+Groups?src=contextnavpagetreemode) để xem hướng dẫn cách tạo Security Groups. Trong ngữ cảnh của dịch vụ đám mây tại VNG Cloud, chúng tôi có 2 khái niệm chính là "Master node security group" và "Minion node Security Group" là  khái niệm liên quan đến quản lý bảo mật cho nhóm các máy chủ điều khiển (master nodes và minion nodes) trong một hệ thống phân tán như Kubernetes cluster.

Cụ thể, các hệ thống phân tán như Kubernetes có một tập hợp các máy chủ điều khiển (master nodes) chịu trách nhiệm quản lý và điều phối các minion nodes và các tác vụ trong cluster. Master nodes chứa các thành phần như kube-apiserver, kube-controller-manager và kube-scheduler. Để đảm bảo an toàn và bảo mật cho master nodes, ta cần cấu hình một "security group" đặc biệt, được gọi là "master node security group."

Một "security group" trong các dịch vụ đám mây trong VNG Cloud là một tập hợp các quy tắc bảo mật (firewall rules) xác định cách các instance hoặc máy chủ trong nhóm này có thể giao tiếp với nhau và với các nguồn tài nguyên bên ngoài mạng. Security group giúp kiểm soát lưu lượng mạng đến và từ các máy chủ, đảm bảo rằng chỉ các liên kết được xác định mới được phép.

Master node security group là một security group đặc biệt, chỉ áp dụng cho các master nodes trong Kubernetes cluster. Nó thường được cấu hình để cho phép các Minion nodes và các thành phần quan trọng khác trong cluster (như kubelet) kết nối và giao tiếp với các master nodes. Đồng thời, nó sẽ hạn chế các kết nối từ bên ngoài hoặc từ các nguồn không được xác định, nhằm bảo vệ master nodes khỏi các tấn công không mong muốn và xâm nhập.

Cấu hình master node security group và minion node security group là một phần quan trọng của việc bảo vệ và duy trì tính ổn định của Kubernetes cluster, đồng thời giúp bảo đảm rằng chỉ những người dùng và máy chủ được ủy quyền mới có thể truy cập và tương tác với master nodes và minion nodes.

***

#### Chủ đề <a href="#securitygroup-chude" id="securitygroup-chude"></a>

* [Cập nhật Master security group](cap-nhat-master-security-group.md)
* [Cập nhật Minion security group](cap-nhat-minion-security-group.md)

\
