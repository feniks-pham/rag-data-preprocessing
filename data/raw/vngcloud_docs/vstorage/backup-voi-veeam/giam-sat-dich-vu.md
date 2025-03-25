# Giám sát dịch vụ

## Tổng quan

Việc giám sát và theo dõi các hoạt động sao lưu và phục hồi dữ liệu là một phần quan trọng trong các giải pháp lưu trữ. Khi sử dụng Veeam các quá trình đang thực hiện đồng bộ (chạy job) hay phục hồi dữ liệu, Veeam đều trực quan hiển thị tiến trình xử lý và thông báo kết quả. Bên cạnh đó, để bạn giám sát việc sao lưu backup và phục hồi với những lần đã sao lưu và phục hồi dữ liệu, bạn có thể sử dụng chức năng History của Veeam và để trực quan việc quản lý dữ liệu lưu trữ có thể dùng S3 Browser để giám sát các dữ liệu đã lưu trữ:

* **History:** Theo dõi việc sao lưu và phục hồi;
* **Versions & Event Log:** Giám sát các phiên bản và các tương tác với dữ liệu đã backup.

***

## History - Theo dõi sao lưu và phục hồi&#x20;

Đây là chức năng trong Veeam Backup & Replication, hiển thị các số liệu thống kê cho các hoạt động được thực hiện với Veeam:

* Job: Liệt kê tất cả các Job với thông tin thời điểm sao lưu dữ liệu gần nhất của job đó (cho biết đã backup thành công hay thất bại);
* Restore: Lịch sử tất cả những lần phục hồi dữ liệu (cho biết đã phục hồi thành công hay thất bại);
* System: Lịch sử tất cả các phiên lưu trữ trong cơ sở dữ liệu cấu hình;

## Versions & Event Log

Để kiểm tra các phiên bản dữ liệu backup, bạn có thể xem tại Storage đã sao lưu dữ liệu (vStorage, AWS...). Ở bài viết này đề cập đến một cách đơn giản khác để theo dõi những thông tin này là trên S3 Browser.

Sau khi đã cài đặt và truy cập vào Tài khoản Lưu trữ, tại Bucket/Container mà đã sao lưu dữ liệu, bạn có thể thấy các tab cần thiết cho việc theo dõi việc sao lưu:

* Versions: Liệt kê tất cả phiên bản của dữ liệu sao lưu và cho biết cả thời điểm sao lưu dữ liệu đó là lúc nào;
* Event Log: Liệt kê tất cả các tác vụ mà đã cập nhật bucket/container thành công.

**Ví dụ:**

Trường hợp đã bật **Immutable** để bảo vệ dữ liệu;

Khi đó nếu có sự cố dữ liệu, như xóa mất một version, thì tại Event Log ghi nhận tác vụ "Detele" nhưng cũng sẽ ghi nhận "Access Denied" từ chối việc xóa dữ liệu.

Lúc này với vai trò quản trị, bạn có thể thấy toàn bộ version còn tồn tại và các tác vụ thực hiện tương tác với dữ liệu sao lưu.
