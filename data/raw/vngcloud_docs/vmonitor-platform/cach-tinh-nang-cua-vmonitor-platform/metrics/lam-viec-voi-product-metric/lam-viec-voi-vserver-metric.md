# Làm việc với vServer-Metric

Khi bạn tạo các vServer, hệ thống sẽ tự động thu thập các Metric cơ bản và hiển thị ở tab Infrastructure List/ vServer, giúp bạn có thể theo dõi được các vServer trên VNG Cloud hoàn toàn miễn phí, thông tin monitor các vServer được vMonitor lấy thông qua lớp hypervisor nên một số các metric như Memory Usage sẽ có thể không chính xác và không có metric Disk Usage, để có được các Metric này và đầy đủ hơn bạn sẽ cần sử dụng Metric Agent và cài vào các vServer như hướng dẫn tại [Làm việc với Metric Agent](../lam-viec-voi-metric-agent/).

<figure><img src="../../../../.gitbook/assets/image (146).png" alt=""><figcaption></figcaption></figure>

Tại trang này ở mỗi vServer bạn sẽ thấy các thông tin như sau:

* **Host**: tên và ID của vServer
* **Status**: trạng thái của vServer
* **CPU**: thông tin CPU hiện tại
* **Memory**: thông tin Memory hiện tại
* **Load**: thông tin Load hiện tại
* **Detailed Monitoring**: mặc định sẽ là tắt, khi bạn có nhu cầu cần vẽ các Metric khác ngoài các Metric mà dashboard mặc định chúng tôi đã vẽ và tạo các Alarm để cảnh báo với tài nguyên này, thì bạn cần bật tính năng này lên. Để bật tính năng này bạn cần mua gói Metric Quota (gói có phí hay miễn phí đều được), tuy nhiên bạn sẽ không bị tính là 1 Host khi bật và hoàn toàn miễn phí, chỉ khi tạo Alarm là sẽ bị tính Alarm quota.

&#x20;Khi nhấn vào tên của vServer, bạn sẽ được chuyển sang trang Dashboard, và xem default dashboard của vServer này, quy tắc đặt tên dashboard của vServer sẽ là vServer-hostname-ID (lấy block thứ 3 của ID vServer)

<figure><img src="../../../../.gitbook/assets/image (147).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Hệ thống vMonitor sẽ mất 1 khoảng thời gian trung bình 5-10 phút (có thể có trường hợp tệ nhất là 20 phút) để cập nhập vServer mới sau khi bạn tạo.
* Để xem danh sách metrics tương ứng của mỗi product này, hãy xem tại [Danh sách Metrics hỗ trợ](../danh-sach-metrics-ho-tro/).
* Để xem danh sách số liệu tương ứng của từng sản phẩm này, vui lòng xem tại Danh sách số liệu được hỗ trợ.
{% endhint %}
