# Khởi tạo S3 key

Để khởi tạo S3 key, làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **vStorage credentials**.&#x20;
3. Chọn **Create a S3 key**.
4. Nhập **Name** của S3 key mà bạn muốn tạo.&#x20;
5. Chọn **Region** chứa project trên vStorage của bạn.
6. Chọn **vStorage project** mà bạn mong muốn tạo S3 key.
7. Chọn **Create.**
8. Chọn **Copy** hoặc **Download** để tải xuống thông tin Access Key/Secret Key mà bạn vừa khởi tạo.

Lưu ý sau khi nhấn tạo S3 key, bạn cần **lưu lại cặp Access Key/Secret Key** để sử dụng, nếu bạn không lưu trữ ngay lúc này thì sau đó không thể lấy được Secret Key của Access Key này.

{% hint style="info" %}
**Chú ý:**&#x20;



* Khi S3 key được tạo ra, mặc định trạng thái Restriction by IAM của S3 key này là NO (**Restriction by IAM = NO**), lúc này bạn có thể sử dụng S3 key này để truy cập tới tài nguyên thuộc project mà bạn chọn khi tạo S3 key, hệ thống vIAM sẽ không thực hiện kiểm tra quyền hạn đối với S3 key này.&#x20;
* Khi bạn bật thuộc tính Restriction by IAM của S3 key thành YES (**Restriction by IAM = YES**), S3 key này sẽ được quản lý và kiểm tra quyền hạn bởi hệ thống vIAM. Do đó để có thể sử dụng các S3 key này, bạn cần **liên kết chúng tới một Service Account** để chúng thừa hưởng quyền trên Service Account được liên kết đó. Chi tiết tham khảo tại [Liên kết S3 key, Swift user với tài khoản Service Account tương ứng](lien-ket-s3-key-swift-user-voi-tai-khoan-service-account-tuong-ung.md).


{% endhint %}

<figure><img src="../../../../../../../.gitbook/assets/Khoi_tao_S3key.gif" alt=""><figcaption></figcaption></figure>
