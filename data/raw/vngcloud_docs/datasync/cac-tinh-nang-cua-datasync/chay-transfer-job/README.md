# Chạy Transfer Job

Sau khi tạo một Transfer Job, bạn có thể bắt đầu chạy task để transfer dữ liệu. Mỗi lần chạy của một transfer job được gọi là một task.&#x20;

**Để chạy Transfer Job, hãy làm theo hướng dẫn:**

**Bước 1:** Truy cập vào [https://datasync.console.vngcloud.vn/](https://datasync.console.vngcloud.vn/transfer-job/list)

**Bước 2:** Tại menu bên trái, chọn mục **Transfer Job**.&#x20;

**Bước 3:** Trên danh sách các transfer job đã tạo, hãy chọn một **Transfer Job** mà bạn muốn chạy.&#x20;

**Bước 4:** Chọn biểu tượng <img src="http://docs.vngcloud.vn/download/thumbnails/73761189/image2024-3-14_10-4-28.png?version=1&#x26;modificationDate=1710385469000&#x26;api=v2" alt="" data-size="line"> hoặc chọn biểu tượng <img src="http://docs.vngcloud.vn/download/thumbnails/73761189/image2024-3-14_10-4-58.png?version=1&#x26;modificationDate=1710385499000&#x26;api=v2" alt="" data-size="line">sau đó chọn hành động <img src="http://docs.vngcloud.vn/download/thumbnails/73761189/image2024-3-14_10-5-14.png?version=1&#x26;modificationDate=1710385515000&#x26;api=v2" alt="" data-size="line">

Lúc này bạn có thể chọn vào **transfer job** đó để xem chi tiết về thông số của transfer job khi chạy. Chi tiết tham khảo tại [Theo dõi kết quả chạy Transfer Job](../theo-doi-ket-qua-chay-transfer-job.md)

{% hint style="info" %}
**Chú ý:**

* Để đảm bảo việc transfer dữ liệu thành công, bạn cần đảm bảo các thông tin Source và Destination hợp lệ, trong đó:&#x20;
  * **Access key và Secret key** tại Source phải có tối thiểu quyền đọc dữ liệu.
  * **Access key và Secret key** tại Destination phải có tối thiểu quyền đọc và ghi dữ liệu.
* Việc transfer một lượng lớn dữ liệu trong một lần chạy transfer job có thể gây ảnh hưởng đến hiệu suất và thời gian thực hiện transfer job. Để tăng tốc độ cũng như cải thiện độ ổn định của hệ thống, chúng tôi khuyến cáo bạn nên chia nhỏ tập dữ liệu thông qua tính năng **Data Filtering** (Filter Include Prefix, Filter Exclude Prefix) đầu vào giúp giảm tải hệ thống và đẩy nhanh quá trình di chuyển dữ liệu. Giả sử bạn có một transfer job transfer 100GB dữ liệu từ Amazon S3 sang vStorage. Việc transfer có thể mất nhiều thời gian và ảnh hưởng đến hệ thống. Bạn có thể chia nhỏ dữ liệu thành 10 phần, mỗi phần 10GB. Sau đó, sử dụng tính năng Data Filtering để transfer từng phần dữ liệu riêng lẻ.&#x20;
{% endhint %}

\
