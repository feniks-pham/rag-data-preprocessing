# Di chuyển object

Bạn đã tải object lên một container. Lúc này bạn nhận ra object mình vừa tải lên chưa nằm đúng trong container hoặc directory mà bạn mong muốn. Thay vì bạn phải thực hiện xóa object và tải nó lên một container hoặc directory khác, chúng tôi hỗ trợ bạn tính năng di chuyển object.&#x20;

Để thực hiện di chuyển object, hãy làm theo hướng dẫn bên dưới:



{% tabs %}
{% tab title="Sử dụng vStorage Portal" %}
1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **project, container** sau đó chọn các **object** bạn muốn thực hiện di chuyển.
3. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648528/image2023-3-6\_10-53-48.png?version=1\&modificationDate=1678074829000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648528/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1678074833000\&api=v2)tại **object** bạn muốn thực hiện di chuyển và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648528/image2023-3-6\_10-54-15.png?version=1\&modificationDate=1678074856000\&api=v2)**.**
4. &#x20;Chọn **container** và **directory** nếu có mà bạn muốn di chuyển object tới. Chúng tôi cũng hỗ trợ bạn tạo directory mới nếu directory bạn muốn di chuyển tới chưa tồn tại.&#x20;

Bạn có thể di chuyển object qua các container trong một project. Hiện tại chúng tôi không hỗ trợ bạn di chuyển object qua các project khác nhau.

<figure><img src="../../../../../.gitbook/assets/Di_chuyen_object.gif" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để di chuyển object qua vStorage API, hãy xem [API Developers](../../api-developers/).

\

{% endtab %}

{% tab title=" Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để di chuyển object qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}
{% endtabs %}

&#x20;

1\.&#x20;
