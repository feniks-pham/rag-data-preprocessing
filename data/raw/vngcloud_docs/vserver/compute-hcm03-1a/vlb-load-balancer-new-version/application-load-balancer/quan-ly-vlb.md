# Quản lý Load Balancer (ALB)

VNG cloud cung cấp giao diện trực quan trong việc quản lý Load Balancer, bao gồm các tính năng quan trọng như:

1. **Khởi tạo Load Balancer**
2. **Xem danh sách Load Balancer**
3. **Quản lý thông tin chi tiết Load Balancer**
4. **Thay đổi gói Load Balancer**
5. **Nhân bản Load Balancer (Duplicate)**
6. **Xóa Load Balancer**

#### **1. Khởi tạo Load Balancer** <a href="#manageloadbalancer-1.khoitaoloadbalancer" id="manageloadbalancer-1.khoitaoloadbalancer"></a>

Để sử dụng dịch vụ vLB tại VNG Cloud, điều đầu tiên bạn cần làm là khởi tạo một Load Balancer theo nhu cầu sử dụng. Tham khảo hướng dẫn dưới đây cho việc khởi tạo một Application Load Balancer.

**Cách khởi tạo một Application Load Balancer**

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn "Create a Load Balancer".**
3. **Chọn cấu hình Load Balancer**
   * _**Tên Load Balancer**_**:** Trường hợp người dùng không chủ động điền tên Load Balancer, hệ thống sẽ tự động sinh ra tên Load Balancer. Lưu ý rằng tên Load balancer không thể thay đổi trong quá trình sử dụng, do đó người dùng nên chủ động nhập tên nếu có nhu cầu quản lý theo tên.
   * _**Layer**_**:** Chọn **"Application - HTTP/HTTPS"**
   * _**Cơ chế/Scheme**_:
     * Chọn **Internet facing** nếu: Cho phép truy cập từ Internet
     * Chọn **Internal** nếu: Chỉ cho phép truy cập với mạng nội bộ
   * _**Load Balancer Package**_: Chọn gói khởi tạo phù hợp với nhu cầu và mục đích sử dụng, lưu ý rằng gói này là yếu tố chính dùng để tính chi phí khởi tạo và vận hành Load Balancer của bạn. Gói này có thể thay đổi trong quá trình sử dụng.
   * **Auto-scale:** Chọn bật/tắt tính năng auto-scale số lượng LB. Xem chi tiết tính năng auto-scale [tại đây.](../auto-scaling.md)
   * _**Cài đặt Network**_**: Chọn Virtual Private Cloud (VPC) và Subnet** có sẵn từ danh sách VPC của bạn, trường hợp khởi tạo VPC, tham khảo hướng dẫn [Virtual Private Cloud (VPC)](../../network/virtual-private-cloud-vpc/).
4. **Chọn cấu hình Listener**
   * **Tên Listener:** Trường hợp người dùng không chủ động điền tên Listener, hệ thống sẽ tự động sinh ra tên Listener.
   * **Giao thức & Cổng (Protocol & Port)**
     * Trường hợp chọn Giao thức (Protocol) = **HTTP**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **80**) và **Header** (mặc định điền sẵn X-Fowarded-For, X-Forwarded-Proto, X-Fowarded-Port, có thể bỏ chọn Header nếu không có nhu cầu).
     * Trường hợp chọn Giao thức (Protocol) = **HTTPS**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **443**) và **Certificate** (tham khảo hướng dẫn [Upload a certificate](certificate/upload-a-certificate.md) nếu chưa có Certificate).
5. **Chọn cấu hình Pool mặc định**
   * **Tên Pool**: Trường hợp người dùng không chủ động điền tên Pool, hệ thống sẽ tự động sinh ra tên Pool.
   * **Giao thức HTTP mặc định**
   * **Thuật toán:** Chọn thuật toán cân bằng tải phù hợp
   * **Cài đặt Health Check**: Giao thức: TCP / HTTP (nhập đường dẫn mặc định trong trường hợp chọn Giao thức HTTP)
6. **Chọn Pool Member: Thêm các máy chủ backend vào Pool**
   * **Chọn Pool Member** từ một danh sách các máy chủ backend khả dụng thuộc Load Balancer Network
   * **Click nút "Gắn / Attach"** để thực hiện việc thêm máy chủ thành viên
