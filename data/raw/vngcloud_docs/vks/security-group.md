# Security Group

Security Group đóng vai trò như một firewall giúp bạn kiểm soát lưu lượng truy cập ra vào máy chủ (VM). Trên hệ thống VKS, để đảm bảo cluster hoạt động an toàn và hiệu quả, các Security Group mặc định được thiết lập để cho phép các truy cập cần thiết cho hoạt động nội bộ của cluster. Việc tự động tạo Security Group giúp đơn giản hóa quá trình triển khai cluster và đảm bảo rằng cluster được bảo vệ ngay từ đầu. Cụ thể, khi bạn thực hiện khởi tạo một Cluser, chúng tôi sẽ tự động khởi tạo một vài Security Group với các thông số như sau:&#x20;

### Security group mặc định được tạo tự động cho tất cả Cluster

Mỗi Cluster được tạo ra trong hệ thống VKS, chúng tôi sẽ tự động tạo một Security Group. Security group này sẽ bao gồm:

* Inbound:

<table><thead><tr><th width="114">Protocol</th><th width="83">Ether type</th><th width="140">Port range</th><th width="215">Source</th><th>Ý nghĩa</th></tr></thead><tbody><tr><td>TCP</td><td>IPv4</td><td>30000-32767</td><td>CIDR của VPC mà bạn sử dụng cho Cluster.</td><td>Security group rule sử dụng cho TCP Node Port Services</td></tr><tr><td>UDP</td><td>IPv4</td><td>30000-32767</td><td>CIDR của VPC mà bạn sử dụng cho Cluster.</td><td>Security group rule sử dụng cho UDP Node Port Services</td></tr><tr><td>TCP</td><td>IPv4</td><td>10250</td><td>External IP của Load Balancer sử dụng cho Cluster.</td><td>Security group rule sử dụng cho Kubelet API control-plane</td></tr><tr><td>TCP</td><td>IPv4</td><td>10250</td><td>CIDR của VPC mà bạn sử dụng cho Cluster.</td><td>Security group rule sử dụng cho Kubelet API control-plane</td></tr><tr><td>TCP</td><td>IPv4</td><td>179</td><td>CIDR của VPC mà bạn sử dụng cho Cluster.</td><td>Security group rule sử dụng cho Kubelet API control-plane</td></tr><tr><td>4</td><td>IPv4</td><td>1-65535</td><td>CIDR của VPC mà bạn sử dụng cho Cluster.</td><td>Security group rule sử dụng cho Calico IP-in-IP</td></tr><tr><td>TCP</td><td>IPv4</td><td>5473</td><td>CIDR của VPC mà bạn sử dụng cho Cluster.</td><td>Security group rule sử dụng cho Calico Typha</td></tr></tbody></table>

* Outbound

<table><thead><tr><th width="114">Protocol</th><th width="131">Ether type</th><th width="126">Port range</th><th width="125">Destination</th><th>Ý nghĩa</th></tr></thead><tbody><tr><td>ANY</td><td>IPv4</td><td>0-65535</td><td>0.0.0.0/0</td><td>Rule mặc định của tất cả Security group</td></tr><tr><td>ANY</td><td>IPv6</td><td>0-65535</td><td>::/0</td><td>Rule mặc định của tất cả Security group</td></tr></tbody></table>

### Security group được tạo tự động bởi VNGCLOUD LoadBalancer Controller&#x20;

Khi bạn sử dụng VNGCloud LoadBalancer Controller để tích hợp Network Load Balancer với Cluster trên hệ thống VKS, chúng tôi sẽ tự động tạo một Security Group. Security group này sẽ bao gồm:

* Inbound:

<table><thead><tr><th width="207">Protocol</th><th width="108">Ether type</th><th>Port range</th><th>Source</th></tr></thead><tbody><tr><td>TCP, UDP hoặc ICMP</td><td>IPv4</td><td>Port của Service</td><td>Subnet Mask của Subnet mà bạn sử dụng cho Cluster.</td></tr></tbody></table>

* Outbound:

<table><thead><tr><th width="113">Protocol</th><th width="115">Ether type</th><th width="126">Port range</th><th width="127">Destination</th><th>Ý nghĩa</th></tr></thead><tbody><tr><td>ANY</td><td>IPv4</td><td>0-65535</td><td>0.0.0.0/0</td><td>Rule mặc định của tất cả Security group</td></tr><tr><td>ANY</td><td>IPv6</td><td>0-65535</td><td>::/0</td><td>Rule mặc định của tất cả Security group</td></tr></tbody></table>

### Security group được tạo tự động bởi VNGCLOUD Ingress Controller

Khi bạn sử dụng VNGCloud Ingress Controller để tích hợp Application Load Balancer với Cluster trên hệ thống VKS, chúng tôi sẽ tự động tạo một Security Group. Security group này sẽ bao gồm:

* Inbound:

<table><thead><tr><th width="141">Protocol</th><th width="117">Ether type</th><th>Port range</th><th>Source</th></tr></thead><tbody><tr><td>TCP</td><td>IPv4</td><td>Port của Service</td><td>Subnet Mask của Subnet mà bạn sử dụng cho Cluster.</td></tr></tbody></table>

* Outbound:

<table><thead><tr><th width="105">Protocol</th><th width="109">Ether type</th><th width="122">Port range</th><th width="162">Destination</th><th>Ý nghĩa</th></tr></thead><tbody><tr><td>ANY</td><td>IPv4</td><td>0-65535</td><td>0.0.0.0/0</td><td>Rule mặc định của tất cả Security group</td></tr><tr><td>ANY</td><td>IPv6</td><td>0-65535</td><td>::/0</td><td>Rule mặc định của tất cả Security group</td></tr></tbody></table>

{% hint style="info" %}
**Chú ý:**

* Các Security Group mặc định được thiết lập để đáp ứng các nhu cầu bảo mật cơ bản của cluster. Nếu bạn sửa hoặc xóa các Security Group được tạo sẵn cho cluster, có thể dẫn đến các vấn đề về kết nối và truy cập giữa các node trong cluster hoặc cluster có thể không hoạt động chính xác hoặc thậm chí không thể khởi động được. Để đảm bảo tính ổn định và bảo mật của cluster, hệ thống sẽ tự động reset các Security Group về cài đặt mặc định sau mỗi khoảng thời gian cố định.
{% endhint %}
