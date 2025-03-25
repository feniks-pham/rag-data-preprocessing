# Xóa Snapshot

Snapshot lưu trữ bản sao dữ liệu tại một thời điểm cụ thể. Khi loại bỏ các Snapshot không còn cần, bạn giải phóng dung lượng lưu trữ, cho phép sử dụng không gian đó cho mục đích khác hoặc tiết kiệm chi phí lưu trữ. Điều này cũng giúp quản lý chi phí hiệu quả hơn trong dịch vụ điện toán đám mây, nơi bạn thường phải trả phí dựa trên dung lượng lưu trữ và thời gian sử dụng.

Tuy nhiên, việc duy trì các Snapshot không cần thiết hoặc không liên quan đến quá trình phục hồi có thể làm cho việc quản lý dữ liệu trở nên phức tạp. Xóa các Snapshot không còn cần giúp duy trì sự sạch sẽ và hiệu quả trong quản lý dữ liệu của bạn.

Hơn nữa, lưu ý rằng các Snapshot cũng có thể ảnh hưởng đến hiệu suất của hệ thống và máy chủ. Khi có quá nhiều Snapshot hoặc chúng được tạo và duy trì một cách không cân nhắc, hiệu suất tổng thể của hệ thống và hệ thống lưu trữ có thể bị ảnh hưởng. Xóa các Snapshot không cần thiết có thể cải thiện hiệu suất này.

***

### **Giới hạn** <a href="#xoasnapshot-gioihan" id="xoasnapshot-gioihan"></a>

* Khi bạn xóa Snapshot, dữ liệu chứa trong ảnh chụp nhanh sẽ bị xóa nhưng đĩa nơi tạo ảnh chụp nhanh đó không bị ảnh hưởng.
* Xóa Snapshot có nghĩa là bạn sẽ không thể khôi phục dữ liệu từ chúng trong tương lai. Đảm bảo rằng bạn có sẵn chiến lược sao lưu nếu bạn cần giữ lại dữ liệu cho mục đích tuân thủ hoặc khắc phục thảm họa.

***

**Bạn có thể thực hiện xóa Snapshot cho Server và Volume trên trình điều khiển của chúng tôi, vui lòng xem theo các hướng dẫn bên dưới:**

Lưu ý

Bạn chỉ có thể xóa Snapshot cho Volume tại trang quản lý Snapshot, để xoá Snapshot cho Server bạn cần thực hiện xóa chúng tại trang chi tiết Server.

### **Xoá Snapshot Volume tại trang danh sách Snapshot trên bảng điều khiển** <a href="#xoasnapshot-xoasnapshotvolumetaitrangdanhsachsnapshottrenbangdieukhien" id="xoasnapshot-xoasnapshotvolumetaitrangdanhsachsnapshottrenbangdieukhien"></a>

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/).
2. Trong ngăn điều hướng, chọn **Snapshot**.
3. Chọn Snapshot cần xóa rồi chọn **Hành động**, nhấn **Xóa Snapshot.**

***

### **Xoá Snapshot Volume tại trang chi tiết Volume trên bảng điều khiển** <a href="#xoasnapshot-xoasnapshotvolumetaitrangchitietvolumetrenbangdieukhien" id="xoasnapshot-xoasnapshotvolumetaitrangchitietvolumetrenbangdieukhien"></a>

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/).
2. Trong ngăn điều hướng, chọn **Volume**.
3. Nhấn vào tên Volume để vào trang chi tiết Volume
4. Chuyển sang Tab **Associated Snapshot**
5. Thực hiện chọn Snapshot Volume cần xoá và chọn **Delete**

***

### **Xoá Snapshot Server tại trang chi tiết Server trên bảng điều khiển** <a href="#xoasnapshot-xoasnapshotservertaitrangchitietservertrenbangdieukhien" id="xoasnapshot-xoasnapshotservertaitrangchitietservertrenbangdieukhien"></a>

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/).
2. Trong ngăn điều hướng, chọn Server.
3. Nhấn vào tên Server để vào trang chi tiết Server
4. Chuyển sang Tab **Associated Snapshot**
5. Thực hiện chọn Snapshot Server cần xoá và chọn **Delete.**
