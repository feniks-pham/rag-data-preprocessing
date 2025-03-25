# Bảo mật (security)

VNG Cloud có trách nhiệm đảm bảo tính bảo mật của hạ tầng vật lý cũng như hạ tầng ảo hóa đang cung cấp cho các dịch vụ của VNG Cloud. Ngoài ra VNG cũng cung cấp các dịch vụ cho phép khách hàng tự triển khai các chức năng bảo mật cho hệ thống của khách hàng đặt tại VNG Cloud.

An toàn mạnh là ưu tiên hàng đầu tại VNG Cloud. Khách hàng của VNG Cloud sẽ được thừa hưởng các tiêu chuẩn bảo mật tiêu chuẩn nhất dành cho các tổ chức, doanh nghiệp. Trách nhiệm an toàn bảo mật sẽ bao gồm ở cả 2 bên là VNG Cloud và chính khách hàng, có thể kể đến các trách nhiệm của KH như:

* Quản lý việc truy cập các tài nguyên lưu trữ của KH thông qua quản lý quyền hạn truy cập đến tài nguyên lưu trữ của KH.
* Quản lý các thông tin tuy cập tài khoản người dùng như **Tên đăng nhập, Mật khẩu**.
* Phân quyền truy cập hệ thống đúng đắn dựa trên IAM cho các tài nguyên của KH tại VNG Cloud.

Để bảo vệ thông tin của KH và dữ liệu mà KH lưu trữ trên dịch vụ vStorage, hiện tại đang áp dụng các biện pháp kiểm soát bảo mật như:

1. **Bảo mật quyền hạn truy cập:** VNG Cloud sử dụng IAM để quản lý quyền truy cập của người dùng vào các tài nguyên vStorage. IAM cho phép các doanh nghiệp tạo và quản lý các chính sách truy cập cho từng tài nguyên vStorage. Điều này giúp đảm bảo rằng chỉ những người có quyền truy cập cần thiết mới có thể truy cập vào dữ liệu.
2. **Bảo mật dữ liệu trên đường truyền:** VNG Cloud sử dụng HTTPS để mã hóa dữ liệu trên đường truyền. HTTPS là một giao thức bảo mật dựa trên HTTP, sử dụng mã hóa TLS/SSL để bảo vệ dữ liệu trong quá trình truyền.
3. **Bảo mật dữ liệu lưu trữ trên vStorage:** VNG Cloud cung cấp hai cơ chế mã hóa nội dung các tệp tin (object) được lưu trữ trên dịch vụ vStorage:
   * **Mã hóa tại người dùng (Client-side encryption):** Trong cơ chế này, người dùng sẽ chịu trách nhiệm quản lý key và workload của quá trình mã hóa. Dữ liệu sẽ được mã hóa tại máy chủ của người dùng hoặc lớp ứng dụng của người dùng.

VNG Cloud luôn nỗ lực để nâng cao các biện pháp bảo mật của mình để đảm bảo an toàn cho dữ liệu của khách hàng.
