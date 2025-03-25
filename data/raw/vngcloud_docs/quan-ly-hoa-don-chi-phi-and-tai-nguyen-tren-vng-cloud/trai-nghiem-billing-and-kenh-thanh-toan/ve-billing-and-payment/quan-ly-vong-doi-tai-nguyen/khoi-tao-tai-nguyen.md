# Khởi tạo tài nguyên

Sử dụng tài liệu này như là một hướng dẫn khởi tạo tài nguyên. Tài liệu sẽ mô tả chi tiết các bước xử lý liên quan đến việc **quản lý tài nguyên khi khởi tạo**. Các bước khác sẽ giản lược bớt và chỉ đề cập đến như một phần của quy trình.&#x20;

#### Tính năng khởi tạo tài nguyên áp dụng đối với: <a href="#khoitaotainguyen-tinhnangkhoitaotainguyenapdungdoivoi" id="khoitaotainguyen-tinhnangkhoitaotainguyenapdungdoivoi"></a>

* **Đối tượng:** Người dùng trả trước và trả sau
* **Nguồn tiền:** Ví VNG Cloud hoặc các nguồn khác (thực hiện qua cổng thanh toán)
* **Tài nguyên:** Tất cả tài nguyên thuộc các sản phẩm VNG Cloud

#### **Người dùng trả trước khởi tạo tài nguyên** <a href="#khoitaotainguyen-nguoidungtratruockhoitaotainguyen" id="khoitaotainguyen-nguoidungtratruockhoitaotainguyen"></a>

***

#### **Quy trình khởi tạo tài nguyên** <a href="#khoitaotainguyen-quytrinhkhoitaotainguyen" id="khoitaotainguyen-quytrinhkhoitaotainguyen"></a>

* **Bước 1: Cấu hình tài nguyên**&#x20;
  * 1.1 Truy cập vào trang sản phẩm **vServer, vStorage, vMonitor**
  * 1.2 Chọn tài nguyên và cấu hình cần sử dụng tại trang sản phẩm
  * 1.3 Xác nhận sử dụng tài nguyên để chuyển đến bước thanh toán: Tại đây, hệ thống sẽ điều hướng người dùng đến trang thanh toán tài nguyên
* **Bước 2: Thanh toán tài nguyên**
  * Xem hướng dẫn chi tiết [**tại đây**](../thanh-toan/)
* **Bước 3: Kiểm tra thông tin tài nguyên và thông tin thanh toán**
  * 3.1 Kiểm tra thông tin tài nguyên tại trang sản phẩm
  * 3.2 Kiểm tra **thông tin thanh toán, hóa đơn tại**
    * **User Portal:** [**https://dashboard.console.vngcloud.vn/**](https://dashboard.console.vngcloud.vn/)
* **Bước 4: Hệ thống thực hiện**
  * Email thông báo thông tin tài nguyên vừa khởi tạo
  * Phát sinh hóa đơn tương ứng: Tham khảo thêm cách tính thành tiền cũng như thông tin hóa đơn [**tại đây**](../../quan-ly-hoa-don.md)

#### **Hướng dẫn tính giá tài nguyên** <a href="#khoitaotainguyen-huongdantinhgiatainguyen" id="khoitaotainguyen-huongdantinhgiatainguyen"></a>

Giá tiền hiển thị ngay tại bước thanh toán tài nguyên cũng là giá hiển thị trên hóa đơn tương ứng với tài nguyên đó.&#x20;

Dưới đây là hướng dẫn tính giá khi khởi tạo Server, người dùng có thể áp dụng công thức để tính tương tự cho các tài nguyên khác trong hệ thống VNG Cloud Service.

_Ví dụ công thức tính giá trị hóa đơn khi khởi tạo Server bao gồm thông tin_:

| Cấu hình Server (1)                                                                                                     | Đơn giá (bao gồm VAT) (2) | Thời gian sử dụng (3) | Giá trị Coupon (4) | Thành tiền = (2) \* (3)  |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------- | ------------------ | ------------------------ |
| Image (dev.v1.small1x1)                                                                                                 | 90,000 VND / 30 ngày      | 60 ngày               | 20,000 VND         | 180,000                  |
| Root disk (Size 20GB, IOPS 3000)                                                                                        | 35,000 VND / 30 ngày      | 60 ngày               | 70,000             |                          |
| Giá sử dụng tài nguyên cần thanh toán = Total thành tiền - Giá trị Coupon **=** 180,000 + 70,000 - 20,000 = 230,000 VND |                           |                       |                    |                          |

#### **Người dùng trả sau khởi tạo tài nguyên** <a href="#khoitaotainguyen-nguoidungtrasaukhoitaotainguyen" id="khoitaotainguyen-nguoidungtrasaukhoitaotainguyen"></a>

***

#### **Quy trình khởi tạo tài nguyên** <a href="#khoitaotainguyen-quytrinhkhoitaotainguyen.1" id="khoitaotainguyen-quytrinhkhoitaotainguyen.1"></a>

* **Bước 1: Cấu hình tài nguyên tại trang**&#x20;
  * 1.1 Truy cập vào trang sản phẩm **vServer, vStorage, vMonitor**
  * 1.2 Chọn tài nguyên và cấu hình cần sử dụng tại trang sản phẩm
  * 1.3 Xác nhận sử dụng tài nguyên
  * 1.4 Kiểm tra thông tin tài nguyên
* **Bước 2: Hệ thống gửi thông tin xác nhận đến người dùng**
  * Email thông báo thông tin tài nguyên vừa khởi tạo
  * Ghi nhận thời gian bắt đầu sử dụng tài nguyên dùng cho việc tính giá sử dụng tài nguyên tại thời điểm cuối tháng
