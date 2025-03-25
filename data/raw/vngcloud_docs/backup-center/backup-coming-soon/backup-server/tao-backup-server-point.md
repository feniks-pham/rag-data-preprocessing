# Tạo Backup Server Point

**Backup Server Point** là một bản sao lưu đầy đủ hoặc một phần của dữ liệu máy chủ của bạn tại một thời điểm cụ thể. Việc tạo và quản lý Backup Server Point là vô cùng quan trọng để đảm bảo dữ liệu luôn an toàn và có thể khôi phục khi cần thiết.

**Backup Center** cung cấp cho bạn hai cách linh hoạt để tạo Backup Server Point:

1. Tạo Backup Server Point theo Backup Policy
2. Tạo Backup Server Point thủ công bằng cách thực hiện "Backup Now"

## Tạo Backup Server Point tự động theo Backup Policy

1. **Tạo Backup Plan (Backup Server):** Nếu chưa có, bạn cần tạo một Backup Server mới để thiết lập các quy tắc sao lưu.
2. **Tạo Backup Policy:** Trong Backup Server, bạn tạo và liên kết với một Backup Policy để đáp ứng các nhu cầu sao lưu khác nhau. Ví dụ Policy được cài đặt như sau:
   * Thời gian khởi chạy **16h:00**
   * Tấn suất backup là **mỗi 4 giờ**, hệ thống sẽ tạo một bản backup
   * Khoảng cách giữa 2 bản Backup Full sẽ là **4 bản Backup Incremental**
   * Hệ thống giữ lại **2 bản Backup Full gần nhất.**
3. **Hệ thống tự động thực hiện:** Hệ thống sẽ tự động tạo Backup Server Point theo đúng lịch trình đã đặt như sau:
   * Vào **16h:00** của lần khởi chạy đầu tiên, hệ thống sẽ tạo một backup server point **(bản Full)**.
   * Lần lượt 4 tiếng tiếp theo vào **20h:00, 00h:00, 04h:00 và 08h:00** (ngày hôm sau) sẽ tạo lần lượt một backup server point **(bản Incremental).**
   * Vào 4 tiếng tiếp theo lúc 12h:00, hệ thống sẽ tạo một backup server point **(bản Full).**
   * Cứ tiếp tục mỗi 4 tiếng, hệ thống sẽ tạo các bản backup server point (bản Incremental) cho đến khi đủ 4 bản Incremental, thì lần tiếp theo sẽ là bản backup server point (bản Full).
   * Sau khi tạo được 3 bản backup server point (bản Full), hệ thống sẽ tiến hành xóa backup server point (bản Full) đầu tiên, và 4 bản backup server point (bản Incremental) liên tiếp sau đó.

## Tạo Backup Server Point thủ công bằng cách thực hiện "Backup Now"

Tính năng Backup Now cho phép bạn thực hiện một phiên sao lưu dữ liệu ngay lập tức bằng cách nhấn vào một nút "Backup Now" cho bản Backup Server hoặc Server bạn chọn. Thường thì, người dùng có thể cần thực hiện việc sao lưu định kỳ, nhưng đôi khi cũng cần thực hiện một phiên sao lưu ngay tức thì để bảo vệ dữ liệu quan trọng tại thời điểm đó.

**Lợi ích của Sao lưu Dữ liệu Ngay Lập Tức:**

* **Tính Linh Hoạt và Khẩn Cấp:** Sao lưu dữ liệu ngay lập tức cho phép bạn thực hiện việc sao lưu bất kỳ khi nào bạn cảm thấy cần thiết, thay vì phải chờ đến thời điểm sao lưu định kỳ. Điều này rất hữu ích trong tình huống khẩn cấp hoặc khi bạn muốn bảo vệ dữ liệu ngay lập tức trước một sự cố có thể xảy ra.
* **Bảo Vệ Dữ Liệu Quan Trọng Trong Thời Gian Ngắn:** Nếu bạn chỉ cần sao lưu một phần nhỏ hoặc một dự án cụ thể, việc sao lưu ngay lập tức sẽ giúp bạn bảo vệ những dữ liệu quan trọng mà bạn vừa làm việc trên chúng.
* **Phục Hồi Nhanh Chóng:** Khi bạn cần phục hồi dữ liệu, bạn sẽ có bản sao lưu gần nhất.

**Hướng dẫn chi tiết các bước:**

### Cách 1: Backup now từ Backup Server

1. Truy cập vào trang quản lý Backup Server tại đây: [https://backupcenter.console.vngcloud.vn/backup-server/list](https://backupcenter.console.vngcloud.vn/backup-server/list)
2. Chọn Backup Server cần thực hiện Backup Now.
3.  Tìm và nhấn chọn "Backup Now" như hình bên dưới&#x20;

    <figure><img src="../../../.gitbook/assets/image (764).png" alt=""><figcaption></figcaption></figure>

**Lưu ý:**&#x20;

* Khi backup now, các bản backup server point sẽ là các bản backup full
* Các bản backup server point được tạo ra sẽ thuộc loại Manual và sẽ không bị ảnh hưởng bởi backup policy, người dùng cần chủ động xóa khi không có nhu cầu sử dụng.

### Cách 2: Backup now từ Server

1. Truy cập vào trang quản lý Server tại đây: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Chọn Server cần thực hiện Backup Now.
3.  Tìm và nhấn chọn "Backup Now" như hình bên dưới.&#x20;

    <figure><img src="../../../.gitbook/assets/image (765).png" alt=""><figcaption></figcaption></figure>

**Lưu ý:**&#x20;

* Nếu Server được chọn chưa liên kết với một Backup Server nào, hệ thống sẽ tự động tạo một Backup Server với Backup Policy và Backup Location mặc định, và liên kết với Server này, sau đó mới tiến hành tạo bản backup server point tương ứng.
* Khi backup now, các bản backup server point sẽ là các bản backup full
* Các bản backup server point được tạo ra sẽ thuộc loại Manual và sẽ không bị ảnh hưởng bởi backup policy, người dùng cần chủ động xóa khi không có nhu cầu sử dụng.
