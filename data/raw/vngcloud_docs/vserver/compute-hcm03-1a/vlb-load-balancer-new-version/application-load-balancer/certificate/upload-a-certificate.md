# Upload a certificate

Để có thể sử dụng chứng chỉ SSL bạn phải có sẵn chứng chỉ SSL hoặc sử dụng chứng chỉ SSL miễn phí được cung cấp bởi Let’s Encrypt. Các certificate được VNG CLOUD lưu tại một nơi bảo mật, an toàn, hệ thống lưu trữ các certificate được mã hóa và không thể truy cập bởi bất cứ ai bao gồm cả các nhân viên của VNG CLOUD.

Trình quản lý Certificate hỗ trợ tải lên và quản lý hai loại Certificate như sau:

* **TLS/SSL Certificate**
* **CA Certificate**

### 1. Hướng dẫn tải lên TLS/SSL Certificate <a href="#uploadacertificate-1.huongdantailentls-sslcertificate" id="uploadacertificate-1.huongdantailentls-sslcertificate"></a>

* **Truy cập trình quản lý Certificate theo đường dẫn:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/certificate**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/certificate)
* **Nhấn nút "Tải lên Certificate / Upload Certificate"**
* **Một cửa sổ giao diện bật lên cho phép bạn điền thông tin Certificate, bao gồm**
  * **Tên gợi nhớ**: Khuyến khích sử dụng tên miền làm tên gợi nhớ
  * **Chọn loại Certificate TLS/SSL**
  * **Điền Certificate Input bao gồm**:
    * [x] **Nội dung Certificate:** Là Server Certificate domain của bạn (thường có đuôi \*.crt), có định dạng chuẩn PEM
    * [x] **Thông tin Private Key:** Là khóa riêng của certificate trên (thường có đuôi \*.key), có định dạng chuẩn PEM
  *   **Điền Certificate Chain:** Là chuỗi certificate bao gồm server certificate và intermediate certificate (nếu có), có định dạng chuẩn PEM.

      _Chú ý thứ tự add chain sẽ như sau:_

      &#x20;            \---BEGIN CERTIFICATE---\
      &#x20;            \[Your certificate]\
      &#x20;            \---END CERTIFICATE---\
      &#x20;            \---BEGIN CERTIFICATE---\
      &#x20;            \[Intermidate#1 certificate]\(option)\
      &#x20;            \---END CERTIFICATE---\
      &#x20;            \---BEGIN CERTIFICATE---\
      &#x20;           \[Intermidate#2 certificate]\(option)\
      &#x20;            \---END CERTIFICATE---
  * **Passphrase**: Trong trường hợp khóa riêng (private key) có mật khẩu thì cần nhập mật khẩu của khóa riêng, ngược lại bỏ trống trường này.
  * **Expiration**: Ngày hết hạn của Certificate.
*   **Nhấn nút "Tải lên / Upload" tại góc dưới bên phải của cửa sổ giao diện để hoàn tất tải lên.**



### 2. Hướng dẫn tải lên CA Certificate

* **Truy cập trình quản lý Certificate theo đường dẫn:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/certificate**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/certificate)
* **Nhấn nút "Tải lên Certificate / Upload Certificate"**
* **Một cửa sổ giao diện bật lên cho phép bạn điền thông tin Certificate, bao gồm**
  * **Tên gợi nhớ**: Khuyến khích sử dụng tên miền làm tên gợi nhớ
  * **Chọn loại Certificate CA**
  *   **Điền Certificate Input bao gồm**:

      * **Nội dung Certificate:** Là Server Certificate domain của bạn (thường có đuôi \*.crt), có định dạng chuẩn PEM.
      * **Expiration**: Ngày hết hạn của Certificate.


  * **Nhấn nút "Tải lên / Upload" tại góc dưới bên phải của cửa sổ giao diên để hoàn tất tải lên.**
