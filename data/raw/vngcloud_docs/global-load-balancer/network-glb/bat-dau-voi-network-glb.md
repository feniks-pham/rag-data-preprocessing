# Bắt đầu với Network GLB

Trong phần này, chúng ta sẽ tìm hiểu về cách sử dụng và quản lý một Network GLB theo cách cơ bản nhất, từ đó cung cấp cái nhìn tổng quan hơn về việc sử dụng Network GLB.

#### Trước khi bắt đầu <a href="#gettingstarted-nlb-truockhibatdau" id="gettingstarted-nlb-truockhibatdau"></a>

* Tìm hiểu cách **truy cập VNG Cloud Portal** với Root User Account hoặc IAM User Account, tham khảo hướng dẫn [How to Login into VNG Cloud](../../identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md).
* Trong trường hợp người dùng muốn bắt đầu với IAM User Account, tham khảo hướng dẫn [IAM cho GLB.](../../identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/iam-cho-global-load-balancer.md)

#### 1. Truy cập GLB Console <a href="#gettingstarted-nlb-1.truycapvlbconsole" id="gettingstarted-nlb-1.truycapvlbconsole"></a>

GLB Console là giao diện người dùng dựa trên web, cho phép bạn quản lý các Global Load Balancers trong môi trường điện toán đám mây của bạn. Nó cung cấp giao diện một cách trực quan để kiểm soát và quản lý GLBr của bạn.

**Cách truy cập Bảng điều khiển GLB**

* Truy cập từ trang chủ vConsole: [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/)
  * Tại mục **"VNG Cloud Service"** trên giao diện, click **chọn "vServer"**, sau đó click **chọn "GLB"** từ danh sách sản phẩm/dịch vụ tương ứng bên phải
* Truy cập trực tiêp đến vLB Portal thông qua đường dẫn: [https://glb.console.vngcloud.vn/overview](https://glb.console.vngcloud.vn/overview)

#### 2. Khởi tạo Network GLB <a href="#gettingstarted-nlb-2.khoitaonlb" id="gettingstarted-nlb-2.khoitaonlb"></a>

**Cách khởi tạo một Network GLB**

1. **Tại trang chủ Global Load Balancer, click chọn "Create Global Load Balancer".**
2. **Chọn cấu hình Load Balancer**
   * _**Tên Global Load Balancer**_**:** Trường hợp người dùng không chủ động điền tên GLB, hệ thống sẽ tự động sinh ra tên cho GLB đó.
   * _**Layer**_**:** Chọn **"Network - TCP"**
3. **Chọn cấu hình Listener**
   * **Tên Listener:** Trường hợp người dùng không chủ động điền tên Listener, hệ thống sẽ tự động sinh ra tên Listener.
   * **Giao thức & Cổng (Protocol & Port)**
     * Trường hợp chọn Giao thức (Protocol) = **TCP**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **80)**.
4. **Chọn cấu hình Global Pool**
   * **Tên Global Pool**: Trường hợp người dùng không chủ động điền tên Pool, hệ thống sẽ tự động sinh ra tên Pool.
   * **Giao thức: TCP/Proxy** (đối với Listener TCP)
   * **Thuật toán:** Chọn thuật toán cân bằng tải phù hợp
   * **Cài đặt Health Check**: Giao thức: **TCP / HTTP / HTTPS** (đối với Pool TCP/Proxy)
5. **Chọn Global Pool Member: Thêm các máy chủ backend vào Global Pool Member**
   * Global pool member cho phép người dùng thêm các máy chủ backend từ nhiều Region
   * Chọn **Region, VPC** cho Global pool member
   * Tiếp theo, đính kèm **các máy chủ backend** (từ các subnet trong cùng một VPC) vào pool
6. **Kiểm tra thông tin khởi tạo: Người dùng có thể kiểm tra thông tin cấu hình trước khi hoàn tất khởi tạo, phần thông tin này sẽ được hiển thị phía bên phải màn hình nhập liệu**
   * **Tab "Tóm tắt / Summary"**: Kiểm tra lần lượt các thông tin cấu hình GLB, Global Listener, Global Pool và Global Pool Member
7. **Hoàn tất khởi tạo:** Sau khi hoàn tất việc cấu hình và kiểm tra thông tin, click nút "Tạo Global Load Balancer / Create Load Balancer" để hoàn tất việc khởi tạo.

#### 3. Quan sát và kiểm tra NGLB <a href="#gettingstarted-nlb-3.quansatvakiemtranlb" id="gettingstarted-nlb-3.quansatvakiemtranlb"></a>

* Sau khi hoàn tất khởi tạo thành công, hệ thống sẽ điều hướng người dùng đến trang danh sách Global Load Balancer, tại đây người dùng có thể theo dõi trạng thái khởi tạo Global Load Balancer từ **Creating (đang khởi tạo)** đến khi **Active (Khởi tạo thành công).**
* Sau khi khởi tạo thành công, người dùng có thể truy cập vào trang chi tiết Global Load Balancer để quan sát và kiểm tra tính đúng đắn của GLB.

