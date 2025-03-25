# Stop & Resume Replication

Trong quá trình sử dụng dịch vụ Server Disaster Recovery (SDR), có thể có những thời điểm bạn cần tạm dừng quá trình sao chép dữ liệu từ máy chủ chính sang máy chủ dự phòng. Tính năng Stop Replication & Resume Replication cung cấp cho bạn sự linh hoạt trong việc quản lý sao chép, giúp bạn:

* **Tiết kiệm chi phí:** Trong một số trường hợp, bạn có thể muốn tạm dừng sao chép để tiết kiệm chi phí lưu trữ snapshot, đặc biệt là khi máy chủ chính không có nhiều thay đổi dữ liệu.
* **Thực hiện bảo trì:** Khi cần bảo trì máy chủ chính, bạn có thể tạm dừng sao chép để tránh xung đột dữ liệu và đảm bảo tính toàn vẹn của quá trình bảo trì.
* **Kiểm soát quá trình sao chép:** Bạn có thể chủ động tạm dừng và tiếp tục sao chép bất cứ lúc nào, tùy theo nhu cầu và tình hình thực tế.

## **Tạm dừng Sao chép (Stop Replication)**

**Bước 1: Truy cập trang chủ Server Disaster Recovery tại đây:**

**Bước 2: Chọn máy chủ**

* Trong danh sách các máy chủ đã được bảo vệ (Servers Disaster Recovery), xác định máy chủ bạn muốn tạm dừng sao chép.
* Nhấp vào **DR Pair ID** tương ứng với máy chủ đó để xem thông tin chi tiết.

**Bước 3: Tạm dừng sao chép**

* Trong giao diện chi tiết của máy chủ, tìm và nhấp vào nút **"Stop Replication"**.

**Bước 4: Xác nhận**

* Một cửa sổ bật lên sẽ xuất hiện để xác nhận hành động của bạn.
* Nhấn nút **"Stop Replication"** để tạm dừng quá trình sao chép.
* Trạng thái của pairing sẽ chuyển sang **"Pending"** trong khi tạm thời tạm dừng Replication

## **Tiếp tục Sao chép (Resume Replication)**

**Bước 1: Truy cập trang chủ Server Disaster Recovery tại đây:**

**Bước 2: Chọn máy chủ**

* Trong danh sách các máy chủ đã được bảo vệ (Servers Disaster Recovery), xác định máy chủ bạn muốn tạm dừng sao chép.
* Nhấp vào **DR Pair ID** tương ứng với máy chủ đó để xem thông tin chi tiết.

**Bước 3: Tiếp tục sao chép**

* Trong giao diện chi tiết của máy chủ, tìm và nhấp vào nút **"Actions"**.
* Từ menu xổ xuống, chọn **"Resume Replication"**.

**Bước 4: Xác nhận**

* Một cửa sổ bật lên sẽ xuất hiện để xác nhận hành động của bạn.
* Nhấn nút **"Resume Replication"** để tiếp tục quá trình sao chép.
* Trạng thái của máy chủ sẽ chuyển sang **"Replicating"** khi quá trình sao chép đã được tiếp tục.

**Lưu ý:**

* Bạn chỉ có thể tạm dừng và tiếp tục sao chép khi máy chủ đang ở trạng thái **"Replicating"**.
* Khi tạm dừng sao chép, các điểm khôi phục (Recovery Point) đã tạo trước đó vẫn được giữ nguyên.
* Khi tiếp tục sao chép, hệ thống sẽ tiếp tục tạo ra các điểm khôi phục mới theo lịch trình đã định sẵn.

Với tính năng Stop Replication & Resume Replication, bạn có thể linh hoạt quản lý quá trình sao chép dữ liệu, tối ưu hóa chi phí và đảm bảo tính toàn vẹn của hệ thống trong quá trình bảo trì.
