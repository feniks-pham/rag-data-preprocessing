# Trải nghiệm sản phẩm vServer

Sử dụng hướng dẫn này để bắt đầu với VNG Cloud (vServer). Bạn sẽ học cách khởi chạy, kết nối và sử dụng. Một ví dụ điển hình cho việc khởi tạo một máy chủ ảo trong đám mây của VNG Cloud. với vServer, bạn có thể thiết lập và định cấu hình hệ điều hành cũng như các ứng dụng đi kèm dự kiến.

Khi lần đầu đăng ký dịch vụ vServer, bạn có thể bắt đầu với việc sử dụng miễn phí để có sự trải nghiệm tuyệt vời trước khi quyết định thanh toán. Nếu bạn đã tạo tài khoản của mình trong 3 ngày và chưa vượt quá lợi ích của cấp miễn phí cho vServer, bạn sẽ không mất bất kỳ chi phí nào để hoàn thành hướng dẫn này vì chúng tôi giúp bạn chọn các tùy chọn nằm trong lợi ích của cấp miễn phí. Khi kết thúc cấp miễn phí, bạn sẽ phải chịu phí sử dụng vServer tiêu chuẩn kể từ thời điểm bạn khởi chạy cho đến khi bạn kết thúc phiên bản, ngay cả khi nó không hoạt động.

### **Tổng quan** <a href="#trainghiemsanphamvserver-tongquan" id="trainghiemsanphamvserver-tongquan"></a>

Bạn cần hoàn tất các bước sau để có thể sử dụng dịch vụ vServer của chúng tôi:

***

### **Bước 1: Kích hoạt vServer:** <a href="#trainghiemsanphamvserver-buoc1-kichhoatvserver" id="trainghiemsanphamvserver-buoc1-kichhoatvserver"></a>

1. Mở trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview)
2. Đối với tài khoản của khách hàng mới, để có thể sử dụng được dịch vụ trước tiên bạn cần kích hoạt vServer bằng cách khởi tạo một Project. Ở tab "**Overview"** nhấn chọn **Active**

***

### **Bước 2: Khởi tạo VPC:** <a href="#trainghiemsanphamvserver-buoc2-khoitaovpc" id="trainghiemsanphamvserver-buoc2-khoitaovpc"></a>

Tiếp theo để khởi tạo được vServer, bạn cần có VPC:

1. Mở trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview)
2. Tại thanh menu điều hướng, chọn Tab **VPC**
3. Chọn **Tạo VPC**
4. Đối với **Tên** hãy nhập tên mô tả cho VPC. Tên VPC có thể bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào nằm trong khoảng từ 5 đến 50. Nó không được bao gồm khoảng trắng ở đầu hoặc ở cuối.
5. Nhập thông tin IP tại mục **CIDR** . Địa chỉ IP nên là Private và có thể được lựa chọn cho các giá trị sau:
   * 10.0.0.0 - 10.255.0.0
   * 172.16.0.0 - 172.24.0.0
   * 192.168.0.0

***

### **Bước 3: Khai báo Subnet:** <a href="#trainghiemsanphamvserver-buoc3-khaibaosubnet" id="trainghiemsanphamvserver-buoc3-khaibaosubnet"></a>

Sau khi khởi tạo hoàn tất VPC ban đầu, cần thực hiện thêm một bước khởi tạo Subnet. Chúng ta có thể tạo nhiều Subnet cho VPC của mình:

