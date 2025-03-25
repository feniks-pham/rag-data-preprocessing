# Floating IP

Địa chỉ Floating IP (FIP) là địa chỉ IP công cộng mà bạn có thể đặt trước và sử dụng như một tài nguyên độc lập. FIP có thể được giữ lại một cách độc lập và liên kết với hoặc tách rời khỏi giao diện chính của các phiên bản trong đám mây riêng ảo (VPC).

### **Tổng quan** <a href="#floatingip-tongquan" id="floatingip-tongquan"></a>

FIP là địa chỉ IP NAT nằm trong cổng của VNG Cloud. Bằng NAT, các FIP được ánh xạ tới các giao diện mạng chính của các cá thể vServer. Bạn có thể kết hợp FIP với các phiên bản vServer nằm trong VPC để cho phép các Server này giao tiếp qua Internet. FIP là vô hình bên trong hệ điều hành của các phiên bản vServer.

### **Hạn mức** <a href="#floatingip-hanmuc" id="floatingip-hanmuc"></a>

FIP có thể được liên kết với các cá thể vServer. Một FIP ​​chỉ có thể được liên kết với một phiên bản vServer đáp ứng các yêu cầu sau:

* Phiên bản vServer nằm trong VPC.
* Thể hiện vServer nằm trong cùng vùng với FIP.
* Thể hiện vServer ở trạng thái Đang chạy hoặc Đã dừng.
* Không có giao diện bên ngoài nào được đính kèm.

***

### **Làm việc với Floating IP** <a href="#floatingip-lamviecvoifloatingip" id="floatingip-lamviecvoifloatingip"></a>

#### **Tạo Floating IP:** <a href="#floatingip-taofloatingip" id="floatingip-taofloatingip"></a>

Floating IP được tạo kèm khi khởi tạo Server, tuy nhiên bạn có thể xem danh sách các Floating IP được đính kèm với Server tại bảng điều khiển vServer tại đường link: [https://hcm-3.console.vngcloud.vn/vserver/network/wan-ip](https://hcm-3.console.vngcloud.vn/vserver/network/wan-ip)

#### **Liên kết Floating IP ​​với một phiên bản vServer:** <a href="#floatingip-lienketfloatingip-voimotphienbanvserver" id="floatingip-lienketfloatingip-voimotphienbanvserver"></a>

* Bạn có thể đăng nhập vào [Trang Server ](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)và liên kết FIP ​​với một phiên bản vServer nằm trong VPC và không được đính kèm Giao diện bên ngoài.
* Bạn cũng có thể truy cập [Trang Floating IP](https://hcm-3.console.vngcloud.vn/vserver/network/wan-ip) và liên kết FIP ​​với một phiên bản vServer nằm trong VPC và không được đính kèm Giao diện bên ngoài.

#### **Tách một Floating IP ​​khỏi một phiên bản vServer** <a href="#floatingip-tachmotfloatingip-khoimotphienbanvserver" id="floatingip-tachmotfloatingip-khoimotphienbanvserver"></a>

* Nếu bản sao vServer của bạn không cần FIP nữa, bạn có thể tách FIP khỏi bản sao trong [Trang Server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server).
* Bạn cũng có thể tách FIP khỏi phiên bản vServer trên [Trang Floating IP](https://hcm-3.console.vngcloud.vn/vserver/network/wan-ip).



\
