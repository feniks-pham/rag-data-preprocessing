# Tích hợp công cụ S3 Browser với vStorage

Để tích hợp công cụ S3 Browser với vStorage, bạn có thể thực hiện theo hướng dẫn bên dưới:&#x20;

1. Tải công cụ người dùng S3 Browser tại đây [https://s3browser.com/download.aspx](https://s3browser.com/download.aspx).
2. Mở ứng dụng **S3 Browser** → **Account** → **Add new account**

<figure><img src="../../../../../.gitbook/assets/image (536).png" alt=""><figcaption></figcaption></figure>

3\. Điền các thông tin đăng nhập như sau:

* **Display name:** Tên hiển thị của account.
* **Account type**: Chọn **S3 Compatible Storage.**
* **REST Endpoint**: Đường dẫn đến vstorage, [hcm01.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/) (region HCM01 - Hồ Chí Minh) hoặc [han01.vstorage.vngcloud.vn](http://han01.vstorage.vngcloud.vn/) (Region HAN01 - Hà Nội).
* **Access Key ID & Secret Access Key:** Là cặp key được cấp trên Portal vStorage.

4\. Chọn **Use Secure transfer (SSL/TLS)** vì vStorage chỉ hỗ trợ kênh truyền đã được mã hoá (HTTPS, port 443) để đảm bảo an toàn dữ liệu, không hỗ trợ kênh truyền không mã hoá (HTTP, port 80).

5\. Cuối cùng là click chọn phần cài đặt nâng cao **Advanced S3-Compatible Storage Settings** ở góc dưới - bên trái cửa sổ.

<figure><img src="../../../../../.gitbook/assets/image (537).png" alt=""><figcaption></figcaption></figure>

* **Signature version**: vStorage hỗ trợ cả 2 loại Signature V2 và Signature V4, nhưng khuyến nghị là sử dụng Signature V4 vì AWS S3 đã không còn hỗ trợ Signature V2
* **Addressing model**: vStorage hỗ trợ cả 2 loại là Path Style và Virtual hosted style. Khác nhau giữa 2 loại là đường dẫn của request khi gửi lên gateway của vstorage, đối với path style là [https://hcm01.vstorage.vngcloud.vn](https://hcm01.vstorage.vngcloud.vn/)/v1/AUTH\_{project\_id}/{bucket}/{file} còn đối với Virtual hosted style sẽ là https://{bucket}.[hcm01.vstorage.vngcloud.vn/{file](http://hcm01.vstorage.vngcloud.vn/%7Bfile)}
* Chọn **Override storage region**: điền vào giá trị của Default region = HCM01 hoặc HAN01.
* **Close → Save changes.**

<figure><img src="../../../../../.gitbook/assets/image (538).png" alt=""><figcaption></figcaption></figure>

6\. Sau đó nếu S3 Browser kết nối thành công sẽ ra kết quả như sau:

<figure><img src="../../../../../.gitbook/assets/image (539).png" alt=""><figcaption></figcaption></figure>
