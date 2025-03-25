# Tạo máy chủ bằng bảng điều khiển

Tạo máy chủ ảo bằng quy trình khởi tạo trên VNG Cloud

Cách thực hiện: [Trải nghiệm sản phẩm vServer](../trai-nghiem-san-pham-vserver/)

VNG Cloud cung cấp quy trình khởi tạo máy chủ ảo đơn giản với những thông tin cấu hình cần thiết đảm bảo tính bảo mật và tiện dụng.

### **Chuẩn bị** <a href="#taomaychubangbangdieukhien-chuanbi" id="taomaychubangbangdieukhien-chuanbi"></a>

Bạn cần tạo tài khoản tại VNG Cloud và xác thực các thông tin chủ quản. Bạn cũng cần nạp một khoản tiền nhỏ để thanh toán chi phí khi khởi tạo máy chủ ảo.

### **Cấu hình cơ bản** <a href="#taomaychubangbangdieukhien-cauhinhcoban" id="taomaychubangbangdieukhien-cauhinhcoban"></a>

Tại bước cấu hình cơ bản, bạn cần cung cấp thông tin về số lượng tài nguyên và hệ điều hành cho máy chủ ảo. Tên máy chủ dài từ 5-50 ký tự và chỉ chứa các ký tự chữ cái, số, dấu gạch nối hoặc gạch dưới.

Bạn cần xác định hệ điều hành cho máy chủ thông qua lựa chọn Images, bảng bên dưới mô tả các loại Image được cung cấp bởi VNG Cloud:

| **Image type**          | **Description**                                                                                                                                                                                                                                           | **Notes or References**                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| OS Image / Public Image | Image chung là các image được VNG Cloud xây dựng sẵn, đảm bảo các tiêu chuẩn về hiệu năng và bảo mật. Các image này đều là các loại hệ điều hành phổ biến Windows Server hoặc các dòng Linux chủ đạo (Ubuntu, CentOS)                                     | [{Trang Image}](../image.md)                                                                  |
| My Image / Custom Image | Người dùng có thể tạo máy chủ ảo từ image đã được tùy biến riêng. Các image này thường được cài đặt sẵn các phần mềm hoặc môi trường riêng theo nhu cầu của người dùng, giúp giảm thời gian lặp lại các bước cài đặt thủ công khi cần tạo mới máy chủ ảo. | [{Trang Tùy chỉnh Image}](../image.md)                                                        |
| GPU Image               | Image có chứa sẵn các driver và phần mềm của NVIDIA, mục đích sử dụng các GPU NVIDIA nếu máy chủ ảo được lựa chọn có sử dụng GPU NVIDIA. Image này do VNG Cloud xây dựng sẵn dựa trên hệ điều hành Windows OS và Ubuntu.                                  | Người dùng cũng có thể chọn image chung và cài đặt các công cụ GPU tùy ý theo nhu cầu sau đó. |

Lựa chọn loại máy chủ ảo để xác định số lượng tài nguyên CPU, RAM phù hợp cho nhu cầu ứng dụng. Người dùng có thể tham khảo chi phí dự kiến cho từng loại cấu hình của máy chủ ảo ở khung bên phải.

### **Cấu hình Volume** <a href="#taomaychubangbangdieukhien-cauhinhvolume" id="taomaychubangbangdieukhien-cauhinhvolume"></a>

Máy chủ ảo có thể được gắn các Volume để lưu trữ dữ liệu như các ổ cứng gắn liền.

Giải pháp Block Storage tại VNG Cloud được dùng hoàn toàn bằng SSD.

Cấu hình IOPS thể hiện hạn mức hoạt động trong việc đọc ghi dữ liệu trên Volume. Tùy thuộc vào nhu cầu của ứng dụng, người dùng sẽ chọn cấu hình hạn mức phù hợp để sử dụng hiệu quả nhất.

Tính năng mã hóa Volume cung cấp nhu cầu bảo mật toàn diện cho dữ liệu của người dùng. Khóa mã hóa được quản lý an toàn bởi hệ thống KMS của VNG Cloud, hoạt động độc lập với máy chủ ảo. Người dùng còn có thể chọn lưu trữ dữ liệu trên Volume được mã hóa hoặc không.

