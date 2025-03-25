# Test Failover

Tính năng Test Failover cho phép bạn mô phỏng quá trình chuyển đổi sang máy chủ dự phòng (Shadow Server) để kiểm tra kế hoạch DR và đảm bảo hệ thống sẵn sàng hoạt động khi cần thiết, mà không ảnh hưởng đến hoạt động của máy chủ chính.

1. **Truy cập trang chủ Server Disaster Recovery tại đây:**&#x20;
2. **Chọn máy chủ cần kiểm tra**
   1. Trong danh sách các máy chủ đã được bảo vệ (Servers DR), xác định máy chủ bạn muốn thực hiện kiểm tra chuyển đổi dự phòng.
   2. Nhấp vào **DR Pair ID** tương ứng với máy chủ đó để xem thông tin chi tiết.
3. **Bắt đầu Test Failover**: Trong giao diện chi tiết của máy chủ, tìm và nhấp vào nút **"Test Failover"**.
4. **Cấu hình thông tin Test Failover Server**

Một cửa sổ bật lên sẽ xuất hiện, yêu cầu bạn cung cấp các thông tin cần thiết cho quá trình kiểm tra chuyển đổi dự phòng:

* **Failover Server Name:** Đặt tên cho máy chủ chuyển đổi dự phòng tạm thời (từ 5-50 ký tự, chỉ chứa chữ cái, số, dấu gạch dưới và dấu gạch ngang).
* **Region:** Vùng địa lý nơi bạn muốn tạo máy chủ chuyển đổi dự phòng tạm thời (mặc định là vùng của Shadow Server).
* **Recovery Point:** Chọn điểm thời gian bạn muốn khôi phục dữ liệu (thời điểm hiện tại hoặc một điểm khôi phục trước đó).
* **Network Settings:**
  * **VPC:** Chọn VPC mà bạn muốn máy chủ chuyển đổi dự phòng tạm thời thuộc về.
  * **Subnet:** Chọn subnet cụ thể trong VPC đã chọn.
  * **IP:** (Tùy chọn) Nhập địa chỉ IP bạn muốn gán cho máy chủ chuyển đổi dự phòng tạm thời. Nếu để trống, hệ thống sẽ tự động cấp phát một địa chỉ IP.
  * **Floating Setting:** Đánh dấu nếu bạn muốn gán một Floating IP cho máy chủ chuyển đổi dự phòng tạm thời để truy cập từ Internet.
* **Volume Settings:**
  * **Test Server volume type:** Chọn loại ổ đĩa cho máy chủ chuyển đổi dự phòng tạm thời (SSD hoặc NVMe).
  * **Test Server Volume IOPS:** Chọn mức IOPS cho máy chủ chuyển đổi dự phòng tạm thời.
* **Instance Type:**
  * **Instance Family:** Chọn họ máy chủ (ví dụ: General Purpose, Compute Optimized, Memory Optimized).

5. **Bắt đầu kiểm tra**

* Sau khi đã cấu hình xong, nhấn nút **"Test Failover"** để bắt đầu quá trình kiểm tra.
* Trạng thái của pairing ở cột **In Testing Failover** sẽ chuyển sang **"Processing"** trong khi hệ thống đang xử lý yêu cầu của bạn.

6. **Thay đổi Recovery Point (tùy chọn)**

* Trong quá trình kiểm tra, nếu bạn muốn thử nghiệm khả năng khôi phục tại một thời điểm khác, bạn có thể thay đổi Recovery Point.
* Tại trang chi tiết pairing, tìm và nhấn nút **"Change Recovery Point".**
* Một cửa sổ giao diện sẽ hiển thị cho phép bạn chọn điểm khôi phục mong muốn từ danh sách các điểm khôi phục khả dụng.
* Nhấn nút **"Change Recovery Point"** để áp dụng thay đổi.

7. **Dọn dẹp môi trường kiểm tra**

* Sau khi hoàn tất kiểm tra, tìm và chọn **"Clean Test Environment"** để xóa các tài nguyên tạm thời đã tạo ra trong quá trình Test Failover để tránh phát sinh chi phí.
* Trạng thái của pairing ở cột **In Testing Failover** sẽ chuyển sang rỗng.

**Lưu ý:**

* Quá trình sao chép dữ liệu vẫn diễn ra bình thường trong khi bạn đang thực hiện kiểm tra chuyển đổi dự phòng.
* Hãy thường xuyên thực hiện Test Failover để đảm bảo hệ thống DR của bạn luôn sẵn sàng hoạt động khi cần thiết.
