# Thống kê sử dụng

**Thống kê sử dụng / Usage report** tại vConsole cung cấp các báo cáo, thống kê chi phí sử dụng các sản phẩm VNG Cloud Service như (vServer, vMonitor, vStorage, vCDN,...) cụ thể theo từng Resource. Tại đây, người dùng có thể theo dõi thời gian sử dụng Resource cũng như các lần thay đổi cấu hình (nếu có).

Truy cập đến trang **Thống kê sử dụng / Usage report** [**tại đây**](https://dashboard.console.vngcloud.vn/usage-report)**.**

Tại trang **Thống kê sử dụng / Usage report**, người dùng sẽ thấy  bảng biểu dữ liệu chính, bao gồm các thành phần:

### **1. Thanh công cụ tìm kiếm** <a href="#thongkesudung-usagereport-1.thanhcongcutimkiem" id="thongkesudung-usagereport-1.thanhcongcutimkiem"></a>

***

**Hỗ trợ tìm kiếm thông tin sử dụng Resource với nhiều tiêu chí như:**

* **Loại Sản phẩm:** Tìm kiếm thông tin sử dụng của Resource theo từng Sản phẩm cụ thể:
  * **Tất cả:** Mặc định khi truy cập vào trang, tìm kiếm thông tin sử dụng Resource của tất cả Sản phẩm
  * **vServer:** Tìm kiếm thông tin sử dụng Resource của vServer
  * **vStorage:** Tìm kiếm thông tin sử dụng Resource của vStorage
  * **vMonitor:** Tìm kiếm thông tin sử dụng Resource của vMonitor
  * **vCDN:** Tìm kiếm thông tin sử dụng Resource của vCDN
* **Thời gian sử dụng:** Mặc định tìm kiếm theo tháng trước đó, chỉ hỗ trợ tìm kiếm dữ liệu trong tháng
* **Từ khóa:** Hỗ trợ tìm kiếm theo từ khóa là _Mã hóa đơn, Tên tài nguyên, Tài nguyên ID, Sản phẩm, Dịch vụ, Mặt hàng, Mã Coupon._

_Cuối cùng, người dùng cần bấm biểu tượng **"Kính lúp"** để xem kết quả tìm kiếm theo các tiêu chí trên._

**Hỗ trợ xuất báo cáo dữ liệu theo tiêu chí tìm kiếm:**

_Để trích xuất dữ liệu lịch sử thanh toán, người dùng cần:_

* Bấm vào biểu tượng **"Xuất báo cáo"** kế bên **"Kính lúp"** để xuất toàn bộ lịch sử thanh toán theo kết quả tìm kiếm.
* Định dạng hỗ trợ: Dạng excel (.xlsx)
* Thư mục lưu trữ: File dữ liệu mặc định lưu trữ tại thư mục "Tải về" hoặc theo cài đặt trình duyệt web.

### **2. Kết quả tìm kiếm** <a href="#thongkesudung-usagereport-2.ketquatimkiem" id="thongkesudung-usagereport-2.ketquatimkiem"></a>

***

Kết quả tìm kiếm được thể hiện dựa trên các tiêu chí tìm kiếm áp dụng ở "Thanh công cụ tìm kiếm", bao gồm các thông tin chính như:

* **Mã hóa đơn:** Mã định danh hóa đơn
* **Ngày tạo:**&#x4E;gày phát sinh hóa đơn
* **Trạng thái:** Trạng thái hóa đơn (Paid / Partial\_Paid / Unpaid)
* **Tên tài nguyên:** Tên tài nguyên sử dụng
* **Tài nguyên ID:** Mã định danh tài nguyên
* **Tên sản phẩm:** Cho biết tài nguyên sử dụng thuộc loại sản phẩm nào (vServer, vStorage, vMonitor, vCDN)
* **Tên dịch vụ:** Cho biết tài nguyên sử dụng thuộc loại dịch vụ nào
* **Mặt hàng:** Cho biết tài nguyên sử dụng là mặt hàng nào
* **Đơn vị:** Cho biết đơn vị dùng để tính giá của mặt hàng. **VD: Đơn vị là GB đối với dịch vụ VPC-Bandwidth sản phẩm vServer)**
* **Thời gian đối soát trong tháng:** Cho biết khoảng thời gian sử dụng tài nguyên với cùng cấu hình (thời gian bắt đầu và kết thúc)
* **Đơn giá (VND):** Cho biết giá tiền phải trả trên 1 đơn vị tính
* **Số lượng:** Cho biết số lượng mặt hàng sử dụng trong 1 tài nguyên
* **Giảm giá (%):** Cho biết phần trăm giá được giảm trên 1 mặt hàng tại thời điểm mua tài nguyên
* **Thuế suất (%):** Thuế áp dụng tại thời điểm mua tài nguyên
* **Giá trị Coupon (VND):** Giá trị Coupon được áp dụng tại thời điểm mua tài nguyên
* **Mã Coupon:** Mã Coupon được áp dụng tại thời điểm mua tài nguyên
* **Tổng số tiền (VND):** Tổng chi phí sử dụng tài nguyên trong tháng

