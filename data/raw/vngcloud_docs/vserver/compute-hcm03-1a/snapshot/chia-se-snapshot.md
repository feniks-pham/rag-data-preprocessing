# Chia sẻ Snapshot

Với VNG Cloud, User có thể **Chia sẻ Snapshot** (Share Snapshot) với các tài khoản VNG Cloud khác. Những tài khoản VNG Cloud khác có thể sử dụng Snapshot được chia sẻ để tạo nhanh VM để đáp ứng nhu cầu. Bài viết này sẽ mô tả làm thế nào để Share Snapshot và làm thế nào để ngừng Share Snapshot.

**Lưu ý**

Trước khi chia sẻ một snapshot, cần lưu ý một số vấn đề sau:

* Chức năng thực hiện chia sẻ Snapshot là **hoàn toàn miễn phí**;
* User chỉ **trả phí theo dung lượng** khi tạo tài nguyên từ file snapshot đã chia sẻ;
* File Snapshot chỉ được **chia sẻ cho những tài khoản của VNG Cloud**;
* User có thể được chia sẻ một file snapshot cho **tối đa 64 tài khoản** VNG Cloud;
* Mỗi User có thể được chia sẻ **tối đa 1024 file Snapshot**.

## **Các bước chuẩn bị** <a href="#chiasesnapshot-cacbuocchuanbi" id="chiasesnapshot-cacbuocchuanbi"></a>

***

* Phải có file Snapshot tạo sẳn trước đó . vui lòng tham khảo cách [Kích hoạt Snapshot](kich-hoat-snapshot.md) và [Tạo snapshot](tao-snapshot.md) trước,
* File snapshot muốn sẻ nên đảm bảo không bao gồm các nội dung và tài liệu nhạy cảm.
* Cần yêu cầu User được chia sẻ file Snapshot cung cấp mã ID và Email của tài khoản VNG Cloud.
* Để lấy có được mã ID và Email của User được chia sẻ, thì tại thanh _**Account menu**_, User sẽ thấy thông tin _**Account ID và Account Email**_ (xem hình minh họa ở bên dưới), cung cấp thông tin này cho User muốn chia sẻ file Snapshot.

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761438/image2024-3-25_15-32-8.png?version=1&#x26;modificationDate=1711355529000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Đối với User chia sẽ cần biết trường những thống tin sau: Account ID & Account Email, User Project ID, Snapshot Server ID;
  * Thông tin **Account ID và Account Email** có thể xem ở Account menu giống user được chia sẻ Snapshot.
  * Thông tin **User Project ID**: lấy từ mục Limit;
  * Thông tin **Snapshot Server ID**: lấy từ mục Snapshot/ file Snapshot Server muốn share.

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761438/image2024-3-25_16-5-12.png?version=1&#x26;modificationDate=1711357513000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761438/image2024-3-25_15-46-29.png?version=1&#x26;modificationDate=1711356390000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

## **Thực hiện Chia sẻ Snapshot** <a href="#chiasesnapshot-thuchienchiasesnapshot" id="chiasesnapshot-thuchienchiasesnapshot"></a>

***

* Bước 1: Đăng nhập vào tài khoản VNG Cloud / chọn Sản phẩm **vServer**;
* Bước 2: Chọn mục **Snapshots / Snapshot**: User xem được giao diện Snapshot;
* Bước 3: Chọn **Action** của một file Snapshot đã tạo sẳn trước đó;
* Bước 4: Chọn "**Chia sẻ Snapshot**";
* Bước 5: Một pop-up hiển thị thông báo về "Chia sẻ Snapshot Server" Chọn vào link "_**Liên hệ Dịch vụ chăm sóc khách hàng**_";
* Bước 6: Điều hướng đến màn hình **VNG Cloud Help Desk:**
  * User nhấn chọn "**Add Ticket**" để đến giao diện "**Submit a ticket**" ;
  * Điền các trường với yêu cầu Share file Snapshot và cung cấp đủ các thông tin cần thiết để admin xử lý:
    * Account ID của user share;
    * Account Email của user share;
    * User Project ID của user share;
    * Snapshot Server ID của user share;
    * Account ID của user được share;
    * Account Email của user được share;&#x20;
  * Sau đó nhấn "**Submit**" để gửi đến hệ thống VNG Cloud để xử lý.
* Bước 7: Sau khi VNG Cloud xử lý thành công, khi vào lại danh sách Snapshot thì tại file Snapshot yêu cầu chia sẻ, nếu user thấy tại cột "**Chia sẻ với**" (Share to)  có hiển thị thông tin tài khoản user chia sẻ (Owner) và user được chia sẻ, Bên cạnh đó sẽ có email thông báo cho tài khoản được chia sẻ đã nhận file snapshot thành công.

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761438/image2024-3-22_13-15-47.png?version=1&#x26;modificationDate=1711088148000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761438/image2024-3-22_13-17-52.png?version=1&#x26;modificationDate=1711088273000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761438/image2024-3-22_13-42-2.png?version=1&#x26;modificationDate=1711089723000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

## **Thực hiện Ngừng Chia sẻ Snapshot** <a href="#chiasesnapshot-thuchienngungchiasesnapshot" id="chiasesnapshot-thuchienngungchiasesnapshot"></a>

***

* Bước 1: Đăng nhập vào tài khoản VNG Cloud / chọn Sản phẩm **vServer**;
* Bước 2: Chọn mục **Snapshots / Snapshot**: User xem được giao diện Snapshot;
* Bước 3: Tại file Snapshot muốn ngừng chia sẻ, ở cột "**Chia sẻ với**" (Share to), User click chọn vào icon Account VNG cloud;
* Bước 4: Hiển thị danh sách các Account được chia sẻ file Snapshot, user quản lý file snapshot (Owner) có quyền click vào nút "**Gỡ bỏ**" (Remove) để ngừng chia sẻ file snapshot;
* Bước 5: **Xác nhận** để hoàn tất việc ngừng chia sẻ file snapshot./.

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761438/image2024-3-22_14-53-2.png?version=1&#x26;modificationDate=1711093983000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
