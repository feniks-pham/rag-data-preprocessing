# Sử dụng tính năng Event notification

**Event Notification** trong vStorage là tính năng cho phép bạn nhận thông báo về các sự kiện xảy ra trong bucket dưới dạng tệp tin JSON, chẳng hạn như khi một object được upload, delete hay ghi đè.

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** chứa **bucket** bạn muốn thiết lập event notification.

3\. Chọn biểu tượng **Action** và chọn **Configure event notification.**

<figure><img src="../../../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4\. Chọn **Create an Event notification**.

5\. Tại đây, bạn hãy cấu hình thông tin Event Notification bao gồm:

* **Rule name**: Tên gợi nhớ cho Event Notification, tên này phải là duy nhất trên account của bạn và rule name phải từ 1 tới 63 ký tự. Các ký tự có thể bao gồm chữ cái, chữ số và dấu gạch ngang (-). Rule name phải bawtss đầu và kết thúc với một chữ cái.
* **Filter:** chọn phạm vi nhận event
  * **Prefix**: Chỉ theo dõi các event với object có tiền tố cụ thể (ví dụ: `images/`).
  * **Suffix**: Chỉ theo dõi các event với object có hậu tố cụ thể (ví dụ: `.jpg`).
* **Description**: nhập mô tả cho rule.
* **Event types**: Bạn có thể chọn một hoặc nhiều loại event cần theo dõi. Các event phổ biến bao gồm:
  * **Object Creation:** Gồm tất cả các sự kiện khi object được tạo, bao gồm PUT, POST, COPY và action Complete Multipart Upload.
  * **Object Removal**: Theo dõi các sự kiện khi object bị xóa, bao gồm Delete, Delete Marker
  * **Object Lifecycle Expiration:** Theo dõi các sự kiện khi một lifecycle expiration chạy trên bucket, bao gồm Expire Current version of object, Delete Marker
* **Report Bucker**: Chọn bucket đích nhận Event notification. Chúng tôi khuyến khích bạn nên tạo các bucket riêng biệt chuyên dùng để lưu Event notification phục vụ Audit.
* **Report Name Rule:** Chọn các đặt tên, chia folder cho các event.
  * **No-date-based partitioning**:
    * File JSON sẽ được lưu với tên bao gồm tên bucket và thời gian lưu, mà không có cấu trúc phân vùng thư mục theo ngày. Phù hợp nếu bạn không cần quản lý file theo thư mục ngày tháng.
    * Cấu trúc tên file: `[Bucket][YYYY]-[MM]-[DD]-[hh]-[mm]`.
    * Ví dụ: `bucketA/2013-11-01-21-32` (tên bucket + ngày giờ).
  * **Date-based partitioning**:
    * File JSON sẽ được lưu trong các thư mục theo từng phần của ngày (năm/tháng/ngày), giúp phân chia dữ liệu theo từng ngày để dễ dàng truy xuất. Phù hợp nếu bạn cần tổ chức dữ liệu theo ngày để quản lý dễ hơn trong trường hợp có nhiều báo cáo.
    * Cấu trúc thư mục và tên file: `[Bucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]`.
    * Ví dụ: `bucketB/2023/03/01/2023-03-01-21-32`&#x20;

<figure><img src="../../../../../../.gitbook/assets/image (8) (1) (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (9) (4).png" alt=""><figcaption></figcaption></figure>

5\. Chọn **Create event notification** để khởi tạo event này.

{% hint style="info" %}
**Chú ý:**

* **Hạn chế trùng lặp event**: Nếu có nhiều cấu hình Event Notification cho cùng một event, bucket của bạn chọn có thể phải lưu trữ nhiều file JSON. Điều này có thể gây tốn resource, nên thiết lập cẩn thận để tránh trùng lặp.
{% endhint %}
