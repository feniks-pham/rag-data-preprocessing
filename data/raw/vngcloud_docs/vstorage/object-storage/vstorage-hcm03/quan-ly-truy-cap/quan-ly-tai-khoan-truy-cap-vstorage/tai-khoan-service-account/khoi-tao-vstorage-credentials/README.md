# Khởi tạo vStorage Credentials

#### **Tổng quan** <a href="#khoitaovstoragecredentials-tongquan" id="khoitaovstoragecredentials-tongquan"></a>

vStorage Credentials là các cặp key mà cho phép bạn tạo và cấp quyền để truy cập vStorage project/container. vStorage credentials bao gồm 2 loại chính

* S3 key: là cặp s3 key có access key và secret key được vStorage tích hợp để có tính tương thích với các client tool của S3 như s3cmd, s3 SDK,...
* Swift user: là cặp user/password được hỗ trợ chính của vStorage.

#### **Quyền hạn của vStorage credentials** <a href="#khoitaovstoragecredentials-quyenhancuavstoragecredentials" id="khoitaovstoragecredentials-quyenhancuavstoragecredentials"></a>

* Khi s3 key/swift user được tạo ra, mặc định vẫn sẽ có đầy đủ quyền truy cập vào các vStorage project/container (thiết lập Restriction by IAM mặc định là NO), để có thể phân quyền các cặp key và user này, đầu tiên bạn cần bật thuộc tính Restriction by IAM thành YES
* Khi bạn bật thuộc tính Restriction by IAM thành YES, các cặp key và user này sẽ được quản lý và phân quyền bởi IAM, vì vậy mặc định các cặp key và user đã bật sẽ không có quyền truy cập bất kì vStorage project/container nào.
* Sau khi bật Restriction by IAM thành YES, để có thể phân quyền bạn cần gắn các key, user vào các Service Account để chúng thừa hưởng quyền trên Service Account được gắn.

***

#### Chủ đề <a href="#khoitaovstoragecredentials-chude" id="khoitaovstoragecredentials-chude"></a>

* Khởi tạo S3 key
* Khởi tạo Swift user
* Liên kết S3 key, Swift user với tài khoản Service Account tương ứng
* Hủy S3 key, Swift user

\
