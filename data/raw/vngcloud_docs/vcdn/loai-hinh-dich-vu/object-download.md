# Object Download

## **Tổng quan** <a href="#objectdownload-tongquan" id="objectdownload-tongquan"></a>

Dịch vụ Object Download của VNG Cloud giúp doanh nghiệp: tối ưu chi phí, đảm bảo sự linh hoạt, dễ dàng tương thích với đa dạng thiết bị đầu cuối, từ đó, tăng mức độ hài lòng của khách hàng với dịch vụ với khả năng phân tích dữ liệu đa chiều theo thời gian thực.

***

## **Sơ đồ hoạt động** <a href="#objectdownload-cochephanphoidulieu" id="objectdownload-cochephanphoidulieu"></a>

<figure><img src="../../.gitbook/assets/image (216).png" alt=""><figcaption></figcaption></figure>

***

## **Cơ Chế Phân Phối Dữ Liệu** <a href="#objectdownload-cochephanphoidulieu" id="objectdownload-cochephanphoidulieu"></a>

* **Dữ liệu đầu vào**:
  * Hệ thống **Origin Gateway** của VNGCloud sẽ kết nối đến **origin server** hoặc **storage của khách hàng** để lấy nội dung được yêu cầu từ phía client. Nội dung này có thể ở bất kỳ định dạng nào, ví dụ: `.js`, `.css`, hình ảnh, font (`.tff`), v.v.
  * Nếu nội dung có kích thước lớn, **Origin Gateway** sẽ chia nội dung thành các request nhỏ (5MB) và tải đồng thời (byte-range download). Điều này giúp tăng tốc độ tải và phục vụ người dùng ngay khi nhận được dữ liệu đầu tiên.
  * Dữ liệu từ **Origin Gateway** sau đó sẽ được phân phối tới các **Edge servers** để phục vụ người dùng.
* **Dữ liệu đầu ra**:
  * **Hỗ trợ giao thức HTTPS**:
    * Mặc định, tất cả CDN được tạo trên hệ thống đều hỗ trợ SSL trên domain của CDN.
    * Khách hàng cũng có thể upload **Certificate** của riêng mình để sử dụng với domain tùy chỉnh. (Xem thêm hướng dẫn tại phần Quản lý Certificate).
  * **Hỗ trợ HTTP/2**:
    * HTTP/2 giúp tăng tốc độ kết nối và truyền dữ liệu trên trình duyệt, mang lại trải nghiệm mượt mà hơn.

***

## **Tính Năng Dịch Vụ** <a href="#objectdownload-tinhnangdichvu" id="objectdownload-tinhnangdichvu"></a>

* **Hỗ trợ kết nối trực tiếp đến Origin:** Hệ thống vCDN hỗ trợ kết nối trực tiếp đến các nguồn dữ liệu dạng Object Storage sử dụng chuẩn giao thức S3-compatible. Điều này giúp khách hàng dễ dàng tích hợp dữ liệu từ các dịch vụ lưu trữ đám mây phổ biến hoặc từ vStorage.
* **Tùy chỉnh cơ chế caching:**&#x63;ho phép người dùng cấu hình mức độ caching dữ liệu tại các Edge Server, phù hợp với từng loại nội dung.
* **Hỗ trợ Origin khi tạo CDN:** Hệ thống vCDN cho phép định nghĩa nguồn dữ liệu từ Object Storage hoặc Origin Server do khách hàng chỉ định. Điều này cung cấp sự linh hoạt trong việc tích hợp dữ liệu từ nhiều nguồn khác nhau.
* **Hỗ trợ HTTPS:** Mặc định tất cả các CDN được tạo ra đều hỗ trợ HTTPS để bảo mật dữ liệu. Người dùng cũng có thể **tự upload chứng chỉ SSL** để sử dụng với domain riêng.
* **Tự động Redirect từ HTTP sang HTTPS**: Hỗ trợ tính năng tự động chuyển hướng tất cả các yêu cầu HTTP sang HTTPS nhằm tăng cường bảo mật và cải thiện trải nghiệm người dùng.
* **Bảo mật link đầu ra:** Hỗ trợ các cơ chế bảo mật nâng cao để bảo vệ nội dung, bao gồm: CORS, Whitelist/ Blacklist IP, Geo Block, HTTP Referer Block,...
* **Hỗ trợ chế độ nhà phát triển (Development Mode):** Tính năng này cho phép tạm thời tắt caching tại Edge Server để hỗ trợ giai đoạn thử nghiệm hoặc kiểm tra nội dung trong khi phát triển. Mọi yêu cầu sẽ được trả về trực tiếp từ Origin, giúp cập nhật nội dung ngay lập tức mà không cần xóa cache.

***

## **Hướng dẫn khởi tạo Object Download CDN** <a href="#objectdownload-huongdankhoitaoobjectdownloadcdn" id="objectdownload-huongdankhoitaoobjectdownloadcdn"></a>

