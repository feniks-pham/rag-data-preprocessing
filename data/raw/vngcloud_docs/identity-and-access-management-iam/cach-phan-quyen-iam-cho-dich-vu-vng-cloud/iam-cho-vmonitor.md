# IAM for vMonitor

IAM là yếu tố cần thiết để bảo vệ tài nguyên trong các dịch vụ của vMonitor. Nếu thiếu kiểm soát truy cập đúng đắn, người dùng trái phép có thể truy cập vào dữ liệu nhạy cảm hoặc làm gián đoạn các hoạt động quan trọng. IAM giúp thực thi nguyên tắc đặc quyền tối thiểu, giảm thiểu các bề mặt tấn công tiềm năng và bảo vệ các tài nguyên máy chủ của bạn khỏi việc truy cập trái phép và xâm nhập dữ liệu.

### **1. Bắt đầu sử dụng IAM** <a href="#iamforvmonitor-1.batdausudungiam" id="iamforvmonitor-1.batdausudungiam"></a>

Hướng dẫn này nhằm hướng dẫn người dùng có thể nhanh chóng bắt đầu sử dụng IAM trong các dịch vụ vMonitor bằng cách sử dụng quyền mặc định **(được định nghĩa bởi VNG Cloud Managed Policies)** cho hệ thống vMonitor gọi là **vMonitorFullAccess.**

**1. Truy cập IAM Console**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.

**2. Tạo Tài khoản Người dùng IAM mới**

1. Nhấp vào "Create user" trong menu bên trái.
2. Nhấp vào "Create a user account."
3. Nhập chi tiết tài khoản người dùng, bao gồm tên người dùng và mật khẩu.
4. Xem lại các thiết lập và nhấp vào "Create user account" ở góc trên bên phải.

