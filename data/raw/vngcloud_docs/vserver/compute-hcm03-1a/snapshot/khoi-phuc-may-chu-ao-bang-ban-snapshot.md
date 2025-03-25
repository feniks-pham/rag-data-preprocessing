# Khôi phục máy chủ ảo bằng bản Snapshot

Bạn có thể khôi phục ổ đĩa ảo hoặc máy chủ ảo bằng các bản Snapshot đã tạo, nội dung bên dưới mô tả cách khôi phục máy chủ ảo bằng các bản Snapshot.

Sử dụng bản Snapshot cho phép bạn khôi phục dữ liệu và hệ thống nhanh chóng sau khi xảy ra sự cố. Điều này giúp giảm thời gian chịu ảnh hưởng của hệ thống. Đồng thời Khôi phục Snapshot là cách an toàn để sao lưu dữ liệu quan trọng của bạn. Nó đảm bảo rằng bạn có thể khôi phục dữ liệu và ổ đĩa trong trường hợp cần thiết, như lỗi phần cứng, lỗi phần mềm hoặc xóa dữ liệu một cách không cẩn thận. So với việc tái cấu hình và khôi phục hệ thống từ đầu, việc sử dụng Snapshot tiết kiệm thời gian và công sức đáng kể.

***

### **Các trường hợp cần khôi phục máy chủ ảo** <a href="#khoiphucmaychuaobangbansnapshot-cactruonghopcankhoiphucmaychuao" id="khoiphucmaychuaobangbansnapshot-cactruonghopcankhoiphucmaychuao"></a>

* **Sự cố hệ thống nghiêm trọng**: Khi máy chủ ảo gặp sự cố nghiêm trọng không thể khắc phục hoặc gây ảnh hưởng lớn đến dịch vụ và dữ liệu, bạn có thể xem xét khôi phục máy chủ ảo từ một bản sao lưu gần đây để khôi phục dịch vụ và dữ liệu.
* **Lỗi phần mềm cụ thể**: Nếu máy chủ ảo gặp lỗi phần mềm cụ thể hoặc không hoạt động đúng cách sau khi cài đặt hoặc cập nhật phần mềm, bạn có thể khôi phục máy chủ ảo về trạng thái trước khi lỗi xảy ra.
* **Rủi ro bảo mật**: Nếu máy chủ ảo của bạn bị tấn công mạng hoặc có nghi ngờ về việc xâm nhập, bạn nên xem xét khôi phục máy chủ ảo từ một thời điểm trước khi rủi ro xảy ra để loại bỏ các lỗ hổng bảo mật.
* **Thử nghiệm và phát triển**: Trong quá trình phát triển ứng dụng hoặc thử nghiệm các cấu hình mới, bạn có thể khôi phục máy chủ ảo về trạng thái ban đầu sau khi thử nghiệm để làm sạch môi trường và chuẩn bị cho các bước thử nghiệm tiếp theo.
* **Tạo môi trường thử nghiệm**: Nếu bạn cần tạo một môi trường thử nghiệm hoàn toàn mới, bạn có thể khôi phục máy chủ ảo từ bản sao lưu hoặc snapshot để có môi trường làm việc riêng biệt.
* **Lỗi người dùng cuối**: Nếu người dùng cuối hoặc người quản trị máy chủ ảo của bạn gây ra lỗi nghiêm trọng trên hệ thống, bạn có thể xem xét khôi phục máy chủ ảo để loại bỏ các thay đổi không mong muốn.
* **Phục hồi dữ liệu nhầm**: Nếu bạn xóa dữ liệu quan trọng hoặc thay đổi sai dữ liệu trên máy chủ ảo, bạn có thể khôi phục máy chủ ảo từ một bản sao lưu gần đây để khôi phục dữ liệu mất mát.

***

### **Rủi ro** <a href="#khoiphucmaychuaobangbansnapshot-ruiro" id="khoiphucmaychuaobangbansnapshot-ruiro"></a>