### **Bước 1: Tạo Object Download**

Đầu tiên, bạn cần thực hiện khởi tạo một Object Download theo hướng dẫn sau:&#x20;

1. Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)
2. Chọn mục **Object Download**, sau đó chọn **Create new.**

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Tiếp tục thực hiện nhập/chọn:&#x20;

* **CDN Info:**&#x20;
  * **CDN Name:** Nhập tên định danh cho CDN mà bạn muốn tạo.&#x20;

<figure><img src="../../.gitbook/assets/image (11) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Origin:**&#x20;
  * **HTTP Origin**: Server hỗ trợ giao thức HTTP.
    * **Fail-Over Error Code:** Danh sách các mã lỗi HTTP (ví dụ: 500, 502, 503, 504) mà nếu xảy ra sẽ kích hoạt chuyển đổi dự phòng (fail-over) đến Origin khác.
    * **Origin Load Balancing:** Cơ chế cân bằng tải giữa các Origin Server được chỉ định.
    * **Origin Host Header:** Header được sử dụng khi gửi yêu cầu từ vCDN đến Origin Server.
    * **IP Address:** Địa chỉ IP của Origin Server (ví dụ: IPv4 như 1.1.1.1 hoặc IPv6).
    * **Weight:** Định nghĩa mức ưu tiên của từng Origin Server khi cân bằng tải (giá trị càng cao, lưu lượng nhận được càng nhiều).
  * **S3 Origin**: Nguồn dữ liệu trên hệ thống Object Storage chuẩn S3-compatible.
    * **Access key:** Access key được lấy từ hệ thống Object Storage của bạn.&#x20;
    * **Secret key:** Secret key tương ứng với Access key đã nhập bên trên.
    * **Bucket:** Tên của bucket chứa nội dung trên S3.
    * **Region:** Region nơi bucket của bạn được lưu trữ.
    * **Endpoint**: Đường dẫn URL kết nối với dịch vụ S3.&#x20;
    * **S3 Signature:** Signature của S3 được sử dụng. Bạn có thể chọn sử dụng Signature v2 hoặc v4.
    * **Use SSL:** Chọn sử dụng SSL để mã hóa kết nối giữa vCDN và S3 Origin.
  * **Host Origin**: Dữ liệu từ một host cụ thể.
    * **Origin Host Header:** Header được gửi tới Origin Server trong yêu cầu HTTP.
    * **Use SSL:** Kích hoạt SSL để mã hóa kết nối với Host Origin.
    * **Host Origin**

