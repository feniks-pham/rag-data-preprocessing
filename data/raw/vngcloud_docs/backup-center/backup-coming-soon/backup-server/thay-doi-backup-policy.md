# Thay đổi backup policy

Việc cập nhật backup policy là một hoạt động thường xuyên để đảm bảo dữ liệu được bảo vệ một cách hiệu quả và phù hợp với nhu cầu hiện tại. Bài hướng dẫn này sẽ hướng dẫn bạn cách cập nhật chính sách sao lưu trên backup server, bao gồm việc thay đổi lịch trình sao lưu, quy tắc giữ dữ liệu (retention rule) và các cấu hình khác.

**Có 2 cách để thay đổi policy đang áp dụng tại một backup server:**

* Chuyển áp dụng từ backup policy này sang backup policy khác.
* Chỉnh sửa trực tiếp trên backup policy đang áp dụng.

**Hướng dẫn dưới đây giúp bạn cập nhật policy được áp dụng tại một backup server sang một policy khác:**

## 1. Chọn backup server cần thay đổi policy

Đầu tiên, bạn cần truy cập vào trang backup server để chọn các backup server cần thay đổi policy

* Truy cập trang backup server tại đây: [https://backupcenter.console.vngcloud.vn/backup-server/list](https://backupcenter.console.vngcloud.vn/backup-server/list)
*   Tìm và **chọn các backup server** cần cập nhật policy, sau đó nhấn chọn **Change policy.**&#x20;

    <figure><img src="../../../.gitbook/assets/image (780).png" alt=""><figcaption></figcaption></figure>

## 2. Chọn policy mới để áp dụng tại các backup server vừa chọn

Sau khi chọn **Change policy**, một giao diện sẽ hiển thị cho phép bạn chọn một backup policy để áp dụng cho các backup server này. Tiếp theo, nhấn **"Apply"** để hoàn tất quá trình thay đổi

<figure><img src="../../../.gitbook/assets/image (781).png" alt=""><figcaption></figcaption></figure>

## 3. Tự động áp dụng policy mới tại backup server

Sau khi xác nhận áp dụng thành công, một phút sau, hệ thống sẽ tự động áp dụng policy mới lên các backup server point của các backup server vừa thay đổi. Tham khảo ví dụ sau để hiểu thêm về cách vận hành:

* **Policy cũ:** Chạy lúc **00:00** hàng ngày, cách **6 tiếng chạy 1 lần**, giữ **2 backup full** và có **4 backup incremental** giữa 2 bản full.
* **Policy mới:** Chạy lúc **00:00** hàng ngày, cách **6 tiếng chạy 1 lần**, giữ **1 backup full** và có **3 backup incremental** giữa 2 bản full.
* Tại thời điểm xác nhận thay đổi:
  * Thời gian thực hiện: 15h
  * Số lượng backup server point: 2 bản backup full và 4 backup incremental.
* **Hệ thống cập nhật backup server point theo policy mới:**
  * Thời gian thực hiện: 15h01
  * Tác vụ: Chỉ giữ lại 1 bản backup full (gần nhất) và 3 bản backup incremental (gần nhất).
* **Sau khi cập nhật backup server point theo policy mới, lịch backup sẽ hoạt động theo policy đã cập nhật như sau:**
  * Lần tạo backup tiếp theo: 18h00
  * Loại backup server point được tạo: 1 Backup Full được tạo, và xóa 1 Backup Full trước đó (theo policy mới)