7. **Kiểm tra thông tin khởi tạo: Người dùng có thể kiểm tra thông tin cấu hình và đơn giá trước khi hoàn tất khởi tạo, phần thông tin này sẽ được hiển thị phía bên phải màn hình nhập liệu**
   * **Tab "Tóm tắt / Summary"**: Kiểm tra lần lượt các thông tin cấu hình Load Balancer, Listener, Pool và Pool Member
   * **Tab " Danh sách / Item list":** Kiểm tra thông tin Load Balancer Package và Chi phí
8. **Hoàn tất khởi tạo: Sau khi hoàn tất việc cấu hình và kiểm tra thông tin, click nút "Tạo load Balancer / Create Load Balancer" để hoàn tất việc khởi tạo.**
   * Đối với người dùng trả trước, bạn sẽ được điều hướng đến trang thanh toán, tại đây bạn cần cung cấp một phương thức thanh toán khả dụng để hoàn tất việc khởi tạo Application Load Balancer. Tham khảo thêm hướng dẫn [Thanh toán trực tuyến](../../../../quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/trai-nghiem-billing-and-kenh-thanh-toan/ve-billing-and-payment/thanh-toan/thanh-toan-truc-tuyen.md)

**Việc khởi tạo ban đầu cho phép cấu hình một Listener và một Pool tương ứng, sau khi hoàn tất khởi tạo thành công, người dùng có thể truy cập vào chi tiết Load Balancer để thêm mới/chỉnh sửa Listener và Pool tùy ý.**

Lưu ý

Lưu ý rằng phần các thông tin dưới đây sẽ không thể thay đổi sau khi khởi tạo:

* **Tên và định danh**: Bao gồm tên Load Balancer, Listener và Pool
* **Phần** **thông tin chung** của Load Balancer: Bao gồm **Layer, Cơ chế (Scheme), Network và Subnet**
* **Giao thức và Port**: Bao gồm giao thức Listener, Pool và Health Check

#### **2. Xem danh sách Load Balancer** <a href="#manageloadbalancer-2.xemdanhsachloadbalancer" id="manageloadbalancer-2.xemdanhsachloadbalancer"></a>

Sử dụng hướng dẫn này để phục vụ cho việc xem danh sách tất cả các Load Balancer có sẵn trong hệ thống

**Truy cập danh sách Load Balancer**

