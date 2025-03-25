# Object Storage S3

## Tổng quan

**S3 Origin** là một loại nguồn dữ liệu (origin) được sử dụng trong vCDN để phục vụ nội dung từ các dịch vụ lưu trữ đối tượng (object storage) như **Amazon S3** hoặc các giải pháp tương tự (ví dụ: vStorage của VNG Cloud). Khi sử dụng S3 Origin, nội dung được phân phối từ bucket S3 của bạn thông qua mạng lưới CDN, giúp cải thiện tốc độ truy cập và giảm tải cho hệ thống gốc.

## Chi tiết

Hiện tại, vCDN đang hỗ trợ bạn kết nối trực tiếp đến origin là Object Storage thuộc chuẩn S3-compatible. Để thực hiện kết nối, bạn cần nhập các thông tin, bao gồm:&#x20;

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Access key:** Access key được lấy từ hệ thống Object Storage của bạn.
* **Secret key:** Secret key tương ứng với Access key đã nhập bên trên.
* **Bucket:** Tên của bucket chứa nội dung trên S3.
* **Region:** Region nơi bucket của bạn được lưu trữ.
* **Endpoint**: Đường dẫn URL kết nối với dịch vụ S3.
* **S3 Signature:** Signature của S3 được sử dụng. Bạn có thể chọn sử dụng Signature v2 hoặc v4.
* **Use SSL:** Chọn sử dụng SSL để mã hóa kết nối giữa vCDN và S3 Origin.
