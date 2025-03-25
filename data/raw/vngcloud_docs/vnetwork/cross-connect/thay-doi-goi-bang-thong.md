# Thay đổi gói băng thông

Trong trường hợp bằng thông không đáp ứng được nhu cầu của dịch vụ Cross Connect, người dùng có thể thay đổi băng thông bằng cách thay đổi Gói Bằng thông (Resize).

### **Thay đổi Gói Băng Thông** <a href="#thaydoikichthuocmaychuao-thaydoiflavor" id="thaydoikichthuocmaychuao-thaydoiflavor"></a>

Băng Thông (Bandwidth) là một thông số cấu hình định nghĩa cho tốc độ giao tiếp truyền dữ liệu. Khi cần thay đổi Băng thông cho đường truyền, người dùng sẽ chọn gói mới từ danh sách có sẵn.

Khi có nhu cầu thay đổi Băng Thông cho Cross Connect khi đang sử dụng, ta hoàn toàn có thể thực hiện thay đổi, hệ thống sẽ tính toán lại chi phí bổ sung hoặc hoàn trả số dư cho người dùng.

Chi phí và cách tính toán theo gói Băng thông mới sẽ xuất hiện ở bên phải màn hình khi người dùng thực hiện 'Thay đổi gói Băng thông'

### **Cách thực hiện** <a href="#thaydoikichthuocmaychuao-cachthuchien" id="thaydoikichthuocmaychuao-cachthuchien"></a>

Trước khi thực hiện thay đổi gói Băng thông của Cross Connect, bạn cần xác định trước gói cũng như tìm hiểu Băng thông nào là phù hợp với nhu cầu. Xem thêm tại [Các gói Băng Thông](cac-goi-bang-thong.md).

Chi tiết các bước thực hiện Thay đổi như sau:

**Bước 1:** Truy cập thành công vào VNG Cloud, tại màn hình Console chọn đến dịch vụ vNetwork;

**Bước 2:** Tại thanh menu bên trái của giao diện vNetwork, chọn mục Cross Connect;

**Bước 3:** Màn hình được điều hướng tới màn hình Danh sách Cross Connect;

**Bước 4:** Tìm đến Cross Connect muốn thay đổi Băng Thông, chọn nút '**Hành động**', sau đó nhấn '**Thay đổi gói**'.

<figure><img src="../../.gitbook/assets/image (790).png" alt=""><figcaption></figcaption></figure>

**Bước 5:** Màn hình '**Thay đổi gói**' hiển thị tất cả gói mà người dùng có thể thay đổi. Chọn vào gói muốn thay đổi.

{% hint style="info" %}
Lưu ý:

* Trường hợp thay đổi với gói có **Băng thông lớn hơn gói hiện tại** đang sử dụng, hệ thống sẽ tự động tính **thêm phí phát sinh** mà người dùng cần bổ sung khi tăng Băng thông.
* Trường hợp thay đổi với gói có **Băng thông nhỏ hơn gói hiện tại** đang sử dụng, hệ thống sẽ tự động tính **phí hoàn lại (refund)** mà người dùng khi giảm Băng thông.
{% endhint %}

**Bước 6:** Sau khi chọn gói phù hợp cần thay đổi, người dùng có thể xem tóm tắt chi phí phát sinh hoặc chi phí được hoàn lại trong trường hợp gói băng thông nhỏ hơn. Nhấn nút "Thay đổi gói" để hoàn thành. Khi trạng thái của CrossConnect từ '<mark style="color:blue;">**Changing**</mark>' trở lại '<mark style="color:blue;">**Active**</mark>**'** thì quá trình thay đổi băng thông hoàn tất.

<figure><img src="../../.gitbook/assets/image (791).png" alt=""><figcaption></figcaption></figure>





