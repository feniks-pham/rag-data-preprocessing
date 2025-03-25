# Lịch sử hóa đơn

**Lịch sử hóa đơn / Billing history** tại vConsole cung cấp các báo cáo, thống kê chi phí sử dụng các sản phẩm VNG Cloud Service như (vServer, vMonitor, vStorage, vCDN,...). Tại đây, vConsole cung cấp 2 loại báo cáo, thống kê (Tổng quan và chi tiết) phù hợp với nhu cầu người dùng như:

* Biểu đồ tròn: Thống kê chi phí sử dụng dịch vụ VNG Cloud Service phân loại theo từng sản phẩm cụ thể theo khoảng thời gian nhất định.
* Biểu đồ cột: Thống kê chi phí thanh toán hóa đơn theo giá tiền và tình trạng thanh toán theo khoảng thời gian nhất định.

Truy cập đến trang **Lịch sử hóa đơn / Billing history** [**tại đây**](https://dashboard.console.vngcloud.vn/billing-report)**.**

Tại trang **Lịch sử hóa đơn / Billing history**, người dùng sẽ thấy 2 mục chính, bao gồm:

### **1. Lịch sử sử dụng / Usage history** <a href="#lichsuhoadon-billinghistory-1.lichsusudung-usagehistory" id="lichsuhoadon-billinghistory-1.lichsusudung-usagehistory"></a>

***

Tại đây, người dùng có thể chọn xem Tổng thanh toán của các dịch vụ VNG Cloud Service bao gồm (_vServer, vStorage, vMonitor, vCDN_) theo các mốc thời gian tại **time box (đơn vị tháng)** như

* **Quick**: Với các lựa chọn _This month, Last month, Last 2 months, Last 3 months, Last 6 months_
* **Relative**: Nhập số tháng bất kỳ kể từ thời điểm hiện tại. Ví dụ: hiện tại là tháng **12/2022**, tại trường "From", bạn nhập con số 5, có nghĩa mốc thời gian được áp dụng là từ tháng **07/2022** đến tháng **12/2022**. Đối với trường "To", nếu bạn nhập thêm con số 2, có nghĩa mốc thời gian được áp dụng là từ tháng **07/2022** đến tháng **10/2022.** Bấm nút **"View this range"** để áp dụng khoảng thời gian vừa chọn.
* **Absolute:** Nhập khoảng thời gian cụ thể ("From" → "To") mà bạn muốn xem, sau đó bấm nút **"View this range"** để áp dụng khoảng thời gian vừa chọn.

Tương ứng với các mốc thời gian được áp dụng, bạn sẽ thấy được 2 loại báo cáo / thống kê như sau:

* **Biểu đồ tròn**: Thống kê _chi phí sử dụng dịch vụ đã phát sinh hóa đơn_ trong khoảng thời gian chọn từ **time box,** bao gồm các thông số:
  * Tổng chi phí tất cả các dịch vụ: Thể hiện ở giữa biểu đồ
  * Các chi phí cụ thể theo từng sản phẩm: **vMonitor**, **vCDN**, **vStorage**, **vServer.** Người dùng có thể chọn / bỏ chọn một / nhiều sản phẩm để xem số liệu trên biểu đồ. Để ánh xạ dữ liệu từ Biểu đồ tròn sang Biểu đồ cột, người dùng cần bấm chọn một sản phẩm cụ thể trên Biểu đồ chọn
* **Biểu đồ cột**: Thống kê tình trạng thanh toán hóa đơn (Đã thanh toán và Chưa thanh toán) theo từng tháng, trong khoảng thời gian chọn từ **time box.** Người dùng có thể chọn xem thống kê hóa đơn Đã thanh toán / Chưa thanh toán / cả hai.

Để xem tình trạng thanh toán hóa đơn của 1 sản phẩm cụ thể, bạn chọn sản phẩm cần xem trên trên Biểu đồ tròn, khi ấy Biểu đồ cột sẽ thể hiện trạng thái thanh toán hóa đơn, trên tổng số hóa đơn của sản phầm đó.

* Ví dụ: **Biểu đồ tròn** đang thể hiện thể hiện chi phí hóa đơn của 2 sản phẩm là **vServer và vMonitor**, bạn bấm chọn **vServer** trên **Biểu đồ tròn** để xem thông tin thanh toán hóa đơn theo từng tháng của **vServer** ở **Biểu đồ cột**, và bấm chọn **vServer** lần nữa để xem dữ liệu của **Tất cả** sản phẩm. Thao tác tương tự đối với các sản phẩm khác.

### **2. Thống kê hóa đơn / Billing report** <a href="#lichsuhoadon-billinghistory-2.thongkehoadon-billingreport" id="lichsuhoadon-billinghistory-2.thongkehoadon-billingreport"></a>

***

Tại đây, người dùng có thể xem thống kê chi tiết hóa đơn, bao gồm các thông tin: _Mã hóa đơn, Dịch vụ, Ngày tạo đơn, Chi tiết hóa đơn, Tình trạng **(Thanh toán / Chưa thanh toán / Thanh toán 1 phần)**, Tổng tiền VND_

Cùng với các chức năng chính như:

* **Tìm kiếm:** Hỗ trợ tìm kiếm hóa đơn theo nhiều tiêu chí
  1. **Theo sản phẩm / dịch vụ**: Tìm kiếm hóa đơn theo từng sản phẩm / dịch vụ của VNG Cloud Service, hiện tại vConsole đang hỗ trợ lọc theo 04 sản phẩm / dịch vụ chính như _vServer, vStorage, vMonitor, vCDN._
  2. **Theo thời gian**: Hỗ trợ chọn tìm kiềm theo đơn vị ngày.
  3. **Theo từ khóa:** Hỗ trợ tìm kiếm theo từ khóa là _Mã hóa đơn / Chi tiết hóa đơn / Tình trạng hóa đơn_

_Cuối cùng, người dùng cần bấm biểu tượng **"Kính lúp"** để xem kết quả tìm kiếm theo các tiêu chí trên._

* **Xuất báo cáo:** Bấm vào biểu tượng **"Xuất báo cáo"** kế bên **"Kính lúp"** đểxuất toàn bộ thông tin hóa đơn theo kết quả tìm kiếm (Hỗ trợ định dạng pdf, .xlsx).

### **3. Hỏi đáp** <a href="#lichsuhoadon-billinghistory-3.hoidap" id="lichsuhoadon-billinghistory-3.hoidap"></a>

***

**Tại sao lại có tình trạng hóa đơn là thanh toán 1 phần / Partial\_Paid?**

* Hóa đơn có trạng thái là thanh toán 1 phần / Partial\_Paid xuất hiện khi người dùng không đủ số dư để thanh toán toàn bộ hóa đơn, lúc này hóa đơn sẽ được thanh toán 1 phần và thông báo đến người dùng qua mail phần thông tin hóa đơn, bao gồm:
  * Thông tin hóa đơn
  * Tổng hóa đơn
  * Số tiền đã thanh toán
  * Số tiền chưa thanh toán
