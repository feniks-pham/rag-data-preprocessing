# Làm việc với Root User Account

## **Tổng quan**

Tài khoản người dùng Root (Root User Account) là tài khoản mà người dùng khởi tạo vào ngày đầu tiên truy cập và sử dụng dịch vụ trên VNG Cloud. Tài khoản Root User Account có đầy đủ quyền truy cập vào tất cả các dịch vụ và tài nguyên của người dùng. Khi tạo tài khoản VNG Cloud, bạn bắt đầu với một danh tính đăng nhập có toàn quyền truy cập vào tất cả các dịch vụ của VNG Cloud và tài nguyên trong tài khoản. Danh tính này được gọi là Root User Account và được truy cập bằng cách đăng nhập bằng địa chỉ email và mật khẩu mà bạn đã sử dụng để tạo tài khoản. Chúng tôi khuyến khích bạn không nên sử dụng tài khoản Root User Account cho các tác vụ hàng ngày của mình và chỉ sử dụng tài khoản này để thực hiện các tác vụ mà chỉ tài khoản Root User Account mới có thể thực hiện.

***

## **Khởi tạo Root User Account**

Để khởi tạo tài khoản người dùng Root, bạn vui lòng đăng ký tài khoản tại trang đăng ký [https://register.vngcloud.vn/signup](https://register.vngcloud.vn/signup).

Sau khi khởi tạo tài khoản người dùng Root, bạn thu thập thông tin sau để truy cập và làm việc với tài nguyên sử dụng tài khoản người dùng Root:

* Địa chỉ email được sử dụng để tạo tài khoản người dùng Root.
* Mật khẩu cho của tài khoản người dùng Root.

Để thực hiện đăng nhập sử dụng vStorage với tài khoản Root, hãy xem thêm tại [Truy cập tài nguyên sử dụng tài khoản người dùng Root](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-truy-cap-tai-nguyen-vstorage/truy-cap-tai-nguyen-su-dung-tai-khoan-nguoi-dung-root).

***

## **Hủy Root User Account**

Để hủy tài khoanr Root, bạn cần liên hệ với chúng tôi thông qua việc tạo một ticket yêu cầu hủy tài khoản. Chi tiết xem thêm tại [Hướng dẫn hủy tài khoản](https://docs.vngcloud.vn/vng-cloud-document/vn/huong-dan-su-dung-tai-khoan/huong-dan-huy-tai-khoan).

***

## Truy cập vào vStorage sử dụng Root User Account

Để truy cập vào tài nguyên của bạn trên dịch vụ lưu trữ vStorage, bạn có thể truy cập thông qua vStorage Portal, vStorage API, S3 Rest API và Swift/ s3 client tool. Đối với vStorage Portal, bạn sử dụng tài khoản người dùng Root (Root User Account) để truy cập vào. Nếu bạn chưa có tài khoản người dùng Root, bạn vui lòng tham khảo tại [Tài khoản người dùng Root](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-nguoi-dung-root).

Thực hiện theo các bước bên dưới để đăng nhập vào vStorage với tài khoản người dùng Root:

1. Truy cập vào trang đăng nhập của dịch vụ vStorage: [https://signin.vngcloud.vn.](https://signin.vngcloud.vn/ap/auth?clientId=c9e78411-f2a2-41ba-a9e4-3c56263c181a\&responseType=code\&codeChallenge=f09ybYi-GTZYYwuHVRv2f1UPRhjM_wI-0J_aXpbUsv4\&codeChallengeMethod=S256\&appState=55eab53a-30f3-43ae-837b-bf3a469dd9db\&redirectUri=https%3A%2F%2Fdashboard.console.vngcloud.vn%2F)
2. Trang đăng nhập chính sẽ xuất hiện. Chọn **ĐĂNG NHẬP VỚI ROOT USER**.
3. Nhập địa chỉ **email** và **mật khẩu** được liên kết với tài khoản của bạn và chọn **Đăng nhập**. Nếu trước đó bạn đã đăng nhập với tư cách người dùng root trong trình duyệt này, thì trình duyệt của bạn có thể nhớ địa chỉ email cho tài khoản Root User Account. Nếu vậy, bạn sẽ thấy màn hình hiển thị trong bước tiếp theo. Nếu trước đây bạn đã đăng nhập với tư cách là người dùng IAM sử dụng tài khoản người dùng IAM (IAM User Account) bằng trình duyệt này, thì trình duyệt của bạn có thể hiển thị trang đăng nhập của người dùng IAM thay thế. Để quay lại trang đăng nhập chính, hãy chọn **ĐĂNG NHẬP VỚI ROOT USER.**
4. Sau khi đăng nhập thành công, bạn có toàn quyền truy cập và thực hiện các tính năng được cung cấp bởi dịch vụ vStorage trên các tài nguyên của bạn.&#x20;

<figure><img src="../../../../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

***

## Phân quyền làm việc cho Root User Account

Mặc định, **Root User Account** sẽ có **toàn quyền** làm việc trên bucket của bạn, nhưng bạn cũng có thể phân quyền cho **Root User Account khác** truy cập vào bucket của bạn như là **IAM User Account** của bạn qua tính năng **Bucket ACLs** và **Bucket Policy**.

<details>

<summary>Bucket ACLs</summary>

Bạn có thể cấp quyền Đọc, Ghi hoặc Đọc và Ghi cho 1 hoặc tất cả Root user khác. (Root user được cấp quyền truy cập qua ACLS phải là tài khoản được cấp quyền trên hệ thống VNG Cloud của chúng tôi). Để biết thêm thông tin, hãy xem tại [Sử dụng tính năng ACLs.](../cac-tinh-nang-cua-object-storage/lam-viec-voi-bucket/lam-viec-voi-bucket-thong-qua-vstorage-portal/su-dung-tinh-nang-acls.md)

</details>

<details>

<summary>Bucket Policy</summary>

Bạn có thể quản lý quyền truy cập vào bucket của bạn thông qua các quy tắc dạng JSON. Để biết thêm thông tin, hãy xem tại [Sử dụng tính năng Bucket Policy.](../cac-tinh-nang-cua-object-storage/lam-viec-voi-bucket/lam-viec-voi-bucket-thong-qua-vstorage-portal/su-dung-tinh-nang-bucket-policy.md)

</details>
