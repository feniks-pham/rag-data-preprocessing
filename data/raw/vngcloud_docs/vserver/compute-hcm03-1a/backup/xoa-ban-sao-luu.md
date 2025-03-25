# Xóa bản sao lưu

Sau khi tạo bản sao lưu, bạn có thể thực hiện xóa chúng. Chúng tôi khuyên bạn nên sử dụng vBackup Policy để tự động xóa các bản sao lưu mà bạn không cần nữa bằng cách định cấu hình vòng đời của bạn khi bạn tạo gói sao lưu. Ví dụ: Nếu bạn tạo bản sao lưu với một chính sách sao lưu được lựa chọn tần suất sao lưu theo **Hàng Ngày** lúc **12:00** và số bản lưu **4** vào ngày 16/03/2023. Vào ngày hôm sau 17/03/2023, lúc 12:00 trưa, hệ thống theo khung giờ trên sẽ tạo bản sao lưu cho máy chủ ảo, và lưu giữ dưới hệ thống, sau đó sẽ tiếp tục tạo các bản sao lưu vào các ngày 18,19,20. Tuy nhiên tới ngày 21/03/2023, khi hệ thống tạo bản sao lưu, bản sao lưu của ngày 17/03/2023 sẽ tự động bị xoá. Để tìm hiểu thêm về cách định cấu hình chính sách lưu giữ vòng đời của bản sao lưu, hãy xem [Cấu trúc bộ lịch Policy](chinh-sach-sao-luu/cau-truc-bo-lich-policy.md).

Tuy nhiên, bạn có thể muốn xóa thủ công một hoặc nhiều điểm khôi phục. Ví dụ:

Bạn tạo bản Backup Now. Đây là những điểm khôi phục mà vBackup không thể tự động xóa. Khi vBackup cố gắng xóa chúng, nó không có quyền làm như vậy, vBackup chỉ có quyền xoá với các bản sao lưu dưới hiệu lực của Policy, cón các bản tạo bởi Backup now, nó vô hiệu.

{% hint style="info" %}
**Quan trọng**

Nếu bạn tiếp tục lưu trữ các điểm khôi phục không cần thiết trong tài khoản của mình. Điều này có thể làm tăng chi phí lưu trữ của bạn.
{% endhint %}

Bạn không còn muốn một gói dự phòng hoạt động theo cách bạn đã định cấu hình. Việc cập nhật kế hoạch sao lưu sẽ ảnh hưởng đến các điểm khôi phục trong tương lai mà nó sẽ tạo, nhưng không ảnh hưởng đến điểm khôi phục mà nó đã tạo. Để tìm hiểu thêm, hãy xem [Cập nhật chính sách sao lưu](chinh-sach-sao-luu/).

***

### **Xóa bản sao lưu bằng cách thủ công trên trình điều khiển vBackup** <a href="#xoabansaoluu-xoabansaoluubangcachthucongtrentrinhdieukhienvbackup" id="xoabansaoluu-xoabansaoluubangcachthucongtrentrinhdieukhienvbackup"></a>

1. Truy cập vào bảng điều khiển vBackup tại: [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-server](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-server)
2. Chọn vào xem chi tiết bản Backup Server bằng cách nhấn vào tên
3. Tại trang chi tiết, chọn **Tab Restore Point,** tại đây sẽ hiển thị các bản Backup tại các điểm khôi phục khác nhau được tạo theo thời gian của bộ lịch Policy
4. Chọn bản Backup Server hoặc Backup Volume bạn cần xóa sau đó nhấn vào biểu tượng **Delete**
