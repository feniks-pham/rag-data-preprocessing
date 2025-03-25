# Tạo Snapshot

Dịch vụ Snapshot dựa trên đám mây do VNG Cloud cung cấp là dịch vụ sao lưu dữ liệu hoạt động liền mạch, cho phép bạn tạo các Snapshot phù hợp cho đĩa hệ thống hoặc đĩa dữ liệu ngay tức thời mà không cần các tác nhân nào khác. Những snapshot này có thể được sử dụng để sao lưu dữ liệu, khôi phục lại dữ liệu khi xảy ra sự cố không mong muốn. Trước khi khôi phục ổ đĩa, sửa đổi các tệp hệ thống quan trọng hoặc thay đổi hệ điều hành của một server, bạn có thể tạo snapshot của ổ đĩa để nâng cao khả năng chịu lỗi.

Bạn có khả năng tạo snapshot theo thời điểm của ổ đĩa, đóng vai trò là điểm cơ bản để tạo ổ đĩa mới hoặc bảo mật dữ liệu của bạn thông qua các bản sao lưu. Trong trường hợp bạn thiết lập các snapshot định kỳ cho một ổ đĩa cụ thể, các snapshot này sẽ hoạt động tăng dần, nghĩa là mỗi snapshot mới chỉ ghi lại các khối dữ liệu đã thay đổi kể từ khi snapshot trước đó được chụp.

Quá trình chụp ảnh nhanh hoạt động không đồng bộ. Mặc dù snapshot tại thời điểm được bắt đầu ngay lập tức nhưng trạng thái của nó vẫn đang chờ xử lý cho đến khi toàn bộ quá trình chụp ảnh nhanh được hoàn tất. Việc hoàn thành quá trình này đòi hỏi phải chuyển tất cả các khối dữ liệu đã sửa đổi sang ổ đĩa gốc. Đối với những snapshot ban đầu quan trọng hoặc những snapshot tiếp theo có những thay đổi đáng kể, thao tác này có thể tiêu tốn vài giờ. Điều quan trọng là trong khoảng thời gian hoạt động này, snapshot đang thực hiện vẫn không bị ảnh hưởng bởi các hoạt động đọc và ghi đang diễn ra trên ổ đĩa.

***

### **Điều kiện tiên quyết** <a href="#taosnapshot-dieukientienquyet" id="taosnapshot-dieukientienquyet"></a>

* Snapshot phải được được kích hoạt. Để biết thêm thông tin, hãy xem [Kích hoạt Snapshot](kich-hoat-snapshot.md).
* Đĩa mà bạn muốn tạo ảnh chụp nhanh đang ở trạng thái Đang sử dụng hoặc Chưa đính kèm. Hãy lưu ý các mục sau:
  * Nếu đĩa ở trạng thái Đang sử dụng, hãy đảm bảo rằng phiên bản mà đĩa được gắn vào ở trạng thái Đang chạy hoặc Đã dừng.
  * Nếu đĩa ở trạng thái Chưa được đính kèm, hãy đảm bảo rằng đĩa đã được gắn vào một Server tại một thời điểm nào đó. Không thể tạo snapshot cho các ổ đĩa đám mây chưa từng được gắn vào Server.

***

### **Tạo Snapshot cho Volume trên bảng điều khiển** <a href="#taosnapshot-taosnapshotchovolumetrenbangdieukhien" id="taosnapshot-taosnapshotchovolumetrenbangdieukhien"></a>

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/snapshot/overview](https://hcm-3.console.vngcloud.vn/vserver/block-store/snapshot/overview).
2. Chọn tạo **Snapshot**
3. Tại trang nhập thông tin tạo Snapshot, bạn cần hoàn thành các mục sau đây:
   * **Loại Snapshot** – Chọn đối tượng bạn muốn tạo Snapshot theo Volume.&#x20;
   * **Tên Snapshot** – Tên cho Snapshot của bạn. Tên chỉ có thể chứa các ký tự chữ và số (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào của bạn phải từ 5 đến 50. Tên phải là duy nhất trong Khu vực và tài khoản VNG Cloud mà bạn đang tạo Snapshot.
   * **Cài đặt Snapshot:**\

     * **Volume ID:** Chọn Volume bạn cần tạo Snapshot theo ID
     * **Description** – Nhập ghi chú cho bản Snapshot
     * **Thời gian lưu giữ:** Lựa chọn thời gian lưu Snapshot, bạn có thể chọn lưu giữ bản Snapshot vĩnh viễn hoặc theo số ngày bạn nhập
4. Sau khi điền các thông tin cần thiết, hãy chọn **Tạo Snapshot** để xác nhận khởi tạo. Trường Trạng thái hiển thị **Creating** khi Snapshot được tạo. Hành động này sẽ nhắc cơ sở hạ tầng đám mây bắt đầu thu thập dữ liệu từ ổ đĩa đã chọn.

***

### **Tạo Snapshot cho Server trên bảng điều khiển** <a href="#taosnapshot-taosnapshotchoservertrenbangdieukhien" id="taosnapshot-taosnapshotchoservertrenbangdieukhien"></a>

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/snapshot/overview](https://hcm-3.console.vngcloud.vn/vserver/block-store/snapshot/overview).
2. Chọn tạo **Snapshot**
3. Tại trang nhập thông tin tạo Snapshot, bạn cần hoàn thành các mục sau đây:
   * **Loại Snapshot** – Chọn đối tượng bạn muốn tạo Snapshot theo Server. Nếu lựa chọn theo Server đồng nghĩa với việc bạn sẽ tạo Snapshot được đính kèm với Server đã chọn.
   * **Tên Snapshot** – Tên cho Snapshot của bạn. Tên chỉ có thể chứa các ký tự chữ và số (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào của bạn phải từ 5 đến 50. Tên phải là duy nhất trong Khu vực và tài khoản VNG Cloud mà bạn đang tạo Snapshot.
   * **Cài đặt Snapshot:**\

     * **Volume ID:** Chọn Volume bạn cần tạo Snapshot theo ID
     * **Description** – Nhập ghi chú cho bản Snapshot
     * **Thời gian lưu giữ:** Lựa chọn thời gian lưu Snapshot, bạn có thể chọn lưu giữ bản Snapshot vĩnh viễn hoặc theo số ngày bạn nhập
4. Sau khi điền các thông tin cần thiết, hãy chọn **Tạo Snapshot** để xác nhận khởi tạo. Trường Trạng thái hiển thị **Creating** khi Snapshot được tạo. Hành động này sẽ nhắc cơ sở hạ tầng đám mây bắt đầu thu thập dữ liệu từ ổ đĩa đã chọn.

***

### **Mã hóa Snapshot** <a href="#taosnapshot-mahoasnapshot" id="taosnapshot-mahoasnapshot"></a>

Mã hóa Snapshot đảm bảo tính bảo mật cho dữ liệu của bạn trong môi trường đám mây. Khi ảnh chụp nhanh được tạo từ các ổ đĩa được mã hóa, chúng sẽ tự động được mã hóa, bảo vệ dữ liệu khi lưu trữ và trong quá trình truyền tải. Cơ chế mã hóa này cung cấp khả năng bảo vệ toàn diện cho cả ổ đĩa và mọi ảnh chụp nhanh liên quan. Để biết thêm chi tiết, vui lòng tham khảo tài liệu về [mã hóa Volume](../server/compute-encryption-volume/).
