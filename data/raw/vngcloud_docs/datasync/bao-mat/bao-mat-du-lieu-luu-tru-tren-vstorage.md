# Bảo mật dữ liệu lưu trữ trên vStorage

Mã hóa nội dung các tệp tin (object) được lưu trữ là một giải pháp bảo mật dữ liệu hiệu quả. Bằng cách mã hóa dữ liệu khi lưu trữ, dữ liệu sẽ được biến đổi thành một dạng không thể đọc được đối với những người không có quyền truy cập. Điều này giúp bảo vệ dữ liệu khỏi bị truy cập trái phép, ngay cả khi kẻ tấn công có thể truy cập vào gateway storage của hệ thống.

VNG Cloud hiện tại cung cấp cơ chế mã hóa nội dung các tệp tin (object) được lưu trữ trên dịch vụ vStorage như sau:

* **Mã hóa tại người dùng (Client-side encryption):** Trong cơ chế này, người dùng sẽ chịu trách nhiệm quản lý key và workload của quá trình mã hóa. Dữ liệu sẽ được mã hóa tại máy của người dùng hoặc lớp ứng dụng của người dùng.

Do đó, nếu khách hàng muốn triển khai mã hóa nội dung các tệp tin (object) được lưu trữ trên dịch vụ vStorage của VNG Cloud, VNG Cloud khuyến nghị khách hàng sử dụng cơ chế mã hóa tại máy của người dùng.
