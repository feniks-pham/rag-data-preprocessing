# Bước 4: Phục hồi dữ liệu trên Veeam

Bạn đã tạo được Repository và Job trên phần mềm Veeam Backup & Replication. Bây giờ bạn đã có thể  thực hiện phục hồi dữ liệu khi có sự cố xảy ra với những cấu hình tr6en Veeam đã tạo.

### Thực hiện Phục hồi dự liệu theo những bước sau:

1. Tại **Home**, chọn mục **Backups/Object Storage,** chọn Job đã backup , chọn máy Computer). Nhấn chuột phải chọn "**Restore guest files**" rồi chọn "Microsoft Windows" **;**
2. Tại màn hình "File Level Restore", tại Tab "**Restore Point**", bạn chọn thời điểm backup phù hợp muốn lấy lại dữ liệu, sau đó nhấn "**Next**".
3. Tại màn hình "Reason", điền lý do cần phục hồi dữ liệu, sau đó nhấn "**Next**".
4. Tại tab "Summary", sau đó nhấn "**Browse**".
5. Màn hình giao diện Backup Browse hiện ra, chọn đến folder cần restore dữ liệu;
6. Chọn Nút "**Restore**" trên thanh menu, chọn "**Overwrite**";
7. Hệ thống tự động chạy phục hồi dữ liệu, sau khi phục hồi hoàn tất thì nhấn "**Close**".

***

### Video hướng dẫn cài đặt&#x20;

Đang cập nhật.

***

### Ví dụ hướng dẫn Phục hồi dữ liệu với Phiên bản Veeam Backup & Replication 12

Hướng dẫn sau đây để phục hồi (restore) lại dữ liệu khi gặp sự cố sự cố mất file

Ở đây Dữ liệu ở Mục E:\Backup\_Veem có dữ liệu "Backup File" bị hỏng (hoặc bị mất) để phục hồi thì thực hiện các bước sau:

<figure><img src="../../../.gitbook/assets/image (372).png" alt="" width="260"><figcaption></figcaption></figure>

**Bước 1:** Tại **Home**, chọn mục **Backups/Object Storage**

Tại đây, người dùng chọn Job đã backup cho folder đã backup, sau đó chọn máy (Computer) mà Job chạy backup. Nhấn chuột phải chọn "**Restore guest files**" rồi chọn "**Microsoft Windows**".

<figure><img src="../../../.gitbook/assets/image (373).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 2:** Giao diện "**File Level Restore**" hiện ra, tại Tab "**Restore Point**", tất cả thời điểm đã backup sẽ liệt kê, người dùng chỉ chọn thời điểm backup phù hợp muốn lấy lại dữ liệu. Sau đó nhấn "**Next**".

<figure><img src="../../../.gitbook/assets/image (374).png" alt="" width="559"><figcaption></figcaption></figure>

**Bước 3:** Tại tab "**Reason**", người dùng có thể điền mô tả lý do cần restore phục hồi file. sau đó nhấn "**Next**".

<figure><img src="../../../.gitbook/assets/image (375).png" alt="" width="559"><figcaption></figcaption></figure>

**Bước 4:** Tại tab "**Summary**", hiển thị tổng kết những thông tin phục hồi dữ liệu. Sau đó nhấn "**Browse**".

<figure><img src="../../../.gitbook/assets/image (376).png" alt=""><figcaption></figcaption></figure>

**Bước 5:** Màn hình giao diện Backup Browse hiện ra, chọn đến folder cần restore dữ liệu. (Có thể thấy được "file đã mất" cần phục hồi có trong phần backup.

<figure><img src="../../../.gitbook/assets/image (378).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 6:** Chọn Nút "**Restore**" trên thanh menu, chọn "**Overwrite**" (chép đè lên những đang tồn tại).

<figure><img src="../../../.gitbook/assets/image (379).png" alt="" width="258"><figcaption></figcaption></figure>

**Bước 7**: Hệ thống tự động chạy phục hồi dữ liệu:

<figure><img src="../../../.gitbook/assets/image (380).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 8**: Khi hệ thống xử lý hoàn tất, người dùng có thể thấy "file đã mất" được phục hồi thành công .

<figure><img src="../../../.gitbook/assets/image (381).png" alt="" width="563"><figcaption></figcaption></figure>

Hoàn tất việc phục hồi dữ liệu.
