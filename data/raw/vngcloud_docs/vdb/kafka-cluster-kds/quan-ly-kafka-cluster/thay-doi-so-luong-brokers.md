# Thay đổi số lượng Brokers

## Tại sao cần thay đổi số lượng Broker?

Trong thế giới dữ liệu không ngừng phát triển, việc điều chỉnh số lượng broker trong cụm Kafka là rất cần thiết để đáp ứng sự thay đổi về lưu lượng dữ liệu và đảm bảo hiệu suất tối ưu.

* **Scale Up (Tăng số lượng Broker):** Khi lưu lượng dữ liệu tăng cao, việc tăng số lượng broker giúp phân tán tải trên nhiều máy chủ, ngăn ngừa tình trạng quá tải trên một broker duy nhất. Điều này đảm bảo rằng hệ thống có thể xử lý lượng dữ liệu lớn hơn mà không bị giảm hiệu suất và duy trì khả năng chịu lỗi cao.
* **Scale Down (Giảm số lượng Broker):** Khi lưu lượng dữ liệu giảm, việc giảm số lượng broker giúp tiết kiệm tài nguyên và chi phí vận hành. Bằng cách loại bỏ các broker không cần thiết, bạn có thể tối ưu hóa việc sử dụng tài nguyên mà không ảnh hưởng đến hiệu suất của hệ thống.

**Cơ chế Re-balance Topic**

Khi bạn thay đổi số lượng broker, Kafka cần phân phối lại các phân vùng (partition) của các topic trên các broker mới để đảm bảo cân bằng tải và khả năng chịu lỗi. Quá trình này được gọi là re-balance.

* **Tự động Re-balance:** vDB Kafka Cluster cung cấp tùy chọn tự động re-balance topic sau khi thay đổi số lượng broker. Điều này giúp đơn giản hóa quá trình và đảm bảo rằng dữ liệu được phân phối đều trên các broker.
* **Cân nhắc khi Re-balance:** Quá trình re-balance có thể ảnh hưởng tạm thời đến hiệu suất của cụm Kafka, vì dữ liệu cần được di chuyển giữa các broker. Hãy cân nhắc thời điểm thực hiện re-balance để giảm thiểu ảnh hưởng đến ứng dụng của bạn.

## Hướng dẫn Thay đổi Số lượng Broker

1. **Chọn Cụm Kafka:** Đăng nhập vào vDB Kafka Cluster tại đây và chọn cụm Kafka mà bạn muốn điều chỉnh.
2. **Thay đổi Số lượng Broker:**
   * Tìm và truy cập vào phần quản lý cụm Kafka.
   * Chọn tùy chọn "Edit number of broker" để tăng hoặc giảm số lượng broker.
   * Nhập số lượng broker mới mong muốn.
   * Chọn "Tự động Re-balance Topic" nếu bạn muốn hệ thống tự động phân phối lại các phân vùng sau khi thay đổi.
3. **Xác nhận Thay đổi:** Xem lại các thay đổi về sồ lượng broker cũng như chi phí chênh lệch và nhấp vào nút "Xác nhận" để bắt đầu quá trình.
4. **Theo dõi Tiến trình:** Hệ thống sẽ tự động thêm hoặc xóa broker và thực hiện re-balance topic nếu bạn đã chọn tùy chọn này. Bạn có thể theo dõi tiến trình thông qua giao diện quản lý.
