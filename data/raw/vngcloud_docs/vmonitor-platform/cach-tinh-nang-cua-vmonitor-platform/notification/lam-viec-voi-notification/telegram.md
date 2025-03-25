# Telegram

Để tạo Notification với kênh gửi/ nhận là Telegram, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Notification.**
3. Chọn **Create a Notification**.
4. Màn hình **Create Notification** được hiển thị. Nhập **Notification name**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho Notification của bạn. Sau khi tạo Notification, bạn có thể thay đổi tên cho Notification của bạn. Để biết thêm thông tin về cách đặt tên Notification, hãy xem [Notification](../).
5. Chọn **Notification type** là **Telegram**.
6. Nhập **Chat ID.** Để lấy thông tin Chat ID của bạn, hãy làm theo hướng dẫn bên dưới:
   1. Mở trình duyệt web của Telegram theo đường dẫn: [https://web.telegram.org/z](https://web.telegram.org/z).
   2. Tạo một nhóm chat Telegram mới của bạn với thành viên là **@VMONITOR\_TELEGRAM\_BOT**.
   3. Sau khi nhóm chat đã được tạo, hãy truy cập vào đường dẫn tới nhóm chat trên trình duyệt. Đường dẫn tới nhóm chat này sẽ có định dạng [**https://web.telegram.org/z/#\[group\_chat\_id**](https://web.telegram.org/z/#\[group\_chat\_id)**]**. Từ đây, bạn có thể sao chép Group Chat ID và thực hiện định danh notification. \
      Ví dụ đường dẫn nhóm chat của bạn là [**https://web.telegram.org/z/#-123456789**](https://web.telegram.org/z/#-123456789), thì Chat ID của bạn là **-123456789**. Hãy dùng Chat ID này để định danh notification.

7\. Chọn **Send OTP,** hệ thống sẽ gửi mã OTP vào Telegram channel bạn đã nhập ở trên. OTP là viết tắt của One Time Password tức là mật khẩu sử dụng một lần, bạn sử dụng mã này để xác thực chính xác nhóm chat của bạn trên Telegram không phải là nhóm chat rác.

8\. Nhập mã **OTP** vào OTP. Mã OTP sẽ có hiệu lực trong vòng **120s**, sau 120s mã OTP này sẽ hết hiệu lực và không thể sử dụng để định danh nhóm chat Telegram. Bạn có thể chọn **Gửi lại OTP** để nhận mã mới sau đó tiếp tục nhập mã mới này để định danh.

9\. Chọn **Create.**&#x20;

<figure><img src="../../../../.gitbook/assets/image (103).png" alt="" width="512"><figcaption></figcaption></figure>
