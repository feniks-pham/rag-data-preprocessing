# Changing the Backup Policy

1. Đăng nhập vào bảng điều khiển vBackup tại: [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-server](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-server). Bạn phải đăng nhập với tư cách người dùng IAM, đảm nhận vai trò IAM account hoặc đăng nhập với tư cách Root user account (không được khuyến nghị) trong tài khoản quản lý của tổ chức.
2. Tại tab Backup Server, chỉ định Backup Server sau đó hãy chọn **Thay đổi Policy**
3. Tìm chính sách mà bạn muốn thay đổi, rồi chọn **Áp dụng**, lưu ý rằng: bạn có thể thay đổi Policy đồng thời cho một hoặc nhiều Backup Server.

**Để thay đổi chính sách sao lưu cho bản Backup Server:**

Để thay đổi các chính sách sao lưu, bạn phải có quyền chạy hành động sau:\
IAM: UpdateBackupPolicy

**Quyền tối thiểu**

Khi đăng nhập vào tài khoản trên bảng điều khiển vServer, bạn có thể đính kèm chính sách sao lưu khi khởi tạo Backup Server, và sau đó, có thể thay đổi lại chính sách sao lưu khác tùy theo nhu cầu sử dụng

### **Thay đổi chính sách sao lưu** <a href="#thaydoichinhsachsaoluu-thaydoichinhsachsaoluu" id="thaydoichinhsachsaoluu-thaydoichinhsachsaoluu"></a>

***

* Khi bạn đính kèm một chính sách sao lưu vào Backup Server, chính sách này sẽ áp dụng cho tất cả các Volume được đính kèm với Server đó.
* Bạn chỉ có thể đính kém duy nhất 1 chính sách sao lưu cho Backup Server, nếu bạn muốn thay đổi chính sách khác, hãy tách chính sách sao lưu cũ và đính kèm chính sách sao lưu mới vào.
* Ngoài những chính sách sao lưu bạn tự tạo, chúng tôi đã tạo sẵn các chính sách sao lưu mặc định với hiệu quả tối ưu, vì thế hãy cân nhắc sử dụng chúng.

Bạn có thể thay đổi chính sách sao lưu khác cho Backup Server. Hãy ghi nhớ những điểm sau:

\


\