Máy chủ ảo có thể được gắn nhiều Volume lưu trữ dữ liệu khác nhau. Người dùng có thể thao tác gắn thêm volume khi cần.

### **Cấu hình Network** <a href="#taomaychubangbangdieukhien-cauhinhnetwork" id="taomaychubangbangdieukhien-cauhinhnetwork"></a>

Người dùng có thể tạo thông tin Network và Security Group phù hợp để quản lý giao tiếp giữa các máy chủ ảo trong môi trường Network VPC.

VPC là một không mang mạng riêng ảo. Người dùng có toàn quyền quản lý thông tin VPC này từ việc đặt range IP đến điều chỉnh routing hoặc điều khiển chính sách network trong VPC. Xem thêm tại [{Trang VPC}](../network/virtual-private-cloud-vpc/).

Nếu bạn chưa từng tạo VPC trước đây, hệ thống sẽ tự động tạo trước VPC và subnet mặc định để nhanh chóng sử dụng tiếp trong quá trình khởi tạo máy chủ ảo.

#### Lựa chọn Floating IP cho máy chủ ảo <a href="#taomaychubangbangdieukhien-luachonfloatingipchomaychuao" id="taomaychubangbangdieukhien-luachonfloatingipchomaychuao"></a>

Để máy chủ ảo có thể truy cập được Internet, bạn cần gán địa chỉ IP public vào máy chủ ảo đó. FIP sẽ được NAT 1:1 với địa chỉ IP private của máy chủ ảo (thuộc subnet của VPC), FIP sẽ không được nhìn thấy nếu đứng từ trong OS của máy chủ.

Người dùng có thể chọn dùng FIP khi tạo máy chủ ảo hoặc thực hiện gán FIP sau khi máy chủ ảo được tạo để cung cấp khả năng kết nối internet cho máy chủ ảo. Người dùng có thể chọn mua dành riêng FIP để giữ lại sau khi máy chủ ảo không hoạt động.

#### Lựa chọn security group <a href="#taomaychubangbangdieukhien-luachonsecuritygroup" id="taomaychubangbangdieukhien-luachonsecuritygroup"></a>

Security group là một lớp firewall ảo dùng để quản trị việc truy cập qua đường mạng đối với các máy chủ ảo.

Người dùng có thể sử dụng security group mặc định đã tạo sẵn của hệ thống với các nội dung có sẵn như cho phép truy cập SSH port tcp/234, RDP port tcp/3490 và Ping (ICMP). Người dùng có thể quản trị thay đổi các nội dung này theo ý muốn.

#### Chứng thực <a href="#taomaychubangbangdieukhien-chungthuc" id="taomaychubangbangdieukhien-chungthuc"></a>

Bạn nên sử dụng SSH Key để truy cập vào máy chủ ảo Linux. Bạn có thể tạo SSH Key mới hoặc nhập Public Key có sẵn của bạn lên VNG Cloud để sử dụng sau này. Xem thêm ở [{Trang SSH Key}](../security/ssh-key-bo-khoa.md).

Ngoài ra, bạn có thể điều thông tin username, password để truyền vào máy chủ khi khởi tạo.

### **Các tùy chọn khác** <a href="#taomaychubangbangdieukhien-cactuychonkhac" id="taomaychubangbangdieukhien-cactuychonkhac"></a>

Bạn có thể chọn tính năng Server Group để tạo ràng buộc về vị trí đặt cho các máy chủ ảo trong quá trình khởi tạo.

### **Kết quả** <a href="#taomaychubangbangdieukhien-ketqua" id="taomaychubangbangdieukhien-ketqua"></a>

Sau khi máy chủ ảo được tạo ra, bạn vào trang Instance để kiểm tra trạng thái của máy chủ. Trạng thái Running báo hiệu máy chủ đã sẵn sàng để sử dụng. Bạn cũng sẽ nhận được thông tin truy cập qua email.
