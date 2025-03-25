# Video On Demand Streaming

## **Tổng quan** <a href="#videoondemandstreaming-tongquan" id="videoondemandstreaming-tongquan"></a>

Đảm bảo trải nghiệm người dùng tốt nhất khi lựa chọn và xem video trên các thiết bị qua internet.

Dịch vụ VOD của VNG Cloud giúp doanh nghiệp:

* Tối ưu chi phí.
* Đảm bảo sự linh hoạt, dễ dàng tương thích với đa dạng thiết bị đầu cuối.
* Tăng mức độ hài lòng của khách hàng với dịch vụ.
* Phân tích dữ liệu đa chiều theo thời gian thực.

***

## **Sơ đồ hoạt động** <a href="#videoondemandstreaming-cochephanphoidulieu" id="videoondemandstreaming-cochephanphoidulieu"></a>

<figure><img src="../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

***

## **Cơ Chế Phân Phối Dữ Liệu** <a href="#videoondemandstreaming-cochephanphoidulieu" id="videoondemandstreaming-cochephanphoidulieu"></a>

### **Quy trình xử lý dữ liệu đầu vào**

Hệ thống vCDN thực hiện kết nối đến **Storage của khách hàng** để lấy nội dung, cụ thể:

* **Các định dạng hỗ trợ đầu vào**:
  * **MP4** (video), **MP3** (audio).
  * **HLS** và **MpegDash** (chuẩn streaming).
* **Tùy chọn xử lý với định dạng gốc**:
  * **MP4/MP3**: Được **chuyển đổi thành HLS**, định dạng phổ biến để phát trên các thiết bị OTT (Over-the-Top).
  * **HLS/MpegDash**: Nếu dữ liệu đã có định dạng này, hệ thống giữ nguyên (không chuyển đổi).
* **Media Segment**:
  * Tùy chọn độ dài mỗi media segment khi packaging thành HLS.

### **Quy trình xử lý dữ liệu trên Media Preparation Server**

* **Chuyển đổi định dạng**:\
  Hệ thống đọc file đầu vào từ origin và chuyển đổi:
  * **MP4/MP3 → HLS**.
  * Đọc file SMIL (nếu có) để tạo chuẩn **Adaptive Bitrate (ABR)**.
* **Hỗ trợ SMIL cho Adaptive Bitrate**:
  * SMIL là file đặc tả chứa thông tin bitrate và các phiên bản video tương ứng.
  * Hệ thống đọc file SMIL từ origin và chuyển đổi thành HLS ABR, đảm bảo trải nghiệm mượt mà trên nhiều tốc độ mạng.
* **Phân phối dữ liệu**: Sau khi chuyển đổi, các file được đẩy đến **Edge Server** để phục vụ người xem.

### **Dữ liệu đầu ra**

Hệ thống vCDN cung cấp các chuẩn phát phổ biến, hỗ trợ giao thức HTTPS và tính năng Adaptive Bitrate. Chi tiết như sau:

* **Các đường dẫn chuẩn đầu ra**
  *   **MP4**: Phát trực tiếp file từ origin (MP4 Progressive Streaming).

      ```perl
      https://<CDN Domain>/<đường dẫn file MP4 trên origin>
      ```
  *   **HLS**:Dùng cho nội dung phân đoạn hoặc có SMIL hỗ trợ ABR.

      ```perl
      https://<CDN Domain>/<đường dẫn file MP4/SMIL trên origin>/index.m3u8
      ```
  *   **MpegDash**:

      ```perl
      https://<CDN Domain>/<đường dẫn file manifest trên origin>
      ```
* **Hỗ trợ HTTPS**
  * **Mặc định**: Tất cả CDN đều được hỗ trợ HTTPS qua chứng chỉ SSL của hệ thống.
  * **Tùy chỉnh**: Người dùng có thể upload chứng chỉ SSL riêng để sử dụng với domain tùy chỉnh.
* **Hỗ trợ Adaptive Bitrate (HLS SMIL ABR)**
  *   URL hỗ trợ ABR thông qua file SMIL:

      ```bash
      https://<CDN Domain>/<Đường dẫn tới file SMIL trên origin>/index.m3u8
      ```

## **Tính Năng Dịch Vụ** <a href="#videoondemandstreaming-tinhnangdichvu" id="videoondemandstreaming-tinhnangdichvu"></a>

* **Hỗ trợ kết nối trực tiếp đến Origin:** Hệ thống vCDN hỗ trợ kết nối trực tiếp đến các nguồn dữ liệu dạng Object Storage sử dụng chuẩn giao thức S3-compatible. Điều này giúp khách hàng dễ dàng tích hợp dữ liệu từ các dịch vụ lưu trữ đám mây phổ biến hoặc từ vStorage.
* **Tùy chỉnh cơ chế caching:**&#x63;ho phép người dùng cấu hình mức độ caching dữ liệu tại các Edge Server, phù hợp với từng loại nội dung.
* **Hỗ trợ Origin khi tạo CDN:** Hệ thống vCDN cho phép định nghĩa nguồn dữ liệu từ Object Storage hoặc Origin Server do khách hàng chỉ định. Điều này cung cấp sự linh hoạt trong việc tích hợp dữ liệu từ nhiều nguồn khác nhau.
* **Hỗ trợ HTTPS:** Mặc định tất cả các CDN được tạo ra đều hỗ trợ HTTPS để bảo mật dữ liệu. Người dùng cũng có thể **tự upload chứng chỉ SSL** để sử dụng với domain riêng.
* **Tự động Redirect từ HTTP sang HTTPS**: Hỗ trợ tính năng tự động chuyển hướng tất cả các yêu cầu HTTP sang HTTPS nhằm tăng cường bảo mật và cải thiện trải nghiệm người dùng.
* **Bảo mật link đầu ra:** Hỗ trợ các cơ chế bảo mật nâng cao để bảo vệ nội dung, bao gồm: CORS, Whitelist/ Blacklist IP, Geo Block, HTTP Referer Block,...
* **Hỗ trợ chế độ nhà phát triển (Development Mode):** Tính năng này cho phép tạm thời tắt caching tại Edge Server để hỗ trợ giai đoạn thử nghiệm hoặc kiểm tra nội dung trong khi phát triển. Mọi yêu cầu sẽ được trả về trực tiếp từ Origin, giúp cập nhật nội dung ngay lập tức mà không cần xóa cache.
* **Multi Audio Selection:**&#x20;
  * **Chức năng tách Audio**:
    * Hỗ trợ tách và chọn các track audio khác nhau trong một file MP4 nếu file chứa nhiều định dạng audio (ví dụ: nhiều ngôn ngữ hoặc phiên bản).
    * Tính năng này tương thích với **Adaptive Bitrate (ABR)** và sử dụng file SMIL để định nghĩa.
  *   **Cú pháp URL Multi Audio Selection (cùng với ABR)**:

      ```bash
      https://<CDN Domain>/<Đường dẫn tới file SMIL trên VNGCloud Storage/Origin>/index.m3u8
      ```