### **3. Hỏi đáp** <a href="#thongkesudung-usagereport-3.hoidap" id="thongkesudung-usagereport-3.hoidap"></a>

***

**Tổng chi phí sử dụng tài nguyên trong tháng được tính theo công thức nào?**

* **Tổng chi phí chưa thuế** = \[**Thời gian đối soát trong tháng** (tính theo phút) \* **Đơn giá** \* **Số lượng** \* (**1 - Giảm giá/100**) / (**30\*24\*60**)]
* **Số tiền thuế** = **Tổng chi phí chưa thuế** \* **Thuế suất** / 100
* **Tổng chi phí sử dụng trong tháng** = **Tổng chi phí chưa thuế + Số tiền thuế** - **Giá trị Coupon**
* Lưu ý: Công thức trên ví dụ trong trường hợp **Đơn vị** tính trên 30 ngày, (30\*24\*60) quy đổi ra phút.

**Thời gian sử dụng tài nguyên dài hơn 1 tháng thì xem như thế nào?**

* Trang Usage Report chỉ hỗ trợ xem thông tin sử dụng tài nguyên trong 1 tháng.
* Trường hợp thời gian sử dụng tài nguyên kéo dài từ tháng này sang tháng khác, khách hàng chủ động thay đổi tháng cần xem trên thanh công cụ tìm kiếm.
* Giá trị Coupon hiển thị cũng sẽ chia đều cho số tháng sử dụng, ví dụ:
  * Tại thời điểm mua tài nguyên, Giá trị Coupon được áp dụng là 100,000 VND. Tài nguyên sử dụng kéo dài từ tháng 01/2023 đến tháng 02/2023, thì:
    * Giá trị Coupon khi hiển thị trong tháng 01/2023 là 50,000 VND
    * Giá trị Coupon khi hiển thị trong tháng 02/2023 là 50,000 VND

**Trong 1 tháng có sự thay đổi cấu hình tài nguyên thì xem như thế nào?**

* Trường hợp có sự thay đổi cấu hình tài nguyên, sẽ phát sinh thêm 1 đầu hóa đơn để mapping với cấu hình mới của tài nguyên
* Có nghĩa sẽ có nhiều đầu hóa đơn gắn với cùng 1 tài nguyên trong trường hợp thay đổi cấu hình nhiều lần

**Bảng dữ liệu có quá nhiều thông tin, làm sao để xem 1 vài thông tin cần thiết thôi?**

* Khách hàng có thể chủ động ẩn / hiện các cột dữ liệu không cần thiết / cần thiết theo nhu cầu của mình bằng cách click vào **icon Setting** trên góc phải của bảng dữ liệu
