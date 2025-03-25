# Bắt đầu với vCR

Trong phần này, chúng ta sẽ tìm hiểu về cách sử dụng và quản lý image tại Repository theo cách cơ bản nhất, từ đó cung cấp cái nhìn tổng quan hơn về việc sử dụng dịch vụ Container Registry (vCR).

#### Trước khi bắt đầu <a href="#gettingstarted-vcr-truockhibatdau" id="gettingstarted-vcr-truockhibatdau"></a>

Để bắt đầu sử dụng Container Registry, bạn cần tìm hiểu trước các hướng dẫn/khái niệm sau:

* Nếu chưa có tài khoản VNG Cloud, người dùng cần đăng ký tài khoản để có thể sử dụng dịch vụ. Tham khảo hướng dẫn [Đăng ký tài khoản](../huong-dan-su-dung-tai-khoan/dang-ky-tai-khoan.md)
* Tìm hiểu cách **truy cập VNG Cloud Portal** với Root User Account hoặc IAM User Account, tham khảo hướng dẫn [Cách đăng nhập vào VNG Cloud](../identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md).
* **Tải về và cài đặt Docker/Podman hoặc bất kỳ tool nào** trên máy tính local/oncloud dùng để tương tác với Container Registry.

#### 1. Truy cập vCR Console <a href="#gettingstarted-vcr-1.truycapvcrconsole" id="gettingstarted-vcr-1.truycapvcrconsole"></a>

vCR Console là giao diện người dùng dựa trên web, cho phép bạn quản lý các Repositories, Images, Repository User trong môi trường điện toán đám mây của bạn. Nó cung cấp giao diện một cách trực quan để kiểm soát và quản lý các container images một cách dễ dàng hơn.

**Cách truy cập vCR Console**

* Truy cập trực tiêp đến vCR Console thông qua đường dẫn: [https://vcr.console.vngcloud.vn/list](https://vcr.console.vngcloud.vn/list)
* Truy cập từ trang chủ vServer: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
  * Tại trang chủ vServer, điều hướng đến vCR portal bằng cách click **chọn "Container Registry" trong mục "Container Registry"** tại thanh menu bên trái.
* Truy cập từ trang chủ vConsole: [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/)
  * Tại mục **"VNG Cloud Service"** trên giao diện, click **chọn "vServer"**, sau đó click **chọn "Container Registry"** từ danh sách sản phẩm/dịch vụ tương ứng bên phải

#### 2. Khởi tạo Repository <a href="#gettingstarted-vcr-2.khoitaorepository" id="gettingstarted-vcr-2.khoitaorepository"></a>

**Cách khởi tạo Repository**

1. Tại trang chủ Container Registry, nhấn vào **menu "Repository"** phía bên tay phải để truy cập đến danh sách Repository, nhấn nút **"Create a repository"** để bắt đầu tạo mới một Repository.
2. Một popup **"Create Repository"** hiển thị cho phép bạn điền các thông tin như:
   * **Repository name (optional)**: Tên của Repository, trường hợp không điền tên, hệ thống sẽ tự động sinh ra tên tương ứng. Lưu ý tên sau khi điền/sinh tự động sẽ được add thêm prefix {AccountID} tương ứng với tài khoản VNG Cloud đang đăng nhập.
   * **Access level:** Khả năng truy cập đến Repository (Public / Private).&#x20;
     * Public: Là các Repository mà tại đó, người dùng có thể Pull/Push thoải mái mà không thông qua Repository User
     * Private: Là các Repository mà tại đó, người dùng phải cung cấp đinh danh (username/password) để có thể truy cập đến các Images được quản lý tại Repository này.
   * **Quota Limit:** Dung lượng lưu trữ tối đa mà Repository có thể lưu trữ. Ví dụ bạn điền 20GB, thì Repository của bạn chỉ có thể lưu trữ tối đa 20GB dung lượng. Tuy nhiên, bạn hoàn toàn có thể thay đổi con số này tùy thuộc với nhu cầu tế sau khi khởi tạo.
3. Nhấn **"Create"** để hoàn tất quá trình khởi tạo.
4. Kiểm tra thông tin Repository vừa khởi tạo tại danh sách.

#### 3. Khởi tạo Repository User <a href="#gettingstarted-vcr-3.khoitaorepositoryuser" id="gettingstarted-vcr-3.khoitaorepositoryuser"></a>

**Cách khởi tạo Repository User**

1. Tại trang chủ Container Registry, nhấn vào **menu "Repository User"** phía bên tay phải để truy cập đến danh sách Repository User, nhấn nút **"CreateRepository User"** để bắt đầu tạo mới một Repository User.
2. Một popup **"Create Repository"** hiển thị cho phép bạn điền các thông tin như:
   * **User Name (optional)**: Tên của Repository User, trường hợp không điền tên, hệ thống sẽ tự động sinh ra tên tương ứng. Lưu ý tên sau khi điền/sinh tự động sẽ được add thêm prefix {AccountID} tương ứng với tài khoản VNG Cloud đang đăng nhập.
   * **Expiration Date:** Ngày hết hạn của User. Có 3 chế độ như sau:
     * Để trống: Đồng nghĩa với việc user này không có thời gian expired
     * Điền ngày cụ thể: User này sẽ expired tại thời điểm được chọn. Đối với user bị expired, hệ thống sẽ tạm khóa toàn bộ các tính năng có liên quan đối với Repository User này cho đến khi user được gia hạn thêm thời gian
   * **Description (optional):** Thông tin thêm về Repository User
   * **Repositories (required):** Đính kèm các Repository và cài đặt Permission tương ứng
     * Tìm Repository cần attach theo repository name
     * Nhấn nút "Add"
     * Tại danh sách Repository được thêm vào bên dưới, cài đặt permission tương ứng Push\&Pull/Pull Only
3. Nhấn nút **"Create"** để hoàn tất việc khởi tạo
4. Kiểm tra thông tin Repository vừa khởi tạo tại danh sách

#### 4. Tiến hành Push (Tải lên) Image cần quản lý <a href="#gettingstarted-vcr-4.tienhanhpush-tailen-imagecanquanly" id="gettingstarted-vcr-4.tienhanhpush-tailen-imagecanquanly"></a>

**Cách Push image để lưu trữ tại Repository**

1. Mở docker/podman và đăng nhập với Repository User vừa khởi tạo;
   * User name: Reposiotry Name
   * Password: Reposiotry User Secret Key
2. Truy cập vào vCR Console, nhấn vào Repository cần tải lên image, tại tab **"Image"**, nhấn vào **"Push Command"** để xem nhanh các lệnh cần thao tác.
3. Sao chép lệnh **"Tag an image for this project"** để đánh tag cho image cần push lên.&#x20;
4. Sao chép lệnh **"Push an image to this project"** để push image lên Repository.
5. Kiểm tra xem image đã được push lên thành công hay chưa tại tab "Image" tại trang chi tiết Reposiotry.

\
