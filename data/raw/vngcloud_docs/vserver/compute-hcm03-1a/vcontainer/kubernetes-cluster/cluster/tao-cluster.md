# Tạo Cluster

Chủ đề này cung cấp thông tin tổng quan về các tùy chọn khả dụng và mô tả những điều cần xem xét khi bạn tạo Kubernetes Cluster (K8S). Nếu đây là lần đầu tiên bạn tạo K8S, chúng tôi khuyên bạn nên làm theo hướng dẫn sau đây của chúng tôi. Hướng dẫn này giúp bạn tạo một Kubernetes Cluster mặc định, đơn giản mà không cần mở rộng thành tất cả các tùy chọn có sẵn.

***

### **Điều kiện tiên quyết** <a href="#taocluster-dieukientienquyet" id="taocluster-dieukientienquyet"></a>

* Một VPC hiện có và các Subnet đáp ứng các yêu cầu của K8S. Trước khi bạn triển khai một Cluster để sử dụng trong sản xuất, chúng tôi khuyên bạn nên hiểu rõ về VPC và các yêu cầu Subnet. Nếu không có VPC và Subnet, bạn có thể tạo chúng trên giao diện của vServer.
* Công cụ dòng lệnh kubectl được cài đặt trên thiết bị của bạn. Phiên bản có thể giống hoặc tối đa một phiên bản nhỏ sớm hơn hoặc muộn hơn phiên bản Kubernetes của Cluster của bạn. Ví dụ: nếu phiên bản Cluster của bạn là 1.23.16, thì bạn có thể sử dụng phiên bản kubectl 1.22, 1.23 hoặc 1.24 cùng với phiên bản đó.
* Nếu bạn đang sử dụng Kubernetes Cluster trong lớp mạng pfsense hay Fortigate, bạn cần Config MTU cho các loại FW về 1450 theo hướng dẫn [MTU và “DF flag” best practice on VNG Cloud](broken-reference).
* Tài khoản IAM chính có quyền tạo và mô tả K8S. Để biết thêm thông tin, hãy xem phần [Phân quyền IAM cho vServer](../../../quan-ly-dinh-danh-va-truy-cap-iam-cho-vserver/cac-hanh-dong-tai-nguyen-va-dieu-kien-can-cho-phan-quyen-truy-cap-vserver.md).

***

### **Tạo Kubernetes Cluster** <a href="#taocluster-taokubernetescluster" id="taocluster-taokubernetescluster"></a>

**Quyền tối thiểu**

Để tạo Kubernetes Cluster, bạn phải có quyền IAM chạy các hành động sau:

* CreateCluster
* GetCluster (specify by all resources)
* ListClusterSecGroupDefault (specify by all resources)\
  GetClusterConfig (specify by all resources)

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster).
2. Chọn tạo **Kubernetes Cluster**
3. Tại trang **cài đặt thông số cấu hình cơ bản Cluster**, hãy nhập các trường thông tin sau:
   * **Name** – A name for your cluster. It must be unique in your AWS account. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you're creating the cluster in.
   * **Tên** – Tên cho Cluster của bạn. Nó phải là duy nhất trong tài khoản VNG Cloud của bạn. Tên chỉ có thể chứa các ký tự chữ và số (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào của bạn phải từ 5 đến 50. Tên phải là duy nhất trong Khu vực và tài khoản VNG Cloud mà bạn đang tạo Cluster.
   * **Phiên bản Kubernetes** – Phiên bản Kubernetes sẽ sử dụng cho Cluster của bạn. Chúng tôi khuyên bạn nên chọn phiên bản mới nhất, trừ khi bạn cần phiên bản cũ hơn.
   * **Mô tả** – Nhập vào thông tin bạn muốn ghi chú cho Cluster nhằm tạo dấu hiệu riêng cho việc quản lý chúng dễ dàng hơn trong tương lai.
   * **Tùy chọn nâng cao:** Bạn có thể tùy chọn bật **HA, Auto Healing, Auto Healing, Ingress Control, Auto Scaling Minion** tùy theo nhu cầu sử dụng, để xem thông tin chi tiết và ý nghĩa các tùy chọn vui lòng xem tại [Bật Highly Available](bat-highly-available-cho-cluster.md)
   * **Số lượng Master nodes** – Nhập vào số lượng Master node cho Cluster của mình, lưu ý với non-HA (Highly available) bạn cần nhập số lượng 1 node và HA số lượng là 3 hoặc 5 nodes.
   * **Số lượng Minion nodes** – Nhập vào số lượng Minion node cho Cluster của mình, lưu ý số lượng node cần lớn hơn hoặc bằng 1 và nhỏ hơn hoặc bằng 10.
4. Kéo xuống dưới, bạn sẽ thấy mục **Cấu hình bộ lưu trữ ETCD:**
   * **Thông tin bộ lưu trữ ETCD** – Chọn cấu hình lưu trữ ETCD cho Cluster của bạn theo gói **Small** hoặc **Medium.**
5. Tại mục **Instance type** chọn loại phiên bản cấu hình phù hợp cho Master node và Minion node theo nhu cầu sử dụng của bạn.
6. Thiết lập các ổ đĩa cho Kubernetes cluster tại mục **Cài đặt Volume:**
   * **Cấu hình Boot Volume** – Các thông số được cài đặt mặc định bởi hệ thống giúp tối ưu cho Cluster của bạn
   * **Cấu hình Docker Volume** – Chọn thông số kích thước và loại ổ đĩa phù hợp với nhu cầu sử dụng, kích thước của Data Disk phải lớn hơn hoặc bằng 20 GB và không vượt quá 4000 GB.
7. Tại mục **Cài đặt Network**, hãy chọn giá trị cho các trường sau:
   * **VPC** – Chọn một VPC hiện có đáp ứng các yêu cầu của K8S để tạo Cluster của bạn. Trước khi chọn một VPC, chúng tôi khuyên bạn nên làm quen với tất cả các yêu cầu và cân nhắc trong VPC cũng như các yêu cầu và cân nhắc về Subnet. Bạn không thể thay đổi VPC nào bạn muốn sử dụng sau khi tạo Cluster. Nếu không có VPC nào được liệt kê, trước tiên bạn cần tạo một VPC. Để biết thêm thông tin, hãy xem [**Tạo VPC**](../../../network/virtual-private-cloud-vpc/)**.**
   * **Loại Network, Chế độ Encapsulation** được tự chọn mặc định bởi hệ thống và bạn không thể thay đổi chúng, tuy nhiên bạn có thể nhập lại thông số **Calico CIDR** (lưu ý IP phải là riêng tư và có thể chọn theo các tùy chọn sau (10.0.0.0 - 10.255.0.0 / 172.16.0.0 - 172.24.0.0 / 192.168.0.0)
   * **Subnets** – Theo mặc định, tất cả các mạng con khả dụng trong VPC được chỉ định trong trường trước đó sẽ được chọn ngẫu nhiên ở thứ tự đầu tiên, bạn có thể chọn lại Subnet khác, tuy nhiên chỉ được chọn duy nhất 1.
   * SSH keys - để Import vô Kubernetes trong quá trình khởi tạo (Nhấp vào [**đây**](../../../security/ssh-key-bo-khoa.md) để xem hướng dẫn tạo SSH Key)
8. Sau khi điền các thông tin cần thiết để khởi tạo K8S, cần xem lại tóm tắt các thông tin thanh toán tại tab **Summary** phía bên trái màn hình và thông tin thanh toán chi tiết các mục tại tab **Item list,** nếu cần hay thực hiện thay đổ&#x69;**.** Khi bạn đã hài lòng hãy chọn **Tạo Kubernetes Cluster** để xác nhận khởi tạo Cluster của bạn. Trường Trạng thái hiển thị **Creating** khi Cluster được cung cấp.