***

## **Hướng dẫn khởi tạo VOD CDN** <a href="#videoondemandstreaming-huongdankhoitaovodcdn" id="videoondemandstreaming-huongdankhoitaovodcdn"></a>

### **Bước 1: Tạo VOD**

Đầu tiên, bạn cần thực hiện khởi tạo một VOD theo hướng dẫn sau:&#x20;

1. Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)
2. Chọn mục **Video On Demand**, sau đó chọn **Create new.**

<figure><img src="../../.gitbook/assets/image (21) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Tiếp tục thực hiện nhập/chọn:&#x20;

* **CDN Info:**&#x20;
  * **CDN Name:** Nhập tên định danh cho CDN mà bạn muốn tạo.&#x20;
  * **VOD Type:** Chọn loại VOD type mà bạn mong muốn sử dụng. Hiện tại vCDN đang hỗ trợ 3 loại VOD bao gồm:&#x20;
    * **CDN Packaging:** Hệ thống vCDN sẽ packaging media từ file video gốc của khách hàng
    * **Origin Packaging:** Origin của khách hàng tự packaging, vCDN chỉ phục vụ
    * **MP4:** vCDN phục vụ trực tiếp file mp4 gốc từ origin cho end-user
  * **Segment Size:** Chọn thời gian "băm" của các file "ts" với loại dịch vụ VoD là CDN Packaging.

<figure><img src="../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   **Security:**

    * **HTTPS (HTTP/2)**: Bật hoặc tắt chế độ bảo mật HTTPS cho luồng CDN. Bạn có thể tạo mới một **Certificate** bằng cách chọn **Add new**.
    * **Always Use HTTPS:** Bật hoặc tắt tính năng tự động chuyển hướng tất cả các yêu cầu HTTP sang HTTPS nhằm tăng cường bảo mật và cải thiện trải nghiệm người dùng.
    * **Minimum TLS Version**: Phiên bản thấp nhất của giao thức TLS được phép sử dụng. Chúng tôi đang hỗ trợ các giao thức TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3. Bạn hãy chọn sử dụng các phiên bản cao (TLS 1.2 hoặc 1.3) để đảm bảo tính bảo mật.
    * **Token Configuration**:
      * **Token Type**: Chọn loại token dùng để xác thực người xem. Bạn có thể chọn token type Akamai, SBD hoặc VNG.

    <figure><img src="../../.gitbook/assets/image (10) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Access Filter:**
      * **IP Address CIDR**: Giới hạn cho phép/ từ chối truy cập dựa trên địa chỉ IP bằng cách chọn **Allow**/ **Block** và nhập địa chỉ IP hoặc CIDR tương ứng.
      * **HTTP Referer**: Giới hạn cho phép/ từ chối truy cập từ các website cụ thể bằng cách chọn **Allow/ Block** và nhập domain tương ứng.
      * **Geo Location:** Giới hạn cho phép, từ chối truy cập theo quốc gia/khu vực bằng cách chọn **Allow/ Block** và nhập mã Geo Location tương ứng. Bạn có thể tham khảo giá trị country code tương ứng tại [https://en.wikipedia.org/wiki/List\_of\_ISO\_3166\_country\_codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    * **CORS Configuration**
      * **Simple**: Khi chọn Simple, bạn chỉ cần chỉ định các domain cụ thể được phép truy cập thông qua **Allow Origin.**
      * **Advance**: Khi chọn Advance, ngoài việc chỉ định domain cụ thể, bạn cần cấu hình chi tiết hơn về **Allow Header, Allow Method, Expose Header, Allow Credentials** được phép.

    <figure><img src="../../.gitbook/assets/image (841).png" alt=""><figcaption></figcaption></figure>

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

    4. Chọn **Submit** để hoàn thành việc tạo VOD.

### **Bước 2: Truy cập VOD**

Sau khi bạn đã thực hiện khởi tạo xong VOD, bạn có thể truy cập các CDN VOD theo các link dưới đây:

* **MP4:**&#x20;

```
https:// <CDN Domain>/<đường dẫn file MP4 trên origin>
```

* **MP3:**&#x20;

```
https:// <CDN Domain>/<đường dẫn file MP3 trên origin >
```

* **HLS:**&#x20;

```
https:// <CDN Domain>/<đường dẫn file MP4/SMIL trên origin>/index.m3u8
```

* MpegDash:&#x20;

```
https:// <CDN Domain>/<đường dẫn file manifest trên origin>
```
