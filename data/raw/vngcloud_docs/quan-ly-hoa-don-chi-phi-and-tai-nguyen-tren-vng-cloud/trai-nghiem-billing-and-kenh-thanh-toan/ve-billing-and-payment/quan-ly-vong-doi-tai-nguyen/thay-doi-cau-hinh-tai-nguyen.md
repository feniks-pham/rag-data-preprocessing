# Thay đổi cấu hình tài nguyên

Sử dụng tài liệu này như là một hướng dẫn thay đổi cấu hình tài nguyên. Tài liệu sẽ mô tả chi tiết các bước xử lý liên quan đến việc **quản lý tài nguyên và chi phí thay đổi** khi thay đổi cấu hình. Các bước khác sẽ giản lược bớt và chỉ đề cập đến như một phần của quy trình.&#x20;

#### Tính năng thay đổi cấu hình tài nguyên áp dụng đối với: <a href="#thaydoicauhinhtainguyen-tinhnangthaydoicauhinhtainguyenapdungdoivoi" id="thaydoicauhinhtainguyen-tinhnangthaydoicauhinhtainguyenapdungdoivoi"></a>

* **Đối tượng:** Người dùng trả trước và trả sau
* **Nguồn tiền:** Ví VNG Cloud hoặc các nguồn khác (thực hiện qua cổng thanh toán)
* **Tài nguyên:** Tất cả tài nguyên thuộc các sản phẩm VNG Cloud cho phép thay đổi cấu hình

#### **Người dùng trả trước thay đổi cấu hình tài nguyên** <a href="#thaydoicauhinhtainguyen-nguoidungtratruocthaydoicauhinhtainguyen" id="thaydoicauhinhtainguyen-nguoidungtratruocthaydoicauhinhtainguyen"></a>

***

#### **Quy trình thay đổi cấu hình tài nguyên** <a href="#thaydoicauhinhtainguyen-quytrinhthaydoicauhinhtainguyen" id="thaydoicauhinhtainguyen-quytrinhthaydoicauhinhtainguyen"></a>

* **Bước 1: Chọn tài nguyên và cấu hình mới**&#x20;
  * 1.1 Truy cập vào trang sản phẩm **vServer, vStorage, vMonitor**
  * 1.2 Chọn tài nguyên và cấu hình cần sử dụng tại trang sản phẩm
  * 1.3 Xác nhận thay đổi cấu tài nguyên để chuyển đến bước thanh toán: Tại đây, hệ thống sẽ điều hướng người dùng đến trang thanh toán tài nguyên
* **Bước 2: Thanh toán tài nguyên**
  * Xem hướng dẫn chi tiết [**tại đây**](../thanh-toan/)
* **Bước 3: Kiểm tra thông tin tài nguyên và thông tin thanh toán**
  * 3.1 Kiểm tra thông tin tài nguyên tại trang sản phẩm
  * 3.2 Kiểm tra **thông tin thanh toán, hóa đơn tại**
    * **User Portal:** [**https://dashboard.console.vngcloud.vn/**](https://dashboard.console.vngcloud.vn/)
* **Bước 4: Hệ thống thực hiện**
  * Email thông báo thông tin tài nguyên vừa thay đổi cấu hình
  * Phát sinh hóa đơn theo cấu hình mới

#### **Hướng dẫn tính giá tài nguyên khi thay đổi cấu hình** <a href="#thaydoicauhinhtainguyen-huongdantinhgiatainguyenkhithaydoicauhinh" id="thaydoicauhinhtainguyen-huongdantinhgiatainguyenkhithaydoicauhinh"></a>

Giá tiền hiển thị ngay tại bước thanh toán khi thực hiện thay đổi cấu hình tài nguyên vServer (áp dụng tương tự đối với các tài nguyên khác) được tính như sau:

| Hành động                   | Cấu hình                      | Thời điểm thực hiện | Thời điểm kết thúc tài nguyên | Tổng thời gian sử dụng theo cấu hình mới (1) | Đơn giá cấu hình mới tại thời điểm thực hiện (VND) (2) | Giá trị tài nguyên chưa sử dụng theo cấu hình cũ (VND) (3) = (2) / 30 \* (1) | Giá trị tài nguyên tính theo cấu hình mới (VND) (4) = (2) / 30 \* (1) | Giá trị tài nguyên cần thanh toán (VND) (5) = (4) - (3) |
| --------------------------- | ----------------------------- | ------------------- | ----------------------------- | -------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------- |
| **Khởi tạo**                | instance type (s-general-1x1) | 06-03-2023          | 06-06-2023                    | 90 ngày                                      | 181,000 / 30 ngày                                      | <p><br></p>                                                                  | 181,000 / 30 \* 90 = 543,000                                          | 543,000                                                 |
| **Thay đổi cấu hình lần 1** | instance type (s-general-2x4) | 16-04-2023          | 06-06-2023                    | 50 ngày                                      | 520,000 / 30 ngày                                      | 181,000 / 30 \* 50 = 301,667                                                 | 520,000 / 30 \* 50 = 866,667                                          | 866,667 - 301,667 = 565,000                             |
| **Thay đổi cấu hình lần 2** | instance type (s-general-1x1) | 16-05-2023          | 06-06-2023                    | 20 ngày                                      | 181,000 / 30 ngày                                      | 520,000 / 30 \* 20 = 346,667                                                 | 181,000 / 30 \* 20 = 120,667                                          | 120,667 - 346,667 = -226,000                            |

→ **Thay đổi cấu hình lần 1** **từ s-general-1x1 lên s-general-2x4,** người dùng phải thanh toán thêm 565,000 (VND)

→ **Thay đổi cấu hình lần 2** **từ s-general-2x4 xuống s-general-1x1,** người dùng sẽ được hoàn trả lại số tiền 226,000 (VND) vào ví credit

#### (\*) Lưu ý <a href="#thaydoicauhinhtainguyen-luuy" id="thaydoicauhinhtainguyen-luuy"></a>

* Giá trị tài nguyên chưa sử dụng được tính chính xác đến đơn vị phút
* Sẽ có dịch vụ không áp dụng hoàn phí tùy vào điều khoản sử dụng của từng sản phẩm (vServer, vStorage, vMonitor)

#### **Người dùng trả sau khởi tạo tài nguyên** <a href="#thaydoicauhinhtainguyen-nguoidungtrasaukhoitaotainguyen" id="thaydoicauhinhtainguyen-nguoidungtrasaukhoitaotainguyen"></a>

***

* **Bước 1: Cấu hình tài nguyên tại trang**&#x20;
  * 1.1 Truy cập vào trang sản phẩm **vServer, vStorage, vMonitor**
  * 1.2 Chọn tài nguyên và cấu hình cần sử dụng tại trang sản phẩm
  * 1.3 Xác nhận thay đổi cấu hình
  * 1.4 Kiểm tra thông tin tài nguyên
* **Bước 2: Hệ thống gửi thông tin xác nhận đến người dùng**
  * Email thông báo thông tin tài nguyên vừa thay đổi
  * Ghi nhận thời gian bắt đầu sử dụng tài nguyên theo cấu hình mới.
