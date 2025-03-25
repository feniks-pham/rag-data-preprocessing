# Làm việc với vDB-Metric

Khi bạn tạo các vDB, hệ thống sẽ tự động thu thập các Metric và hiển thị ở tab Infrastructure List/vDB, giúp bạn có thể theo dõi được các vDB trên VNG Cloud hoàn toàn miễn phí

<figure><img src="../../../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

Tại trang này ở mỗi vDB bạn sẽ thấy các thông tin như sau:

* **Host**: tên và ID của vDB&#x20;
* **Status**: trạng thái của vDB
* **CPU**: thông tin CPU hiện tại
* **Memory**: thông tin Memory hiện tại
* **Disk**: thông tin sử dụng disk hiện tại
* **Detailed** **Monitoring**: mặc định sẽ là tắt, khi bạn có nhu cầu cần vẽ các Metric khác ngoài các Metric mà dashboard mặc định chúng tôi đã vẽ và tạo các Alarm để cảnh báo với tài nguyên này, thì bạn cần bật tính năng này lên. Để bật tính năng này bạn cần mua gói Metric Quota (gói có phí hay miễn phí đều được), tuy nhiên bạn sẽ không bị tính là 1 Host khi bật và hoàn toàn miễn phí, chỉ khi tạo Alarm là sẽ bị tính Alarm quota.

&#x20;Khi nhấn vào tên của vDB, bạn sẽ được chuyển sang trang Dashboard, và xem default dashboard của vDB này, quy tắc đặt tên dashboard của vDB sẽ là vDB-hostname-ID (lấy block thứ 3 của ID vDB)

<figure><img src="../../../../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Hệ thống vMonitor sẽ mất 1 khoảng thời gian trung bình 5-10 phút (có thể có trường hợp tệ nhất là 20 phút) để cập nhập vDB mới sau khi bạn tạo.
* Để xem danh sách metrics tương ứng của mỗi product này, hãy xem tại [Danh sách Metrics hỗ trợ](../danh-sach-metrics-ho-tro/)
{% endhint %}