1. Truy cập vào trang chủ Load Balancer tại đây: [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. Tại trang chủ Load Balancer, một danh sách Load Balancer sẽ xuất hiện bao gồm các thông tin như:
   * Tên và định danh Load Balancer: Có hỗ trợ sao chép định danh Load Balancer nhằm mục đích sử dụng cho Terraform hoặc các nhu cầu khác
   * Trạng thái Load Balancer: Cho biết trạng thái hiện tại của Load Balancer
   * Các thông tin khác như: Endpoint, Cơ chế (Internet/Internal), Loại (Application/Network), Gói sử dụng, Ngày tạo.

**Lọc và Sắp xếp Load Balancer**

Người dùng có thể sắp xếp danh sách Load Balancer theo như cầu bằng cách nhấn chọn vào tên cột cần sắp xếp tại bảng danh sách Load Balancer như: Sắp xếp theo Tên, Trạng Thái, Endpoint, Cơ chế, Loại load balancer.&#x20;

**Tìm kiếm Load Balancer**

Để tìm kiếm chính xác một/nhiều Load Balancer có tên giống/tương tự nhau, người dùng có thể nhập tên Load Balancer vào ô tìm kiếm tại góc trên, bên phải của bảng danh sách Load Balancer.

#### **3. Quản lý thông tin chi tiết Load Balancer** <a href="#manageloadbalancer-3.quanlythongtinchitietloadbalancer" id="manageloadbalancer-3.quanlythongtinchitietloadbalancer"></a>

Truy cập vào Load Balancer để xem và quản lý thông tin chi tiết

**Truy cập chi tiết Load Balancer**

1. Nhấn vào Load Balancer cần xem chi tiết tại màn hình danh sách Load Balancer
2. Hướng dẫn xem thông tin Load Balancer: Tại màn hình chi tiết Load Balancer chia thành 3 phần chính
   * **Thống kê tính khả dụng**
     * Thống kê tổng số Listener trong Load Balancer
     * Thống kê tổng số Pool trong Load Balancer
     * Thống kê số lượng Pool đang hoạt động tốt / Tổng số Pool
     * Thống kê số lượng Pool đang hoạt động không tốt / Tổng số Pool
   * **Thông tin chung của Load Balancer**
     * Thông tin tên, định danh Load Balancer&#x20;
     * Cơ chế / Scheme (Internet / Internal)
     * Private subnet & Endpoint
     * Thông tin gói Load Balancer: Connections, Data Transfer, Package name
   * **Thông tin chi tiết**
     * Listener: Danh sách và thông tin chi tiết từng Listener&#x20;
     * Pool: Danh sách và thông tin chi tiết từng Pool
     * Monitor: Danh sách Metrics và Logs

Thông tin

Tìm hiểu thêm thông tin chi tiết Load Balancer thông qua các bài viết sau:

* [Listener](listener/)
* [Pool](pool/)
* [Monitor your load balancers](quan-ly-vlb.md)

#### **4. Thay đổi gói Load Balancer (Resize)** <a href="#manageloadbalancer-4.thaydoigoiloadbalancer-resize" id="manageloadbalancer-4.thaydoigoiloadbalancer-resize"></a>

Tính năng "Thay Đổi gói Load Balancer" là một phần quan trọng trong việc quản lý Load Balancer của bạn. Nó cho phép bạn tùy chỉnh và cập nhật các gói dịch vụ phù hợp với nhu cầu sử dụng cả về mặt tài chính lẫn vận hành của một Load Balancer như:

* Tăng hoặc giảm Connection cũng như Data Transfer để đáp ứng việc thay đổi tải lưu lượng.
* Tối ưu hóa cấu hình gói Load Balancer để phù hợp với nhu cầu thực tế sau thời gian dài sử dụng.

**Cách thay đổi gói Load Balancer**

1. Thực hiện Resize Load Balancer theo 2 cách:
   * Tại màn hình danh sách Load Balancer: Nhấn vào **biểu tượng "ba chấm"** tại cuối mỗi hàng thông tin Load Balancer, một danh sách hành động sẽ hiện ra, **nhấn chọn hành động** **"Resize"**
   * Tại màn hình chi tiết Load Balancer: Nhấn vào **hành động "Resize"** tại góc trên bên phải của màn hình chi tiết
2. Sau khi nhấn chọn "Resize", một cửa sổ giao diện hiện lên, bao gồm danh sách các gói Load Balancer khả dụng, **nhấn chọn gói cần sử dụng**.
3. Kiểm tra và So sánh 2 gói: Sau khi chọn gói, người dùng có thể **so sánh thông tin gói hiện tại và gói mới** tại phần thông tin bên phải cửa sổ bật lên, về cả cấu hình lẫn chi phí.
4. Xác nhận thay đổi: Sau khi đã chắc chắn, nhấn **chọn nút "Resize Load Balancer"** tại góc dưới bên phải của cửa sổ bật lên để kết thúc quá trình Resize.

Lưu ý

**Một vài lưu ý cần biết khi thực hiện Resize:**

* Đối với người dùng trả trước, hệ thống sẽ điều hướng giao diện đến trang thanh toán để hoàn tất quá trình
* Quá trình Resize sẽ diễn ra trong một khoảng thời gian nhất định, do đó, Load Balancer của bạn sẽ bị gián đoạn trong thời gian này và tiếp tục hoạt động bình thường sau khi hoàn tất quá trình.
* Sau khi Resize thành công, người dùng cần kiểm tra các thông số/dữ liệu thực tế của Load Balancer tại tab Monitor, để đảm bảo rằng gói Load Balancer mới có thể đáp ứng nhu cầu sử dụng thực tế.

#### **5. Duplicate Load Balancer** <a href="#manageloadbalancer-5.duplicateloadbalancer" id="manageloadbalancer-5.duplicateloadbalancer"></a>

Tính năng "Duplicate Load Balancer" là một phần quan trọng trong việc quản lý Load Balancer của bạn. Nó cho phép bạn tạo bản sao chính xác của một Load Balancer hiện có để sử dụng cho các mục đích khác nhau hoặc để đảm bảo tính dự phòng của hệ thống của bạn.

**Tại sao cần Duplicate Load Balancer?**

Có nhiều lý do mà bạn có thể muốn nhân bản một Load Balancer:

* Đảm bảo tính dự phòng và sẵn sàng của ứng dụng.
* Tạo một môi trường thử nghiệm hoặc phát triển không ảnh hưởng đến ứng dụng hiện tại.
* Tạo bản sao của cấu hình đã được kiểm tra và chứng minh để triển khai cho các ứng dụng mới.

**Cách thực hiện Duplicate Load Balancer**

1. Thực hiện Resize Load Balancer theo 2 cách:
   * Tại màn hình danh sách Load Balancer: Nhấn vào **biểu tượng "ba chấm"** tại cuối mỗi hàng thông tin Load Balancer, một danh sách hành động sẽ hiện ra, **nhấn chọn hành động** **"Duplicate"**
   * Tại màn hình chi tiết Load Balancer: Nhấn vào **hành động "Duplicate"** tại góc trên bên phải của màn hình chi tiết
2. Sau khi nhấn chọn "Duplicate", một cửa sổ giao diện hiện lên cho phép bạn cấu hình các thông tin cần thiết, bao gồm:
   * **Tên Load Balancer**
   * **Gói Load Balancer**
   * **Thông tin Listener:** Để phù hợp với nhu cầu sử dụng thực tế, tính năng Duplicate cho phép người chỉnh sửa thông tin Listener khi Duplicate như
     * Thêm/Xóa/Sửa Certificate, SNI cho Listener
     * Remove các Listener không cần thiết đối với Load Balancer mới
3. Kiểm tra thông tin gói Load Balancer: Thông tin về cấu hình và chi phí tại phần bên phải của cửa sổ bật lên
4. Xác nhận Duplicate: Sau khi đã chắc chắn, nhấn **chọn nút "Duplicate Load Balancer"** tại góc dưới bên phải của cửa sổ bật lên để kết thúc quá trình Duplicate.

Lưu ý

**Một vài lưu ý cần biết khi thực hiện Duplicate:**

* Đối với người dùng trả trước, hệ thống sẽ điều hướng giao diện đến trang thanh toán để hoàn tất quá trình
* Việc Duplicate đảm bảo Load Balancer mới được tạo ra với cấu hình chính xác 100% từ Load Balancer được chọn (trừ khi thay đổi gói Load Balancer và Listener).
* Duplicate Load Balancer sẽ mất một khoảng thời gian nhất định, trường hợp Load Balancer được chọn để Duplicate cấu hình càng phức tạp thì thời gian cung cấp dịch vụ càng mất thời gian.

#### **6. Xóa Load Balancer** <a href="#manageloadbalancer-6.xoaloadbalancer" id="manageloadbalancer-6.xoaloadbalancer"></a>

Trước khi thực hiện xóa Load Balancer, người dùng cần cân nhắc kĩ lưỡng, vì một khi đã xóa, Load Balancer sẽ không thể khôi phục lại được.

**Cách thực hiện xóa một Load Balancer**

1. Thực hiện Xóa Load Balancer theo 2 cách:
   * Tại màn hình danh sách Load Balancer: Nhấn vào **biểu tượng "ba chấm"** tại cuối mỗi hàng thông tin Load Balancer, một danh sách hành động sẽ hiện ra, **nhấn chọn hành động** **"Xóa"**
   * Tại màn hình chi tiết Load Balancer: Nhấn vào **hành động "Xóa"** tại góc trên bên phải của màn hình chi tiết
2. Sau khi nhấn chọn "Xóa", một cửa xóa giao diện hiện lên để xác nhận hành động xóa Load Balancer của người dùng
3. Nhấn "Xóa" để hoàn tất việc xóa Load Balancer

**Cách thực hiện xóa nhiều Load Balancer**

1. Truy cập vào màn hình danh sách Load Balancer
2. Nhấn chọn Load Balancer cần xóa tại check box ở đầu mỗi hàng thông tin Load Balancer
3. Nhấn nút "Xóa" tại góc trên bên trái của bảng danh sách Load Balancer
4. Một cửa xóa giao diện hiện lên để xác nhận hành động xóa Load Balancer của người dùng
5. Nhấn "Xóa" để hoàn tất việc xóa các Load Balancer được chọn

{% hint style="info" %}
**Lưu ý**

Đối với người dùng trả trước, trường hợp xóa Load Balancer trước thời hạn, người dùng sẽ được hoàn phí dịch vụ theo thời gian sử dụng thực tế.
{% endhint %}

\
