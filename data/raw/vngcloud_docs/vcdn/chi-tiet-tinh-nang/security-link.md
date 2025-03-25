# Security Link

## **Secure Token** <a href="#securitylink-securetoken" id="securitylink-securetoken"></a>

Secure token là các đoạn mã có cấu trúc nhằm bảo vệ nội dung không bị đánh cắp và phát tán trên các nơi khác. Trên vCDN, chúng tôi hỗ trợ bạn có thể thực hiện bật tính năng Secure token khi tạo hoặc chỉnh sửa CDN đã tạo trước đó.

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Sơ đồ hoạt động <a href="#securitylink-sodohoatdong" id="securitylink-sodohoatdong"></a>

Khi người dùng cuối cần truy cập vào nội dung đã được thiết lập kích hoạt "Secure token" thì yêu cầu này sẽ được hệ thống kiểm tra lại yêu cầu có thỏa công thức hay không, nếu thỏa thì người dùng cuối lấy được nội dung, nếu không thì yêu cầu sẽ bị từ chối.

<figure><img src="../../.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>

Trong đó:&#x20;

* **Passphase**: là key kèm theo công thức bạn đã thiết lập để hệ thống có thể nhận dạng có truy cập đã được cấp quyền.
* **Include client IP**: là IP của end user request content.
* Để "Secure token" có thể hoạt động được, người quản trị dịch vụ cần phải tích hợp KEY vào hệ thống. Tùy theo loại Token Type sẽ có công thức generate KEY khác nhau, cụ thể:
  * **VNG**:
    * **URL Format**: http(s)://\<domain>/\<token>/\<expiredTime>/\<uri>
    * **\<token>**: md5(\<Passphare>\<filePath>\<expiredTime>\<clientIP>)
    * **\<expiredTime>:** Thời gian epochtime hết hạn của URL, tính bằng mili-seconds
    * **\<filePath>**:  /path/to/media/xxx.\[m3u8|ts|mpd|dash] (tức là \<uri> bỏ đi phần xxx.\[m3u8|ts|mpd|dash], trường hợp ví dụ này sẽ là: /path/to/media)
    * **\<ClientIP>**: IP của client được cấp phép truy cập vào nội dung, chỉ cung cấp trong đường hợp bạn đã chọn bật "Include IP" trong cấu hình của dịch vụ CDN
    * Ví dụ: [http://abcxyz.vcdn.cloud/cb0a229fa7a81c219c0c0f964f9b6e68/1603691495000/test/index.m3u8](http://abcxyz.vcdn.cloud/cb0a229fa7a81c219c0c0f964f9b6e68/1603691495000/test/index.m3u8)
  * **SBD**:
    * **URL Format**: http(s)://\<domain>/\<token>/\<expiredTime>/\<uri>
    * **\<token>**: md5(\<clientIP>**:<**&#x50;assphare>**:**\<exiredTime>**:**\<filePath>)
    * **\<expiredTime>**: Thời gian epochtime hết hạn của URL, tính bằng seconds
    * **\<filePath>:/path/to/media**/xxx.\[m3u8|ts|mpd|dash] (tức là \<uri> bỏ đi phần xxx.\[m3u8|ts|mpd|dash], trường hợp ví dụ này sẽ là: /path/to/media)
    * **\<ClientIP>**: IP của client được cấp phép truy cập vào nội dung, chỉ cung cấp trong đường hợp bạn đã chọn bật "Include IP" trong cấu hình của dịch vụ CDN
  * **Akamai**:&#x20;
    * Tham khảo hướng dẫn từ document của Akamai tại: [https://learn.akamai.com/en-us/webhelp/adaptive-media-delivery/adaptive-media-delivery-implementation-guide/GUID-041AEFDE-7E25-4AD8-B6C4-73F1B7200F02.html](https://learn.akamai.com/en-us/webhelp/adaptive-media-delivery/adaptive-media-delivery-implementation-guide/GUID-041AEFDE-7E25-4AD8-B6C4-73F1B7200F02.html)&#x20;

***

## **Sử dụng tính năng CORS** <a href="#securitylink-sudungtinhnangcors" id="securitylink-sudungtinhnangcors"></a>

CORS là tính năng bảo mật đầu ra của vCDN cho phép truy cập có các cấu hình như: tên miền, địa chỉ IP,  Header, Method, Expose Header truy cập vào Link đầu ra của vCDN.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## **Khởi tạo Whitelist / Blacklist IP** <a href="#securitylink-khoitaowhitelist-blacklistip" id="securitylink-khoitaowhitelist-blacklistip"></a>

* **WhiteList IP:** Bạn có thể add các danh sách IP của các Origin cho phép truy cập vào link đầu ra bằng cách chọn **Allow** và nhập **IP Address** hoặc **CIDR** mà bạn mong muốn:&#x20;

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **BlackList IP:** Bên cạnh đó, bạn cũng có thể khóa các IP không cho phép Origin truy cập vào link đầu ra của vCDN:&#x20;

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## **Geo Block** <a href="#securitylink-geoblock" id="securitylink-geoblock"></a>

* Ngoài ra, bạn có thể tạo danh sách những origin ở các quốc gia nào có thể truy cập link đầu ra bằng cách chọn **Allow** và nhập **mã quốc gia** mong muốn:&#x20;

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Bạn cũng có thể thiết lập không cho phép những Origin ở quốc gia nào truy cập link đầu ra bằng cách chọn **Block** và nhập **mã quốc gia** mong muốn:

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## **HTTP Referer Block** <a href="#securitylink-httprefererblock" id="securitylink-httprefererblock"></a>

* Bạn có thể cho phép Origin có domain trong list có thể truy cập link đầu ra bằng cách chọn **Allow** và nhập **domain** mong muốn:&#x20;

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Sau cùng, bạn có thể không cho phép Origin có domain trong danh sách có thể truy cập link đầu ra bằng cách chọn **Block** và nhập **domain** mong muốn:

<figure><img src="../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
