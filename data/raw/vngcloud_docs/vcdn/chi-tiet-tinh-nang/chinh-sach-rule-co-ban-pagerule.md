# Page Rule

## Tổng quan

**Page Rule** là một công cụ mạnh mẽ trong hệ thống vCDN cho phép bạn tùy chỉnh cách CDN xử lý các yêu cầu đến website dựa trên các quy tắc được định nghĩa trước. Với Page Rule, bạn có thể áp dụng các thiết lập cụ thể cho một hoặc nhiều URL, giúp tối ưu hóa hiệu suất, tăng cường bảo mật, hoặc cải thiện trải nghiệm người dùng.

## Chi tiết

Khi khởi tạo Live Stream, Object Download,...bạn có thể khởi tạo Page Rule bằng cách chọn **Create Page Rule**. Một Rules sẽ được thực thi khi mà có URI request đúng với điều kiện đã được định nghĩa trong Rule.

<figure><img src="../../.gitbook/assets/image (18) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Sau khi bạn chọn Create Page Rule, màn hình hiển thị như sau:

<figure><img src="../../.gitbook/assets/image (19) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

Trong đó:&#x20;

* **URL Pattern:** nhập URL pattern cần áp dụng Page Rule, vCDN hỗ trợ kiểu khai báo “\*” đại diện cho một chuỗi nhiều ký tự. Ví dụ: /trang\_landing\_cu.html
* **Các hành động khi thỏa điều kiện:** Mỗi Rules khi thỏa điệu kiện đúng URI được request sẽ có thể tùy chọn thực thi một trong khác hành động sau:
  * Always Use HTTPS&#x20;
  * Auto Minify&#x20;
  * Automatic HTTPS Rewrites&#x20;
  * Server Cache TTL&#x20;
  * Browser Cache TTL&#x20;
  * Bypass Cache by Cookie&#x20;
  * Bypass Cache By Device Type
  * Forwarding URL&#x20;
  * Add Response Header&#x20;
  * Brotli&#x20;
  * Gzip
  * Origin Override

Cụ thể, vui lòng tham khảo bảng bên dưới.

Mỗi Page Rule sẽ có các hành động action khác nhau được thể hiện ở bảng dưới đây. “Order” nhằm sắp xếp vị trí các rule, số càng nhỏ, ưu tiên thực hiện càng lớn.

<figure><img src="../../.gitbook/assets/image (20) (1) (1).png" alt="" width="279"><figcaption></figcaption></figure>

Sau khi tạo xong, chọn **Save changes** để cập nhật thay đổi.

***

Bảng mô tả các loại hành động:

<table data-full-width="true"><thead><tr><th width="297">Rule</th><th width="369">Action</th><th>Mô tả</th></tr></thead><tbody><tr><td><strong>Always Use HTTPS</strong></td><td>ON/OFF</td><td>Bật/Tắt tùy chọn “Luôn sử dụng giao thức HTTPS” trên trang chỉ định.</td></tr><tr><td><strong>Auto Minify</strong></td><td>Javascript / CSS / HTML</td><td>Tùy chọn ghi đè chức năng minify trên trang chỉ định.</td></tr><tr><td><strong>Automatic HTTPS Rewrites</strong></td><td>ON/OFF</td><td>Bật tắt tính năng tự động replace các URL HTTP thành HTTPS trong trang chỉ định.</td></tr><tr><td><strong>Server Cache TTL</strong></td><td><br></td><td>Tùy chọn lại thời gian lưu cache trên các Edge Servers hoặc “Bypass Cache” trên trang chỉ định.</td></tr><tr><td><strong>Browser Cache TTL</strong></td><td><br></td><td>Tương tự “Server Cache TTL”, nhưng là quy định thời gian cache trên trình duyệt End-user.</td></tr><tr><td><strong>Bypass Cache By Cookie</strong></td><td>Nhập giá trị “cookie_name” và “cookie_value”</td><td><p>Nếu có cookie được chỉ định từ end-user gửi lên, hệ thống sẽ thực hiện lệnh bypass cache trên trang chỉ định.</p><p>Nếu giá trị “cookie_value” là rỗng, hệ thống chỉ xét nếu tồn tại “cookie_name” và không quan tâm giá trị của “cookie_value”</p></td></tr><tr><td><strong>Bypass Cache By Device Type</strong></td><td>Nhập các giá trị “Agent Text”, hỗ trợ nhiều giá trị, phân cách bởi dấu “Tab” hoặc “Enter”</td><td>Nếu trình duyệt end-user sử dụng có thông tin giống một trong các Agent Text, hệ thống sẽ tự bypass cache trên trang chỉ định.</td></tr><tr><td><strong>Forwarding URL</strong></td><td>Mã chuyển hướng (301/302) và URL đích.</td><td>Tự chuyển hướng URL được chỉ định về URL đích mới.</td></tr><tr><td><strong>Host Header Override</strong></td><td>Header_name và header_value</td><td>Tự động add thêm header trả về cho trình duyệt end-user trên trang được chỉ định.</td></tr><tr><td><strong>Brotli</strong></td><td>ON/OFF</td><td>Tùy chọn bật/tắt Brotli trên trang được chỉ định.</td></tr><tr><td><strong>Gzip</strong></td><td>ON/OFF</td><td>Tùy chọn bật/tắt Gzip trên trang được chỉ định.</td></tr><tr><td><strong>Resolve Origin Override</strong></td><td>IP New Origin</td><td>Tùy chọn thay đổi IP Server Origin ở trang chỉ định.*</td></tr></tbody></table>
