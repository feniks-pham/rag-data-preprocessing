# Làm việc với Notification

### Tổng quan <a href="#lamviecvoinotification-tongquan" id="lamviecvoinotification-tongquan"></a>

Hiện tại vMonitor Platform hỗ trợ 5 kênh thông báo mà bạn có thể thiết lập bao gồm:

* **Email**: là dạng gửi thông báo từ hệ thống tới người nhận thông qua thư điện tử.
* **SMS**: là dạng gửi thông báo từ hệ thống tới người nhận thông qua tin nhắn văn bản.
* **Slack**: là dạng gửi thông báo từ hệ thống tới người nhận thông qua ứng dụng Slack.
* **Telegram**: là dạng gửi thông báo từ hệ thống tới người nhận thông qua ứng dụng Telegram.
* **Webhook**: là dạng gửi thông báo từ hệ thống tới người nhận thông qua Webhook.

***

### Phạm vi giới hạn Dashboard <a href="#lamviecvoinotification-phamvigioihandashboard" id="lamviecvoinotification-phamvigioihandashboard"></a>

**Quy tắc đặt tên Notification**

Các quy tắc sau áp dụng cho việc đặt tên Notification trong vMonitor Platform:

* Tên Notification phải dài từ 5 (tối thiểu) đến 50 (tối đa) ký tự.
* Tên Notification chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Tên Notification phải bắt đầu bằng một chữ cái viết hoa, viết thường (a-z, A-Z) và kết thúc bởi một chữ cái viết hoa, viết thường (a-z, A-Z) hoặc một chữ số.
* Tên Notification không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...).&#x20;
* Tên Notification phải là duy nhất trong một tài khoản VNG Cloud cho đến khi Notification đó bị xóa.&#x20;

#### Ví dụ minh họa <a href="#lamviecvoinotification-viduminhhoa" id="lamviecvoinotification-viduminhhoa"></a>

* Các tên Notification ví dụ sau đây hợp lệ và tuân theo các nguyên tắc đặt tên được đề xuất:
  * Noti\_email\_group1
  * technical@sms
  * ...
* Các tên Notification ví dụ sau đây hợp lệ nhưng chúng tôi không khuyến khích bạn sử dụng:
  * [docexamplewebsite.com](http://docexamplewebsite.com/)
  * 1.1.1.2
  * ...
* Các tên Notification ví dụ sau không hợp lệ:
  * Report\_usage\_80\_% (chứa ký tự %)
  * Notification\&Report (chứa ký tự &)
  * ...

***

### Khởi tạo Notification <a href="#lamviecvoinotification-khoitaonotification" id="lamviecvoinotification-khoitaonotification"></a>

Mỗi Notification **chỉ có thể chứa một nhóm người dùng với cùng một kênh gửi/ nhận thông báo**. Ví dụ một notification có thể chứa nhóm người nhận [ABC@gmail.com](mailto:ABC@gmail.com), [XYZ@gmail.com](mailto:XYZ@gmail.com) thông qua kênh nhận là Email nhưng notification này không thể chứa nhóm người nhận 123@gmail.com, 0988123123 thông qua kênh nhận cả Email và SMS. Để tạo Notification, hãy làm theo hướng dẫn bên dưới:

* [SMS](sms.md)
* [Email](email.md)
* [Slack](slack.md)
* [Telegram](telegram.md)
* [Webhook](webhock.md)

Chúng tôi không giới hạn số lượng notification bạn có thể tạo, số lượng thông báo được gửi ra sẽ phụ thuộc vào các thông số quota của gói SMS Notification, Email Notification hoặc quota của gói Metrics, Logs tương ứng.&#x20;

***

### Chỉnh sửa Notification <a href="#lamviecvoinotification-chinhsuanotification" id="lamviecvoinotification-chinhsuanotification"></a>

Bạn đã khởi tạo một Notification trên hệ thống của chúng tôi. Hiện tại notification này không đáp ứng đúng mong muốn về người nhận và kênh gửi thông báo của bạn, lúc này bạn có thể chỉnh sửa notification. Để chỉnh sửa notification, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Notification.**
3. Tại notification mà bạn muốn chỉnh sửa, chọn **Edit**.&#x20;
4. Chỉnh sửa các thông số cho notification mà bạn mong muốn. Các thông số mà bạn có thể chỉnh sửa bao gồm: **Tên Notification**, Loại Notification, Địa chỉ Email, Số điện thoại, Đường dẫn Webhook, ... cũng như các thông số cấu hình chi tiết một notification.&#x20;

Việc chỉnh sửa này tương tự như khi bạn thực hiện tạo mới một Notification theo hướng dẫn tại [Khởi tạo Notification](./#lamviecvoinotification-khoitaonotification).

5\. Chọn **Save.**

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, notification đã được cập nhật theo cấu hình mới. Nếu bạn không có nhu cầu sử dụng notification này, hãy làm theo hướng dẫn [Xóa Notification](./#lamviecvoinotification-xoanotification).

***

### Xóa Notification <a href="#lamviecvoinotification-xoanotification" id="lamviecvoinotification-xoanotification"></a>

Khi bạn không có nhu cầu sử dụng một notification nữa, bạn có thể thực hiện xóa notification khỏi hệ thống theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Notification.**
3. Tại **Notification** mà bạn muốn xóa, chọn **Checkbox Chọn**. Bạn có thể chọn một hoặc nhiều notification để thực hiện xóa ở bước này.
4. Chọn **Xóa**.
5. Tại màn hình xác nhận xóa notification, chọn **Xóa**.

Sau khi bạn thực hiện xóa thành công thì notification của bạn sẽ bị xóa hoàn toàn khỏi hệ thống của chúng tôi. Bạn không thể khôi phục lại notification đã xóa nên hãy lưu ý cẩn thận khi sử dụng tính năng này.&#x20;
