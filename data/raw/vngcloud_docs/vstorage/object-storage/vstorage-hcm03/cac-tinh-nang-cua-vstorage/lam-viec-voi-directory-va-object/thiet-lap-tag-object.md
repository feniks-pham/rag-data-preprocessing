# Thiết lập tag object

Tag là một nhãn (label) gắn liền với một object với mục đích nhận dạng, phân loại hoặc cung cấp thêm thông tin khác liên quan đến object. Trong vStorage, khi bạn tải lên các object, chúng tôi hỗ trợ bạn gắn tag cho một hoặc nhiều object này.&#x20;

Để thiết lập tags cho object, bạn có thể thực hiện theo hướng dẫn bên dưới:&#x20;



{% tabs %}
{% tab title=" Sử dụng vStorage Portal" %}
1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project, container** sau đó chọn các **object** bạn muốn thực hiện thiết lập tag.&#x20;

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648536/image2023-3-6\_10-57-38.png?version=1\&modificationDate=1678075059000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648536/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1676341468000\&api=v2)tại **object** bạn muốn thực hiện thiết lập tag và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648536/image2023-3-6\_10-58-34.png?version=1\&modificationDate=1678075115000\&api=v2)**.**

Màn hình **Thiết lập Tags** được hiển thị.

4\. Chọn các nhãn bạn muốn gán cho object vừa chọn, các nhãn được ngăn cách bằng dấu phẩy (,). Chọn **Thêm** sau đó chọn **Cập nhật.**

Sau khi thực hiện 4 bước trên bên, tags đã được thiết lập thành công cho object của bạn. Chúng tôi có giới hạn tổng số ký tự tối đa tất cả các tag của một object không được vượt quá (xem [phần phạm vi và giới hạn object](pham-vi-gioi-han-object.md)) nên chúng tôi khuyến khích bạn cân nhắc kỹ việc lựa chọn tag nào được gắn cho một object cũng như tổng số tag có thể được gắn cho object đó.

<figure><img src="../../../../../.gitbook/assets/Thiet_lap_tag.gif" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để thiết lập tag cho object qua vStorage API, hãy xem [API Developers](../../api-developers/).
{% endtab %}

{% tab title=" Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để thiết lập tag cho object qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}
{% endtabs %}
