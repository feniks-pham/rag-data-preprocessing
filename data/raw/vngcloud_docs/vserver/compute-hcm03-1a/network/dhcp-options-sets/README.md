# Bộ tùy chọn DHCP

## Tổng quan

Chức năng Bộ tùy chọn **DHCP** (Dynamic Host Configuration Protocol) hay DHCP Options Sets cho phép bạn cấu hình địa chỉ DNS server IP cho máy chủ ảo (VM) của vServer trong VPC. Trước khi bạn có thể sử dụng DHCP options set, bạn phải có trước địa chỉ DNS server IP, sau đó bạn có thể gán (Associate) DHCP options sets với VPC. Sau khi DHCP options set được gán vào VPC, nếu tạo máy ảo VM có VPC sẽ sử dụng DHCP options set vừa tạo, thì sau khi DHCP options set được đồng bộ với các máy chủ VM, máy chủ đó cũng sẽ sử dụng DHCP option set đó.

**Một số lưu ý khi cấu hình DHCP options set:**

* Một DHCP option set được gán với chỉ 1 VPC được deploy trong region của DHCP tạo ra;
* **Một DHCP option set** được cho phép **gán với nhiều VPC**;
* **Một VPC chỉ** được **gán vào một DHCP**;
* Có giới hạn số lượng tạo **10 DHCP options set** (không tăng giới hạn sử dụng được)

{% hint style="info" %}
**Lưu ý:**

Sau khi cấu hình DNS cho máy ảo VM xong, để làm mới việc sử dụng DHCP trên VM, các VM cần các <mark style="background-color:orange;">enable dhcp:true trong network config</mark>, sau đó, bạn có thể thao tác cập nhật dhcp theo 2 cách:

**Cách 1: Khởi động lại VM (restart)**

**Cách 2: Chủ động chạy câu lệnh sau để thực hiện:**

* **Với máy chủ Linux**: gõ các lệnh sau

```bash
sudo dhclient -r && sudo dhclient
resolvectl status
```

_Ghi chú: eth0 là card mặc định, nếu bạn tùy chỉnh qua interface khác thì lưu ý thay thế cho đúng card._

* &#x20;**Với máy chủ Windows Server**: gõ câu lệnh

```bash
ipconfig /renew
```
{% endhint %}

***

## Tạo DHCP Options Set

Với hướng dẫn này sẽ giúp bạn cách tạo ra một DHCP Options set, hãy thực hiện những bước như sau:

1. Đăng nhập vào VNG Cloud, chọn đến dịch vụ vServer;
2. Tại màn hình vServer, chọn vùng (region) phù hợp;
3. Trên thanh menu bên tay trái, chọn **DHCPs**;

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Tại giao diện màn hình danh sách DHCP options sets, chọn nút **Create a DHCP Options Set**;

<figure><img src="../../../../.gitbook/assets/image (4) (2).png" alt=""><figcaption></figcaption></figure>

5. Tại Trang tạo DHCP options set, hãy những thông số sau:

* **DHCP Option Set name**: Điền tên cho DHCP options set này;
* **Description:** Điền mô tả cho DHCP options set này;
* **DHCP Server IP:** Mặc định, VNG Cloud DNS Server được cung cấp tự động cho VPC
  * Chọn nút "**Set to Optimize**" để tùy chọn điền DNS Server IP;
  * Lưu ý, nếu bạn không dùng DNS mặc định, có thể bạn sẽ truy cập thất bại vào các dịch vụ VNG Cloud.

{% hint style="info" %}
**DNS server IP mặc định (default) mà VNG cloud cung cấp:**

* 10.166.12.196
* 10.166.12.197

DNS Server IP cho phép **điền tối đa là 4 IP** (có thể điền thêm 2 IP nếu vẫn sử dụng 2 IP default của hệ thống)
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (5) (2).png" alt=""><figcaption></figcaption></figure>

6. Sau khi thiết lập hoàn tất, chọn nút "**Create**" để hoàn thành việc thiết lập.

<figure><img src="../../../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

***

## Thực hiện gán vào VPC

Sau khi tạo được DHCP options set, cần thực hiện việc gán VPC vào, có hai cách thực hiện hiện việc gán VPC (Associate), xem các bước sau để thực hiện:

1. Đăng nhập vào VNG Cloud, chọn đến dịch vụ vServer;
2. Tại màn hình vServer, chọn vùng (region) phù hợp;
3. Trên thanh menu bên tay trái, chọn **DHCPs**;
4. Chọn một bộ DHCP đã tạo trước, để vào màn hình thông tin chi tiết;
5. Tại màn hình thông tin chi tiết, ở Tab Associated VPCs liệt kê tất cả VPC được gán vào;

<figure><img src="../../../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

6. Nhấn vào nút "**Associate**", màn hình liệt kê tất cả các VPC, chọn VPC cần gán sau đó nhấn nút "**Associate**".&#x20;

<figure><img src="../../../../.gitbook/assets/image (9) (2).png" alt=""><figcaption></figcaption></figure>

Sau khi gán thành công thì thông tin VPC được gán sẽ hiển thị ở màn hình danh sách VPC được gán vào DHCP.

<figure><img src="../../../../.gitbook/assets/image (10) (2).png" alt=""><figcaption></figcaption></figure>

***

## Thực hiện xóa DHCP options set

Trong quá trình sử dụng DHCP options set, người dùng có thể xóa DHCP options set. Tuy nhiên, khi xóa được một DHCP options set cần thực hiện:

### Bước 1: Gỡ tất cả các VPC của DHCP options set

1. Đăng nhập vào VNG Cloud, chọn đến dịch vụ vServer;
2. Tại màn hình vServer, chọn vùng (region) phù hợp;
3. Trên thanh menu bên tay trái, chọn **DHCPs**;
4. Chọn một bộ DHCP đã tạo trước và muốn xóa, để vào màn hình thông tin chi tiết;
5. Tại màn hình thông tin chi tiết, ở Tab Associated VPCs liệt kê tất cả VPC được gán vào, người dùng chọn tất cả các VPC đã gán và nhấn chọn "**Detach**"  để gỡ VPC ra;

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Nhấn xác nhận gỡ tất cả VPC khỏi DHCP options set.

### Bước 2: Xóa DHCP options set

1. Sau khi gỡ tất cả VPC khỏi DHCP option set, người dùng quay trở lại màn hình danh sách DHCP options set;
2. Tại DHCP muốn xóa, nhấn chọn hành động "Delete" để thực hiện việc xóa;
3. Xác nhận xóa DHCP options set. Khi đã xóa DHCP options set thì không thể phục hồi được.

<figure><img src="../../../../.gitbook/assets/image (12) (2).png" alt=""><figcaption></figcaption></figure>
