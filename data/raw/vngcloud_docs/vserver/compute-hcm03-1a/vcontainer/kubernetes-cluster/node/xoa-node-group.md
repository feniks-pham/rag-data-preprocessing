# Xóa Node Group

Chủ đề này mô tả cách bạn có thể xóa Node Group được quản lý bởi VNG Cloud. Lưu ý rằng bạn không thể xoá Node Group Default, chỉ có thể xoá Node Group tự tạo

Trước khi kết thúc mỗi máy chủ, VNG Cloud sẽ gửi tín hiệu để rút các Pod khỏi nút đó. Nếu các Pod không hết sau vài phút, VNG Cloud cho phép Tự động thay đổi quy mô tiếp tục chấm dứt máy chủ.&#x20;

***

### **Xóa Node Group trên bảng điều khiển vServer** <a href="#xoanodegroup-xoanodegrouptrenbangdieukhienvserver" id="xoanodegroup-xoanodegrouptrenbangdieukhienvserver"></a>

**Quyền tối thiểu**

Để xóa Node Group, bạn phải có quyền IAM tối thiểu chạy hành động sau:

* DeleteClusterNodeGroups

1. Truy cập vào bảng điều khiển vServer của chúng tôi tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Chọn vào xem chi tiết Cluster bằng cách nhấn vào tên của Cluster, sau đó chọn Tab Node Group tại trang chi tiết
3. Trong phần Node Group, chọn Node Group cần xóa. Sau đó chọn **Xóa**.\
   Trong hộp thoại xác nhận Xóa Node Group, chọn **Xóa** để xác nhận

\
