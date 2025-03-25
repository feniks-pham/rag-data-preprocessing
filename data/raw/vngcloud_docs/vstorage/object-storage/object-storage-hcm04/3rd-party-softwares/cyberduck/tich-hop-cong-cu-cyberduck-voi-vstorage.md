# Tích hợp công cụ Cyberduck với vStorage

Để xem hướng dẫn tích hợp công cụ Cyberduck với vStorage, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn thư mục **Integration.**
3. Chọn biểu tượng **Cyberduck**.
4. Tại mục **Authentication**, bạn cần điền thông tin cần thiết để cấu hình Cyberduck của bạn nhằm tích hợp với vStorage bao gồm:
   1. Chọn một **Project** trong danh sách các project đang tồn tại trong Region mà bạn chọn trước đó. Nếu danh sách project hiển thị chưa đầy đủ, bạn có thể chọn , chúng tôi sẽ tải lại danh sách project mới nhất tại thời điểm bạn thực hiện hành động này.
   2. Chọn một **Access key** trong danh sách các access key đang tồn tại thuộc project mà bạn chọn trước đó.
   3. Nhập **Secret key** tương ứng của **Access key** vừa chọn. Cặp access key và secret key được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Click here to visit vIAM and manage S3 keys](https://hcm-3.console.vngcloud.vn/iam/vstorage-credentials/s3) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý S3 keys. Để biết thêm thông tin về S3 keys, hãy xem tại [Khởi tạo vStorage Credentials](../../../vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/).
5. Sau khi hoàn tất chọn cấu hình **Authentication**, chọn **Tích hợp cyberduck** để chuyển tới màn hình **Configuration**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Tích hợp cyberduck** để cập nhật cách sử dụng theo thông số mới của bạn. Bạn có thể xem hướng dẫn cách cài đặt, cấu hình Cyberduck ngay trên màn hình này. Chi tiết tham khảo thêm tại: [Tích hợp vStorage.](https://vstorage.console.vngcloud.vn/integration/integration)
6. Chọn **Download configuration file.**

***

#### **Tiếp tục thực hiện theo các bước bên dưới để hoàn thành việc tích hợp S3cmd với vStorage:**  <a href="#tichhopcongcucyberduckvoivstorage-tieptucthuchientheocacbuocbenduoidehoanthanhviectichhops3cmdvoivst" id="tichhopcongcucyberduckvoivstorage-tieptucthuchientheocacbuocbenduoidehoanthanhviectichhops3cmdvoivst"></a>

1. Tải công cụ người dùng **Cyberduck** tại đây [https://cyberduck.io/download/](https://cyberduck.io/download/).
2. Mở ứng dụng **Cyberduck**.&#x20;
3. Chọn **Open Connection** hoặc **Bookmark + New Bookmark**.

<figure><img src="../../../../../.gitbook/assets/image (530).png" alt="" width="375"><figcaption></figcaption></figure>

4\. Nhập thông tin kết nối bao gồm:

* **Protocol**: HCM04. Khi bạn chọn phương thức này, các thông tin Server, Port, URL sẽ tự động được ghi nhận và hiển thị.
* **Access key**: nhập S3 access key mà bạn tạo từ vStorage cũng chính là thông tin access key lấy từ bước 4 bên trên.
* **Secret key**: nhập S3 access key mà bạn tạo từ vStorage cũng chính là thông tin access key lấy từ bước 4 bên trên.

<figure><img src="../../../../../.gitbook/assets/image (871).png" alt=""><figcaption></figcaption></figure>

5\. Chọn **Connect**.

6\. Bây giờ **Cyberduck** đã kết nối thành công tới **vStorage**. Bạn đã có thể sử dụng Cyberduck để truy xuất tới vStorage, tham khảo thêm tại Sử dụng công cụ Cyberduck.

<figure><img src="../../../../../.gitbook/assets/image (532).png" alt="" width="375"><figcaption></figcaption></figure>
