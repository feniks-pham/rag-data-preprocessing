# Quản lý Backup Server Point

Backup Server Point là một bản sao lưu đầy đủ hoặc một phần của dữ liệu máy chủ tại một thời điểm cụ thể. Việc quản lý hiệu quả các Backup Server Point giúp bạn đảm bảo tính liên tục của hoạt động kinh doanh và giảm thiểu rủi ro mất mát dữ liệu.&#x20;

Bài hướng dẫn này sẽ hướng dẫn bạn từng bước để thực hiện các thao tác quản lý Backup Server Point, bao gồm xem danh sách, xem lịch sử, tải về và xóa.

### Xem danh sách backup server point

1. Truy cập vào trang danh sách backup server tại đây: [https://backupcenter.console.vngcloud.vn/backup-server/list](https://backupcenter.console.vngcloud.vn/backup-server/list)
2. Chọn Backup Server cần xem backup server point. Bạn có thể nhấn vào ô tìm kiếm, nhập tên backup server cần tìm. ![](<../../../.gitbook/assets/image (767).png>)
3. Tại trang chi tiết của Backup Server, nhấn chọn tab Restore Point. Tại đây, bạn sẽ thấy danh sách các bản backup server point đã tạo. Thông tin bao gồm:
   1. **Backup Server Point ID** /Định danh backup server point
   2. **Estimated Backup Size** / Dung lượng bản backup
   3. **Backup Type**: Full / Incremental (diff)
   4. **Schedule Type**: Policy (backup tự động theo lịch) / Manual (người dùng thực hiện [backup now](tao-backup-server-point.md))
   5. **Backup Location**: Vị trí lưu trữ các backup server point
   6.  **Status**: Trạng thái bản backup (Active / Failed)

       <figure><img src="../../../.gitbook/assets/image (768).png" alt=""><figcaption></figcaption></figure>
4. Ngoài ra, người dùng có thể thao tác xóa và tải về các bản backup server point từ tab Restore Point này

### Xem lịch sử Backup Server

Để xem lịch sử các lần khởi tạo backup server point, làm theo hướng dẫn sau:

1. Truy cập trang History của Backup Center tại đây: [https://backupcenter.console.vngcloud.vn/backup-history/list](https://backupcenter.console.vngcloud.vn/backup-history/list)
2. Chọn tab Backup History để xem lịch sử các lần khởi tạo backup
3. Nhập Backup Server ID vào ô tìm kiếm để xem lịch sử khởi tạo backup của một backup server. Thông tin hiển thị bao gồm:
   1. **Status:** Trạng thái khởi tạo backup server point (Active -> Tạo thành công; Error -> Tạo thất bại)
   2. **Backup Type**: Full / Incremental (diff)
   3. **Schedule Type**: Policy (backup tự động theo lịch) / Manual (người dùng thực hiện [backup now](tao-backup-server-point.md)).
   4. **Size (GB)**: Dung lượng bản backup
   5. **Time period:** Thời gian khởi tạo backup server point
   6. **Deletion status:**&#x20;
      1. **Trống** (nếu bản backup server point đang tồn tại);&#x20;
      2. **Deleted** (bản backup server point đã bị xóa);&#x20;
      3. **Soft deleted** (bản backup server point đang được xóa tạm thời, có thể khôi phục lại).

<figure><img src="../../../.gitbook/assets/image (769).png" alt=""><figcaption></figcaption></figure>