1. Mở tab VPC tại: [https://hcm-3.console.vngcloud.vn/vserver/network/vpc](https://hcm-3.console.vngcloud.vn/vserver/network/vpc)
2. Nhấn chọn **VPC** của mình, chọn tab **Subnet** tại cuối trang và chọn **Add Subnet**
3. Đối với **Name**, hãy nhập tên mô tả cho Subnet. Tên Subnet có thể bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào nằm trong khoảng từ 5 đến 50. Nó không được bao gồm khoảng trắng ở đầu hoặc ở cuối.
4. Nhập thông tin **IP** tại mục **CIDR** . Giá trị CIDR của Subnet phải thuộc lớp mạng của VPC đã tạo trước đó. Ví dụ: VPC trước đó chúng ta tạo với CIDR là 192.168.0.0/16 thì Subnet sẽ có dạng: 192.168.xxx.0/24

***

### **Bước 4: Khởi tạo Server:** <a href="#trainghiemsanphamvserver-buoc4-khoitaoserver" id="trainghiemsanphamvserver-buoc4-khoitaoserver"></a>

Hướng dẫn này giúp bạn nhanh chóng khởi chạy **Server** đầu tiên của mình, vì vậy nó sẽ không bao gồm tất cả các tùy chọn phải có, tuy nhiên bạn sẽ sử dụng Server chỉ sau vài thao tác đơn giản sau đây:

1. Mở tab Server tại: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Chọn **Create a Server**
3. Ở mục **Basic Configuration**, nhập **Server name** để mô tả tên cho Server của bạn. Tên Server có thể bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào nằm trong khoảng từ 5 đến 50. Nó không được bao gồm khoảng trắng ở đầu hoặc ở cuối và tên Server name phải khác với Username
4. Lựa chọn theo các tùy chọn sau tại mục **Image:**

**Option 1**: Khởi tạo vServer từ một OS trống hoàn toàn mới

* Tại tab **OS IMAGES**, chọn OS Type (_Ubuntu, Debian, CentOS, Windows, ..._) và version OS tương ứng, chọn **Next**

**Option 2**: Khởi tạo vServer với **GPU IMAGES** hỗ trợ nâng cao cho xử lý đồ họa

* Tại tab **GPU IMAGES**, chọn OS Type (_Ubuntu, Windows, ..._) và version OS tương ứng, chọn **Next**

**Option 3**: Khởi tạo vServer với **MY IMAGES** đã được tạo ra trước đó, nhằm phục vụ cho việc Clone Server đang chạy trên Cloud thành các Server mới hoặc Backup / Restore Server

* Tại tab **My Images**, chọn images tương ứng cần để tạo vServer, chọn **Next**. Hoặc bạn có thể tạo riêng cho mình một Image bằng cách nhấn vào [**đây**](../image.md) _để xem hướng dẫn tạo MY IMAGES_

5\. Dưới mục **Instance type,** là danh sách các cấu hình Flavor, bạn có thể chọn cấu hình Flavor mong muốn cho Server của mình theo. **iot.v1.small1x1** được chúng tôi đề xuất như một cấu hình cơ bản mặc định để khởi tạo Server

6\. Ở mục **Volume Settings**, nhập cấu hình cho Boot OS Volume (Root) gồm **Size GB**, **Volume Type SSD** và **IOPS**, sau đó chọn **Next**

Ngoài ra có thể thêm **Data Volume** vào Server trong quá trình khởi tạo bằng cách chọn **Add Data volume,** sau đó **n**hập cấu hình cho Data Volume gồm **Volume name**, **Size GB**, **Volume Type SSD** và **IOPS**, chọn **Next**

7\. Kế tiếp là mục **Network settings:**

\+  Tại đây có thể chọn **VPC** để cấp Private IP cho Server và **Subnet** từ danh sách bạn đã tạo trước đó, hoặc có thể nhấn vào [**đây**](https://hcm-3.console.vngcloud.vn/vserver/network/vpc) để tạo mới VPC và Subnet, cần lưu ý ràng sau khi tạo VPC và Subnet, nó sẽ hiển thị tại trang danh sách cho phép bạn chọn trong quá trình khởi tạo Server

\+  Tích vào ô Floating IP để gán Public IP cho Server (Nhấn vào [**đây**](../network/floating-ip/) để xem hướng dẫn attach/ detach Floating IP)

\+  **Security group** để quản lý bộ ACL - Access Control List cho Server. (Nhấp vào [**đây**](../security/security-groups.md) để xem hướng dẫn tạo và quản lý Security group)

\+  **SSH Key** để import vô Server trong quá trình khởi tạo. (Nhấp vào [**đây**](../security/ssh-key-bo-khoa.md) để xem hướng dẫn tạo SSH Key)

\+  Thông tin **Authentication**: Empty: hệ thống sẽ tự động tạo và gắn password hoặc user tự tinh chỉnh và enable hay disable việc bỏ qua change password lần đầu.

8\. Ở mục **Other Settings**, có thể tùy chọn server Group hoặc không theo nhu cầu sử dụng. Bạn có thể gán Server vào các Group trước đó đã tạo (Với các thuộc tính như cùng Compute Host hay khác Compute Host)

***

### **Bước 5: Thanh toán và hoàn tất quá trình khởi tạo Server:** <a href="#trainghiemsanphamvserver-buoc5-thanhtoanvahoantatquatrinhkhoitaoserver" id="trainghiemsanphamvserver-buoc5-thanhtoanvahoantatquatrinhkhoitaoserver"></a>

Sau khi điền các thông tin cần thiết để khởi tạo Server, cần xem lại tóm tắt các thông tin thanh toán tại tab **Summary** phía bên trái màn hình và thông tin thanh toán chi tiết các mục tại tab **Item list.** Nếu bạn đã sẵn sàng hãy chọn **Launch Server** để xác nhận khởi tạo Server của bạn.

Trên màn hình danh sách Server, bạn có thể xem trạng thái khởi chạy. Phải mất một thời gian ngắn để một Server khởi chạy, trạng thái ban đầu của nó đang chờ xử lý. Sau khi Server bắt đầu, trạng thái của nó chuyển sang đang chạy. Lưu ý rằng có thể mất vài phút để Server sẵn sàng để bạn có thể kết nối với nó. Kiểm tra xem Server của bạn đã vượt qua kiểm tra trạng thái chưa; bạn có thể xem thông tin này trong cột Kiểm tra trạng thái.

Sau khi khởi tạo thành công Server, và trạng thái Server là **Active**, bạn có thể thực hiện theo hướng dẫn [{Đăng nhập vào Server}](../server/ket-noi-vao-may-chu-ao/) để thực hiện sử dụng Server của mình.

***

### Tìm kiếm Server đã tạo

Trong trường hợp người dùng tạo rất nhiều máy chủ ảo (VM), thì VNG Cloud cung cấp công cụ hỗ trợ tìm kiếm các máy chủ ảo mà người dùng đã tạo trước một cách nhanh chóng.

**Bước 1:** Mở trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview)

**Bước 2:** Chọn mục Servers để đến màn hình danh sách các máy chủ ảo đã tạo;

**Bước 3:** Chọn vào ô "Search with Suggestion" để chọn tiêu chí để search đúng máy ảo cần tìm:

* Search by Name: Tìm theo tên của Server;
* Search by Private IP: Tìm theo private IP của Server;
* Search by Public IP: Tìm theo public IP của Server;
* Search by Subnet ID: Tìm theo Subney ID đã tạo Server;
* Search by VPC ID: Tìm thao VPC ID đả tạo Server;
* Search by Tag: Tìm Tag của Server lúc khởi tạo;

**Bước 4:** Điền thông tin cần tìm kiếm và xác nhận tìm để hệ thống tự động tra máy chủ phù hợp với từ khóa.
