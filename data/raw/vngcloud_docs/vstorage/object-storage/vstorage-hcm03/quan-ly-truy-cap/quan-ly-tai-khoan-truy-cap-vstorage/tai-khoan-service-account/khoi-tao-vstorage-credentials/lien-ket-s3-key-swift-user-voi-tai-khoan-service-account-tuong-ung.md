# Liên kết S3 key, Swift user với tài khoản Service Account tương ứng

Sau khi bạn đã khởi tạo S3 key, Swift user mong muốn và thiết lập **Restriction by IAM = YES**, tiếp theo bạn cần liên kết S3 key, Swift user với tài khoản Service Account theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục vStorage credentials.
   1. Tại mục S3, trên danh sách S3 key đang có tiếp tục chọn bật ![](https://docs.vngcloud.vn/download/thumbnails/59804923/image2023-6-30\_9-42-4.png?version=1\&modificationDate=1688092925000\&api=v2)**.** Khi trạng thái hiển thị là ![](https://docs.vngcloud.vn/download/thumbnails/59804923/image2023-6-30\_9-44-16.png?version=1\&modificationDate=1688093057000\&api=v2) tức là bạn đã bật thành công việc kiểm soát quyền hạn của S3 key bởi hệ thống vIAM.
   2. Tại mục Swift, trên danh sách Swift user đang có tiếp tục chọn bật ![](https://docs.vngcloud.vn/download/thumbnails/59804923/image2023-6-30\_9-42-4.png?version=1\&modificationDate=1688092925000\&api=v2)**.** Khi trạng thái hiển thị là ![](https://docs.vngcloud.vn/download/thumbnails/59804923/image2023-6-30\_9-44-16.png?version=1\&modificationDate=1688093057000\&api=v2) tức là bạn đã bật thành công việc kiểm soát quyền hạn của Swift user bởi hệ thống vIAM.&#x20;
3. Chọn thư mục **Service Account.**&#x20;
4. Chọn **Service Account** muốn thực hiện gán S3 key, Swift user.&#x20;
5. Chọn mục **Security credential.**
6. Tại mục vStorage credential, chọn **Attach.**
7. Chọn các **S3 key và Swift user** mà bạn mong muốn liên kết tới Service Account đang chọn. Hệ thống vIAM hỗ trợ bạn liên kết nhiều S3 key, Swift user vào một tài khoản Service Account nhưng một S3 key hay một Swift user chỉ có thể gán vào một Service Account.&#x20;

Sau khi bạn thực hiện 7 bước bên trên, lúc này bạn đã có thể sử dụng Service Account để truy cập vào tài nguyên vStorage. Để biết thêm thông tin, hãy xem tại [Truy cập tài nguyên sử dụng tài khoản Service Account](../../../quan-ly-truy-cap-tai-nguyen-vstorage/truy-cap-tai-nguyen-su-dung-tai-khoan-service-account.md).

<figure><img src="../../../../../../../.gitbook/assets/Lien_ket_S3_key_Swift_user_voi_Service_Account.gif" alt=""><figcaption></figcaption></figure>
