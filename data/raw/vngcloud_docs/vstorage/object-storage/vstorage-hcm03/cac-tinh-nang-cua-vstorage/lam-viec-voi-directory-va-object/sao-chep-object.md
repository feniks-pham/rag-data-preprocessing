# Sao chép object

Bạn cũng có thể sao chép object mà bạn đã tải lên qua các container khác nhau. Để thực hiện sao chép object, hãy làm theo hướng dẫn bên dưới:



{% tabs %}
{% tab title=" Sử dụng vStorage Portal" %}
1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project, container** sau đó chọn các **object** bạn muốn thực hiện sao chép.

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648526/image2023-3-6\_10-55-13.png?version=1\&modificationDate=1678074914000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648526/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1678074922000\&api=v2)tại **object** bạn muốn thực hiện sao chép và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648526/image2023-3-6\_10-55-35.png?version=1\&modificationDate=1678074936000\&api=v2)**.**

4\. Chọn container và directory nếu có mà bạn muốn sao chép object tới. Chúng tôi cũng hỗ trợ bạn tạo directory mới nếu directory bạn muốn sao chép tới chưa tồn tại.&#x20;

Bạn có thể sao chép object qua các container trong một project. Hiện tại chúng tôi không hỗ trợ bạn sao chép object qua các project khác nhau.

<figure><img src="../../../../../.gitbook/assets/Sao_chep_object.gif" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để sao chép object qua vStorage API, hãy xem [API Developers](../../api-developers/).
{% endtab %}

{% tab title=" Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để sao chép object qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}
{% endtabs %}
