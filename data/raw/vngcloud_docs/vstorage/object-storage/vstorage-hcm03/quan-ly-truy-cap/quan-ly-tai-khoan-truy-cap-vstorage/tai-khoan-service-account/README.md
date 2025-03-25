# Tài khoản Service Account

#### Tổng quan <a href="#taikhoanserviceaccount-tongquan" id="taikhoanserviceaccount-tongquan"></a>

Service Account là một danh tính mà bạn có thể tạo trong tài khoản của mình có các quyền cụ thể. Service Account có một số điểm tương đồng với người dùng IAM. Service Account và IAM User Account đều là danh tính với các Policy cho phép xác định những gì danh tính có thể và không thể làm với tài nguyên Đám mây của VNG. Tuy nhiên, Service Account là danh tính được sử dụng bởi một ứng dụng hoặc một máy chứ không phải một người, để thực hiện các lệnh gọi API được ủy quyền và truy cập các tài nguyên được chỉ định. Để biết thêm thông tin về Service account, hãy xem tại [đây.](https://docs.vngcloud.vn/pages/viewpage.action?pageId=59805240)

Để truy cập và làm việc với các tài nguyên vStorage sử dụng tài khoản Service Account, bên cạnh tài khoản Service Account, bạn cần tạo thêm **vStorage Credentials** - chính là các cặp S3 keys và tài khoản người dùng Swift - được gắn vào tài khoản Service Account đó.

***

#### Chủ đề <a href="#taikhoanserviceaccount-chude" id="taikhoanserviceaccount-chude"></a>

* Khởi tạo tài khoản Service Account
* Khởi tạo policy cho Service Account
* Liên kết tài khoản Service Account với policy tương ứng
* Khởi tạo vStorage Credentials
  * Khởi tạo S3 key
  * Khởi tạo Swift user
  * Liên kết S3 key, Swift user với tài khoản Service Account tương ứng
  * Hủy S3 key, Swift user
* Hủy tài khoản Service Account

\
