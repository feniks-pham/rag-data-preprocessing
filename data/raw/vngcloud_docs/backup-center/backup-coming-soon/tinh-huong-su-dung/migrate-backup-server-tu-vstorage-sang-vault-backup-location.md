# Migrate backup server từ vStorage sang Vault (backup location)

Bài viết này nhằm mục đích hướng dẫn người dùng dịch vụ Backup Server cập nhật vị trí lữu trữ backup server point từ vStorage sang Vault.

Lưu ý rằng, VNG Cloud chỉ khuyến khích người dùng thay đổi vị trí lưu trữ backup server point, vì các [tính năng vượt trội mà Vault (backup location) mang lại](../backup-location/). Do đó, nếu không có nhu cầu thay đổi, người dùng vẫn có thể tiếp tục lưu trữ backup tại vStorage mà không hề ảnh hưởng đến chất lượng dịch vụ backup server.

Làm theo hướng dẫn dưới đây để cập nhật vị trí lưu trữ mới cho các backup server của bạn:

## 1. Tạo mới một backup location

Đầu tiên, bạn cần tạo mới một backup location để chuẩn bị cho việc thay đổi vị trí lưu trữ của backup server.

* **Đăng nhập:** Đăng nhập vào tài khoản quản lý dịch vụ VNG Cloud.
* **Truy cập vào phần quản lý Backup Location:** Tìm và chọn mục "Backup Location" tại đây [https://backupcenter.console.vngcloud.vn/backup-location/list](https://backupcenter.console.vngcloud.vn/backup-location/list)
* **Tạo mới:** Nhấp vào nút "Create backup location", một cửa sổ giao diện hiện lên cho bạn điền các thông tin cần thiết.
* **Điền thông tin:**
  * **Tên vị trí:** Đặt tên dễ nhớ và mô tả cho vị trí lưu trữ.
  * **Vùng lưu trữ (Backup region):** Chọn vùng địa lý nơi muốn lưu trữ bản sao lưu.
  * **Dung lượng tối đa (Max quota):** Xác định giới hạn dung lượng tối đa cho vị trí lưu trữ.
  * **Soft Delete:**
    * **Bật/tắt:** Quyết định có cho phép soft delete bản sao lưu hay không.
    * **Thời gian giữ dữ liệu (Retention day):** Nếu bật soft delete, nhập số ngày bản sao lưu sẽ được giữ trước khi xóa vĩnh viễn.
  * **Đặt làm vị trí mặc định:** Chọn backup location này làm vị trí lưu trữ mặc định cho các bản sao lưu mới.
  * **Location Lock:**
    * **Thời gian giữ dữ liệu tối thiểu (Min retention day):** Thời gian ngắn nhất mà bản sao lưu phải được giữ lại.
    * **Thời gian giữ dữ liệu tối đa (Max retention day):** Thời gian dài nhất mà bản sao lưu được giữ lại.
    * **Thời gian thay đổi (Change duration):** Trong thời gian này, người dùng có thể thay đổi các cấu hình về Min và Max retention day, cũng như tắt tính năng Lock. Khi vượt qua thời gian này, cấu hình trên tính năng Lock sẽ không thể thay đổi.
* **Lưu:** Nhấp vào nút "Lưu" để hoàn tất. Backup location mới tạo sẽ có type mặc định là Vault

## 2. Chọn các backup server cần thay đổi vị trí lưu trữ

Tiếp theo, bạn cần truy cập vào trang backup server để chọn các backup server cần thay đổi vị trí lưu trữ

* **Truy cập trang backup server** tại đây: [https://backupcenter.console.vngcloud.vn/backup-server/list](https://backupcenter.console.vngcloud.vn/backup-server/list)
* **Tìm và chọn backup server lưu tại vStorage project:**
  * Đầu tiên, bạn cần **xác định tên của vị trí lưu trữ cũ** bằng cách truy cập vào backup location, xác định tên của backup location có **type = vStorage** như hình dưới đây ![](<../../../.gitbook/assets/image (773).png>)
  *   Tiếp theo, truy cập trang **backup serve**r, chọn các backup server có nơi lưu trữ là **vBackup-Project-5fa985c8** (lưu ý rằng, tên này sẽ thay đổi tùy vào từng người dùng).&#x20;

      <figure><img src="../../../.gitbook/assets/image (774).png" alt=""><figcaption></figcaption></figure>

## 3. Tìm và nhấn chọn change location

Sau khi chọn xong các backup server cần thay đổi, nhấn chọn tính năng **Change Location**, một giao diện sẽ hiển thị cho phép bạn chọn vị trí lưu trữ mới cho các backup server này.

*   Chọn nơi lưu trữ mới cho backup server như hình bên dưới&#x20;

    <figure><img src="../../../.gitbook/assets/image (775).png" alt=""><figcaption></figcaption></figure>
* Nhấn **"Change"** để xác nhận hoàn tất thay đổi.

## 4. Lưu backup server point tại nơi lưu trữ mới

Sau khi hoàn tất thay đổi, bạn có thể vào trang [backup server](https://backupcenter.console.vngcloud.vn/backup-server/list) để xem backup location mới được ghi nhận lại. Lưu ý rằng:

* **Lịch chạy backup** và **retention rules** vẫn theo backup policy,  chỉ khác là các backup server point mới được tạo ra, sẽ được lưu trữ tại backup location mới.
* Các **backup server point được lưu trữ tại vBackup-Project** trước đó không có gì thay đổi, người dùng vẫn có thể truy cập khi cần thiết.
* VNG Cloud khuyến nghị khách hàng nên tải về các backup server point cần dùng, và xóa **vBackup-Project** để tránh phát sinh chi phí lưu trữ tại vStorage sau khi đã **chuyển hết backup server qua backup location mới** và **đã phát sinh lưu trữ các backup server point (Full)** tại đây.
