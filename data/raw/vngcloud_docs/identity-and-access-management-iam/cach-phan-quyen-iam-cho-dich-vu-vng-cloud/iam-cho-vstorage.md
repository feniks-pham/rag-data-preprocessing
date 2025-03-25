# IAM cho vStorage

IAM là yếu tố cần thiết để bảo vệ tài nguyên trong các dịch vụ của vStorage. Nếu thiếu kiểm soát truy cập đúng đắn, người dùng trái phép có thể truy cập vào dữ liệu nhạy cảm hoặc làm gián đoạn các hoạt động quan trọng. IAM giúp thực thi nguyên tắc đặc quyền tối thiểu, giảm thiểu các bề mặt tấn công tiềm năng và bảo vệ các tài nguyên máy chủ của bạn khỏi việc truy cập trái phép và xâm nhập dữ liệu.

### **1. Bắt đầu sử dụng IAM** <a href="#iamforvstorage-1.batdausudungiam" id="iamforvstorage-1.batdausudungiam"></a>

Hướng dẫn này nhằm hướng dẫn người dùng có thể nhanh chóng bắt đầu sử dụng IAM trong các dịch vụ vStorage bằng cách sử dụng quyền mặc định **(được định nghĩa bởi VNG Cloud Managed Policies)** cho hệ thống vStorage gọi là **vStorageFullAccess.**

**1. Truy cập IAM Console**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.

**2. Tạo Tài khoản Người dùng IAM mới**

1. Nhấp vào "Create user" trong menu bên trái.
2. Nhấp vào "Create a user account."
3. Nhập chi tiết tài khoản người dùng, bao gồm tên người dùng và mật khẩu.
4. Xem lại các thiết lập và nhấp vào "Create user account" ở góc trên bên phải.

