# CNAME

## Tổng quan <a href="#cname-tongquan" id="cname-tongquan"></a>

CNAME trong CDN là một loại bản ghi DNS (Hệ thống tên miền) được sử dụng để **định hướng lưu lượng truy cập từ tên miền của bạn đến máy chủ CDN**.&#x20;

***

## **Cách hoạt động**

* **Bước 1:** Khi người dùng truy cập tên miền của bạn, trình duyệt của họ sẽ gửi yêu cầu đến máy chủ DNS.
* **Bước 2:** Máy chủ DNS sẽ tìm kiếm bản ghi CNAME cho tên miền của bạn.
* **Bước 3:** Nếu bản ghi CNAME tồn tại, máy chủ DNS sẽ trả về địa chỉ IP của máy chủ CDN.
* **Bước 4:** Trình duyệt của người dùng sẽ gửi yêu cầu đến máy chủ CDN.
* **Bước 5:** Máy chủ CDN sẽ trả về nội dung được yêu cầu cho trình duyệt.

***

## **Lợi ích của việc sử dụng CNAME**

* **Cải thiện hiệu suất:** CDN lưu trữ nội dung của bạn trên nhiều máy chủ trên toàn thế giới. Khi người dùng truy cập nội dung của bạn, họ sẽ được kết nối với máy chủ gần nhất, giúp cải thiện tốc độ tải trang.
* **Tăng độ tin cậy:** CDN có khả năng chịu lỗi cao. Nếu một máy chủ CDN gặp sự cố, các máy chủ khác sẽ tiếp tục cung cấp nội dung của bạn.
* **Giảm tải cho máy chủ gốc của bạn:** CDN có thể xử lý một lượng lớn lưu lượng truy cập, giúp giảm tải cho máy chủ gốc của bạn.

***

## **Khởi tạo CDN Name**

Để sử dụng CNAME trong CDN, bạn có thể thực hiện thiết lập CNAMEs tại trường thông tin CDN Name trên thư mục CDN Info khi thực hiện tạo 1 CDN bất kỳ trên hệ thống vCDN.

<figure><img src="../../.gitbook/assets/image (234).png" alt=""><figcaption></figcaption></figure>
