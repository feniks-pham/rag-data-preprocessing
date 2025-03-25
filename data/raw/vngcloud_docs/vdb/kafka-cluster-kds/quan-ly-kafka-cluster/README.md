# Quản lý Kafka Cluster

Kafka Cluster DB không phải là một cơ sở dữ liệu truyền thống. Nó là một cụm máy chủ Kafka hoạt động cùng nhau để lưu trữ và xử lý luồng sự kiện theo thời gian thực. Kafka Cluster DB giúp tăng khả năng mở rộng, độ bền dữ liệu và hiệu suất xử lý so với việc sử dụng một máy chủ Kafka đơn lẻ.

**Nó thường được sử dụng để:**

* Xử lý dữ liệu theo thời gian thực
* Xây dựng hệ thống nhắn tin
* Ghi log tập trung

**Theo dõi các bài viết sau để hiểu hơn về cách sử dụng Kafka Cluster:**

* **Tạo Cụm Kafka Cluster:** Để bắt đầu sử dụng Kafka trên nền tảng vDB, bạn cần tạo một cụm Kafka. Cụm này sẽ là nơi lưu trữ và xử lý các sự kiện (events) của ứng dụng bạn.
* **Scale Up/Down Số Lượng Broker:** Cần scale up khi lưu lượng dữ liệu tăng cao, việc tăng số lượng broker giúp phân tán tải, đảm bảo hiệu suất và khả năng chịu lỗi của hệ thống. Ngược lại, cần scale down khi lưu lượng dữ liệu giảm, giảm số lượng broker giúp tiết kiệm tài nguyên.
* **Scale Up Broker Storage:** Khi dữ liệu tích lũy ngày càng nhiều, việc tăng dung lượng lưu trữ giúp đảm bảo cụm Kafka không bị đầy và vẫn hoạt động ổn định.
* **Chỉnh Sửa Config Group:** Kafka có rất nhiều tham số cấu hình ảnh hưởng đến hiệu suất, độ bền dữ liệu, và các khía cạnh khác. Việc chỉnh sửa config group cho phép bạn tùy chỉnh Kafka theo yêu cầu cụ thể của ứng dụng.
* **Chỉnh Sửa Access Method**: mTLS đảm bảo tính bảo mật cao hơn bằng cách xác thực hai chiều giữa client và server; SASL cung cấp cơ chế xác thực người dùng linh hoạt.
* **Public Accessibility:** Cho phép truy cập từ bên ngoài.
* **Quản Lý Topic**: vDB Kafka Cluster cung cấp các tính năng quản lý topic như sau tạo, xóa, sửa,...
* **Quản Lý User:** vDB Kafka Cluster cung cấp các tính năng quản lý kafka user như tạo, xóa, sửa permission, access method, re-Generate Certificate,...

#### Lưu ý:

* Luôn kiểm tra kỹ cấu hình trước khi áp dụng thay đổi.
* Sao lưu dữ liệu quan trọng trước khi thực hiện các thay đổi lớn.
* Tham khảo tài liệu hướng dẫn chi tiết của vDB Kafka Cluster để biết thêm thông tin.
