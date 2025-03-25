# Tạo Cross Connect

**Thực hiện các bước sau để thực hiện việc tạo một kết nối Cross Connect:**

**Bước 1:** Truy cập thành công vào VNG Cloud, tại màn hình Console chọn đến dịch vụ vNetwork;

**Bước 2:** Tại thanh menu bên trái của giao diện vNetwork, chọn mục Cross Connect;

**Bước 3:** Màn hình được điều hướng tới màn hình Danh sách Cross Connect;

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

**Bước 4:** Tại màn hình danh sách các Cross Connect, nhấn chọn "<mark style="color:blue;">**Tạo Cross Connect**</mark>";

**Bước 5:** Tại màn hình Create a Cross Connect, điền các thông tin khởi tạo như sau:

* <mark style="color:blue;">**Tên Cross Connect**</mark>: Điền tên của Cross Connect được tạo;
* Mô tả: (tùy chọn) Điền mô tả về Cross Connect được tạo;
* <mark style="color:blue;">**Cấu hình Cross Connect**</mark>: Chọn Requester (mặc định theo vùng đang cấu hình) và Accepter là hai region cần kết nối giao tiếp với nhau;
* <mark style="color:blue;">**Cấu hình Băng thông:**</mark> Chọn gói băng thông phù hợp với nhu cầu.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

**Bước 6:** Tại bên phải màn hình, xem tổng chi phí gói Băng thông đã chọn, sau đó nhấn chọn "<mark style="color:blue;">**Tạo**</mark>" đề xác nhận và tiến hành thanh toán;

**Bước 7:** Sau khi thanh toán thành công, hệ thống sẽ xử lý kết nối thành công tuyến Cross Connect vừa tạo.

{% hint style="success" %}
**Lưu ý:**

* Tại màn hình danh sách Cross Connect, có thể thấy Cross Connect vừa tạo với trạng thái "<mark style="color:blue;">**Provisioning**</mark>" (là trạng thái hệ thống đang thiết lập kết nối);
* Quá trình thiết lập tuyến Cross Connect này, hệ thống cần nhiều thời gian để thực hiện xác thực giữa hai vùng, do đó có thể <mark style="color:blue;">**mất tối đa 20 phút để xử lý**</mark>, sau khi hệ thống xử lý xong thì trạng thái sẽ tự động chuyển thành "<mark style="color:blue;">**Active**</mark>".
* Lúc này người dùng có thể thực hiện thiết lập [Tạo kết nối VPC giữa hai vùng](tao-ket-noi-vpc.md).
{% endhint %}

