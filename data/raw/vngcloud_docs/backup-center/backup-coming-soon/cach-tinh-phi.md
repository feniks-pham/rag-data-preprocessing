# Cách tính phí

Backup location là một dịch vụ lưu trữ dữ liệu sao lưu vô cùng tiện lợi, giúp bạn bảo vệ dữ liệu quan trọng khỏi bị mất mát. Để hiểu rõ hơn về chi phí khi sử dụng dịch vụ này, chúng ta sẽ cùng tìm hiểu về hai yếu tố chính ảnh hưởng đến giá thành: **Usage (lượng dữ liệu sử dụng)** và **Traffic (lượng dữ liệu truyền tải)**.

## Billing element

### Usage (Lượng dữ liệu sử dụng)

* **Đơn vị tính:** GB/giờ
* **Nguyên tắc tính phí:** Bạn sẽ chỉ phải trả phí cho lượng dữ liệu thực tế mà bạn sử dụng trong mỗi giờ. Ví dụ:
  * Nếu bạn sử dụng 100GB dữ liệu trong 1 giờ, bạn sẽ bị tính phí cho 100GB.
  * Nếu bạn chỉ sử dụng 50GB trong giờ tiếp theo, bạn sẽ chỉ bị tính phí cho 50GB.
* **Ưu điểm:**
  * Linh hoạt: Bạn chỉ trả cho những gì mình sử dụng, không phải trả phí cố định cho một dung lượng nhất định.
  * Tiết kiệm: Nếu nhu cầu sử dụng của bạn thay đổi theo thời gian, bạn có thể điều chỉnh lượng dữ liệu sao lưu cho phù hợp và giảm chi phí.

### Traffic (Lượng dữ liệu truyền tải)

* **Đơn vị tính:** GB
* **Nguyên tắc tính phí:** Hiện tại, VNG Cloud Backup đang miễn phí hoàn toàn lượng dữ liệu truyền tải. Điều này có nghĩa là bạn có thể tải lên và tải xuống dữ liệu sao lưu mà không phải trả thêm bất kỳ khoản phí nào.

## Billing Method

Hiện tại, VNG Cloud Backup hỗ trợ cả 2 hình thức là trả trước và trả sau:

### Đối với trả sau

* Đối tượng áp dụng: Người dùng trả sau tại VNG Cloud
* Hình thức thanh toán: Trả sau
* Cuối mỗi tháng, VNG Cloud Backup sẽ xuất hóa đơn dịch vụ, và người dùng sẽ tiến hành thanh toán hóa đơn tương tự các dịch vụ trả sau khác. Lưu ý rằng, một backup location sẽ tương ứng với 1 hóa đơn.

### Đối với trả trước

* Đối tượng áp dụng: Người dùng trả trước tại VNG Cloud
* Hình thức thanh toán: [Tạm giữ credit (hold credit)](../../quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/trai-nghiem-billing-and-kenh-thanh-toan/ve-billing-and-payment/thanh-toan/tam-giu-credit.md)
  * Theo đó, người dùng cần chuẩn bị sẵn lượng credit đủ dùng trong tài khoản VNG Cloud, cứ mỗi ngày, hệ thống sẽ tiến hành tạm giữ credit dựa trên số usage thực tế của toàn bộ backup location.
  * Trường hợp lượng credit trong tài khoản không đủ để tiến hành tạm giữ, VNG Cloud sẽ nhắc nhở và có các biện pháp xử lý nếu người dùng không chủ động nạp thêm credit.
* Cuối mỗi tháng, VNG Cloud sẽ xuất hóa đơn dịch vụ, và người dùng sẽ tiến hành thanh toán hóa đơn tương tự các dịch vụ trả sau khác. Lưu ý rằng, một backup location sẽ tương ứng với 1 hóa đơn.
  * Lượng credit được tạm giữ sẽ được dùng để thanh toán hóa đơn dịch vụ, nếu không đủ sẽ trừ thêm trong tài khoản VNG Cloud, nếu tạm giữ dư so với số thực tế, chúng tôi sẽ hoàn lại vào tài khoản VNG Cloud.
