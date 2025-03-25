# Phân quyền truy cập thông qua IAM

Phân quyền truy cập là yếu tố thiết yếu của bảo mật nhằm xác định đối tượng và điều kiện để truy cập vào một số dữ liệu, ứng dụng và tài nguyên nhất định.

Chính sách kiểm soát truy cập chủ yếu dựa trên các kỹ thuật như xác thực và ủy quyền, cho phép tổ chức xác minh rõ ràng rằng người dùng không bị giả mạo và được cấp mức độ truy cập thích hợp dựa trên thông tin người dùng, vai trò cùng nhiều yếu tố khác.&#x20;

Thông qua IAM, người dùng VNG Cloud, cụ thể là website vConsole có thể chủ động phân quyền hoặc được phân quyền truy cập/hành động trên từng tính năng cụ thể.

Để hiểu rõ hơn, người dùng cần tìm hiểu xem:

* **IAM là gì và sử dụng như thế nào?** Tham khảo tài liệu hướng dẫn [tại đây](../../../../identity-and-access-management-iam.md)
* **Truy cập đến IAM tại**: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)

Khi đã hiểu rõ về cách hoạt động cũng như sử dụng vIAM, người dùng có thể truy cập đến vIAM để phân quyền cho các tính năng của vConsole như sau

### **Hướng dẫn phân quyền tính năng vConsole thông qua vIAM** <a href="#phanquyentruycapthongquaiam-huongdanphanquyentinhnangvconsolethongquaviam" id="phanquyentruycapthongquaiam-huongdanphanquyentinhnangvconsolethongquaviam"></a>

***

* Bước 1: Truy cập vào website IAM[ tại đây](https://hcm-3.console.vngcloud.vn/iam/)
* Bước 2: Khởi tạo **Policy**
  * 2.1: Chọn Product vConsole
  * 2.2 Chọn nhóm tính năng được phép truy cập hoặc không đối với các trang chức năng tại vConsole

| Access level | Usage Report                                                         | Billing History                                                  | Payment History | Credit History | Other Features                                                    |
| ------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------- | -------------- | ----------------------------------------------------------------- |
| List         | ListUsages                                                           | ListBillings                                                     | ListPayments    | List Credit    | <p><br></p>                                                       |
| Read         | <p>ExportUsages</p><p>GetTrafficUsages</p><p>ExportTrafficUsages</p> | <p>ExportBillings</p><p>GetBillingStatistic</p><p>GetBilling</p> | ExportPayments  | ExportCredits  | <p>GetUserInfo</p><p>ResultBackBuyCredit</p><p>GetUserBalance</p> |
| Write        | <p><br></p>                                                          | <p><br></p>                                                      | <p><br></p>     | <p><br></p>    | BuyCredit                                                         |

* Bước 3: Khởi tạo Policy thành công
* Bước 4: Khởi tạo **User Account** / **Group Permissions & Users**
  * Trong trường hợp khởi tại Group Permissions, lưu ý nhớ thêm User Account vào Group vừa tạo
* Bước 5: Attach Policy vừa khởi tạo vào Group Permission / User Account
* Bước 6: Lúc này, bạn đã hoàn tất việc phân quyền tính năng trên vConsole cho user trên hệ thống IAM. IAM user dùng tài khoản & mật khẩu được cấp đăng nhập vào [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/) và truy cập, sử dụng các tính năng được cấp quyền để sử dụng.

\
