# Development Mode

Hiện tại, vCDN đang hỗ trợ cơ chế “nhà phát triển” (Development Mode). Cơ chế này sẽ cho phép tất cả các request sẽ được bỏ qua cache và đi trực tiếp đến origin nhằm kiểm tra dữ liệu ở origin một cách trực tiếp:

<figure><img src="../../.gitbook/assets/image (237).png" alt=""><figcaption></figcaption></figure>

## Tổng quan

Cơ chế "Nhà phát triển" của vCDN là một tính năng đặc biệt cho phép các nhà phát triển kiểm tra, gỡ lỗi và cập nhật nội dung trên website một cách nhanh chóng và hiệu quả. Khi kích hoạt chế độ này, tất cả các yêu cầu từ người dùng sẽ không được lưu vào cache của vCDN mà sẽ được chuyển trực tiếp đến máy chủ gốc (origin). Điều này giúp đảm bảo rằng mọi thay đổi được thực hiện trên máy chủ gốc sẽ được phản ánh ngay lập tức trên website, mà không cần chờ đợi quá trình làm mới cache.

#### Một số lưu ý khi sử dụng chế độ "Nhà phát triển":

* **Chỉ sử dụng trong môi trường phát triển:** Chế độ này nên được sử dụng trong môi trường phát triển hoặc thử nghiệm. Không nên bật chế độ này trên môi trường sản xuất vì nó có thể làm giảm hiệu suất của website.
* **Tắt chế độ khi đã hoàn thành:** Sau khi hoàn thành việc phát triển và kiểm thử, hãy nhớ tắt chế độ này để tận dụng lợi ích của caching.
* **Ảnh hưởng đến hiệu suất:** Việc tắt cache có thể làm tăng tải lên máy chủ gốc, đặc biệt là khi có nhiều yêu cầu đồng thời.
* **Không phù hợp với các website có lưu lượng lớn:** Với các website có lưu lượng truy cập cao, việc tắt cache hoàn toàn có thể gây ra tình trạng quá tải máy chủ.

## Chi tiết

* Trên vCDN, để bật/ tắt chế độ Nhà phát triển, bạn có thể chọn **Enable/ Disable** tại mục Development mode:

<figure><img src="../../.gitbook/assets/image (8) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
