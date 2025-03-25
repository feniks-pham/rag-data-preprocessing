# Quản lý tài khoản truy cập vStorage

#### Tổng quan <a href="#quanlytaikhoantruycapvstorage-tongquan" id="quanlytaikhoantruycapvstorage-tongquan"></a>

Bạn có thể sử dụng 3 loại tài khoản để truy cập vào vStorage. Chi tiết 3 loại này bao gồm:

* **Root user account:** Là tài khoản [khởi tạo đầu tiên](https://register.vngcloud.vn/signup) để truy cập vào VNG Cloud với đầy đủ quyền truy cập vào tất cả dịch vụ tài nguyên trên VNG Cloud.
* **IAM user account (User account):** Là tài khoản được tạo ra từ tài khoản Root user account duy nhất với những quyền truy cập phụ thuộc vào chính sách cho phép truy cập được thiết lập từ Root user account.
* **Service account:** Tài khoản được sử dụng bởi 1 ứng dụng/máy, thực hiện các lệnh gọi API được ủy quyền và truy cập các tài nguyên được chỉ định trên VNG Cloud.

***

#### Chủ đề <a href="#quanlytaikhoantruycapvstorage-chude" id="quanlytaikhoantruycapvstorage-chude"></a>

* Tài khoản người dùng Root
* Tài khoản người dùng IAM
  * Khởi tạo tài khoản IAM User Account
  * Khởi tạo policy cho IAM User Account
  * Liên kết tài khoản IAM User Account với policy tương ứng
  * Hủy tài khoản IAM User Account
* Tài khoản Service Account
  * Khởi tạo tài khoản Service Account
  * Khởi tạo policy cho Service Account
  * Liên kết tài khoản Service Account với policy tương ứng
  * Khởi tạo vStorage Credentials
    * Khởi tạo S3 key
    * Khởi tạo Swift user
    * Liên kết S3 key, Swift user với tài khoản Service Account tương ứng
    * Hủy S3 key, Swift user
  * Hủy tài khoản Service Account
