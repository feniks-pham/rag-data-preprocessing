# Tích hợp công cụ S3cmd với vStorage

Để xem hướng dẫn tích hợp công cụ S3cmd với vStorage, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn thư mục **Integration.**
3. Chọn biểu tượng **S3cmd**.
4. Tại mục **Authentication**, bạn cần điền thông tin cần thiết để cấu hình S3cmd của bạn nhằm tích hợp với vStorage bao gồm:
   1. Chọn một **Project** trong danh sách các project đang tồn tại trong Region mà bạn chọn trước đó. Nếu danh sách project hiển thị chưa đầy đủ, bạn có thể chọn , chúng tôi sẽ tải lại danh sách project mới nhất tại thời điểm bạn thực hiện hành động này.
   2. Chọn một **Access key** trong danh sách các access key đang tồn tại thuộc project mà bạn chọn trước đó.
   3. Nhập **Secret key** tương ứng của **Access key** vừa chọn. Cặp access key và secret key được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Nhấn vào đây để vào vIAM và quản lý s3 keys](https://hcm-3.console.vngcloud.vn/iam/vstorage-credentials/s3) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý S3 keys. Để biết thêm thông tin về S3 keys, hãy xem tại [Khởi tạo vStorage Credentials](../../../vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/).
5. Sau khi hoàn tất chọn cấu hình **Authentication**, chọn **Cấu hình S3cmd** để chuyển tới màn hình **Configuration**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Cấu hình S3cmd** để cập nhật cách sử dụng theo thông số mới của bạn. Bạn có thể xem hướng dẫn cách cài đặt, cấu hình S3cmd ngay trên màn hình này. Chi tiết tham khảo thêm tại: [Tích hợp vStorage.](https://vstorage.console.vngcloud.vn/integration/integration)
6. Chọn **Download Configuration file.**

#### **Nếu bạn sử dụng hệ điều hành Windows, tiếp tục thực hiện theo các bước bên dưới để hoàn thành việc tích hợp S3cmd với vStorage:**  <a href="#tichhopcongcus3cmdvoivstorage-neubansudunghedieuhanhwindows-tieptucthuchientheocacbuocbenduoidehoant" id="tichhopcongcus3cmdvoivstorage-neubansudunghedieuhanhwindows-tieptucthuchientheocacbuocbenduoidehoant"></a>

1. Lưu tệp tin cấu hình **s3cnf.s3cfg** tải về vào thư mục **C:\Users\\\[User]\AppData\Roaming.**
2. Đổi tên tệp tin từ **s3cnf.s3cfg** thành **s3cmd.ini**
3. Tải và cài đặt **Python** theo hướng dẫn tại [https://www.python.org/](https://www.python.org/) trên máy tính cá nhân.
4. Tải ứng dụng **S3cmd** theo hướng dẫn tại [https://s3tools.org/download](https://s3tools.org/download) về máy tính cá nhân.
5. **Extract** tệp tin ứng dụng **S3cmd** vừa tải xuống.
6. Mở **Command Prompt** trên máy tính hoặc nhấn tổ hợp phím **Windows + R** sau đó nhập **cmd** và nhấn **Enter.**
7. Trong **Command Prompt**, thực hiện **trỏ** tới thư mục **s3cmd** vừa **extract**. Cú pháp trỏ thư mục như sau: cd <đường dẫn tới thư mục s3cmd>
8. Lúc này, bạn đã có thể sử dụng các cú pháp để lấy **danh sách bucket, tải lên object**, cũng như thực hiện các thao tác khác tại [3rd party softwares](../../../vstorage-hcm03/3rd-party-softwares/).

<figure><img src="../../../../../.gitbook/assets/image (865).png" alt=""><figcaption></figcaption></figure>
