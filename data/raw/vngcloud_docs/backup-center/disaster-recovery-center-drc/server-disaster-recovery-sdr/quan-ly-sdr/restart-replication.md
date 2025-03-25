# Restart Replication

Trong một số trường hợp, quá trình sao chép dữ liệu từ máy chủ chính sang máy chủ dự phòng có thể gặp lỗi hoặc bạn muốn bắt đầu lại quá trình sao chép từ đầu để đảm bảo tính đồng bộ và toàn vẹn của dữ liệu. Tính năng Restart Replication cho phép bạn thực hiện điều này một cách dễ dàng.

**Khi nào nên sử dụng Restart Replication:**

* **Quá trình sao chép gặp lỗi:** Nếu quá trình sao chép bị gián đoạn do lỗi kỹ thuật, mạng hoặc các vấn đề khác, bạn có thể khởi động lại sao chép để hệ thống tự động khắc phục và tiếp tục quá trình sao chép.
* **Cần đồng bộ lại dữ liệu:** Nếu bạn nghi ngờ có sự không đồng bộ giữa dữ liệu trên máy chủ chính và máy chủ dự phòng, bạn có thể khởi động lại sao chép để đảm bảo dữ liệu được đồng bộ hoàn toàn.
* **Thay đổi cấu hình:** Nếu bạn đã thay đổi cấu hình của máy chủ chính (ví dụ: thêm hoặc xóa ổ đĩa), bạn có thể khởi động lại sao chép để đảm bảo máy chủ dự phòng cũng được cập nhật cấu hình tương ứng.

## Khởi động lại (Restart Replication)

**Bước 1: Truy cập trang chủ Server Disaster Recovery tại đây:**

**Bước 2: Chọn máy chủ**

* Trong danh sách các máy chủ đã được bảo vệ (Servers Disaster Recovery), xác định máy chủ bạn muốn tạm dừng sao chép.
* Nhấp vào **DR Pair ID** tương ứng với máy chủ đó để xem thông tin chi tiết.

**Bước 3: Khởi động lại sao chép**

* Trong giao diện chi tiết của máy chủ, tìm và nhấp vào nút **"Restart Replication"**.
* Từ menu xổ xuống, chọn **"Restart Replication"**.

**Bước 4: Xác nhận**

* Một cửa sổ bật lên sẽ xuất hiện để xác nhận hành động của bạn và cảnh báo rằng tất cả các điểm khôi phục (Recovery Point) đã tạo trước đó sẽ bị xóa.
* Nhấn nút **"Restart Replication"** để bắt đầu quá trình khởi động lại sao chép.
* Trạng thái của máy chủ sẽ chuyển sang **"Start Replication"** trong khi hệ thống đang xử lý yêu cầu của bạn. Sau đó, trạng thái sẽ chuyển sang **"Replicating"** khi quá trình sao chép mới đã bắt đầu.

**Lưu ý quan trọng**

* **Xóa bỏ Recovery Point:** Khi bạn khởi động lại sao chép, tất cả các điểm khôi phục đã tạo trước đó sẽ bị xóa vĩnh viễn. Hãy cân nhắc kỹ trước khi thực hiện hành động này, đặc biệt là nếu bạn cần khôi phục dữ liệu về một thời điểm cụ thể trong quá khứ.
* **Thời gian sao chép:** Quá trình sao chép lại toàn bộ dữ liệu có thể mất một khoảng thời gian đáng kể, tùy thuộc vào dung lượng dữ liệu của máy chủ chính. Trong thời gian này, máy chủ dự phòng sẽ chưa sẵn sàng để chuyển đổi dự phòng.

**Tóm tắt:**

Tính năng Restart Replication cho phép bạn bắt đầu lại quá trình sao chép dữ liệu từ đầu, hữu ích trong các trường hợp quá trình sao chép gặp lỗi hoặc bạn cần đồng bộ lại dữ liệu. Hãy sử dụng tính năng này một cách cẩn thận và lưu ý về việc xóa bỏ các điểm khôi phục đã tạo trước đó.
