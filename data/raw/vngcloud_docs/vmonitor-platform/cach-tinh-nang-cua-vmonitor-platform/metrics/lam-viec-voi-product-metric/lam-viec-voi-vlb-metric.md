# Làm việc với vLB-Metric

Khi bạn tạo các vLB, hệ thống sẽ tự động thu thập các Metric và hiển thị ở tab Infrastructure List/vLB, giúp bạn có thể theo dõi được các vLB trên VNG Cloud hoàn toàn miễn phí

<figure><img src="../../../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

Tại trang này ở mỗi vLB bạn sẽ thấy các thông tin như sau:

* **Host**: tên và ID của vLB&#x20;
* **Status**: trạng thái của vLB
* **vLBDataIn**: thông tin dữ liệu đang vào hiện tại
* **vLBDataOut**: thông tin dữ liệu đang ra hiện tại
* **Connection**: thông tin sô lượng connection hiện tại
* **Detailed Monitoring**: mặc định sẽ là tắt, khi bạn có nhu cầu cần vẽ các Metric khác ngoài các Metric mà dashboard mặc định chúng tôi đã vẽ và tạo các Alarm để cảnh báo với tài nguyên này, thì bạn cần bật tính năng này lên. Để bật tính năng này bạn cần mua gói Metric Quota (gói có phí hay miễn phí đều được), tuy nhiên bạn sẽ không bị tính là 1 Host khi bật và hoàn toàn miễn phí, chỉ khi tạo Alarm là sẽ bị tính Alarm quota.

&#x20;Khi nhấn vào tên của vLB, bạn sẽ được chuyển sang trang Dashboard, và xem default dashboard của vLB này, quy tắc đặt tên dashboard của vLB sẽ là vLB-hostname-ID (lấy block thứ 3 của ID vLB)

<figure><img src="../../../../.gitbook/assets/image (149).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Hệ thống vMonitor sẽ mất 1 khoảng thời gian trung bình 5-10 phút (có thể có trường hợp tệ nhất là 20 phút) để cập nhập vLB mới sau khi bạn tạo.
* Để xem danh sách metrics tương ứng của mỗi product này, hãy xem tại [Danh sách Metrics hỗ trợ](../danh-sach-metrics-ho-tro/).
{% endhint %}
