# Sử dụng tính năng container versioning

Version là một thuật ngữ được sử dụng để chỉ một phiên bản của một phần mềm, tài liệu. Chúng tôi cung cấp cho bạn tính năng versioning để làm việc với nhiều phiên bản lưu trữ dữ liệu. Versioning là một tính năng hỗ trợ lưu trữ nhiều phiên bản quá khứ của các object được lưu trữ trong một container. Bạn có thể sử dụng tính năng versioning để lưu giữ, truy xuất và khôi phục mọi phiên bản của object được lưu trữ trong container của bạn. Khi bật tính năng Versioning, khi thực hiện tải lên/ xóa một object thì thay vì xóa hẳn object khỏi hệ thống, chúng tôi sẽ chuyển các object bị xóa hoặc bị ghi đè sang versioning container. Từ đó bạn có thể dễ dàng khôi phục lại các object bị xóa nhầm hoặc tải về các phiên bản cũ của dữ liệu khi có nhu cầu sử dụng.

<details>

<summary> Sử dụng vStorage Portal</summary>

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container** bạn muốn tạo version.

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648511/image2023-3-6\_10-15-7.png?version=1\&modificationDate=1678072508000\&api=v2) hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648511/image2023-2-6\_10-19-45.png?version=1\&modificationDate=1675653587000\&api=v2)tại **container** và chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648511/image2023-3-6\_10-16-20.png?version=1\&modificationDate=1678072581000\&api=v2)tại container bạn muốn thực hiện sử dụng tính năng versioning.

4\. Màn hình **Bật versioning** được hiển thị. Nhập **Tên phiên bản containers.**&#x20;

Sau khi tạo container, bạn không thể thay đổi tên của container. Để biết thêm thông tin về cách đặt tên container, hãy xem [Phạm vi giới hạn container](pham-vi-gioi-han-container.md).

5\. Chọn **Bật versioning.**

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, tính năng container versioning đã được bật. Nếu bạn có nhiều container trong 1 project và tất cả container đều cần sử dụng tính năng versioning, bạn nên đặt tên riêng biệt cho các container versioning và không được tạo nhiều hơn 1 container versioning cho 1 container.&#x20;

Để tải về một version object, hãy xem tại [Tải xuống object](../lam-viec-voi-directory-va-object/tai-xuong-object.md).

<img src="../../../../../.gitbook/assets/Su_dung_container_version.gif" alt="" data-size="original">

</details>

<details>

<summary>Sử dụng vStorage API</summary>

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để sao lưu phiên bản container qua vStorage API, hãy xem [API Developers](../../api-developers/).



</details>

