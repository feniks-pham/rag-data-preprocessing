# Snapshot

Tính năng snapshot là một thành phần quan trọng trong hệ thống lưu trữ đám mây của VNG Cloud. Nó cung cấp khả năng tạo và quản lý các phiên bản sao lưu của dữ liệu ổ đĩa ảo của bạn tại các điểm thời gian cụ thể, mang lại nhiều lợi ích quan trọng trong việc bảo vệ dữ liệu, tối ưu hóa tài nguyên và đảm bảo khả năng phục hồi dữ liệu trong trường hợp cần thiết.

Mỗi snapshot chứa đầy đủ thông tin cần thiết để khôi phục dữ liệu của bạn đến trạng thái tại thời điểm snapshot được tạo ra. Khi bạn tạo một ổ đĩa mới dựa trên một snapshot, ổ đĩa mới này bắt đầu như một bản sao chính xác của ổ đĩa gốc được sử dụng để tạo snapshot. Quá trình sao chép dữ liệu được thực hiện ẩn sau cùng để bạn có thể bắt đầu sử dụng nó ngay lập tức. Nếu bạn truy cập dữ liệu chưa được tải, ổ đĩa sẽ tự động tải dữ liệu yêu cầu từ hệ thống, sau đó tiếp tục tải dữ liệu còn lại của ổ đĩa trong nền.

Snapshot cũng hỗ trợ mã hóa dữ liệu một cách toàn diện, đảm bảo tính bảo mật của dữ liệu lưu trữ và giúp tuân thủ các yêu cầu về bảo mật và quyền riêng tư. Bạn có thể tạo snapshot cho các ổ đĩa đã được mã hóa và thể tạo ổ đĩa mới từ các snapshot đã được mã hóa.

Tại VNG Cloud, chúng tôi hỗ trợ việc tạo Snapshot cho cả Server và Volume, giúp đơn giản hóa quá trình tạo Snapshot và phù hợp với mọi nhu cầu sử dụng của bạn. Khi đã tạo Snapshot cho máy chủ ảo và ổ đĩa ảo, bạn có thể sử dụng tính năng Roll Back của chúng tôi để khôi phục lại trạng thái của máy ảo và ổ đĩa ảo đến thời điểm Snapshot được tạo.

Bên cạnh việc khôi phục Roll Back máy chủ từ file snapshot, VNG Cloud cho phép tạo máy chủ mới dựa trên file Snapshot đã tạo. Từ đó, chúng tôi hỗ trợ việc chia sẻ và sử dụng file Snapshot cho người dùng khác trong VNG Cloud, mang đến cho người dùng những trải nghiệm quản lý hệ thống tốt hơn.

<figure><img src="../../../.gitbook/assets/image (382).png" alt="" width="563"><figcaption></figcaption></figure>



***

### **Snapshot hoạt động như thế nào** <a href="#snapshot-snapshothoatdongnhuthenao" id="snapshot-snapshothoatdongnhuthenao"></a>

Sự hình thành của các snapshot trong hệ thống lưu trữ đám mây của chúng tôi, là một quá trình có sự phức tạp và tối ưu hóa đáng kinh ngạc. Khi bạn tạo snapshot đầu tiên từ một ổ đĩa, nó luôn luôn được xem như là một bản snapshot đầy đủ, chứa tất cả các khối dữ liệu đã được ghi vào ổ đĩa gốc tại thời điểm tạo snapshot đó.

Các snapshot sau này, theo một cách ấn tượng, là các phiên bản tăng dần của snapshot ban đầu. Chúng không đòi hỏi lưu trữ lại toàn bộ dữ liệu trên ổ đĩa nguồn, mà chỉ tập trung vào việc sao lưu các khối dữ liệu mới và đã thay đổi từ thời điểm snapshot trước đó được tạo ra. Điều quan trọng cần lưu ý là kích thước của snapshot đầy đủ không phụ thuộc vào kích thước của ổ đĩa nguồn, mà là dựa trên kích thước của dữ liệu bạn sao lưu. Chẳng hạn, nếu bạn tạo snapshot đầu tiên từ một ổ đĩa có dung lượng 200 GB nhưng chỉ chứa 50 GB dữ liệu, snapshot đầy đủ sẽ có kích thước là 50 GB và bạn sẽ chỉ bị tính phí cho dung lượng lưu trữ của snapshot 50 GB đó.

