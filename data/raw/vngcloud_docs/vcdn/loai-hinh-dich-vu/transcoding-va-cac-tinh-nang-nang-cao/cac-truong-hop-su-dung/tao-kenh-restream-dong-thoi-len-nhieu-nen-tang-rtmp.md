# Tạo kênh Restream đồng thời lên nhiều nền tảng (RTMP)

Để tạo kênh Restream đồng thời trên nhiều nền tảng, hãy làm theo hướng dẫn sau:

## Cài đặt Sigma Media Server

Đầu tiên, bạn cần cài đặt Sigma Media Server theo các bước tại [đây](../cai-dat-sigma-media-server.md).

## Khởi tạo và cấu hình dịch vụ Media Service để livestream.&#x20;

**Bước 1:** Sau khi đã cài đặt **Sigma Media Server** thành công, bạn hãy truy cập vào [https://portal.sigma.video/apps](https://portal.sigma.video/apps) với email mà bạn đã đăng ký sử dụng dịch vụ trước đó.

<figure><img src="../../../../.gitbook/assets/image (647).png" alt=""><figcaption></figcaption></figure>

**Bước 2:** Bạn chọn xổ menu **Product** xuống và chọn mục **Media Live.** Tiếp tục bạn chọn tab **Channel -> Transcode channels**

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Chọn nút **Add** ở góc phải. Màn hình **Create Transcode Channel** hiển thị, trong tab Config, bạn cần nhập các thông tin cơ bản cho kênh bao gồn **Name** và **Name Modifier**

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 4:** Tiếp tục thực hiện configure đầu vào ở tab **Input**

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 5:** Tại màn hình **Create Input Transcode**, bạn chọn kiểu đầu vào **RTMP** như sau:

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 6:** Sau khi đóng màn hình **Create** bên trên, hệ thống sẽ hiển thị **danh sách** các đầu vào của kênh. Tại đây, bạn cần **chọn** các đầu vào tương ứng:

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 7:** Tại tab **profile**, bạn nhập các profile của đầu vào bằng cách chọn **Add profile** nếu đã có sẵn hoặc chọn **New profile** để tạo profile mới

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 8:** Trong ví dụ này, chúng tôi sẽ thêm một profile **video** định dạng 1080p và một **audio** 44\_1khz

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 9:** Tiếp theo, bạn cấu hình các luồng nhận stream mà bạn mong muốn stream tới

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 10:** Nhập thông tin **RTMP** sau đó nhấn **Submit**

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Tương tự như trên, quý khách có thể stream đồng thời tới nhiều RTMP khác bằng cách thêm cấu hình tại mục Target.**

**Sau khi thực hiện các bước bên trên, tại mục Input sẽ hiển thị thông tin RTMP nhận luồng stream. Quý khách thực hiện stream thông qua đường dẫn tại mục này.**
