# Xóa container

Bạn đã khởi tạo một container và thực hiện tải lên/ tải xuống object trong container đó. Hiện tại nhu cầu kinh doanh của bạn thay đổi, bạn không có nhu cầu sử dụng container đã tạo. Bạn có thể thực hiện xóa container theo các cách mà chúng tôi mô tả bên dưới.

Để xóa một container, bạn có thể:&#x20;

<details>

<summary>Sử dụng vStorage Portal</summary>

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container** bạn muốn thực hiện xóa.

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648522/image2023-3-6\_10-38-41.png?version=1\&modificationDate=1678073922000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648522/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1678073899000\&api=v2)tại **container** bạn muốn thực hiện xóa container và chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648522/image2023-3-6\_10-39-5.png?version=1\&modificationDate=1678073946000\&api=v2).

Sau khi chọn Xóa, hệ thống sẽ tự động chuyển ra màn hình chính, nếu bạn thấy container vừa thực hiện biến mất khỏi danh sách thì bạn đã xoá thành công. Container lúc này đã được xóa vĩnh viễn khỏi hệ thống và bạn không thể khôi phục container cũng như các object được lưu trữ trong container. Vì vậy hãy đảm bảo kiểm tra dữ liệu của bạn trước khi thực hiện thao tác này. Nếu container đang được bật versioning thì khi bạn thực hiện xóa container, tất cả object trong container sẽ được chuyển thành một version trong container version. Bạn không thể thực hiện xóa các container segment khi thực hiện xóa container gốc.

Để biết thêm thông tin về container segment, hãy xem tại [Tổng quan container](tong-quan-container.md).

<img src="../../../../../.gitbook/assets/Xoa_container.gif" alt="" data-size="original">

</details>

<details>

<summary>Sử dụng vStorage API</summary>

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để xóa một container qua vStorage API, hãy xem [API Developers](../../api-developers/).

</details>

<details>

<summary>Sử dụng 3rd party softwares</summary>

vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và học cách tích hợp, sử dụng các công cụ này.&#x20;

Để xóa một container qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).

\


</details>
