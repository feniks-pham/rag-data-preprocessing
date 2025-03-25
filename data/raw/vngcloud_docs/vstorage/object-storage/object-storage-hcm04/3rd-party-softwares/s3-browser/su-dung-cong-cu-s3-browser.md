# Sử dụng công cụ S3 Browser

## Các usecase cơ bản

Bên dưới là hướng dẫn cho một số use case thông thường bạn có thể thực hiện trên S3 Browser:

### **Tạo / Xóa bucket**

* Thực hiện tạo xóa bucket bằng cách chọn nút **New bucket**, lúc này bạn thực hiện nhập **Bucket name** và chọn **Create new bucket.**

### **Upload / Download file**

* Sau khi đã tạo bucket, bạn chọn vào bucket cần tải file lên/ xuống. Tiếp theo, bạn chọn **Upload/ Download** tùy theo nhu cầu tải lên/ xuống của bạn.

### **Tạo / Xóa Folder**

* Bạn cũng có thể tạo/ xóa folder bằng cách chọn **New Folder** hoặc **Delete**.

<figure><img src="../../../../../.gitbook/assets/image (589).png" alt=""><figcaption></figcaption></figure>

***

## Các usecase nâng cao

Tiếp theo đây là các hướng dẫn cho các tính năng nâng cao bạn có thể thực hiện trên S3 Browser:

### **ACL**

**ACL** là tính năng trên S3 cho phép bạn kiểm soát quyền truy cập cho từng object trong bucket S3 của bạn. Tính năng này sẽ xác định người dùng hoặc nhóm người dùng nào có thể truy cập object và các thao tác họ có thể thực hiện, chẳng hạn như tải xuống, tải lên, xóa hoặc ghi đè object.

