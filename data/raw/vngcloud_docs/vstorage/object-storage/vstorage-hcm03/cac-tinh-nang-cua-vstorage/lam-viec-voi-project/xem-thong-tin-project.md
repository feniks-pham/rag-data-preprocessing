# Xem thông tin project

Sau khi tạo project và thực hiện hành động trên project đó. Bạn có thể xem và sử dụng các thuộc tính cho project bao gồm thông tin chung của project, các member truy cập, các cặp S3 key được tạo, lịch sử tác động cũng như thông tin kết nối project với S3,...

Để xem các thuộc tính cho một project, bạn có thể:&#x20;

&#x20;Sử dụng vStorage Portal

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn/storage](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648432/image2023-2-1\_14-25-3.png?version=1\&modificationDate=1675236304000\&api=v2) tại **project** bạn muốn xem chi tiết.

3\. Trên trang hiển thị thông tin chi tiết **project**, bạn có thể xem và sử dụng các thuộc tính cho project&#x20;

* **Thông tin**: Cung cấp các thông tin chung của project như Tổng quota, Tổng lưu lượng, Tổng dung lượng sử dụng, Tổng số request tới project, Tổng lượt tải xuống, Tổng lượt tải lên, Project type, Account URL, Temp URL key. Bạn có thể xem chi tiết mức độ thay đổi lưu lượng, dung lượng sử dụng theo từng khoảng thời gian mong muốn bằng cách chọn **Chi tiết** trong các phần thông tin này.
* **Thành viên**: Cung cấp thông tin member được thêm quyền truy cập vào project từ vStorage Portal cũ. Chúng tôi chỉ hỗ trợ tính năng **Thêm thành viên** trên vStorage Portal cũ. Bây giờ bạn có thể phân quyền truy cập cho người dùng từ hệ thống phân quyền truy cập vIAM mà VNG Cloud cung cấp. Tham khảo thêm tại: [Phân quyền truy cập](../../quan-ly-truy-cap/).
* **IP range ACLs:** Cung cấp thông tin các IP/ Subnet được thêm quyền truy cập vào project. Tham khảo thêm tại: [Sử dụng tính năng IP range ACLs project](su-dung-tinh-nang-ip-range-acls-project.md).
* **S3 key**: Cung cấp thông tin các cặp S3 key được khởi tạo cho project từ vStorage Portal cũ. Chúng tôi chỉ hỗ trợ tính năng **Khởi tạo S3 key** trên vStorage Portal cũ. Bây giờ bạn có thể khởi tạo các cặp S3 key từ hệ thống phân quyền truy cập vIAM mà VNG Cloud cung cấp. Tham khảo thêm tại: [Phân quyền truy cập](../../quan-ly-truy-cap/).
* **Lịch sử**: Cung cấp thông tin lịch sử tác động tới project bao gồm loại hành động, trạng thái hành động, thời gian hành động xảy ra và mô tả chi tiết hành động nếu có.&#x20;
* **Thông tin kết nối**: Cung cấp các câu lệnh và tệp tin cấu hình để kết nối project với S3.&#x20;



<figure><img src="../../../../../.gitbook/assets/Xem_thong_tin_project.gif" alt=""><figcaption></figcaption></figure>
