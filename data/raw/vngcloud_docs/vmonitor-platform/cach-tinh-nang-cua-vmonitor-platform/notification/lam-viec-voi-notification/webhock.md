# Webhook

Để tạo Notification với kênh gửi/ nhận là Webhook, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Notification.**
3. Chọn **Create a Notification**.
4. Màn hình **Create Notification** được hiển thị. Nhập **Notification name**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho Notification của bạn. Sau khi tạo Notification, bạn có thể thay đổi tên cho Notification của bạn. Để biết thêm thông tin về cách đặt tên Notification, hãy xem [Notification](../).

5\. Chọn **Notification type** là **Webhook**.

6\. Nhập **Webhook address**.

7\. Nhập **Header** của webhook nếu có. Nếu bạn muốn định danh webhook thông qua header, hãy đảm bảo bạn cần nhập đầy đủ **Key** và **Value** của từng **header** đó. **Key** và **value** của **header** là các thông tin được gửi kèm theo yêu cầu HTTP từ ứng dụng server-side đến ứng dụng client-side khi có một sự kiện nào đó phát sinh trên server-side. **Key** và **value** **header** có thể được sử dụng để xác thực, mã hóa, định dạng hoặc chuyển đổi dữ liệu được gửi qua webhook.

8\. Chọn **Add header** nếu muốn thêm vùng nhập thông tin **Key**, **Value**.

9\. Chọn **Xóa** nếu muốn xóa cặp **Key, Value** đã nhập.

10\. Chọn **Create**.

<figure><img src="../../../../.gitbook/assets/image (104).png" alt="" width="510"><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/59807037/image2023-8-14_15-8-49.png?version=1&#x26;modificationDate=1692000532000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
