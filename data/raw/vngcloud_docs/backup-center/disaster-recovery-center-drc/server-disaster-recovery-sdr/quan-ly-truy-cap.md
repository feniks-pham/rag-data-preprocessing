# Quản lý truy cập

Khi triển khai và quản lý Server Disaster Recovery (SDR) trên VNG Cloud, việc thiết lập chính sách truy cập và phân quyền (IAM) là rất quan trọng để đảm bảo an ninh và kiểm soát chặt chẽ các hoạt động liên quan đến DR. Tham khảo bài viết dưới đây để tiến hành quản lý truy cập và phân quyền trên SDR

## 1. Danh sách endpoint

<table><thead><tr><th width="138">Level</th><th>Action</th><th>Mô tả</th></tr></thead><tbody><tr><td>Write</td><td>DrPairAttachServer</td><td>Thêm máy chủ chính vào DRC</td></tr><tr><td>Write</td><td>DrPairStartReplication</td><td>Khởi tạo quá trình sao chép</td></tr><tr><td>Write</td><td>DrPairTestFailover</td><td>Kiểm tra chuyển đổi dự phòng</td></tr><tr><td>Write</td><td>DrPairChangeRecoveryPoint</td><td>Thay đổi Recovery Point</td></tr><tr><td>Write</td><td>DrPairCleanTestEnvironment</td><td>Xóa môi trường kiểm tra chuyển đổi dự phòng</td></tr><tr><td>Write</td><td>DrPairCommitFailover</td><td>Xác nhận chuyển đổi dự phòng</td></tr><tr><td>Write</td><td>DrPairDetachServer</td><td>Xóa thông tin pairing</td></tr><tr><td>Write</td><td>DrPairFailover</td><td>Chuyển đổi dự phòng</td></tr><tr><td>Write</td><td>DrPairRestartReplication</td><td>Khởi tạo lại quá trình sao chép</td></tr><tr><td>Write</td><td>DrPairResumeReplication</td><td>Tiếp tục sao chép </td></tr><tr><td>Write</td><td>DrPairStopReplication</td><td>Tạm dừng sao chép</td></tr><tr><td>List</td><td>ListDrPairs</td><td>Xem danh sách pairing</td></tr><tr><td>Get</td><td>GetDrPair</td><td>Xem thông tin chi tiết pairing</td></tr><tr><td>Get</td><td>GetDrPairHistory</td><td>Xem lịch sử thao tác trên pairing</td></tr><tr><td>Get</td><td>GetDrPairRecoveryPoints</td><td>Xem danh sách recovery point</td></tr></tbody></table>

## **2. Danh sách VNG Managed DR Policies**  <a href="#iamforvserver-2.danhsachvngmanagedpolicies" id="iamforvserver-2.danhsachvngmanagedpolicies"></a>

VNG Managed Policy là các Chính Sách IAM (IAM Policy) được tạo mặc định bởi hệ thống IAM VNG Cloud. Các Chính Sách này được quản lý bởi chính VNG Cloud nhằm mục đích hỗ trợ người dùng trong việc cài đặt nhanh chóng các quyền truy cập cần thiết cho các tài khoản người dùng IAM đối với các tài nguyên của từng Product cụ thể. Cùng tìm hiểu danh sách VNG Managed Policies cho DR:

* [DRFullAccess:](https://iam.console.vngcloud.vn/policies/76de3567-c57c-4167-b304-9133f9af7daf) Bao gồm toàn quyền truy cập đến các tài nguyên thuộc Disaster Recovery Center
* [DRReadOnlyAccess:](https://iam.console.vngcloud.vn/policies/3d44e007-fcd1-4d6f-85b9-f3981ef286a1) Chỉ bao gồm quyền Đọc (Read) trên các tài nguyên thuộc hệ Disaster Recovery Center

## 3. Bắt đầu sử dụng IAM với DRC

Hướng dẫn này nhằm hướng dẫn người dùng có thể nhanh chóng bắt đầu sử dụng IAM trong các dịch vụ DRC bằng cách sử dụng quyền mặc định **(được định nghĩa bởi VNG Cloud Managed Policies)** cho hệ thống DRC gọi là **DRFullAccess.** Tuy nhiên, các tính năng, dịch vụ tại DRC có liên kết và thừa hưởng từ vServer, do đó, để có thể phân quyền trên DRC, bạn cần chú ý thêm các quyền tương ứng của vServer (các quyền trên Server, Volume,...)

### **3.1 Truy cập IAM Console**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.

### **3.2 Tạo Tài khoản Người dùng IAM mới**

1. Nhấp vào "Create user" trong menu bên trái.
2. Nhấp vào "Create a user account."
3. Nhập chi tiết tài khoản người dùng, bao gồm tên người dùng và mật khẩu.
4. Xem lại các thiết lập và nhấp vào "Create user account" ở góc trên bên phải.

### **3.3 Truy cập Cổng thông tin DRC với Tài khoản Người dùng IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL trang web DRC tại đây:&#x20;
2. Hãy nhớ đăng xuất khỏi tài khoản Người dùng Gốc và Đăng nhập với Tài khoản Người dùng IAM đã tạo ở bước 2.
3. Sau khi đăng nhập, bạn sẽ thấy tổng quan về trang web DRC nhưng sẽ không có quyền thao tác với bất kỳ tính năng nào.&#x20;

**Lưu ý:**

* **Tài khoản Người dùng IAM** đã được tạo ở bước 3.2 hiện không có quyền thực hiện các hành động trên dịch vụ DRC.
* Để cấp quyền cho Tài khoản Người dùng IAM trên, hãy tham khảo hướng dẫn ở **Bước 3.4 dưới đây**. Lưu ý rằng hướng dẫn này cung cấp một ví dụ về **DRFullAccess và vServerFullAccess.**

### **3.4 Gán Quyền cho Tài khoản IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản **Người dùng Gốc (Root User)**. Bạn có thể cần cung cấp tên người dùng và mật khẩu hoặc sử dụng các phương thức xác thực khác như đăng nhập duy nhất (SSO) nếu đã được cấu hình.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.
4. Nhấp vào **"User account"** trong menu bên trái.
5. Tìm kiếm tài khoản người dùng IAM bằng cách nhập tên người dùng vào ô tìm kiếm.
6. Nhấp vào dòng chứa thông tin tài khoản người dùng IAM trong kết quả tìm kiếm.
7. Theo mặc định, bạn sẽ thấy tab "**Permission**" tại trang thông tin chi tiết của tài khoản người dùng IAM.
8. Nhấp vào nút "**Attach policies**" và sau đó bạn sẽ thấy một hộp thoại xuất hiện chứa tất cả các Chính sách.
9. Tìm kiếm **chính sách DRFullAccess** và **vServerFullAccess** bằng cách nhập tên chính xác của nó vào ô tìm kiếm.
10. Tick vào kết quả tìm được và nhấp vào nút **"Attach"** ở góc dưới bên phải của hộp thoại.

**5. Truy cập lại Cổng thông tin vServer với Tài khoản Người dùng IAM**

Truy cập lại Cổng thông tin DRC bằng cách làm theo hướng dẫn ở Bước 3.3, sau đó bạn có thể truy cập vào tất cả các tính năng trên DRC sau khi gán chính sách DRFullAccess và vServerFullAccess cho tài khoản người dùng IAM.
