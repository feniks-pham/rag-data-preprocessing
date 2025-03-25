# Quản lý NGLB

VNG cloud cung cấp giao diện trực quan trong việc quản lý NGLB, bao gồm các tính năng quan trọng như:

1. **Khởi tạo Global Load Balancer**
2. **Xem danh sách Global Load Balancer**
3. **Quản lý thông tin chi tiết Global Load Balancer**
4. **Xóa Global Load Balancer**

### **1. Khởi tạo Global Load Balancer** <a href="#manageloadbalancer-nlb-1.khoitaoloadbalancer" id="manageloadbalancer-nlb-1.khoitaoloadbalancer"></a>

Để sử dụng dịch vụ GLB tại VNG Cloud, điều đầu tiên bạn cần làm là khởi tạo một Global Load Balancer theo nhu cầu sử dụng. Tham khảo hướng dẫn dưới đây cho việc khởi tạo một Network Global Load Balancer.

**Cách khởi tạo một Network Global Load Balancer**

1. **Truy cập vào trang chủ Global Load Balancer tại đây:** [**https://glb.console.vngcloud.vn/glb/list**](https://glb.console.vngcloud.vn/glb/list)
2. **Tại trang chủ GLB, click chọn "Create Global Load Balancer".**
3. **Chọn cấu hình Global Load Balancer**
   * _**Tên Load Balancer**_**:** Trường hợp người dùng không chủ động điền tên Load Balancer, hệ thống sẽ tự động sinh ra tên Load Balancer. Lưu ý rằng tên Load balancer không thể thay đổi trong quá trình sử dụng, do đó người dùng nên chủ động nhập tên nếu có nhu cầu quản lý theo tên.
   * _**Layer**_**:** Chọn **"Network - TCP/UDP"**
4. **Chọn cấu hình Listener**
   * **Tên Listener:** Trường hợp người dùng không chủ động điền tên Listener, hệ thống sẽ tự động sinh ra tên Listener.
   * **Giao thức & Cổng (Protocol & Port)**
     * Trường hợp chọn Giao thức (Protocol) = **TCP**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **80)**.
5. **Chọn cấu hình Global Pool mặc định**
   * **Tên Pool**: Trường hợp người dùng không chủ động điền tên Pool, hệ thống sẽ tự động sinh ra tên Pool.
   * **Giao thức: TCP/Proxy** (đối với Listener TCP)
   * **Thuật toán:** Chọn thuật toán cân bằng tải phù hợp
   * **Cài đặt Health Check**: Giao thức: **TCP / HTTP / HTTPS** (đối với Pool TCP/Proxy).
6. **Chọn Global Pool Member: Thêm các máy chủ backend vào Global Pool**
   * Global pool member cho phép người dùng thêm các máy chủ backend từ nhiều Region
   * Chọn **Region, VPC** cho Global pool member
   * Tiếp theo, đính kèm **các máy chủ backend** (từ các subnet trong cùng một VPC) vào pool
7. **Kiểm tra thông tin khởi tạo: Người dùng có thể kiểm tra thông tin cấu hình trước khi hoàn tất khởi tạo, phần thông tin này sẽ được hiển thị phía bên phải màn hình nhập liệu**
   * **Tab "Tóm tắt / Summary"**: Kiểm tra lần lượt các thông tin cấu hình Load Balancer, Listener, Pool và Pool Member
8. **Hoàn tất khởi tạo:** Sau khi hoàn tất việc cấu hình và kiểm tra thông tin, click nút "Tạo Global Load Balancer / Create Load Balancer" để hoàn tất việc khởi tạo.

**Việc khởi tạo ban đầu cho phép cấu hình một Global Listener và một Global Pool tương ứng, sau khi hoàn tất khởi tạo thành công, người dùng có thể truy cập vào chi tiết Global Load Balancer để thêm mới/chỉnh sửa Global Listener và Global Pool tùy ý.**

Lưu ý

Lưu ý rằng phần các thông tin dưới đây sẽ không thể thay đổi sau khi khởi tạo:

* **Tên và định danh**: Bao gồm tên Global Load Balancer, Gloabl Listener và Global Pool
* **Giao thức và Port**: Bao gồm giao thức Global Listener, Global Pool và Health Check

### **2. Xem danh sách Global Load Balancer** <a href="#manageloadbalancer-nlb-2.xemdanhsachloadbalancer" id="manageloadbalancer-nlb-2.xemdanhsachloadbalancer"></a>

