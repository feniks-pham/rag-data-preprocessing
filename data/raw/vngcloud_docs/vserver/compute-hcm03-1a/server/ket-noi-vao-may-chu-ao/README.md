# Kết nối vào máy chủ ảo

Người dùng có nhiều cách để kết nối vào máy chủ ảo như chức năng Console trên VNG Cloud Portal hoặc các công cụ client khác. Tùy thuộc vào hệ điều hành của máy chủ ảo, hệ điều hành của máy cá nhân hoặc loại kết nối mong muốn mà bạn có thể lựa chọn phương pháp kết nối phù hợp.

### **Kết nối sử dụng trình điều khiển vServer** <a href="#ketnoivaomaychuao-ketnoisudungtrinhdieukhienvserver" id="ketnoivaomaychuao-ketnoisudungtrinhdieukhienvserver"></a>

Phương pháp này đòi hỏi bạn phải có mật khẩu của máy chủ. Mặc định, hệ thống VNG Cloud tự động sinh ra password cho máy chủ ảo khi bạn tạo mới. Thông tin này sẽ được gửi qua email khi máy chủ ảo đuợc tạo xong và ở trạng thái Active. Bạn cũng có thể dùng username và password đã điền vào trước đó trong quy trình tạo mới máy chủ.

Một số trường hợp cần phải dùng phương pháp kết nối này để giải quyết, chẳng hạn như:

* Máy chủ gặp vấn đề về kết nối mạng
* Khi cần tìm hiểu sự cố và xử lý chấm dứt những chương trình bất thường đang chạy trên máy chủ gây nghẽn mạng hoặc xử lý CPU quá cao
* Máy chủ bị cấu hình firewall chưa chính xác

#### Cách thực hiện <a href="#ketnoivaomaychuao-cachthuchien" id="ketnoivaomaychuao-cachthuchien"></a>

1. Truy cập vào trang Server tại bảng điều khiển: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Tại trang **Server**, xác định máy chủ muốn kết nối, tại **Menu** lựa chọn ở bên phải, chọn **Console** để mở cửa sổ quản lý server qua console
3. Bạn sẽ cần mật khẩu hệ điều hành của máy chủ để đăng nhập
4. Bạn cũng có thể gọi tổ hợp phím tắt CTRL+ALT+DEL để thực hiện khởi động lại máy chủ bằng cách nhấn vào nút **Send CtrlAltDel** ở góc trên bên phải

***

### **Kết nối máy chủ Windows sử dụng công cụ Remote Desktop** <a href="#ketnoivaomaychuao-ketnoimaychuwindowssudungcongcuremotedesktop" id="ketnoivaomaychuao-ketnoimaychuwindowssudungcongcuremotedesktop"></a>

Giao thức Remote Desktop (RDP) yêu cầu thông tin người dùng và mật khẩu để xác thực đơn giản khi truy cập vào máy chủ

#### Yêu cầu <a href="#ketnoivaomaychuao-yeucau" id="ketnoivaomaychuao-yeucau"></a>

Trước khi kết nối máy chủ Windows, bạn cần đảm bảo các yêu cầu sau:

* Máy chủ Windows đang ở trạng thái Running, nếu khác, bạn cần khởi động lại máy chủ
* Bạn cần mật khẩu kết nối vào Instance, nếu bạn chưa cung cấp thông tin mật khẩu khi tạo máy chủ, bạn có thể dùng thông tin tài khoản và mật khẩu được tạo tự động gửi trong email
* Máy chủ ảo phải có kết nối network hoạt động tốt
* Thiết lập Security Group cần được định nghĩa như cho phép traffic port tcp/3490 cho giao thức RDP

#### Cách thực hiện <a href="#ketnoivaomaychuao-cachthuchien.1" id="ketnoivaomaychuao-cachthuchien.1"></a>

[Kết nối vào máy chủ Windows sử dụng công cụ Remote Desktop](./#ketnoivaomaychuao-ketnoimaychuwindowssudungcongcuremotedesktop)



***

### **Kết nối vào máy chủ Linux bằng công cụ SSH Client** <a href="#ketnoivaomaychuao-ketnoivaomaychulinuxbangcongcusshclient" id="ketnoivaomaychuao-ketnoivaomaychulinuxbangcongcusshclient"></a>

Người dùng có thể sử dụng mật khẩu hệ điều hành hoặc cặp khóa SSH để kết nối vào máy chủ thông qua giao thức SSH.

Khi thực hiện kết nối vào máy chủ Linux, bạn nên ưu tiên phương pháp sử dụng cặp khóa SSH và các công cụ hỗ trợ giao thức SSH như Linux terminal hoặc PuTTY trên Windows. Đây là phương pháp bảo mật và thuận tiện nhất để kết nối vào máy chủ.

#### Yêu cầu <a href="#ketnoivaomaychuao-yeucau.1" id="ketnoivaomaychuao-yeucau.1"></a>

* Cặp khóa SSH phải được tạo trước vào khai báo trong quy trình tạo mới máy chủ ảo
* Máy chủ Linux cần kết nối vào phải ở trạng thái Active
* Máy chủ ảo cần có kết nối mạng phù hợp, ví dụ như sử dụng Floating IP để kết nối internet trực tiếp
* Một thiết lập Security Group được khai báo và security group này được gán vào máy chủ cần kết nối để cho phép traffic được thông suốt. Thiết lập cụ thể như allow traffic port tcp/234 cho giao thức SSH

#### Cách thực hiện <a href="#ketnoivaomaychuao-cachthuchien.2" id="ketnoivaomaychuao-cachthuchien.2"></a>

[Kết nối vào máy chủ Linux bằng công cụ SSH Client](./#ketnoivaomaychuao-ketnoivaomaychulinuxbangcongcusshclient)

\
