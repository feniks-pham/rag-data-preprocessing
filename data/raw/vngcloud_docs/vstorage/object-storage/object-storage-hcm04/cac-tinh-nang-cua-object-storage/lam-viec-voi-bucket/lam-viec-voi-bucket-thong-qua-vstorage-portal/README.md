# Làm việc với bucket thông qua vStorage Portal

Bên dưới là các tính năng cơ bản khi bạn làm việc với bucket

## Khởi tạo bucket

Trước khi có thể lưu trữ dữ liệu trong vStorage, bạn phải tạo 1 Bucket. Trên vStorage, Bucket là đối tượng chứa dữ liệu (Object).&#x20;

Để khởi tạo một project, vui lòng thực hiện theo các bước bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list). Chọn **project** muốn thực hiện tạo **bucket.**
2. Chọn **Create a bucket**.
3. Nhập **Bucket name** theo quy định của chúng tôi.
4. Chọn **Enable Object Locked** nếu bạn muốn sử dụng tính năng **Object locked** cho bucket này.&#x20;

{% hint style="info" %}
**Chú ý:**

* Để sử dụng tính năng **Object locked** cho một bucket trên vStorage, khi khởi tạo bucket, bạn bắt buộc phải lựa chọn **Enable Object Locked**.
* Khi bạn chọn **Enable Object Locked**, chúng tôi sẽ tự động bật tính năng **Object version** cho bucket của bạn.
{% endhint %}

<figure><img src="../../../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Xem thông tin bucket

Sau khi tạo bucket và tải lên object vào bucket đó. Bạn có thể xem chi tiết thông tin bucket và sử dụng các tính năng mà chúng tôi cung cấp cho bucket bao gồm: ACLs, Lifecycle, CORS,...&#x20;

Để xem chi tiết thông tin của một bucket, bạn có thể:&#x20;

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** chứa **bucket** bạn muốn xem chi tiết.

3\. Chọn **bucket** bạn muốn xem chi tiết và chọn **View detail**.

4\. Trên trang hiển thị thông tin chi tiết **bucket**, bạn có thể xem và sử dụng các tính năng mà chúng tôi cung cấp cho bucket bao gồm:

* **Thông tin chung**: Cung cấp các thông tin chung của bucket như Name, Owner, Created date, Versioning, Encryption, Object Lock.
* **ACLs**: Cung cấp thông tin quản lý truy cập Read/Write/Read+Write của một hay nhiều tài khoản Root đang có trên hệ thống được cấp phép truy cập trên bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại [Sử dụng tính năng ACLs](su-dung-tinh-nang-acls.md).
* **CORS**: Cung cấp thông tin các đường dẫn được phép truy cập vào tài nguyên của bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại [Sử dụng tính năng CORS.](su-dung-tinh-nang-cors.md)
* **Lifecycle**: Cung cấp thông tin các lifecycle được thiết lập cho bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại[ Sử dụng tính năng lifecycle.](su-dung-tinh-nang-lifecycle.md)
* **Event notification**: Cung cấp thông tin các event notification được thiết lập cho bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại [Sử dụng tính năng Event notification.](su-dung-tinh-nang-event-notification.md)

<figure><img src="../../../../../../.gitbook/assets/image (798).png" alt=""><figcaption></figcaption></figure>

***

## Sử dụng tính năng Bucket encryption

**SSE-S3 (Server-Side Encryption with S3 Managed Keys)** là tính năng mã hóa dữ liệu phía máy chủ do Amazon S3 cung cấp. Với SSE-S3, dữ liệu của bạn được mã hóa tự động khi được tải lên S3 và được giải mã tự động khi bạn tải xuống.

Để sử dụng tính năng Bucket encryption, vui lòng thực hiện theo các bước bên dưới:

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** chứa **bucket** bạn muốn thiết lập encryption.

3\. Chọn biểu tượng **Action** và chọn **Configure encryption**

<figure><img src="../../../../../../.gitbook/assets/image (799).png" alt=""><figcaption></figcaption></figure>

4\. Trên trang xác nhận sử dụng encryption SSE-S3, vui lòng chọn **Enable ecryption.**

<figure><img src="../../../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Xóa bucket

Để xóa một bucket, vui lòng thực hiện theo các bước bên dưới:

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **bucket** bạn muốn thực hiện xóa.

3\. Chọn biểu tượng **Action** và chọn **Delete**

<figure><img src="../../../../../../.gitbook/assets/image (800).png" alt=""><figcaption></figcaption></figure>

Sau khi chọn Xóa, hệ thống sẽ tự động chuyển ra màn hình chính, nếu bạn thấy bucket vừa thực hiện biến mất khỏi danh sách thì bạn đã xoá thành công. Bucket lúc này đã được xóa vĩnh viễn khỏi hệ thống và bạn không thể khôi phục bucket cũng như các object được lưu trữ trong bucket. Vì vậy hãy đảm bảo kiểm tra dữ liệu của bạn trước khi thực hiện thao tác này.&#x20;
