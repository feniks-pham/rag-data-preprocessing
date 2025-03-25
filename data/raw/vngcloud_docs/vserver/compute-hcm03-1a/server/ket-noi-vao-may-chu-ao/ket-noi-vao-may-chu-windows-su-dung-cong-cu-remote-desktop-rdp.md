# Kết nối vào máy chủ Windows sử dụng công cụ Remote Desktop (RDP)

Bạn có thể kết nối dễ dàng với các máy chủ Window được tạo từ trình điều khiển VNG Cloud bằng Remote Desktop. Để làm điều này, bạn cần tải về RDP và làm theo hướng dẫn bên dưới của chúng tôi. RDP có sẵn trên hầu hết các phiên bản Windows và cũng có sẵn cho Mac OS.

Để biết thông tin về cách kết nối với phiên bản Linux, hãy xem hướng dẫn  [Kết nối vào máy chủ Linux bằng công cụ SSH Client](ket-noi-vao-may-chu-linux-bang-cong-cu-ssh-client.md) dành cho Phiên bản Linux về cách kết nối với máy chủ của bạn.

***

### **Điều kiện tiên quyết** <a href="#ketnoivaomaychuwindowssudungcongcuremotedesktop-rdp-dieukientienquyet" id="ketnoivaomaychuwindowssudungcongcuremotedesktop-rdp-dieukientienquyet"></a>

**Để có thể kết nối vào máy chủ Window:**

