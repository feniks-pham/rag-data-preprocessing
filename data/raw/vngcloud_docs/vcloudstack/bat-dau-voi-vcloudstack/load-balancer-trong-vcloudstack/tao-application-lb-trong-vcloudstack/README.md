# Tạo Application LB trong vCloudStack

Trong bài viết này, ta sẽ tìm hiểu về cách sử dụng và quản lý một Application Load Balancer (ALB) với dịch vụ vCloudStack.

## **Điều kiện tiêu quyết:**

* Cần có một Network để thực hiện, tham khảo bài viết cấu hình Network;
* Có tài khoản truy cập vào VNG Cloud với Region CloudStack của doanh nghiệp;
* Có ít nhất một chứng chỉ TLS/SSL.

## **Cách thực hiện:**

**Bước 1:** Tại trang chủ Load Balancers, click chọn **"Create a Load Balancer".**

**Bước 2:** Cấu hình Load Balancer

* _**Tên Load Balancer**_**:** Trường hợp người dùng không chủ động điền tên Load Balancer, hệ thống sẽ tự động sinh ra tên Load Balancer.
* _**Layer**_**:** Chọn **"Application - HTTP/HTTPS"**
* **Tags:** Điền Tags và giá trị để đánh dấu của Load Balancer sẽ tạo
* _**Load Balancer Package**_: Chọn gói khởi tạo phù hợp với nhu cầu và mục đích sử dụng, lưu ý rằng gói này là yếu tố chính dùng để khởi tạo và vận hành Load Balancer của bạn
* _**Cài đặt Network**_**: Chọn Network (VPC)** có sẵn từ danh sách network của bạn, trường hợp chưa khởi tạo VPC, tham khảo hướng dẫn <mark style="color:blue;">Cấu hình Network</mark>.

{% hint style="info" %}
Dịch vụ vCloudStack chỉ áp dụng **cơ chế Scheme là Internal**, tức chỉ cho phép truy cập với mạng nội bộ, do đó mặc định hệ thống cấu hình với cơ chế Internal.
{% endhint %}

**Bước 3**: Cấu hình Listener

* **Tên Listener:** Trường hợp người dùng không chủ động điền tên Listener, hệ thống sẽ tự động sinh ra tên Listener.
* **Giao thức & Cổng (Protocol & Port)**
  * Trường hợp chọn Giao thức (Protocol) = **HTTP**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **80**) và **Header** (mặc định điền sẵn X-Fowarded-For, X-Forwarded-Proto, X-Fowarded-Port, có thể bỏ chọn Header nếu không có nhu cầu).
  * Trường hợp chọn Giao thức (Protocol) = **HTTPS**: Người dùng cần **chọn Port** (mặc định điền sẵn Port **443**) và **Certificate** (tham khảo hướng dẫn [Upload a certificate](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/certificate/upload-a-certificate.md) nếu chưa có Certificate).

**Bước 4:** Cấu hình Pool mặc định

* **Tên Pool**: Trường hợp người dùng không chủ động điền tên Pool, hệ thống sẽ tự động sinh ra tên Pool.
* **Giao thức HTTP mặc định**
* **Thuật toán:** Chọn thuật toán cân bằng tải phù hợp
* **Cài đặt Health Check**: Giao thức: TCP / HTTP (nhập đường dẫn mặc định trong trường hợp chọn Giao thức HTTP)

**Bước 5:** Chọn Pool Member: Thêm các máy chủ backend vào Pool

* **Chọn Pool Member** từ một danh sách các máy chủ backend khả dụng thuộc Load Balancer Network (cùng subnet với LB)
* **Click nút "Gắn / Attach"** để thực hiện việc thêm máy chủ thành viên

**Bước 6:** Kiểm tra thông tin khởi tạo: Người dùng có thể kiểm tra thông tin cấu hình trước khi hoàn tất khởi tạo, phần thông tin này sẽ được hiển thị phía bên phải màn hình nhập liệu

* **Tab "Tóm tắt / Summary"**: Kiểm tra lần lượt các thông tin cấu hình Load Balancer, Listener, Pool và Pool Member
* **Tab " Danh sách / Item list":** Kiểm tra thông tin Load Balancer Package&#x20;

**Bước 7:** Hoàn tất khởi tạo: Sau khi hoàn tất việc cấu hình và kiểm tra thông tin, click nút "Tạo load Balancer / Create Load Balancer" để hoàn tất việc khởi tạo.

**Bước 8:** Quan sát và kiểm tra ALB

* Sau khi hoàn tất khởi tạo thành công, hệ thống sẽ điều hướng người dùng đến trang danh sách Load Balancer, tại đây người dùng có thể theo dõi trạng thái khởi tạo Load Balancer từ **Creating (đang khởi tạo)** đến khi **Active (Khởi tạo thành công).**
* Sau khi khởi tạo thành công, người dùng có thể truy cập vào trang chi tiết Load Balancer để quan sát và kiểm tra tính đúng đắn của Load Balancer.

Trên đây là các hướng dẫn cơ bản trong việc khởi tạo Application Load Balancer một cách nhanh chóng nhất. Ngoài ra, còn có các cấu hình nâng cao cho từng nhu cầu sử dụng Load Balancer khác nhau. Cùng tìm hiểu chi tiết cách hoạt động cũng như các tính năng nâng cao của một Application Load Balancer thông qua chuỗi bài viết Các tính năng nâng cao.

