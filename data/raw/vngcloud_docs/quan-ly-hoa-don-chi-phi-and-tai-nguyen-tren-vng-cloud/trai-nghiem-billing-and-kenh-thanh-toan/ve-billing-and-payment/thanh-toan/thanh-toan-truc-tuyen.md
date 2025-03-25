# Thanh toán trực tuyến

Thanh toán trực tuyến là 1 trong những phương thức thanh toán chính tại VNG Cloud Service. Hiện phương thức thanh toán trực tuyến áp dụng đối với:

* **Đối tượng**:
  * Người dùng trả trước
* **Nguồn tiền**:
  * Ví VNG Cloud (Ví Credit)
  * Cổng thanh toán trực tuyến: MoMo, ZaloPay,...
* **Tác vụ**:
  * Người dùng chọn phương thức và xác nhận thanh toán
  * Hệ thống tiến hành thanh toán
    * Thanh toán thành công: Tiến hành cung cấp tài nguyên theo cấu hình, phát sinh giao dịch tại [Payment History](https://dashboard.console.vngcloud.vn/payment-history) và [Credit History](https://dashboard.console.vngcloud.vn/credit-history) (trong trường hợp có dùng credit)
    * Thanh toán thất bại: Hủy tác vụ
  * Cung cấp tài nguyên theo cấu hình:
    * Thành công: Phát sinh lịch sử hóa đơn tại [Billing History](https://dashboard.console.vngcloud.vn/billing-report)
    * Thất bại: Hoàn tiền (Phát sinh giao dịch hoàn tiền tại[ Credit History](https://dashboard.console.vngcloud.vn/credit-history)), Hủy tác vụ
* **Kết quả khi hoàn thành tác vụ:**
  * Gửi mail thông báo thông tin cấu hình tài nguyên
  * Phát sinh các lịch sử giao dịch tại [Credit History](https://dashboard.console.vngcloud.vn/credit-history), [Payment History](https://dashboard.console.vngcloud.vn/payment-history), [Billing History](https://dashboard.console.vngcloud.vn/billing-report)

#### Hiện tại, tính năng thanh toán trực tuyến tại VNG Cloud đang hỗ trợ các phương thức thanh toán sau: <a href="#thanhtoantructuyen-hientai-tinhnangthanhtoantructuyentaivngclouddanghotrocacphuongthucthanhtoansau" id="thanhtoantructuyen-hientai-tinhnangthanhtoantructuyentaivngclouddanghotrocacphuongthucthanhtoansau"></a>

* **Thanh toán bằng ví VNG Cloud (Credit)**
  * Thanh toán toàn bộ đơn hàng bằng Credit (với điều kiện đủ số dư khả dụng)
  * Trong trường hợp không đủ số dư Credit, người dùng có thể chọn:
    * **Top up & Pay**: Sử dụng toàn bộ số dư credit hiện có và phần còn thiếu sẽ được nạp thêm thông qua cổng thanh toán trực tuyến
* **Thanh toán thông qua cổng thanh toán**
  * Thanh toán toàn bộ giá trị đơn hàng thông qua cổng thanh toán trực tuyến mà không ảnh hưởng đến ví Credit (hiện hỗ trợ các phương thức thanh toán như **MoMo, Zalo Pay,...**)

Ngoài ra, khi chọn phương thức thanh toán thông qua cổng thanh toán, VNG Cloud Service cung cấp thêm một hình thức thanh toán khác, gọi là **Thanh toán hộ**

### **Thanh toán hộ** <a href="#thanhtoantructuyen-thanhtoanho" id="thanhtoantructuyen-thanhtoanho"></a>

***

Thanh toán hộ sinh ra nhằm mục đích hỗ trợ khách hàng doanh nghiệp hoặc cá nhân là **người dùng trả trước** có nhu cầu sử dụng tài nguyên VNG Cloud Service nhưng phụ thuộc về mặt tài chính đối với cá nhân / doanh nghiệp khác.

Hình thức thanh toán hộ chỉ khả dụng khi người dùng chọn thanh toán thông qua cổng thanh toán trực tuyến.

Tại bước xác nhận trừ tiền, thay vì nhấn chọn **Pay** / **Thanh toán**, người dùng nhấn chọn **Share / Chia sẻ,** với mục đích ủy quyền thanh toán:

* Bước 1: Nhấn chọn **Share / Chia sẻ**
* Bước 2: Nhập email của người được ủy quyền thanh toán, nhấn **Xác nhận**
  * Sau khi nhấn xác nhận, hệ thống sẽ gửi mail bao gồm url dẫn tới trang thanh toán đơn hàng, url có thời hạn trong vòng 3 ngày kể từ thời điểm nhận email
* Bước 3: Người được ủy quyền truy cập vào url được gửi trong mail (với điều kiện url còn thời hạn)
* Bước 4: Người được ủy quyền xác nhận thanh toán đơn hàng
* Bước 5: Hệ thống sau khi xác nhận thành công sẽ tiến hành cung cấp tài nguyên.
* Bước 6: Sau khi cung cấp tài nguyên thành công, hệ thống phát sinh hóa đơn tương ứng cho người dùng (người gửi yêu cầu thanh toán hộ). Trong trường hợp có lỗi trong quá trình cung cấp tài nguyên, hệ thống sẽ hoàn tiền vào ví VNG Cloud của người dùng (người gửi yêu cầu thanh toán hộ).
