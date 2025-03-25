# Dashboard

### Tổng quan <a href="#dashboard-tongquan" id="dashboard-tongquan"></a>

Dashboard là một công cụ trực quan hóa dữ liệu giúp người dùng có thể nhanh chóng tìm ra những thông tin quan trọng và hiểu rõ hơn về dữ liệu. Một Dashboard trong vMonitor Platform là một nhóm các biểu đồ sử dụng để theo dõi tài nguyên của bạn từ một số dịch vụ, ứng dụng, máy chủ nhất định. Nhóm biểu đồ sẽ thể hiện cho bạn thấy sức khỏe của hệ thống một cách rõ ràng.&#x20;

Trên hệ thống vMonitor Platform, có 2 loại Dashboard được chúng tôi định nghĩa bao gồm:&#x20;

* **Dashboard mặc định**: là loại Dashboard được tự động tạo bởi hệ thống của chúng tôi ngay khi bạn bật monitoring trong các dịch vụ bạn đang sử dụng hoặc khi bạn thiết lập thành công monitoring các hosts của mình. Đặc điểm của loại Dashboard này là bạn có thể xem, tạo bản sao và không thể thay đổi các thông số cũng như các Widget nằm trong Dashboard.&#x20;
* **Dashboard tùy chỉnh**: là loại Dashboard được tạo bởi chính bạn. Đặc điểm của loại Dashboard này là bạn có toàn quyền xem, tạo mới, tạo bản sao, chỉnh sửa thông số cũng như thêm bớt hay sắp xếp các Widget nằm trong Dashboard theo ý muốn của mình.&#x20;

***

### Phạm vi giới hạn Dashboard <a href="#dashboard-phamvigioihandashboard" id="dashboard-phamvigioihandashboard"></a>

**Quy tắc đặt tên Dashboard**

Các quy tắc sau áp dụng cho việc đặt tên Dashboard trong vMonitor Platform:

* Tên Dashboard phải dài từ 1 (tối thiểu) đến 50 (tối đa) ký tự.
* Tên Dashboard chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-) , ký tự / và ký tự @.
* Tên Dashboard không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...).&#x20;
* Tên Dashboard phải là duy nhất trong một tài khoản VNG Cloud cho đến khi Dashboard đó bị xóa.&#x20;

Ví dụ minh họa

* Các tên Dashboard ví dụ sau đây hợp lệ và tuân theo các nguyên tắc đặt tên được đề xuất:
  * monitor\_host@1
  * logproject-DashboardA
  * ...
