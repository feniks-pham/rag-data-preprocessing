# Sao chép định kỳ và Recovery Point

Sau khi bạn nhấn **"Start Replication"** và quá trình sao chép ban đầu (Full Replication) hoàn tất, hệ thống sẽ tự động tiến hành sao chép định kỳ theo lịch trình.&#x20;

Mặc định, **cứ mỗi 15 phút**, hệ thống sẽ tạo ra một **Recovery Point** mới, ghi lại trạng thái dữ liệu của máy chủ chính tại thời điểm đó. Điều này đảm bảo rằng dữ liệu của bạn được bảo vệ thường xuyên và bạn có thể khôi phục về một thời điểm gần nhất có thể trong trường hợp xảy ra sự cố.

Tuy nhiên, để tiết kiệm chi phí lưu trữ, không phải tất cả các Recovery Point đều được giữ lại. Chỉ những Recovery Point trùng với **Interval Time** (khoảng thời gian giữa hai điểm khôi phục) mà bạn đã thiết lập tại bước **Start Replication** mới được lưu giữ. Các Recovery Point khác sẽ bị xóa đi sau khi một Recovery Point mới được tạo ra.

**Ví dụ cụ thể:**

Giả sử bạn đã thiết lập Interval Time là 4 giờ. Điều này có nghĩa là hệ thống sẽ chỉ giữ lại các Recovery Point được tạo ra vào các thời điểm: 0:00, 4:00, 8:00, 12:00, 16:00 và 20:00 mỗi ngày.

* Nếu một Recovery Point được tạo ra lúc 3:45, nó sẽ bị xóa đi khi Recovery Point tiếp theo được tạo ra lúc 4:00.
* Nếu một Recovery Point được tạo ra lúc 4:00, nó sẽ được giữ lại vì trùng với Interval Time.
* Các Recovery Point được tạo ra lúc 0:15, 0:30, 0:45,... cũng sẽ bị xóa đi tương tự.

**Tóm lại:**

* Sao chép định kỳ diễn ra mỗi 15 phút, tạo ra các Recovery Point mới.
* Chỉ các Recovery Point trùng với Interval Time mới được lưu giữ.
* Các Recovery Point khác sẽ bị xóa để tiết kiệm chi phí lưu trữ.

**Lợi ích:**

* Đảm bảo dữ liệu luôn được cập nhật và bảo vệ.
* Tiết kiệm chi phí lưu trữ bằng cách chỉ giữ lại các Recovery Point cần thiết.
* Cho phép bạn khôi phục dữ liệu về một thời điểm cụ thể trước khi xảy ra sự cố.
