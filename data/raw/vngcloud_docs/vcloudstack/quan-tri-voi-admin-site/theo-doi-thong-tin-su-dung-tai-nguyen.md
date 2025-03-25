# Theo dõi thông tin sử dụng tài nguyên

## Tỗng quan

Giao diện User Resource cho phép người quản trị có thể theo dõi tất cả Tài nguyên (bao gồm VM và Volume) đã tạo và đang sử dụng của hạ tầng được ảo hóa bởi người vận hành tài nguyên đó.&#x20;

Để truy cập vào màn hình User Resource, bạn truy cập vào vCloudStack Admin Site chọn vào mục User Resource ở thanh điều khiển để được điều hướng tới màn hình User Resource.

Giao diện gồm danh sách của các tài nguyên (như VM Server, Volume, LB). Các thông số chi tiết được hiển thị trong màn hình giao diện gồm:

**Tại Tab giao diện Server (VM)**:

* **Name:** Hiển thị tên của VM và Mã định danh của VM đã tạo hoặc đang hoạt động;
* **Status:** Cho phép nhận biết tài nguyên VM đang ở trạng thái hoạt động gì;
* **Internal IP:** Cho biết VM này đang dùng địa chỉ IP Internal nào;
* **Location:** Thông tin vị trí&#x20;
* **External IP:** Cho biết VM này đang dùng địa chỉ IP External nào;
* **Instance Type:** Thống tin cấu hình VM và hệ điều hành
* **Owner:** Email của tài khoản người dùng đã tạo VM này.

{% hint style="info" %}
**Lưu ý**: Chỉ có những VM nào mà do chính Admin tạo ra thì có thể chọn nhanh để điều hướng đến xem chi tiết của VM đó và ngược lại.
{% endhint %}

**Tại Tab giao diện Volume:**

* **Name:** Hiển thị tên của Volume và Mã định danh của Volume đã tạo hoặc đang hoạt động;
* **Status:** Cho phép nhận biết tài nguyên Volume đang ở trạng thái hoạt động gì;
* **Type:** Hiển thị ID  loại cấu hình của Volume này;
* **IOPS:** Hiển thị số IOPS;
* **Size:** Dung lượng của volume đã tạo;
* **Attachment:** Cho biết Volume được gắn vào Volume nào ;
* **Multi-attach:** Cho biết Volume có được gắn nhiều tài nguyên không;
* **Owner:** Email của tài khoản người dùng đã tạo Volume này.
