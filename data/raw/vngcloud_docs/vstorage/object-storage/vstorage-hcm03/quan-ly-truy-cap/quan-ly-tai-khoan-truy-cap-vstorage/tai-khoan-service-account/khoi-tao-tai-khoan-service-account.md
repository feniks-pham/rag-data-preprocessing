# Khởi tạo tài khoản Service Account

Để khởi tạo tài khoản Service Account, hãy làm theo các bước bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn mục **Service Account**.
3. Chọn **Create a Service Account.**
4. Tại mục **Add information**, nhập **Name** mà bạn mong muốn. Tên của Service Account phải dài từ 1 (tối thiểu) đến 50 (tối đa) ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-) và khoảng trắng( ). Tên của Service Account không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, mật khẩu đăng nhập,...) cũng như tên Service Account phải là duy nhất trên một tài khoản VNG Cloud cho đến khi Service Account đó bị xóa. Ví dụ tên Service Account sau là hợp lệ: SA\_Client\_tool\_01.
5. Tại mục Trusted relationship, nhập Account Root IS nếu bạn muốn thêm thông tin liên kết giữa Service Account và Root User Account.
6. Chọn **Next step**.
7. Tại mục **Add permission**, bạn có thể:
   1. Chọn 1 hoặc nhiều policy mà bạn đang có để liên kết với Service Account. Hệ thống vIAM hỗ trợ bạn gán nhiều policy vào một tài khoản Service Account. Nếu các policy này chứa các quyền hạn độc lập thì chúng sẽ bổ sung cho nhau (tức là danh sách quyền hạn được hợp lại). Ngược lại nếu các policy này chứa các quyền hạn trái ngược thì bạn sẽ không thể truy cập vào tài nguyên tương ứng theo danh sách quyền hạn này (tức là danh sách quyền được hợp lại và khi trái ngược thì sẽ triệt tiêu nhau). Chi tiết tham khảo thêm tại [Liên kết tài khoản Service Account với policy tương ứng](lien-ket-tai-khoan-service-account-voi-policy-tuong-ung.md).
   2. Nếu danh sách policy chưa có policy mà bạn mong muốn, bạn có thể tiếp tục các bước bên dưới và chúng tôi chấp nhận việc khởi tạo policy sau khi khởi tạo tài khoản Service Account nhưng bạn nên liên kết chúng theo hướng dẫn tại [Liên kết tài khoản Service Account với policy tương ứng](lien-ket-tai-khoan-service-account-voi-policy-tuong-ung.md).
8. Chọn **Copy** để sao chép Secret key. Bạn bắt buộc phải thu thập được thông tin này để có thể truy cập vào vStorage sử dụng Service Account.
9. Chọn **Download** để tải xuống secret key này và lưu trữ chúng tại thiết bị local của bạn.
10. Chọn **Back to list** để quay lại màn hình chứa danh sách Service Account.

Sau khi bạn thực hiện 10 bước bên trên, một tài khoản Service Account đã được khởi tạo.

<figure><img src="../../../../../../.gitbook/assets/Khoi_tao_Service_Account.gif" alt=""><figcaption></figcaption></figure>