<figure><img src="../../.gitbook/assets/image (12) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (13) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (14) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   **Security:**

    * **HTTPS (HTTP/2)**: Bật hoặc tắt chế độ bảo mật HTTPS cho luồng CDN. Bạn có thể tạo mới một **Certificate** bằng cách chọn **Add new**.
    * **HTTP Strict Transport Security (HSTS)**: Áp dụng chính sách bảo mật web cho trang web của bạn, gửi các header HSTS với tất cả các request HTTPS. Nếu cấu hình sai, HSTS có thể làm cho trang web của bạn không thể truy cập được trong một thời gian dài.
    * **Max Age Header (max-age):** Xác định thời gian các header HSTS được lưu trữ trong trình duyệt.
    * **Apply HSTS policy to subdomains (includeSubDomains):** Mọi domain sẽ kế thừa các header HSTS giống nhau. Nếu bất kỳ domain nào của bạn không hỗ trợ HTTPS, chúng sẽ không thể truy cập được.
    * **Preload:** Cho phép trình duyệt tải trước cấu hình HSTS tự động. Preload có thể làm cho một trang web không hỗ trợ HTTPS hoàn toàn không thể truy cập được.
    * **Relative Canonical URL:** Một URL canonical cho phép bạn thông báo cho các công cụ tìm kiếm rằng các URL tương tự thực sự là cùng một nội dung. Điều này hữu ích khi bạn có sản phẩm hoặc nội dung có thể được tìm thấy trên nhiều URL hoặc thậm chí nhiều trang web.&#x20;
    * **No-Sniff Header:** Gửi header "X-Content-Type-Options: nosniff" để ngăn Internet Explorer và Google Chrome không kiểm tra MIME khác với Content-Type đã khai báo.

    <figure><img src="../../.gitbook/assets/image (15) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (16) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Token Configuration**:
      * **Token Type**: Chọn loại token dùng để xác thực người xem. Bạn có thể chọn token type Akamai, SBD hoặc VNG.

    <figure><img src="../../.gitbook/assets/image (17) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Access Filter:**
      * **IP Address CIDR**: Giới hạn cho phép/ từ chối truy cập dựa trên địa chỉ IP bằng cách chọn **Allow**/ **Block** và nhập địa chỉ IP hoặc CIDR tương ứng.
      * **HTTP Referer**: Giới hạn cho phép/ từ chối truy cập từ các website cụ thể bằng cách chọn **Allow/ Block** và nhập domain tương ứng.
      * **Geo Location:** Giới hạn cho phép, từ chối truy cập theo quốc gia/khu vực bằng cách chọn **Allow/ Block** và nhập mã Geo Location tương ứng. Bạn có thể tham khảo giá trị country code tương ứng tại [https://en.wikipedia.org/wiki/List\_of\_ISO\_3166\_country\_codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    * **CORS Configuration**
      * **Simple**: Khi chọn Simple, bạn chỉ cần chỉ định các domain cụ thể được phép truy cập thông qua **Allow Origin.**
      * **Advance**: Khi chọn Advance, ngoài việc chỉ định domain cụ thể, bạn cần cấu hình chi tiết hơn về **Allow Header, Allow Method, Expose Header, Allow Credentials** được phép.

    <figure><img src="../../.gitbook/assets/image (841).png" alt=""><figcaption></figcaption></figure>

    * **Always Use HTTPS:** Bật hoặc tắt tính năng tự động chuyển hướng tất cả các yêu cầu HTTP sang HTTPS nhằm tăng cường bảo mật và cải thiện trải nghiệm người dùng.
    * **Small Object:** Khi bạn bật option này, nếu nội dung có kích thước lớn, **Origin Gateway** sẽ chia nội dung thành các request nhỏ (5MB) và tải đồng thời (byte-range download). Điều này giúp tăng tốc độ tải và phục vụ người dùng ngay khi nhận được dữ liệu đầu tiên.
    * **Minimum TLS Version**: Phiên bản thấp nhất của giao thức TLS được phép sử dụng. Chúng tôi đang hỗ trợ các giao thức TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3. Bạn hãy chọn sử dụng các phiên bản cao (TLS 1.2 hoặc 1.3) để đảm bảo tính bảo mật.

    <figure><img src="../../.gitbook/assets/image (18) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Caching:**
      * **Caching Level**: Xác định mức độ cache của CDN. Với VOD, vCDN đang cung cấp 3 mức độ cache bao gồm: URL without query string only, Skip Query String of URL, URL With Query String.
      * **Server Cache Expiration (TTL):** Khoảng thời gian mà hệ thống vCDN sẽ lưu trữ tài nguyên của bạn trong bộ nhớ cache. Trong khoảng thời gian này, hệ thống vCDN sẽ không truy cập server gốc mà phản hồi yêu cầu từ bộ nhớ cache của vCDN. Bạn có thể chọn thời gian này từ 30 phút cho tới 1 năm tùy theo nhu cầu cho hệ thống của bạn.
      * **Browser Cache Expiration:** Thời gian vCDN yêu cầu trình duyệt của người dùng lưu trữ tệp trong bộ nhớ cache cục bộ.&#x20;
      * **Development mode:** Chế độ nhà phát triển. Tính năng này cho phép tạm thời tắt caching tại Edge Server để hỗ trợ giai đoạn thử nghiệm hoặc kiểm tra nội dung trong khi phát triển. Mọi yêu cầu sẽ được trả về trực tiếp từ Origin, giúp cập nhật nội dung ngay lập tức mà không cần xóa cache.

    <figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Page Rules:** Tính năng này giúp khách hàng tối ưu các điều kiện và các tùy chọn để giúp website thể hiện được nhiều mục đích khác nhau. Để tạo Page rules, vui lòng chọn **Create Page Rule**, popup sẽ hiện ra, lúc này bạn cần chọn:&#x20;
      * **URL pattern:** cần áp dụng pagerule, hỗ trợ kiểu khai báo “\*” đại diện cho một chuỗi nhiều ký tự. Ví dụ: /trang\_landing\_cu.html. Sau khi nhập URL pattern, bạn hãy chọn **Add new rule**. Mỗi Rules khi thỏa điệu kiện đúng URI được request sẽ có thể tùy chọn thực thi một trong các hành động sau:
        * Always Use HTTPS
        * Server Cache TTL
        * Browser Cache TTL
        * Bypass Cache By Cookie
        * Bypass Cache By Device Type
        * Forwarding URL
        * Response Header Override
        * Resolve Origin Override
        * Origin Base Directory
        * Deny Access
      * Chọn **Save changes** để lưu thay đổi.

    <figure><img src="../../.gitbook/assets/image (843).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (844).png" alt="" width="375"><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="348"><figcaption></figcaption></figure>

    4. Chọn **Submit** để hoàn thành việc tạo Object Download.

### **Bước 2: Tải tệp xuống**

Sau khi bạn đã thực hiện khởi tạo xong Object Download, bạn có thể thực hiện tải xuống file theo các link dưới đây:

```
https:// <CDN Domain>/<đường dẫn file trên origin>
```

Nếu bạn sử dụng S3 origin, lưu ý đường dẫn file trên origin của bạn sẽ bao gồm cả tên bucket.&#x20;

Ví dụ:&#x20;

```
https:// <CDN Domain>/<tên bucket>/<tên object>
```
