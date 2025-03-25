# Khởi tạo một Private SMB File Storage

## Tổng quan

SMB (Server Message Block) là giao thức phổ biến được sử dụng để chia sẻ tệp, thư mục trên môi trường Windows server, việc triển khai SMB có thể sử dụng hai phương thức xác thực chính: **Basic Authentication** và **Active Directory (AD) Authentication**. Dưới đây là sự khác biệt và ứng dụng của mỗi phương thức.

## Chi tiết

* SMB với Basic Authentication: Người dùng đăng nhập vào File Storage SMB bằng **username/password** được cấu hình thủ công khi khởi tạo File Storage.
* **SMB với AD Authentication:** Người dùng xác thực qua tài khoản **Active Directory** mà người dùng khởi tạo qua Windows server.
