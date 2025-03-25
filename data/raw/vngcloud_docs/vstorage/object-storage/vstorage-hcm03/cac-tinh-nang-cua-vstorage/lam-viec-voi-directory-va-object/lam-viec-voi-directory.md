# Làm việc với directory

Directory là một thư mục chứa dữ liệu trong vStorage.

{% tabs %}
{% tab title="Khởi tạo directory" %}
Trong vStorage, directory được chúng tôi định nghĩa là các thư mục nằm trong một container. Để tạo directory, hãy làm theo hướng dẫn bên dưới:

1. **Sử dụng vStorage Portal:**

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container** mà bạn bạn muốn tạo directory.

3\. Chọn **Tạo một directory.**

Màn hình **Tạo mới directory** được hiển thị.

4\. Trong **Tên directory**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho directory của bạn.&#x20;

Sau khi tạo container, bạn không thể thay đổi tên của directory. Chúng tôi khuyến cáo tên của directory nên chứa các chữ cái viết thường, các chữ số và không có các ký tự đặc biệt cụ thể như #, @, $, %, ?, /, \`, \~ ... Nếu bạn thực sự cần đặt tên với các ký tự chữ cái viết hoa, vui lòng lưu ý rằng, nó có thể gặp một số vấn đề khi làm việc với các 3rd party softwares được hỗ trợ từ các nhà cung cấp khác.

5\. Chọn **Tạo directory.**

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, directory đã được tạo. Bạn có thể tải directory lên directory này hoặc chia sẻ, xóa directory.

<figure><img src="../../../../../.gitbook/assets/Khoi_tao_directory.gif" alt=""><figcaption></figcaption></figure>

2. **Sử dụng vStorage API**

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía bạn của bạn với vStorage để lưu trữ dữ liệu.

Để tạo mới một directory qua vStorage API, hãy xem [API Developers](../../api-developers/).

\
3\.  **Sử dụng 3rd party softwares**

vStorage cũng tương thích với các công cụ phía bạn sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để tạo mới một directory qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}

{% tab title="Chia sẻ directory" %}
Để chia sẻ directory, hãy làm theo hướng dẫn bên dưới:

1. **Sử dụng vStorage Portal**



Để thực hiện chia sẻ một directory trong một container, bạn có thể thực hiện theo các bước bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **project, container** sau đó chọn một hoặc nhiều các **directory** bạn muốn thực hiện chia sẻ.
3. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648478/image2023-3-6\_10-50-12.png?version=1\&modificationDate=1699348122000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648478/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1678075522000\&api=v2)tại **directory** bạn muốn thực hiện chia sẻ và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648478/image2023-3-6\_10-50-38.png?version=1\&modificationDate=1699348122000\&api=v2)
4. Chọn **Mode**:&#x20;
5. Nếu **Protocol** là **OpenStack Swift** thì bạn có thể chọn **Mode** là **Download** hoặc **View**.

7\. Nhập **Thời gian hết hạn** bạn muốn chia sẻ directory tức là thời gian đường dẫn (Temporary URL) truy cập tới directory có hiệu lực. Bạn có thể giới hạn số **ngày**, **giờ**, **phút** mà đường dẫn truy cập tới directory tồn tại.&#x20;

8\. Chọn **Tạo đường dẫn** .

9\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648478/image2023-3-6\_10-51-24.png?version=1\&modificationDate=1699348123000\&api=v2) để sao chép từng đường dẫn cho từng directory. Mỗi directory được chúng tôi tạo ra một URL riêng biệt.

Sau khi bạn chia sẻ directory thông qua Temporary URL ở cơ chế View, bạn sẽ nhận được 1 đường dẫn (URL). Bạn sao chép đường dẫn này và dán vào bất kỳ trình duyệt nào mà bạn sử dụng. Lúc này hệ thống vStorage không hỗ trợ bạn xem trực tiếp directory, bạn cần thêm tên object thuộc directory này để xem object đó.

