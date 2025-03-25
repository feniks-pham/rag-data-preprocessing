# IAM cho vServer

IAM là yếu tố cần thiết để bảo vệ tài nguyên trong các dịch vụ của vServer. Nếu thiếu kiểm soát truy cập đúng đắn, người dùng trái phép có thể truy cập vào dữ liệu nhạy cảm hoặc làm gián đoạn các hoạt động quan trọng. IAM giúp thực thi nguyên tắc đặc quyền tối thiểu, giảm thiểu các bề mặt tấn công tiềm năng và bảo vệ các tài nguyên máy chủ của bạn khỏi việc truy cập trái phép và xâm nhập dữ liệu.

### **1. Bắt đầu sử dụng IAM** <a href="#iamforvserver-1.batdausudungiam" id="iamforvserver-1.batdausudungiam"></a>

Hướng dẫn này nhằm hướng dẫn người dùng có thể nhanh chóng bắt đầu sử dụng IAM trong các dịch vụ vServer bằng cách sử dụng quyền mặc định **(được định nghĩa bởi VNG Cloud Managed Policies)** cho hệ thống vServer gọi là **vServerFullAccess.**

**1. Truy cập IAM Console**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.

**2. Tạo Tài khoản Người dùng IAM mới**

1. Nhấp vào "Create user" trong menu bên trái.
2. Nhấp vào "Create a user account."
3. Nhập chi tiết tài khoản người dùng, bao gồm tên người dùng và mật khẩu.
4. Xem lại các thiết lập và nhấp vào "Create user account" ở góc trên bên phải.

**3. Truy cập Cổng thông tin vServer với Tài khoản Người dùng IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL trang web vServer: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
2. Hãy nhớ đăng xuất khỏi tài khoản Người dùng Gốc và Đăng nhập với Tài khoản Người dùng IAM đã tạo ở bước 2.
3. Sau khi đăng nhập, bạn sẽ thấy tổng quan về trang web vServer.
4. Thử truy cập vào các trang Network, Server, Bock store, Load balancer, Container & Billing, bạn sẽ thấy thông báo về quyền bị giới hạn như dưới đây.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806584/image2023-7-24_17-9-44.png?version=1&#x26;modificationDate=1690193385000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Notice

* **Tài khoản Người dùng IAM** đã được tạo ở bước 2 hiện không có quyền thực hiện các hành động trên dịch vụ đám mây vServer.
* Để cấp quyền cho Tài khoản Người dùng IAM trên, hãy tham khảo hướng dẫn ở **Bước 4 dưới đây**. Lưu ý rằng hướng dẫn này cung cấp một ví dụ về **vServerFullAccess.**

**4. Gán Quyền cho Tài khoản IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản **Người dùng Gốc (Root User)**. Bạn có thể cần cung cấp tên người dùng và mật khẩu hoặc sử dụng các phương thức xác thực khác như đăng nhập duy nhất (SSO) nếu đã được cấu hình.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.
4. Nhấp vào **"User account"** trong menu bên trái.
5. Tìm kiếm tài khoản người dùng IAM bằng cách nhập tên người dùng vào ô tìm kiếm.
6. Nhấp vào dòng chứa thông tin tài khoản người dùng IAM trong kết quả tìm kiếm.
7. Theo mặc định, bạn sẽ thấy tab "**Permission**" tại trang thông tin chi tiết của tài khoản người dùng IAM.
8. Nhấp vào nút "**Attach policies**" và sau đó bạn sẽ thấy một hộp thoại xuất hiện chứa tất cả các Chính sách.
9. Tìm kiếm **chính sách vServerFullAccess** bằng cách nhập tên chính xác của nó vào ô tìm kiếm.
10. Tick vào kết quả tìm được và nhấp vào nút **"Attach"** ở góc dưới bên phải của hộp thoại.

**5. Truy cập lại Cổng thông tin vServer với Tài khoản Người dùng IAM**

Truy cập lại Cổng thông tin vServer bằng cách làm theo hướng dẫn ở Bước 3, sau đó bạn có thể truy cập vào tất cả các phần trong Cổng thông tin vServer sau khi gán chính sách vServerFullAccess cho tài khoản người dùng IAM.

### **2. Danh sách VNG Managed Policies** <a href="#iamforvserver-2.danhsachvngmanagedpolicies" id="iamforvserver-2.danhsachvngmanagedpolicies"></a>

VNG Managed Policy là các Chính Sách IAM (IAM Policy) được tạo mặc định bởi hệ thống IAM VNG Cloud. Các Chính Sách này được quản lý bởi chính VNG Cloud nhằm mục đích hỗ trợ người dùng trong việc cài đặt nhanh chóng các quyền truy cập cần thiết cho các tài khoản người dùng IAM đối với các tài nguyên của từng Product cụ thể. Cùng tìm hiểu danh sách VNG Managed Policies cho vServer:

* [vServerFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/ef38ac9e-ae09-4953-8b55-b28687b2cc79): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc hệ thông vServer
* [vServerReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/b63dd647-347f-47a2-9a21-4003bcef7bac): Chỉ bao gồm quyền Đọc (Read) trên các tài nguyên thuộc hệ thống vServer
* [vLBFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/5dbe289b-4fc0-46ad-9f18-47064a0faae0): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc dịch vụ Load Balancer
* [vLBReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/f3486bbe-81a2-480b-99c4-9980728e86df): Chỉ bao gồm quyền Đọc (Read) trên các tài nguyên thuộc dịch vụ Load Balancer

### **3. Khám phá chi tiết cách sử dụng IAM cho vServer** <a href="#iamforvserver-3.khamphachitietcachsudungiamchovserver" id="iamforvserver-3.khamphachitietcachsudungiamchovserver"></a>

* Tìm hiểu thêm về IAM cho vServer: [Quản lý định danh và truy cập (IAM) cho vServer](../../vserver/compute-hcm03-1a/quan-ly-dinh-danh-va-truy-cap-iam-cho-vserver/)
* Tìm hiểu thêm về IAM:
  * [IAM Identity](../quan-ly-truy-cap-iam/)
  * [Các trường hợp sử dụng thông thường của IAM](../ung-dung-pho-bien/)
