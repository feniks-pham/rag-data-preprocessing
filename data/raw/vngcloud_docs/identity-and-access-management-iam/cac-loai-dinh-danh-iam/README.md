# Các loại Định danh IAM

IAM Identities (Định danh IAM) là các thực thể trong hệ thống Quản lý Định danh và Truy cập (IAM) đại diện cho cácIAM User Account, User Group và Service Account. IAM Identities được sử dụng để quản lý quyền truy cập đến tài nguyên và dịch vụ trong môi trường đám mây một cách an toàn. Mỗi IAM Identity có một bộ thông tin đăng nhập duy nhất và các quyền liên kết liên quan xác định các hành động mà chúng có thể thực hiện trên các tài nguyên cụ thể.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806590/Identities-Page-1.drawio%20(1).png?version=1&#x26;modificationDate=1691474663000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

#### Root User Account <a href="#iamidentities-rootuseraccount" id="iamidentities-rootuseraccount"></a>

Root User Account là một thực thể bạn tạo đầu tiên trong VNG Cloud và sử dụng, mặc định có quyền truy cập đầy đủ vào tất cả các sản phẩm/dịch vụ và tài nguyên của VNG Cloud trong tài khoản đó.

#### User Account <a href="#iamidentities-useraccount" id="iamidentities-useraccount"></a>

IAM User Account là một thực thể đại diện cho người dùng tương tác với VNG Cloud trên giao diện Portal. Một IAM User Account trong VNG Cloud bao gồm thông tin đăng nhập (tên người dùng, mật khẩu) và mặc định bị từ chối quyền truy cập. IAM User Account không phải là các tài khoản riêng biệt; chúng là người dùng trong cùng một Root User Account và không cần phải có phương thức thanh toán được đăng ký với VNG Cloud. Mọi hoạt động được thực hiện bởi các IAM User Account trong tài khoản Root User sẽ được tính phí cho tài khoản Root User đó.

Nếu bạn có nhân viên cần truy cập vào VNG Cloud, không nên chia sẻ thông tin đăng nhập tài khoản Root User với họ. Thay vào đó, hãy tạo các IAM User Account riêng lẻ trong tài khoản Root User và cấp quyền khác nhau cho từng IAM User Account đó. Tìm hiểu thêm hướng dẫn chi tiết tại:

* [Quản lý User Account](tai-khoan-user-accounts/).

#### User Group <a href="#iamidentities-usergroup" id="iamidentities-usergroup"></a>

IAM User Group là một tập hợp các IAM User Account. IAM User Group giúp đơn giản hóa việc quản lý quyền bằng cách cho phép bạn cấp, thay đổi và loại bỏ quyền truy cập cho nhiều User Account cùng một lúc. Ví dụ, bạn có thể tạo một User Group có tên "Admins" và gán cho Group đó các quyền quản trị. Bất kỳ IAM User Account nào trong Group đều tự động có các quyền được gán cho Group đó. tìm hiểu thêm hướng dẫn chi tiết tại:

* [Quản lý User Group](tai-khoan-user-groups.md)

#### Service Account <a href="#iamidentities-serviceaccount" id="iamidentities-serviceaccount"></a>

Service Account là một danh tính bạn có thể tạo trong tài khoản Root User của mình với các quyền cụ thể. Service Account có một số điểm tương đồng với IAM User Account. Cả Server Account và User Account đều là các danh tính với các chính sách quyền xác định những gì danh tính đó có thể và không thể làm với các tài nguyên của VNG Cloud. Tuy nhiên, Service Account là các danh tính được ứng dụng hoặc máy tính sử dụng, không phải là người, để thực hiện các cuộc gọi API được ủy quyền và truy cập vào các tài nguyên cụ thể. Tìm hiểu thêm hướng dẫn chi tiết tại:

* [Quản lý Service Account](../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md)

#### vStorage credentials <a href="#iamidentities-vstoragecredentials" id="iamidentities-vstoragecredentials"></a>

**vStorage credentials là tính năng hỗ trợ riêng cho sản phẩm/dịch vụ vStorage. vStorage credentials bao gồm các cặp khóa cho phép bạn tạo và cấp quyền truy cập vào các tài nguyên của vStorage. Có hai loại chính của vStorage credentials:**

1. S3 Key: Khóa S3 bao gồm một khóa truy cập và khóa bí mật tích hợp với vStorage để đảm bảo tích hợp với các Client tools S3 như s3cmd và S3 SDK.
2. Swift User: Bao gồm thông tin về người dùng/mật khẩu và là phương pháp xác thực chính được hỗ trợ bởi vStorage.

**Quyền truy cập của vStorage credentials**

1. Khi các khóa S3 hoặc người dùng Swift được tạo, theo mặc định, chúng có quyền truy cập đầy đủ vào tất cả các dự án/đối tượng vStorage (với cài đặt **Hạn chế bởi IAM** là **KHÔNG**). Để bật kiểm soát truy cập thích hợp cho các cặp khóa và người dùng này, bạn cần bật thuộc tính **Hạn chế bởi IAM** bằng cách đặt nó thành **CÓ**.
2. Một khi bạn bật **Hạn chế bởi IAM thành CÓ**, IAM sẽ quản lý và cấp quyền cho các cặp khóa và người dùng này. Do đó, theo mặc định, các cặp khóa và người dùng được kích hoạt sẽ không có quyền truy cập vào bất kỳ dự án/đối tượng vStorage nào.
3. Sau khi bật Hạn chế bởi IAM thành CÓ, để cấp quyền, bạn cần liên kết các cặp khóa và người dùng này với Tài khoản Dịch vụ để chúng thừa hưởng các quyền được gán cho Tài khoản Dịch vụ được đính kèm.

Tìm thêm hướng dẫn chi tiết về cách sử dụng và áp dụng vStorage credentials trên tài nguyên vStorage tại:

* [Cách hoạt động của vStorage credentials](./#iamidentities-vstoragecredentials)

#### Identity Provider <a href="#iamidentities-identityprovider" id="iamidentities-identityprovider"></a>

Identity Providers là dịch vụ cho phép người dùng xác thực danh tính và truy cập nhiều ứng dụng và dịch vụ với một bộ thông tin đăng nhập duy nhất, sử dụng các giao thức xác thực để trao đổi thông tin định danh một cách an toàn và quản lý các chính sách kiểm soát truy cập. Hệ thống của chúng tôi hiện hỗ trợ SAML2 là giao thức xác thực chính, tạo điều kiện cho việc trao đổi định danh an toàn giữa IDP (các nhà cung cấp xác thực) và VNG Cloud (Service Provider). SAML2 đã chứng minh hiệu quả trong việc kích hoạt đăng nhập một lần (SSO) và truy cập liền mạch nhiều ứng dụng và dịch vụ.

* Để tích hợp với hệ thống của chúng tôi bằng SAML, bạn có thể sử dụng ID thực thể SAML của chúng tôi: [https://signin.vngcloud.vn/auth/realms/iam](https://signin.vngcloud.vn/auth/realms/iam)
* URL này hoạt động như là điểm cuối để khởi tạo quá trình xác thực SAML và trao đổi thông tin định danh một cách an toàn.

Tìm thêm hướng dẫn chi tiết tại:

* [Quản lý Identity Providers](thiet-lap-identity-providers.md)\


