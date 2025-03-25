# Thông báo và hướng dẫn về cách chuyển đổi gói trên hệ thống vMonitor Platform

#### Tổng quan <a href="#thongbaovahuongdanvecachchuyendoigoitrenhethongvmonitorplatform-tongquan" id="thongbaovahuongdanvecachchuyendoigoitrenhethongvmonitorplatform-tongquan"></a>

Từ ngày **29/02/2024**, hệ thống vMonitor Platform sẽ thay đổi cách mua tài nguyên đơn giản hơn nhằm đáp ứng nhu cầu đa dạng của Quý khách hàng. Cụ thể thay vì chọn các gói dịch vụ (package) có sẵn mà chúng tôi cung cấp thì bạn có thể tự lựa chọn cấu hình tài nguyên tùy theo nhu cầu. Bên cạnh đó, bạn cũng có thể mua đồng thời nhiều loại tài nguyên trên hệ thống vMonitor Platform. Kể từ thời điểm này tới ngày **22/04/2024**, nếu bạn còn ít nhất 1 tài nguyên Metric Quota, Log Project trên hệ thống vMonitor Platform, hãy thực hiện chuyển đổi theo hướng dẫn bên dưới của chúng tôi. Sau thời gian này, nếu bạn chưa thực hiện chuyển đổi tài nguyên thì hệ thống vMonitor Platform sẽ tự động thực hiện chuyển đổi. Dưới đây là một vài điểm lưu ý trước khi bạn thực hiện chuyển đổi gói:

{% hint style="info" %}
**Chú ý:**&#x20;

Sẽ có vài lưu ý khi thực hiện chuyển gói trên hệ thống vMonitor Platform mà bạn cần biết, bao gồm:&#x20;

* Các **tier** hiện tại sẽ được chúng tôi chuyển đổi thành các **class**. Cụ thể:
  * Free tier được chúng tôi chuyển đổi thành Class Basic. Tham khảo thông tin chi tiết cho các class tại [Metric Quota Class](../vmonitor-platform-la-gi/vmonitor-platform-metric-la-gi/metric-quota-class.md), [Log Project Class](../vmonitor-platform-la-gi/vmonitor-platform-log-la-gi/log-project-class.md) và [Synthetic Test Quota Class](../vmonitor-platform-la-gi/vmonitor-platform-synthetic-la-gi/synthetic-test-quota-class.md)
  * Small/ Medium/ Large,... tier được chúng tôi chuyển đổi thành Class Pro. Tham khảo thông tin chi tiết cho các class tại [Metric Quota Class](../vmonitor-platform-la-gi/vmonitor-platform-metric-la-gi/metric-quota-class.md), [Log Project Class](../vmonitor-platform-la-gi/vmonitor-platform-log-la-gi/log-project-class.md) và [Synthetic Test Quota Class](../vmonitor-platform-la-gi/vmonitor-platform-synthetic-la-gi/synthetic-test-quota-class.md)
* Với các class **Basic, Pro** mới, chúng tôi sẽ không giới hạn số lượng **alarm** bạn có thể tạo.&#x20;
* Việc chuyển đổi gói sang dạng mới sẽ hoàn toàn **miễn phí** và **không ảnh hưởng** đến:
  * **Chi phí**: Giá cước của bạn sẽ **giữ nguyên** sau khi chuyển đổi.
  * **Chức năng**: Bạn vẫn sẽ **giữ nguyên** tất cả các chức năng của gói cước hiện tại.
  * **Downtime**: Hệ thống sẽ **không bị gián đoạn** trong quá trình chuyển đổi.
* Đối với khách hàng cũ, lượng **Email/ SMS** sẽ được chúng tôi tự động thêm vào **free notification quota** tương ứng cho bạn. Bên cạnh đó, chúng tôi cũng có cung cấp các gói SMS/ Email miễn phí, bạn có thể thực hiện mua và sử dụng chúng theo hướng dẫn tại [Làm việc với SMS Notification Quota](../cach-tinh-nang-cua-vmonitor-platform/notification/lam-viec-voi-sms-notification-quota.md) và [Làm việc với Email Notification Quota](../cach-tinh-nang-cua-vmonitor-platform/notification/lam-viec-voi-email-notification-quota.md).
{% endhint %}

***

#### **Các bước thực hiện chuyển đổi** <a href="#thongbaovahuongdanvecachchuyendoigoitrenhethongvmonitorplatform-cacbuocthuchienchuyendoi" id="thongbaovahuongdanvecachchuyendoigoitrenhethongvmonitorplatform-cacbuocthuchienchuyendoi"></a>

Dưới đây là hướng dẫn chi tiết về cách chuyển đổi gói trên hệ thống vMonitor Platform:

* **Bước 1:** Truy cập vào hệ thống vMonitor Platform tại [https://hcm-3.console.vngcloud.vn/vmonitor/quota-usage/quota](https://hcm-3.console.vngcloud.vn/vmonitor/quota-usage/quota).
* **Bước 2:** Đăng nhập vào tài khoản của Quý khách hàng.
* **Bước 3:** Chọn **Usage & Quota** từ menu bên trái.
* **Bước 4:** Lúc này, bạn sẽ thấy gợi ý chuyển đổi gói trên giao diện của bạn. Chọn **Convert.**

<figure><img src="../../.gitbook/assets/image (30) (1).png" alt=""><figcaption></figcaption></figure>

* **Bước 5:** Chúng tôi cung cấp bảng so sánh các thay đổi khi thực hiện Convert, bạn có thể chọn qua từng mục bao gồm: **Metric Quota, Log Project, Paid SMS Notification, Paid Email Notification, Synthetic Test Quota** để xem chi tiết thông số gói dịch vụ của từng loại trước khi thực hiện chuyển đổi. Bạn cần Xác nhận thông tin chuyển đổi và chọn **Convert**.

<figure><img src="../../.gitbook/assets/image (31) (1).png" alt=""><figcaption></figcaption></figure>

Quá trình chuyển đổi gói sẽ diễn ra ngay lập tức. Các thông số về Quota/ Usage của sẽ được bảo toàn sau khi bạn thực hiện Convert. Lúc này, màn hình hiển thị theo định dạng gói cước mới như sau:

<figure><img src="../../.gitbook/assets/image (32) (1).png" alt=""><figcaption></figcaption></figure>

Trong ví dụ này, tôi đã mua gói Metric Quota, Log Project có tính phí nên khi chuyển đổi, tôi đã tự động được tặng thêm 200 SMS và 200 Email miễn phí trong vòng 6 tháng. Cụ thể:&#x20;

<figure><img src="../../.gitbook/assets/image (33) (1).png" alt=""><figcaption></figcaption></figure>

Sau khi đã chuyển đổi tài nguyên, bạn có thể tiếp tục thực hiện Tăng/ giảm kích thước, Gia hạn tài nguyên theo các hướng dẫn khác trong tài liệu này.
