# Cách thức hoạt động

Cụm Kafka (Kafka Cluster) là một hệ thống phân tán gồm nhiều máy chủ Kafka (Kafka Brokers) làm việc cùng nhau để cung cấp dịch vụ xử lý luồng sự kiện (event streaming). Dữ liệu được tổ chức thành các chủ đề (Topics), mỗi chủ đề được chia thành nhiều phân vùng (Partitions) để tăng khả năng mở rộng và chịu lỗi.

## **Các thành phần và thuật ngữ quan trọng**

1. **Kafka Broker:**
   * Là một máy chủ trong cụm Kafka, chịu trách nhiệm lưu trữ và quản lý một phần dữ liệu của các chủ đề.
   * Nhận dữ liệu từ Producers và cung cấp dữ liệu cho Consumers.
   * Duy trì trạng thái của cụm và đảm bảo tính nhất quán của dữ liệu.
2. **Kafka Storage:**
   * Là nơi lưu trữ vật lý dữ liệu của Kafka, thường là trên đĩa cứng hoặc các thiết bị lưu trữ khác.
   * Kafka sử dụng một cấu trúc lưu trữ hiệu quả để ghi và đọc dữ liệu tuần tự, giúp đạt được hiệu suất cao.
3. **Topic:**
   * Là một danh mục (category) hoặc luồng (stream) các sự kiện có liên quan.
   * Ví dụ: một ứng dụng thương mại điện tử có thể có các topic như "đơn hàng mới", "thanh toán thành công", "giao hàng hoàn tất".
4. **Partition count:**
   * Là số lượng phân vùng mà một topic được chia thành.
   * Tăng số lượng phân vùng giúp tăng khả năng mở rộng và xử lý song song, nhưng cũng làm tăng độ phức tạp của hệ thống.
5. **Replica Factor:**
   * Là số lượng bản sao của mỗi phân vùng được lưu trữ trên các broker khác nhau.
   * Tăng hệ số nhân bản giúp tăng khả năng chịu lỗi, nhưng cũng làm tăng dung lượng lưu trữ cần thiết.
6. **Produce & Consume:**
   * **Produce:** Quá trình gửi dữ liệu (sự kiện) vào một topic bởi Producers.
   * **Consume:** Quá trình đọc dữ liệu từ một topic bởi Consumers.
7. **Access method:**
   * **mTLS (Mutual TLS):** Cơ chế xác thực hai chiều, yêu cầu cả client và server phải xác thực lẫn nhau bằng chứng chỉ số. Đảm bảo tính bảo mật cao.
   * **SASL (Simple Authentication and Security Layer):** Cơ chế xác thực linh hoạt, hỗ trợ nhiều phương thức xác thực SCRAM.
8. **Encryption:**
   * **At Rest:** Mã hóa dữ liệu khi chúng được lưu trữ trên đĩa, bảo vệ dữ liệu khỏi truy cập trái phép khi máy chủ không hoạt động.
   * **In Transit:** Mã hóa dữ liệu khi chúng được truyền giữa các thành phần khác nhau (client-broker), đảm bảo tính bảo mật trong quá trình truyền tải dữ liệu.
   * **Within Cluster:** Mã hóa dữ liệu khi chúng được truyền giữa các broker trong cùng một cụm Kafka.

## **Cách thức hoạt động**

1. **Producers** gửi dữ liệu đến các **topic** cụ thể.
2. Kafka phân phối dữ liệu vào các **phân vùng** của topic theo một chiến lược phân vùng (partitioning strategy).
3. Mỗi phân vùng được **nhân bản** trên nhiều broker để đảm bảo tính chịu lỗi.
4. **Consumers** đăng ký (subscribe) vào các topic và đọc dữ liệu từ các phân vùng.
5. Kafka đảm bảo rằng mỗi consumer chỉ đọc một bản sao duy nhất của mỗi sự kiện, tránh việc xử lý trùng lặp.

**Tóm lại:**

Cụm Kafka cung cấp một nền tảng mạnh mẽ và linh hoạt để xử lý luồng sự kiện theo thời gian thực. Với khả năng mở rộng, độ bền dữ liệu và bảo mật cao, Kafka là một công cụ quan trọng trong việc xây dựng các ứng dụng dữ liệu hiện đại.
