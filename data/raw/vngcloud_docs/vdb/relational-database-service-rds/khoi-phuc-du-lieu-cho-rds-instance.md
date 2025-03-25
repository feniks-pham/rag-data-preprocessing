# Khôi phục dữ liệu cho RDS Instance

VNG Cloud vDB hỗ trợ bạn khôi phục (Restore) lại một RDS Instance mới từ bản sao lưu (Backup) trước đó. Quá trình khôi phục này không phụ thuộc vào loại Backup (Full Backup hay Incremetal Backup) hay cách tạo ra bản backup đó (Manual Backup hay Automactic Daily Backup).

Để thực hiện tiến trình khôi phục, bạn truy cập màn hình quản lý Backup vDB Relational [tại đây](https://vdb.console.vngcloud.vn/relational/backup).

Tại đây, bạn click chọn vào bản Backup mà bạn muốn khôi phục, chọn Action **Restore**.

Quá trình Restore cũng gần tương tự như quá trình **Khởi tạo một RDS Instance** mới.&#x20;

* Bước 1 Cấu hình cơ bản: bạn có thể đặt tên cho RDS Instance mới này.
* Bước 2 Thông số kỹ thuật: bạn có thể tùy chỉnh cấu hình Flavor (CPU/Memory), Storage Type và Storage Size.
* Bước 3 Mạng và bảo mật: bạn có lựa chọn Cloud Network & bật/tắt khả năng truy cập từ Internet (**Public Accessibility**). Cloud Network ở đây có thể giống hoặc khác Cloud Network của RDS Instance cũ.
* Bước 4 Tùy chọn DB: tại mục DB Options, bạn có thể lựa chọn **DB Configuration Group (Optional)** cho RDS Instance này. Lựa chọn này cũng có thể giống hoặc khác so với RDS Instance cũ.
* Bước 5 Cài đặt sao lưu: cài đặt bật/tắt sao lưu tự động, cũng như các thông tin về backup retention day và backup time

Sau khi chắc chắn các thông tin đã chính xác, bạn nhấp nút **Restore Backup**.

Sau đó, bạn quay lại màn hình quản lý Database, sẽ thấy xuất hiện một RDS Instance đang được khôi phục.

Trạng trái của RDS Instance mới này cũng sẽ thay đổi từ Building/Build sang Active nếu thành công.

Thông tin **Master User,** **Databases name** sẽ được giữ nguyên như cũ.

Khi khôi phục thành công, RDS Instance mới sẽ có trạng thái **Active**.
