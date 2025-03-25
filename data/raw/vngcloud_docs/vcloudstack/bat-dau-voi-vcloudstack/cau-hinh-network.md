# Cấu hình Network

## Tổng quan <a href="#tong-quan" id="tong-quan"></a>

Khi triển khai giải pháp điện toán đám mây hybrid như vCloudStack, việc cài đặt mạng đóng vai trò trung tâm trong việc đảm bảo rằng các ứng dụng và dữ liệu có thể được xử lý một cách hiệu quả cả trên đám mây và tại cơ sở nội bộ. Do đó, người dùng cũng như là người quản trị hệ thống cần thiết kế một cách thận trọng để đảm bảo các dịch vụ được chạy mượt mà, an toàn và hiệu quả, giúp doanh nghiệp đạt được sự cân bằng tối ưu giữa linh hoạt của đám mây và yêu cầu về hiệu suất và tuân thủ tại cơ sở cục bộ.

vCloudstack cung cấp cho người quản trị giao diện để cấu hình cài đặt thông tin Network tại giao diện Admin Site, đây là bước tiền đề để người dùng thực hiện việc Khởi tạo máy chủ ảo tại giao diện User Site.

## Các bước thực hiện: <a href="#cac-buoc-thuc-hien" id="cac-buoc-thuc-hien"></a>

**Bước 1**: Người dùng truy cập và đăng nhập vào Admin Site vào mục Infrastructure/Network;

{% hint style="info" %}
**Lưu ý:** Người dùng thực hiện phải được phân quyền sử dụng chức năng Tạo Network tại Admin Site.
{% endhint %}

**Bước 2:** Người dùng thực hiện điền các thông số để cấu hình Network;

* **Tên Mạng** (bắt buộc): Điền tên tùy ý để người dùng nhận diện Network đã tạo;
* **CIDR** (bắt buộc): Điền phân bổ địa chỉ IP
* **IP Gateway** (bắt buộc): điền địa chỉ IP gateway cho subnet;
* **Network Type** (bắt buộc): Hiện vCloudStack đang hỗ trợ loại mạng vlan;
* **Segment ID** (bắt buộc): điền mã tương thích vớí loại mạng;
* **Physical Network**: mặc định hiển thị vlan theo loại mạng;
* **Share Type/Owner** (bắt buộc): Điền email của người dùng sẽ quản lý và sử dụng network này;
* **Shared all**: Tùy chọn cho phép tất cả user có thể sử dụng Network này để tạo máy ảo;

{% hint style="info" %}
**Lưu ý:**

* Nếu tạo Network private thì chỉ cần điền Email Owner là Email User sử dụng tạo máy ảo và không cần chọn Share all;
* Nếu tạo Network public thì có thể sử dụng chức năng Share all cho tất cả user sử dụng để tạo máy ảo.
{% endhint %}

_Ví dụ nội dung cấu hình Network:_

* Tên Mạng: _network-01_
* CIDR: _192.168.1.0/24_
* IP Gateway: _192.168.1.1_
* Network Type: _vlan_
* Segment IP: _100_
* Share Type/Owner: _admin01@abc.com_

**Bước 3**: Tạo thành công Network

* Người dùng nào được sử dụng Network sẽ thấy các Network ở màn hình User Site/Network;
* Người dùng sau đó có thể sử dụng Network đã tao để Khởi tạo máy chủ ảo.
