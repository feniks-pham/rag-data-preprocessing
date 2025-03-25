# Thêm/ Xóa NAT Port

* Người dùng có thể thêm NAT port khi có nhu cầu sử dụng hoặc xóa NAT port khi không còn nhu cầu sử dụng
* Thực hiện theo thứ tự sau đây

### Thêm NAT Port

* Tại màn hình danh sách NAT, chọn NAT muốn thêm port
* Nhấn chọn vào tên NAT để vào màn hình chi tiết NAT
* Di chuyển đến phần Inbound Rules, nhấn chọn “Create an inbound rule”
* Điền thông tin thích hợp vào màn hình nhập mới inbound rule:

&#x20;                o   Protocol

&#x20;                o   Ether Type

&#x20;                o   Port range

&#x20;                o   Description

* Nhấn chọn Create để tạo Port

### Xóa NAT Port



{% hint style="danger" %}
_Người dùng không thể xóa rule do hệ thống tạo_
{% endhint %}

* Tại màn hình danh sách NAT, chọn NAT xóa port
* Nhấn chọn vào tên NAT để vào màn hình chi tiết NAT
* Di chuyển đến phần Inbound Rules
* Định vị tại dòng inbound rule muốn xóa, nhấn vào biểu tượng Xóa
