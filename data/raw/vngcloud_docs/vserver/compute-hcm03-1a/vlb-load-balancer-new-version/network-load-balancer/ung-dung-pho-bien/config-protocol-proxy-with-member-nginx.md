# Config protocol Proxy with member Nginx

Protocol Proxy là một protocol đặc thù cho phép Load Balanacer chuyển tiếp thông tin kết nối của end-user (client connection information) đến các Member servers. Từ đó các Member Servers sẽ có thông tin để cấu hình các tính năng nâng cao như Rate-limit by IP, GeoIP, thống kê log access của client,.... Để sử dụng Protocol Proxy, bạn cần tạo vLB Layer 4 với Pool Settings là Proxy Protocol, đồng thời Member Server của bạn phải hỗ trợ Protocol Proxy này. Một số Web Server phổ biến đã hỗ trợ Proxy Protocol là Nginx, Apache,... Bài hướng dẫn này sẽ dùng Nginx.



* **Bước 1**: Bạn tạo Pool với Setting là Proxy Protocol:

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-59-17.png?version=1&#x26;modificationDate=1699597645000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


* **Bước 2:** Trên Nginx server, kiểm tra module proxy protocol **http\_realip\_module** đã được cài đặt trước hay chưa bằng command. Nếu chưa, bạn cần install hoặc rebuild nginx từ source với module trên.

| `nginx -V 2>&1` `\| grep -- 'http_realip_module'` |
| ------------------------------------------------- |

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-46-47.png?version=1&#x26;modificationDate=1699597645000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**\* Chú ý**: Module này sẽ được install sẵn từ version **Ubuntu Bionic Beaver (18.04).**



* **Bước 3:** Cấu hình bật Proxy Protocol tại Virtual Host:

**+** Cấu hình thêm tham số **proxy\_protocol** tại **server {}** bloc&#x6B;**:**

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-48-12.png?version=1&#x26;modificationDate=1699597645000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\+ Xác định Load Balancer IP nơi mình nhận traffic Proxy Protocol tại **server {}** block với cấu hình **set\_real\_ip\_from**

| `set_real_ip_from <Load balancer IP>;` |
| -------------------------------------- |

\


VD: ở đây IP của vLB đang là 103.245.248.204.&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-49-14.png?version=1&#x26;modificationDate=1699597645000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


\+ Cấu hình thay đổi IP của Load balancer với IP của client, được lấy từ Proxy Protocol Header tại **server {}** block với cấu hình **real\_ip\_header** và tham số **proxy\_protocol**

| `real_ip_header proxy_protocol;` |
| -------------------------------- |

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-50-39.png?version=1&#x26;modificationDate=1699597645000&#x26;api=v2" alt=""><figcaption></figcaption></figure>



* **Bước 4:** Cấu hình Header để lấy giá trị xuất log tại **http {}** block với cấu hình **proxy\_set\_header**



| <p><code>proxy_set_header X-Real-IP       $proxy_protocol_addr;</code><br><code>proxy_set_header X-Forwarded-For $proxy_protocol_addr;</code></p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------- |



<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-51-10.png?version=1&#x26;modificationDate=1699597645000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Bước 5:** Cấu hình Custom log với giá trị Client IP (Optional nếu bạn cần xuất log nginx kèm theo log client ip).

Định nghĩa log\_format custom có kèm theo Client IP

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-52-12.png?version=1&#x26;modificationDate=1699597645000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Thêm trong block **server{}** **access\_log** với log\_format là **custom** trên.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-52-47.png?version=1&#x26;modificationDate=1699597646000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Bước 6:** Kiểm thử cấu hình và restart nginx để hoàn tất bằng command

| `nginx -t` |
| ---------- |

Nếu không có errror, bạn tiến hành restart nginx.

| `systemctl restart nginx` |
| ------------------------- |



* **Bước 7**: Thực hiện gửi request và kiểm tra log ra sẽ thấy IP Client xuất hiện trong log file:

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553636/image2021-10-27_11-55-33.png?version=1&#x26;modificationDate=1699597646000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
