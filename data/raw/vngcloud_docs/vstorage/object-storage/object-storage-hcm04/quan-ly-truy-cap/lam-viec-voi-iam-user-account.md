# Làm việc với IAM User Account

## **Tổng quan**

**Tài khoản người dùng IAM (IAM User Account)**, là những tài khoản đại diện dùng để tương tác với VNG Cloud thông qua trang Portal UI. Một tài khoản user account ở VNG sẽ bao gồm những thông tin xác thực (tên đăng nhập và mật khẩu) và được mặc định thiết lập ở trạng thái không có quyền truy cập. Những tài khoản user account này không tồn tại độc lập; chúng thuộc về một tài khoản root user account duy nhất và không đi kèm bất kỳ chi phí nào.

Nếu doanh nghiệp bạn có nhiều thành viên cần được cấp quyền truy cập vào VNG Cloud, đừng chia sẻ thông tin bảo mật của tài khoản root user account. VNG khuyến khích bạn nên tạo những tài khoản user account cho từng thành viên này trên tài khoản root user account của bạn và bạn sẽ có thể cấp các phân quyền khác nhau cho từng user account này.

***

## Khởi tạo IAM User Account

Để khởi tạo tài khoản người dùng IAM, trước tiên bạn vui lòng tham khảo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn mục **User Account**.
3. Chọn **Create a User Account.**
4. Tại mục **Account username**, nhập **Account username** mà bạn mong muốn. Tên của IAM User Account phải dài từ 5 (tối thiểu) đến 50 (tối đa) ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-). Tên của IAM User Account không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, mật khẩu đăng nhập,...) cũng như tên IAM User Account phải là duy nhất trên một tài khoản VNG Cloud cho đến khi IAM User Account đó bị xóa. Ví dụ tên IAM User Account sau là hợp lệ: IAM\_Phong\_kinh\_doanh\_01.
5. Chọn **Add a username**.
6. Tại mục **Account password**, bạn có thể:
   1. Nhập **password** mà bạn mong muốn. Password phải dài từ 8 (tối thiểu) đến 50 (tối đa) ký tự và phải bao gồm ít nhất 1 ký tự viết hoa (A-Z), 1 ký tự viết thường (a-z), 1 ký tự số (0-9) và 1 ký tự đặc biệt (!@#$%,...).
   2. Chọn **Auto-generate** nếu bạn muốn hệ thống tự động tạo mật khẩu cho bạn.
7. Chọn **Copy** để sao chép mật khẩu. Bạn bắt buộc phải thu thập được thông tin này để có thể truy cập vào vStorage sử dụng IAM User Account.
8. Chọn **Create User Account.**

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Phân quyền truy cập vào project cho IAM User Account

### Khởi tạo IAM Policy

Để khởi tạo một policy sử dụng để truy cập vào tài nguyên vStorage, hãy làm theo các bước bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **Policy**.
3. Chọn **Create a Policy**.
4. Nhập **Name** và **Description** nếu cho cho Policy.
5. Chọn **Next step**.
6. Chọn **Product là&#x20;**<mark style="background-color:blue;">**vstorage-hcm04**</mark>.
7. Chọn **Actions**:
   1. Chọn **Allow permissions**: mặc định hệ thống vIAM sẽ luôn bật tức là cho phép quyền hạn được áp dụng trên policy. Nếu bạn tắt mode này thì hệ thống sẽ từ chối (đảo chiều) quyền hạn tương ứng.
      1. **Allow permissions**: cho phép truy cập theo action đã chọn.
      2. **Deny permissions**: từ chối truy cập theo action đã chọn.
   2. Chọn <mark style="background-color:blue;">**All vstorage-hcm04 actions**</mark> nếu muốn tạo policy có quyền thực hiện tất cả các hành động trên vStorage. Hoặc bạn có thể chọn một số hành động cụ thể mà bạn muốn phân quyền cho IAM User Account.
8. Chọn **Resources**: chọn **All resources.**&#x20;
9. Chọn **Request conditions:** nhập điều kiện đặc biệt cho policy nếu có.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Attach IAM Policy vào IAM User Account

Sau khi bạn đã khởi tạo IAM User Account và Policy mong muốn, tiếp theo bạn cần liên kết tài khoản IAM User Account vào policy theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **User Account.**
3. Chọn **IAM User Account** muốn thực hiện gán quyền.
4. Chọn **Attach policies**.
5. Chọn các **policy** mà bạn mong muốn. Hệ thống vIAM hỗ trợ bạn gán nhiều policy vào một tài khoản IAM User Account. Nếu các policy này chứa các quyền hạn độc lập thì chúng sẽ bổ sung cho nhau (tức là danh sách quyền hạn được hợp lại). Ngược lại nếu các policy này chứa các quyền hạn trái ngược thì bạn sẽ không thể truy cập vào tài nguyên tương ứng theo danh sách quyền hạn này (tức là danh sách quyền được hợp lại và khi trái ngược thì sẽ triệt tiêu nhau).
6. Chọn **Attach**.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Phân quyền truy cập vào bucket/ object cho IAM User Account

Để phân quyền truy cập vào bucket/ object cho IAM User Account, bạn cần thực hiện phân quyền qua tính băng Bucket Policy, cụ thể các bước thực hiện như sau:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng ![](<../../../../.gitbook/assets/image (7) (1) (1).png>)tại project chứa bucket bạn muốn phân quyền.
3. Tại mục **Identity and Access Management**, thực hiện sao chép thông tin **vStorage User ID** tại mục **List of IAM User Account**.&#x20;

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Tiếp tục chọn **Bucket** bạn muốn thực hiện phân quyền cho IAM User Account.
5. Chọn biểu tượng **Action** và chọn **Configure policy.**

<figure><img src="../../../../.gitbook/assets/image (868) (1).png" alt=""><figcaption></figcaption></figure>

6. Tại đây, bạn có thể chọn cấu hình cho từng **Statement** ở bên trái hoặc trực tiếp chỉnh sửa file JSON ở cột bên phải. Cụ thể cấu trúc một Bucket Policy bao gồm:

* **Version**: Xác định phiên bản của Bucket Policy (nên dùng `"2012-10-17"`).
* **Statement**: Mỗi chính sách sẽ có một hoặc nhiều **Statement** (mục đích cụ thể của policy).
  * **Effect**: `Allow` hoặc `Deny` quyền truy cập.
  * **Principal**: Đối tượng được cấp quyền truy cập, chính là thông tin IAM vStorage User ID bạn đã sao chép bên trên
  * **Action**: Các hành động cho phép trên bucket, ví dụ: `s3:GetObject` (xem object), `s3:PutObject` (tải lên object), `s3:DeleteObject` (xóa object),…
  * **Resource**: Các bucket và object cụ thể bị ảnh hưởng bởi policy (dùng ARN để định danh tài nguyên).
  * **Condition**: (Tùy chọn) Điều kiện cụ thể giới hạn quyền truy cập.

5\. Chọn **Save** để lưu lại cấu hình Bucket Policy.

<figure><img src="../../../../.gitbook/assets/image (869).png" alt=""><figcaption></figcaption></figure>

## Thực hiện truy cập vào vStorage thông qua IAM User Account

Thực hiện theo các bước bên dưới để đăng nhập vào vStorage với tài khoản người dùng IAM:

1. Truy cập vào trang đăng nhập của dịch vụ vStorage: [https://signin.vngcloud.vn.](https://signin.vngcloud.vn/ap/auth?clientId=c9e78411-f2a2-41ba-a9e4-3c56263c181a\&responseType=code\&codeChallenge=f09ybYi-GTZYYwuHVRv2f1UPRhjM_wI-0J_aXpbUsv4\&codeChallengeMethod=S256\&appState=55eab53a-30f3-43ae-837b-bf3a469dd9db\&redirectUri=https%3A%2F%2Fdashboard.console.vngcloud.vn%2F)
2. Trang đăng nhập chính sẽ xuất hiện. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**.
3. Nhập địa chỉ **email** của người dùng Root khi đăng ký tài khoản VNG Cloud.
4. Nhập **tên người dùng** và **mật khẩu** của tài khoản IAM user account được tạo trên hệ thống vIAM.
5. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**. Nếu trước đó bạn đã đăng nhập với tư cách người dùng IAM user account trong trình duyệt này, thì trình duyệt của bạn có thể nhớ địa chỉ tài khoản IAM user account. Nếu vậy, bạn sẽ thấy màn hình hiển thị ở bước 3. Sau khi đăng nhập thành công với IAM user account, trên màn hình chính của vStorage sẽ thể hiện loại user mà bạn đang sử dụng để đăng nhập (Root user account hay IAM user account).
6. Sau khi đăng nhập thành công, bạn có quyền truy cập và thực hiện các tính năng được cung cấp bởi dịch vụ vStorage trên các tài nguyên được cấp quyền cho bạn.&#x20;

<figure><img src="../../../../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

***

## Xóa IAM User Account

Để hủy (xóa) một tài khoản IAM User Account đã tạo trước đó, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn mục **User Account**.
3. Trên danh sach các IAM User Account đang có, bạn hãy chọn một hoặc nhiều tài khoản người dùng IAM mà bạn muốn hủy bỏ (xóa).
4. Chọn **Delete**.

Kể từ thời điểm IAM User Account bị hủy thành công, bạn sẽ không thể sử dụng IAM User Account này để truy xuất vào vStorage. Hãy thận trọng khi thực hiện thao tác hủy (xóa) tài khoản IAM User Account bởi bạn sẽ không thể khôi phục tài khoản đã xóa này.
