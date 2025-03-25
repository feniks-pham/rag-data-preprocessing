# Khởi tạo Kafka Cluster

Việc khởi tạo cụm Kafka là bước quan trọng đầu tiên để xây dựng một hệ thống xử lý dữ liệu phân tán, có khả năng mở rộng và chịu lỗi cao. Phần hướng dẫn này sẽ giúp bạn từng bước khởi tạo một cụm Kafka mới trên nền tảng đám mây, sử dụng giao diện quản lý trực quan và các tùy chọn cấu hình linh hoạt.

Bằng cách làm theo hướng dẫn này, bạn sẽ có thể nhanh chóng triển khai một cụm Kafka sẵn sàng sử dụng, đặt nền móng vững chắc cho việc xây dựng các ứng dụng dữ liệu mạnh mẽ và đáng tin cậy.

## **Bước 1: Truy cập Giao diện Quản lý Kafka**

1. Mở trình duyệt web và truy cập vào giao diện quản lý Kafka của VNG Cloud tại đây:&#x20;
2. Đăng nhập vào tài khoản của bạn. Nếu bạn chưa có tài khoản, hãy đăng ký một tài khoản mới.

## **Bước 2: Bắt đầu Tạo Cụm Kafka**

Tìm và nhấp vào nút "Tạo Kafka Cluster", cấu hình thông tin Kafka Cluster như sau:

1. **Tên Cụm:**
   * Nhập một tên mô tả cho cụm Kafka của bạn. Tên này sẽ giúp bạn dễ dàng nhận diện và quản lý cụm trong tương lai.
   * Lưu ý rằng tên này sẽ không thể thay đổi sau khi khởi tạo.
2. **Phiên bản Kafka:**
   * Chọn phiên bản Kafka mà bạn muốn sử dụng. Lưu ý rằng các phiên bản khác nhau có thể có các tính năng và khả năng tương thích khác nhau.
   * Lưu ý rằng hiện tại, vDB Kafka Cluster chưa hỗ trợ upgrade version đối với Kafka Cluster đang hoạt động, tính năng sẽ được hỗ trợ trong thời gian tới.
3. **Cấu hình Phần cứng (Flavor):**
   * Chọn cấu hình phần cứng (flavor) cho các broker trong cụm Kafka của bạn. Các flavor thường bao gồm các tùy chọn về CPU, RAM và Network. Chọn một flavor phù hợp với khối lượng công việc dự kiến của bạn.
4. **Số lượng Broker:**
   * Xác định số lượng broker mà bạn muốn có trong cụm Kafka của bạn. Số lượng broker ảnh hưởng đến khả năng chịu lỗi, khả năng mở rộng và hiệu suất của cụm.
5. **Lưu trữ cho mỗi Broker:**
   * Chọn dung lượng lưu trữ và IOPS (Số lượng hoạt động nhập/xuất mỗi giây) cho mỗi broker. Lưu ý rằng yêu cầu về lưu trữ có thể thay đổi tùy thuộc vào khối lượng dữ liệu mà bạn dự định xử lý.
6. **Mạng (VPC và Subnet):**
   * Chọn mạng ảo (VPC) và subnet mà bạn muốn triển khai cụm Kafka của bạn. Hãy chắc chắn rằng VPC và subnet đã được cấu hình đúng cách và cho phép giao tiếp cần thiết.
7. **Kiểm soát Phương thức Truy cập:**
   * Chọn phương thức xác thực và ủy quyền mà bạn muốn sử dụng cho cụm Kafka của mình. Các tùy chọn phổ biến bao gồm mTLS và SASL.
8. **Chế độ Mã hóa:**
   * Chọn chế độ mã hóa dữ liệu. Mặc định, mã hóa in transit (dữ liệu được mã hóa khi truyền giữa client và broker) và within cluster (dữ liệu được mã hóa khi lưu trữ trên các broker) được bật.
9. **Nhóm Cấu hình:**
   * Nếu có, chọn một nhóm cấu hình để áp dụng các thiết lập cấu hình cụ thể cho cụm Kafka của bạn.

## **Bước 3: Xem lại và Khởi tạo**

1. Xem lại tất cả các cấu hình mà bạn đã chọn để đảm bảo rằng chúng chính xác.
2. Xem lại chi phí chi trả tương ứng với cấu hình bạn vừa chọn.
3. Nhấp vào nút "Khởi tạo" để bắt đầu quá trình khởi tạo cụm Kafka.

## **Bước 4: Theo dõi Tiến trình**

1. Theo dõi tiến trình khởi tạo cụm Kafka thông qua giao diện quản lý. Quá trình này có thể mất một chút thời gian tùy thuộc vào cấu hình mà bạn đã chọn.
2. Sau khi cụm Kafka được khởi tạo thành công, bạn có thể bắt đầu sử dụng nó để tạo topic, produce và consume dữ liệu.
