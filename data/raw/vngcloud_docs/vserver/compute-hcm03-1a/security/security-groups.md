# Security Groups

Security Group hoạt động như một firewall ảo điều khiển traffic vào và ra, đảm bảo tính bảo mật cho các máy chủ ảo.

Khi tạo một máy chủ ảo, bạn cần xác định một hoặc nhiều Security group. Nếu không thay đổi, hệ thống sẽ chọn Security Group mặc định. Bạn có thể thêm rule vào Security Group để cho phép traffic đi vào hoặc đi ra đối với máy chủ ảo đang được gắn với Security Group đó. Bạn có thể thay đổi các rule này bất cứ thời điểm nào. Những rule mới sẽ có hiệu lực tức thì lên tất cả máy chủ ảo đang được gắn với Security Group đó.

Security Group là một công cụ sàng lọc packet có tính chất stateful. Khi cần quyết định cho phép traffic có được đi qua hay không, security group sẽ duyệt qua tất cả các rule của tất cả các group đang được gắn với máy chủ ảo đó.

***

### **Security group rules** <a href="#securitygroups-securitygrouprules" id="securitygroups-securitygrouprules"></a>

Các rule trong security group điều khiển traffic có được phép đi vào đến các máy chủ ảo đang gắn với security group đó hay không. Nó cũng điều khiển traffic có được phép đi ra khỏi máy chủ ảo hay không.

Các rule sẽ có những đặc tính sau đây:

* Mặc định, security group chứa các rule outbound cho phép tất cả traffic đi ra. Bạn có thể xóa các rule này.
* Các security group rules luôn là permissive, bạn tạo rule để cho phép traffic đi vào. Security group mặc định là từ chối tất cả, bạn không thể tạo các rule từ chối khác.
* Security group rule cho phép bạn định nghĩa theo giao thức, port và địa chỉ đầu xa.
* Security group có tính chất stateful, nếu bạn gửi request đi ra từ máy chủ ảo của bạn, traffic trả về cho request đó sẽ được chấp nhận mà không cần quan tâm đến các rule đi vào của security group đó. Và ngược lại, traffic trả về cũng được phép đi qua nếu nó đã được cho phép đi vào, bất kể các rule đi ra của security group đó.
* Khi bạn gán nhiều security group cho một máy chủ ảo, tất cả các rule của các security group sẽ được tổ hợp lại. Do đó, một máy chủ ảo có thể được gán hàng trăm rule. Điều này có thể gây khó khăn trong việc truy cập vào máy chủ, cần khuyến khích rút gọn các rule này tối đa có thể.

Mỗi rule cho phép sẽ chứa các thông tin sau:

* **Rule**: định nghĩa sẵn một số protocol phổ biến như SSH, HTTP, HTTPS, ICMP…
* **Protocol**: Giao thức của packet, các giao thức phổ biến như 6 (TCP), 17 (UDP), và 1 (ICMP).
* **Port range**: Đối với giao thức TCP, UDP hoặc giao thức tùy biến, dãy port có thể được chỉ định. Bạn có thể chỉ định từng port riêng lẻ (VD port 22) hoặc 1 dãy port liên tiếp (VD **7000 - 8000**).
* **CIDR of remote address**: Địa chỉ đầu xa tức là địa chỉ nguồn của packet đối với rule inbound hoặc địa chỉ đích của packet đối với rule outbound. Thường có dạng như sau:
  * Một địa chỉ IP cụ thể: Bạn cần chỉ định /32 netmask, Ví dụ: 192.168.10.10/32.
  * Một dãy địa chỉ IP: Bạn cần chỉ định CIDR block cụ thể, Ví dụ: 192.168.10.0/24
* **(Optional) Description**: Bạn có thể điền các mô tả ngắn để thuận tiện quản lý sau này.

### **Security group mặc định** <a href="#securitygroups-securitygroupmacdinh" id="securitygroups-securitygroupmacdinh"></a>

Mỗi máy chủ ảo phải có một hoặc nhiều security group. Khi bạn tạo máy chủ ảo qua giao diện portal hoặc API, bạn có thể sử dụng security group mặc định. Security group mặc định sẽ gồm có các rule mặc định sau:

Outbound rules:

* Cho phép tất cả traffic đi ra

Inbound rules:

* Cho phép tất cả traffic đi vào port 234 (SSH) và port 3490 (RDP)
* Cho phép tất cả traffic đi vào port 80 (HTTP) và port 443 (HTTPS)
* Cho phép tất cả traffic ICMP đi vào tất cả các port

Bạn có thể điều chỉnh hoặc xóa các rule mặc định bất cứ lúc nào.

***

### **Làm việc với Security group** <a href="#securitygroups-lamviecvoisecuritygroup" id="securitygroups-lamviecvoisecuritygroup"></a>

Bạn có thể thực hiện các thao tác sau để sử dụng Security Group điều khiển traffic cho máy chủ ảo:

#### Tạo security group <a href="#securitygroups-taosecuritygroup" id="securitygroups-taosecuritygroup"></a>

1. Vào trang VNG Cloud Portal console, đến trang Security Group
2. Tạo security group với tên và mô tả theo ý muốn

#### Xem chi tiết security group <a href="#securitygroups-xemchitietsecuritygroup" id="securitygroups-xemchitietsecuritygroup"></a>

1. Vào trang VNG Cloud Portal console, đến trang Security Group
2. Chọn security group cần xem và nhấn **Detail,** bạn có thể xem nội dung chi tiết của các rule inbound và outbound. Mục **Server** hiển thị các máy chủ ảo đang được gán với security group này.

#### Thêm và xóa rule đối với security groups <a href="#securitygroups-themvaxoaruledoivoisecuritygroups" id="securitygroups-themvaxoaruledoivoisecuritygroups"></a>

1. Vào trang VNG Cloud Portal console, đến trang Security Group
2. Chọn security group cần thao tác và nhấn **Detail**
3. Chuyển sang mục Inbound hoặc Outbound để thao tác thêm hoặc xóa rules
4. Để thêm rule mới, bạn phải cung cấp các thông tin như giao thức, port, CIDR như mong muốn

#### Gắn và tháo gỡ security groups đối với máy chủ ảo <a href="#securitygroups-ganvathaogosecuritygroupsdoivoimaychuao" id="securitygroups-ganvathaogosecuritygroupsdoivoimaychuao"></a>

1. Vào trang VNG Cloud Portal console, đến trang Instance
2. Chọn máy chủ ảo cần thao tác, chọn **Update Security** trong menu action bên phải
3. Gắn thêm hoặc gỡ bỏ Security Groups khỏi danh sách
