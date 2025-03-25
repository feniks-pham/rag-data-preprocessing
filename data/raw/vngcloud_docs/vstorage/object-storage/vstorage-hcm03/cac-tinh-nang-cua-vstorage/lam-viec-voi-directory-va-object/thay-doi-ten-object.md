# Thay đổi tên object

Bạn cũng có thể thay đổi tên của object mà bạn đã tải lên một container. Để thực hiện thay đổi tên object, hãy làm theo hướng dẫn bên dưới:



{% tabs %}
{% tab title=" Sử dụng vStorage Portal" %}
1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project, container** sau đó chọn các **object** bạn muốn thực hiện đổi tê&#x6E;**.**

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648530/image2023-3-6_10-56-24.png?version=1\&modificationDate=1678074986000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648530/image2023-2-6_10-20-54.png?version=1\&modificationDate=1678074993000\&api=v2)tại **object** bạn muốn thực hiện đổi tên và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648530/image2023-3-6_10-56-49.png?version=1\&modificationDate=1678075010000\&api=v2)**.**

4\. Nhập tên object mà bạn muốn thay đổi, tên object cần tuân thủ theo mô tả của chúng tôi tạo [Phạm vi giới hạn object](pham-vi-gioi-han-object.md).

Khi thực hiện thay đổi tên của object, bạn không nên thay đổi phần kiểu tệp tin (ví dụ: abc.pdf, .pdf chính là kiểu tệp tin) trong tên của object. Việc thay đổi phần extension này của tên của object có thể làm thay đổi content type của object đó, điều này có thể gây lỗi khi bạn tải object xuống thiết bị cá nhân.&#x20;

<figure><img src="../../../../../.gitbook/assets/Doi_ten_object.gif" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title=" Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để thay đổi tên object qua vStorage API, hãy xem [API Developers](../../api-developers/).
{% endtab %}

{% tab title="Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để thay đổi tên object qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}
{% endtabs %}
