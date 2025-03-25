# Áp dụng coupon khi thanh toán

Coupon là mã giảm giá được VNG Cloud cung cấp.&#x20;

Coupon chỉ có thể sử dụng cho sản phẩm **vServer, vStorage, vCDN, vDB, vMonitor, vWAF** khi thực hiện thanh toán dịch vụ từ các sản phẩm trên.

Để sử dụng coupon, bạn chỉ cần thực hiện theo các bước sau:

* **Bước 1:** Cấu hình tài nguyên tại trang sản phẩm (vServer, vStorage, vServer).
* **Bước 2:** Xác nhận sử dụng tài nguyên để chuyển đến trang thanh toán
* **Bước 3:** Nhập mã coupon tại trang thanh toán để áp dụng giảm giá
  * Người dùng sẽ nhận được thông báo mã coupon không hợp lệ trong các trường hợp: Coupon hết hiệu lực, coupon không áp dụng cho dịch vụ đang thực hiện thanh toán,...
* **Bước 4:** Nhấn xác nhận thanh toán để hoàn tất việc mua hàng

## Cách tính giá trị coupon cho 1 lần thanh toán <a href="#id-apdungcouponkhithanhtoan-cachtinhgiatricouponcho1lanthanhtoan" id="id-apdungcouponkhithanhtoan-cachtinhgiatricouponcho1lanthanhtoan"></a>

* Trong trường hợp người dùng sử dụng Coupon khi thanh toán cho **đơn hàng gồm nhiều tài nguyên**, khi đó giá trị Coupon sẽ được chia cho các tài nguyên theo giá trị tài nguyên trên tổng số đơn hàng.
* Dưới đây là ví dụ áp dụng **Coupon 150,000 VND** cho 1 lần thanh toán gồm nhiều tài nguyên:

| Tài nguyên         | Giá tài nguyên (Tính theo cấu hình và thời gian sử dụng, đã bao gồm VAT) | Coupon áp dụng | Tiền cần thanh toán | Giá trị ghi nhận trên hóa đơn |
| ------------------ | ------------------------------------------------------------------------ | -------------- | ------------------- | ----------------------------- |
| Server (vServer)   | 1,000,000 VND                                                            | 100,000 VND    | 900,000 VND         | 900,000 VND                   |
| Project (vStorage) | 500,000 VND                                                              | 50,000 VND     | 450,000 VND         | 450,000 VND                   |

→ **Tổng số đơn hàng ban đầu** = 1,500,000 VND

→ **Tỉ lệ % giá trị coupon được áp dụng**:

* Server = 1,000,000/1,500,000 = 2/3 giá trị coupon
* Project storage = 500,000/1,500,000 = 1/3 giá trị coupon

Từ ví dụ trên, người dùng phải thanh toán số tiền 900,000 + 450,000 = 1,350,000 VND trong 1 lần cho 2 tài nguyên được mua cùng 1 lúc. Đồng thời, hệ thống sẽ phát sinh 2 hóa đơn ghi nhận thông tin giá tiền của từng tài nguyên tương ứng (đã áp dụng coupon).

\
