# Nâng cấp Storage

## Tại sao cần tăng dung lượng lưu trữ Broker?

Kafka được thiết kế để lưu trữ một lượng lớn dữ liệu theo thời gian. Khi dữ liệu tích lũy ngày càng nhiều, việc tăng dung lượng lưu trữ cho các broker trong cụm Kafka trở nên cần thiết để đảm bảo hệ thống hoạt động ổn định và tránh tình trạng đầy đĩa.

* **Tránh mất dữ liệu:** Khi dung lượng lưu trữ của broker đầy, Kafka sẽ không cho phép ghi mới. Việc tăng dung lượng lưu trữ giúp bạn tránh mất dữ liệu quan trọng và đảm bảo rằng bạn có thể truy cập vào dữ liệu lịch sử khi cần.
* **Duy trì hiệu suất:**&#x20;
  * Khi broker gần đầy, hiệu suất đọc và ghi dữ liệu có thể bị ảnh hưởng.&#x20;
  * Do đó, vDB Kafka Cluster sẽ alert (qua mail) đến quý khách hàng khi dung lượng lưu trữ trên broker vượt ngưỡng cho phép (80%).&#x20;
  * Quý khách hàng cần chủ động tăng dung lượng lưu trữ giúp duy trì hiệu suất tối ưu của cụm Kafka, theo dõi các mail alert, cảnh báo từ dịch vụ của chúng tôi để đưa ra quyết định nhanh chóng.

**Hướng dẫn Tăng Dung lượng Lưu trữ Broker**

1. **Chọn Cụm Kafka:** Đăng nhập vào vDB Kafka Cluster và chọn cụm Kafka mà bạn muốn điều chỉnh.
2. **Tăng Kích thước Đĩa Lưu trữ:**
   * Tìm và truy cập vào phần quản lý cụm Kafka.
   * Tìm tùy chọn "Scale Up Broker Storage" hoặc tương tự.
   * Chọn kích thước đĩa mới lớn hơn kích thước hiện tại.
3. **Xác nhận Thay đổi:** Xem lại các thay đổi và nhấp vào nút "Xác nhận" hoặc tương tự để bắt đầu quá trình.
4. **Theo dõi Tiến trình:** Hệ thống sẽ tự động mở rộng dung lượng lưu trữ cho các broker. Bạn có thể theo dõi tiến trình thông qua giao diện quản lý.

**Lưu ý quan trọng:**

* Thời gian cần thiết để mở rộng dung lượng lưu trữ có thể khác nhau tùy thuộc vào nhà cung cấp dịch vụ và kích thước đĩa mới.
* Trong quá trình mở rộng dung lượng lưu trữ, cụm Kafka vẫn có thể hoạt động bình thường, nhưng hiệu suất có thể bị ảnh hưởng tạm thời.
* Hãy lên kế hoạch mở rộng dung lượng lưu trữ trước khi broker của bạn gần đầy để tránh mất dữ liệu và giảm hiệu suất.

**Kết luận**

Việc tăng dung lượng lưu trữ cho các broker trong cụm Kafka là một phần quan trọng của việc quản lý và bảo trì hệ thống Kafka. Bằng cách thực hiện các bước đơn giản trên, bạn có thể đảm bảo rằng cụm Kafka của bạn có đủ không gian lưu trữ để xử lý lượng dữ liệu ngày càng tăng và hoạt động ổn định trong thời gian dài.
