# Làm việc với vStorage-Metric

Khi bạn tạo các vStorage Project, hệ thống sẽ tự động thu thập các vStorage metric và hiển thị ở tab Infrastructure List/vStorage, giúp bạn có thể theo dõi được các vStorage Project trên VNG Cloud hoàn toàn miễn phí

<figure><img src="../../../../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

Tại trang này ở mỗi vStorage Project bạn sẽ thấy các thông tin như sau:

* **Host**: tên và ID của vStorage Project
* **Status**: trạng thái về monitor của vStorage Project, UP là đang có dữ liệu, UNDERTERMINE là trong vòng 5p chưa có dữ liệu mới
* **Usage**: thông tin về usage/quota của vStorage Project
* **Detailed Monitoring**: mặc định sẽ là tắt, khi bạn có nhu cầu cần vẽ các vStorage metric khác ngoài các Metric mà dashboard mặc định chúng tôi đã vẽ và tạo các Alarm để cảnh báo với tài nguyên này, thì bạn cần bật tính năng này lên. Để bật tính năng này bạn cần mua gói Metric Quota (gói có phí hay miễn phí đều được), tuy nhiên bạn sẽ không bị tính là 1 Host khi bật và hoàn toàn miễn phí, chỉ khi tạo Alarm là sẽ bị tính vào Alarm quota.

&#x20;Khi nhấn vào tên của vStorage Project, bạn sẽ được chuyển sang trang Dashboard, và xem default dashboard của vStorage Project này, quy tắc đặt tên dashboard của vStorage sẽ là vStorage-Project\_Name-ID (lấy block thứ 3 của ID vStorage)

<figure><img src="../../../../.gitbook/assets/image (155).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (156).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Hệ thống vMonitor sẽ mất 1 khoảng thời gian trung bình 5-10 phút (có thể có trường hợp tệ nhất là 20 phút) để cập nhập vStorage Project mới sau khi bạn tạo.
* Để xem danh sách metrics tương ứng của mỗi product này, hãy xem tại [Danh sách Metrics hỗ trợ](../danh-sach-metrics-ho-tro/).
{% endhint %}

\
