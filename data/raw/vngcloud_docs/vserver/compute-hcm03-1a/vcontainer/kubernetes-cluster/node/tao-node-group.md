# Tạo Node Group

Chủ đề này mô tả cách bạn có thể khởi chạy các Node Group được quản lý VNG Cloud Kubernetes Cluster gồm các Node được đăng ký với Kubernetes Cluster của bạn. Sau khi các Node tham gia Cluster, bạn có thể triển khai các ứng dụng Kubernetes cho chúng.

Cần lưu ý rằng hướng dẫn này sẽ giúp bạn tạo thêm các Node Group trên Kubernetes Cluster có sẵn đã được tạo trước đó. Khi tạo một Kubernetes Cluster bạn sẽ được tạo một Node Group Default và sau đó bạn có thể tạo thêm các Node Group tùy chỉnh cho Kubernetes Cluster của mình theo hướng dẫn bên dưới. Bạn có thể lựa chọn số lượng Node và cấu hình Node trong quá trình khởi tạo Node Group.

Lưu ý

Các Node là các phiên bản Server tiêu chuẩn. Bạn được lập hóa đơn dựa trên giá Server thông thường. Để biết thêm thông tin, hãy xem Giá của Server.

***

### **Tạo Node Group trên bảng điều khiển vServer** <a href="#taonodegroup-taonodegrouptrenbangdieukhienvserver" id="taonodegroup-taonodegrouptrenbangdieukhienvserver"></a>

**Quyền tối thiểu**

Để tạo mới Node Group, bạn phải có quyền IAM chạy các hành động sau:

* CreateClusterNodeGroups

1. Truy cập vào bảng điều khiển vServer của chúng tôi tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Sau khi tạo Cluster bạn cần đợi trạng thái của nó chuyển sang ACTIVE. Bạn không thể tạo Node Group cho một Cluster có trạng thái CREATING hay ERROR.
3. Chọn vào xem chi tiết Cluster bằng cách nhấn vào tên của Cluster, sau đó chọn Tab Node Group tại trang chi tiết
4. Chọn Tạo Node Group
5. Trên trang Cấu hình Node Group, hãy điền các tham số tương ứng rồi chọn Thêm mới, trong đó:
   * Friendly name: Nhập tên của Node Group (Chỉ cho phép các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào của bạn phải từ 5 đến 50).
   * Số lượng Node: Nhập số lượng Node bạn muốn tạo trong Node Group (Số lượng node cần lớn hơn hoặc bằng 1, và nhỏ hơn hoặc bằng 10).
   * Boot Volume: Không cho phép chọn cấu hình, tại mục này hệ thống sẽ tự động cấu hình theo cấu hình ban đầu của Cluster
   * Docker Volume: Cho phép cấu hình theo Size, type, IOPS của Volume
6. Chọn Minion Flavor tương ứng với nhu cầu sử dụng
7. Nhấn chọn **Thêm mới,** lúc giao diện sẽ trả về trang chi tiết Cluster với trạng thái **CREATING NODE GROUP** kèm một Node Group được tạo mới.
8. Bạn cần chờ đến khi Cluster trở về trạng thái ACTIVE và sử dụng Node Group vừa tạo
