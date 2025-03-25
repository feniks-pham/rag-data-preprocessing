# Tích hợp công cụ S3 SDK với vStorage

Để xem hướng dẫn tích hợp công cụ S3 SDK với vStorage, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn thư mục **Tích hợp.**
3. Chọn biểu tượng **S3 SDK**.
4. Tại mục **Cấp quyền**, bạn cần điền thông tin cần thiết để cấu hình SDK S3 của bạn nhằm tích hợp với vStorage bao gồm:
   1. Chọn một **Region** chứa project mà bạn muốn thực hiện truy xuất dữ liệu tới trong danh sách các Region mà chúng tôi cung cấp.
   2. Chọn một **Project** trong danh sách các project đang tồn tại trong Region mà bạn chọn trước đó. Nếu danh sách project hiển thị chưa đầy đủ, bạn có thể chọn , chúng tôi sẽ tải lại danh sách project mới nhất tại thời điểm bạn thực hiện hành động này.
   3. Chọn một **Access key** trong danh sách các access key đang tồn tại thuộc project mà bạn chọn trước đó.
   4. Nhập **Secret key** tương ứng của **Access key** vừa chọn. Cặp access key và secret key được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Nhấn vào đây để vào vIAM và quản lý s3 keys](https://hcm-3.console.vngcloud.vn/iam/vstorage-credentials/s3) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý S3 keys. Để biết thêm thông tin về S3 keys, hãy xem tại [Khởi tạo vStorage Credentials](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/).
5. Sau khi hoàn tất chọn cấu hình **Cấp quyền**, chọn **Tích hợp S3 SDK** để chuyển tới màn hình **Cấu hình**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Tích hợp S3 SDK** để cập nhật cách sử dụng theo thông số mới của bạn. Bạn có thể xem hướng dẫn cách tích hợp S3 SDK với các ngôn ngữ khác nhau theo các bước bên dưới:
   1. Chọn một **Ngôn ngữ** lập trình mà bạn muốn tích hợp trong danh sách các ngôn ngữ lập trình mà chúng tôi cung cấp, bao gồm: Java, Python, Golang, Ruby, C#, NodeJS.
   2. Chọn một **Thư viện** mà bạn muốn thực hiện giao tiếp với các API của server.

Bên dưới là danh sách các ngôn ngữ, thư viện và phiên bản (version) tương ứng mà chúng tôi cung cấp cho bạn để tích hợp với vStorage:

| STT       | Ngôn ngữ                    | Thư viện | Phiên bản (version) hỗ trợ    |
| --------- | --------------------------- | -------- | ----------------------------- |
| 1         | Java                        | AWS SDK  | Java 8 và AWS SDK 1.11.163    |
| MinIO SDK | Java 8 và MinIO 8.5.2       |          |                               |
| 2         | Python                      | AWS SDK  | Python 3.8 và Boto3 1.26.110  |
| MinIO SDK | Python 3.8 và Minio 7.1.14  |          |                               |
| 3         | Golang                      | AWS SDK  | Go 1.17.10                    |
| MinIO SDK | Go 1.17.10                  |          |                               |
| 4         | Ruby                        | AWS SDK  | Ruby 2.7.0                    |
| 5         | C#                          | AWS SDK  | .Net 7.0 và AWS SDK 3.7.4     |
| MinIO SDK | .Net 7.0 và Minio 4.0.7     |          |                               |
| 6         | NodeJS                      | AWS SDK  | Node 16.15.0                  |
| MinIO SDK | Node 16.15.0                |          |                               |

\


6\. Lúc này màn hình hướng dẫn chi tiết cách tích hợp S3 SDK cho các ngôn ngữ được hiển thị. Phần nội dung hướng dẫn tích hợp được hiển thị theo 4 mục:

a. **Thiết lập cho hướng dẫn này**: Chứa các hướng dẫn về cài đặt và kết nối the**o ngôn ngữ và thư viện mà bạn chọn.**

b. **Viết code**: Chứa mã nguồn tích hợp cho từng tính năng khi **Làm việc với container** và **Làm việc với object** theo **ngôn ngữ** và **thư viện** mà bạn chọn.

c. **Build và deployment**: Chứa hướng dẫn xây dựng và khởi chạy S3 SDK theo **ngôn ngữ** và **thư viện** mà bạn chọn.

d. **Tải code mẫu**: Mục để bạn chọn tải về toàn bộ mã nguồn hướng dẫn từ 3 mục bên trên theo **ngôn ngữ** và **thư viện** mà bạn chọn.

Bạn có thể chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/59805522/image2023-5-18\_13-37-39.png?version=1\&modificationDate=1689229600000\&api=v2) hoặc ![](https://docs.vngcloud.vn/download/thumbnails/59805522/image2023-5-18\_13-37-55.png?version=1\&modificationDate=1689229601000\&api=v2) để mở hay đóng từng mục này. Đối với mỗi bước chúng tôi đều cung cấp cho bạn mã nguồn mẫu theo thông tin xác thực bạn đã nhập trước đó và ngôn ngữ hay thư viện bạn đã chọn, bạn có thể chọn Sao chép mã nguồn tại mỗi tính năng bằng cách chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/59805522/image2023-5-18\_13-38-42.png?version=1\&modificationDate=1689229601000\&api=v2) tại mỗi đoạn mã nguồn hoặc bạn cũng có thể tìm kiếm nhanh mã nguồn hỗ trợ cho tính năng mà bạn mong muốn bằng cách chọn tính năng trong phần **Chỉ mục** (góc phải màn hình). Nếu bạn muốn tải xuống toàn bộ mã nguồn hướng dẫn tích hợp S3 SDK cho ngôn ngữ này, hãy chọn **Tải về** trong mục **Tải code mẫu**. Như vậy là bạn đã hoàn thành việc tích hợp S3 SDK bằng 1 trong cách ngôn ngữ mà bạn mong muốn

<figure><img src="../../../../../.gitbook/assets/Tich_hop_S3_SDK.gif" alt=""><figcaption></figcaption></figure>
