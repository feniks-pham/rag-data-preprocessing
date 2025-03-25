# Làm việc với Service Account

## **Tổng quan**

**Service Account** là một danh tính mà bạn có thể tạo trong tài khoản của mình có các quyền cụ thể. Service Account có một số điểm tương đồng với người dùng IAM. Service Account và IAM User Account đều là danh tính với các Policy cho phép xác định những gì danh tính có thể và không thể làm với tài nguyên Đám mây của VNG. Tuy nhiên, Service Account là danh tính được sử dụng bởi một ứng dụng hoặc một máy chứ không phải một người, để thực hiện các lệnh gọi API được ủy quyền và truy cập các tài nguyên được chỉ định.&#x20;

***

## Khởi tạo Service Account

Để khởi tạo tài khoản Service Account, hãy làm theo các bước bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn mục **Service Account**.
3. Chọn **Create a Service Account.**
4. Tại mục **Add information**, nhập **Name** mà bạn mong muốn. Tên của Service Account phải dài từ 1 (tối thiểu) đến 50 (tối đa) ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-) và khoảng trắng( ). Tên của Service Account không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, mật khẩu đăng nhập,...) cũng như tên Service Account phải là duy nhất trên một tài khoản VNG Cloud cho đến khi Service Account đó bị xóa. Ví dụ tên Service Account sau là hợp lệ: SA\_Client\_tool\_01.
5. Tại mục Trusted relationship, nhập Account Root IS nếu bạn muốn thêm thông tin liên kết giữa Service Account và Root User Account.
6. Chọn **Next step**.
7. Tại mục **Add permission**, bạn có thể:
   1. Chọn 1 hoặc nhiều policy mà bạn đang có để liên kết với Service Account. Hệ thống vIAM hỗ trợ bạn gán nhiều policy vào một tài khoản Service Account. Nếu các policy này chứa các quyền hạn độc lập thì chúng sẽ bổ sung cho nhau (tức là danh sách quyền hạn được hợp lại). Ngược lại nếu các policy này chứa các quyền hạn trái ngược thì bạn sẽ không thể truy cập vào tài nguyên tương ứng theo danh sách quyền hạn này (tức là danh sách quyền được hợp lại và khi trái ngược thì sẽ triệt tiêu nhau).&#x20;
   2. Nếu danh sách policy chưa có policy mà bạn mong muốn, bạn có thể tiếp tục các bước bên dưới và chúng tôi chấp nhận việc khởi tạo policy sau khi khởi tạo tài khoản Service Account.
8. Chọn **Copy** để sao chép Secret key. Bạn bắt buộc phải thu thập được thông tin này để có thể truy cập vào vStorage sử dụng Service Account.
9. Chọn **Download** để tải xuống secret key này và lưu trữ chúng tại thiết bị local của bạn.
10. Chọn **Back to list** để quay lại màn hình chứa danh sách Service Account.

Sau khi bạn thực hiện 10 bước bên trên, một tài khoản Service Account đã được khởi tạo.

<figure><img src="../../../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

***

## Phân quyền làm việc với project (vStorage API) cho Service Account

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
   2. Chọn <mark style="background-color:blue;">**All vstorage-hcm04 actions**</mark> nếu muốn tạo policy có quyền thực hiện tất cả các hành động trên vStorage. Hoặc bạn có thể chọn một số hành động cụ thể mà bạn muốn phân quyền cho Service Account.
8. Chọn **Resources**: chọn **All resources.**&#x20;
9. Chọn **Request conditions:** nhập điều kiện đặc biệt cho policy nếu có.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Attach IAM Policy vào Service Account

Sau khi bạn đã khởi tạo Service Account và Policy mong muốn, tiếp theo bạn cần liên kết tài khoản Service Account vào policy theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **Service Account.**
3. Chọn **Service Account** muốn thực hiện gán quyền.
4. Chọn **Attach policies**.
5. Chọn các **policy** mà bạn mong muốn. Hệ thống vIAM hỗ trợ bạn gán nhiều policy vào một tài khoản Service Account. Nếu các policy này chứa các quyền hạn độc lập thì chúng sẽ bổ sung cho nhau (tức là danh sách quyền hạn được hợp lại). Ngược lại nếu các policy này chứa các quyền hạn trái ngược thì bạn sẽ không thể truy cập vào tài nguyên tương ứng theo danh sách quyền hạn này (tức là danh sách quyền được hợp lại và khi trái ngược thì sẽ triệt tiêu nhau).
6. Chọn **Attach**.

<figure><img src="../../../../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

