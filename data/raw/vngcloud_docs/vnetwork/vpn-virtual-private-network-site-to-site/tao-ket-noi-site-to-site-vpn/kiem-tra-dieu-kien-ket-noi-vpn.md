---
description: >-
  VPN Site to Site là một mô hình kết nối VPN dùng để liên kết hai hay nhiều
  mạng riêng tư thông qua liên kết mã bảo mật và an toàn.
---

# Kiểm tra điều kiện kết nối VPN

Để thực hiện kết nối Site-to-Site VPN giữa hai Site thông qua giao thức IPsec cần thực hiện cấu hình kết nối giữa hai site , theo đó để kết nối thành công giữa hai site cần thỏa các điều kiện, nếu không hệ thống sẽ báo lỗi không có phép thiết lập kết nối.

### **Các điều kiện để hai site kết nối với nhau là:**

<table><thead><tr><th width="88">STT</th><th width="316">Điều kiện</th><th>Báo lỗi</th></tr></thead><tbody><tr><td>1</td><td>Chỉ tạo được kết nối VPN khi CIDR ở hai đầu phải khác nhau . </td><td><p>(mã 2017) </p><p>Vi: CIDR bị trùng lấp ở hai đầu site</p></td></tr><tr><td>2</td><td>Chỉ tạo được kết nối VPN khi CIDR ở đầu xa không được trùng với CIDR đầu xa đã kết nối trước đó.</td><td>(mã 2023)<br>Vi: RemoteSite Subnet mới tạo trùng với RemoteSite Subnet đã tạo trước đó.</td></tr><tr><td>3</td><td>Tạo kết nối VPN phải được cấu hình thuật toán IKEv2 và IPsec không được empty nếu sử dụng Key Cá nhân</td><td>(mã 2022)<br>Vi: Thuật toán không phù hợp</td></tr><tr><td>4</td><td>CIDR của site remote phải đúng format và là Private CIDR</td><td>(mã 2018, 2019)<br>Vi: CIDR của Remote VPN phải là CIDR Private</td></tr><tr><td>5</td><td>IP Gateway  của site Remote  phải đúng format và là Public</td><td>(mã 2020, 2021)<br>VI: Gateway IP của Remote VPN là IP Public</td></tr></tbody></table>

## **Ví dụ về các mã lỗi khi tạo kết nối Site-to-Site VPN:**

### <mark style="color:blue;">**\[**</mark><mark style="color:blue;">Mã lỗi 2017</mark><mark style="color:blue;">**]**</mark> <mark style="color:blue;"></mark><mark style="color:blue;">CIDR bị trùng lấp ở hai đầu site khi tạo kết nối</mark>

<figure><img src="../../../.gitbook/assets/image (822) (1).png" alt=""><figcaption></figcaption></figure>

Từ hình mô tả trên ta thấy rằng:

* Tại Site HCM03 có CIDR của VPC1 là 10.1.0.0/16;
* Tại Site HAN01 có CIDR của VPC1 là 10.1.0.0/16;
* Nhận thấy là hai CIDR của hai site HCM03 và HAN01 đang trùng nhau;
* Do đó, việc tạo kết nối Site-to-Site VPN giữa hai site là không được thực hiện.

### <mark style="color:blue;">**\[**</mark><mark style="color:blue;">Mã lỗi 2023</mark><mark style="color:blue;">**]**</mark> <mark style="color:blue;"></mark><mark style="color:blue;">RemoteSite Subnet mới tạo trùng với RemoteSite Subnet đã tạo trước đó.</mark>

<figure><img src="../../../.gitbook/assets/image (823).png" alt=""><figcaption></figcaption></figure>

Từ hình mô tả trên ta thấy rằng:

* Tại Site HCM03 có CIDR của VPC1 là 10.1.0.0/16;
* Tại Site HAN01 có CIDR của VPC1 là 172.16.0.0/16;
* Tại site On Premise có CIDR là 172.16.0.0/16;
* Một kết nối Site-to-Site VPN được thiết lập từ Site HCM03 đến HAN01;
* Ta thấy rằng CIDR của site On-Premise trùng với site HAN01 là 172.16.0.0/16, mà CIDR này đã được dùng kết kết nối trước với site HCM03;
* Do đó, việc tạo kết nối Site-to-Site VPN giữa hai site HCM03 và site On-Premise là không được thực hiện.



