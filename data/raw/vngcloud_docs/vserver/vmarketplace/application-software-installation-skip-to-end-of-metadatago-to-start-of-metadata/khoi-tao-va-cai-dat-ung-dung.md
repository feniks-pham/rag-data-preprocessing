# Khởi tạo và cài đặt ứng dụng

vMarketplace cung cấp nhiều ứng dụng (app) đã được build sẵn giúp bạn có thể ngay lập tức khởi tạo và cài đặt lên vServer chỉ trong vài bước.  Để khởi chạy ứng dụng, làm theo các bước sau:

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
