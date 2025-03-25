# Auto Healing

### Tổng quan

Trên hệ thống VKS, tính năng Auto Healing được apply cho mỗi Node Group và luôn luôn ở trạng thái bật. Việc bật tính năng tự phục hồi (self-healing) trong Kubernetes mang lại nhiều lợi ích quan trọng, giúp đảm bảo tính sẵn sàng và độ tin cậy cao cho ứng dụng của bạn.&#x20;

Tính năng Auto Healing có những điểm nổi bật sau:

* **Tự động phát hiện lỗi:** Kubernetes có thể tự động phát hiện các node bị lỗi hoặc gặp sự cố thông qua việc theo dõi trạng thái của các node. Một số dấu hiệu cho thấy node bị lỗi bao gồm: node báo cáo trạng thái "NotReady", node không thể ping được, node bị lỗi phần cứng, v.v.
* **Tự động khởi động lại node:** Khi một node bị phát hiện lỗi, Kubernetes sẽ tự động khởi động lại node. Việc khởi động lại node có thể giúp khắc phục các lỗi tạm thời và đưa node trở lại trạng thái hoạt động bình thường.
* **Giảm thiểu sự can thiệp thủ công:** Auto Healing giúp giảm thiểu sự can thiệp thủ công của người quản trị viên hệ thống, tiết kiệm thời gian và công sức.
* **Cải thiện hiệu quả hoạt động:** Auto Healing giúp cải thiện hiệu quả hoạt động của hệ thống bằng cách đảm bảo rằng các node luôn hoạt động bình thường.

***

### Cơ chế hoạt động

#### Cơ chế Auto Healing: hệ thống VKS thực hiện kích hoạt auto healing khi

* Node báo cáo trạng thái **NotReady** trong các lần kiểm tra liên tiếp trong khoảng thời gian **10 phút**.

Nếu thỏa mãn điều kiện trên, hệ thống sẽ ngay lập tức thực hiện auto healing. Quá trình này được thực hiện theo 2 bước:

* **Bước 1:** Hệ thống VKS thực hiện drain node, tức là di chuyển tất cả các pod đang chạy trên node NotReady này sang các node khác trong node group trước khi gỡ bỏ node đó khỏi node group.&#x20;
* **Bước 2:** Hệ thống sẽ tạo lại node mới với cấu hình đã được thiết lập trên node group và thực hiện join node này vào cụm. Nếu sau khi khởi động lại, node vẫn báo cáo trạng thái "NotReady", hệ thống sẽ tiếp tục khởi động lại node cho đến khi node trở lại trạng thái hoạt động bình thường.&#x20;

{% hint style="info" %}
**Chú ý:**

* Khi hệ thống thực hiện Auto Healing, việc tạo ra node mới có thể gặp lỗi nếu bạn không có đủ credit hoặc bạn đã hết quota để tạo VM trên hệ thống vServer. Lúc này, mỗi 30 phút thì hệ thống sẽ thực hiện khởi động lại node cho đến khi node trở lại trạng thái hoạt động bình thường. Để tránh gặp lỗi bên trên, bạn cần:
  * **Đảm bảo bạn có đủ credit:** Nếu bạn là người dùng trả trước, hãy nạp thêm credit vào tài khoản của bạn.
  * **Yêu cầu tăng quota:** Bạn có thể yêu cầu tăng quota cho tài khoản của mình tại [đây](https://hcm-3.console.vngcloud.vn/vserver/limit).
{% endhint %}

***

### Bật Auto Healing

Hiện tại, tính năng Auto Healing được apply cho mỗi Node Group và luôn luôn ở trạng thái **bật**. Bạn không cần thao tác bật thủ công khi khởi tạo Cluster cũng như Node Group.