**3. Truy cập Cổng thông tin vStorage với Tài khoản Người dùng IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL trang web vStorage: [https://vstorage.console.vngcloud.vn/overview](https://vstorage.console.vngcloud.vn/overview)
2. Hãy nhớ đăng xuất khỏi tài khoản Người dùng Gốc và Đăng nhập với Tài khoản Người dùng IAM đã tạo ở bước 2.
3. Sau khi đăng nhập, bạn sẽ thấy tổng quan về trang web vStorage.
4. Thử truy cập vào các trang Storage, Report và Integration bạn sẽ thấy thông báo về quyền bị giới hạn như dưới đây.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806586/image2023-8-1_16-51-34.png?version=1&#x26;modificationDate=1690883495000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Lưu ý

* **Tài khoản Người dùng IAM** đã được tạo ở bước 2 hiện không có quyền thực hiện các hành động trên dịch vụ đám mây vStorage.
* Để cấp quyền cho Tài khoản Người dùng IAM trên, hãy tham khảo hướng dẫn ở **Bước 4 dưới đây**. Lưu ý rằng hướng dẫn này cung cấp một ví dụ về **vStorageFullAccess.**

**4. Gán Quyền cho Tài khoản IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản **Người dùng Gốc (Root User)**. Bạn có thể cần cung cấp tên người dùng và mật khẩu hoặc sử dụng các phương thức xác thực khác như đăng nhập duy nhất (SSO) nếu đã được cấu hình.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.
4. Nhấp vào **"User account"** trong menu bên trái.
5. Tìm kiếm tài khoản người dùng IAM bằng cách nhập tên người dùng vào ô tìm kiếm.
6. Nhấp vào dòng chứa thông tin tài khoản người dùng IAM trong kết quả tìm kiếm.
7. Theo mặc định, bạn sẽ thấy tab "**Permission**" tại trang thông tin chi tiết của tài khoản người dùng IAM.
8. Nhấp vào nút "**Attach policies**" và sau đó bạn sẽ thấy một hộp thoại xuất hiện chứa tất cả các Chính sách.
9. Tìm kiếm **chính sách vStorageFullAccess** bằng cách nhập tên chính xác của nó vào ô tìm kiếm.
10. Tick vào kết quả tìm được và nhấp vào nút **"Attach"** ở góc dưới bên phải của hộp thoại.

**5. Truy cập lại Cổng thông tin vStorage với Tài khoản Người dùng IAM**

Truy cập lại Cổng thông tin vStorage bằng cách làm theo hướng dẫn ở **Bước 3**, sau đó bạn có thể truy cập vào tất cả các phần trong Cổng thông tin vStorage sau khi gán chính sách **vStorageFullAccess** cho tài khoản người dùng IAM.

### **2. Danh sách VNG Managed Policies** <a href="#iamforvstorage-2.danhsachvngmanagedpolicies" id="iamforvstorage-2.danhsachvngmanagedpolicies"></a>

VNG Managed Policy là các Chính Sách IAM (IAM Policy) được tạo mặc định bởi hệ thống IAM VNG Cloud. Các Chính Sách này được quản lý bởi chính VNG Cloud nhằm mục đích hỗ trợ người dùng trong việc cài đặt nhanh chóng các quyền truy cập cần thiết cho các tài khoản người dùng IAM đối với các tài nguyên của từng Product cụ thể. Cùng tìm hiểu danh sách VNG Managed Policies cho vStorage:

* [vStorageAPIFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/d882a78f-c08b-4e33-991d-3b276723335c): Bao gồm toàn bộ quyền truy cập đến các tài nguyên thuộc hệ thống vStorage thông qua publi API
* [vStorageIAMUserFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/9d4e2ff8-3920-44df-a81d-058e19120161): Bao gồm toàn bộ quyền truy cập đến hệ thống IAM của vStorage.
* [vStorageAPIReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/3e1ee27d-f8bd-401a-8ab2-03a3d1fdf71e): Chỉ bao gồm quyền Đọc (Read) đến các tài nguyên thuộc hệ thống vStorage thông qua publi API
* [vStorageFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/6085cebd-17bf-4df6-b6d2-bb7c7769f1a0): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc hệ thông vStorage
* [vStorageClientToolReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/000ef518-534e-4c39-890d-19d2f1a6ae9e): Chỉ bao gồm quyền Đọc (Read) đến các tài nguyên thuộc hệ thống vStorage từ các Client Tool
* [vStorageReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/17b31005-2760-4f6c-ac73-5953ec52ddfa): Chỉ bao gồm quyền Đọc (Read) trên các tài nguyên thuộc hệ thống vStorage
* [vStorageClientToolFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/b8500577-1e38-45ee-8049-0c1bef0f4e8b): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc hệ thông vStorage từ các Client Tool
* [vStorageIAMUserReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/1617a48f-7c0a-4292-bab2-f341799ab309): Chỉ bao gồm quyền Đọc (Read) đến hệ thống IAM của vStorage.
* [vStorageNormalAccess](https://hcm-3.console.vngcloud.vn/iam/policies/0f5fe828-ab47-441d-a167-398b6d7a3577): Bao gồm toàn bộ quyền truy cập đến các tài nguyên thuộc hệ thống vStorage (ngoại trừ các hành động liên quan đến vStorage - Billing system)

### **3. Khám phá chi tiết cách sử dụng IAM cho vStorage** <a href="#iamforvstorage-3.khamphachitietcachsudungiamchovstorage" id="iamforvstorage-3.khamphachitietcachsudungiamchovstorage"></a>

* Tìm hiểu thêm về IAM cho vStorage: [Quản lý định danh và truy cập (IAM) cho vStorage](https://docs.vngcloud.vn/vng-cloud-document/v/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap)

Tìm hiểu thêm về IAM:

* [IAM Identity](../quan-ly-truy-cap-iam/)
* [Các trường hợp sử dụng thông thường của IAM](../ung-dung-pho-bien/)
