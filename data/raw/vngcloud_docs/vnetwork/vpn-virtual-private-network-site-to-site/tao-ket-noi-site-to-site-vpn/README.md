---
description: >-
  VPN Site to Site là một mô hình kết nối VPN dùng để liên kết hai hay nhiều
  mạng riêng tư thông qua liên kết mã bảo mật và an toàn.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Tạo kết nối Site-to-Site VPN

**Thực hiện các bước sau để thực hiện việc tạo một kết nối Site-to-Site VPN:**

## **Bước 1:**  Truy cập trang khởi tạo VPN từ vNetwork Dashboard

* Truy cập thành công vào VNG Cloud, tại màn hình Console chọn đến dịch vụ vNetwork.
* Tại thanh menu bên trái của giao diện vNetwork, chọn mục VPN Site-to-Site.
* Tại màn hình danh sách này, nhấn chọn "<mark style="color:blue;">**Tạo mới kết nối VPN**</mark>".

<figure><img src="../../../.gitbook/assets/1 (2).png" alt=""><figcaption></figcaption></figure>

## **Bước 2:** Tại màn hình Tạo mới kết nối VPN, điền các thông tin khởi tạo như sau:

### Cấu hình thông tin cơ bản

* <mark style="color:blue;">**Tên VPN**</mark>: Điền tên của Cross Connect được tạo.
* <mark style="color:blue;">**Chọn gói dịch vụ VPN**</mark>: Chọn gói dịch vụ VPN phù hợp với nhu cầu sử dụng.
* <mark style="color:blue;">**Cấu hình VPN:**</mark> Điền các thông tin cấu hình:
  * **VPC** (Local Private CIDR): Network Local Private CIDR của VPN (VNGCloud site) và thông tin này sẽ được dùng để cấu hình tại remote VPN để allow các gói tin, và tập tin đến từ VNGCloud VPN. Tại trường này, hãy chọn VPC đã tạo từ trước.
  * **Subnet**: Chọn subnet nằm trong VPC được chọn. Sau khi VPN tạo xong, sẽ cấp một IP private cho VPN nằm trong subnet này, mục đích làm Private Gateway IP. IP dùng cho việc thêm Route Rule để điều hướng traffic đến remote VPN LAN.

### <mark style="color:blue;">**Cấu hình Default Tunnel**</mark>

* **Remote Public Gateway IP**: Điền thông tin Địa chỉ IP WAN của remote VPN Server.
* **Remote Private CIDR**:  Điền Dải địa chỉ IP LAN của server OnPremise pfsense.
* Tùy chọn **Pre-shared Key**: Là mật khẩu, keys mà VPN VNGCloud và Remote VPN OnPremise(Ví dụ: PFsense) sẽ dùng để auth cho nhau (Pre-shared Key – PSK phải giống nhau trên cả 2 bên). _Nếu không tích chọn_  _**"Used Your Pre-shared Key"** hệ thống sẽ tự sinh ra PSK_

<figure><img src="../../../.gitbook/assets/image (13) (1) (1).png" alt=""><figcaption><p>VPN Basic Configuration</p></figcaption></figure>

* Bên cạnh đó có mục <mark style="color:blue;">**Cấu hình thuật toán**</mark> cho kết nới VPN, được thiết lập với hai cấu hình chính được thiết lập mặc định. Các cấu hình IPSEC hỗ trợ có thểm xem [tại đây](cac-cau-hinh-ho-tro.md)
  * &#x20;**IKE Policy**: Cấu hình các config cho phase 1 của VPN IPSEC (Config tại 2 bên phải trùng nhau thì VPN mới hoạt động).
  * **IPsec Policy**: Cấu hình các config cho phase 2 của VPN IPSEC (Config tại 2 bên phải trùng nhau thì VPN mới hoạt động).
* Tại bên phải màn hình, xem tổng chi phí gói VPN đã chọn, sau đó nhấn chọn <mark style="color:blue;">**"Tạo mới kết nối VPN"**</mark> đề xác nhận và tiến hành thanh toán;

<figure><img src="../../../.gitbook/assets/image (11) (1) (1).png" alt=""><figcaption><p>VPN Tunnel Configuration</p></figcaption></figure>

_-> Sau khi thanh toán thành công, hệ thống sẽ xử lý kết nối thành công tuyến VPN vừa tạo và chuyển về màn hình danh sách VPN_ [_https://hcm-3-vnetwork.console.vngcloud.vn/vpn/list_](https://hcm-3-vnetwork.console.vngcloud.vn/vpn/list)

{% hint style="success" %}
**Lưu ý về trạng thái tạo VPN:**

* Tại màn hình danh sách VPN, có thể thấy kết nối VPN vừa tạo với trạng thái "<mark style="color:blue;">**Provisioning**</mark>" (là trạng thái hệ thống đang thiết lập kết nối);
* Sau khi hệ thống xử lý xong thì trạng thái sẽ tự động chuyển thành "<mark style="color:blue;">**Active**</mark>".
* Thời gian tạo một VPN dao động từ 3-5 phút. Vì cần khởi tạo dịch vụ VPN và Default Tunnel.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (4) (5).png" alt=""><figcaption><p>VPN List</p></figcaption></figure>

## **Bước 3:** Kiểm tra lại thông tin VPN vừa tạo, bằng cách click vào VPN để chuyển qua trang Detail.

<figure><img src="../../../.gitbook/assets/image (14) (1) (1).png" alt=""><figcaption><p>VPN Detail - Local Configuration</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (15) (1) (1).png" alt=""><figcaption><p>VPN Detail - Default Tunnel</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (16) (1) (1).png" alt=""><figcaption><p>VPN Detail - Tags</p></figcaption></figure>

## **Bước 4:** Tạo Route Rule để điều hướng các request đến Remote LAN CIDR đi qua VPN thông qua **Private Gateway IP** _(Detail Page)._

Truy cập vServer Router Tables để  thêm cấu hình điều hướng đến VPN [https://hcm-3.console.vngcloud.vn/vserver/network/route-table](https://hcm-3.console.vngcloud.vn/vserver/network/route-table)

* Destination: Remote Private CIDR.
* Target: Local Private Gateway.

<figure><img src="../../../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption><p>VPN Detail - VPN Gateway</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (3) (5).png" alt=""><figcaption><p>Update Route Table</p></figcaption></figure>

