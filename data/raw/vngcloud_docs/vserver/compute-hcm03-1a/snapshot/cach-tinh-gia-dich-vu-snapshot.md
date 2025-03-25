# Cách tính giá dịch vụ Snapshot

Dịch vụ Snapshot cung cấp hai phương thức thanh toán để phục vụ các mục tiêu và chiến lược tài chính khác nhau của từng khách hàng. Hai hình thức thanh toán được triển khai cho dịch vụ Snapshot tại VNG Cloud bao gồm:

* Phương thức thanh toán Trả Trước.
* Phương thức thanh toán Trả Sau.

Các phương thức thanh toán và cách tính phí này cung cấp tính linh hoạt và kiểm soát đối với các chi phí dịch vụ Snapshot. Người dùng có thể chọn phương thức thanh toán phù hợp nhất với chiến lược tài chính và nhu cầu sử dụng của họ. Điều quan trọng là hiểu rõ phương thức thanh toán đã chọn để quản lý hiệu quả các chi phí bản snapshot và duy trì truy cập liên tục vào dịch vụ này.

#### **1. Cách Tính Phí Snapshot** <a href="#cachtinhgiadichvusnapshot-1.cachtinhphisnapshot" id="cachtinhgiadichvusnapshot-1.cachtinhphisnapshot"></a>

Cách tính phí Snapshot áp dụng chung cho cả 2 hình thức thanh toán, bao gồm Trả Trước và Trả Sau.

* **Công thức**: Chi phí của việc tạo bản snapshot được tính dựa trên kích thước của bản snapshot (theo đơn vị gigabyte) và thời gian sử dụng của nó (thường được đo bằng giờ).
* **Thời gian sử dụng**: Người dùng sẽ được tính phí cho thời gian tồn tại của bản snapshot. Thời gian này được ghi nhận theo giờ.
* **Ví dụ**: Ví dụ, nếu bạn có một bản snapshot có kích thước 100GB và giá đơn vị cho Dịch Vụ Snapshot là 7,7 VND cho mỗi GB-giờ, thì chi phí sẽ được tính như sau:
  * Theo giờ: 7,7 VND \* 100 GB = 770 VND mỗi giờ.
  * Theo ngày: 770 VND \* 24 = 18,480 VND mỗi ngày.
  * Theo tháng: 18,480 \* 30 = 554,400 VND mỗi tháng.
* **Lưu ý**: Giá đơn vị được cung cấp chỉ để tham khảo. Thời gian sử dụng thực tế của các bản snapshot được ghi nhận hàng giờ, dựa trên kích thước thực tế của các bản snapshot của bạn.

#### 2. Phương thức thanh toán trả trước <a href="#cachtinhgiadichvusnapshot-2.phuongthucthanhtoantratruoc" id="cachtinhgiadichvusnapshot-2.phuongthucthanhtoantratruoc"></a>

Đối với người dùng Trả Trước, VNG Cloud áp dụng hình thức Hold Credit - Tạm giữ Credit để hỗ trợ việc sử dụng cũng như tính chi phí cho dịch vụ Snapshot. Tìm hiểu thêm về Hold Credit tại [Tạm giữ Credit](../../../quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/trai-nghiem-billing-and-kenh-thanh-toan/ve-billing-and-payment/thanh-toan/tam-giu-credit.md).

* **Hình thức**: Dưới phương thức Tạm giữ Credit, người dùng phải duy trì số dư trả trước đủ để chi trả phần sử dụng dịch vụ trong tài khoản của họ.
* **Kích hoạt Snapshot:** Khi kích hoạt Snapshot lần đầu, người dùng sẽ được điều hướng đến cổng thanh toán của VNG Cloud để ghi nhận nguồn tiền được sử dụng cho dịch vụ Snapshot. Lưu ý rằng, hành động này chỉ nhằm mục đích ghi nhận nguồn tiền sử dụng, người dùng hoàn toàn không mất phí cho lần kích hoạt đầu tiên.
* **Chi phí tạo Snapshot**: Khi người dùng tạo một bản snapshot, hệ thống sẽ không tính chi phí ngay lập tức, mà sẽ được ghi nhận lại mỗi giờ sau đó. Cứ mỗi ngày một lần, hệ thống sẽ tiến hành Tạm giữ Credit cho phần sử dụng dịch vụ, chi phí này được xác định dựa trên kích thước của bản snapshot và thời gian sử dụng trong ngày hôm đó.
* **Quản lý số dư**: Người dùng có trách nhiệm quản lý số dư trả trước của họ để đảm bảo đủ để chi trả cho việc sử dụng bản snapshot thep kế hoạch dự kiến, phần số dư này phải đủ để bao phủ cho việc sử dụng dịch vụ đến thời điểm hiện tại và 3 ngày tiếp theo đó. Chi tiết tham khảo tại [Tạm giữ Credit](../../../quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/trai-nghiem-billing-and-kenh-thanh-toan/ve-billing-and-payment/thanh-toan/tam-giu-credit.md).
* **Thông báo số dư thấp**: Để tránh gián đoạn dịch vụ, hệ thống sẽ gửi thông báo khi số dư trả trước giảm xuống dưới một ngưỡng cụ thể, khuyến nghị người dùng nạp thêm tiền. Trường hợp đã được nhắc nhở nhiều lần, nhưng số dư vẫn liên tục không đảm bảo, VNG Cloud sẽ tạm thời dừng cung cấp dịch vụ ([Vô hiệu hóa dịch vụ Snapshot](vo-hieu-hoa-dich-vu-snapshot.md)) Snapshot đến người dùng.

#### **3. Phương Thức Thanh Toán Trả Sau** <a href="#cachtinhgiadichvusnapshot-3.phuongthucthanhtoantrasau" id="cachtinhgiadichvusnapshot-3.phuongthucthanhtoantrasau"></a>

Đối với người dùng trả sau, VNG Cloud áp dụng hình thức sử dụng trước - trả tiền sau, tương tự các dịch vụ khác

* **Chu kỳ thanh toán**: Người dùng sử dụng phương thức thanh toán trả sau không cần duy trì số dư trả trước. Thay vào đó, các khoản phí dịch vụ Snapshot được tính vào cuối mỗi chu kỳ thanh toán hàng tháng.
* **Tính linh hoạt trong việc sử dụng Snapshot**: Với thanh toán trả sau, người dùng có thể kích hoạt & tạo bản snapshot khi cần mà không cần quan tâm đến số dư khả dụng, cung cấp tính linh hoạt lớn hơn.
* **Hóa đơn thanh toán hàng tháng**: Các khoản phí dịch vụ Snapshot được liệt kê trên bảng kê thanh toán hàng tháng, cung cấp cho người dùng một bản tóm tắt rõ ràng về các chi phí liên quan đến bản snapshot.
* **Thanh toán đúng hạn**: Thanh toán đúng hạn hóa đơn hàng tháng là rất quan trọng để đảm bảo truy cập liên tục vào dịch vụ Snapshot.
* **Theo dõi sử dụng**: Người dùng có thể theo dõi việc sử dụng Snapshot của mình thông qua cổng thanh toán, giúp họ nắm bắt chi phí và việc sử dụng tài nguyên.

\
