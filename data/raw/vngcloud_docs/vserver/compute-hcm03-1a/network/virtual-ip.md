# Virtual IP

### **Các trường hợp sử dụng Virtual IP** <a href="#virtualip-cactruonghopsudungvirtualip" id="virtualip-cactruonghopsudungvirtualip"></a>

Cấu hình thêm Virtual IP cho máy chủ ảo thường hữu dụng trong các trường hợp như:

* Thêm địa chỉ phụ để dùng cho 1 số trường hợp như LVS, sub interface…
* Tự xây dựng giải pháp Load Balance, HA với chi phí thấp.

### **Tổng quát về Virtual IP** <a href="#virtualip-tongquatvevirtualip" id="virtualip-tongquatvevirtualip"></a>

Một Virtual IP được dùng chung bởi nhiều máy chủ ảo. Một máy chủ ảo có thể có cả IP private và Virtual IP, bạn có thể truy cập đến máy chủ ảo bằng cả 2 IP trên. Virtual IP có đầy đủ chức năng tương tự IP private của máy chủ.

Bạn có thể gán Virtual IP cho các máy chủ ảo trong cùng hệ thống của mô hình active/standby. Virtual IP thường được dùng kết hợp với Keepalived để đảm bảo tính sẵn sàng cao. Nếu máy chủ chính gặp lỗi, máy chủ dự phòng sẽ tự động chạy tiếp dịch vụ. Virtual IP thường dùng để cấu hình HA hoặc cân bằng tải cho hệ thống.

### **Làm việc với Virtual IP** <a href="#virtualip-lamviecvoivirtualip" id="virtualip-lamviecvoivirtualip"></a>

#### Tạo Virtual IP <a href="#virtualip-taovirtualip" id="virtualip-taovirtualip"></a>

1. Vào VNG Cloud portal console, đến trang Virtual IP
2. Chọn VPC và subnet cho Virtual IP cần tạo, chỉ những máy chủ có cùng subnet với Virtual IP mới có thể được gán sử dụng virtual IP
3. Sau khi tạo bạn sẽ có thông tin của Virtual IP
4. Bạn có thể gán Virtual IP vào các máy chủ ảo bằng cách vào **Detail** của Virtual IP cần gán, chuyển qua mục **Address Pair Interface**, chọn **Add Address Pair Interface** để thực hiện thêm máy chủ ảo mà bạn muốn gán.

#### Gán/ Xóa Virtual IP cho Instance <a href="#virtualip-gan-xoavirtualipchoinstance" id="virtualip-gan-xoavirtualipchoinstance"></a>

Sau khi tạo Virtual IP, bạn cần gán nó vào máy chủ ảo để sử dụng:

1. Vào VNG Cloud portal console, đến trang Virtual IP
2. Xem chi tiết của Virtual IP và chuyển qua mục **Address Pair Interface,** chọn **Add Address Pair Interface/Remove Address Pair Interface** và chọn máy chủ ảo mà bạn muốn gán hay xóa
3. Bạn sẽ cần cấu hình network trong máy chủ ảo để có thể sử dụng đc Virtual IP

#### Xóa Virtual IP <a href="#virtualip-xoavirtualip" id="virtualip-xoavirtualip"></a>

1. Vào VNG Cloud portal console, đến trang Virtual IP
2. Chọn Virtual IP cần xóa và nhấn **Delete** ở phía bên phải