***

## Phân quyền làm việc với bucket/ object cho Service Account

Để phân quyền truy cập vào bucket/ object cho Service Account, bạn cần thực hiện phân quyền qua tính băng Bucket Policy, cụ thể các bước thực hiện như sau:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng ![](<../../../../.gitbook/assets/image (7) (1) (1).png>)tại project chứa bucket bạn muốn phân quyền.
3. Tại mục **Identity and Access Management**, thực hiện sao chép thông tin **vStorage User ID** tại mục **List of Service Account**.&#x20;

<figure><img src="../../../../.gitbook/assets/image (13) (1).png" alt=""><figcaption></figcaption></figure>

4. Tiếp tục chọn **Bucket** bạn muốn thực hiện phân quyền cho Service Account.
5. Chọn biểu tượng **Action** và chọn **Configure policy.**

<figure><img src="../../../../.gitbook/assets/image (870).png" alt=""><figcaption></figcaption></figure>

6. Tại đây, bạn có thể chọn cấu hình cho từng **Statement** ở bên trái hoặc trực tiếp chỉnh sửa file JSON ở cột bên phải. Cụ thể cấu trúc một Bucket Policy bao gồm:

* **Version**: Xác định phiên bản của Bucket Policy (nên dùng `"2012-10-17"`).
* **Statement**: Mỗi chính sách sẽ có một hoặc nhiều **Statement** (mục đích cụ thể của policy).
  * **Effect**: `Allow` hoặc `Deny` quyền truy cập.
  * **Principal**: Đối tượng được cấp quyền truy cập, chính là thông tin IAM vStorage User ID bạn đã sao chép bên trên
  * **Action**: Các hành động cho phép trên bucket, ví dụ: `s3:GetObject` (xem object), `s3:PutObject` (tải lên object), `s3:DeleteObject` (xóa object),…
  * **Resource**: Các bucket và object cụ thể bị ảnh hưởng bởi policy (dùng ARN để định danh tài nguyên).
  * **Condition**: (Tùy chọn) Điều kiện cụ thể giới hạn quyền truy cập.

5\. Chọn **Save** để lưu lại cấu hình Bucket Policy.

<figure><img src="../../../../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

***

## Thực hiện làm việc với vStorage API thông qua Service Account

Thực hiện theo các bước bên dưới làm việc với vStorage thông qua Service Account

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn thư mục **Integration.**
3. Chọn biểu tượng **vStorage API**.
4. Tại mục **Authentication**, bạn cần điền thông tin cần thiết để cấu hình vStorage API của bạn bao gồm:
   1. Nhập **Client ID**. Một **Client ID** là một chuỗi ký tự được sử dụng bởi Service API để định danh ứng dụng, đồng thời cũng được dùng để xây dựng "authorization URL" hiển thị phía người dùng. Bạn có thể tạo và quản lý **Client ID** thông qua hệ thống vIAM. **Client ID** sẽ được tự động sinh ra khi bạn tạo mới một **Service Account**. .
   2. Nhập **Client Secret** tương ứng của **Client ID** vừa nhập. Cặp Client ID và Client Secret được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Click here to manage your Client ID.](https://hcm-3.console.vngcloud.vn/iam/service-accounts) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý Service Account.&#x20;
5. Sau khi hoàn tất chọn cấu hình **xác thực**, chọn **Authentication** để chuyển tới màn hình **Configuration. Tại đây bạn có thể sử dụng trực tiếp các vStorage API hoặc bạn có thể sử dụng API thông qua Postman**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Xác thực** để cập nhật danh sách S3 Rest API theo thông số mới của bạn.

Chi tiết, vui lòng tham khảo thêm tại [https://docs.api.vngcloud.vn/service-docs/vstorage-api.html](https://docs.api.vngcloud.vn/service-docs/vstorage-api.html).

<figure><img src="../../../../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt=""><figcaption></figcaption></figure>

***

## Xóa Service Account

Để hủy (xóa) một tài khoản Service Account đã tạo trước đó, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn mục **Service Account**.
3. Trên danh sách các Service Account đang có, bạn hãy chọn một hoặc nhiều tài khoản Service Account mà bạn muốn hủy bỏ (xóa).
4. Chọn **Delete**.

Kể từ thời điểm Service Account bị hủy thành công, bạn sẽ không thể sử dụng Service Account này để truy xuất vào vStorage. Hãy thận trọng khi thực hiện thao tác hủy (xóa) tài khoản Service Account bởi bạn sẽ không thể khôi phục tài khoản đã xóa này.
