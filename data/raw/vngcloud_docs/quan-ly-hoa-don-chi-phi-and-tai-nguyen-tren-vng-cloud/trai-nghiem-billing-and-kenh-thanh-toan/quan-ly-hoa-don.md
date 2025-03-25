# Quản lý hóa đơn

Sử dụng tài liệu này như là một hướng dẫn giúp bạn quản lý và kiểm soát các hóa đơn khi sử dụng dịch vụ tại VNG Cloud Service tốt hơn.

Tại đây, chúng tôi cung cấp cho người dùng cái nhìn đầy đủ và chi tiết về cách xử lý hóa đơn ở cấp VNG Cloud Service như:

* **Thời điểm khởi tạo hóa đơn**
* **Thông tin hóa đơn**
* **Thời điểm thanh toán hóa đơn**
* **Xem danh sách hóa đơn**

### **Thời điểm khởi tạo hóa đơn** <a href="#quanlyhoadon-thoidiemkhoitaohoadon" id="quanlyhoadon-thoidiemkhoitaohoadon"></a>

***

Hóa đơn được khởi tạo trong các trường hợp sau:

1. **Người dùng trả trước thực hiện hành động làm phát sinh / thay đổi về chi phí sử dụng tài nguyên như**:
   1. Khởi tạo tài nguyên:
      1. Phát sinh hóa đơn mới tương ứng với tài nguyên khởi tạo
   2. Thay đổi cấu hình tài nguyên:&#x20;
      1. Cập nhật thông tin hóa đơn cũ, phát sinh hóa đơn mới với cấu hình mới
   3. Gia hạn tài nguyên:
      1. Phát sinh hóa đơn mới với cùng cấu hình tài nguyên, khác thời gian sử dụng
   4. Khôi phục tài nguyên:
      1. Phát sinh hóa đơn mới với cùng cấu hình tài nguyên, khác thời gian sử dụng
2. **Hệ thống chốt thông tin sử dụng tài nguyên của người dùng trả sau cuối mỗi tháng:**
   1. Đối với người dùng trả sau, tương ứng với mỗi tài nguyên sẽ phát sinh 1 hóa đơn để ghi nhận lại con số sử dụng thực tế
   2. Trường hợp người dùng có nhiều tài nguyên thì sẽ phát sinh nhiều đầu hóa đơn tương ứng cho từng tài nguyên

### **Thông tin hóa đơn** <a href="#quanlyhoadon-thongtinhoadon" id="quanlyhoadon-thongtinhoadon"></a>

***

**Thông tin trên hóa đơn** bao gồm các thông tin chính tương ứng với 1 tài nguyên cụ th&#x1EC3;**:**

* Mã hóa đơn
* Ngày tạo hóa đơn
* Thời gian sử dụng tài nguyên
* Mô tả chi tiết: Mô tả chi tiết tài nguyên và cấu hình sử dụng
* Số tiền

**Đối với người dùng trả trước**

* **Số tiền trên hóa đơn** là số tiền người dùng cần phải trả để **sử dụng 1 tài nguyên cụ thể**, tính trên các yếu tố:
  * (1) Cấu hình tài nguyên
  * (2) Đơn giá theo cấu hình (Có giảm giá hoặc không): Tại thời điểm thực hiện hành động trên tài nguyên (đã bao gồm VAT)
  * (3) Thời gian sử dụng tài nguyên: Ngày bắt đầu, Ngày kết thúc (tính tới phút)
  * (4) Giảm trừ Coupon (nếu có)

Ví dụ công thức tính giá trị hóa đơn khi khởi tạo Server bao gồm thông tin:

| Cấu hình Server (1)                                                                                                      | Đơn giá (bao gồm VAT) (2) | Thời gian sử dụng (3) | Giá trị Coupon (4) | Thành tiền = (2) \* (3)  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------- | --------------------- | ------------------ | ------------------------ |
| Image (dev.v1.small1x1)                                                                                                  | 90,000 VND / 30 ngày      | 60 ngày               | 20,000 VND         | 180,000                  |
| Root disk (Size 20GB, IOPS 3000)                                                                                         | 35,000 VND / 30 ngày      | 60 ngày               | 70,000             |                          |
| Giá sử dụng tài nguyên in trên hóa đơn = Total thành tiền - giá trị Coupon **=** 180,000 + 70,000 - 20,000 = 230,000 VND |                           |                       |                    |                          |

**Đối với người dùng trả sau**

* Số tiền trên hóa đơn là số tiền được tính dựa trên chi phí thực tế khi sử dụng tài nguyên
* Báo cáo chi phí sử dụng tài nguyên sẽ được xuất vào cuối tháng, tại user portal: [https://dashboard.console.vngcloud.vn/usage-report](https://dashboard.console.vngcloud.vn/usage-report)
* Để hiểu thêm về cách tính giá tiền sử dụng tài nguyên tài nguyên trong tháng, mời tham khảo thêm [**tại đây**](../vconsole-kenh-quan-ly-chung-ve-hoa-don-va-tai-nguyen-tren-vng-cloud/trai-nghiem-vconsole/thong-ke-su-dung.md)**.**

### **Thời điểm thanh toán hóa đơn** <a href="#quanlyhoadon-thoidiemthanhtoanhoadon" id="quanlyhoadon-thoidiemthanhtoanhoadon"></a>

***

* **Đối với người dùng trả trước:**
  * Hóa đơn được phát sinh ngay sau khi hệ thống cung cấp tài nguyên thành công, lúc này hóa đơn được phát sinh với trạng thái đã thanh toán
* **Đối với người dùng trả sau**:
  * Sau khi phát sinh hóa đơn dịch vụ vào cuối tháng, người dùng có thể trả theo nhiều hình thức
    * Trao đổi bên ngoài như chuyển khoản cho bộ phận Sale Operation
    * Thanh toán ngay tại user portal bằng cách nạp credit vào ví

### **Xem danh sách hóa đơn** <a href="#quanlyhoadon-xemdanhsachhoadon" id="quanlyhoadon-xemdanhsachhoadon"></a>

***

Chúng tôi cung cấp website user portal để giúp người dùng quản lý hóa đơn sử dụng tại nguyên một cách tốt nhất và hiệu quả nhất:

* Truy cập vào trang quản lý hóa đơn tại đây: [https://dashboard.console.vngcloud.vn/billing-report](https://dashboard.console.vngcloud.vn/billing-report)
* Để xem thêm hướng dẫn sử dụng cũng như các tính năng của trang quản lý hóa đơn, mời tham khảo thêm [**tại đây**](../vconsole-kenh-quan-ly-chung-ve-hoa-don-va-tai-nguyen-tren-vng-cloud/trai-nghiem-vconsole/lich-su-hoa-don.md)
