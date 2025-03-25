# Kiểm tra điều kiện kết nối VPC

Để thực hiện giao tiếp với hai vùng thông qua Cross Connect cần thực hiện cấu hình kết nối giữa hai VPC, theo đó để kết nối thành công giữa hai VPC cần thỏa các điều kiện, nếu không hệ thống sẽ báo lỗi không có phép thiết lập kết nối.

### **Các điều kiện để hai VPC kết nối với nhau là:**

<table><thead><tr><th width="88">STT</th><th width="424">Điều kiện</th><th>Báo lỗi</th></tr></thead><tbody><tr><td>1</td><td>Hai VPC của hai vùng (region) không được trùng CIDR.</td><td>CIDR bị trùng lấp lẫn nhau (mã 2009)</td></tr><tr><td>2</td><td>Không cho phép kết nối giữa hai VPC đang tồn tại kết nối với nhau. <br>Dù là tạo một Cross Connect khác cũng không cho phép thực hiện kết nối.</td><td><a href="kiem-tra-dieu-kien-ket-noi-vpc.md#ma-loi-2010-dang-ton-tai-mot-cap-ket-noi-vpc-san-truoc">Đang tồn tại một VPC Connect cho cặp Vpc này (mã 2010)</a></td></tr><tr><td>3</td><td>Không cho tạo kết nối  VPC khi có một VPC đang kết nối trước đó ở chiều Requester trùng CIDR của VPC ở Accepter.</td><td><a href="kiem-tra-dieu-kien-ket-noi-vpc.md#ma-loi-2011-trung-cidr-cua-mot-ket-noi-vpc-trong-cross-connect-o-requester">Tồn tại một VPC Connection trong Cross Connect mở từ CIDR này (mã 2011)</a></td></tr><tr><td>4</td><td>Không cho tạo kết nối  VPC khi có một VPC đang kết nối trước đó ở chiều Accepter trùng CIDR của VPC ở Requester.</td><td><a href="kiem-tra-dieu-kien-ket-noi-vpc.md#ma-loi-2013-trung-cidr-cua-mot-ket-noi-vpc-trong-cross-connect-o-accepter">Tồn tại một VPC Connection trong Cross Connect mở đến CIDR này (mã 2013)</a></td></tr><tr><td>5</td><td>Hai VPC kết nối với nhau không ở chung một vùng (region).</td><td>Không được tạo VPC Connect trong cùng một Region (mã 2012)</td></tr></tbody></table>

## **Ví dụ về các mã lỗi khi tạo kết nối VPC:**

### <mark style="color:blue;">**\[**</mark><mark style="color:blue;">Mã lỗi 2010</mark><mark style="color:blue;">**] Đang tồn tại một cặp kết nối VPC sẵn trước**</mark>

<figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

Từ hình mô tả trên ta thấy rằng:

* Tại thời điểm T, người dùng có thể tạo thành công kết nối HCM-VPC01 đến HAN-VPC01 giữa hai vùng thông qua Cross Connect 1.
* Sau đó, tại thời điểm sau đó (T+1) thì hệ thống không cho phép việc tạo kết nối giữa HCM-VPC01 và HAN-VPC01 nữa, do đã tạo trước đó trong cùng một Cross Connect.
* Việc tạo cặp kết nối HCM-VPC01 đến HAN-VPC01 ở một Cross Connect khác vào thời điểm khác (T+2) cũng không thực hiện được, do hệ thống cũng sẽ kiểm tra việc một cặp VPC có đã tồn tại ở khác Cross Connect hay không.&#x20;

### <mark style="color:blue;">**\[Mã lỗi 2011] Trùng CIDR của một kết nối VPC trong Cross Connect ở**</mark>**&#x20;**<mark style="color:blue;background-color:red;">**Requester**</mark>

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

&#x20;         Từ hình mô tả trên ta thấy rằng:

* Tại thời điểm T, người dùng có thể tạo thành công kết nối HCM-VPC02 đến HAN-VPC01 giữa hai vùng thông qua Cross Connect 1.
* Sau đó, tại thời điểm sau đó (T+1) thì hệ thống không cho phép việc tạo kết nối HCM-VPC03 đến HAN-VPC03, do có CIDR 10.15.0.0/16 của HCM-VPC02 (đã kết nối với HAN-VPC01 trước đó) **trùng với CIDR của HAN-VPC03** mà HCM-VPC03 đang muốn kết nối đến.

### <mark style="color:blue;">**\[Mã lỗi 2013] Trùng CIDR của một kết nối VPC trong Cross Connect ở**</mark>**&#x20;**<mark style="color:blue;background-color:red;">**Accepter**</mark>

<figure><img src="../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

Từ hình mô tả trên ta thấy rằng:

* Tại thời điểm T, người dùng có thể tạo thành công kết nối HCM-VPC01 đến HAN-VPC02 giữa hai vùng thông qua Cross Connect 1.
* Sau đó, tại thời điểm sau đó (T+1) thì hệ thống không cho phép việc tạo kết nối HCM-VPC03 đến HAN-VPC03, do có CIDR 10.14.0.0/16 của HAN-VPC02 (đã kết nối với HCM-VPC01 trước đó) **trùng với CIDR của HCM-VPC03** đang muốn kết nối đến HAN-VPC03.
