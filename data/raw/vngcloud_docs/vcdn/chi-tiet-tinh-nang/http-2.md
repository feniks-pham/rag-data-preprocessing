# Cryptography

## Tổng quan

**Crypto** trong CDN là một nhóm các thiết lập và công cụ giúp quản lý các tính năng mã hóa và bảo mật liên quan đến website.

## Chi tiết

Khi khởi tạo một Web Accelerator trên hệ thống vCDN, tại mục Crypto, bạn cần chọn/ nhập:

<figure><img src="../../.gitbook/assets/image (14) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Trong đó:&#x20;

* **HTTPS (HTTP/2)**: Bật hoặc tắt chế độ bảo mật HTTPS cho luồng CDN. Bạn có thể tạo mới một **Certificate** bằng cách chọn **Add new**.
* **HTTP Strict Transport Security (HSTS)**: thông báo cho trình duyệt người dùng rằng họ chỉ có thể kết nối với máy chủ Web thông qua giao thức HTTPS. Điều này có thể được sử dụng để ngăn chặn một số cuộc tấn công hạ cấp kết nối từ HTTPS xuống HTTP. Bật tính năng này để bảo vệ người truy cập website khách hàng.
* **Max Age Header (max-age):** Xác định thời gian các header HSTS được lưu trữ trong trình duyệt.
* **Apply HSTS policy to subdomains (includeSubDomains):** Mọi domain sẽ kế thừa các header HSTS giống nhau. Nếu bất kỳ domain nào của bạn không hỗ trợ HTTPS, chúng sẽ không thể truy cập được.
* **Preload:** Cho phép trình duyệt tải trước cấu hình HSTS tự động. Preload có thể làm cho một trang web không hỗ trợ HTTPS hoàn toàn không thể truy cập được.
* **Relative Canonical URL:** Một URL canonical cho phép bạn thông báo cho các công cụ tìm kiếm rằng các URL tương tự thực sự là cùng một nội dung. Điều này hữu ích khi bạn có sản phẩm hoặc nội dung có thể được tìm thấy trên nhiều URL hoặc thậm chí nhiều trang web.
* **No-Sniff Header:** Gửi header "X-Content-Type-Options: nosniff" để ngăn Internet Explorer và Google Chrome không kiểm tra MIME khác với Content-Type đã khai báo.
