# Xem thông tin object/ directory

Sau khi bạn đã tạo directory và tải lên object vào container hay tải lên object vào directory. Bạn có thể xem thông tin object/ directory đó và sử dụng các tính năng mà chúng tôi cung cấp cho object/ directory bao gồm: di chuyển, sao chép, đổi tên object,...

Để xem thông tin của một object/ directory, bạn có thể:&#x20;

{% tabs %}
{% tab title="Sử dụng vStorage Portal" %}


1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** sau đó chọn **container** chứa **object/ directory** bạn muốn xem thông tin chi tiết.

3\. Trên trang hiển thị danh sách object/ directory, bạn có thể xem thông tin object/ directory trên bảng dữ liệu bao gồm:

* **Tên**: tên object/ directory.
* **Kích thước**: nếu là object thì chúng tôi sẽ hiển thị kích thước của object mà bạn đã tải lên, nếu là directory thì sẽ không có thông tin này.
* **Lớp lưu trữ**: lớp lưu trữ trên container chứa object/ directory.
* **Sửa đổi lần cuối**: thời gian sửa đổi lần gần với hiện tại nhất của object/ directory.

4\. Bạn có thể chọn vào ![](https://docs.vngcloud.vn/download/thumbnails/59805571/image2023-7-13\_12-22-47.png?version=1\&modificationDate=1689225769000\&api=v2) tại object/ directory mà bạn muốn xem chi tiết. Khi bạn chọn:

* **Object**: màn hình hiển thị thông tin chi tiết của object được chọn bao gồm: **Tên**, **Kích thước,** **Content** **type**, **Sửa đổi lần cuối**, **Đường dẫn**, **Thông tin Checksum**, **Thông tin Phiên bản**.
* **Directory**: màn hình hiển thị thông tin chi tiết của object được chọn bao gồm: **Tên**, **Content type**, **Đường dẫn**, **Thông tin Phiên bản.**

<figure><img src="../../../../../.gitbook/assets/Xem_thong_tin_object_directory.gif" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để xem thông tin một object/ directory qua vStorage API, hãy xem [API Developers](../../api-developers/).
{% endtab %}

{% tab title="Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để xem thông tin một object/ directory qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}
{% endtabs %}
