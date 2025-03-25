# Phạm vi giới hạn container

#### Quy tắc đặt tên container <a href="#phamvigioihancontainer-quytacdattencontainer" id="phamvigioihancontainer-quytacdattencontainer"></a>

Các quy tắc sau áp dụng cho việc đặt tên container trong vStorage:

* Tên container phải dài từ 3 (tối thiểu) đến 235 (tối đa) ký tự.
* Tên container chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Tên container không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...). Chúng tôi khuyến cáo bạn nên đặt tên container bằng các chữ cái viết thường, chữ số và không có các ký tự cụ thể như #, @, $, %, ?, /, \`, \~ ... Nếu bạn thực sự cần đặt tên với các ký tự viết hoa, vui lòng lưu ý rằng, bạn có thể gặp một số vấn đề khi làm việc với các 3rd party softwares được hỗ trợ từ các nhà cung cấp khác.
* Tên container phải là duy nhất trong một project cho đến khi container đó bị xóa.&#x20;

#### Ví dụ minh họa <a href="#phamvigioihancontainer-viduminhhoa" id="phamvigioihancontainer-viduminhhoa"></a>

* Các tên container ví dụ sau đây hợp lệ và tuân theo các nguyên tắc đặt tên được đề xuất:
  * containerexample1
  * container-data-2022
  * ...
* Các tên container ví dụ sau đây hợp lệ nhưng chúng tôi không khuyến khích bạn sử dụng:
  * [docexamplewebsite.com](http://docexamplewebsite.com/)
  * [www.docexamplewebsite.com](http://www.docexamplewebsite.com/)
  * ...
* Các tên container ví dụ sau không hợp lệ:
  * Container data đạt hiệu quả 80 % (chứa ký tự %)
  * con\_1/2022 (chứa ký tự /)
  * ...

\
