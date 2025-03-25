# Bắt đầu sử dụng

Trong phần này, chúng ta sẽ tìm hiểu về cách sử dụng và quản lý một Network Load Balancer (NLB) theo cách cơ bản nhất, từ đó cung cấp cái nhìn tổng quan hơn về việc sử dụng Network Load Balancer.

#### Trước khi bắt đầu <a href="#gettingstarted-nlb-truockhibatdau" id="gettingstarted-nlb-truockhibatdau"></a>

* Để bắt đầu sử dụng Network Load Balancer, bạn cần có ít nhất **một Virtual Private Cloud (VPC)**, tham khảo hướng dẫn [Virtual Private Cloud (VPC)](../../network/virtual-private-cloud-vpc/).
* Tìm hiểu cách **truy cập VNG Cloud Portal** với Root User Account hoặc IAM User Account, tham khảo hướng dẫn [How to Login into VNG Cloud](../../../../identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md).
* Trong trường hợp người dùng muốn bắt đầu với IAM User Account, tham khảo hướng dẫn [IAM for vServer](../../../../identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/iam-cho-vserver.md).

#### 1. Truy cập vLB Console <a href="#gettingstarted-nlb-1.truycapvlbconsole" id="gettingstarted-nlb-1.truycapvlbconsole"></a>

vLB Console là giao diện người dùng dựa trên web, cho phép bạn quản lý các Load Balancers trong môi trường điện toán đám mây của bạn. Nó cung cấp giao diện một cách trực quan để kiểm soát và quản lý Load Balancer của bạn.

**Cách truy cập Bảng điều khiển vLB**

* Truy cập từ trang chủ vConsole: [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/)
  * Tại mục **"VNG Cloud Service"** trên giao diện, click **chọn "vServer"**, sau đó click **chọn "vLB"** từ danh sách sản phẩm/dịch vụ tương ứng bên phải
* Truy cập từ trang chủ vServer: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
  * Tại trang chủ vServer, điều hướng đến vLB portal bằng cách click **chọn "Load Balancers" trong mục "Load Balancing"** tại thanh menu bên trái.
* Truy cập trực tiêp đến vLB Portal thông qua đường dẫn: [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)

#### 2. Khởi tạo NLB <a href="#gettingstarted-nlb-2.khoitaonlb" id="gettingstarted-nlb-2.khoitaonlb"></a>

**Cách khởi tạo một Network Load Balancer**

1. **Tại trang chủ Load Balancer, click chọn "Create a Load Balancer".**
2. **Chọn cấu hình Load Balancer**
   * _**Tên Load Balancer**_**:** Trường hợp người dùng không chủ động điền tên Load Balancer, hệ thống sẽ tự động sinh ra tên Load Balancer.
   * _**Layer**_**:** Chọn **"Network - TCP/UDP"**
   * _**Cơ chế/Scheme**_:
     * Chọn **Internet facing** nếu: Cho phép truy cập từ Internet
     * Chọn **Internal** nếu: Chỉ cho phép truy cập với mạng nội bộ
   * _**Load Balancer Package**_: Chọn gói khởi tạo phù hợp với nhu cầu và mục đích sử dụng, lưu ý rằng gói này là yếu tố chính dùng để tính chi phí khởi tạo và vận hành Load Balancer của bạn
   * **Auto-scale:** Chọn bật/tắt tính năng auto-scale số lượng LB. Xem chi tiết tính năng auto-scale [tại đây.](../auto-scaling.md)
   * _**Cài đặt Network**_**: Chọn Virtual Private Cloud (VPC) và Subnet** có sẵn từ danh sách VPC của bạn, trường hợp chưa khởi tạo VPC, tham khảo hướng dẫn [Virtual Private Cloud (VPC)](../../network/virtual-private-cloud-vpc/).
3. **Chọn cấu hình Listener**
   * **Tên Listener:** Trường hợp người dùng không chủ động điền tên Listener, hệ thống sẽ tự động sinh ra tên Listener.
   * **Giao thức & Cổng (Protocol & Port)**
     * Trường hợp chọn Giao thức (Protocol) = **TCP**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **80)**.
     * Trường hợp chọn Giao thức (Protocol) = **UDP**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **53**).
4. **Chọn cấu hình Pool mặc định**
   * **Tên Pool**: Trường hợp người dùng không chủ động điền tên Pool, hệ thống sẽ tự động sinh ra tên Pool.
   * **Giao thức: TCP/Proxy** (đối với Listener TCP) hoặc **UDP** (đối với Listener UDP)
   * **Thuật toán:** Chọn thuật toán cân bằng tải phù hợp
   * **Cài đặt Health Check**: Giao thức: **TCP / HTTP / HTTPS** (đối với Pool TCP/Proxy) hoặc **PING-UDP** (đối với Pool UDP)
5. **Chọn Pool Member: Thêm các máy chủ backend vào Pool**
   * **Chọn Pool Member** từ một danh sách các máy chủ backend khả dụng thuộc Load Balancer Network (cùng subnet với LB)
   * **Click nút "Gắn / Attach"** để thực hiện việc thêm máy chủ thành viên
6. **Kiểm tra thông tin khởi tạo: Người dùng có thể kiểm tra thông tin cấu hình và đơn giá trước khi hoàn tất khởi tạo, phần thông tin này sẽ được hiển thị phía bên phải màn hình nhập liệu**
   * **Tab "Tóm tắt / Summary"**: Kiểm tra lần lượt các thông tin cấu hình Load Balancer, Listener, Pool và Pool Member
   * **Tab " Danh sách / Item list":** Kiểm tra thông tin Load Balancer Package và Chi phí
7. **Hoàn tất khởi tạo: Sau khi hoàn tất việc cấu hình và kiểm tra thông tin, click nút "Tạo load Balancer / Create Load Balancer" để hoàn tất việc khởi tạo.**
   * Đối với người dùng trả trước, bạn sẽ được điều hướng đến trang thanh toán, tại đây bạn cần cung cấp một phương thức thanh toán khả dụng để hoàn tất việc khởi tạo Application Load Balancer. Tham khảo thêm hướng dẫn [Thanh toán trực tuyến](../../../../quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/trai-nghiem-billing-and-kenh-thanh-toan/ve-billing-and-payment/thanh-toan/thanh-toan-truc-tuyen.md)

#### 3. Quan sát và kiểm tra NLB <a href="#gettingstarted-nlb-3.quansatvakiemtranlb" id="gettingstarted-nlb-3.quansatvakiemtranlb"></a>

* Sau khi hoàn tất khởi tạo thành công, hệ thống sẽ điều hướng người dùng đến trang danh sách Load Balancer, tại đây người dùng có thể theo dõi trạng thái khởi tạo Load Balancer từ **Creating (đang khởi tạo)** đến khi **Active (Khởi tạo thành công).**
* Sau khi khởi tạo thành công, người dùng có thể truy cập vào trang chi tiết Load Balancer để quan sát và kiểm tra tính đúng đắn của Load Balancer.