**3. Truy cập Cổng thông tin vMonitor với Tài khoản Người dùng IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL trang web vMonitor: [https://hcm-3.console.vngcloud.vn/vmonitor/](https://hcm-3.console.vngcloud.vn/vmonitor/)
2. Hãy nhớ đăng xuất khỏi tài khoản Người dùng Gốc và Đăng nhập với Tài khoản Người dùng IAM đã tạo ở bước 2.
3. Sau khi đăng nhập, bạn sẽ thấy tổng quan về trang web vMonitor.
4. Thử truy cập vào các trang Quota & Usage, Dashboard, Notification, Alarm, Infrastructure list, Metri, Log và Synthetic test bạn sẽ thấy thông báo về quyền bị giới hạn như dưới đây.

![](https://docs.vngcloud.vn/download/attachments/59806588/image2023-8-1\_16-51-34.png?version=1\&modificationDate=1690883873000\&api=v2)

Lưu ý

* **Tài khoản Người dùng IAM** đã được tạo ở bước 2 hiện không có quyền thực hiện các hành động trên dịch vụ đám mây vStorage.
* Để cấp quyền cho Tài khoản Người dùng IAM trên, hãy tham khảo hướng dẫn ở **Bước 4 dưới đây**. Lưu ý rằng hướng dẫn này cung cấp một ví dụ về **vMonitorFullAccess.**

**4. Gán Quyền cho Tài khoản IAM**

1. Mở trình duyệt web của bạn và truy cập vào URL IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Đăng nhập với tư cách là tài khoản **Người dùng Gốc (Root User)**. Bạn có thể cần cung cấp tên người dùng và mật khẩu hoặc sử dụng các phương thức xác thực khác như đăng nhập duy nhất (SSO) nếu đã được cấu hình.
3. Sau khi đăng nhập, bạn sẽ thấy giao diện IAM Console, nơi cung cấp tổng quan về cấu hình IAM của bạn.
4. Nhấp vào **"User account"** trong menu bên trái.
5. Tìm kiếm tài khoản người dùng IAM bằng cách nhập tên người dùng vào ô tìm kiếm.
6. Nhấp vào dòng chứa thông tin tài khoản người dùng IAM trong kết quả tìm kiếm.
7. Theo mặc định, bạn sẽ thấy tab "**Permission**" tại trang thông tin chi tiết của tài khoản người dùng IAM.
8. Nhấp vào nút "**Attach policies**" và sau đó bạn sẽ thấy một hộp thoại xuất hiện chứa tất cả các Chính sách.
9. Tìm kiếm **chính sách vMonitorFullAccess** bằng cách nhập tên chính xác của nó vào ô tìm kiếm.
10. Tick vào kết quả tìm được và nhấp vào nút **"Attach"** ở góc dưới bên phải của hộp thoại.

**5. Truy cập lại Cổng thông tin vMonitor với Tài khoản Người dùng IAM**

Truy cập lại Cổng thông tin vMonitor bằng cách làm theo hướng dẫn ở **Bước 3**, sau đó bạn có thể truy cập vào tất cả các phần trong Cổng thông tin vMonitor sau khi gán chính sách **vMonitorFullAccess** cho tài khoản người dùng IAM.

### **2. Danh sách VNG Managed Policies** <a href="#iamforvmonitor-2.danhsachvngmanagedpolicies" id="iamforvmonitor-2.danhsachvngmanagedpolicies"></a>

VNG Managed Policy là các Chính Sách IAM (IAM Policy) được tạo mặc định bởi hệ thống IAM VNG Cloud. Các Chính Sách này được quản lý bởi chính VNG Cloud nhằm mục đích hỗ trợ người dùng trong việc cài đặt nhanh chóng các quyền truy cập cần thiết cho các tài khoản người dùng IAM đối với các tài nguyên của từng Product cụ thể. Cùng tìm hiểu danh sách VNG Managed Policies cho vMonitor:

* [vMonitorFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/5e892948-7052-4042-b69b-e584c87948df): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc hệ thông vMonitor
* [vMonitorMetricPush](https://hcm-3.console.vngcloud.vn/iam/policies/4679ef00-d815-11ed-afa1-0242ac120002): Chỉ bao gồm các quyền liên quan đến việc Push Metric
* [vMonitorMetricNormalAccess](https://hcm-3.console.vngcloud.vn/iam/policies/70397a23-9632-4816-a2dd-aedaede4cafc): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc loại Metric (ngoại trừ các action lên quan đến Billing)
* [vMonitorMetricReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/9e4c030a-660e-4c55-b5f9-9626892f403a): Chỉ bao gồm quyền Đọc (Read) đến các tài nguyen Metric.
* [vMonitorMetricFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/008dbe64-27b6-438b-a7cd-092cf1e1498d): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc loại Metric
* [vMonitorSyntheticReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/7af1a187-9f58-4e3d-9fa3-db3380ecffbb): Chỉ bao gồm quyền Đọc (Read) đến các tài nguyen Synthetic.
* [vMonitorSyntheticNormalAccess](https://hcm-3.console.vngcloud.vn/iam/policies/2d844b3a-467f-4216-9f77-2270467fd710): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc loại Synthetic (ngoại trừ các action lên quan đến Billing)
* [vMonitorSyntheticFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/a0b85faa-8cff-481a-b549-1e7d5a5a085c): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc loại Synthetic
* [vMonitorNotificationReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/8e42191e-b8ad-4d2e-a38e-410db9ca00c5): Chỉ bao gồm quyền Đọc (Read) đến các tài nguyen Notification.
* [vMonitorNotificationFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/a80df946-8d72-4ce2-aa83-d4288cbbf5b9): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc loại Notification
* [vMonitorLogNormalAccess](https://hcm-3.console.vngcloud.vn/iam/policies/bb6325b2-14cf-456c-996a-2388d6f6289b): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc loại Log (ngoại trừ các action lên quan đến Billing)
* [vMonitorLogReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/d2ae3ffd-b607-4d05-b247-9b300206f4c2): Chỉ bao gồm quyền Đọc (Read) đến các tài nguyen Log.
* [vMonitorLogFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/9ea5e2fe-6e44-4bb7-8b7a-6a42d6f614f1): Bao gồm toàn quyền truy cập đến các tài nguyên thuộc loại Log
* [vMonitorBillingFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/9218604f-2a14-4d30-86b8-fde0d6a1630a): Bao gồm toàn quyền truy cập đến trang vMonitor - Billing
* [MonitorDashboardReadOnlyAccess](https://hcm-3.console.vngcloud.vn/iam/policies/7246921b-f0c3-4fee-8a00-341d8785800a): Chỉ bao gồm quyền Đọc (Read) đến trang vMonitor - Dashboard.
* [vMonitorDashboardFullAccess](https://hcm-3.console.vngcloud.vn/iam/policies/e5ce8dc3-4d25-4a0c-8af9-50e939f13759): Bao gồm toàn quyền truy cập đến trang vMonitor - Dashboard

### **3. Khám phá chi tiết cách sử dụng IAM cho vMonitor Platform** <a href="#iamforvmonitor-3.khamphachitietcachsudungiamchovmonitorplatform" id="iamforvmonitor-3.khamphachitietcachsudungiamchovmonitorplatform"></a>

* Tìm hiểu thêm về IAM:
  * IAM Identity: [IAM Identities](https://docs.vngcloud.vn/display/ONVINA/IAM+Identities)
  * Quản lý Truy cập IAM: [IAM Access Management](https://docs.vngcloud.vn/display/ONVINA/IAM+Access+Management)
  * Các trường hợp sử dụng thông thường của IAM: [Example of Common Use Cases](https://docs.vngcloud.vn/display/ONVINA/Example+of+Common+Use+Cases)

\
