# Web Accelerator

## **Tổng quan** <a href="#webaccelerator-tongquan" id="webaccelerator-tongquan"></a>

Web Accelerator là giải pháp giúp tăng tốc độ hiển thị nội dung và trải nghiệm người dùng.

***

## **Sơ đồ hoạt động** <a href="#webaccelerator-cochephanphoidulieu" id="webaccelerator-cochephanphoidulieu"></a>

<figure><img src="../../.gitbook/assets/image (219).png" alt=""><figcaption></figcaption></figure>

***

## **Cơ Chế Phân Phối Dữ Liệu** <a href="#webaccelerator-cochephanphoidulieu" id="webaccelerator-cochephanphoidulieu"></a>

Dịch vụ Web Accelerator cache tất cả các đối tượng đi qua nó không chỉ bao gồm các nội dung tĩnh như Image, javascript, css mà còn có cả HTML code và API. Bên cạnh đó còn thực hiện các cơ chế tự động tối ưu hóa source code và hình ảnh.

***

## **Tính Năng Dịch Vụ** <a href="#webaccelerator-tinhnangdichvu" id="webaccelerator-tinhnangdichvu"></a>

* **Hỗ trợ CNAME**: Cho phép bạn sử dụng tên miền tùy chỉnh.
* **Hỗ trợ tùy chỉnh Origin**: Cho phép cấu hình nguồn gốc dữ liệu.
* **Tối ưu hóa kích thước file thiết bị đầu cuối**: Giảm kích thước file để tải nhanh hơn.
* **Chế độ bảo mật HSTS**: Bảo vệ trang web khỏi các cuộc tấn công.
* **Tùy chỉnh các tính năng cache**: Quản lý bộ nhớ đệm theo nhu cầu.
* **Tự động redirect từ HTTP sang HTTPS**: Chuyển hướng an toàn.
* **Đổi các link HTTP sang HTTPS trong source code**: Đảm bảo tất cả các liên kết đều an toàn.
* **Chỉnh sửa CDN đã tạo**: Cho phép thay đổi cấu hình CDN.

***

## **Hướng dẫn khởi tạo Web Accelerator CDN** <a href="#webaccelerator-cachtaowebacceleratorcdn" id="webaccelerator-cachtaowebacceleratorcdn"></a>

### **Bước 1: Tạo Web Accelerator**

Đầu tiên, bạn cần thực hiện khởi tạo một Web Accelerator theo hướng dẫn sau:&#x20;

1. Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)
2. Chọn mục **Web Accelerator**, sau đó chọn **Create new.**
3. Tiếp tục thực hiện nhập/chọn:&#x20;

* **CDN Info:**&#x20;
  * **CDN Name:** Nhập tên định danh cho CDN mà bạn muốn tạo.&#x20;

<figure><img src="../../.gitbook/assets/image (19) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **HTTP Origin**: Server hỗ trợ giao thức HTTP.
  * **Fail-Over Error Code:** Danh sách các mã lỗi HTTP (ví dụ: 500, 502, 503, 504) mà nếu xảy ra sẽ kích hoạt chuyển đổi dự phòng (fail-over) đến Origin khác.
  * **Origin Load Balancing:** Cơ chế cân bằng tải giữa các Origin Server được chỉ định.
  * **Origin Host Header:** Header được sử dụng khi gửi yêu cầu từ vCDN đến Origin Server.
  * **IP Address:** Địa chỉ IP của Origin Server (ví dụ: IPv4 như 1.1.1.1 hoặc IPv6).
  * **Weight:** Định nghĩa mức ưu tiên của từng Origin Server khi cân bằng tải (giá trị càng cao, lưu lượng nhận được càng nhiều).

