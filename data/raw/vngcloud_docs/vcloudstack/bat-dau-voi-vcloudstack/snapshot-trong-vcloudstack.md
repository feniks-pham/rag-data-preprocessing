# Snapshot trong vCloudStack

## Tổng quan

Tính năng snapshot là một thành phần quan trọng trong hệ thống lưu trữ. Nó cung cấp khả năng tạo và quản lý các phiên bản sao lưu của dữ liệu ổ đĩa ảo của bạn tại các điểm thời gian cụ thể, mang lại nhiều lợi ích quan trọng trong việc bảo vệ dữ liệu, tối ưu hóa tài nguyên và đảm bảo khả năng phục hồi dữ liệu trong trường hợp cần thiết.

Mỗi snapshot chứa đầy đủ thông tin cần thiết để khôi phục dữ liệu của bạn đến trạng thái tại thời điểm snapshot được tạo ra. Khi bạn tạo một ổ đĩa mới dựa trên một snapshot, ổ đĩa mới này bắt đầu như một bản sao chính xác của ổ đĩa gốc được sử dụng để tạo snapshot. Quá trình sao chép dữ liệu được thực hiện ẩn sau cùng để bạn có thể bắt đầu sử dụng nó ngay lập tức. Nếu bạn truy cập dữ liệu chưa được tải, ổ đĩa sẽ tự động tải dữ liệu yêu cầu từ hệ thống, sau đó tiếp tục tải dữ liệu còn lại của ổ đĩa trong nền.

Snapshot cũng hỗ trợ mã hóa dữ liệu một cách toàn diện, đảm bảo tính bảo mật của dữ liệu lưu trữ và giúp tuân thủ các yêu cầu về bảo mật và quyền riêng tư. Bạn có thể tạo snapshot cho các ổ đĩa đã được mã hóa và thể tạo ổ đĩa mới từ các snapshot đã được mã hóa.

vCloudStack hỗ trợ việc tạo Snapshot cho cả Server và Volume, giúp đơn giản hóa quá trình tạo Snapshot và phù hợp với mọi nhu cầu sử dụng của bạn. Khi đã tạo Snapshot cho máy chủ ảo và ổ đĩa ảo, bạn có thể sử dụng tính năng Roll Back của chúng tôi để khôi phục lại trạng thái của máy ảo và ổ đĩa ảo đến thời điểm Snapshot được tạo.

Ổ đĩa mà bạn muốn tạo Snapshot ở trạng thái **Đang sử dụng** hoặc **Chưa đính kèm**. Hãy lưu ý các mục sau:

* Nếu đĩa ở **trạng thái Đang sử dụng:** hãy đảm bảo rằng phiên bản mà đĩa được gắn vào ở trạng thái Đang chạy hoặc Đã dừng.
* Nếu đĩa ở **trạng thái Chưa được đính kèm:** hãy đảm bảo rằng đĩa đã được gắn vào một Server tại một thời điểm nào đó. Không thể tạo snapshot cho các ổ đĩa đám mây chưa từng được gắn vào VM.

***

### **Tạo Snapshot**  <a href="#taosnapshot-taosnapshotchovolumetrenbangdieukhien" id="taosnapshot-taosnapshotchovolumetrenbangdieukhien"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Snapshot.

**Bước 2:** Chọn tạo **Snapshot**

**Bước 3:** Tại trang nhập thông tin tạo Snapshot, bạn cần hoàn thành các mục sau đây:

* **Loại Snapshot** – Mặc định theo Server.&#x20;
* **Tên Snapshot** – Hệ thống tự tạo ra dựa trên tên VM và thời gian tạo Snapshot
* **Chọn Volume** – Chọn loại tài nguyên bạn muốn sao lưu, ở đây là danh sách Server và Volume đính kèm với nó.
* **Cài đặt Policy:** Chọn **Policy** bạn muốn áp dụng cho bản snapshot.

**Bước 4:** Nhập thông tin **ghi chú** cho các bản sao lưu của bạn để tạo sự gợi nhớ&#x20;

**Bước 5:** Chọn nút **Tạo** để xác nhận khởi tạo. Trường Trạng thái hiển thị **Creating** khi Snapshot được tạo. Hành động này sẽ nhắc cơ sở hạ tầng đám mây bắt đầu thu thập dữ liệu từ ổ đĩa đã chọn.

***

### **Khôi phục máy chủ ảo bằng Snapshot trên bảng điều khiển** <a href="#khoiphucmaychuaobangbansnapshot-khoiphucmaychuaobangsnapshottrenbangdieukhien" id="khoiphucmaychuaobangbansnapshot-khoiphucmaychuaobangsnapshottrenbangdieukhien"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Snapshot.

