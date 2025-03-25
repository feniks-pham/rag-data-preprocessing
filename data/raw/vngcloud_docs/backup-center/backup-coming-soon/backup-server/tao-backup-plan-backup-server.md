# Tạo Backup Plan (Backup Server)

Để bảo về server thông qua việc tạo các bản backup định kỳ, đầu tiên, bạn cần liên kết server với 1 backup plan (backup server). Backup Center hỗ trợ người dùng server tạo backup plan (backup server) thông qua các cách sau:

* Tạo backup plan và liên kết với server.
* Kích hoạt tạo backup plan khi tạo server

## Tạo backup plan (backup server)

1. Truy cập giao diện Backup Server thuộc Backup Center tại đây:  [https://backupcenter.console.vngcloud.vn/backup-server/list](https://backupcenter.console.vngcloud.vn/backup-server/list)
2. Chọn **Create Backup Server.**
3. Chọn server cần tạo backup, lưu ý rằng trang này chỉ hiển thị những server chưa liên kết backup plan.
4. Chọn backup policy áp dụng cho backup plan (backup server) này. Tìm hiểu thêm về backup policy tại đây.
5. Chọn backup location (nơi lưu trữ các backup server point). Tìm hiểu thêm về backup location tại đây.
6. Điền thông tin mô tả để gợi nhớ (optional).
7. Nhấn **Create**

Sau đó bạn có thể xem thông tin công việc sao lưu vừa tạo tại màn hình danh sách, chọn Backup Server để xem các thông tin về server được bảo vệ và volume đính kèm, backup policy, backup server và kích thước bản backup point cũng như thời gian backup gần nhất.

## Kích hoạt tạo backup plan khi tạo server

Người dùng có thể kích hoạt backup plan (backup server) cùng với việc khởi tạo server để tiết kiệm thời gian, cũng như bảo vệ server một cách toàn diện. Tham khảo các bước hướng dẫn sau

1. Truy cập giao diện Cloud Server.
2. Chọn **Create a server**
3.  Tại trang tạo mới Server bạn có thể tích chọn vào ô **Enable Backup** tại mục **Other settings.**&#x20;

    <figure><img src="../../../.gitbook/assets/image (766).png" alt=""><figcaption></figcaption></figure>
4. Sau đó khi Server được tạ&#x6F;**,** một backup plan (backup server) sẽ được tạo kèm với backup policy và backup location mặc định. Có nghĩa, việc tạo bản backup và vị trí lưu trữ đối với server này sẽ phụ thuộc vào backup policy và backup location mặc định. Bạn có thể tùy ý thay đổi backup policy và backup location sau đó.

