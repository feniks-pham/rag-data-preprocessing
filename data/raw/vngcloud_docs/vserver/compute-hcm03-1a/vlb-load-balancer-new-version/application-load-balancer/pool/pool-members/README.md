# Pool Members

Pool Member là thành viên trong một nhóm máy chủ (Pool) trên Load Balancer, và chúng chịu trách nhiệm phục vụ các yêu cầu từ người dùng hoặc các thiết bị khác thông qua Load Balancer. Dưới đây là giải thích về cơ chế hoạt động của Pool Member và các thuộc tính quan trọng:

**Weight**

* **Giải thích**: Trọng số quy định mức độ ưu tiên của mỗi Pool Member trong việc xử lý các yêu cầu. Các Member có trọng số cao sẽ nhận được nhiều yêu cầu hơn so với các Member có trọng số thấp.
* **Ví dụ**: Nếu bạn có hai Member với trọng số 3 và 1, Member có trọng số 3 sẽ nhận được khoảng 75% yêu cầu, trong khi Member có trọng số 1 chỉ nhận được khoảng 25%.

**Port**

* **Giải thích**: Port mà Member sẽ lắng nghe để xử lý các yêu cầu đến. Port này thường liên quan đến dịch vụ cụ thể mà Member cung cấp.
* **Ví dụ**: Nếu bạn có một ứng dụng web chạy trên Member, bạn có thể sử dụng cổng 80 cho HTTP và cổng 443 cho HTTPS.

**Monitor Port**

* **Giải thích**: Đây là Port mà Load Balancer sử dụng để kiểm tra sức khỏe của Member. Load Balancer sẽ gửi các yêu cầu kiểm tra đến Port này để đảm bảo rằng Member đang hoạt động đúng cách. Nếu không chỉ định cụ thể Monitor Port, thì mặc định Monitor Port = Port dùng để nhận request đến.
* **Ví dụ**: Nếu bạn muốn kiểm tra sức khỏe của một máy chủ web, bạn có thể sử dụng cổng 80 hoặc 443 để kiểm tra tính khả dụng.

**Backup Role**

* **Giải thích**: Thuộc tính này xác định vai trò của Member trong một Pool. Có hai vai trò chính: Primary (Chính) và Backup (Sao lưu). Member Chính nhận các yêu cầu chính thức từ người dùng, trong khi Member Sao lưu chỉ nhận yêu cầu khi Member Chính không khả dụng.
* **Ví dụ**: Nếu bạn có hai Member trong một Pool, Member A có vai trò Chính và Member B có vai trò Sao lưu, yêu cầu sẽ được gửi đến Member A trước. Nếu Member A không khả dụng, Load Balancer sẽ chuyển yêu cầu đến Member B.

Nhìn chung, cơ chế này cho phép bạn tùy chỉnh cách Load Balancer phân phối lưu lượng truy cập giữa các Member trong một Pool. Bằng cách sử dụng trọng số, bạn có thể cân nhắc sự phân phối của lưu lượng. Đồng thời, vai trò Sao lưu giúp đảm bảo tính khả dụng và độ tin cậy của hệ thống khi Member Chính gặp sự cố.

#### &#x20;<a href="#poolmembers-cacchudelienquan" id="poolmembers-cacchudelienquan"></a>

\