* Temporary URL của Directory1: [https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/directory1?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1](https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/directory1?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1)
* Temporary URL khi bạn muốn xem object **setting.ini** thuộc Directory1: [https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/Directory1/**setting.ini**?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1](https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/Directory1/setting.ini?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1)

Sau khi bạn chia sẻ directory thông qua  Temporary URL ở cơ chế Download, bạn sẽ nhận được 1 đường dẫn (URL). bạn sao chép đường dẫn này và dán vào bất kỳ trình duyệt nào mà bạn sử dụng. Lúc này hệ thống vStorage không hỗ trợ bạn xem trực tiếp directory, bạn cần thêm tên object thuộc directory này để tải xuống object đó. Ví dụ:

* Temporary URL của Directory1: [https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/directory1?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1](https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/directory1?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1)
* Temporary URL khi bạn muốn xem object **setting.ini** thuộc Directory1: [https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/Directory1/**setting.ini**?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1](https://hcm01.vstorage.vngcloud.vn/v1/AUTH\_410ded5c02674846b534ff7b4a894c2e/my-web/Directory1/setting.ini?temp\_url\_sig=a41703737ce078e14803362ca681ac959a1df476\&temp\_url\_expires=1687854410\&temp\_url\_prefix=directory1)

Khi bạn dán đường dẫn và chọn mở đường dẫn:

* Nếu trình duyệt của bạn hỗ trợ mở trực tiếp loại object này trên trình duyệt thì bạn có thể xem trực tiếp object ngay tại màn hình này. Khi object đang được mở trên trình duyệt thì thời gian tồn tại của link vẫn được tính. Nếu thời gian chưa hết hạn, bạn có thể nhấn chuột phải và tải xuống object ( tải từ trình duyệt về thiết bị cá nhân chứ không phải tải từ vStorage về thiết bị cá nhân). Nếu thời gian đã hết hạn, bạn không thể nhấn chuột phải để tải xuống object và khi bạn Reload lại trình duyệt, dữ liệu của object hiển thị cũng sẽ mất.
* Nếu trình duyệt của bạn không hỗ trợ mở trực tiếp loại object này trên trình duyệt thì hệ thống tự động chuyển cơ chế chia sẻ object qua Download, hệ thống sẽ tự động tải xuống object này về thiết bị cá nhân của bạn.
* Chi tiết từng trình duyệt hỗ trợ mở trực tiếp loại object này tham khảo thêm ở : [![](https://fileinfo.com/svg/favicon.svg)FileInfo.com - The File Format Database](https://fileinfo.com/) .

**2.Sử dụng vStorage API**

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía bạn của bạn với vStorage để lưu trữ dữ liệu.

Để lấy đường dẫn TempURL nhằm chia sẻ directory qua vStorage API, hãy xem [API Developers](../../api-developers/).

3. **Sử dụng 3rd party softwares**

vStorage cũng tương thích với các công cụ phía bạn sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để lấy đường dẫn TempURL nhằm chia sẻ directory qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).


{% endtab %}

{% tab title=" Xóa directory" %}
Để xóa hoặc nhiều directory, bạn có thể:

1. **Sử dụng vStorage Portal**

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container**, **directory** bạn muốn thực hiện xóa.

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648478/image2023-3-6\_11-7-16.png?version=1\&modificationDate=1678075637000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648478/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1678075522000\&api=v2)tại directory bạn muốn thực hiện xóa và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648478/image2023-3-6\_11-7-37.png?version=1\&modificationDate=1678075658000\&api=v2).

Sau khi chọn Xóa, hệ thống sẽ tự động chuyển ra màn hình chính, nếu bạn thấy directory vừa thực hiện biến mất khỏi danh sách thì bạn đã xoá thành công. Directory và các directory thuộc directory lúc này đã được xóa vĩnh viễn khỏi hệ thống.

<figure><img src="../../../../../.gitbook/assets/Xoa_directory.gif" alt=""><figcaption></figcaption></figure>

2. **Sử dụng vStorage API**

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía bạn của bạn với vStorage để lưu trữ dữ liệu.

Để xóa directory qua vStorage API, hãy xem [API Developers](https://docs.vngcloud.vn/display/VV/API+Developers).

3. **Sử dụng 3rd party softwares**

vStorage cũng tương thích với các công cụ phía bạn sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](https://docs.vngcloud.vn/display/VV/3rd+party+softwares) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để xóa directory qua 3rd party software, hãy xem [3rd party softwares](https://docs.vngcloud.vn/display/VV/3rd+party+softwares).
{% endtab %}
{% endtabs %}





