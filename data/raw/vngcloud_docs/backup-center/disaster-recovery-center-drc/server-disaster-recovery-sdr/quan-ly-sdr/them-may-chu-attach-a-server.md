# Thêm máy chủ (Attach a Server)

Làm theo các hướng dẫn bên dưới để thêm một máy chủ chính vò Server Disaster Recovery.

1. Trong bảng điều khiển Server Disaster Recovery Center, nhấp vào nút **"Attach a Server"** ở góc trên bên trái.
2. Một cửa sổ bật lên sẽ xuất hiện, yêu cầu bạn cung cấp thông tin cấu hình cho máy chủ chính và máy chủ dự phòng.
   * **Region (Vùng):** Chọn vùng địa lý nơi máy chủ chính của bạn đang hoạt động (ví dụ: HCM-03).
   * Nhấn **chọn máy chủ chính** cần thêm vào Server Disaster Recovery
   * **Shadow Server Configuration (Cấu hình Máy chủ Dự phòng):**
     * **Region:** Chọn vùng địa lý nơi bạn muốn đặt máy chủ dự phòng.
     * **VPC (Virtual Private Cloud):** Chọn VPC mà bạn muốn máy chủ dự phòng thuộc về.
     * **Subnet:** Chọn subnet cụ thể trong VPC đã chọn để đặt máy chủ dự phòng.
   * **Chọn nhiều máy chủ (Multiple Main Servers):**
     * Nếu bạn muốn thêm nhiều máy chủ chính cùng lúc, hãy đánh dấu vào các ô vuông bên cạnh tên máy chủ.
     * Bạn cũng có thể chọn tất cả các máy chủ cùng một lúc bằng cách đánh dấu vào ô vuông ở đầu danh sách.
3. **Xác nhận:** Sau khi đã cung cấp đầy đủ thông tin, nhấn nút **"Attach"** để hoàn tất quá trình thêm máy chủ.

* Nếu quá trình thêm máy chủ thành công, bạn sẽ nhận được thông báo **"Attach Server Successful"** và hệ thống sẽ tự động chuyển hướng về bảng điều khiển Server Disaster Recovery.

**Lưu ý:**

* Máy chủ chính đã hết hạn vẫn được hiển thị nhưng không thể chọn để thêm vào DRC. Bạn cần gia hạn máy chủ trước khi thêm vào SDR.
* Máy chủ dự phòng (Shadow Server) đang trong quá trình ghép cặp hoặc chưa xác nhận trạng thái chuyển đổi dự phòng cũng không thể được chọn.
* Máy chủ chính có các ổ đĩa với cài đặt "multi-attach" (cho phép gắn vào nhiều máy chủ cùng lúc) không thể được thêm vào SDR.
