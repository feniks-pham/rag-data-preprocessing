# Quản lý truy cập

## Tài khoản truy cập <a href="#tai-khoan-truy-cap" id="tai-khoan-truy-cap"></a>

Trên hệ thống File Storage, bạn có thể sử dụng 2 loại tài khoản để truy cập vào File Storage. Chi tiết 2 loại này bao gồm:

* **Root user account:** Là tài khoản [khởi tạo đầu tiên](https://register.vngcloud.vn/signup) để truy cập vào VNG Cloud với đầy đủ quyền truy cập vào tất cả dịch vụ tài nguyên trên VNG Cloud.
* **IAM user account:** Là tài khoản được khởi tạo thông qua hệ thống IAM và được sử dụng để thao tác thông qua File Storage Portal.

### Root user account <a href="#root-user-account" id="root-user-account"></a>

**Khởi tạo tài khoản người dùng Root (Root User Account)**

Để khởi tạo tài khoản người dùng Root, bạn vui lòng đăng ký tài khoản tại trang đăng ký [https://register.vngcloud.vn/signup](https://register.vngcloud.vn/signup).

Sau khi khởi tạo tài khoản người dùng Root, bạn thu thập thông tin sau để truy cập và làm việc với tài nguyên sử dụng tài khoản người dùng Root:

* Địa chỉ email được sử dụng để tạo tài khoản người dùng Root.
* Mật khẩu cho của tài khoản người dùng Root.

***

**Hủy tài khoản người dùng Root (Root User Account)**

Để hủy tài khoản Root, bạn cần liên hệ với chúng tôi thông qua việc tạo một ticket yêu cầu hủy tài khoản. Chi tiết xem thêm tại [Hướng dẫn hủy tài khoản](https://docs.vngcloud.vn/vng-cloud-document/v/vn/huong-dan-su-dung-tai-khoan/huong-dan-huy-tai-khoan).

### IAM user account <a href="#root-user-account" id="root-user-account"></a>

**Khởi tạo tài khoản người dùng IAM (IAM User Account)**

Để khởi tạo tài khoản người dùng IAM, trước tiên bạn vui lòng tham khảo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn mục **User Account**.
3. Chọn **Create a User Account.**
4. Tại mục **Account username**, nhập **Account username** mà bạn mong muốn. Tên của IAM User Account phải dài từ 5 (tối thiểu) đến 50 (tối đa) ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-). Tên của IAM User Account không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, mật khẩu đăng nhập,...) cũng như tên IAM User Account phải là duy nhất trên một tài khoản VNG Cloud cho đến khi IAM User Account đó bị xóa. Ví dụ tên IAM User Account sau là hợp lệ: IAM\_Phong\_kinh\_doanh\_01.
5. Chọn **Add a username**.
6. Tại mục **Account password**, bạn có thể:
   1. Nhập **password** mà bạn mong muốn. Password phải dài từ 8 (tối thiểu) đến 50 (tối đa) ký tự và phải bao gồm ít nhất 1 ký tự viết hoa (A-Z), 1 ký tự viết thường (a-z), 1 ký tự số (0-9) và 1 ký tự đặc biệt (!@#$%,...).
   2. Chọn **Auto-generate** nếu bạn muốn hệ thống tự động tạo mật khẩu cho bạn.
7. Chọn **Copy** để sao chép mật khẩu. Bạn bắt buộc phải thu thập được thông tin này để có thể truy cập vào File Storage sử dụng IAM User Account.
8. Chọn **Create User Account.**

<figure><img src="../../../.gitbook/assets/image (6) (4).png" alt=""><figcaption></figcaption></figure>

***

**Khởi tạo policy cho IAM user account**

Để khởi tạo một policy sử dụng để truy cập vào tài nguyên File Storage, hãy làm theo các bước bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **Policy**.
3. Chọn **Create a Policy**.
4. Nhập **Name** và **Description** nếu cho cho Policy.
5. Chọn **Next step**.
6. Chọn **Product là file-storage**.
7. Chọn **Actions**:
   1. Chọn **Allow permissions**: mặc định hệ thống vIAM sẽ luôn bật tức là cho phép quyền hạn được áp dụng trên policy. Nếu bạn tắt mode này thì hệ thống sẽ từ chối (đảo chiều) quyền hạn tương ứng.
      1. **Allow permissions**: cho phép truy cập theo action đã chọn.
      2. **Deny permissions**: từ chối truy cập theo action đã chọn.
   2. Chọn **All file storage actions** nếu muốn tạo policy có quyền thực hiện tất cả các hành động trên File Storage. Chi tiết ý nghĩa của các action vui lòng tham khảo tại [Tính năng, tài nguyên File Storage và quyền truy cập](tinh-nang-tai-nguyen-file-storage-va-quyen-truy-cap.md)
8. Chọn **Resources**:
   1. Chọn **All resources** nếu muốn quyền truy cập đã chọn bên trên được phép truy cập vào mọi tài nguyên trên tài khoản SSO account của bạn.
   2. Chọn **Specify resources**: chọn file storage id cụ thể mà bạn muốn cho phép truy cập tới. Bạn có thể nhập thông tin cho mỗi loại resources này bằng 1 trong những cách sau:
      1. **Nhập \*** nếu bạn muốn chọn tất cả tài nguyên.
      2. **Nhập cụ thể ID của file storage** nếu bạn muốn chỉ định tới chính xác file storage đó.
   3. Bạn cũng có thể chọn **Any** để cho phép truy cập tới mọi file storage trong tài khoản SSO account của bạn.
   4. Chọn **Request conditions:** nhập điều kiện đặc biệt cho policy nếu có.

Sau khi bạn thực hiện 8 bước bên trên, policy cho file storage đã được khởi tạo. Tiếp theo, bạn hãy gán nó vào IAM User Account.&#x20;

<figure><img src="../../../.gitbook/assets/image (7) (4).png" alt=""><figcaption></figcaption></figure>

**Liên kết tài khoản IAM User Account với policy tương ứng**

Sau khi bạn đã khởi tạo IAM User Account và Policy mong muốn, tiếp theo bạn cần liên kết tài khoản IAM User Account vào policy theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **User Account.**
3. Chọn **IAM User Account** muốn thực hiện gán quyền.
4. Chọn **Attach policies**.
5. Chọn các **policy** mà bạn mong muốn. Hệ thống vIAM hỗ trợ bạn gán nhiều policy vào một tài khoản IAM User Account. Nếu các policy này chứa các quyền hạn độc lập thì chúng sẽ bổ sung cho nhau (tức là danh sách quyền hạn được hợp lại). Ngược lại nếu các policy này chứa các quyền hạn trái ngược thì bạn sẽ không thể truy cập vào tài nguyên tương ứng theo danh sách quyền hạn này (tức là danh sách quyền được hợp lại và khi trái ngược thì sẽ triệt tiêu nhau).
6. Chọn **Attach**.

## Quản lý truy cập <a href="#quan-ly-truy-cap" id="quan-ly-truy-cap"></a>

### Truy cập tài nguyên sử dụng Root user account

Thực hiện theo các bước bên dưới để đăng nhập vào File Storage với tài khoản người dùng Root:

1. Truy cập vào trang đăng nhập của dịch vụ File storage: [https://signin.vngcloud.vn.](https://signin.vngcloud.vn/ap/auth?clientId=c9e78411-f2a2-41ba-a9e4-3c56263c181a\&responseType=code\&codeChallenge=f09ybYi-GTZYYwuHVRv2f1UPRhjM\_wI-0J\_aXpbUsv4\&codeChallengeMethod=S256\&appState=55eab53a-30f3-43ae-837b-bf3a469dd9db\&redirectUri=https%3A%2F%2Fdashboard.console.vngcloud.vn%2F)
2. Trang đăng nhập chính sẽ xuất hiện. Chọn **ĐĂNG NHẬP VỚI ROOT USER**.
3. Nhập địa chỉ **email** và **mật khẩu** được liên kết với tài khoản của bạn và chọn **Đăng nhập**. Nếu trước đó bạn đã đăng nhập với tư cách người dùng root trong trình duyệt này, thì trình duyệt của bạn có thể nhớ địa chỉ email cho tài khoản Root User Account. Nếu vậy, bạn sẽ thấy màn hình hiển thị trong bước tiếp theo. Nếu trước đây bạn đã đăng nhập với tư cách là người dùng IAM sử dụng tài khoản người dùng IAM (IAM User Account) bằng trình duyệt này, thì trình duyệt của bạn có thể hiển thị trang đăng nhập của người dùng IAM thay thế. Để quay lại trang đăng nhập chính, hãy chọn **ĐĂNG NHẬP VỚI ROOT USER.**
4. Sau khi đăng nhập thành công, bạn có toàn quyền truy cập và thực hiện các tính năng được cung cấp bởi dịch vụ File storage trên các tài nguyên của bạn.&#x20;

### Truy cập tài nguyên sử dụng IAM user account

Thực hiện theo các bước bên dưới để đăng nhập vào File storage với tài khoản người dùng IAM:

1. Truy cập vào trang đăng nhập của dịch vụ File storage: [https://signin.vngcloud.vn.](https://signin.vngcloud.vn/ap/auth?clientId=c9e78411-f2a2-41ba-a9e4-3c56263c181a\&responseType=code\&codeChallenge=f09ybYi-GTZYYwuHVRv2f1UPRhjM\_wI-0J\_aXpbUsv4\&codeChallengeMethod=S256\&appState=55eab53a-30f3-43ae-837b-bf3a469dd9db\&redirectUri=https%3A%2F%2Fdashboard.console.vngcloud.vn%2F)
2. Trang đăng nhập chính sẽ xuất hiện. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**.
3. Nhập địa chỉ **email** của người dùng Root khi đăng ký tài khoản VNG Cloud.
4. Nhập **tên người dùng** và **mật khẩu** của tài khoản IAM user account được tạo trên hệ thống vIAM.
5. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**. Nếu trước đó bạn đã đăng nhập với tư cách người dùng IAM user account trong trình duyệt này, thì trình duyệt của bạn có thể nhớ địa chỉ tài khoản IAM user account. Nếu vậy, bạn sẽ thấy màn hình hiển thị ở bước 3. Sau khi đăng nhập thành công với IAM user account, trên màn hình chính của File storage sẽ thể hiện loại user mà bạn đang sử dụng để đăng nhập (Root user account hay IAM user account).
6. Sau khi đăng nhập thành công, bạn có quyền truy cập và thực hiện các tính năng được cung cấp bởi dịch vụ File storage trên các tài nguyên được cấp quyền cho bạn.&#x20;
