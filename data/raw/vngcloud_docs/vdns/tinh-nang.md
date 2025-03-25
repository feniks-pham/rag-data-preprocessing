---
description: Giải pháp DNS mạnh mẽ cho hạ tầng Private Cloud
---

# Tính năng

vDNS là dịch vụ DNS được thiết kế đặc biệt cho môi trường Private Cloud trên VNG Cloud, cung cấp khả năng quản lý và phân giải tên miền một cách an toàn, linh hoạt và hiệu quả trong mạng riêng ảo (VPC).

**Các tính năng cơ bản của vDNS:**

## **Kích hoạt máy chủ DNS (Enable Private DNS Server cho VPCs)**

* Tính năng này cho phép bạn kích hoạt một máy chủ DNS riêng biệt trong VPC của mình. Điều này đảm bảo rằng các máy ảo (VM) trong VPC có thể phân giải tên miền một cách riêng tư, không thông qua internet công cộng.
* Việc kích hoạt Private DNS Server sẽ tạo ra một hoặc nhiều địa chỉ IP dành riêng cho DNS server trong VPC. Các địa chỉ này sẽ được tự động cấu hình cho các VM trong VPC thông qua DHCP.
* Đây là bước tiên quyết để sử dụng các tính năng khác của vDNS trong VPC.

{% hint style="info" %}
**Lưu ý quan trọng:** Việc kích hoạt Private DNS _dẫn đến việc thay đổi DHCP Option Set_ của các VM trong mạng. Do đó, sau khi kích hoạt, bạn _cần cập nhật DHCP_ cho các VM để chúng nhận được cấu hình DNS mới. Vui lòng tham khảo hướng dẫn cập nhật DHCP [tại đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/network/dhcp-options-sets#tong-quan).
{% endhint %}

## **Tạo Hosted Zone**&#x20;

Hosted Zone là một vùng chứa các bản ghi DNS cho một tên miền cụ thể (ví dụ: `example.com`).

* vDNS cho phép bạn tạo hai loại Hosted Zone:
  * **Public Hosted Zone:** Dùng cho các tên miền công khai, có thể phân giải từ internet. (Hiện tại chưa hỗ trợ phiên bản Public)
  * **Private Hosted Zone:** Dùng cho các tên miền nội bộ, chỉ có thể phân giải trong phạm vi VPC được liên kết.
* **Điểm quan trọng:** Khi tạo Private Hosted Zone, vDNS _chỉ cho phép_ bạn liên kết với các VPC đã được kích hoạt tính năng Private DNS Server. Điều này đảm bảo tính bảo mật và cô lập của mạng riêng.

## **Chỉnh sửa Hosted Zone**&#x20;

Gắn thêm hoặc gỡ bỏ VPC khỏi/vào Hosted Zone

* Sau khi tạo Hosted Zone (đặc biệt là Private Hosted Zone), bạn có thể dễ dàng chỉnh sửa nó bằng cách thêm hoặc gỡ bỏ liên kết với các VPC.
* Việc này cho phép bạn kiểm soát phạm vi phân giải của tên miền. Ví dụ: bạn có thể cho phép một tên miền nội bộ được phân giải bởi nhiều VPC khác nhau hoặc giới hạn nó chỉ trong một VPC duy nhất.

## **Tạo Record**&#x20;

Bao gồm 6 loại record type và 3 loại routing policy

* vDNS hỗ trợ đầy đủ các loại bản ghi DNS phổ biến:
  * **A:** Trỏ tên miền đến địa chỉ IPv4.
  * **CNAME:** Tạo bí danh cho một tên miền khác.
  * **MX:** Xác định máy chủ thư điện tử.
  * **SRV:** Xác định vị trí của các dịch vụ cụ thể.
  * **TXT:** Lưu trữ văn bản tùy ý.
  * **PTR:** Phân giải ngược (reverse DNS lookup), từ địa chỉ IP trở lại tên miền
* vDNS cũng cung cấp các chính sách định tuyến linh hoạt:
  * **Simple Routing:** Định tuyến đơn giản, trả về một tập hợp các tài nguyên theo thứ tự.
  * **Geolocation Routing:** Định tuyến dựa trên vị trí địa lý của người dùng.
  * **Weighted Routing (có Sticky Session):** Phân phối lưu lượng truy cập dựa trên trọng số, với khả năng duy trì phiên dính.
