# Người dùng trả trước & trả sau

Sử dụng tài liệu này để hiểu rõ hơn về các hình thức sử dụng tài nguyên theo loại người dùng. Ở cấp độ VGN Cloud Service, chúng tôi hỗ trợ 2 loại người dùng chính:

* **Người dùng trả trước:** Là người dùng phải thanh toán chi phí sử dụng tài nguyên trước khi được phép sử dụn&#x67;**.** Thanh toán chi phí sử dụng tài nguyên theo cấu hình và thời gian muốn sử dụng (Cần xác định thời điểm ngừng sử dụng tài nguyên).
* **Người dùng trả sau:** Là người dùng được phép sử dụng tài nguyên trước và trả tiền sau, dựa trên chi phí sử dụng tài nguyên thực tế. Số tiền phải chi trả sẽ được chốt định kỳ mỗi cuối tháng cho đến khi người dùng không sử dụng tài nguyên nữa.

Cùng điểm qua một số khác biệt về khái niệm cũng như quyền hạn và chức năng giữa 2 loại người dùng này đối với các dịch vụ VNG Cloud như:

* **Quy trình action trên tài nguyên:** Khởi tạo, thay đổi cấu hình, gia hạn, khôi phục, xóa tài nguyên
* **Quy trình cung cấp tài nguyên**
* **Quản lý tài nguyên**
* **Quản lý hóa đơn**
* **Quản lý thanh toán**

#### **So sánh người dùng trả trước và trả sau** <a href="#nguoidungtratruoc-and-trasau-sosanhnguoidungtratruocvatrasau" id="nguoidungtratruoc-and-trasau-sosanhnguoidungtratruocvatrasau"></a>

***

#### 1. Quy trình action trên tài nguyên <a href="#nguoidungtratruoc-and-trasau-1.quytrinhactiontrentainguyen" id="nguoidungtratruoc-and-trasau-1.quytrinhactiontrentainguyen"></a>

* **Người dùng trả trước**

<figure><img src="https://docs.vngcloud.vn/download/attachments/49649325/Daily_Job_HC%20(3)-Page-5.drawio.png?version=1&#x26;modificationDate=1678094370000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Người dùng trả sau**

<figure><img src="https://docs.vngcloud.vn/download/attachments/49649325/Daily_Job_HC%20(3)-Page-6.drawio.png?version=1&#x26;modificationDate=1678094411000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

#### 2. Quy trình cung cấp tài nguyên <a href="#nguoidungtratruoc-and-trasau-2.quytrinhcungcaptainguyen" id="nguoidungtratruoc-and-trasau-2.quytrinhcungcaptainguyen"></a>

* **Người dùng trả trước**
  * Sau khi xác nhận thanh toán thành công, phía Product sẽ tiến hành cung cấp tài nguyên theo cấu hình mà người dùng yêu cầu
  * Trong quá trình cung cấp tài nguyên, nếu có xảy ra lỗi quá trình, hệ thống sẽ tiến hành hoàn trả tiền dịch vụ đã thanh toán của người dùng ở bước trước đó. Tiền được hoàn trả sẽ quy về Credit và chuyển vào ví VNG Cloud
* **Người dùng trả sau**
  * Ngay tại bước "Xác nhận", Product sẽ tiến hành cung cấp tài nguyên theo cấu hình người dùng yêu cầu, và hệ thống sẽ ghi nhận lại thời gian bắt đầu sử dụng tài nguyên.

_→ Ghi chú: Vì là người dùng trả sau nên sẽ không cần phải thực hiện bước thanh toán tại quy trình action trên tài nguyên._

#### 3. Quản lý tài nguyên <a href="#nguoidungtratruoc-and-trasau-3.quanlytainguyen" id="nguoidungtratruoc-and-trasau-3.quanlytainguyen"></a>

Về cơ bản, các tính năng mà người dùng có thể thực hiện trên tài nguyên như:

* **Đối với người dùng trả trước**:
  * Khởi tạo mới
  * Thay đổi cấu hình
  * Gia hạn
  * Khôi phục tài nguyên
  * Tự động gia hạn
  * xóa tài nguyên
* **Đối với người dùng trả sau:**
  * Khởi tạo mới
  * Thay đổi cấu hình
  * xóa tài nguyên

Tham khảo chi tiết hơn tại mục: [**Quản lý tài nguyên**](nguoi-dung-tra-truoc-and-tra-sau.md#nguoidungtratruoc-and-trasau-3.quanlytainguyen)

#### 4. Quản lý hóa đơn <a href="#nguoidungtratruoc-and-trasau-4.quanlyhoadon" id="nguoidungtratruoc-and-trasau-4.quanlyhoadon"></a>

* **Người dùng trả trước**
  * Tại bước thanh toán thành công, sau khi cung cấp tài nguyên thành công, hệ thống sẽ phát sinh **hóa đơn được tính là đã thanh toán** tương ứng với tài nguyên của người dùng.&#x20;
* **Người dùng trả sau**
  * Hóa đơn theo tài nguyên sẽ được phát sinh mỗi cuối tháng, dựa vào sử dụng thực tế của khách hàng trong tháng đó.
  * Hóa đơn được phát sinh sẽ được tính là chưa thanh toán, người dùng có thể thanh toán qua hai hình thức sau:
    * Liên hệ đội ngũ Sale, Support
    * Truy cập vào [**user portal, mục Billing history**](https://dashboard.console.vngcloud.vn/billing-report), chọn hóa đơn cần thanh toán và tiến hành thanh toán

#### 5. Quản lý thanh toán <a href="#nguoidungtratruoc-and-trasau-5.quanlythanhtoan" id="nguoidungtratruoc-and-trasau-5.quanlythanhtoan"></a>

* **Người dùng trả trước**
  * Lịch sử thanh toán sẽ xuất hiện ngay tại [**User Portal, mục Payment history**](https://dashboard.console.vngcloud.vn/payment-history) ngay sau khi người dùng thực hiện thanh toán tài nguyên
* **Người dùng trả sau**
  * Về cơ bản, người dùng trả sau sẽ có lịch sử thanh toán trong các trường hợp sau:
    * Hệ thống thanh toán hóa đơn tự động → Tìm hiểu thêm tại phần [**thanh toán hóa đơn tự động**](thanh-toan/thanh-toan-hoa-don-tu-dong.md)
    * Người dùng chủ động thực hiện thanh toán hóa đơn tại User Portal

#### **Làm sao để thay đổi từ trả trước sang trả sau và ngược lại?** <a href="#nguoidungtratruoc-and-trasau-lamsaodethaydoitutratruocsangtrasauvanguoclai" id="nguoidungtratruoc-and-trasau-lamsaodethaydoitutratruocsangtrasauvanguoclai"></a>

***

* **Khi người dùng đăng ký mới tài khoản tại VNG Cloud**, hệ thống sẽ mặc định đây là **người dùng trả trước.**
* Để **chuyển sang loại người dùng trả sau**, người dùng chủ động **liên hệ bộ phân Sale / Support** để được hỗ trợ theo yêu cầu.
* Trường hợp người dùng là loại trả sau và muốn **quay về loại trả trước**, cũng chủ động **liên hệ bộ phân Sale / Support** để được hỗ trợ theo yêu cầu.
