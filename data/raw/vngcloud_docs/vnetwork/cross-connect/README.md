# Cross Connect

## Tổng quan

**Cross Connect** là một kết nối mạng giữa hai VPC với nhau cho phép bạn định tuyến lưu lượng giữ chúng bằng cách sử dụng địa chỉ IPv4 riêng kết nối đến các region khác nhau. Các máy chủ ảo (VM) có gán VPC có thể liên kết giao tiếp nếu tất cả có cùng một kết nối với nhau ở những vùng khác nhau.

Để thiết lập một kết nối **Cross Connect**, cần ghép cặp kết nối từ yêu cầu của VPC ở một vùng (**Requester**) và có sự chấp thuận của một VPC ở vùng khác (**Accepter**). Một khi kết nối được thiết lập, bạn có thể định tuyến kết nối giữa các VPC, điều này cho phép máy chủ ảo (VM) của một VPC có thể truy cập vào tài nguyên của một VPC ở vùng khác.

## Kết nối VPC trong Cross Connect

Để hiểu rõ về kết nối VPC trong Cross Connect của hai vùng, hãy xem mô tả cụ thể bên dưới về một kết nối Cross Connect giữa 2 VPC của hai vùng Hà Nội và Hồ Chí Minh:

Giả thiết đang có 2 vùng dữ liệu là Hồ Chí Minh (HCM03) và Hà Nội (HAN01), mỗi vùng đều đã thiết lập sẵn các VPC từ trước.&#x20;

Region HCM03 có các VPC:

* HCM-VPC01 (10.10.0.0/16);
* HCM-VPC02 (10.11.0.0/16);

Region HAN01 có các VPC:

* HAN-VPC01 (10.13.0.0/16);
* HAN-VPC02 (10.14.0.0/16);

Thực hiện việc tạo Cross Connect 1 để tạo tuyền kết nối giữa hai vùng Hồ Chí Minh và Hà Nội, từ đó tạo kết nối với các cặp VPC với nhau giữa hai vùng:

* HCM-VPC01 kết nối với HAN-VPC01;
* HCM-VPC01 kết nối với HAN-VPC02;
* HCM-VPC02 kết nối với HAN-VPC02;

<figure><img src="../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Sơ đồ kết nối cơ bản của một tuyền Cross Connect giữa HCM03 và HAN01</p></figcaption></figure>

***

VNG Cloud cung cấp cho người dùng dịch vụ Cross Connect có thể thực hiện các tác vụ như sau:

* [Tạo kết nối Cross Connect](tao-cross-connect.md);
* [Tạo kết nối VPC giữa hai region](tao-ket-noi-vpc.md);
* [Xóa kết nối Cross Connect](xoa-cross-connect.md);
* [Kiểm tra điều kiện kết nối VPC](kiem-tra-dieu-kien-ket-noi-vpc.md).



