# Tạo kênh Live Transcode

Để tạo kênh Live Transcode, hãy làm theo hướng dẫn sau:

## Cài đặt Sigma Media Server

Đầu tiên, bạn cần cài đặt Sigma Media Server theo các bước tại [đây](../cai-dat-sigma-media-server.md).

## Khởi tạo và cấu hình dịch vụ Media Service để livestream.&#x20;

**Bước 1:** Sau khi đã cài đặt **Sigma Media Server** thành công, bạn hãy truy cập vào [https://portal.sigma.video/apps](https://portal.sigma.video/apps) với email mà bạn đã đăng ký sử dụng dịch vụ trước đó.

<figure><img src="../../../../.gitbook/assets/image (647).png" alt=""><figcaption></figcaption></figure>

**Bước 2:** Bạn chọn xổ menu **Product** xuống và chọn mục **Livestream**

<figure><img src="../../../../.gitbook/assets/image (648).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Tiếp tục bạn chọn tab **Channel**

<figure><img src="../../../../.gitbook/assets/image (649).png" alt=""><figcaption></figcaption></figure>

**Bước 4:** Chọn nút **Add channel** ở góc phải

<figure><img src="../../../../.gitbook/assets/image (650).png" alt=""><figcaption></figcaption></figure>

**Bước 5:** Màn hình **Create Channel** hiển thị, bạn configure các tham số của kênh, chọn server xử lý trong mục **Advance configuration**.

<figure><img src="../../../../.gitbook/assets/image (651).png" alt=""><figcaption></figcaption></figure>

**Bước 6:** Quay trở lại màn hình list **Channel** chúng ta sẽ thấy kênh vừa được tạo nằm trong danh sách. Click vào tên kênh để vào màn hình detail của kênh.

<figure><img src="../../../../.gitbook/assets/image (652).png" alt=""><figcaption></figcaption></figure>

**Bước 7:** Trong màn hình detail của kênh ta sẽ thấy thông tin RTMP Stream URL, Quý khách thay thế **Stream URL** trên màn hình bằng _<mark style="color:blue;">**rtmp://\<server\_public\_ip>:1935/livestream**</mark>_ để stream.

<figure><img src="../../../../.gitbook/assets/image (653).png" alt=""><figcaption></figcaption></figure>

## Khởi tạo và cấu hình dịch vụ vCDN.

**Bước 1:** Bạn thực hiện truy cập [VNG Cloud – ](https://vcdn.vngcloud.vn/)[vCDN](https://vcdn.vngcloud.vn/)[ Portal](https://vcdn.vngcloud.vn/)

**Bước 2:** Khởi tạo một domain CDN dành cho **Live Streaming** theo hướng dẫn tại [đây](../../live-streaming.md).

**Bước 3**: Thực hiện trỏ **Origin** của CDN về **server Sigma** đang xử lý livestream

<figure><img src="../../../../.gitbook/assets/image (631).png" alt=""><figcaption></figcaption></figure>
