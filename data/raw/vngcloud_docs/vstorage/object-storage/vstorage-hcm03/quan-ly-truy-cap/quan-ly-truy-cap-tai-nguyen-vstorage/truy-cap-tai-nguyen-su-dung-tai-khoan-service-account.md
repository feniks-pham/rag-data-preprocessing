# Truy cập tài nguyên sử dụng tài khoản Service Account

Để truy cập vào tài nguyên của bạn trên dịch vụ lưu trữ vStorage, bạn có thể truy cập thông qua vStorage Portal, vStorage API, Swift Rest API, S3 Rest API và 3rd party softwares. Đối với các kênh truy cập vStorage API, Swift Rest API, S3 Rest API hoặc 3rd party softwares, bạn sử dụng tài khoản người Service Account để truy cập vào. Nếu bạn chưa có tài khoản Service Account, bạn vui lòng tham khảo tại [Tài khoản Service Account](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/).

* Để sử dụng tài khoản Service Account truy cập vào tài nguyên vStorage thông qua vStorage API, S3 Rest API, Swift Rest API, hãy xem chi tiết tại [API developers](../../api-developers/).
* Để sử dụng tài khoản Service Account truy cập vào tài nguyên vStorage thông qua 3rd party softwares hãy xem chi tiết tại [3rd party softwares](../../3rd-party-softwares/).

#### Bên dưới là một ví dụ minh họa việc sử dụng Service Account truy cập vào tài nguyên vStorage thông qua công cụ S3cmd: <a href="#truycaptainguyensudungtaikhoanserviceaccount-benduoilamotviduminhhoaviecsudungserviceaccounttruycapv" id="truycaptainguyensudungtaikhoanserviceaccount-benduoilamotviduminhhoaviecsudungserviceaccounttruycapv"></a>

1. Tạo tài khoản S3 key theo hướng dẫn tại [Khởi tạo S3 key](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-s3-key.md).&#x20;
2. Nếu tài khoản S3 key vừa tạo đang có trạng thái **Restriction by vIAM = ON** thì bạn tiếp tục tạo tài khoản Service Account theo hướng dẫn tại [Khởi tạo tài khoản Service Account](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md), [Khởi tạo policy cho Service Account](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-policy-cho-service-account.md), [Liên kết tài khoản Service Account với policy tương ứng](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/lien-ket-tai-khoan-service-account-voi-policy-tuong-ung.md). Ngược lại nếu tài khoản S3 key có trạng thái **Restriction by vIAM = OFF** thì chuyển tới bước 4.&#x20;
3. Liên kết tài khoản S3 key với Service Account theo hướng dẫn tại [Liên kết S3 key, Swift user với tài khoản Service Account tương ứng](../quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/lien-ket-s3-key-swift-user-voi-tai-khoan-service-account-tuong-ung.md).
4. Tích hợp S3 key này với ứng dụng S3cmd. Chi tiết như sau:
   1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
   2. Chọn thư mục **Tích hợp.**
   3. Chọn biểu tượng **S3cmd**.
   4. Tại mục **Cấp quyền**, bạn cần điền thông tin cần thiết để cấu hình S3cmd của bạn nhằm tích hợp với vStorage bao gồm:
      1. Chọn một **Region** chứa project mà bạn muốn thực hiện truy xuất dữ liệu tới trong danh sách các Region mà chúng tôi cung cấp.
      2. Chọn một **Project** trong danh sách các project đang tồn tại trong Region mà bạn chọn trước đó. Nếu danh sách project hiển thị chưa đầy đủ, bạn có thể chọn , chúng tôi sẽ tải lại danh sách project mới nhất tại thời điểm bạn thực hiện hành động này.
      3. Chọn một **Access key** mà bạn vừa tạo ở bước 1 bên trên.
      4. Nhập **Secret key** tương ứng của **Access key** vừa chọn. Cặp access key và secret key được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Nhấn vào đây để vào vIAM và quản lý s3 keys](https://hcm-3.console.vngcloud.vn/iam/vstorage-credentials/s3) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý S3 keys.&#x20;
   5. Sau khi hoàn tất chọn cấu hình **Cấp quyền**, chọn **Cấu hình S3cmd** để chuyển tới màn hình **Cấu hình**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Cấu hình S3cmd** để cập nhật cách sử dụng theo thông số mới của bạn. Bạn có thể xem hướng dẫn cách cài đặt, cấu hình S3cmd ngay trên màn hình này.
   6. Nhấn **Tải tệp tin cấu hình** về máy tính cá nhân. Tệp tin tải về sẽ có tên mặc định là **s3cnf.s3cfg**.

***

#### **Nếu bạn sử dụng hệ điều hành Windows, tiếp tục thực hiện theo các bước bên dưới để hoàn thành việc tích hợp S3cmd với vStorage:**  <a href="#truycaptainguyensudungtaikhoanserviceaccount-neubansudunghedieuhanhwindows-tieptucthuchientheocacbuo" id="truycaptainguyensudungtaikhoanserviceaccount-neubansudunghedieuhanhwindows-tieptucthuchientheocacbuo"></a>

1. Lưu tệp tin cấu hình **s3cnf.s3cfg** tải về vào thư mục **C:\Users\\\[User]\AppData\Roaming.**
2. Đổi tên tệp tin từ **s3cnf.s3cfg** thành **s3cmd.ini**
3. Tải và cài đặt **Python** theo hướng dẫn tại [https://www.python.org/](https://www.python.org/) trên máy tính cá nhân.
4. Tải ứng dụng **S3cmd** theo hướng dẫn tại [https://s3tools.org/download](https://s3tools.org/download) về máy tính cá nhân.
5. **Extract** tệp tin ứng dụng **S3cmd** vừa tải xuống.
6. Mở **Command Prompt** trên máy tính hoặc nhấn tổ hợp phím **Windows + R** sau đó nhập **cmd** và nhấn **Enter.**
7. Trong **Command Prompt**, thực hiện **trỏ** tới thư mục **s3cmd** vừa **extract**. Cú pháp trỏ thư mục như sau: cd <đường dẫn tới thư mục s3cmd>
8. Lúc này, bạn đã có thể sử dụng các cú pháp để lấy **danh sách container, tải lên object**, cũng như thực hiện các thao tác khác tại [3rd party softwares](../../3rd-party-softwares/).

<figure><img src="../../../../../.gitbook/assets/Tich_hop_s3cmd.gif" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/Su_dung_S3cmd.gif" alt=""><figcaption></figcaption></figure>

Để biết thêm thông tin về cách tích hợp, sử dụng các công cụ khác, vui lòng xem thêm tại [3rd party softwares](../../3rd-party-softwares/).

\