* Các tên Dashboard ví dụ sau đây hợp lệ nhưng chúng tôi không khuyến khích bạn sử dụng:
  * [docexamplewebsite.com](http://docexamplewebsite.com/)
  * 1.1.1.2/10
  * ...
* Các tên Dashboard ví dụ sau không hợp lệ:
  * Report\_usage\_80\_% (chứa ký tự %)
  * Dashboard\&Report (chứa ký tự &)
  * ...

***

### Khởi tạo Dashboard <a href="#dashboard-khoitaodashboard" id="dashboard-khoitaodashboard"></a>

Để khởi tạo một Dashboard, bạn có thể sử dụng vMonitor Platform theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Dashboard.**
3. Chọn **Create a Dashboard.**
4. Màn hình **Create Dashboard** được hiển thị. Nhập **Dashboard name**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho Dashboard của bạn. Đừng lo lắng, sau khi tạo Dashboard, bạn có thể thay đổi tên cho Dashboard của bạn.&#x20;
5. chọn **Create**.

***

### Xem danh sách Dashboard <a href="#dashboard-xemdanhsachdashboard" id="dashboard-xemdanhsachdashboard"></a>

Để xem các Dashboards, bạn có thể:&#x20;

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Dashboard.**
3. Trên trang hiển thị danh sách **Dashboard** hiển thị, bạn có thể lọc hiển thị danh sách **Dashboard** theo các Loại Dashboard và ý nghĩa được mô tả tại các bảng bên dưới:

<table data-header-hidden><thead><tr><th width="194"></th><th></th></tr></thead><tbody><tr><td><strong>Loại Dashboard</strong></td><td><strong>Mô tả</strong></td></tr><tr><td>All Dashboards</td><td>Tất cả các dashboard đang có</td></tr><tr><td>All host</td><td>Tất cả các Dashboard được tạo tự động bởi vMonitor Platform khi bạn thiết lập một Host.</td></tr><tr><td>All integration</td><td>Tất cả các Dashboard được tạo tự động bởi vMonitor Platform khi bạn thiết lập các ứng dụng tích hợp.</td></tr><tr><td>All VNG Cloud</td><td>Tất cả các Dashboard được tạo bởi hệ thống vMonitor Platform cho các Product của VNG Cloud</td></tr><tr><td>Created by you</td><td>Các Dashboard được tạo bởi người sử dụng</td></tr><tr><td>Favourite</td><td>Các Dashboard được đánh dấu là yêu thích.</td></tr></tbody></table>

Bạn có thể đánh dấu 1 **Dashboard tùy chỉnh** là Dashboard yêu thích cũng như bỏ chúng khỏi danh sách yêu thích bằng cách chọn <img src="../../../.gitbook/assets/image (47).png" alt="" data-size="line">trên mỗi **Dashboard**. Khi biểu tượng trên Dashboard là <img src="../../../.gitbook/assets/image (48).png" alt="" data-size="line">nghĩa là **Dashboard** đã được thêm vào danh sách yêu thích thành công và ngược lại khi biểu tượng trên **Dashboard** là <img src="../../../.gitbook/assets/image (49).png" alt="" data-size="line">nghĩa là **Dashboard** chưa được thêm vào danh sách yêu thích thành công.

***

### Thay đổi tên Dashboard <a href="#dashboard-thaydoitendashboard" id="dashboard-thaydoitendashboard"></a>

Để thay đổi tên của Dashboard là bạn đã tạo trước đó, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Dashboard.**
3. Tại **Dashboard** mà bạn muốn thay đổi tên, chọn biểu tượng<img src="../../../.gitbook/assets/image (50).png" alt="" data-size="line">
4. Chọn **Rename**.
5. Nhập **Dashboard name**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho Dashboard của bạn.&#x20;
6. Chọn **Save**.

Bạn chỉ có thể thay đổi tên những Dashboard được tạo bởi chính bạn. Đối với những **Dashboard mặc định** được tạo tự động bởi hệ thống của chúng tôi, bạn không thể đổi tên mà chỉ có thể tạo bản sao Dashboard.

***

### Tạo bản sao Dashboard <a href="#dashboard-taobansaodashboard" id="dashboard-taobansaodashboard"></a>

Để tạo bản sao cho một Dashboard, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Dashboard.**
3. Tại **Dashboard** mà bạn muốn tạo bản sao, chọn <img src="../../../.gitbook/assets/image (51).png" alt="" data-size="line">
4. Chọn **Clone Dashboard.**
5. Nhập **Dashboard name**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho Dashboard của bạn.&#x20;
6. Chọn **Clone.**

Lúc này một **Dashboard** mới với thông số giống như **Dashboard** ban đầu được tạo. Trên **Dashboard** mới này, bạn có thể thực hiện tùy chỉnh các thông số cũng như cấu hình thêm, xóa Widget theo mong muốn.

***

### Xóa Dashboard <a href="#dashboard-xoadashboard" id="dashboard-xoadashboard"></a>

Khi bạn không có nhu cầu sử dụng một **Dashboard** tùy chỉnh nữa, bạn có thể thực hiện xóa **Dashboard** khỏi hệ thống theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Dashboard.**
3. Tại **Dashboard** mà bạn muốn xóa, chọn <img src="../../../.gitbook/assets/image (52).png" alt="" data-size="line">
4. Chọn **Delete**.
5. Tại màn hình xác nhận xóa Dashboard, chọn **Delete**.

Sau khi bạn thực hiện xóa thành công thì **Dashboard** của bạn sẽ bị xóa hoàn toàn khỏi hệ thống của chúng tôi. Bạn không thể khôi phục lại **Dashboard** đã xóa nên hãy lưu ý cẩn thận khi sử dụng tính năng này.&#x20;
