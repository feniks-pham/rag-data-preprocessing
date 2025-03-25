# Quản lý Certificate

## Tổng quan

Tính năng **Quản lý Certificate** trên dịch vụ vCDN cho phép khách hàng **upload SSL Certificate và SSL Key**, bao gồm cả **key chain CA** (Certificate Authority). Điều này giúp thiết lập kết nối bảo mật HTTPS cho các tài nguyên CDN và đảm bảo rằng mọi dữ liệu được truyền qua mạng đều được mã hóa và bảo vệ.

***

## **Chi tiết**

* **Private Key**: file private key tương ứng với chứng chỉ SSL. Đây là khóa bảo mật của chứng chỉ, chỉ có máy chủ của bạn mới có quyền sử dụng.
* **SSL Certificate**: file certificate SSL của bạn. Đây là chứng chỉ do Certificate Authority (CA) phát hành, xác nhận rằng kết nối giữa người dùng và máy chủ là an toàn.
* **CA Root Chain**: Nếu chứng chỉ của bạn yêu cầu **Chain CA** (bao gồm các chứng chỉ trung gian giữa chứng chỉ SSL và CA gốc), bạn cần tải lên các chứng chỉ trung gian này dưới dạng một chuỗi (chain).&#x20;

## Các bước thực hiện

**Bước 1:** Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)

**Bước 2:** Chọn mục **Certificate**, sau đó chọn **Upload.**

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Chọn vào nút **Upload Private Key** để tải lên private key của Certificate, hoặc cũng có thể paste private key vào khung bên dưới.

**Bước 4:** Chọn vào nút Upload Certificate để tải lên file CRT/PEM của Certificate hoặc cũng có thể paste thông tin CRT/PEM vào khung bên dưới.

**Bước 5:** Chọn vào nút Upload CA Root Chain để tải lên thông tin certificate của nhà cung cấp chứng chỉ. Có thể để trống nếu không có thông tin. _<mark style="background-color:blue;">Một số trình duyệt phiên bản cũ có thể báo lỗi Certificate không hợp lệ nếu thiếu thông tin CA Root Chain.</mark>_

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1).png" alt="" width="278"><figcaption></figcaption></figure>

**Bước 6:** Sau khi nhập/upload đầy đủ thông tin, chọn **Save and Deploy** để lưu và kích hoạt certificate, sẳn sàng cho các CDN sử dụng.

Nếu chứng chỉ chưa sẳn sàng để dùng ngay, chọn **Save as Draft** để lưu trữ.

{% hint style="info" %}
**Chú ý:**

* vCDN do VNG Cloud cung cấp là dịch vụ phân phối nội dung thông qua giao thức HTTP có hỗ trợ TLS/SSL (HTTPS). Do vậy, các TLS Certificate - được tải lên bởi khách hàng nhằm mục đích mã hóa kênh truyền HTTP giữa người dùng và hệ thống máy chủ CDN - đồng thời được lưu trữ và quản lý bởi khách hàng và VNG Cloud cho đến khi khách hàng thực hiện lệnh xóa thông qua giao diện Web Portal/API.
* VNG Cloud cam kết không chia sẻ các TLS Certificate này cho bên thứ ba bất kỳ.
{% endhint %}
