# Certificate trong vCloudstack

VNG Cloud cung cấp trình quản lý Certificate, cho phép người dùng tải lên và quản lý các chứng chỉ của mình. Chúng tôi hỗ trợ quản lý 2 loại chứng chỉ chính:&#x20;

* **TLS/SSL Certificate**
* **CA Certificate**

**1. Chứng chỉ TLS/SSL (TLS/SSL Certificate):**

* **Chứng chỉ TLS/SSL (TLS/SSL Certificate)** là một tài liệu số hóa chứa thông tin về khóa công khai và thông tin xác thực của một trang web hoặc máy chủ. Chúng được sử dụng để thiết lập kết nối an toàn giữa máy tính của người dùng và máy chủ web, đảm bảo tính bảo mật và toàn vẹn của dữ liệu truyền qua mạng.
* **Chức năng của Chứng chỉ TLS/SSL:** Chứng chỉ TLS/SSL đảm bảo rằng thông tin như mật khẩu, dữ liệu cá nhân và giao dịch tài chính được mã hóa và bảo vệ trước các mối đe dọa bảo mật. Nó cũng xác minh tính xác thực của máy chủ web, giúp người dùng biết họ đang truy cập trang web đúng và không phải là một trang web giả mạo.
* **Loại Chứng chỉ TLS/SSL:** Có nhiều loại chứng chỉ TLS/SSL, bao gồm chứng chỉ miễn phí, chứng chỉ tự ký và chứng chỉ được cấp bởi cơ quan chứng thực uy tín (CA).

**2. Chứng chỉ CA (Certificate Authority):**

* **Chứng chỉ CA (Certificate Authority)** là một tổ chức hoặc công ty chịu trách nhiệm cấp phát, xác thực và quản lý Chứng chỉ TLS/SSL. CA là một bên đáng tin cậy có vai trò kiểm tra và đảm bảo tính xác thực của các đơn vị yêu cầu Chứng chỉ TLS/SSL.
* **Chức năng của Chứng chỉ CA:** Chứng chỉ CA chứng thực danh tính của các trang web và máy chủ bằng cách ký và cấp phát các Chứng chỉ TLS/SSL. Nó đảm bảo rằng thông tin trong Chứng chỉ TLS/SSL là xác thực và an toàn.
* **Tính chất của Chứng chỉ CA:** Các CA lớn thường được tin tưởng rộng rãi và được các trình duyệt web và hệ thống máy tính công nhận. Khi một trang web sử dụng Chứng chỉ TLS/SSL do CA cấp, trình duyệt sẽ hiển thị biểu tượng mở ổ khóa hoặc xác thực trang web, tạo sự tin tưởng cho người dùng.

***

## **Hướng dẫn tải lên Certificate**

### 1/ Hướng dẫn tải lên TLS/SSL Certificate <a href="#uploadacertificate-1.huongdantailentls-sslcertificate" id="uploadacertificate-1.huongdantailentls-sslcertificate"></a>

* Truy cập trình quản lý Certificate
* Nhấn nút "Tải lên Certificate / Upload Certificate"
* Một cửa sổ giao diện bật lên cho phép bạn điền thông tin Certificate, bao gồm
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
* Nhấn nút "Tải lên / Upload" tại góc dưới bên phải của cửa sổ giao diện để hoàn tất tải lên.

### 2. Hướng dẫn tải lên CA Certificate

* Truy cập trình quản lý Certificate
* Nhấn nút "Tải lên Certificate / Upload Certificate"
* Một cửa sổ giao diện bật lên cho phép bạn điền thông tin Certificate, bao gồm
  * **Tên gợi nhớ**: Khuyến khích sử dụng tên miền làm tên gợi nhớ
  * **Chọn loại Certificate CA**
  * **Điền Certificate Input bao gồm**:
    * **Nội dung Certificate:** Là Server Certificate domain của bạn (thường có đuôi \*.crt), có định dạng chuẩn PEM.
    * **Expiration**: Ngày hết hạn của Certificate.
* Nhấn nút "Tải lên / Upload" tại góc dưới bên phải của cửa sổ giao diên để hoàn tất tải lên.
