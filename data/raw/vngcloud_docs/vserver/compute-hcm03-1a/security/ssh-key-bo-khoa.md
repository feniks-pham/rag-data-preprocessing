# SSH Key (Bộ khóa)

Key pair là 1 cặp Public và Private key, chứa thông tin chứng thực dùng để truy cập vào máy chủ ảo. Đối với máy chủ ảo chạy hệ điều hành Linux, bộ khóa được dùng để truy cập vào máy chủ qua giao thức SSH.

Bất cứ ai sở hữu Private key sẽ có thể truy cập vào máy chủ, nên việc bảo vệ private key là cực kỳ quan trọng.

Khi tạo máy chủ ảo Linux, bạn được yêu cầu chọn thông tin Bộ khóa. Khi máy chủ khởi động lần đầu tiên, thông tin Public key được đưa vào trong máy chủ ảo tại `~`**`/.ssh/authorized_keys`** .Khi dùng giao thức SSH để truy cập vào máy chủ, bạn cần chọn private tương ứng để thực hiện xác thực. Xem thêm thông tin ở [{](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647965)[Kết nối vào máy chủ ảo](../server/ket-noi-vao-may-chu-ao/)[}](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647965).

VNG Cloud không thể khôi phục lại được Private key nếu bạn đánh mất. Bạn có thể tạo mới SSH Key thông qua VNG Cloud Portal hoặc dùng các công cụ bên thứ 3 khác. VNG Cloud hỗ trợ chuẩn key SSH-2 RSA đối với các máy chủ ảo Linux.

***

### **Làm việc với SSH Key** <a href="#sshkey-bokhoa-lamviecvoisshkey" id="sshkey-bokhoa-lamviecvoisshkey"></a>

#### **Tạo bộ khóa SSH Key** <a href="#sshkey-bokhoa-taobokhoasshkey" id="sshkey-bokhoa-taobokhoasshkey"></a>

Điều đầu tiên bạn có thể làm với SSH Key là tạo mới. Nhấp vào nút "Tạo SSH Key" ở góc trên bên trái, bạn sẽ được chuyển hướng lại trang tạo để nhập thông tin cần thiết để tạo. Tại đây, bạn có thể tạo SSH Key bằng trình chỉnh sửa trực quan của chúng tôi với giao diện thân thiện người dùng.

#### **Nhập SSH Key** <a href="#sshkey-bokhoa-nhapsshkey" id="sshkey-bokhoa-nhapsshkey"></a>

Nếu bạn chưa có SSH Key trên VNG Cloud Portal, bạn phải tạo SSH Key mới để sử dụng cho việc xác thực. Nếu đã có sẵn SSH Key, bạn có thể nhấp vào nút “Nhập SSH Key”, giao diện sẽ xuất hiện trang cho phép nhập thông tin SSH Key, nhập tên SSH Key và dán Public Key vào trường tương ứng để hoàn thành việc nhập SSH Key.

#### **Xóa SSH Key** <a href="#sshkey-bokhoa-xoasshkey" id="sshkey-bokhoa-xoasshkey"></a>

Nếu có SSH Key bạn muốn xóa, hãy chọn một SSH Key và nhấp vào nút "Xóa" ở góc trên bên phải. Một phương thức xác nhận sẽ xuất hiện để đảm bảo rằng bạn sẽ không xóa nhầm vì một khi đã xóa, SSH Key sẽ không thể khôi phục lại.

\
