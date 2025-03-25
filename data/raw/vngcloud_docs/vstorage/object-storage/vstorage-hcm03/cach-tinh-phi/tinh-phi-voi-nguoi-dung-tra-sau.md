# Tính phí với người dùng trả sau

Khi bạn khởi tạo một project, nếu bạn là người dùng trả sau thì mặc định bạn có thể mua project để sử dụng mà không cần thanh toán giá trị gói lưu trữ ngay tại thời điểm mua. Mỗi cuối tháng chúng tôi sẽ cung cấp tới bạn một hóa đơn chứa thông tin sử dụng tài nguyên và chi phí phát sinh trên tài nguyên mà bạn sử dụng thực tế. Thông tin sử dụng tài nguyên bao gồm:&#x20;

* **Mã hóa đơn:** Mã định danh hóa đơn.
* **Ngày tạo:**&#x4E;gày phát sinh hóa đơn.
* **Trạng thái:** Trạng thái hóa đơn (Paid / Partial\_Paid / Unpaid).
* **Tên tài nguyên:** Tên tài nguyên sử dụng.
* **Tài nguyên ID:** Mã định danh tài nguyên.
* **Tên sản phẩm:** Cho biết tài nguyên sử dụng thuộc loại sản phẩm nào (vServer, vStorage, vMonitor, vCDN).
* **Tên dịch vụ:** Cho biết tài nguyên sử dụng thuộc loại dịch vụ nào.
* **Mặt hàng:** Cho biết tài nguyên sử dụng là mặt hàng nào.
* **Đơn vị:** Cho biết đơn vị dùng để tính giá của mặt hàng. VD: Đơn vị là GB đối với dịch vụ VPC-Bandwidth sản phẩm vServer).
* **Thời gian đối soát trong tháng:** Cho biết khoảng thời gian sử dụng tài nguyên với cùng cấu hình (thời gian bắt đầu và kết thúc).
* **Đơn giá (VND):** Cho biết giá tiền phải trả trên 1 đơn vị tính.
* **Số lượng:** Cho biết số lượng mặt hàng sử dụng trong 1 tài nguyên.
* **Giảm giá (%):** Cho biết phần trăm giá được giảm trên 1 mặt hàng tại thời điểm mua tài nguyên.
* **Thuế suất (%):** Thuế áp dụng tại thời điểm mua tài nguyên.
* **Giá trị Coupon (VND):** Giá trị Coupon được áp dụng tại thời điểm mua tài nguyên.
* **Mã Coupon:** Mã Coupon được áp dụng tại thời điểm mua tài nguyên.
* **Tổng số tiền (VND):** Tổng chi phí sử dụng tài nguyên trong tháng.

Bạn có thể xem báo cáo sử dụng tài nguyên tại: [https://dashboard.console.vngcloud.vn/usage-report](https://dashboard.console.vngcloud.vn/usage-report)

**Tổng số tiền bạn cần thanh toán mỗi cuối tháng được tính dựa theo công thức:**&#x20;

* Tổng chi phí chưa thuế: \[Thời gian đối soát trong tháng (tính theo phút) \* Đơn giá \* Số lượng \* (1 - Giảm giá/100) / (30\*24\*60)].
* Số tiền thuế: Tổng chi phí chưa thuế \* Thuế suất / 100.
* Tổng chi phí sử dụng trong tháng: Tổng chi phí chưa thuế + Số tiền thuế - Giá trị Coupon.

Công thức trên ví dụ trong trường hợp Đơn vị tính trên 30 ngày, (30\*24\*60) quy đổi ra phút.

Tương tự khi bạn thực hiện gia hạn project, tăng/ giảm kích thước gói lưu trữ chúng tôi cũng sẽ tính giá tiền bạn cần thanh toán thêm hoặc giá tiền mà bạn có thể được hoàn trả lại. Chi tiết tham khảo tại [Quản lý hóa đơn, chi phí & tài nguyên trên VNG Cloud](../../../../quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/).
