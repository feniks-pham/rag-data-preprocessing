# Chỉnh sửa phương thức truy cập

## Kiểm soát truy cập đến Kafka Cluster

Các tùy chọn Access Method và chức năng

* **mTLS (Mutual TLS):** Đảm bảo tính bảo mật cao bằng cách yêu cầu cả client và server xác thực lẫn nhau thông qua chứng chỉ số. Điều này giúp ngăn chặn các kết nối không được ủy quyền và bảo vệ dữ liệu nhạy cảm.
* **SASL (Simple Authentication and Security Layer):** Cung cấp cơ chế xác thực người dùng linh hoạt, cho phép sử dụng các phương thức xác thực khác nhau như username/password.
* **Public Accessibility:** Cho phép truy cập từ bên ngoài VPC (Virtual Private Cloud) của bạn, ví dụ như từ các ứng dụng khác không nằm trong vDB Kafka Cluster. Tùy chọn này thường được sử dụng khi bạn cần tích hợp Kafka với các dịch vụ bên ngoài.

## Chỉnh sửa truy cập công khai (Public Accessibility)

**1. Chọn Cụm Kafka:** Đăng nhập vào vDB Kafka Cluster tại đây và chọn cụm Kafka mà bạn muốn điều chỉnh.

**2. Bật/Tắt Truy Cập Công Khai:** Tại trang quản lý Kafka Cluster, tìm tùy chọn tính năng "Edit Accessibility" và bật hoặc tắt tùy chọn này để cho phép hoặc chặn truy cập từ bên ngoài VPC.

**3. Lưu Thay đổi:** Sau khi đã chọn, nhấp vào nút "Lưu" hoặc tương tự để áp dụng các thay đổi.

**Lưu ý:**

* Bật "Public Accessibility" có thể làm tăng nguy cơ về bảo mật. Hãy cân nhắc kỹ trước khi bật tùy chọn này và đảm bảo rằng bạn đã áp dụng các biện pháp bảo mật phù hợp.
* Nếu bạn tắt "Public Accessibility", các ứng dụng bên ngoài VPC sẽ không thể kết nối đến cụm Kafka nữa. Hãy đảm bảo rằng bạn đã cập nhật cấu hình các ứng dụng này để sử dụng các phương thức kết nối khác (ví dụ: thông qua VPN) nếu cần thiết.

## Chỉnh sửa access method (mTLS, SASL)

**1. Chọn Cụm Kafka:** Đăng nhập vào vDB Kafka Cluster tại đây và chọn cụm Kafka mà bạn muốn điều chỉnh.

**2. Chọn các Phương thức Xác thực:** Tại trang quản lý Kafka Cluster, tìm và chọn tính nắng "Edit Access Control Method".

* **mTLS:** Bật hoặc tắt tùy chọn mTLS. Nếu bật, bạn có thể cần cấu hình thêm các chứng chỉ số cho client và server.
* **SASL:** Bật hoặc tắt tùy chọn SASL. Nếu bật, bạn có thể cần cấu hình thêm các cơ chế xác thực cụ thể (ví dụ: username/password).

**3. Lưu Thay đổi:** Sau khi đã chọn, nhấp vào nút "Lưu" hoặc tương tự để áp dụng các thay đổi.

**Lưu ý:**

* Việc thay đổi phương thức xác thực có thể ảnh hưởng đến khả năng kết nối của các ứng dụng hiện tại đến cụm Kafka. Hãy đảm bảo rằng bạn đã cập nhật cấu hình các ứng dụng của mình để sử dụng phương thức xác thực mới nếu cần thiết.
* Nếu bạn gặp bất kỳ lỗi kết nối nào sau khi thay đổi, hãy kiểm tra lại cấu hình access method và cấu hình ứng dụng của bạn.

**Kết luận**

Việc chỉnh sửa access method cho phép bạn kiểm soát chặt chẽ hơn việc truy cập vào cụm Kafka, đảm bảo tính bảo mật và an toàn cho dữ liệu của bạn. Bằng cách lựa chọn các phương thức truy cập phù hợp, bạn có thể tạo ra một môi trường Kafka an toàn và đáng tin cậy cho các ứng dụng của mình.