Sử dụng hướng dẫn này để phục vụ cho việc xem danh sách tất cả các Load Balancer có sẵn trong hệ thống

**Truy cập danh sách Global Load Balancer**

1. Truy cập vào trang chủ Global Load Balancer tại đây: [https://glb.console.vngcloud.vn/glb/list](https://glb.console.vngcloud.vn/glb/list)
2. Tại trang chủ Global Load Balancer, một danh sách GLB sẽ xuất hiện bao gồm các thông tin như:
   * Tên và định danh Global Load Balancer: Có hỗ trợ sao chép định danh Global Load Balancer nhằm mục đích sử dụng cho Terraform hoặc các nhu cầu khác
   * Trạng thái GLB: Cho biết trạng thái hiện tại của Global Load Balancer
   * Các thông tin khác như: Endpoint,  Loại (Application/Network), Ngày tạo.

**Lọc và Sắp xếp Load Balancer**

Người dùng có thể sắp xếp danh sách Global Load Balancer theo nhu cầu bằng cách nhấn chọn vào tên cột cần sắp xếp tại bảng danh sách Global Load Balancer như: Sắp xếp theo Tên, Trạng Thái, Endpoint, Loại load balancer.&#x20;

**Tìm kiếm Load Balancer**

Để tìm kiếm chính xác một/nhiều Global Load Balancer có tên giống/tương tự nhau, người dùng có thể nhập tên Global Load Balancer vào ô tìm kiếm tại góc trên, bên phải của bảng danh sách Load Balancer.

### **3. Quản lý thông tin chi tiết Global Load Balancer** <a href="#manageloadbalancer-nlb-3.quanlythongtinchitietloadbalancer" id="manageloadbalancer-nlb-3.quanlythongtinchitietloadbalancer"></a>

Truy cập vào Load Balancer để xem và quản lý thông tin chi tiết

**Truy cập chi tiết Load Balancer**

1. Nhấn vào Global Load Balancer cần xem chi tiết tại màn hình danh sách Load Balancer
2. Hướng dẫn xem thông tin Global Load Balancer: Tại màn hình chi tiết Load Balancer chia thành 3 phần chính
   * **Thống kê tính khả dụng**
     * Thống kê tổng số Global Listener trong G Load Balancer
     * Thống kê tổng số G Pool trong G Load Balancer
   * **Thông tin chung của G Load Balancer**
     * Thông tin tên, định danh G Load Balancer&#x20;
     * Endpoint
   * **Thông tin chi tiết**
     * G Listener: Danh sách và thông tin chi tiết từng G Listener&#x20;
     * G Pool: Danh sách và thông tin chi tiết từng G Pool

### **4. Xóa G Load Balancer** <a href="#manageloadbalancer-nlb-6.xoaloadbalancer" id="manageloadbalancer-nlb-6.xoaloadbalancer"></a>

Trước khi thực hiện xóa G Load Balancer, người dùng cần cân nhắc kĩ lưỡng, vì một khi đã xóa, G Load Balancer sẽ không thể khôi phục lại được.

**Cách thực hiện xóa một G Load Balancer**

1. Thực hiện Xóa G Load Balancer theo 2 cách:
   * Tại màn hình danh sách Load Balancer: Nhấn vào **biểu tượng "ba chấm"** tại cuối mỗi hàng thông tin G Load Balancer, một danh sách hành động sẽ hiện ra, **nhấn chọn hành động** **"Xóa"**
   * Tại màn hình chi tiết G Load Balancer: Nhấn vào **hành động "Xóa"** tại góc trên bên phải của màn hình chi tiết
2. Sau khi nhấn chọn "Xóa", một cửa xóa giao diện hiện lên để xác nhận hành động xóa Load Balancer của người dùng
3. Nhấn "Xóa" để hoàn tất việc xóa Load Balancer

**Cách thực hiện xóa nhiều Load Balancer**

1. Truy cập vào màn hình danh sách G Load Balancer
2. Nhấn chọn Load Balancer cần xóa tại check box ở đầu mỗi hàng thông tin Load Balancer
3. Nhấn nút "Xóa" tại góc trên bên trái của bảng danh sách Load Balancer
4. Một cửa xóa giao diện hiện lên để xác nhận hành động xóa Load Balancer của người dùng
5. Nhấn "Xóa" để hoàn tất việc xóa các Load Balancer được chọn
