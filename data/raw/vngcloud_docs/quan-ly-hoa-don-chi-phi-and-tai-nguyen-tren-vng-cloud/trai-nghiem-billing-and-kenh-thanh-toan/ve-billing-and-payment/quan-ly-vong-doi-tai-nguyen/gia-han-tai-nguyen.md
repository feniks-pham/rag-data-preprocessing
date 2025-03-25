# Gia hạn tài nguyên

Sử dụng tài liệu này như là một hướng dẫn gia hạn tài nguyên. Tài liệu sẽ mô tả chi tiết các bước xử lý liên quan đến việc **quản lý tài nguyên và chi phí phát sinh** khi gia hạn tài nguyên. Các bước khác sẽ giản lược bớt và chỉ đề cập đến như một phần của quy trình.&#x20;

#### Tính năng gia hạn tài nguyên áp dụng đối với: <a href="#giahantainguyen-tinhnanggiahantainguyenapdungdoivoi" id="giahantainguyen-tinhnanggiahantainguyenapdungdoivoi"></a>

* **Đối tượng:** Người dùng trả trước
* **Nguồn tiền:** Ví VNG Cloud hoặc các nguồn khác (thực hiện qua cổng thanh toán)
* **Tài nguyên:** Tất cả tài nguyên thuộc các sản phẩm VNG Cloud cho phép gia hạn

#### **Quy trình gia hạn tài nguyên** <a href="#giahantainguyen-quytrinhgiahantainguyen" id="giahantainguyen-quytrinhgiahantainguyen"></a>

Khi thực hiện gia hạn tài nguyên, mặc định thời gian bắt đầu sẽ được tính từ thời điểm kết thúc tài nguyên hiện tại, người dùng có thể chọn thời điểm kết thúc mới tùy ý, miễn sao lớn hơn thời điểm kết thúc hiện tại, hệ thống sẽ dựa vào đó để tính giá cần thanh toán.

* **Bước 1: Chọn tài nguyên cần gia hạn**&#x20;
  * 1.1 Truy cập vào trang sản phẩm **vServer, vStorage, vMonitor**
  * 1.2 Chọn tài nguyên cần gia hạn tại trang sản phẩm
  * 1.3 Xác nhận gia hạn tài nguyên để chuyển đến bước thanh toán: Tại đây, hệ thống sẽ điều hướng người dùng đến trang thanh toán tài nguyên
* **Bước 2: Thanh toán tài nguyên**
  * Xem hướng dẫn chi tiết [**tại đây**](../thanh-toan/)
* **Bước 3: Kiểm tra thông tin tài nguyên và thông tin thanh toán**
  * 3.1 Kiểm tra thông tin tài nguyên tại trang sản phẩm
  * 3.2 Kiểm tra **thông tin thanh toán, hóa đơn tại**
    * **User Portal:** [**https://dashboard.console.vngcloud.vn/**](https://dashboard.console.vngcloud.vn/)
* **Bước 4: Hệ thống thực hiện**
  * Email thông báo thông tin tài nguyên vừa được gia hạn
  * Phát sinh hóa đơn mới tương ứng với thời gian sử dụng tài nguyên

#### **Hướng dẫn tính giá tài nguyên khi thay đổi cấu hình** <a href="#giahantainguyen-huongdantinhgiatainguyenkhithaydoicauhinh" id="giahantainguyen-huongdantinhgiatainguyenkhithaydoicauhinh"></a>

Giá tiền hiển thị ngay tại bước thanh toán khi thực hiện gia hạn tài nguyên vServer (áp dụng tương tự đối với các tài nguyên khác) được tính như sau:

| Hành động    | Tài nguyên Server             | Thời điểm thực hiện | Thời điểm kết thúc tài nguyên | Tổng thời gian sử dụng (1) | Đơn giá tại thời điểm thực hiện (VND) (2) | Gía trị tài nguyên cần thanh toán (VND) (3) = (1) \* (2) |
| ------------ | ----------------------------- | ------------------- | ----------------------------- | -------------------------- | ----------------------------------------- | -------------------------------------------------------- |
| **Khởi tạo** | instance type (s-general-1x1) | 06-03-2023          | 06-04-2023                    | 1 tháng                    | 181,000 / tháng                           | 181,000                                                  |
| **Gia hạn**  | instance type (s-general-1x1) | 15-03-2023          | 06-06-2023                    | 2 tháng                    | 181,000 / tháng                           | 362,000                                                  |

Từ ví dụ trên, khi thực hiện gia hạn tài nguyên thêm 2 tháng, thời điểm kết thúc tài nguyên sẽ được cập nhật sang ngày 06-06-2023 và người dùng phải chi trả thêm số tiền là 362,000 VND để hoàn tất việc gia hạn&#x20;

\
