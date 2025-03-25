# Truy cập tài nguyên sử dụng tài khoản người dùng IAM

Để truy cập vào tài nguyên của bạn trên dịch vụ lưu trữ vStorage, bạn có thể truy cập thông qua vStorage Portal, vStorage API, Swift Rest API, S3 Rest API và Swift/ s3 client tool. Đối với vStorage Portal, bạn có thể sử dụng tài khoản người dùng IAM (IAM User Account) để truy cập vào. Nếu bạn chưa có tài khoản người dùng IAM, bạn vui lòng tham khảo tại [Tài khoản người dùng IAM](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-nguoi-dung-iam/).

Thực hiện theo các bước bên dưới để đăng nhập vào vStorage với tài khoản người dùng IAM:

1. Truy cập vào trang đăng nhập của dịch vụ vStorage: [https://signin.vngcloud.vn.](https://signin.vngcloud.vn/ap/auth?clientId=c9e78411-f2a2-41ba-a9e4-3c56263c181a\&responseType=code\&codeChallenge=f09ybYi-GTZYYwuHVRv2f1UPRhjM\_wI-0J\_aXpbUsv4\&codeChallengeMethod=S256\&appState=55eab53a-30f3-43ae-837b-bf3a469dd9db\&redirectUri=https%3A%2F%2Fdashboard.console.vngcloud.vn%2F)
2. Trang đăng nhập chính sẽ xuất hiện. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**.
3. Nhập địa chỉ **email** của người dùng Root khi đăng ký tài khoản VNG Cloud.
4. Nhập **tên người dùng** và **mật khẩu** của tài khoản IAM user account được tạo trên hệ thống vIAM.
5. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**.\
   Nếu trước đó bạn đã đăng nhập với tư cách người dùng IAM user account trong trình duyệt này, thì trình duyệt của bạn có thể nhớ địa chỉ tài khoản IAM user account. Nếu vậy, bạn sẽ thấy màn hình hiển thị ở bước 3. \
   Sau khi đăng nhập thành công với IAM user account, trên màn hình chính của vStorage sẽ thể hiện loại user mà bạn đang sử dụng để đăng nhập (Root user account hay IAM user account).
6. Sau khi đăng nhập thành công, bạn có quyền truy cập và thực hiện các tính năng được cung cấp bởi dịch vụ vStorage trên các tài nguyên được cấp quyền cho bạn. Chi tiết về các tính năng vStorage hỗ trợ, bạn vui lòng tham khảo tại [Các tính năng của vStorage](../../cac-tinh-nang-cua-vstorage/). Nếu tài khoản người dùng IAM của bạn chưa được cấp quyền thực hiện các tính năng của dịch vụ vStorage trên các tài nguyên, bạn vui lòng tham khảo [Phân quyền truy cập thông qua IAM](phan-quyen-truy-cap-va-lam-viec-thong-qua-iam/).

<figure><img src="../../../../../.gitbook/assets/Su_dung_IAM.gif" alt=""><figcaption></figcaption></figure>
