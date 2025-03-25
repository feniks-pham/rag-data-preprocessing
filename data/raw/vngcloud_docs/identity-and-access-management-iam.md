# Identity and Access Management (IAM)

##

{% embed url="https://youtu.be/BvrxB9ZK2T0?si=318ook64-hYEhPCi" %}
Hướng dẫn phân quyền IAM và tích hợp S3 Browser cho vStorage
{% endembed %}

#### **1. IAM là gì?** <a href="#identityandaccessmanagement-iam-1.iamlagi" id="identityandaccessmanagement-iam-1.iamlagi"></a>

Quản lý Nhận dạng và Truy cập (Identity and Access Management - IAM) là một công cụ bảo mật quan trọng trong cloud computing, tập trung vào việc quản lý và kiểm soát quyền truy cập đến các tài nguyên khác nhau trong môi trường điện toán đám mây. Nó đảm bảo rằng những cá nhân hoặc dịch vụ sẽ có các quyền thích hợp để truy cập vào các tài nguyên cụ thể, đồng thời bảo vệ chống lại việc truy cập trái phép.

IAM chịu trách nhiệm xác thực người dùng, cấp quyền truy cập vào các tài nguyên của họ và duy trì một trung tâm lưu trữ cho các nhận dạng của người dùng và các quyền liên quan. Nó đóng vai trò quan trọng trong việc thực thi nguyên tắc đặc quyền tối thiểu, trong đó người dùng chỉ được cấp quyền tối thiểu cần thiết để thực hiện các nhiệm vụ của họ, từ đó giảm thiểu rủi ro của việc truy cập trái phép và vi phạm dữ liệu.

#### **2. Tầm quan trọng của IAM trong Dịch vụ Đám mây** <a href="#identityandaccessmanagement-iam-2.tamquantrongcuaiamtrongdichvudammay" id="identityandaccessmanagement-iam-2.tamquantrongcuaiamtrongdichvudammay"></a>

IAM là nền tảng cơ bản cho bảo mật và tuân thủ trong các dịch vụ đám mây. Trong đám mây, tài nguyên thường được truy cập từ bất kỳ đâu và các biện pháp bảo mật dựa vào các ranh giới truy cập truyền thống không đủ. IAM giải quyết những thách thức này bằng cách cung cấp kiểm soát chi tiết đối với quyền truy cập đến các tài nguyên đám mây, bất kể vị trí của chúng hoặc các thiết bị được sử dụng để truy cập chúng.

Bằng việc triển khai IAM, các tổ chức / doanh nghiệp có thể đạt được những lợi ích sau:

1. Tăng cường Bảo mật: IAM thực thi các cơ chế xác thực mạnh mẽ và các chính sách cho phép, giảm thiểu rủi ro truy cập trái phép và vi phạm dữ liệu.
2. Tuân thủ và Quản trị: IAM cho phép tổ chức tuân thủ các yêu cầu pháp lý bằng cách kiểm soát quyền truy cập đến dữ liệu nhạy cảm và ghi lại các yêu cầu truy cập.
3. Quản lý Người dùng Đơn giản: IAM tập trung quản lý người dùng, làm cho việc thêm, xóa hoặc thay đổi quyền truy cập của người dùng trên toàn hạ tầng đám mây trở nên dễ dàng.
4. Quyền truy cập và Đăng nhập duy nhất (SSO): IAM cho phép tích hợp nhà cung cấp nhận dạng bên ngoài, cho phép đăng nhập duy nhất (SSO) cho người dùng và giảm thiểu sự cần thiết của nhiều chứng thực.

#### **3. Các mục tiêu chính của IAM trong VNG Cloud** <a href="#identityandaccessmanagement-iam-3.cacmuctieuchinhcuaiamtrongvngcloud" id="identityandaccessmanagement-iam-3.cacmuctieuchinhcuaiamtrongvngcloud"></a>

IAM là một thành phần quan trọng của kiến trúc bảo mật VNG Cloud, tăng cường bảo mật và đảm bảo tuân thủ các quy định khác nhau. Dưới đây là cách IAM đạt được những mục tiêu này:

1. Xác thực An toàn: IAM thực thi các cơ chế xác thực mạnh mẽ, đảm bảo chỉ những người dùng được ủy quyền mới có thể truy cập vào các tài nguyên đám mây.
2. Kiểm soát Ủy quyền: IAM cung cấp kiểm soát chi tiết đối với quyền truy cập thông qua vai trò và chính sách, giảm thiểu rủi ro truy cập trái phép.
3. Nguyên tắc đặc quyền tối thiểu: IAM tuân thủ nguyên tắc đặc quyền tối thiểu, chỉ cấp quyền tối thiểu cần thiết cho người dùng thực hiện nhiệm vụ của họ.
4. Quản lý tập trung Người dùng: IAM tập trung quản lý người dùng và nhóm, đơn giản hóa việc quản lý quyền truy cập.
5. Auditing and Logging: IAM ghi lại các yêu cầu quản trị và truy cập trên tài nguyên, cho phép audit và giám sát toàn diện.
6. Hỗ trợ Tuân thủ: IAM giúp đáp ứng các yêu cầu tuân thủ bằng cách cung cấp kiểm soát truy cập chi tiết và ghi nhật ký truy cập.

