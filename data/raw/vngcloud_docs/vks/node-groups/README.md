# Node Groups

Node Group là một khái niệm quan trọng trong Kubernetes, dùng để quản lý nhóm các **node** (VM) có cùng chung cấu hình trong một cluster. Đối với một Node Group, bạn có thể:

### Tạo một Node Group <a href="#nodegroups-taomotnodegroup" id="nodegroups-taomotnodegroup"></a>

Để khởi tạo một Node Group, hãy làm theo các bước bên dưới:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại Cluster đã khởi tạo trước đó, hãy chọn **Create a Node group.**

**Bước 3:** Tại màn hình khởi tạo Node Group, chúng tôi đã thiết lập thông tin cho Node Group của bạn. Bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Node Group của bạn tại:

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

**Bước 5:** Chọn **Create Node Group.** Hãy chờ vài phút để chúng tôi khởi tạo Node Group của bạn, trạng thái của Node Group lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Node Group** là **Active**, bạn có thể xem thông tin Node Group bằng cách chọn vào **Node Group Name** tại màn hình chính.

***

### Chỉnh sửa một Node Group <a href="#nodegroups-chinhsuamotnodegroup" id="nodegroups-chinhsuamotnodegroup"></a>

**Đối với Node Group, bạn có thể chỉnh sửa các thông số: Number of Nodes, Auto Scaling, Upgrade Strategy, Security Group trong từng lần chỉnh sửa riêng biệt**. Cụ thể, bạn có thể thực hiện theo các bước sau đây:&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại Cluster đã khởi tạo trước đó, hãy chọn **vào Cluster bạn muốn chỉnh sửa Node group.**

**Bước 3:** Tại màn hình chứa danh sách Node Group đang có, tại Node Group bạn muốn chỉnh sửa chọn một trong các phương án:&#x20;

* Tính năng **Resize:** bạn có thể thay đổi\

  * Number of nodes:  Nhập vào số lượng Worker node cho Cluster của bạn, lưu ý số lượng node cần lớn hơn hoặc bằng 1 và nhỏ hơn hoặc bằng 100.
* Tính năng **Edit Auto Scaling:** bạn có thể thay đổi\

  * Auto Scaling: Bật tính năng tự động mở rộng trong Cluster của bạn. Auto scaling giúp tự động điều chỉnh số lượng pod (đơn vị triển khai ứng dụng) dựa trên nhu cầu sử dụng thực tế, tránh tình trạng lãng phí tài nguyên khi nhu cầu thấp hoặc quá tải khi nhu cầu cao.
    * Minimum node: số node tối thiểu mà Cluster cần có.
    * Maximum node: số node tối đa mà Cluster có thể scale tới.
* Tính năng **Edit Upgrade Stratetry:** bạn có thể thay đổi
  * Node Group upgrade stratetry: chiến lược upgrade Node Group. Khi bạn thiết lập Node Group Upgrade Strategy thông qua phương thức Surge upgrade cho một Node Group trong VKS, hệ thống VKS sẽ cập nhật tuần tự để nâng cấp các node, theo thứ tự không xác định[.](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies.)&#x20;
    * Max surge: giới hạn số lượng node được nâng cấp đồng thời (số lượng node mới (surge) có thể được tạo ra cùng một lúc). Mặc định Max surge = 1 - chỉ nâng cấp một node tại một thời điểm. với maxUnavailable
    * Max unavailable: giới hạn số lượng node không thể truy cập được trong quá trình nâng cấp (số lượng node hiện tại có thể bị gián đoạn cùng một lúc). Mặc định Max unavailable = 0 - đảm bảo tất cả các node đều có thể truy cập được trong quá trình nâng cấp.
* Tính năng **Edit Security Group:** bạn có thể thay đổi
  * Node Group Security Setting: Bạn có thể chọn Security Group và SSH Key cho Node Group của bạn.

***

### Xóa một Node Group <a href="#nodegroups-xoamotnodegroup" id="nodegroups-xoamotnodegroup"></a>

{% hint style="info" %}
**Chú ý:**

Khi không còn nhu cầu sử dụng Node Group, bạn hãy thực hiện xóa chúng để tiết kiệm chi phí.  Khi xoá Node Group, các tài nguyên sau sẽ bị xóa:

* Tất cả các node có trong Node Group (VM)
{% endhint %}

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn menu **Kubernetes Cluster.**

**Bước 3:** Tại **Cluster** đã tạo thành công, chọn Node Group bạn muốn xóa và chọn **Delete.**

**Bước 4:** Chọn **Delete** để xóa hoàn toàn **Node Group** của bạn.