Để thiết lập ACL cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn Edit Permission (ACL) . Trong phần permission, hãy check chọn quyền hạn bạn mong muốn cấp cho người dùng. Chi tiết tham khảo thêm tại [https://s3browser.com/share-s3-bucket-edit-acls.aspx](https://s3browser.com/share-s3-bucket-edit-acls.aspx)

<figure><img src="../../../../../.gitbook/assets/image (590).png" alt=""><figcaption></figcaption></figure>

### **SSE-S3**

SSE-S3 (Server-Side Encryption with S3 Managed Keys) là tính năng mã hóa dữ liệu phía máy chủ do Amazon S3 cung cấp. Với SSE-S3, dữ liệu của bạn được mã hóa tự động khi được tải lên S3 và được giải mã tự động khi bạn tải xuống. **Để thực hiện được tính năng này trên S3 Browser, bạn cần sử dụng S3 Browser phiên bản Pro. Nếu ứng dụng của bạn hiện không hỗ trợ cho việc thực hiện tính năng, vui lòng gửi yêu cầu sử dụng tính năng thông qua ticket tới VNGCloud.** Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-server-side-encryption.aspx](https://s3browser.com/amazon-s3-server-side-encryption.aspx)

### **SSE-C**

**SSE-C** (Server-Side Encryption with Customer-Provided Keys) là tính năng mã hóa dữ liệu phía máy chủ do Amazon S3 cung cấp. Giống như SSE-S3, SSE-C mã hóa dữ liệu của bạn tự động khi được tải lên S3 và giải mã tự động khi bạn tải xuống. Tuy nhiên, với SSE-C, bạn cung cấp và quản lý khóa mã hóa của riêng mình, thay vì sử dụng khóa do AWS quản lý. **Để thực hiện được tính năng này trên S3 Browser, bạn cần sử dụng S3 Browser phiên bản Pro. Nếu ứng dụng của bạn hiện không hỗ trợ cho việc thực hiện tính năng, vui lòng gửi yêu cầu sử dụng tính năng thông qua ticket tới VNGCloud.** Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-server-side-encryption.aspx](https://s3browser.com/amazon-s3-server-side-encryption.aspx)

### **Object Locked**

**Object Lock** là tính năng giúp bảo vệ dữ liệu của bạn khỏi bị xóa hoặc ghi đè trong một khoảng thời gian cố định hoặc vô thời hạn. Tính năng này sử dụng model **WORM** (Write Once, Read Many), nghĩa là sau khi một object được tải lên S3 và được locked, object đó không thể bị xóa hoặc thay đổi bởi bất kỳ ai, kể cả người dùng root.

Để thiết lập Object Locked cho một bucket bằng S3 Browser, khi khởi tạo một bucket mới, bạn cần chọn phương án **Enable S3 Objected Lock.**

<figure><img src="../../../../../.gitbook/assets/image (623).png" alt=""><figcaption></figcaption></figure>

Tiếp theo, khi bucket được tạo thành công, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Object Locked**. Bạn có thể thiết lập object locked ở cả 2 mode **Retention** và **Legal Hold** thông qua S3 Browser. Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-object-lock.aspx](https://s3browser.com/amazon-s3-object-lock.aspx)

<figure><img src="../../../../../.gitbook/assets/image (592).png" alt=""><figcaption></figcaption></figure>

### **Versioning**

Versioning là một tính năng hỗ trợ lưu trữ nhiều phiên bản quá khứ của các object được lưu trữ trong một bucket. Bạn có thể sử dụng tính năng versioning để lưu giữ, truy xuất và khôi phục mọi phiên bản của object được lưu trữ trong bucket của bạn. Khi bật tính năng Versioning, khi thực hiện tải lên/ xóa một object thì thay vì xóa hẳn object khỏi hệ thống, chúng tôi sẽ chuyển các object bị xóa hoặc bị ghi đè sang phiên bản versioning. Từ đó bạn có thể dễ dàng khôi phục lại các object bị xóa nhầm hoặc tải về các phiên bản cũ của dữ liệu khi có nhu cầu sử dụng.

Để thiết lập Versioning cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Edit Versioning Settings**. Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-versioning.aspx](https://s3browser.com/amazon-s3-versioning.aspx)

<figure><img src="../../../../../.gitbook/assets/image (594).png" alt=""><figcaption></figcaption></figure>

### **Lifecycle rotation**

**Lifecycle rotation** là một tính năng quản lý vòng đời của các đối tượng (objects) trong một bucket. Tính năng này cho phép bạn tự động hóa các hành động như xóa các đối tượng sau một khoảng thời gian nhất định.

Để thiết lập Lifecycle rotation cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Lifecycle Configuration**. Chi tiết tham khảo thêm tại [https://s3browser.com/bucket-lifecycle-configuration.aspx](https://s3browser.com/bucket-lifecycle-configuration.aspx)

<figure><img src="../../../../../.gitbook/assets/image (595).png" alt=""><figcaption></figcaption></figure>

### **Lifecycle transit**

Hiện tại trên region HCM04 chúng tôi chỉ hỗ trợ bạn tạo Project với Storage Class **Instant Archive Type**. Do chỉ có 1 storage class duy nhất nên hiện tại tính năng Lifecycle transit sẽ không hoạt động.

### **CORS**

CORS (Cross-Origin Resource Sharing) là cơ chế bảo mật cho phép các trang web được lưu trữ trên một tên miền truy cập tài nguyên từ tên miền khác. Khi bạn sử dụng S3 để lưu trữ nội dung tĩnh và muốn truy cập nội dung đó từ trang web được lưu trữ trên tên miền khác, bạn cần cấu hình CORS cho bucket S3 của mình.

Để thiết lập CORS cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **CORS Configuration**. Chi tiết tham khảo thêm tại [https://s3browser.com/s3-bucket-cors-configuration.aspx](https://s3browser.com/s3-bucket-cors-configuration.aspx)

<figure><img src="../../../../../.gitbook/assets/image (596).png" alt=""><figcaption></figcaption></figure>

### **Public/ Private bucket**

**Public bucket** là tính năng cho phép người dùng chia sẻ công khai bucket trên môi trường điện toán đám mây. Người dùng từ ngoài internet có thể truy cập vào bucket thông qua đường dẫn URL mà không cần chứng thực quyền truy cập với hệ thống. Quyền truy cập công khai tiềm ẩn rủi ro bảo mật, vì vậy nếu kịch bản của bạn không yêu cầu quyền truy cập đó, chúng tôi khuyên bạn không nên cho phép quyền truy cập công khai đối với bucket. Tại bất kỳ thời điểm nào bạn không muốn công khai bucketđó nữa thì có thể chuyển chế độ riêng tư cho bucket.

Để thiết lập chế độ công khai cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Public Access block Configuration**. Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-public-access-block-configuration.aspx](https://s3browser.com/amazon-s3-public-access-block-configuration.aspx)

<figure><img src="../../../../../.gitbook/assets/image (597).png" alt=""><figcaption></figcaption></figure>

### **Bucket policy**

**Bucket Policy** là một loại chính sách truy cập được sử dụng để kiểm soát quyền truy cập vào một bucket S3 cụ thể. Nó cho phép bạn xác định người dùng hoặc nhóm nào có thể truy cập bucket và các thao tác họ có thể thực hiện, chẳng hạn như tải lên, tải xuống, xóa hoặc liệt kê các object trong bucket.

Để thiết lập policy một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Edit Bucket Policy**. Chi tiết tham khảo thêm tại [https://s3browser.com/working-with-amazon-s3-bucket-policies.aspx?v=11.7.5\&fam=x64#amazon-s3-bucket-policies-examples](https://s3browser.com/working-with-amazon-s3-bucket-policies.aspx?v=11.7.5\&fam=x64#amazon-s3-bucket-policies-examples)

<figure><img src="../../../../../.gitbook/assets/image (598).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

1. Không nên sử dụng phiên bản S3 Browser quá cũ/ quá mới trên các hệ điều hành có phiên bản quá cũ/ quá mới vì có thể gặp lỗi.
2. S3 Browser có hỗ trợ dọn incomplete segments khi tải object lớn (multipart upload). Khi bạn sử dụng S3 Browser để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, S3 Browser của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Chúng tôi khuyến cáo bạn thực hiện xóa bỏ những segment rác này để tối ưu hóa chi phí và dung lượng lưu trữ bằng cách:
   1. Mở ứng dụng **S3 Browser**, chọn **Tools** sau đó chọn **Uncompleted Multipart Uploads**.
   2. Chọn một hoặc nhiều phần **tệp tin** được tải lên và chọn **Abort** hoặc nhấp chuột phải và chọn **Abort**.&#x20;

Chi tiết tham khảo tại: [https://s3browser.com/uncompleted-multipart-uploads.aspx](https://s3browser.com/uncompleted-multipart-uploads.aspx)
{% endhint %}
