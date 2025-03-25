# Chạy lại Transfer Job

Trong quá trình chạy transfer job, có thể xảy ra lỗi tại một hoặc một tập file. Khi transfer job chạy hoàn thành, bạn có thể thực hiện chạy lại transfer job này với điều kiện:

* Các thông tin về **Source**, **Destination, Job Information, Job Configuration không thay đổi so với lần chạy trước đó.**
* Chỉ thực hiện transfer danh sách **file** có trạng thái **transfer là** **error** được ghi nhận từ lần chạy trước đó.

Để thực hiện chạy lại Transfer Job, bạn có thể thực hiện như sau:&#x20;

**Bước 1:** Truy cập vào [https://datasync.console.vngcloud.vn/](https://datasync.console.vngcloud.vn/transfer-job/list)

**Bước 2:** Tại menu bên trái, chọn mục **Transfer Job**.&#x20;

**Bước 3:** Trên danh sách các transfer job đã tạo, hãy chọn một **Transfer Job** có File error ở lần chạy trước đó mà bạn muốn chạy lại.

**Bước 4:** Tại mục **Error**, chọn **View error details**.&#x20;

**Bước 5:** Lúc này, danh sách file bị transfer lỗi hiển thị.

**Bước 6:** Chọn <img src="https://docs.vngcloud.vn/download/thumbnails/73761209/image2024-3-14_10-53-48.png?version=1&#x26;modificationDate=1710388429000&#x26;api=v2" alt="" data-size="line">.

**Bước 7:** Chọn **Retry** để xác nhận chạy lại job.

{% hint style="info" %}
**Chú ý:**

* Khi thực hiện Retry, VNG Cloud DataSync sẽ chỉ transfer lại những file lỗi trước đó. Những file đã được di chuyển thành công trước đó sẽ không bị di chuyển lại.
* Bạn có thể thực hiện Retry nhiều lần tới khi nào tất cả file của bạn đã được transfer thành công. Tuy nhiên, nếu việc retry liên tục xảy ra lỗi, bạn nên kiểm tra lại cấu hình Transfer Job và nguồn dữ liệu.
{% endhint %}
