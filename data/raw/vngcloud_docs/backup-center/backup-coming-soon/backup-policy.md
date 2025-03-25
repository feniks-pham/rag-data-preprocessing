# Backup Policy

1. **Backup Policy là gì?**

Backup policy là một tập hợp các quy tắc và tiêu chuẩn được thiết lập để định nghĩa cách thức sao lưu dữ liệu của một hệ thống. Nó bao gồm các thông tin chi tiết về tần suất sao lưu, loại dữ liệu cần sao lưu, loại sao lưu được tạo và các quy tắc giữ dữ liệu. Nói một cách đơn giản, backup policy là "bản thiết kế" cho quá trình sao lưu dữ liệu của bạn.

2. **Tại sao Backup Policy lại quan trọng?**

* **Bảo vệ dữ liệu:** Giúp đảm bảo rằng dữ liệu của bạn luôn được bảo vệ an toàn và có thể khôi phục khi cần thiết.
* **Tối ưu hóa tài nguyên:** Giúp bạn sử dụng hiệu quả tài nguyên lưu trữ bằng cách chỉ sao lưu những dữ liệu cần thiết và giữ lại các bản sao lưu trong một khoảng thời gian hợp lý.
* **Tuân thủ quy định:** Đảm bảo rằng quá trình sao lưu của bạn tuân thủ các quy định về bảo mật và lưu trữ dữ liệu.

3. **Cấu trúc của một Backup Policy**

Một backup policy bao gồm các yếu tố sau:

* **Tần suất sao lưu:**
  * **Hourly:** Sao lưu hàng giờ.
  * **Daily:** Sao lưu hàng ngày.
  * **Weekly:** Sao lưu hàng tuần.
  * **Monthly:** Sao lưu hàng tháng.
* **Thời gian chạy job:** Giờ bắt đầu khởi chạy sao lưu tự động.
* **Rule giữ lại số bản full:** Quy định số lượng bản sao lưu đầy đủ (full backup) cần giữ lại.
* **Rule tạo số lượng bản incremental giữa 2 bản full:** Quy định số lượng bản sao lưu tăng phần (incremental backup) được tạo ra giữa hai bản sao lưu đầy đủ.
* **Phương thức sao lưu:** Xác định phương thức sao lưu (ví dụ: sao lưu toàn phần, sao lưu tăng phần).
* **Notification:** Thông báo khi quá trình sao lưu thành công hoặc thất bại.

4. **Cách hoạt động của Backup Policy**
   1. **Lập lịch:** Hệ thống sẽ tự động thực hiện sao lưu theo đúng lịch trình đã được định cấu hình trong policy.
   2. **Sao lưu dữ liệu:** Hệ thống sẽ sao chép dữ liệu theo đúng các quy tắc đã được định nghĩa.
   3. **Giữ lại dữ liệu:** Hệ thống sẽ tự động xóa các bản sao lưu cũ để đảm bảo tuân thủ quy tắc giữ dữ liệu.
5. **Ví dụ về một Backup Policy**

* **Ví dụ người dùng cài đặt bộ policy như hình dưới đây:**

<figure><img src="../../.gitbook/assets/image (789).png" alt=""><figcaption></figcaption></figure>

* **Giải thích cách hoạt động:**

<table><thead><tr><th width="78">Ngày</th><th width="86">Giờ khởi chạy</th><th width="129">Loại backup</th><th width="168">Retention áp dụng</th><th width="88">Xóa backup</th><th>Ghi chú</th></tr></thead><tbody><tr><td>1</td><td>1:00</td><td>Full</td><td>Hourly và Daily</td><td>Không</td><td></td></tr><tr><td>1</td><td>7:00</td><td>Incremental</td><td>Hourly</td><td>Không</td><td></td></tr><tr><td>1</td><td>13:00</td><td>Incremental</td><td>Hourly</td><td>Không</td><td></td></tr><tr><td>1</td><td>19:00</td><td>Incremental</td><td>Hourly</td><td>Không</td><td></td></tr><tr><td>2</td><td>1:00</td><td>Full</td><td>Hourly và Daily</td><td>Không</td><td>Theo retention daily thì chỉ giữ lại 1 bản full, nếu chỉ áp dụng retention daily thì bản full đầu tiên sẽ bị xóa. Nhưng áp dụng thêm rentention daily (giữ lại 2 bản, nên bản đầu tiên vẫn sẽ được giữ lại)</td></tr><tr><td>2</td><td>7:00</td><td>Incremental</td><td>Hourly</td><td>Không</td><td></td></tr><tr><td>2</td><td>13:00</td><td>Incremental</td><td>Hourly</td><td>Không</td><td></td></tr><tr><td>2</td><td>19:00</td><td>Incremental</td><td>Hourly</td><td>Không</td><td></td></tr><tr><td>3</td><td>1:00</td><td>Full</td><td>Hourly và Daily</td><td>Có</td><td>Theo retention daily (giữ lại 2 bản full), do đó, bản full đầu tiên và 3 bản incremental sau bản full đó sẽ bị xóa.</td></tr></tbody></table>

Trên đây là ví dụ về cách hoạt động của policy cho 3 ngày đầu tiên, các ngày tiếp theo sẽ tiếp tục hoạt động như cài đặt nếu không có gì thay đổi.
