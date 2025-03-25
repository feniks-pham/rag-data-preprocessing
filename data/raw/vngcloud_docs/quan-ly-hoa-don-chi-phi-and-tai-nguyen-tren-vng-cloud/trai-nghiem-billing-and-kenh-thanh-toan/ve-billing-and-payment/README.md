# Về Billing & Payment

Sử dụng hướng dẫn này để bắt đầu với hệ thống **Billing & Payment.** Bạn sẽ có cái nhìn tổng quan về các tính năng chính mà hệ thống đang xử lý, từ đó hiểu rõ hơn cách hành xử của hệ thống lên từng tài nguyên / dịch vụ.

Tại đây, chúng tôi chia hệ thống làm 3 nhóm chức năng chính:

* **Thanh toán:** Xử lý các tác vụ liên quan việc Thanh toán tài nguyên, Thanh toán hóa đơn, Liên kết cổng thanh toán ngoài ví VNG Cloud,...
* **Quản lý hóa đơn:** Ghi nhận hành động người dùng trên tài nguyên, từ đó ghi nhận hóa đơn mới cho tài nguyên tương ứng trên từng hành động cụ thể (tạo mới, thay đổi cấu hình, gia hạn,...),...
* **Quản lý vòng đời tài nguyên:** Kiểm soát tốt vòng đời tài nguyên và thông báo đến người dùng các tài nguyên sắp hết hạn, tự động gia hạn,... giúp người dùng kịp thời đưa ra quyết định để trải nghiệm sử dụng tài nguyên không bị gián đoạn.

#### **Để tìm hiểu chi tiết từng nhóm tính năng, mời tham khảo tại đây:** <a href="#trainghiembilling-and-payment-detimhieuchitiettungnhomtinhnang-moithamkhaotaiday" id="trainghiembilling-and-payment-detimhieuchitiettungnhomtinhnang-moithamkhaotaiday"></a>

***

* [Thanh toán](thanh-toan/)
* [Quản lý hóa đơn](../quan-ly-hoa-don.md)
* [Quản lý vòng đời tài nguyên](quan-ly-vong-doi-tai-nguyen/)

#### **Tổng quan quy trình khởi tạo và thanh toán tài nguyên đối với người dùng VNG Cloud Service** <a href="#trainghiembilling-and-payment-tongquanquytrinhkhoitaovathanhtoantainguyendoivoinguoidungvngcloudserv" id="trainghiembilling-and-payment-tongquanquytrinhkhoitaovathanhtoantainguyendoivoinguoidungvngcloudserv"></a>

***

* **Bước 1: Cấu hình tài nguyên**
  * 1.1 Truy cập vào trang sản phẩm **vServer, vStorage, vMonitor**
  * 1.2 Chọn tài nguyên và cấu hình cần sử dụng tại trang sản phẩm
  * 1.3 Xác nhận sử dụng tài nguyên để chuyển đến bước thanh toán: Tại đây, hệ thống sẽ điều hướng người dùng đến trang thanh toán tài nguyên
* **Bước 2: Thanh toán tài nguyên**
  * 2.1 Chọn số lượng tài nguyên và thời gian sử dụng
  * 2.2 Nhập Coupon áp dụng (nếu có)
  * 2.3 Xác nhận thanh toán: Tại đây, chúng tôi hỗ trợ người dùng thanh toán với các hình thức như sau:
    * Sử dụng số dư Credit
    * Top up & Pay
    * Qua tài khoản liên kết
  * 2.4 Thanh toán thành công: Hệ thống sẽ điều hướng người dùng về trang sản phẩm trước đó (tại bước 1)
* **Bước 3: Kiểm tra thông tin tài nguyên và thông tin thanh toán**
  * 3.1 Kiểm tra thông tin tài nguyên tại trang sản phẩm
  * 3.2 Phát sinh hóa đơn: Kiểm tra thông tin thanh toán, hóa đơn tại
    * **User Portal:** [**https://dashboard.console.vngcloud.vn/**](https://dashboard.console.vngcloud.vn/)

**Lưu ý: Trên đây là hướng dẫn tham khảo cho người dùng trả trước, đối với người dùng trả sau sẽ có 1 số khác biệt. Tham khảo chi tiết tại mục:**

* [Người dùng trả trước và trả sau](nguoi-dung-tra-truoc-and-tra-sau.md)
