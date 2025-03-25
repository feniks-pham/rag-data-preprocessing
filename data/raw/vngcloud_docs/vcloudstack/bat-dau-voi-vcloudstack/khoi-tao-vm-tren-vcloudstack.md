# Khởi tạo VM trên vCloudStack

## Tổng quan <a href="#tong-quan" id="tong-quan"></a>

Sau khi cấu hình thiết bị cơ sở hạ tầng và kết nối với hệ thống đám mây VNG Cloud thành công, người dùng có thể khởi tạo máy chủ ảo tại giao diện User Site trên cơ sở hạ tầng nội bộ. Ngoài ra, người dùng cần Tạo Network trước để sẵn sàng khởi tạo máy chủ ảo.

***

## Các bước thực hiện: <a href="#cac-buoc-thuc-hien" id="cac-buoc-thuc-hien"></a>

**Bước 1**: Người dùng truy cập và đăng nhập vào User Site;

{% hint style="info" %}
Nếu người dùng truy cập vào mục vServer của VNG Cloud, thì có thể truy cập vào vCloudstack đã đăng ký bằng cách click vào mục Region và **chọn đến Region của vCloudStack**
{% endhint %}

**Bước 2:** Tại giao diện User Site, Trên thanh Điều hướng, chọn mục Server/Servers;

**Bước 3:** Tại màn hình Servers, chọn Tạo mới một Server;

**Bước 4:** Tại màn hình Tạo Server, cho phép người dùng điền các thông tin để khởi tạo như sau:

* **Tên server**: điền tên server để nhận diện server sau khi tạo;
* **Thẻ (Tag):** Gắn thẻ cho server;
* **Image của bạn:**
  * OS: Chọn hệ điều hành cho Server
  * My Images: Hoặc chọn Image đã tạo cho Server
  * My Backup: Hoặc chọn phục hồi Server với file Backup đã tạo
  * My Snapshot: Hoặc chọn phục hồi server với file Snapshot đã tạo.
* **Loại cấu hình** (Instance type): Chọn cấu hình cho Server phù hợp với nhu cầu.
* **Volume settings:** Cấu hình loại ổ đĩa bằng cách chọn loại ổ đĩa, dung lượng và IOPS.

{% hint style="info" %}
vCloudStack cung cấp tùy chọn cho phép **Mã hóa Volume (Encryption Volume)**, chức năng cho phép toàn bộ dự liệu lưu trữ lưu trên Volume này được mã hóa, tránh dữ liệu bị mất nhưng tin tặc vẫn không sử dụng hay xem được.
{% endhint %}

* **Cài đặt mạng:**
  * Chọn Network cho Server đã tạo trước ở trang Admin Site. (Có thể điền IP hoặc hệ thống tự chọn IP)
  * Chọn nhóm bảo mật - Security Group
  * Chọn 1 trong 2 tùy chọn thông tin đăng nhập:
    * Tùy chọn 1: Thông tin cơ bản - Base Data: Chọn SSH key đã tạo và điều thông tin Usename/Mật khẩu;
    * Tùy chọn 2: Thông tin người dùng - User Data: Tải file hoặc nhập trực tiếp thông tin người dùng

{% hint style="info" %}
**Lưu ý:** Nếu thông tin người dùng đã được mã hóa, hãy chọn vào ô “**Thông tin user đã được mã hóa base 64**”.
{% endhint %}

* Cài đặt khác:
  * Cài đặt Backup: chọn tùy chọn “Kích hoạt Backup” để hệ thống dựa vào backup policy mặc định để tạo tệp tin Server Backup;
  * Chọn nhóm máy chủ - Placement Group để gộp nhóm các máy chủ lại với nhau;

{% hint style="info" %}
**Lưu ý:** Việc gộp nhóm các máy chủ ào một nhóm liên quan đến việc cho phép các máy chủ được cấp phát trên một host vật lý hay không để đảm bảo hiệu năng cũng như tính sẳn sàng của các máy chủ. (_Xem thêm ở mục Server Group_)
{% endhint %}

**Bước 5:** Xem lại tất cả thông tin khởi tạo máy chủ ảo ở bên trái của màn hình giao diện. Sau đó chọn nút **Khởi tạo Server**.

**Bước 6:** Hệ thống thực hiện khởi tạo thành công, người dùng có thể truy cập vào máy chủ để sử dụng và vận hàng.

&#x20;
