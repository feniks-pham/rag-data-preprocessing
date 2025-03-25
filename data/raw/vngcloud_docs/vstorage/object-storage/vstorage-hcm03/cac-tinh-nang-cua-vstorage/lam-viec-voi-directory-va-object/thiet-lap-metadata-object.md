# Thiết lập metadata object

Metadata là một loại thông tin mở rộng của tập tin (Object) mà bạn đã đưa vào hệ thống vStorage. Chúng có thể là các thông tin cơ bản thường gặp như tên, ngày tạo, kích thước, kiểu tập tin (.doc, .pptx…) hoặc các thuộc tính mà bạn được phép khai báo bổ sung để thực hiện các nghiệp vụ của riêng bạn trong phát triển ứng dụng.

Để thiết lập metadata cho object, bạn có thể thực hiện theo hướng dẫn bên dưới:&#x20;



{% tabs %}
{% tab title=" Sử dụng vStorage Portal" %}
1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project, container** sau đó chọn các **object** bạn muốn thực hiện thiết lập metadata.&#x20;

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648701/image2023-3-6\_11-0-2.png?version=1\&modificationDate=1678075203000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648701/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1676341851000\&api=v2)tại **object** bạn muốn thực hiện thiết lập metadata và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648701/image2023-3-6\_11-0-24.png?version=1\&modificationDate=1678075225000\&api=v2)**.**

Màn hình **Thiết lập Metadata** được hiển thị.

4\. Chúng tôi cung cấp cho bạn hai phương thức thiết lập metadata bao gồm:

* **Key mặc định**: thực hiện chọn key trong danh sách key có sẵn mà chúng tôi cung cấp.&#x20;
* **Key tùy chỉnh**: thực hiện tự tạo key tùy chỉnh theo nhu cầu của bạn với tiền tố X-Object-Meta-Vng-.

5\. Nhập giá trị **Value** tương ứng với **Key** được chọn hoặc được tạo. Chọn **Thêm** sau đó chọn **Cập nhật.**

Sau khi thực hiện 5 bước trên bên, metadata đã được thiết lập thành công cho object của bạn.

Hiện tại chúng tôi đang hỗ trợ 8 loại key metadata mặc định bao gồm: X-Robots-Tag, Cache-Control, X-Delete-At, Content-Disposition, Content-Encoding, Expires, Content-Language, Content-Type.

Chúng tôi có giới hạn tổng số ký tự tối đa tất cả metadata của một object không được vượt quá (xem [phạm vi và giới hạn object](pham-vi-gioi-han-object.md)) nên chúng tôi khuyến khích bạn cân nhắc kỹ việc lựa chọn metadata nào được thiết lập cho một object cũng như tổng số metadata có thể được thiết lập cho object đó.

<figure><img src="../../../../../.gitbook/assets/Thiet_lap_metadata.gif" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để thiết lập metadata cho object qua vStorage API, hãy xem [API Developers](../../api-developers/).
{% endtab %}

{% tab title="Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để thiết lập metadata cho object qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}
{% endtabs %}
