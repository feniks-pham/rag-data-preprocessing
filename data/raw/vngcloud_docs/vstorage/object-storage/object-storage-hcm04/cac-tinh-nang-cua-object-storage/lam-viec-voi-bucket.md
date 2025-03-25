# Làm việc với bucket

## Tổng quan

Để lưu trữ dữ liệu của bạn trong một project, bạn cần tạo một bucket và tải các object lên bucket đó. Trong một project sẽ có thể khởi tạo một hoặc nhiều bucket có vai trò như 1 directory chứa dữ liệu tuy nhiên bucket sẽ khác với directory ở mặt bucket là 1 phân cấp cho phép người dùng hoặc nhà cung cấp dịch vụ đưa ra các tính năng và thực thi chúng từ phân cấp này trở xuống. Ví dụ chúng tôi cung cấp các tính năng bucket policy, bucket ACLs, bucket lifecycle,... cho mỗi bucket trong một project.

Về mặt triển khai, các project, bucket, object là tài nguyên của vStorage và chúng tôi cũng cung cấp API để bạn quản lý chúng. Ví dụ: bạn có thể tạo một project, bucket và tải các object lên bằng cách sử dụng API. Bạn cũng có thể sử dụng giao diện quản trị mà chúng tôi cung cấp hoặc các 3rd party softwares để thực hiện các thao tác này.&#x20;

***

## Phạm vi giới hạn bucket

#### Quy tắc đặt tên bucket <a href="#phamvigioihanbucket-quytacdattenbucket" id="phamvigioihanbucket-quytacdattenbucket"></a>

Các quy tắc sau áp dụng cho việc đặt tên bucket trong vStorage:

* Tên bucket phải dài từ 3 (tối thiểu) đến 235 (tối đa) ký tự.
* Tên bucket chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Tên bucket không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...). Chúng tôi khuyến cáo bạn nên đặt tên bucket bằng các chữ cái viết thường, chữ số và không có các ký tự cụ thể như #, @, $, %, ?, /, \`, \~ ... Nếu bạn thực sự cần đặt tên với các ký tự viết hoa, vui lòng lưu ý rằng, bạn có thể gặp một số vấn đề khi làm việc với các 3rd party softwares được hỗ trợ từ các nhà cung cấp khác.
* Tên bucket phải là duy nhất trong một project cho đến khi bucket đó bị xóa.&#x20;

#### Ví dụ minh họa <a href="#phamvigioihanbucket-viduminhhoa" id="phamvigioihanbucket-viduminhhoa"></a>

* Các tên bucket ví dụ sau đây hợp lệ và tuân theo các nguyên tắc đặt tên được đề xuất:
  * bucketexample1
  * bucket-data-2022
  * ...
* Các tên bucket ví dụ sau đây hợp lệ nhưng chúng tôi không khuyến khích bạn sử dụng:
  * [docexamplewebsite.com](http://docexamplewebsite.com/)
  * [www.docexamplewebsite.com](http://www.docexamplewebsite.com/)
  * ...
* Các tên bucket ví dụ sau không hợp lệ:
  * Bucket data đạt hiệu quả 80 % (chứa ký tự %)
  * con\_1/2022 (chứa ký tự /)
  * ...
