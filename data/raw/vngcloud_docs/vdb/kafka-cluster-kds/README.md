# Kafka Cluster (KDS)

Kafka Cluster DB là một dịch vụ mới trên nền tảng vDB, cung cấp một cụm máy chủ Kafka mạnh mẽ và linh hoạt để quản lý luồng sự kiện theo thời gian thực. Với Kafka Cluster DB, bạn có thể dễ dàng xây dựng các ứng dụng xử lý dữ liệu lớn, hệ thống nhắn tin và ghi log tập trung với khả năng mở rộng cao, độ bền dữ liệu và hiệu suất vượt trội.

## Tính năng <a href="#tinh-nang-moi" id="tinh-nang-moi"></a>

**Quản lý cụm Kafka toàn diện**

* **Tạo cụm:** Dễ dàng khởi tạo cụm Kafka với các tùy chọn cấu hình linh hoạt.
* **Điều chỉnh số lượng broker:** Tăng hoặc giảm số lượng broker để đáp ứng nhu cầu xử lý dữ liệu.
* **Mở rộng lưu trữ:** Tăng dung lượng lưu trữ cho các broker khi cần thiết.
* **Chỉnh sửa cấu hình:** Tùy chỉnh các tham số Kafka để tối ưu hóa hiệu suất và độ tin cậy.
* **Version**: Hỗ trợ các version 3.6, 3.6.1, 3.7

**Bảo mật và kiểm soát truy cập**

* **Phương thức truy cập đa dạng:** Hỗ trợ mTLS, SASL và Public Accessibility.
* **Quản lý người dùng:** Tạo, phân quyền và xóa người dùng Kafka.
* **Quản lý topic:** Tạo, xóa, sửa đổi cấu hình topic.
* **Cập nhật certificate:** Tạo mới chứng chỉ trong trường hợp chứng chỉ cũ hết hạn hoặc không thể truy cập.
* **Hỗ trợ các tính năng encrypt dữ liệu**: Encryption at rest (volume), Encryption within cluster (brokers to brokers), Encryption in transit (clients to brokers)

## Lợi ích <a href="#loi-ich-chinh" id="loi-ich-chinh"></a>

* **Hiệu suất cao:** Xử lý luồng sự kiện lớn với độ trễ thấp.
* **Khả năng mở rộng:** Dễ dàng mở rộng cụm để đáp ứng nhu cầu tăng trưởng.
* **Độ bền dữ liệu:** Đảm bảo tính toàn vẹn và khả năng phục hồi dữ liệu.
* **Bảo mật:** Cơ chế xác thực linh hoạt và kiểm soát truy cập chi tiết.
* **Dễ sử dụng:** Giao diện quản lý trực quan và dễ sử dụng.

So sánh Kafka Cluster DB Managed Service (dịch vụ được quản lý) và Kafka Cluster truyền thống (tự quản lý)

| **Tiêu chí**                | **Kafka Cluster DB Managed Service**                                                                                 | **Kafka Cluster Truyền Thống**                                                                     |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Quản lý cụm**             | Nhà cung cấp dịch vụ (VNG Cloud vDB) chịu trách nhiệm quản lý, bảo trì, nâng cấp và giám sát cụm Kafka.              | Người dùng tự quản lý toàn bộ cụm Kafka, bao gồm cài đặt, cấu hình, bảo trì, nâng cấp và giám sát. |
| **Cấu hình và triển khai**  | Dễ dàng cấu hình và triển khai thông qua giao diện web hoặc API.                                                     | Yêu cầu kiến thức chuyên sâu về Kafka và kỹ năng quản trị hệ thống để cài đặt và cấu hình.         |
| **Mở rộng**                 | Dễ dàng mở rộng bằng cách thêm tài nguyên thông qua giao diện quản lý.                                               | Yêu cầu quy trình mở rộng thủ công, có thể phức tạp và tốn thời gian.                              |
| **Giám sát và xử lý sự cố** | Nhà cung cấp dịch vụ (VNG Cloud vDB) cung cấp công cụ giám sát và hỗ trợ xử lý sự cố.                                | Bạn tự giám sát và xử lý sự cố, đòi hỏi kiến thức chuyên môn và kinh nghiệm.                       |
| **Chi phí**                 | Thường có chi phí thấp hơn về lâu dài do tiết kiệm được chi phí đầu tư hạ tầng, chi phí vận hành và chi phí nhân sự. | Chi phí về lâu dài sẽ cao hơn do cần đầu tư vào hạ tầng, vận hành và nhân sự.                      |
| **Tính linh hoạt**          | Có thể bị giới hạn về khả năng tùy chỉnh và kiểm soát so với cụm tự quản lý.                                         | Cho phép tùy chỉnh và kiểm soát hoàn toàn cụm Kafka.                                               |
| **Phù hợp với**             | Doanh nghiệp muốn tập trung vào phát triển ứng dụng, không muốn đầu tư nhiều vào quản lý hạ tầng.                    | Doanh nghiệp có đội ngũ kỹ thuật mạnh, muốn kiểm soát hoàn toàn hệ thống và có thể tự xử lý sự cố. |

&#x20;
