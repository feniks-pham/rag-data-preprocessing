# Phạm vi giới hạn object

#### Quy tắc đổi tên object <a href="#phamvigioihanobject-quytacdoitenobject" id="phamvigioihanobject-quytacdoitenobject"></a>

Các quy tắc sau áp dụng cho việc đổi tên object trong vStorage:

* Tên object phải dài từ 1 (tối thiểu) đến 255(tối đa) ký tự.
* Tên object có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), tất cả các ký tự đặc biệt và khoảng trắng nếu có.&#x20;
* Để hạn chế lỗi trong quá trình làm việc với các object sử dụng công cụ phía người dùng (client tool) hoặc trên vStorage, chúng tôi khuyến khích việc đặt tên object không nên sử dụng các ký tự đặc biệt như $, #, %, &, ^, v.v. và nên sử dụng hệ chữ viết Latin để đặt tên cho object, directory.

#### Quy định về dung lượng tối đa của tệp tin khi tải lên <a href="#phamvigioihanobject-quydinhvedungluongtoidacuateptinkhitailen" id="phamvigioihanobject-quydinhvedungluongtoidacuateptinkhitailen"></a>

* Không giới hạn số lượng tệp tin trong một lần tải lên hoặc tải xuống.
* Tổng dung lượng tối đa của các tệp tin trong một lần tải lên thông qua vStorage Portal là 20GB.
* Tổng dung lượng tối đa của các tệp tin trong một lần tải lên thông qua 3rd party software hoặc vStorage API là 5TB.
