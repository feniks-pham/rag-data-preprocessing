# Xóa object

Để xóa hoặc nhiều object, bạn có thể:

{% tabs %}
{% tab title=" Sử dụng vStorage Portal" %}
1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project, container** sau đó chọn các **object** bạn muốn thực hiện xó&#x61;**.**

2\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648534/image2023-3-6_11-3-40.png?version=1\&modificationDate=1678075421000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648534/image2023-2-6_10-20-54.png?version=1\&modificationDate=1678075363000\&api=v2)tại object bạn muốn thực hiện xóa và chọn![](https://docs.vngcloud.vn/download/attachments/49648534/image2023-3-6_11-4-15.png?version=1\&modificationDate=1678075456000\&api=v2).

Sau khi chọn Xóa, hệ thống sẽ tự động chuyển ra màn hình chính, nếu bạn thấy object vừa thực hiện biến mất khỏi danh sách thì bạn đã xoá thành công. Object lúc này đã được xóa vĩnh viễn khỏi hệ thống.

**Lưu ý:** một khi object đã bị xóa khỏi hệ thống vStorage, bạn không thể phục hồi object đó.

<figure><img src="../../../../../.gitbook/assets/Xoa_object_container (1).gif" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để xóa một object qua vStorage API, hãy xem [API Developers](../../api-developers/).

\

{% endtab %}

{% tab title="Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để xóa một object qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).

\

{% endtab %}
{% endtabs %}
