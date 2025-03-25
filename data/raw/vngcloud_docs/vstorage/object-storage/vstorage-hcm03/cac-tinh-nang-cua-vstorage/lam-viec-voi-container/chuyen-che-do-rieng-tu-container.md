# Chuyển chế độ riêng tư container

vStorage hỗ trợ chế độ riêng tư (Private container) mặc định cho từng container. Chế độ này được sử dụng khi bạn cần chuyển chế độ công khai (Public container) sang chế độ riêng tư (Private container). Tính năng để chuyển chế độ công khai sang chế độ riêng tư được gọi là **Private container**. Private container là tính năng cho phép người dùng dừng việc chia sẻ công khai container trên môi trường điện toán đám mây. Bạn sẽ không thể truy cập vào container thông qua đường dẫn URL mà cần chứng thực quyền truy cập.

<figure><img src="https://www.vngcloud.vn/documents/20126/1455799/vng-cloud-product-vstorage-acl-vi-01-slideshow.jpg" alt=""><figcaption></figcaption></figure>

<details>

<summary>Sử dụng vStorage Portal</summary>

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container** bạn muốn chuyển chế độ riêng tư.

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648509/image2023-3-6\_10-24-4.png?version=1\&modificationDate=1678073045000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648509/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1675653984000\&api=v2)tại **container** bạn muốn thực hiện sử dụng tính năng chuyển chế độ riêng tư và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648509/image2023-3-6\_10-24-29.png?version=1\&modificationDate=1678073070000\&api=v2)**.**

4\. Màn hình **Chuyển chế độ riêng tư** được hiển thị. Chọn **Chuyển chế độ riêng tư.**

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, tính năng Private container đã được bật. Quyền truy cập riêng tư được cấp cho container và object thông qua danh sách kiểm soát truy cập (ACLs). Cài đặt này hạn chế mọi người truy cập vào tất cả các object bên trong container với các quyền truy cập được chỉ định thông qua danh sách kiểm soát truy cập (ACLs).

<img src="../../../../../.gitbook/assets/Chuyen_che_do_rieng_tu.gif" alt="" data-size="original">

</details>



<details>

<summary>Sử dụng vStorage API</summary>

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để chuyển chế độ riêng tư container qua vStorage API, hãy xem [API Developers](../../api-developers/).

</details>

