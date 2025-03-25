# Truy cập tài nguyên sử dụng tài khoản người dùng Root

Để truy cập vào tài nguyên của bạn trên dịch vụ lưu trữ vStorage, bạn có thể truy cập thông qua vStorage Portal, vStorage API, Swift Rest API, S3 Rest API và Swift/ s3 client tool. Đối với vStorage Portal, bạn sử dụng tài khoản người dùng Root (Root User Account) để truy cập vào. Nếu bạn chưa có tài khoản người dùng Root, bạn vui lòng tham khảo tại [Tài khoản người dùng Root](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-nguoi-dung-root.md).

Thực hiện theo các bước bên dưới để đăng nhập vào vStorage với tài khoản người dùng Root:

1. Truy cập vào trang đăng nhập của dịch vụ vStorage: [https://signin.vngcloud.vn.](https://signin.vngcloud.vn/ap/auth?clientId=c9e78411-f2a2-41ba-a9e4-3c56263c181a\&responseType=code\&codeChallenge=f09ybYi-GTZYYwuHVRv2f1UPRhjM\_wI-0J\_aXpbUsv4\&codeChallengeMethod=S256\&appState=55eab53a-30f3-43ae-837b-bf3a469dd9db\&redirectUri=https%3A%2F%2Fdashboard.console.vngcloud.vn%2F)
2. Trang đăng nhập chính sẽ xuất hiện. Chọn **ĐĂNG NHẬP VỚI ROOT USER**.
3. Nhập địa chỉ **email** và **mật khẩu** được liên kết với tài khoản của bạn và chọn **Đăng nhập**. Nếu trước đó bạn đã đăng nhập với tư cách người dùng root trong trình duyệt này, thì trình duyệt của bạn có thể nhớ địa chỉ email cho tài khoản Root User Account. Nếu vậy, bạn sẽ thấy màn hình hiển thị trong bước tiếp theo. Nếu trước đây bạn đã đăng nhập với tư cách là người dùng IAM sử dụng tài khoản người dùng IAM (IAM User Account) bằng trình duyệt này, thì trình duyệt của bạn có thể hiển thị trang đăng nhập của người dùng IAM thay thế. Để quay lại trang đăng nhập chính, hãy chọn **ĐĂNG NHẬP VỚI ROOT USER.**
4. Sau khi đăng nhập thành công, bạn có toàn quyền truy cập và thực hiện các tính năng được cung cấp bởi dịch vụ vStorage trên các tài nguyên của bạn. Chi tiết về các tính năng vStorage hỗ trợ, bạn vui lòng tham khảo tại [Các tính năng của vStorage](../../cac-tinh-nang-cua-vstorage/).

<figure><img src="../../../../../.gitbook/assets/Su_dung_Root.gif" alt=""><figcaption></figcaption></figure>