* **Dữ liệu lỗi:** Nếu bạn sử dụng một Snapshot đã lỗi hoặc chứa dữ liệu bị hỏng, việc khôi phục có thể đưa ra dữ liệu không đúng hoặc dữ liệu bị hỏng. Điều này đặc biệt quan trọng nếu bạn không kiểm tra Snapshot trước khi sử dụng nó.
* **Thời gian tạo Snapshot:** Nếu bạn tạo Snapshot không đều đặn hoặc không đủ thường xuyên, bạn có thể mất dữ liệu quan trọng nếu sự cố xảy ra giữa các lần tạo Snapshot. Thời gian cách biệt giữa các Snapshot cũng ảnh hưởng đến khả năng khôi phục dữ liệu.
* **Chi phí lưu trữ:** Việc duy trì nhiều Snapshot có thể tạo ra chi phí lưu trữ đáng kể. Bạn cần xem xét cân nhắc giữa lợi ích của việc lưu trữ nhiều Snapshot và chi phí tương ứng.
* **Sự cẩn thận trong quản lý Snapshot:** Quản lý các bản Snapshot đòi hỏi sự cẩn thận để đảm bảo rằng bạn không xóa nhầm các bản sao lưu quan trọng hoặc duy trì quá nhiều bản sao lưu không cần thiết.

Việc sử dụng bản Snapshot để khôi phục máy chủ ảo có nhiều lợi ích quan trọng, nhưng cũng đi kèm với những rủi ro cần phải cân nhắc và quản lý một cách cẩn thận. Điều quan trọng là phải thực hiện các biện pháp bảo mật và kiểm tra tính toàn vẹn của Snapshot trước khi thực hiện việc khôi phục dữ liệu.

\


***

Ghi chú

Bạn chỉ có thể khôi phục máy chủ ảo với bản Snapshot của Boot Volume.

### **Khôi phục máy chủ ảo bằng Snapshot trên bảng điều khiển** <a href="#khoiphucmaychuaobangbansnapshot-khoiphucmaychuaobangsnapshottrenbangdieukhien" id="khoiphucmaychuaobangbansnapshot-khoiphucmaychuaobangsnapshottrenbangdieukhien"></a>

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/).
2. Trong ngăn điều hướng, chọn **Snapshot**.
3. Chọn Snapshot của bản Boot Volume tại trang danh sách rồi chọn **Hành động**, nhấn Rollback Serve&#x72;**.**

### **Tạo máy chủ (Server) bằng Snapshot trên Màn hình Tạo Server**  <a href="#khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhtaoserversnapshotcreateserve" id="khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhtaoserversnapshotcreateserve"></a>

1. Đăng nhập và mở bảng điều kiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver](https://hcm-3.console.vngcloud.vn/vserver/);
2. Trong ngăn điều hướng, chọn **Servers**;
3. Chọn nút "**Tạo Server**" (Create a Server), để điều hướng tới màn hình Tạo Server;
4. Để cấu hình Tạo Server bằng trên snapshot. Tại mục "**Cấu hình cơ bản/Image**" chọn Tab "**My snapshot**";
5. User có thể chọn bản snapshot phù hợp để tạo lại Server với thời điểm tương ứng.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64554116/image2024-3-25_9-46-42.png?version=1&#x26;modificationDate=1711334805000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Lưu ý

Khi cấu hình tạo Server mới bằng Snapshot, user vẫn thực hiện thao tác cấu hình ở các mục khác (Loại cấu hình, volume, Cài đặt mạng, Cài đặt khác) như thông thường, xem hướng dẫn ở link.

### **Tạo máy chủ (Server) bằng Snapshot trên Màn hình Snapshot** <a href="#khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhsnapshot" id="khoiphucmaychuaobangbansnapshot-taomaychu-server-bangsnapshottrenmanhinhsnapshot"></a>

1. Đăng nhập và mở bảng điều kiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver](https://hcm-3.console.vngcloud.vn/vserver/);
2. Trong ngăn điều hướng, chọn **Snapshot**;
3. Tại màn hình danh sách Snapshot, User **click chọn vào một Snapshot Server**, để điều hướng đến màn hình thông tin chi tiết.
4. Tại màn hình chi tiết của Snapshot Server, User chọn Tab "**Restore Point**".
5. Sau đó chọn bản Snapshot tương ứng muốn tạo Server, bằng cách click vào nút hành động, chọn "**Tạo server**".
6. Màn hành điều hướng tới màn hình Tạo Server với tùy chọn file Snapshot đã chọn, và tiếp tục thao tác giống "Tạo Server bằng Snapshot trên Màn hình Tạo Server" như trên./.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64554116/image2024-3-25_10-11-32.png?version=1&#x26;modificationDate=1711336295000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
