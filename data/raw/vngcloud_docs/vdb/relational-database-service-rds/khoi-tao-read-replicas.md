# Khởi tạo Read Replicas

Nhằm mở rộng khả năng read scale cho vDB, bạn có thể tạo read replicas cho các DB Instance, hệ thống sẽ tự động thiết lập mô hình master, slave và đồng bộ dữ liệu với cơ chế async.

Bạn tham khảo videos sau:

{% embed url="https://youtu.be/xGVEQvChdJo" %}

chi tiết các bước làm như sau:

Đầu tiên bạn chọn DB Instance cần tạo read replicas từ đó, lưu ý chỉ những DB Instance có role:standalone hoặc role:master mới khởi tạo đc read replicas, chọn **Action** và chọn **Create Read Replica**&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_15-51-20.png?version=1&#x26;modificationDate=1623660681000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Ở đây bạn chỉ cần đặt **DB Instance Name** cho read replicas và giữ nguyên các thông tin khác như: flavor, storage type, storage size, backup schedule, tuy nhiên chúng tôi khuyến cáo bạn giữ nguyên các thông tin này giống Master hoặc chọn các thông số cao hơn khi cần thiết. Nhấn **Create** để khởi tạo:

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_15-56-10.png?version=1&#x26;modificationDate=1623660971000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Sau khi khởi tạo bạn chờ một khoảng thời gian cho đến khi read replicas đã **ACTIVE**

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_16-3-30.png?version=1&#x26;modificationDate=1623661411000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Vây là bạn đã tạo thành công Read Replica cho vDB hay còn gọi là mô hình master-slave, bạn có thể kiểm tra dữ liệu của master đã được đồng bộ qua slave:

* Tại dbmaster với IP: 103.245.249.88 bạn thấy chúng ta có 6 databases, và với database vngtest chúng ta có 1 table và 1 record

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_16-7-30.png?version=1&#x26;modificationDate=1623661651000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Tại dbslave1 với IP: 61.28.229.96, bạn thấy dữ liệu đã được đồng bộ chính xác từ dbmaster sang dbslave1

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_16-8-57.png?version=1&#x26;modificationDate=1623661739000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Tại dbmaster bạn ghi thêm dữ liệu vào bảng authors tại db: vngtest.

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_16-12-44.png?version=1&#x26;modificationDate=1623661965000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Bạn cũng sẽ thấy dữ liệu đã được đồng bộ qua dbslave1

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_16-15-55.png?version=1&#x26;modificationDate=1623662155000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Ngoài ra bạn không thể ghi dữ liệu lên các read replicas, ở đây là dbslave1 vì ở các read replicas đều được cấu hình với cờ read\_only=true.

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555982/image2021-6-14_16-15-15.png?version=1&#x26;modificationDate=1623662116000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Chúc mừng bạn đã cấu hình read replicas thành công
