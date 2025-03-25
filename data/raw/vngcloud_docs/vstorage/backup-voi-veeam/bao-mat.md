# Bảo mật

## Tổng quan <a href="#baomat-security-tongquan" id="baomat-security-tongquan"></a>

VNG Cloud có trách nhiệm đảm bảo tính bảo mật của hạ tầng vật lý cũng như hạ tầng ảo hóa đang cung cấp cho các dịch vụ của VNG Cloud. Ngoài ra VNG cũng cung cấp các dịch vụ cho phép khách hàng tự triển khai các chức năng bảo mật cho hệ thống của khách hàng đặt tại VNG Cloud.

Do đó, việc sao lưu dữ liệu với phần mềm Veeam cũng đảm bảo an toàn vả giảm rủi ro xâm phạm trong quá trình sao lưu định kỳ, những biện pháp kiểm soát bảo mật như:

* Bảo mật kênh truyền khi sao lưu
* Phân quyền truy cập dữ liệu&#x20;
* Xác thực đa yếu tố (Multi-factor authentification)
* Mã hóa dữ liệu khi sao lưu trên đường truyền (Data encryption);
* Kiểm soát và ghi Logs (Audit & Logging)

***

## Bảo mật kênh truyền khi sao lưu

Để bảo mật kênh truyền cho sao lưu , cần xem xét các khuyên nghị sau:

* Sử dụng phân hoạch mạng (segmentation): Tạo ra các chính sách phân hoạch mạng để kiểm soát lưu lượng, hạn chế truy cập vào các hạ tầng sao lưu nhạy cảm. Đảm bảo chỉ những cổng (ports) được sử dụng mới được mở;
* Cô lập lưu lượng sao lưu: Sử dụng một mạng cô lập để truyền dữ liệu giữa các thành phần hạ tầng sao lưu:
* Vô hiệu quá các giao thức mạng lỗi thời như: SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1, SMB 1.0, LLMNR, NetBIOS.

***

## Phân quyền truy cập&#x20;

Quyền quản trị máy chỉ sao lưu cho phép người dùng truy cập vào các thành phần hạ tầng sao lưu. Nếu tin tặc có những quyền này, thì họ sẽ phá hoại được hầu hết cả dữ liệu và bản sao lưu. Để giảm thiểu rủi ro Veeam phân quyền các tài khoản để hoạt động quản trị các dữ liệu sao lưu. Xem thêm phần <mark style="color:blue;">Quản lý truy cập</mark>

***

## **Xác thực đa yếu tố**

Phần mềm Veeam hỗ trợ xác thực đa yếu tố (Multi-Factor Authentification - MFA)  để xác thực người dùng, với mã OTP được tạo ra trong ứng dụng xác thực trên thiết bị di động được sử dụng như phương thức xác minh. Kết hợp với thông tin đăng nha6p và mật khẩu, thì tạo ra một môi trường an toàn hơn và bảo vệ tài khoản người dùng khỏi những xâm phạm độc hại.

**Kích hoạt chức năng MFA:**

1. Đăng nhập vào Veeam với vai trò Administrator;
2. Chọn mục User and Roles, màn hình Security hiện lên;
3. Màn hình liệt kê danh sách User or Group với Role tương ứng;
4. Chọn tùy chọn "Enable Multi-factor Autentification (MFA)
5. Nhấn OK để hoàn tất việc kích hoạt MFA.

***

## **Mã hóa dữ liệu trên đường truyền**

Khi truyền Khi cấu hình job tự động sao lưu dữ liệu, nếu bật tính năng mã hóa và nén dữ liệu, thì từ phía nguồn dữ liệu sẽ nén dữ liệu trước sau đó mã hóa khá khối dữ liệu đã nén.

Các dữ liệu sau khi mã hóa thì không thể đọc được, với sự hỗ trợ của của thuật toán mã hóa và khóa bí mật (secret key), nên tin tặc không thể mở được hay đọc được dữ liệu đã mã hóa. Chỉ có người nhận biết khóa bí mật (secret key) mới giải mã để xem được dữ liệu.

Việc mã hóa dữ liệu ở những hoạt động sau:

* Chạy Job sao lưu dữ liệu;
* Chạy Job sao lưu log các giao dịch;
* Chạy Job sao chép sao lưu;

***

## Kiểm soát và ghi Logs

Veeam cung cấp khả năng ghi lại Logs tất cả hoạt động đã thực hiện, chẳng hạn như các tác vụ sao lưu dữ liệu hay phục hồi khi có sự cố.

{% hint style="info" %}
**Ví dụ:**

Danh sách các tập tin được phục hồi trong các lần Restore. Kết quả của việc kiểm tra các hoạt động như vậy được trữ dưới dạng tập tin \*.csv gọi là audit logs.
{% endhint %}

Bạn có thể chỉ định thư mục nơi các Logs kiểm tra sẽ được lưu trữ. Theo mặc định, các tệp nhật ký được lưu trữ trong thư mục sau: %ProgramData%\Veeam\Backup\Audit.
