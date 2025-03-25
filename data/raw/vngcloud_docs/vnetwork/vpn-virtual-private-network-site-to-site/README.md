---
description: >-
  VPN Site to Site là một mô hình kết nối VPN dùng để liên kết hai hay nhiều
  mạng riêng tư thông qua liên kết mã bảo mật và an toàn.
---

# VPN (Virtual Private Network) Site-to-Site

## Tổng quan

Theo mặc định, các máy chủ ảo (VM) mà đã được gán vào VPC thì chưa thể giao tiếp với các mạng đầu xa (remote network). Từ đó để có thể truy cập vào mạng đầu xa (remote network) từ VPC bằng cách tạo một kết nối **Site-to-Site VPN** (Virtual Private Network) và cấu hình định tuyến cho các lưu lượng đi qua thông qua kết nối này.

Kết nối Site-to-Site VPN hỗ trợ hỗ trợ kết nối với giao thức Internet Protocal security (viết tắt là IPsec).

## Sự kết nối giữa các site

Để hiểu rõ về sự kết nối giữa các site, hãy xem mô tả cụ thể bên dưới về một kết nối Site-to-Site VPN:

Giả thiết đang có 3 vùng (site) mạng là Hồ Chí Minh (HCM03) và Hà Nội (HAN01) và hệ thống mạng nội bộ riêng (on-premise), mỗi vùng đều đã thiết lập sẵn các VPC từ trước.&#x20;

Region HCM03 có các VPC:

* VPC1 (10.1.0.0/16);
* VPC2 (10.2.0.0/16).

Region HAN01 có các VPC:

* VPC1 (172.16.0.0/16);

Tại Site On-Premise có các thông tin mạng:

* 192.168.1.0/24
* 192.168.2.0/24&#x20;
* 192.168.3.0/24

Thực hiện việc tạo kết nối VPN với 3 đường kết nối như sau:&#x20;

* Cổng VPNGW-01 của HCM03 kết nối đến Cổng VPNGW-01 của HAN01;
* Cổng VPNGW-01 của HCM03 kết nối đến Cổng Router của của hệ thống On-Premise;
* Cổng VPNGW-02 của HCM03 kết nối đến Cổng Router của của hệ thống On-Premise.

Từ đó đồng nghĩa với việc hệ thống mạng kết nối với nhau sau khi:

* VPC1 của HCM03 có route table ghi nhận  VPC là 172.16.0.0/16 của HAN01 và 192.168.1.0/24 của hệ thống On-Premise;
* VPC2 của HCM03 có route table ghi nhận  VPC là 192.168.1.0/24 và 192.168.2.0/24 của hệ thống On-Premise;



<figure><img src="../../.gitbook/assets/image (1) (5).png" alt=""><figcaption><p>Sơ đồ kết nối cơ bản giữa hai site bằng đường IPsec VPN</p></figcaption></figure>

***

VNG Cloud cung cấp cho người dùng dịch vụ VPN có thể thực hiện các tác vụ như sau:

* [Tạo kết nối Site-to-Site VPN](tao-ket-noi-site-to-site-vpn/)
* [Kiểm tra điều kiện kết nối VPN](tao-ket-noi-site-to-site-vpn/kiem-tra-dieu-kien-ket-noi-vpn.md)
* [Thay đổi thông tin Bandwidth](thay-doi-thong-tin-bandwidth.md)
* [Xoá VPN](xoa-cross-connect.md)
* [Các gói VPN](cac-goi-bang-thong.md)
