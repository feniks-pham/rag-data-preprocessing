# Khởi tạo Pfsense trên HCM03

## Khởi tạo Pfsense

Để khởi chạy ứng dụng, làm theo các bước sau:

**Bước 1: Chọn tên và phiên bản ứng dụng**

**Bước 2: Chọn loại máy ảo (Instance type)** (sự kết hợp giữa CPU x RAM x GPU)

**Bước 3: Chọn cài đặt ổ đĩa (Volume)**

**Bước 4: Chọn cài đặt mạng (Network)** bao gồm các hành động sau:

* Chọn VPC cho ứng dụng
* Chọn thứ tự ưu tiên cho các giao diện mạng Bên ngoài và Bên trong: Lưu ý rằng các giao diện này sẽ được sắp xếp chính xác theo thứ tự người dùng nhập vào
* Chọn cài đặt bảo mật (Security): Chọn **Tạo mới nhóm bảo mật (New security group rules)** để tạo một nhóm mới với các tham số cụ thể cho ứng dụng của bạn, hoặc chọn **Nhóm bảo mật hiện có (Existing security group)** để kế thừa các quy tắc từ nhóm hiện tại

**Bước 5: Chọn cài đặt nhóm máy chủ (Server Group)**

* Để kích hoạt tính năng sẵn sàng cao (HA) cho các máy chủ tường lửa của bạn, hãy chọn **Dedicated SOFT ANTI AFFINITY group** để tạo một nhóm máy chủ mới cho ứng dụng tường lửa của bạn, hoặc chọn **Existing server group** nếu nó đã tồn tại

Sau khi máy ảo đã được cấp phát, hãy sửa đổi **Nhóm Bảo mật** để mở các cổng sau cho máy ảo:

* Truy cập qua vServer Console (từ webportal), Theo mặc định, mật khẩu để trống.&#x20;
* Cấu hình truy cập SSH/Web (từ webportal) Theo mặc định, bạn sẽ đăng nhập bằng mật khẩu trống, sau đó ứng dụng sẽ chuyển hướng bạn đến trang thay đổi mật khẩu, vui lòng thay đổi mật khẩu ngay lập tức (Để Mật khẩu cũ trống).&#x20;

**Lưu ý: Ứng dụng Marketplace sẽ khởi tạo trong vài phút.**

## Cấu hình interface thông qua Console&#x20;

* Assign Interface

<figure><img src="../../../../.gitbook/assets/image (675).png" alt=""><figcaption></figcaption></figure>

* Assigne WAN : vtnet0 ; LAN : vtnet1

<figure><img src="../../../../.gitbook/assets/image (676).png" alt=""><figcaption></figcaption></figure>

* WAN : vtnet0

<figure><img src="../../../../.gitbook/assets/image (677).png" alt=""><figcaption></figcaption></figure>

* LAN : vtnet1

<figure><img src="../../../../.gitbook/assets/image (678).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (679).png" alt=""><figcaption></figcaption></figure>

* Gán IP vào mạng LAN

<figure><img src="../../../../.gitbook/assets/image (680).png" alt=""><figcaption></figcaption></figure>

* Lấy IP được cấp trên Portal để gán vào LAN interface
* Gán IP vào interface

<figure><img src="../../../../.gitbook/assets/image (681).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (682).png" alt=""><figcaption></figcaption></figure>

* IP Local Pfsense là https://LocalIP/

<figure><img src="../../../../.gitbook/assets/image (683).png" alt=""><figcaption></figcaption></figure>

* Cấu hình Pfsense ban đầu : access vào https//local\_IP/ và tiến hành step by step cấu hình :&#x20;
