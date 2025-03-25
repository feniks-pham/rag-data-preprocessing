# Quản lý Kafka Topic

## Kafka Topic là gì?

Trong cụm Kafka, topic đóng vai trò là một kênh truyền tải dữ liệu, tương tự như một thư mục hoặc chủ đề trong hệ thống tập tin. Các nhà sản xuất (producer) gửi dữ liệu vào các topic, trong khi người tiêu dùng (consumer) đọc dữ liệu từ các topic đó. Mỗi topic có một tên duy nhất, giúp phân loại và tổ chức dữ liệu theo các chủ đề hoặc mục đích khác nhau.

**Cách hoạt động của Topic**

1. **Phân vùng (Partitions):**
   * Mỗi topic được chia thành nhiều phân vùng. Phân vùng là đơn vị cơ bản của tính song song và phân phối dữ liệu trong Kafka.
   * Mỗi phân vùng chứa một tập hợp các bản ghi (record) được sắp xếp theo thứ tự.
   * Các phân vùng cho phép mở rộng quy mô theo chiều ngang và cải thiện hiệu suất bằng cách phân phối dữ liệu trên nhiều broker trong cụm Kafka.
2. **Bản sao (Replicas):**
   * Mỗi phân vùng có thể có nhiều bản sao để đảm bảo tính chịu lỗi.
   * Một bản sao được chỉ định là leader, chịu trách nhiệm xử lý tất cả các hoạt động đọc và ghi cho phân vùng đó.
   * Các bản sao còn lại đóng vai trò là follower, sao chép dữ liệu từ leader để đảm bảo tính sẵn sàng của dữ liệu trong trường hợp leader gặp sự cố.
3. **Sản xuất (Produce):**
   * Các nhà sản xuất gửi dữ liệu đến các topic bằng cách ghi các bản ghi vào các phân vùng.
   * Kafka đảm bảo rằng các bản ghi được ghi vào phân vùng theo thứ tự.
4. **Tiêu thụ (Consume):**
   * Người tiêu dùng đọc dữ liệu từ các topic bằng cách đọc các bản ghi từ các phân vùng.
   * Kafka theo dõi vị trí đọc của mỗi người tiêu dùng, cho phép họ tiếp tục đọc từ nơi họ đã dừng lại trước đó.
5. **Lưu giữ (Retention):**
   * Kafka lưu trữ dữ liệu trong các topic trong một khoảng thời gian hoặc cho đến khi đạt đến một giới hạn dung lượng nhất định.
   * Điều này cho phép người tiêu dùng đọc lại dữ liệu cũ hoặc xử lý dữ liệu theo lịch trình linh hoạt.

**Chức năng của Topic**

* **Phân loại và tổ chức dữ liệu:** Topic cho phép bạn phân loại và tổ chức dữ liệu theo các chủ đề hoặc mục đích khác nhau, giúp dễ dàng quản lý và truy cập dữ liệu.
* **Mở rộng quy mô và hiệu suất:** Phân vùng trong topic cho phép mở rộng quy mô theo chiều ngang và cải thiện hiệu suất bằng cách phân phối dữ liệu trên nhiều broker.
* **Tính chịu lỗi:** Bản sao trong phân vùng đảm bảo tính chịu lỗi bằng cách sao chép dữ liệu trên nhiều broker.
* **Truyền tải dữ liệu theo thời gian thực:** Kafka cho phép truyền tải dữ liệu theo thời gian thực giữa các ứng dụng khác nhau.
* **Xử lý luồng dữ liệu:** Kafka hỗ trợ xử lý luồng dữ liệu, cho phép bạn xây dựng các ứng dụng phân tích dữ liệu lớn và các hệ thống theo dõi sự kiện.

## Quản lý Kafka Topic

vDB Kafka Cluster cung cấp cho bạn khả năng quản lý toàn diện các topic Kafka, bao gồm tạo, xóa và sửa đổi cấu hình. Dưới đây là hướng dẫn chi tiết từng bước để thực hiện các thao tác này:

**1. Chọn Cụm Kafka**

* Đăng nhập vào giao diện vDB Kafka Cluster tại đây:&#x20;
* Từ danh sách các cụm Kafka có sẵn, chọn cụm mà bạn muốn quản lý topic.

**2. Truy cập Phần "Topics"**

* Sau khi chọn cụm Kafka, tìm và điều hướng đến phần "Topics" trong giao diện quản lý. Đây là nơi bạn sẽ thực hiện các thao tác trên topic.

**3. Tạo Topic**

1. Nhấp vào nút "Tạo Topic" để điền các thông tin cần thiết.
2. Điền các thông tin sau:
   * **Tên Topic:** Đặt tên cho topic mới. Tên này nên mô tả rõ ràng nội dung của topic và không thể thay đổi sau khi khởi tạo.
   * **Số Phân vùng (Partition Count):** Xác định số phân vùng cho topic. Số phân vùng ảnh hưởng đến khả năng mở rộng và song song của topic.
   * **Hệ số Nhân bản (Replication Factor):** Xác định số lượng bản sao của mỗi phân vùng. Điều này ảnh hưởng đến khả năng chịu lỗi của topic.
   * **Retention:** Thiết lập thời gian hoặc dung lượng lưu trữ tối đa cho dữ liệu trong topic.
3. Nhấp vào nút "Tạo" để hoàn tất quá trình tạo topic.

**4. Xóa Topic**

1. Trong danh sách các topic, tìm topic bạn muốn xóa.
2. Nhấp vào biểu tượng "Xóa" tương ứng với topic đó.
3. Xác nhận thao tác xóa. Lưu ý rằng việc xóa topic là không thể hoàn tác và tất cả dữ liệu trong topic sẽ bị mất.

**5. Sửa Topic**

1. Trong danh sách các topic, tìm topic bạn muốn sửa.
2. Nhấp vào biểu tượng  "Sửa" tương ứng với topic đó.
3. Thay đổi các cấu hình topic cần thiết, ví dụ:
   * **Số Phân vùng:** Chỉ cho phép tăng số phân vùng để điều chỉnh khả năng mở rộng của topic.
   * **Retention:** Thay đổi thời gian hoặc dung lượng lưu trữ tối đa cho dữ liệu.
4. Nhấp vào nút "Lưu" để áp dụng các thay đổi.

**Lưu ý:**

* Việc thay đổi số phân vùng của một topic có thể ảnh hưởng đến hiệu suất và khả năng sẵn có của topic trong một khoảng thời gian ngắn.
* Hãy cẩn trọng khi xóa topic, vì thao tác này không thể hoàn tác và tất cả dữ liệu trong topic sẽ bị mất vĩnh viễn.

Với hướng dẫn chi tiết này, bạn có thể dễ dàng quản lý các topic Kafka trong vDB Kafka Cluster, đảm bảo hệ thống xử lý dữ liệu của bạn hoạt động hiệu quả và đáp ứng được các yêu cầu về khả năng mở rộng và độ tin cậy.
