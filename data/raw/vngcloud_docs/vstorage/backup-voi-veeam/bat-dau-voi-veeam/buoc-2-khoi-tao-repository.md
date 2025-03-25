# Bước 2: Khởi tạo Repository

Trước khi thực hiện backup, bạn phải thực hiện tạo nơi lưu trữ (Repository) là nơi mà toàn bộ dữ liệu mà bạn muốn lưu giữ lại một cách an toàn. Sau đây là những hướng dẫn để thực hiện Khởi tạo Repository.&#x20;

Bên cạnh đó Veeam cung cấp chức năng là Scale-out Repository, có thể hiểu là tạo Group Repository, giúp bạn có thể sao lưu dữ liệu tới nhiều nơi cùng một lúc, đảm bảo tính sẵn sàng cao khi khắc phục sự cố.

### Thực hiện Khởi tạo Backup Repository theo những bước sau:

1. Mở phần mềm Veeam Backup & Repository, điền thông tin truy cập và nhấn "C**onnect**";
2. Tại "Backup In**fr**astructure", chọn mục "**Backup Repositories**", nhấn nút "**Add Repository**" ;
3. Hiện giao diện "Add Backup Repository", chọn  "**Object storage**";
4. Chọn "**S3 Compatible**";
5. Hiện giao diện "New Object Storage Reposity", bạn đặt tên vào mục Name và sau đó nhấn "**Next**";
6. Tại bước "Account", bạn điền **Service Point, Region, Credentials** (với Access key và Secret key), sau đó nhấn "**Next**";
7. Tại bước "Bucket", bạn **chọn Bucket và folder** sẽ backup dữ liệu đến. Sau đó nhấn "**Next**";

{% hint style="info" %}
**Quan trọng về Immutable**&#x20;

* Bạn cần chọn vào mục: "<mark style="color:red;">**Make recent backups immutable for (30) days**</mark>";
* Để bảo vệ các bản sao lưu khỏi sự thay đổi hay xóa bỏ người dùng khác hoặc ransomware hoặc tin tặc. Các bản sao lưu được đặt ở trạng thái không thể thay đổi (Immutable) trong suốt thời gian cài đặt này.
{% endhint %}

8. Tại bước "Mount Server", nhấn "**Next**";
9. Tại bước "Review", nhấn "**Apply**". Hệ thống sẽ xử lý tạo Repository;
10. Nhấn "**Finish**" để kết thúc quá trình tạo Repository.

***

### Thực hiện Khởi tạo Scale-out Repository theo những bước sau:

1. Mở phần mềm Veeam Backup & Repository, điền thông tin truy cập và nhấn "**Connect**";
2. Tại "Backup Infrastructure", chọn mục "**Scale-out Repositories**", nhấn chuột phải chọn "**Add Scale-out backup Repository**" ;
3. Hiện giao diện "New Scale-out Backup Repository", bạn đặt tên cho Repository, sau đó nhấn "**Next**";
4. Chọn "**Add**" để chọn các Backup Repository (đã tạo) muốn đưa vào Group Repositories;

{% hint style="info" %}
**Lưu ý**

Các Repository phải có cấu hình Immutable giống nhau và cùng loại Object Storage.
{% endhint %}

5. Tại "Capacity Tier", bạn tiếp tục nhấn "Apply". Hệ thống sẽ xử lý tạo Repository;
6. Nhấn "**Finish**" khi tạo thành công.

***

### Video hướng dẫn cài đặt&#x20;

Đang cập nhật.

***

### Ví dụ hướng dẫn Tạo Backup Repository với phiên bản Veeam Backup & Replication 12



**Bước 1:** Truy cập sử dụng phần mềm

<figure><img src="../../../.gitbook/assets/image (347).png" alt="" width="342"><figcaption></figcaption></figure>

**Bước 2:** Chọn mục "**Backup Infrastructure**", sau đó chọn mục "**Backup Repositories**", Nhấn nút "**Add Repository**" để bắt đầu cài Repositoty:

<figure><img src="../../../.gitbook/assets/image (348).png" alt="" width="477"><figcaption></figcaption></figure>

**Bước 3:** Tại màn hình Add Backup Repository, chọn tùy chọn "**Object storage**".

<figure><img src="../../../.gitbook/assets/image (349).png" alt="" width="423"><figcaption></figcaption></figure>

**Bước 4:** Tại màn hình Object Storage, chọn tùy chọn "**S3 Compatible**" hoặc chọn lựa chọn đối tượng phú hợp muốn backup.

<figure><img src="../../../.gitbook/assets/image (350).png" alt="" width="430"><figcaption></figcaption></figure>

**Bước 5:** Điều hướng đến màn hình "New Object Storage Reposity" để bắt đầu tạo Repository (nơi backup dữ liệu). Tại bước "**Name**", người dùng đặt tên và viết mô tả cho Repository. Sau đó nhấn "N**ext**"

<figure><img src="../../../.gitbook/assets/image (351).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 6:** Tại bước "**Account**", người dùng điền thông tin vào các mục sau đây và ấn "Next":

* Service Point: **https://hcm03-encrypt-vstorage.vngcloud.vn**
* Region: **HCM03**
* Credentials: nhấn "Add" để nhập "**Access key**" và "**Secret key**" . Để tạo key, có thể khảo bài hướng dẫn [<mark style="color:blue;">**Khởi tạo S3 key**</mark>](../../object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-s3-key.md).

<figure><img src="../../../.gitbook/assets/image (352).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 7:** Tại bước "**Bucket**", người dùng chọn Container đã tạo trước trên vStorage (xem hướng dẫn tạo Container ở [<mark style="color:blue;">**đây**</mark>](../../object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-container/khoi-tao-container.md)). Đồng thời người dùng **chọn** hoặc **tạo mới folder** để lưu trữ dữ liệu backup vào folder đó. Sau đó nhấn "Next".

<figure><img src="../../../.gitbook/assets/image (353).png" alt="" width="563"><figcaption></figcaption></figure>

**Lưu ý**: Người dùng cần chọn vào mục: "Make recent backups <mark style="color:red;">**immutable**</mark> for 30 days" . Vì với tùy chọn này giúp bảo vệ bản sao khỏi những rủi ro và ngăn chặn sửa đổi hoặc xóa bản sao lưu trong một khoảng thời gian nhất định, đảm bảo luôn có sẵn bản sao lưu sạch để khôi phục hệ thống trong trường hợp bị tấn công hoặc sự cố.

<figure><img src="../../../.gitbook/assets/image (354).png" alt="" width="464"><figcaption></figcaption></figure>

**Bước 8:** Tại màn hình "**Mount Server**", người dùng có thể chọn máy chủ cần backup dữ liệu, sau đó nhấn "**Next**".

<figure><img src="../../../.gitbook/assets/image (355).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 9:** Người dùng tiếp tục nhấn "**Apply**" tại màn hình Review

<figure><img src="../../../.gitbook/assets/image (356).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 10:** Sau khi nhấn "**Apply**" thì hệ thống sẽ tiến hành xử lý tạo Repository&#x20;

<figure><img src="../../../.gitbook/assets/image (357).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 11:** Khi hoàn tất thì người dùng nhấn "**Finish**".

<figure><img src="../../../.gitbook/assets/image (358).png" alt="" width="563"><figcaption></figcaption></figure>

Sau khi kết thúc quá trình tạo Repository.
