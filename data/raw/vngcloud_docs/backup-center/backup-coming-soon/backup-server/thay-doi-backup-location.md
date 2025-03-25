# Thay đổi backup location

Backup point là một phần quan trọng trong chiến lược bảo vệ dữ liệu của bạn. Việc lựa chọn vị trí lưu trữ phù hợp sẽ giúp đảm bảo tính an toàn và hiệu quả của các bản sao lưu. Nếu bạn muốn thay đổi vị trí lưu trữ backup point, bài viết này sẽ cung cấp cho bạn những hướng dẫn chi tiết và dễ hiểu.

Đầu tiên, bạn cần có sẵn một vị trí lưu trí (backup location) sẵn sàng cho việc lưu trữ backup point mới:

* Tham khảo bài viết hướng dẫn khởi tạo backup location [tại đây](../backup-location/tao-va-quan-ly-backup-location.md#tao-backup-location).

Nếu đã có backup location sẵn sàng cho việc lưu trữ backup point, làm theo các bước dưới đây để cập nhật backup location mới cho backup server của bạn:

## 1. Chọn các backup server cần thay đổi vị trí lưu trữ

Đầu tiên, bạn cần truy cập vào trang backup server để chọn các backup server cần thay đổi vị trí lưu trữ

* Truy cập trang backup server tại đây: [https://backupcenter.console.vngcloud.vn/backup-server/list](https://backupcenter.console.vngcloud.vn/backup-server/list)
*   Tìm và **chọn các backup server** cần cập nhật vị trí lưu trữ, sau đó nhấn chọn **Change location**&#x20;

    <figure><img src="../../../.gitbook/assets/image (779).png" alt=""><figcaption></figcaption></figure>

## 2. Chọn vị trí lưu trữ mới (backup location)

Sau khi chọn **Change Location**, một giao diện sẽ hiển thị cho phép bạn chọn vị trí lưu trữ mới cho các backup server này.

*   Chọn nơi lưu trữ mới cho backup server như hình bên dưới&#x20;

    <figure><img src="../../../.gitbook/assets/image (775).png" alt=""><figcaption></figcaption></figure>
* Nhấn **"Change"** để xác nhận hoàn tất thay đổi.

## 3. Lưu backup server point tại nơi lưu trữ mới

Sau khi hoàn tất thay đổi, bạn có thể vào trang [backup server](https://backupcenter.console.vngcloud.vn/backup-server/list) để xem backup location mới được ghi nhận lại. Lưu ý rằng:

* **Lịch chạy backup** và **retention rules** vẫn theo backup policy,  chỉ khác là các backup server point mới được tạo ra, sẽ được lưu trữ tại backup location mới.
* Các **backup server point được lưu trữ tại backup location** trước đó không có gì thay đổi, người dùng vẫn có thể truy cập khi cần thiết.