<figure><img src="../../.gitbook/assets/image (20) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   **Crypto:**

    * **HTTPS (HTTP/2)**: Bật hoặc tắt chế độ bảo mật HTTPS cho luồng CDN. Bạn có thể tạo mới một **Certificate** bằng cách chọn **Add new**.
    * **HTTP Strict Transport Security (HSTS)**: Áp dụng chính sách bảo mật web cho trang web của bạn, gửi các header HSTS với tất cả các request HTTPS. Nếu cấu hình sai, HSTS có thể làm cho trang web của bạn không thể truy cập được trong một thời gian dài.
    * **Max Age Header (max-age):** Xác định thời gian các header HSTS được lưu trữ trong trình duyệt.
    * **Apply HSTS policy to subdomains (includeSubDomains):** Mọi domain sẽ kế thừa các header HSTS giống nhau. Nếu bất kỳ domain nào của bạn không hỗ trợ HTTPS, chúng sẽ không thể truy cập được.
    * **Preload:** Cho phép trình duyệt tải trước cấu hình HSTS tự động. Preload có thể làm cho một trang web không hỗ trợ HTTPS hoàn toàn không thể truy cập được.
    * **Relative Canonical URL:** Một URL canonical cho phép bạn thông báo cho các công cụ tìm kiếm rằng các URL tương tự thực sự là cùng một nội dung. Điều này hữu ích khi bạn có sản phẩm hoặc nội dung có thể được tìm thấy trên nhiều URL hoặc thậm chí nhiều trang web.&#x20;
    * **No-Sniff Header:** Gửi header "X-Content-Type-Options: nosniff" để ngăn Internet Explorer và Google Chrome không kiểm tra MIME khác với Content-Type đã khai báo.

    <figure><img src="../../.gitbook/assets/image (21) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **Caching:**
  * **Caching Level**: Xác định mức độ cache của CDN. Với VOD, vCDN đang cung cấp 3 mức độ cache bao gồm: URL without query string only, Skip Query String of URL, URL With Query String.
  * **Server Cache Expiration (TTL):** Khoảng thời gian mà hệ thống vCDN sẽ lưu trữ tài nguyên của bạn trong bộ nhớ cache. Trong khoảng thời gian này, hệ thống vCDN sẽ không truy cập server gốc mà phản hồi yêu cầu từ bộ nhớ cache của vCDN. Bạn có thể chọn thời gian này từ 30 phút cho tới 1 năm tùy theo nhu cầu cho hệ thống của bạn.
  * **Browser Cache Expiration:** Thời gian vCDN yêu cầu trình duyệt của người dùng lưu trữ tệp trong bộ nhớ cache cục bộ.&#x20;
  * **Development mode:** Chế độ nhà phát triển. Tính năng này cho phép tạm thời tắt caching tại Edge Server để hỗ trợ giai đoạn thử nghiệm hoặc kiểm tra nội dung trong khi phát triển. Mọi yêu cầu sẽ được trả về trực tiếp từ Origin, giúp cập nhật nội dung ngay lập tức mà không cần xóa cache.

<figure><img src="../../.gitbook/assets/image (23) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **File Size Optimization:**
  * **Image Optimizer:** Tối ưu hóa kích thước và định dạng hình ảnh, từ đó giúp giảm thời gian tải trang và traffic.
  * **Auto Minify:** Thu gọn HTML, CSS, JS bằng cách loại bỏ khoảng cách và chú thích.
  * **Brotli:** Thuật toán nén nội dung hiệu quả hơn Gzip. Sử dụng nén chuẩn Brotli giúp giảm kích thước file truyền tải, cải thiện tốc độ và tiết kiệm traffic.
*   **Page Rules:** Tính năng này giúp khách hàng tối ưu các điều kiện và các tùy chọn để giúp website thể hiện được nhiều mục đích khác nhau. Để tạo Page rules, vui lòng chọn **Create Page Rule**, popup sẽ hiện ra, lúc này bạn cần chọn:&#x20;

    * **URL pattern:** cần áp dụng pagerule, hỗ trợ kiểu khai báo “\*” đại diện cho một chuỗi nhiều ký tự. Ví dụ: /trang\_landing\_cu.html. Sau khi nhập URL pattern, bạn hãy chọn **Add new rule**. Mỗi Rules khi thỏa điệu kiện đúng URI được request sẽ có thể tùy chọn thực thi một trong các hành động sau:
      * Always Use HTTPS
      * Auto Minify
      * Automatic HTTPS Rewrites
      * Server Cache TTL
      * Browser Cache TTL
      * Bypass Cache By Cookie
      * Cache By Device Type
      * Bypass Cache By Device Type
      * Forwarding URL
      * Response Header Override
      * Brotli
      * Gzip
      * Resolve Origin Override
      * Origin Base Directory
      * Deny Access
    * Chọn **Save changes** để lưu thay đổi.

    <figure><img src="../../.gitbook/assets/image (843).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (844).png" alt="" width="375"><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="348"><figcaption></figcaption></figure>

    4. Chọn **Submit** để hoàn thành việc tạo Web Accelerator.

### **Bước 2: Kiểm tra, theo dõi và giám sát**&#x20;

Sau khi đã khởi tạo xong Web Accelerator, bạn có thể thực hiện kiểm tra và theo dõi tốc độ tải trang qua vCDN.