Tương tự, kích thước và chi phí lưu trữ của các snapshot gia tăng sau này sẽ dựa trên kích thước của dữ liệu mới đã được ghi vào ổ đĩa kể từ thời điểm snapshot trước đó. Tiếp tục ví dụ trên, nếu bạn tạo snapshot thứ hai cho ổ đĩa 200 GB sau khi thay đổi 20 GB dữ liệu và thêm 10 GB dữ liệu, snapshot gia tăng sẽ có kích thước là 30 GB. Sau đó, bạn sẽ bị tính phí cho dung lượng lưu trữ snapshot 30 GB bổ sung đó.&#x20;

**Giả sử bạn có một ổ đĩa với dung lượng 25 GB:**

* Ở Trạng thái 1, ổ đĩa có 20 GB dữ liệu. Snap 1 là ảnh chụp nhanh đầu tiên của tập đĩa. Snap 1 là ảnh chụp nhanh đầy đủ và toàn bộ 20 GB dữ liệu được sao lưu.
* Ở Trạng thái 2, ổ đĩa vẫn chứa 20 GB dữ liệu nhưng chỉ có 5 GB thay đổi sau khi chụp Snap 1. Snap 2 là ảnh chụp nhanh tăng dần. Nó chỉ cần sao lưu 5 GB đã thay đổi. 15 GB dữ liệu không thay đổi khác, đã được sao lưu trong Snap 1, được Snap 2 tham chiếu thay vì được sao lưu lại.
* Ở Trạng thái 3, 2 GB dữ liệu đã được thêm vào ổ đĩa, tổng cộng là 22 GB, sau khi chụp Snap 2. Snap 3 là ảnh chụp nhanh tăng dần. Nó chỉ cần sao lưu 2 GB đã được thêm vào sau khi chụp Snap 2, Snap 3 cũng tham chiếu 5 GB dữ liệu được lưu trữ trong Snap 2 và 15 GB dữ liệu được lưu trữ trong Snap 1.

Tổng dung lượng lưu trữ cần thiết cho ba ảnh chụp nhanh ở giai đoạn 3 (giai đoạn cuối) là tổng cộng 27 GB. Điều này chiếm 20 GB cho Snap 1, 5 GB cho Snap 2 và 2 GB cho Snap 3.

Như vậy, bạn đã tạo một chuỗi các ảnh chụp tăng dần, mỗi ảnh chụp chỉ chứa những thay đổi so với ảnh chụp trước đó, giúp tiết kiệm không gian lưu trữ và làm cho quá trình sao lưu và phục hồi dữ liệu hiệu quả hơn.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553870/image2023-10-3_21-18-15.png?version=1&#x26;modificationDate=1696342696000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

***

### **Trường hợp sử dụng** <a href="#snapshot-truonghopsudung" id="snapshot-truonghopsudung"></a>

#### **Lưu trữ & phục hồi Dữ Liệu** <a href="#snapshot-luutru-and-phuchoidulieu" id="snapshot-luutru-and-phuchoidulieu"></a>

Snapshot thường được sử dụng để bảo vệ dữ liệu quan trọng khỏi mất mát. Khi bạn tạo các bản snapshot định kỳ, bạn có thể phục hồi dữ liệu về trạng thái trước khi có sự cố hệ thống hoặc xóa dữ liệu.

#### **Phát Triển và Kiểm Tra** <a href="#snapshot-phattrienvakiemtra" id="snapshot-phattrienvakiemtra"></a>

Khi bạn làm việc trên môi trường phát triển hoặc kiểm tra, snapshot có thể được sử dụng để tạo bản sao lưu của môi trường hiện tại. Sau đó, bạn có thể sử dụng bản snapshot này để triển khai môi trường tương tự hoặc để kiểm tra các thay đổi mà không ảnh hưởng đến môi trường chính.

#### **Chuyển Đổi Giữa Môi Trường** <a href="#snapshot-chuyendoigiuamoitruong" id="snapshot-chuyendoigiuamoitruong"></a>

Snapshot có thể giúp bạn chuyển đổi dữ liệu một cách dễ dàng trong trường hợp bạn muốn di chuyển dữ liệu hoặc ứng dụng giữa các môi trường khác nhau. Chẳng hạn, bạn có thể chuyển dữ liệu từ môi trường phát triển sang môi trường sản xuất.

***

### **Bắt đầu với Snapshot** <a href="#snapshot-batdauvoisnapshot" id="snapshot-batdauvoisnapshot"></a>

Để có thể sử dụng Snapshot bạn cần kích hoạt bản Snapshot tại giao diện bảng điều khiển của chúng tôi, vui lòng xem hướng dẫn [Kích hoạt Snapshot.](kich-hoat-snapshot.md)
