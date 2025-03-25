# Sử dụng tính năng Object lock

**Object Lock** là tính năng giúp bảo vệ dữ liệu của bạn khỏi bị xóa hoặc ghi đè trong một khoảng thời gian cố định hoặc vô thời hạn. Tính năng này sử dụng model **WORM** (Write Once, Read Many), nghĩa là sau khi một object được tải lên S3 và được locked, object đó không thể bị xóa hoặc thay đổi bởi bất kỳ ai, kể cả người dùng root. Hiện tại, trên region HCM04, chúng tôi đã hỗ trợ bạn thiết lập Object Locked ở 2 mode Compliance, Legal Hold và <mark style="color:red;">**chưa hỗ trợ mode Governance**</mark><mark style="color:red;">.</mark> Nếu bạn sử dụng 3rd party software để thiết lập Object Locked ở mode Governance này thì S3 key được tạo ra sẽ có full quyền xóa các object version trên bucket của bạn. Ý nghĩa các mode locked được mô tả bên dưới:&#x20;

* **Retention mode**: ngăn chặn việc xóa và ghi đè object version trong một khoảng thời gian nhất định. Trong Retention period sẽ có 2 mode:
  * **Compliance mode (đã hỗ trợ)**: bất kỳ người dùng hoặc admin,…nào cũng không thể ghi đè object version được locked. Khi hết thời gian được thiết lập trước, người dùng có thể thực hiện xóa hoặc ghi đè object bình thường.
  * **Governance mode (coming soon)**: chỉ những người dùng có quyền đặc biệt (có quyền ByPassGovernance), chẳng hạn như người dùng root hoặc S3 Key không bật Restriction by IAM mới có thể xóa hoặc ghi đè object.
* **Legal Hold:** ngăn chặn việc xóa và ghi đè object version vô thời hạn tới khi nào người dùng disable. Mode này hoạt động độc lập với Retention period. Người dùng có quyền PutObjectLegalHold có thể thực hiện thêm hoặc remove legal hold cho object.

Để thiết lập Object Locked cho một bucket bằng S3 Browser, khi khởi tạo một bucket mới, bạn cần chọn phương án **Enable S3 Objected Lock.&#x20;**<mark style="color:red;">**Hãy nhớ rằng bạn sẽ không thể bật Object Lock cho bucket đã tồn tại.**</mark>

<figure><img src="../../../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Sau khi bucket đã được tạo thành công, để cấu hình thông số cụ thể cho tính năng object lock, vui lòng làm theo các bước bên dưới:&#x20;

## Compliance Mode

Sau khi đã bật Object Lock cho bucket, bạn có thể thiết lập Object Lock cho bucket theo các bước sau:&#x20;

1\. Tại bucket cần thiết lập object lock, chọn **Action** và chọn **Configure object lock retention**

<figure><img src="../../../../../../.gitbook/assets/image (802).png" alt=""><figcaption></figcaption></figure>

2\. Tại màn hình Configure object lock retention, chọn **Enable Object Lock retention policy**

<figure><img src="../../../../../../.gitbook/assets/image (803).png" alt=""><figcaption></figcaption></figure>

3\. Tại mục **Retention Mode**: hiện tại chúng tôi chỉ hỗ trợ **Compliance Mode** (mode này sẽ bảo vệ object version đối với việc thay đổi hay xóa cho đến khi hết thời gian giữ).

4\. Tại mục **Retention Period**: bạn hãy chọn thời gian mong muốn giữ cho các object thuộc bucket của bạn. Ví dụ bạn chọn 30 ngày, 60 ngày, 1000 ngày,...

<figure><img src="../../../../../../.gitbook/assets/image (804).png" alt=""><figcaption></figcaption></figure>

5\. Chọn **Update.**

5\. Bây giờ, bạn hãy tải lên các object của bạn. Tất cả các object được tải lên bây giờ sẽ được giữ trong Retention period mà bạn đã chọn. Trong khoảng thời gian này, không một ai có quyền xóa object của bạn.

Ví dụ: hình bên trên, tôi cấu hình giữ 60 ngày,&#x20;

* Nếu ngày tôi tải lên object là 25/10/2024. Như vậy, object này sẽ được giữ tới **25/10/2024 + 60 ngày = 24/12/2024**
* Nếu ngày tôi tải lên object là 01/11/2024. Như vậy, object này sẽ được giữ tới **25/10/2024 + 60 ngày = 31/12/2024**

***

## Governance Mode

* <mark style="color:red;">**Hiện tại, chúng tôi chưa hỗ trợ mode Governance**</mark><mark style="color:red;">.</mark> Nếu bạn sử dụng 3rd party software để thiết lập Object Locked ở mode Governance này thì S3 key được tạo ra sẽ có full quyền xóa các object version trên bucket của bạn.&#x20;

***

## **Legal Hold**

Tính năng **Object Legal Hold** trên vStorage cho phép bạn giữ một version của object không bị xóa hoặc ghi đè. Khi tính năng này được bật, bất kỳ ai, kể cả Root User Account, đều không thể xóa hoặc chỉnh sửa object đó cho đến khi legal hold được tắt.

Sau khi đã bật Object Lock cho bucket, bạn có thể thiết lập Object Lock loại **Legal Hold** cho từng object trong bucket theo các bước sau:&#x20;

1\. Tại object cần thiết lập object lock, chọn **Action** và chọn **Enable object legal hold**

<figure><img src="../../../../../../.gitbook/assets/image (805).png" alt=""><figcaption></figcaption></figure>

2\. Tại màn hình Enable object legal hold, chọn **Enable**

<figure><img src="../../../../../../.gitbook/assets/image (806).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Legal hold chỉ áp dụng cho từng version của object, nên nếu bật cho một version cụ thể, các version khác vẫn có thể bị chỉnh sửa hoặc xóa.
* Tính năng này khác với **Retention Policy** vì chỉ dừng việc xóa hoặc chỉnh sửa object chứ không có thời gian kết thúc.
{% endhint %}

