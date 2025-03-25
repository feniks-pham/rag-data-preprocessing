# Vòng đời máy chủ ảo

Một Server chuyển đổi qua các trạng thái khác nhau từ thời điểm được tạo đến thời điểm kết thúc.

### **Provisioning** <a href="#vongdoimaychuao-provisioning" id="vongdoimaychuao-provisioning"></a>

Trong giai đoạn này, các cá thể được chuẩn bị để đi vào trạng thái đang chạy. Các tài nguyên máy tính được cấp phát và cấu hình ở giai đoạn này.

Trong VNG Cloud, các Server có trạng thái đang chờ xử lý, các trạng thái thể hiện như vậy được khởi chạy lần đầu tiên hoặc bắt đầu sau giai đoạn dừng.

### **Running** <a href="#vongdoimaychuao-running" id="vongdoimaychuao-running"></a>

Trong giai đoạn này, các Server đang chạy và sẵn sàng để sử dụng. Bạn có thể bắt đầu lưu trữ khối lượng công việc cho nó.

Bạn được phép lập hóa đơn cho các Server trong giai đoạn đang chạy.

### **Shutting Down** <a href="#vongdoimaychuao-shuttingdown" id="vongdoimaychuao-shuttingdown"></a>

Trong một số trường hợp, khi bạn không thể kiểm tra trạng thái Server hoặc nó không chạy như mong đợi, Server sẵn sàng để có thể bị tắt đi.

Bạn có thể bắt đầu việc tắt Server để khắc phục sự cố và khởi động lại dịch vụ này khi đã sẵn sàng.

Khi nó chuyển sang trạng thái tắt, bạn có thể sửa đổi các thuộc tính cụ thể của Server.

### **Terminated** <a href="#vongdoimaychuao-terminated" id="vongdoimaychuao-terminated"></a>

Bạn có thể xóa một Server khi bạn không còn nhu cầu sử dụng, trạng thái này được gọi là kết thúc.

Khi bạn thay đổi trạng thái Server thành tắt hoặc kết thúc. Đối với việc kết thúc Server, bạn sẽ không phải chịu các khoản phí phát sinh và dữ liệu trên các Volume đính kèm sẽ mất đi

Bạn có thể sử dụng các tình huống bảo vệ khi chấm dứt. Điều này ngăn không cho hành động chấm dứt Server xảy ra một cách vô tình.
