# Teams

{% hint style="info" %}
**Chú ý:**&#x20;

* Microsoft Teams dừng support Office 365 connector, vì vậy, không thể tạo mới kênh notify qua Teams trên vMonitor. Team vMonitor Platform đang thay đổi phương thức theo đề suất của Microsoft và sẽ update lại sớm nhất.&#x20;
{% endhint %}

Để tạo Notification với kênh gửi/ nhận là Webhook, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Notification.**
3. Chọn **Create a Notification**.
4. Màn hình **Create Notification** được hiển thị. Nhập **Notification name**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho Notification của bạn. Sau khi tạo Notification, bạn có thể thay đổi tên cho Notification của bạn. Để biết thêm thông tin về cách đặt tên Notification, hãy xem [Notification](../).
5. Chọn **Notification type** là **Teams**.
6. Nhập **Webhook address**.
7. Chọn **Send OTP,** hệ thống sẽ gửi mã OTP vào **URL Webhook** bạn đã nhập ở trên. OTP là viết tắt của One Time Password tức là mật khẩu sử dụng một lần, bạn sử dụng mã này để xác thực chính xác nhóm chat của bạn trên Team  không phải là nhóm chat rác.
8. Nhập mã **OTP** vào OTP. Mã OTP sẽ có hiệu lực trong vòng **120s**, sau 120s mã OTP này sẽ hết hiệu lực và không thể sử dụng để định danh nhóm chat Teams. Bạn có thể chọn **Gửi lại OTP** để nhận mã mới sau đó tiếp tục nhập mã mới này để định danh.
9. Chọn **Create.**&#x20;

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
