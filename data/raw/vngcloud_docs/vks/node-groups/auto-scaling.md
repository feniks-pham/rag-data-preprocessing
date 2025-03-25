# Auto Scaling

### Tổng quan

Auto Scaling cho Cluster là một tính năng trong Kubernetes cho phép tự động điều chỉnh kích thước của cụm (Cluster) cụ thể là số lượng các node trong cụm để đáp ứng nhu cầu sử dụng.&#x20;

Tính năng Auto Scaling có những điểm nổi bật sau:

1. **Tối ưu hóa hiệu suất:** Auto Scaling cho phép cụm tự động mở rộng tài nguyên khi có nhu cầu. Khi khối lượng công việc cao hơn, cụm sẽ tự động tạo thêm các node để đảm bảo các ứng dụng hoạt động với hiệu suất tốt nhất.
2. **Tiết kiệm chi phí:** Auto Scaling cho phép cụm tự động giảm tài nguyên khi không cần thiết. Nếu khối lượng công việc giảm đi, cụm sẽ tự động thu hồi các tài nguyên không sử dụng để tiết kiệm chi phí.
3. **Đảm bảo tính sẵn sàng:** Auto Scaling giúp đảm bảo rằng cụm có sẵn để đáp ứng nhu cầu sử dụng và tránh tình trạng quá tải hoặc thiếu tài nguyên.
4. **Tự động phục hồi:** Auto Scaling giúp tự động phục hồi từ các sự cố hoặc lỗi bằng cách tạo ra các node mới để thay thế các node bị hỏng.

Khi triển khai các ứng dụng trong môi trường cloud, việc sử dụng tính năng Auto Scaling giúp tối ưu hóa việc sử dụng tài nguyên, cải thiện tính sẵn sàng và hiệu suất của ứng dụng, và giúp quản lý cụm trở nên dễ dàng và hiệu quả hơn.

***

### Cơ chế hoạt động

#### Cơ chế Scale up: hệ thống VKS thực hiện scale up khi

* Các pods không thể scheduling trên bất kỳ node hiện tại nào vì lý do thiếu resource.
* Việc tăng thêm 1 node giống với cấu hình node group hiện tại là hữu ích và có thể xử lý vấn đề thiếu resource này.

Minh họa:

<figure><img src="../../.gitbook/assets/image%20(177).png" alt=""><figcaption></figcaption></figure>

Nếu thỏa mãn 2 điều kiện trên, hệ thống sẽ tăng số node (một hoặc nhiều nodes) để đáp ứng toàn bộ pods đang unscheduling. Quá trình này sẽ được thực hiện ngay lập tức theo 2 bước:

* **Bước 1:** Hệ thống VKS tạo node mới theo cấu hình node group hiện tại.
* **Bước 2:** Hệ thống VKS sẽ deploy các pods đang unscheduling này lên các node mới.

{% hint style="info" %}
**Chú ý:**

* Khi hệ thống thực hiện Auto Scaling, việc tạo ra node mới có thể gặp lỗi nếu bạn không có đủ credit hoặc bạn đã hết quota để tạo VM trên hệ thống vServer. Để tránh gặp lỗi bên trên, bạn cần:
  * **Đảm bảo bạn có đủ credit:** Nếu bạn là người dùng trả trước, hãy nạp thêm credit vào tài khoản của bạn.
  * **Yêu cầu tăng quota:** Bạn có thể yêu cầu tăng quota cho tài khoản của mình tại [đây](https://hcm-3.console.vngcloud.vn/vserver/limit).
{% endhint %}

#### Cơ chế Scale down: hệ thống VKS thực hiện scale down khi

* Một hoặc nhiều node có tải thấp liên tục trong một khoảng thời gian. Cụ thể node có utilization (độ khả dụng) bao gồm cả request CPU và memory của pod thấp ở mức <mark style="color:red;">**< 50%.**</mark>
* Tất cả các pod hiện tại của node đó, có thể được di chuyển qua node khác mà không gặp vấn đề gì.

Nếu thỏa mãn 2 điều kiện trên, mặc định là trong khoảng 10 phút, node đó sẽ bị xóa đi khỏi Cluster. Quá trình xóa này sẽ bao gồm 3 bước:

* **Bước 1:** Hệ thống VKS sẽ đánh dấu là node đó là unschedulable.
* **Bước 2:** Hệ thống di chuyển (move) toàn bộ pod qua node khác.
* **Bước 3:** Sau khi di chuyển tất cả các pod qua node khác thành công, hệ thống VKS sẽ xóa node được đánh dấu.

***

### **Bật Auto Scaling** <a href="#autoscaling-batautoscaling" id="autoscaling-batautoscaling"></a>

Trên hệ thống VKS, bạn có thể bật Auto Scaling khi:

* **Khởi tạo một Cluster**
* **Khởi tạo một Node Group**
* **Chỉnh sửa một Node Group**

Để bật Auto Scaling cho Kubernetes Cluster của bạn vui lòng bật lựa chọn **Enable Auto Scaling,** khi bật lựa chọn này bạn cần nhập:.

* **Minimum node**: số node tối thiểu mà Cluster phải có.&#x20;
* **Maximum node**: số node tối đa mà Cluster có thể scale tới.
* **Node Group upgrade stratetry**: chiến lược upgrade Node Group. Khi bạn thiết lập **Node Group Upgrade Strategy** thông qua phương thức **Surge upgrade** cho một Node Group trong VKS, hệ thống VKS sẽ cập nhật tuần tự để nâng cấp các node, theo thứ tự không xác định[.](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies.)&#x20;
  * **Max surge:** giới hạn số lượng node được nâng cấp đồng thời (số lượng node mới (surge) có thể được tạo ra cùng một lúc). Mặc định **Max surge = 1** - chỉ nâng cấp một node tại một thời điểm.&#x20;
  * **Max unavailable**: giới hạn số lượng node không thể truy cập được trong quá trình nâng cấp (số lượng node hiện tại có thể bị gián đoạn cùng một lúc). Mặc định **Max unavailable = 0** - đảm bảo tất cả các node đều có thể truy cập được trong quá trình nâng cấp.

Ví dụ như hình bên dưới: tôi đã khởi tạo một Node Group với:

* **Number of nodes: 3 nodes**
* **Minimum node: 1 nodes**
* **Maximum node: 5 nodes**

Lúc này:&#x20;

* Nếu có một hoặc nhiều pod không thể scheduling trên bất kỳ node trên cụm vì lý do thiếu resource và việc thêm 1 node giống với cấu hình node group này có thể xử lý vấn đề thì hệ thống sẽ thực hiện scale up. Với thiết lập này thì hệ thống có thể scale up tối đa lên tới **5 node**.
* Nếu có 1 node có low utilization (khả dụng) thấp ở mức <mark style="color:red;">**< 50%**</mark> và tất cả các pod của node đó có thể scheduling trên node khác thì hệ thống sẽ thực hiện scale up. Với thiết lập này thì hệ thống có thể scale down xuống mức tối thiểu là **1 node.**

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/73762025/image2024-4-17_11-45-7.png?version=1&#x26;modificationDate=1713329108000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
