# Thanh toán hóa đơn tự động

Thanh toán tự động là tính năng nhằm mục đích hỗ trợ người dùng VNG Cloud thanh toán các hóa đơn chưa hoàn thành thanh toán

* **Đối tượng áp dụng**
  * Người dùng trả trước và trả sau có hóa đơn cần thanh toán
  * Hóa đơn cần thanh toán là hóa đơn có trạng thái Chưa thanh toán / Thanh toán 1 phần
* **Thời gian chạy**
  * Mỗi ngày
* **Nguồn tiền**
  * Ví VNG Cloud (ví Credit)
* **Tác vụ**
  * Lọc ra người dùng có hóa đơn cần thanh toán
  * Kiểm tra còn số dư khả dụng trong ví hay không, nếu:
    * Số dư khả dụng > 0: Thực hiện thanh toán hóa đơn theo độ ưu tiên (Ưu tiên thanh toán hóa đơn cũ và có số tiền nhỏ trước)
    * Số dư khả dụng <= 0: Hủy tác vụ
* **Kết quả khi hoàn thành tác vụ**
  * Gửi mail thông báo đến người dùng thông tin hóa đơn vừa được thanh toán
  * Phát sinh lịch sử giao dịch trên user portal tại:
    * Billing history: [https://dashboard.console.vngcloud.vn/billing-report](https://dashboard.console.vngcloud.vn/billing-report)
    * Credit history: [https://dashboard.console.vngcloud.vn/credit-history](https://dashboard.console.vngcloud.vn/credit-history)
    * Payment history: [https://dashboard.console.vngcloud.vn/payment-history](https://dashboard.console.vngcloud.vn/payment-history)