**Bước 2:** Chọn tạo **Snapshot**

**Bước 3:** Chọn Snapshot của bản Boot Volume tại trang danh sách rồi chọn **Hành động**, nhấn Rollback Serve&#x72;**.**

### **Tạo máy chủ (Server) bằng Snapshot trên Màn hình Tạo Server**  <a href="#khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhtaoserversnapshotcreateserve" id="khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhtaoserversnapshotcreateserve"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack.

**Bước 2:** Trong ngăn điều hướng, chọn **Servers**;

**Bước 3:** Chọn nút "**Tạo Server**" (Create a Server), để điều hướng tới màn hình Tạo Server;

**Bước 4:** Để cấu hình Tạo Server bằng trên snapshot. Tại mục "**Cấu hình cơ bản/Image**" chọn Tab "**My snapshot**";

**Bước 5:** User có thể chọn bản snapshot phù hợp để tạo lại Server với thời điểm tương ứng.

{% hint style="info" %}
**Lưu ý:** Khi cấu hình tạo Server mới bằng Snapshot, user vẫn thực hiện thao tác cấu hình ở các mục khác (Loại cấu hình, volume, Cài đặt mạng, Cài đặt khác) như thông thường, xem hướng dẫn ở [Khởi tạo VM trên vCloudstack](khoi-tao-vm-tren-vcloudstack.md).
{% endhint %}

### **Tạo máy chủ (Server) bằng Snapshot trên Màn hình Snapshot** <a href="#khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhsnapshot" id="khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhsnapshot"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Snapshot.

**Bước 2:** Tại màn hình danh sách Snapshot, User **click chọn vào một Snapshot Server**, để điều hướng đến màn hình thông tin chi tiết.

**Bước 3:** Tại màn hình chi tiết của Snapshot Server, User chọn Tab "**Restore Point**".

**Bước 4:** Sau đó chọn bản Snapshot tương ứng muốn tạo Server, bằng cách click vào nút hành động, chọn "**Tạo server**".

**Bước 5:** Màn hành điều hướng tới màn hình Tạo Server với tùy chọn file Snapshot đã chọn, và tiếp tục thao tác giống "Tạo Server bằng Snapshot trên Màn hình Tạo Server" như trên.



### **Khôi phục ổ đĩa ảo bằng Snapshot trên bảng điều khiển** <a href="#khoiphucodiaaobangbansnapshot-khoiphucodiaaobangsnapshottrenbangdieukhien" id="khoiphucodiaaobangbansnapshot-khoiphucodiaaobangsnapshottrenbangdieukhien"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack.

**Bước 2:** Trong ngăn điều hướng, chọn **Snapshot**;

**Bước 3:** Chọn Snapshot của bản Data Volume tại trang danh sách rồi chọn **Hành động**, nhấn Rollback Volum&#x65;**.**

### **Xoá Snapshot Volume tại trang danh sách Snapshot trên bảng điều khiển** <a href="#xoasnapshot-xoasnapshotvolumetaitrangdanhsachsnapshottrenbangdieukhien" id="xoasnapshot-xoasnapshotvolumetaitrangdanhsachsnapshottrenbangdieukhien"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack.

**Bước 2:** Trong ngăn điều hướng, chọn **Snapshot**;

**Bước 3:** Chọn Snapshot cần xóa rồi chọn **Hành động**, nhấn **Xóa Snapshot.**

### **Xoá Snapshot Volume tại trang chi tiết Volume trên bảng điều khiển** <a href="#xoasnapshot-xoasnapshotvolumetaitrangchitietvolumetrenbangdieukhien" id="xoasnapshot-xoasnapshotvolumetaitrangchitietvolumetrenbangdieukhien"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack.

**Bước 2:** Trong ngăn điều hướng, chọn **Volume**;

**Bước 3:** Nhấn vào tên Volume để vào trang chi tiết Volume

**Bước 4:** Chuyển sang Tab **Associated Snapshot**

**Bước 5:** Thực hiện chọn Snapshot Volume cần xoá và chọn **Delete Snapshot Volume Point**

### **Xoá Snapshot Server tại trang chi tiết Server trên bảng điều khiển** <a href="#xoasnapshot-xoasnapshotservertaitrangchitietservertrenbangdieukhien" id="xoasnapshot-xoasnapshotservertaitrangchitietservertrenbangdieukhien"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack.

**Bước 2:** Trong ngăn điều hướng, chọn **Server**;

**Bước 3:** Nhấn vào tên Server để vào trang chi tiết Server

**Bước 4:** Chuyển sang Tab **Associated Snapshot**

**Bước 5:** Thực hiện chọn Snapshot Server cần xoá và chọn **Delete Snapshot Volume Point.**
