# Tạo và Quản lý backup location

Backup Location là một tính năng hữu ích cho phép bạn tạo ra các vị trí lưu trữ riêng biệt để bảo vệ các bản sao lưu dữ liệu của mình. Việc sử dụng nhiều Backup Location giúp bạn quản lý dữ liệu một cách hiệu quả, linh hoạt và an toàn hơn.

**Hướng dẫn này sẽ giúp bạn:**

* Hiểu rõ khái niệm Backup Location và tầm quan trọng của nó.
* Tự mình tạo và quản lý các Backup Location.
* Cấu hình các tính năng như Soft Delete và Location Lock để bảo vệ dữ liệu tối ưu.

### Tạo Backup Location

#### Mục tiêu:

* Tạo một vị trí lưu trữ an toàn và tùy chỉnh cho các bản sao lưu.
* Quản lý hiệu quả các bản sao lưu dựa trên các tiêu chí khác nhau.

#### Các bước thực hiện:

1. **Đăng nhập:** Đăng nhập vào tài khoản quản lý dịch vụ VNG Cloud.
2. **Truy cập vào phần quản lý Backup Location:** Tìm và chọn mục "Backup Location" tại đây [https://backupcenter.console.vngcloud.vn/backup-location/list](https://backupcenter.console.vngcloud.vn/backup-location/list)
3. **Tạo mới:** Nhấp vào nút "Create backup location", một cửa sổ giao diện hiện lên cho bạn điền các thông tin cần thiết.
4. **Điền thông tin:**
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
5. **Lưu:** Nhấp vào nút "Lưu" để hoàn tất.

#### Lợi ích khi sử dụng:

* **Phân loại dữ liệu:** Tạo nhiều Backup Location để phân loại dữ liệu theo dự án, bộ phận hoặc mức độ quan trọng.
* **Quản lý hiệu quả:** Dễ dàng theo dõi dung lượng sử dụng, thời gian giữ dữ liệu của từng vị trí.
* **Tối ưu hóa chi phí:** Chọn loại lưu trữ phù hợp với từng vị trí để tiết kiệm chi phí.
* **Bảo mật:** Tăng cường bảo mật dữ liệu bằng cách phân quyền truy cập vào các vị trí lưu trữ khác nhau.

### Bật tính năng Soft Delete

#### Mục tiêu:

* Ngăn chặn việc xóa vĩnh viễn các bản sao lưu một cách vô tình.
* Cho phép khôi phục dữ liệu đã xóa trong một khoảng thời gian nhất định.

#### Cách hoạt động:

* Khi một bản sao lưu được đánh dấu xóa, nó sẽ không bị xóa ngay lập tức mà được chuyển vào thùng rác ảo.
* Người dùng có thể khôi phục bản sao lưu này trong khoảng thời gian quy định (retention day).
* Sau khi hết thời gian giữ dữ liệu, bản sao lưu sẽ bị xóa vĩnh viễn.

#### Các bước bật tính năng:

Người dùng có thể bật tính năng soft delete trong lúc khởi tạo backup location, hoặc bật tính năng này sau khi khởi tạo. Để bật tính năng soft delete cho một backup location hiện hữu, làm theo hướng dẫn sau:

* **Truy cập vào Backup Location:** Tìm và chọn Backup Location muốn bật tính năng Soft Delete.
*   **Bật Soft Delete:** Tìm và bật tùy chọn "Edit Soft Delete".&#x20;

    <figure><img src="../../../.gitbook/assets/image (752).png" alt=""><figcaption></figcaption></figure>
* **Cấu hình thời gian giữ dữ liệu:** Nhập số ngày muốn giữ dữ liệu trong thùng rác ảo.
* **Lưu:** Nhấp vào nút "Lưu" để hoàn tất.

#### Lợi ích:

* **Tránh mất dữ liệu:** Ngăn ngừa việc xóa nhầm các bản sao lưu quan trọng.
* **Tăng tính linh hoạt:** Cho phép khôi phục dữ liệu đã xóa khi cần thiết.

#### Lưu ý:

* Đối với các bản backup server point đang được lưu tạm trong thùng rác ảo, người dùng vẫn bị tính phí lưu trữ cho các bản backup này cho đến khi nó được xóa vĩnh viễn.
* Trong trường hợp tắt tính năng Soft Delete, các bản backup (backup server point) đang được lưu tạm trong thùng rác ảo sẽ bị xóa vĩnh viễn ngay lập tức.

### Bật tính năng Location Lock

#### Mục tiêu:

* Bảo vệ các bản sao lưu quan trọng khỏi bị xóa hoặc sửa đổi trái phép.
* Đảm bảo tuân thủ các quy định về lưu trữ dữ liệu.

#### Cách hoạt động:

* **Giữ dữ liệu tối thiểu:** Bản sao lưu phải được giữ lại ít nhất trong khoảng thời gian quy định (min retention day).
* **Giữ dữ liệu tối đa:** Bản sao lưu sẽ bị xóa tự động sau khi vượt quá thời gian quy định (max retention day).
* **Khóa thay đổi cấu hình:** Việc tắt và thay đổi cấu hình của tính năng Location Lock sẽ bị vô hiệu hóa sau khoảng thời gian được phép chỉnh sửa.
* **Chặn xóa backup server point**: Khi bật tính năng Location Lock, các bản backup server point không thõa điều kiện xóa sẽ không được phép xóa bởi người dùng và hệ thống (policy).

#### Các bước bật tính năng:

* **Truy cập vào Backup Location:** Tìm và chọn Backup Location muốn bật tính năng Location Lock.
*   **Bật Location Lock:** Nhấp vào nút "Configure Location lock", một cửa số giao diện sẽ hiện lên cho phép bạn điền các thông tin cần thiết.&#x20;

    <figure><img src="../../../.gitbook/assets/image (752) (1).png" alt=""><figcaption></figcaption></figure>
* **Điền thông tin:** Điền các thông tin cấu hình cần thiết
  * **Thời gian giữ dữ liệu tối thiểu (Min retention day):** Thời gian ngắn nhất mà bản sao lưu phải được giữ lại.
  * **Thời gian giữ dữ liệu tối đa (Max retention day):** Thời gian dài nhất mà bản sao lưu được giữ lại.
  * **Thời gian thay đổi (Change duration):** Trong thời gian này, người dùng có thể thay đổi các cấu hình về Min và Max retention day, cũng như tắt tính năng Lock. Khi vượt qua thời gian này, cấu hình trên tính năng Lock sẽ không thể thay đổi.
* **Lưu:** Nhấp vào nút "Lưu" để hoàn tất.

#### Lợi ích:

* **Bảo mật dữ liệu:** Ngăn chặn việc xóa hoặc sửa đổi trái phép bản sao lưu.
* **Tuân thủ quy định:** Đảm bảo tuân thủ các quy định về lưu trữ dữ liệu (ví dụ: lưu giữ dữ liệu tài chính trong một khoảng thời gian nhất định).
