# Tài khoản Service accounts

Service Account là một danh tính mà bạn có thể tạo trong tài khoản Root User của bạn và có các quyền cụ thể. Nó có một số điểm tương đồng với IAM User Account. Để làm rõ hơn, Service Account và IAM User Account đều là các danh tính có chính sách quyền xác định những gì danh tính đó có thể và không thể làm với tài nguyên VNG Cloud. Tuy nhiên,Service Account được sử dụng bởi một ứng dụng hoặc máy móc, không phải là một người, để thực hiện các cuộc gọi API được ủy quyền và truy cập vào các tài nguyên được chỉ định.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806688/Identities-Service%20Account.drawio%20(1).png?version=1&#x26;modificationDate=1691474588000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

#### 1. Cách Tạo Service Account? <a href="#serviceaccounts-1.cachtaoserviceaccount" id="serviceaccounts-1.cachtaoserviceaccount"></a>

Để tạo một Service Account mới:

1. Truy cập vào IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Nhấp vào **"Service account"** trong menu bên trái.
3. Nhấp vào **"Create service account."**
4. Nhập thông tin Service Account, bao gồm tên và mô tả tùy chọn.
5. Gắn các **Policies** cần thiết
6. Xem lại các thiết lập và nhấp **"Create service account"** ở góc phải trên cùng.
7. Lưu thông tin **Client Secret Key**



Tips

Hãy nhớ lưu Client Secret ở một nơi khác vì nó chỉ hiển thị một lần duy nhất.

#### 2. Gán Quyền cho Service Account <a href="#serviceaccounts-2.ganquyenchoserviceaccount" id="serviceaccounts-2.ganquyenchoserviceaccount"></a>

Để gán Policies vào Service Account:

1. Truy cập vào IAM - Trang Service Acocunt với URL: [https://hcm-3.console.vngcloud.vn/iam/service-accounts](https://hcm-3.console.vngcloud.vn/iam/service-accounts)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Tìm kiếm Service Account bằng cách nhập tên người dùng vào ô tìm kiếm và chọn kết quả đúng trong kết quả tìm kiếm.
4. Mặc định, bạn sẽ thấy tab "**Permission**" tại trang thông tin chi tiết của Service Account.
5. Nhấp vào nút "**Attach Policies**", sau đó bạn sẽ thấy một cửa sổ nhảy lên chứa tất cả Policies.
6. Tìm kiếm các Policies hiện có bằng cách nhập chính xác tên Policies vào ô tìm kiếm.
7. Chọn Policies trong kết quả tìm kiếm và nhấp vào nút "**Attach**" ở góc dưới bên phải của cửa sổ nhảy lên.
8. Bây giờ, Service Account của bạn sẽ có tất cả các quyền hạn nằm trong các Policies đã gắn vào.

#### 3. Cách Tạo Mối Quan Hệ Tin Cậy (Trusted Relationships) <a href="#serviceaccounts-3.cachtaomoiquanhetincay-trustedrelationships" id="serviceaccounts-3.cachtaomoiquanhetincay-trustedrelationships"></a>

**Trusted Relationship** là tính năng chia sẻ quyền giữa các **Root User Accounts** khác nhau, cho phép việc ủy quyền truy cập được điều chỉnh và bảo mật trên các thực thể quản trị riêng biệt. Với tính năng này, các **Root User Accounts** khác nhau có thể hợp tác trong khi vẫn duy trì tính riêng tư và ranh giới bảo mật. Tính năng này đặc biệt hữu ích trong các tình huống khi nhiều tổ chức hoặc nhóm cần làm việc cùng nhau trên các tài nguyên chia sẻ, đảm bảo sự hợp tác hiệu quả mà không đánh đổi tính bảo mật.

**Tìm hiểu thêm về Trusted Relationship tại đây:**

* [Trusted Relationship](xac-dinh-trusted-relationship.md)

#### 4. Quản lý thông tin xác thực Service Account <a href="#serviceaccounts-4.quanlythongtinxacthucserviceaccount" id="serviceaccounts-4.quanlythongtinxacthucserviceaccount"></a>

Một Service Account bao gồm thông tin xác thực (Client ID và Secret Key). Bạn cần lưu trữ Secret Key hoặc tải xuống sau khi tạo Service Account. Tuy nhiên, bạn cũng có thể tạo lại Secret Key bất kỳ lúc nào.

1. Truy cập trang Service account trong Bảng điều khiển IAM: [https://hcm-3.console.vngcloud.vn/iam/service-accounts](https://hcm-3.console.vngcloud.vn/iam/service-accounts)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Tìm kiếm Service Account bằng cách nhập tên vào ô tìm kiếm và chọn đúng kết quả trong danh sách.
4. Nhấp vào tab "**Security credentials**" (Thông tin xác thực bảo mật) trong thông tin chi tiết của Service Account. Bạn sẽ thấy thông tin như hình dưới đây và bạn có thể thực hiện các hành động sau:
   1. Sao chép Client ID.
   2. Đặt lại Client Secret và nhớ lưu lại Secret mới.
   3. Kích hoạt/Tắt kích hoạt Service Account thông qua việc thay đổi Status

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806688/image2023-7-27_13-51-21.png?version=1&#x26;modificationDate=1690440683000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

#### 5. Gắn S3 keys và Swift users vào Service Account <a href="#serviceaccounts-5.gans3keysvaswiftusersvaoserviceaccount" id="serviceaccounts-5.gans3keysvaswiftusersvaoserviceaccount"></a>

Để gắn S3 Key và Swift user chúng tôi khuyến nghị bạn nên tuân theo các hướng dẫn dưới đây:

* [Khởi tạo vStorage Credentials](../../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/)
* [Khởi tạo S3](../../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-s3-key.md)
* [Khởi tạo Swift user](../../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-swift-user.md)
* [Liên kết S3, Swift user](../../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/lien-ket-s3-key-swift-user-voi-tai-khoan-service-account-tuong-ung.md)

#### 6. Xóa Service Account? <a href="#serviceaccounts-6.xoaserviceaccount" id="serviceaccounts-6.xoaserviceaccount"></a>

Bạn có thể xóa Service Account bằng cách tuân theo 2 tùy chọn dưới đây:

1. **Xóa nhiều Service Account cùng một lúc:**
   * Truy cập vào IAM với Tài khoản người dùng Gốc.
   * Nhấp vào **"Service account"** (Tài khoản Dịch vụ) trong menu bên trái.
   * Chọn các Service Account mà bạn muốn xóa (một nút "**Delete**" sẽ được bật ở góc trên bên phải khi bạn chọn ít nhất một tài khoản).
   * Nhấp vào nút "**Delete**" (Xóa), một hộp thoại xác nhận sẽ xuất hiện để đảm bảo bạn không xóa nhầm tài khoản, sau đó nhấp vào nút "**Confirm**" (Xác nhận) để hoàn tất quy trình.
2. **Xóa một Service Account:** Chúng tôi khuyến nghị bạn nên truy cập vào thông tin chi tiết của Service Account và thực hiện xóa từ đó để đảm bảo bạn không xóa nhầm tài khoản.
