# Quản lý cấu hình (config group)

## Kafka Config Group là gì?

Kafka Config Group là một tập hợp các tham số cấu hình (configurations) của Kafka. Bạn có thể tạo nhiều Config Group khác nhau để quản lý các cấu hình cho từng môi trường (development, staging, production) hoặc các ứng dụng khác nhau.

## Quản lý Kafka Config Group

**1. Tạo mới Config Group**

* **Truy cập Kafka Config Group:** Đăng nhập vào vDB và chọn trang Config Group tại đây:
* **Nhấn nút "Tạo mới":** Nhấn nút "Tạo config Group" để bắt đầu tạo Config Group mới.
* **Đặt tên và mô tả:** Nhập tên cho Config Group và một mô tả ngắn gọn (tùy chọn).
* **Thêm các tham số cấu hình:** Thêm các tham số Kafka cần thiết vào Config Group. Bạn có thể sử dụng giao diện đồ họa hoặc nhập trực tiếp các tham số dưới dạng văn bản.
* **Lưu Config Group:** Nhấn nút "Lưu" để tạo Config Group mới.

**2. Tạo mới Version từ Config Group**

* **Chọn Config Group:** Từ danh sách Config Groups, chọn Config Group bạn muốn tạo phiên bản mới.
* **Nhấn nút "Tạo version":** Tìm và nhấn nút "Tạo version".
* **Chọn phiên bản nguồn (tùy chọn):**
  * Mặc định, phiên bản mới sẽ sao chép cấu hình từ phiên bản mới nhất (latest version).
  * Bạn cũng có thể chọn một phiên bản cụ thể để sao chép cấu hình từ đó. Điều này giúp bạn dễ dàng áp dụng cấu hình tương tự cho nhiều cụm Kafka khác nhau và giảm thiểu rủi ro khi điều chỉnh.
* **Chỉnh sửa tham số (nếu cần):** Nếu bạn muốn thay đổi cấu hình, hãy chỉnh sửa các tham số trong phiên bản mới này.
* **Lưu phiên bản mới:** Nhấn nút "Lưu" để tạo phiên bản mới của Config Group.

**3. Áp dụng Config Group vào Kafka Cluster**

* **Chọn cụm Kafka:** Chọn cụm Kafka bạn muốn áp dụng cấu hình.
* **Chọn mục "Cấu hình":** Trong giao diện quản lý cụm Kafka, tìm và chọn mục "Cấu hình".
* **Chọn Config Group:** Từ danh sách Config Groups, chọn Config Group bạn muốn áp dụng.
* **Chọn phiên bản:** Nếu Config Group có nhiều phiên bản, hãy chọn phiên bản cụ thể bạn muốn áp dụng.
* **Xác nhận và áp dụng:** Xem lại các thay đổi và nhấn nút "Áp dụng" để cập nhật cấu hình cho cụm Kafka.

**4. Xóa Version hoặc Config Group**

* **Chọn Version hoặc Config Group:** Từ danh sách, chọn Version hoặc Config Group bạn muốn xóa.
* **Kiểm tra điều kiện xóa:** Hệ thống sẽ kiểm tra xem Version hoặc Config Group đó có đang được áp dụng cho bất kỳ cụm Kafka nào không.
* **Xác nhận và xóa:** Nếu không có cụm Kafka nào đang sử dụng, bạn có thể nhấn nút "Xóa" để xóa Version hoặc Config Group đó. Nếu đang được sử dụng, bạn sẽ nhận được thông báo và không thể xóa cho đến khi gỡ bỏ khỏi các cụm Kafka liên quan.

**Lưu ý quan trọng:**

* Việc thay đổi cấu hình có thể ảnh hưởng đến hoạt động của cụm Kafka. Hãy đảm bảo bạn hiểu rõ các tham số trước khi áp dụng.
* Nên tạo phiên bản mới của Config Group trước khi thực hiện các thay đổi lớn, để có thể dễ dàng quay lại phiên bản cũ nếu cần.
* Luôn kiểm tra kỹ các thay đổi trên môi trường thử nghiệm trước khi áp dụng lên môi trường production.