#### **4. Các tính năng chính của IAM trong VNG Cloud** <a href="#identityandaccessmanagement-iam-4.cactinhnangchinhcuaiamtrongvngcloud" id="identityandaccessmanagement-iam-4.cactinhnangchinhcuaiamtrongvngcloud"></a>

VNG Cloud cung cấp một giải pháp IAM mạnh mẽ, cho phép bạn quản lý quyền truy cập vào các tài nguyên đám mây một cách an toàn. Một số tính năng IAM chính trong VNG Cloud bao gồm:

1. Quản lý Người dùng và Nhóm: Tạo và quản lý người dùng IAM và nhóm để kiểm soát quyền truy cập vào tài nguyên dựa trên các vai trò hoặc trách nhiệm.
2. Quản lý Truy cập: Xác định và gắn các chính sách để kiểm soát quyền được cấp cho người dùng, nhóm hoặc các tài khoản dịch vụ.
3. Tùy chỉnh IAM Policies: Viết các chính sách IAM tùy chỉnh để cấp quyền kiểm soát truy cập chi tiết đối với các tài nguyên.
4. Identity Provider: Tích hợp VNG Cloud với các nhà cung cấp nhận dạng bên ngoài để đơn giản hóa đăng nhập duy nhất (SSO) và quản lý người dùng.

#### 5. Khái niệm và Thuật ngữ của IAM <a href="#identityandaccessmanagement-iam-5.khainiemvathuatngucuaiam" id="identityandaccessmanagement-iam-5.khainiemvathuatngucuaiam"></a>

* **Root User Account**

Root User Account là một thực thể bạn tạo đầu tiên trong VNG Cloud và sử dụng, mặc định có quyền truy cập đầy đủ vào tất cả các sản phẩm/dịch vụ và tài nguyên của VNG Cloud trong tài khoản đó.

* #### **Users Accounts** <a href="#identityandaccessmanagement-iam-usersaccounts" id="identityandaccessmanagement-iam-usersaccounts"></a>

IAM User Account đại diện cho các danh tính riêng lẻ liên kết với Root User Account của bạn. Một IAM User Account bao gồm các chứng chỉ bảo mật, chẳng hạn như tên người dùng và mật khẩu, để xác thực danh tính của nó.

* **Groups**

IAM User Group là nhóm các người dùng chia sẻ các yêu cầu truy cập tương tự. Việc nhóm hóa các User Account giúp đơn giản hóa quản lý quyền bằng cách cấp quyền cho một Group thay vì từng người dùng riêng lẻ.

* **Policies**

IAM Policies là các tài liệu JSON xác định các quyền và quy tắc truy cập tài nguyên. Các Policies này được gắn kèm với IAM User Account, User Group và Service Account để kiểm soát hành động mà họ có thể thực hiện trên các tài nguyên cụ thể. IAM Policies tuân thủ nguyên tắc "cho phép" hoặc "từ chối", tức là chúng rõ ràng cấp quyền hoặc từ chối truy cập tài nguyên và hành động.

* **Service Accounts**

Service Account là một danh tính bạn có thể tạo trong tài khoản của bạn có các quyền cụ thể. Một Service Account có một số điểm tương đồng với IAM User Account. Service Account và IAM User Account đều là những danh tính với các chính sách cho phép xác định những việc danh tính có thể và không thể làm với các tài nguyên của VNG Cloud. Tuy nhiên, Service Acocunt là danh tính được sử dụng bởi một ứng dụng hoặc máy móc, chứ không phải là một cá nhân, để thực hiện các cuộc gọi API được ủy quyền và truy cập vào các tài nguyên cụ thể.

* **Identity Provider**

Identity Provier cho phép bạn tích hợp nhà cung cấp nhận dạng bên ngoài với VNG Cloud Services, cho phép người dùng truy cập tài nguyên đám mây bằng các thông tin đăng nhập hiện có từ nhà cung cấp nhận dạng bên ngoài. Điều này loại bỏ việc người dùng phải nhớ nhiều bộ thông tin đăng nhập cho các hệ thống khác nhau và đơn giản hóa quản lý quyền truy cập.

Trong VNG Cloud, bạn có thể cài đặt Identity Provider bằng cách cấu hình cài đặt kết nối giữa Identity Provider bên ngoài với VNG Cloud. Khi đã cài đặt, người dùng từ nhà cung cấp nhận dạng bên ngoài có thể đăng nhập bằng các thông tin đăng nhập hiện có để truy cập vào tài nguyên trong VNG Cloud.\


Dưới đây là các topic quan trọng mà người dùng cần tìm hiểu thêm về IAM VNG Cloud\


* [How to Login into VNG Cloud](identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md)
* [Get Started with IAM](identity-and-access-management-iam/bat-dau-voi-iam.md)
* [Examples of Common Use Cases](identity-and-access-management-iam/ung-dung-pho-bien/)
* [How IAM supports VNG Cloud Services](identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/)
* [IAM Identities](identity-and-access-management-iam/cac-loai-dinh-danh-iam/)
* [IAM Access Management](identity-and-access-management-iam/quan-ly-truy-cap-iam/)
* [Audit Logs](identity-and-access-management-iam/quan-ly-audit-logs.md)
* [Quota & Limitation](identity-and-access-management-iam/gioi-han-su-dung.md)

