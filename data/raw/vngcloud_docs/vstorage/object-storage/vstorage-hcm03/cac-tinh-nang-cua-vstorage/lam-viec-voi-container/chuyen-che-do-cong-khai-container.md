# Chuyển chế độ công khai container

Sau khi bạn khởi tạo container, ở cấu hình mặc định container của bạn sẽ có trạng thái riêng tư. Bạn có thể chuyển chế độ của container từ riêng tư thành công khai để cho phép bất kỳ ai cũng có thể truy cập vào container để xem, tải xuống, tải lên tất cả tệp tin, object thuộc container được công khai. vStorage hỗ trợ quyền công khai dữ liệu cho người dùng ẩn danh tùy chọn theo từng container. Tính năng này được gọi là **Public container**. **Public container** là tính năng cho phép người dùng chia sẻ công khai container trên môi trường điện toán đám mây. Người dùng từ ngoài internet có thể truy cập vào container thông qua đường dẫn URL mà không cần chứng thực quyền truy cập với hệ thống. Quyền truy cập công khai tiềm ẩn rủi ro bảo mật, vì vậy nếu kịch bản của bạn không yêu cầu quyền truy cập đó, chúng tôi khuyên bạn không nên cho phép quyền truy cập công khai đối với container. Tại bất kỳ thời điểm nào bạn không muốn công khai container đó nữa thì có thể chuyển chế độ riêng tư cho container.&#x20;

<details>

<summary>Sử dụng vStorage Portal</summary>

Trước khi có thể thực hiện chuyển chế độ công khai container, bạn cần thực hiện phân quyền truy cập ACLs container cho toàn bộ người dùng, chi tiết tham khảo tại [Phân quyền truy cập ACLs container](phan-quyen-truy-cap-acls-container.md).

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container** bạn muốn chuyển chế độ công khai.

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648685/image2023-3-6\_10-20-30.png?version=1\&modificationDate=1678072831000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648685/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1675653656000\&api=v2)tại **container** bạn muốn thực hiện sử dụng tính năng chuyển chế độ công khai và chọn![](https://docs.vngcloud.vn/download/thumbnails/49648685/image2023-3-6\_10-21-8.png?version=1\&modificationDate=1678072869000\&api=v2)**.**

4\. Màn hình **Chuyển chế độ công khai** được hiển thị. Chọn **Chuyển chế độ công khai.**

Sau khi bạn hoàn thành 4 bước được mô tả bên trên, tính năng Public container đã được bật. Quyền truy cập công khai được cấp cho container và object thông qua danh sách kiểm soát truy cập (ACLs). Cài đặt này cho phép mọi người truy cập vào tất cả các object bên trong container với các quyền truy cập được chỉ định thông qua danh sách kiểm soát truy cập (ACLs). Để xem thêm thông tin về tính năng Thiết lập ACLS, hãy xem [Phân quyền truy cập ACLs container](phan-quyen-truy-cap-acls-container.md).

<img src="../../../../../.gitbook/assets/Chuyen_che_do_cong_khai_container.gif" alt="" data-size="original">

</details>

&#x20;

<details>

<summary>Sử dụng vStorage API</summary>

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để chuyển chế độ công khai container qua vStorage API, hãy xem [API Developers](../../api-developers/).

</details>