* **Cài đặt RDP**:
  * \[Windows] Theo mặc định, Windows sẽ bao gồm RDP Client. Để xác minh, hãy nhập **mstsc** tại cửa sổ Command Prompt. Nếu máy tính của bạn không nhận ra lệnh này, hãy xem trang chủ Windows và tìm kiếm bản tải xuống cho ứng dụng[ Microsoft Remote Desktop](https://www.microsoft.com/vi-vn/windows).
  * \[Mac OS X] Tải xuống ứng dụng [Microsoft Remote Desktop](https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466?mt=12) từ Mac App Store.
  * \[Linux] Sử dụng [Remmina](https://remmina.org/)
* **Máy chủ phải đang chạy**:
  * Sau khi máy chủ được khởi tạo thành công, thông tin của nó sẽ xuất hiện trên trang danh sách máy chủ của bảng điều khiển và trạng thái của máy chủ là Active
* **Quy tắc Inbound của nhóm bảo mật được tạo** :&#x20;
  * Đảm bảo rằng nhóm bảo mật được liên kết với phiên bản của bạn cho phép lưu lượng RDP đến (cổng 3389) từ địa chỉ IP của bạn. Nhóm bảo mật mặc định không cho phép lưu lượng RDP đến theo mặc định. Để biết thêm thông tin, hãy xem Cho phép lưu lượng truy cập đến cho các phiên bản Windows của bạn.
* **Network Interface** của máy chủ cần có một địa chỉ IP Public
* **Thông tin kết nối đến** máy chủ: Để biết thông tin kết nối của máy chủ, vui lòng kiểm tra email đã đăng ký:

<figure><img src="../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Lưu ý:** Thông tin này là bảo mật và chỉ được gởi cho email đã đăng kí. VNG Cloud không thể can thiệp để phục hồi thông tin login của máy chủ (username/ password/ key) trong mọi tình huống.

***

### **Kết nối sử dụng Client RDP trên Window** <a href="#ketnoivaomaychuwindowssudungcongcuremotedesktop-rdp-ketnoisudungclientrdptrenwindow" id="ketnoivaomaychuwindowssudungcongcuremotedesktop-rdp-ketnoisudungclientrdptrenwindow"></a>

1. Truy cập vào trang quản lý Server tại trình điều khiển của chúng tôi tại: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Chọn Server cần kết nối, sau đó chọn Hành động - **Kết nối**
3.  Trên trang Kết nối tới máy chủ, chọn tab RDP (Window)\
    \


    <figure><img src="../../../../.gitbook/assets/image (417).png" alt=""><figcaption></figcaption></figure>
4. Chọn **Tải xuống tệp RDP**. Trình duyệt của bạn sẽ nhắc bạn mở hoặc lưu tệp RDP. Khi bạn đã hoàn tất tải xuống tệp, hãy chọn **Hoàn thành** để quay lại trang máy chủ:
   * Nếu bạn đã mở tệp RDP, bạn sẽ thấy hộp thoại Kết nối Máy tính Từ xa.
   * Nếu bạn đã lưu tệp RDP, hãy điều hướng đến thư mục tải xuống của bạn và mở tệp RDP để hiển thị hộp thoại.
5.  Bạn có thể nhận được cảnh báo rằng nhà xuất bản của kết nối từ xa không xác định. Chọn **Kết nối** để tiếp tục kết nối với máy chủ của bạn

    <figure><img src="../../../../.gitbook/assets/image (418).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (419).png" alt=""><figcaption></figcaption></figure>
6.  Tài khoản quản trị viên được chọn theo mặc định. Bạn cần sao chép và dán mật khẩu mà bạn đã lưu trước đó vào pop-up đăng nhập (Thông tin này lấy từ mail phía trên), trong đó nhập thông tin **InstanceLogin** vào **Username**, **InstancePassword** vào **Password**:

    <figure><img src="../../../../.gitbook/assets/image (424).png" alt=""><figcaption></figcaption></figure>
7.  Nhấn **OK.** Do tính chất của chứng chỉ tự ký, bạn có thể nhận được cảnh báo rằng chứng chỉ bảo mật không thể được xác thực. Sử dụng các bước sau để xác minh danh tính của máy tính từ xa hoặc chỉ cần chọn **Yes**(Windows) hoặc **Continue** (Mac OS X) nếu bạn tin cậy chứng chỉ.\


    <figure><img src="../../../../.gitbook/assets/image (421).png" alt=""><figcaption></figcaption></figure>
8.  Màn hình sẽ hiển thị đang kết nối đến máy chủ Window thành công\


    <figure><img src="../../../../.gitbook/assets/image (422).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (423).png" alt=""><figcaption></figcaption></figure>

***

### **Câu hỏi thường gặp** <a href="#ketnoivaomaychuwindowssudungcongcuremotedesktop-rdp-cauhoithuonggap" id="ketnoivaomaychuwindowssudungcongcuremotedesktop-rdp-cauhoithuonggap"></a>

* **Q. Màn hình xuất hiện yêu cầu tên người dùng và mật khẩu khi kết nối RDP. Tôi nên làm gì?**\
  Nhập tên người dùng và mật khẩu của bạn từ email được gởi từ hệ thống khi khởi tạo máy chủ để đăng nhập vào máy chủ.
* **Q. Tôi nhận được cảnh báo về chứng chỉ không hợp lệ. Tôi nên làm gì?**\
  Nếu bạn chắc chắn rằng máy chủ là đáng tin cậy và bạn đã đúng địa chỉ IP hoặc tên máy chủ, bạn có thể tiếp tục và chấp nhận cảnh báo. Tuy nhiên, nếu bạn không chắc chắn về tính xác thực của máy chủ, hãy không tiếp tục kết nối và thông báo cho quản trị viên hệ thống.
* **Q. Bạn có muốn kết nối tài nguyên của máy tính địa phương như ổ đĩa hoặc máy in vào máy chủ không?**\
  Tùy vào nhu cầu của bạn. Nếu bạn muốn sử dụng các tài nguyên địa phương trên máy chủ từ xa, hãy chọn "Có". Nếu không, chọn "Không".
* **Q. Bạn có muốn khóa phiên hoặc đăng xuất phiên đăng nhập hiện tại không?**\
  Tùy vào tình huống. Nếu bạn muốn giữ phiên đăng nhập hiện tại và chỉ đóng kết nối RDP, chọn "Không". Nếu bạn muốn khóa phiên, chọn "Khóa phiên" hoặc nếu bạn muốn đăng xuất khỏi phiên đăng nhập hiện tại, chọn "Đăng xuất".
* **Q. Bạn có muốn tiếp tục phiên kết nối không?**\
  Nếu bạn không hoạt động trong phiên một thời gian dài hoặc không dự định sử dụng nó trong một thời gian, bạn có thể chọn "Không" để đóng kết nối mà vẫn giữ phiên đăng nhập trên máy chủ. Nếu bạn vẫn muốn tiếp tục làm việc trong phiên, chọn "Có".
* **Q. Bạn có muốn kết thúc phiên RDP và đóng kết nối từ xa không?**\
  Tùy thuộc vào nhu cầu. Nếu bạn đã hoàn thành công việc của mình và không cần kết nối nữa, chọn "Kết thúc phiên". Nếu bạn muốn giữ phiên đăng nhập mở trên máy chủ và chỉ đóng kết nối RDP, chọn "Không".
* **Q. Tôi có thể kết nối cùng lúc nhiều máy tính vào cùng một máy chủ Window không?**\
  Có, bạn có thể sử dụng Remote Desktop để kết nối nhiều máy tính vào cùng một máy chủ Window, tạo nên một môi trường đa người dùng. Điều này thường được gọi là Remote Desktop Services (RDS) hoặc Terminal Services. Tuy nhiên số lượng người dùng này có thể được giới hạn bởi số lượng phiên Remote Desktop Services (RDS) được cấp phát cho máy chủ.
