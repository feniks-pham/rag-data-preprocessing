# Clusters

**Cluster trong Kubernetes** là một tập hợp gồm một hoặc nhiều máy ảo (VM) được kết nối lại với nhau để chạy các ứng dụng được đóng gói dạng container. Cluster cung cấp một môi trường thống nhất để triển khai, quản lý và vận hành các container trên quy mô lớn.

### Điều kiện cần: <a href="#clusters-dieukiencan" id="clusters-dieukiencan"></a>

Để có thể khởi tạo một **Cluster** và **Deploy** một **Workload**, bạn cần:

* Có ít nhất 1 **VPC** và 1 **Subnet** đang ở trạng thái **ACTIVE**. Nếu bạn chưa có VPC, Subnet nào, vui lòng khởi tạo VPC, Subnet theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)&#x20;
* Có ít nhất 1 **SSH** key đang ở trạng thái **ACTIVE**. Nếu bạn chưa có SSH key nào, vui lòng khởi tạo SSH key theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/security/ssh-key-bo-khoa.md)
* Đã cài đặt và cấu hình **kubectl** trên thiết bị của bạn. vui lòng tham khảo tại [đây](https://kubernetes.io/vi/docs/tasks/tools/install-kubectl/) nếu bạn chưa rõ cách cài đặt và sử dụng kuberctl. Ngoài ra, bạn không nên sử dụng phiên bản kubectl quá cũ, chúng tôi khuyến cáo bạn nên sử dụng phiên bản kubectl sai lệch không quá một phiên bản với version của cluster.

***

### Khởi tạo Cluster <a href="#clusters-khoitaocluster" id="clusters-khoitaocluster"></a>

Để khởi tạo một Cluster, hãy làm theo các bước bên dưới:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn **Activate.**

**Bước 3:** Chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn. Sau khi Activate thành công, bạn hãy chọn **Create a Cluster.**

**Bước 4:** Tại màn hình khởi tạo Cluster, chúng tôi đã thiết lập thông tin cho Cluster và một **Default Node Group** cho bạn, bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Cluster và Node Group của bạn tại Cluster Configuration, Default Node Group Configuration, Plugin.&#x20;

* Cluster Configuration:
  * Cluster Information:&#x20;
    * **Cluster Name:** Tên cho Cluster của bạn. Tên chỉ có thể chứa các ký tự chữ và số (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào của bạn phải từ 5 đến 50. Tên phải là duy nhất trong Khu vực và tài khoản VNG Cloud mà bạn đang tạo Cluster.
    * **Kubernetes Version:** Phiên bản Kubernetes sẽ sử dụng cho Cluster của bạn. Chúng tôi khuyên bạn nên chọn phiên bản mới nhất, trừ khi bạn cần phiên bản cũ hơn.
    * **Description:** Nhập vào thông tin bạn muốn ghi chú cho Cluster nhằm tạo dấu hiệu riêng cho việc quản lý chúng dễ dàng hơn trong tương lai.
  * Network Setting:
    * **Network type:** lựa chọn loại network mà bạn mong muốn sử dụng cho Cluster của bạn. Hiện tại, VKS cung câp cho bạn chọn sử dụng 1 trong 3 loại network Calico Overlay, Cilium  Overlay, Cilium VPC Native Routing.
      * Đối với loại network Calico Overlay, Cilium Overlay, **Encapsulation Mode** được tự chọn mặc định bởi hệ thống và bạn không thể thay đổi chúng, tuy nhiên bạn có thể nhập lại thông số **Calico CIDR:** Dải mạng ảo mà các pod sẽ sử dụng (lưu ý IP phải là riêng tư và có thể chọn theo các tùy chọn sau (10.0.0.0 - 10.255.0.0 / 172.16.0.0 - 172.24.0.0 / 192.168.0.0)
      * Đối với loại network Cilium VPC Native Routing:
        * **Default Pod IP range** là dải địa chỉ IP thứ cấp được sử dụng cho các pod. Nó được gọi là **Secondary IP range** vì nó không trùng với dải IP chính của node (Primary IP range). Các pod trong Cluster sẽ được gán IP từ dải này. Bạn cần lựa chọn ít nhất 1 dải Secondary IP range đã tạo từ vServer.
        * **Node CIDR mask size:** Kích thước của CIDR dành cho các node. Thông số này cho biết mỗi node sẽ được gán bao nhiêu địa chỉ IP từ dải pod IP range. Kích thước này cần được chọn sao cho đảm bảo có đủ địa chỉ IP cho tất cả các pod trên mỗi node. Bạn có thể tham khảo bảng bên dưới để hiểu các tính số lượng IP có thể sử dụng để cấp phát cho node, pod trong cluster của bạn. Bạn cần lựa chọn một giá trị trong danh sách mà chúng tôi cung cấp phù hợp với nhu cầu của bạn.
    * **VPC:** Chọn một VPC hiện có đáp ứng các yêu cầu của K8S để tạo Cluster của bạn. Trước khi chọn một VPC, chúng tôi khuyên bạn nên làm quen với tất cả các yêu cầu và cân nhắc trong VPC cũng như các yêu cầu và cân nhắc về Subnet. Bạn không thể thay đổi VPC nào bạn muốn sử dụng sau khi tạo Cluster. Nếu không có VPC nào được liệt kê, trước tiên bạn cần tạo một VPC. Để biết thêm thông tin, hãy xem [**Tạo VPC**](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)**.**
    * **Subnet:** Theo mặc định, tất cả các mạng con khả dụng trong VPC được chỉ định trong trường trước đó sẽ được chọn ngẫu nhiên ở thứ tự đầu tiên, bạn có thể chọn lại Subnet khác, tuy nhiên chỉ được chọn duy nhất 1.
* Default Node group Configuration:
  * Node Group Information:
    * **Node Group Name**: Tên gợi nhớ cho Node Group của bạn.&#x20;
    * **Number of nodes:** Nhập vào số lượng Worker node cho Cluster của bạn, lưu ý số lượng node cần lớn hơn hoặc bằng 1 và nhỏ hơn hoặc bằng 100.
  * Node Group Automation Setting:
    * **Auto Healing:** Mặc định chúng tôi sẽ bật tính năng HA trong Cluster của bạn. Khi có node hoặc pod bị lỗi, Kubernetes sẽ tự động khởi động lại hoặc tạo mới pod để thay thế, đảm bảo ứng dụng của bạn luôn hoạt động mà không bị gián đoạn.
    * **Auto Scaling:** Bật tính năng tự động mở rộng trong Cluster của bạn. Auto scaling giúp tự động điều chỉnh số lượng pod (đơn vị triển khai ứng dụng) dựa trên nhu cầu sử dụng thực tế, tránh tình trạng lãng phí tài nguyên khi nhu cầu thấp hoặc quá tải khi nhu cầu cao.
      * **Minimum node**: số node tối thiểu mà Cluster cần có.
      * **Maximum node**: số node tối đa mà Cluster có thể scale tới.
    * Node Group upgrade stratetry: chiến lược upgrade Node Group. Khi bạn thiết lập **Node Group Upgrade Strategy** thông qua phương thức **Surge upgrade** cho một Node Group trong VKS, hệ thống VKS sẽ cập nhật tuần tự để nâng cấp các node, theo thứ tự không xác định[.](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies.)&#x20;
      * **Max surge:** giới hạn số lượng node được nâng cấp đồng thời (số lượng node mới (surge) có thể được tạo ra cùng một lúc). Mặc định **Max surge = 1** - chỉ nâng cấp một node tại một thời điểm. với maxUnavailable
      * **Max unavailable**: giới hạn số lượng node không thể truy cập được trong quá trình nâng cấp (số lượng node hiện tại có thể bị gián đoạn cùng một lúc). Mặc định **Max unavailable = 0** - đảm bảo tất cả các node đều có thể truy cập được trong quá trình nâng cấp.
  * Node Group Setting:
    * **Image**: mặc định chúng tôi cung cấp 1 loại Image là Ubuntu with containerd.
    * **Instance type**: chọn loại phiên bản cấu hình phù hợp cho Worker node theo nhu cầu sử dụng của bạn.
  * Node Group Volume Setting: **Cấu hình Boot Volume** – Các thông số được cài đặt mặc định bởi hệ thống giúp tối ưu cho Cluster của bạn
  * Node Group Network Setting: Bạn có thể lựa chọn **Public Node Group** hoặc **Private Node Group** tùy theo nhu cầu sử dụng Cluster của bạn.
  * Node Group Security Setting: Bạn có thể chọn **Security Group và SSH Key** cho Node Group của bạn.
  * Node Group Metadata Setting: Bạn có thể nhập **Metadata** tương ứng cho Node Group.
* Plugin
  * **Enable BlockStore Persistent Disk CSI Driver**: bật để chúng tôi tự động cài đặt CSI Controller trên Cluster của bạn.
  * **Enable vLB Native Integration Driver**: bật để chúng tôi tự động cài đặt LB Controller trên Cluster của bạn.

**Bước 5:** Chọn **Create Kubernetes cluster.** Hãy chờ vài phút để chúng tôi khởi tạo Cluster của bạn, trạng thái của Cluster lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Cluster** là **Active**, bạn có thể xem thông tin Cluster, thông tin Node Group bằng cách chọn vào Cluster Name tại cột **Name**.

***

### Tải xuống tệp tin Kube Config <a href="#clusters-taixuongteptinkubeconfig" id="clusters-taixuongteptinkubeconfig"></a>

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn menu **Kubernetes Cluster.**

**Bước 3:** Tại **Cluster** đã tạo thành công, chọn biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/71729305/image2024-4-16_16-41-12.png?version=1&#x26;modificationDate=1713260474000&#x26;api=v2" alt="" data-size="line">**và** chọn **Download Config File.**

**Bước 4:** File config sẽ được lưu về máy, lúc này bạn có thể sử dụng Kubectl để quản lý Cluster của bạn trên thiết bị cá nhân của mình.

***

### Xóa một Cluster <a href="#clusters-xoamotcluster" id="clusters-xoamotcluster"></a>

{% hint style="info" %}
Chú ý:

**Khi không còn nhu cầu sử dụng Kubernetes Cluster, bạn nên xóa các tài nguyên được liên kết với cụm đó để không phải chịu bất kỳ chi phí không cần thiết nào. Khi xoá Kubernetes Cluster các tài nguyên sau sẽ bị xóa:**

* Control Plane Resource của Cluster.
* Tất cả các node có trong Cluster (VM)
* Tất cả các Pod nào đang chạy trên các node.
* Security Group mặc định tạo cho Cluster đó.
* Load Balancer mặc định tạo cho Cluster đó.
* ETCD.

**Hệ thống có thể không xóa các tài nguyên sau:**

* Load Balancer được integrated vào Cluster bởi bạn.
* Persistent Volume được integrated vào Cluster bởi bạn.
{% endhint %}

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn menu **Kubernetes Cluster.**

**Bước 3:** Tại **Cluster** đã tạo thành công, chọn cluster muốn xóa và chọn **Delete**

**Bước 4:** Chọn **Delete** để xóa hoàn toàn Cluster của bạn.
