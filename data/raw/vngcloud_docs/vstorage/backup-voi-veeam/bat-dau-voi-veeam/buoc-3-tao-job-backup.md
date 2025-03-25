# Bước 3: Tạo Job backup

Sau khi đã <mark style="color:blue;">Khởi tạo Repository,</mark> bạn sẽ thực hiện việc tạo job tự động backup dữ liệu về vStorage, việc tạo job backup có thể cho phép bạn thiết lập job định kỳ tự động sao lưu tới nơi lưu trữ (repository). Nếu tạo job chạy trên Scale-out Repository thì điều đó có nghĩa chỉ cần chạy job thì có thể backup được nhiều nơi.

### Thực hiện Tạo Job Backup theo những bước sau:

1. Tại mục "Inventory", chọn "**Backup Job**", chọn loại computer phù hợp;
2. Tại màn hình "Job Mode", nhấn "**Next**";
3. Tại màn hình "Nam&#x65;**"**, bạn có thể đặt tên cho Job, sau đó nhấn "**Next".**
4. Tại màn hình "Compute&#x72;**"**, chọn computer muốn sao lưu, sau đó nhấn "**Next"**.
5. Tại màn hình "Backup Mod&#x65;**"**,  chọn mode sau đó nhấn "**Next**"; \
   \- Chọn mode: "**Entire Computer**" để sao lưu toàn bộ máy tính, nếu chọn mode này có thể bỏ qua bước 6.\
   \- Chọn mode: "**File level backup (slower)**" để sao lưu file hoặc folder được chọn, nếu chọn mode này thì đi tiếp bước 6.
6. Tại màn hình "Object", chọn đối tượng cần sao lưu, sau đó nhấn "**Next**";
7. Tại màn hình "Storage", chọn Repository, sau đó nhấn "**Next**";
8. Tại màn hình "Guest Processing", bỏ tất cả tùy chọn, sau đó nhấn "**Next**";
9. Tại màn hình "Schedule", bạn có thể cài đặt lịch sao lưu định kỳ, sau đó nhấn "**Apply**";
10. Tại màn hình "Summary", nếu bạn chọn "Run the job when I click Finish" để chạy sao lưu khi tạo Job thành công, sau đó nhấn "**Finish**" để hệ thống tạo job và chạy job đồng bộ.

***

### Video hướng dẫn cài đặt&#x20;

Đang cập nhật.

***

### Ví dụ hướng dẫn Tạo Job với Phiên bản Veeam Backup & Replication 12

**Bước 1**: Người dùng vào mục **Inventory**, người dùng chọn Object - Computer (hạ tầng muốn backup), ở hướng dẫn này localhost là Object cần backup, sau đó nhấn chuột phải vào Object để chọn "Add to backup job" và nhấn "**New Job**".

<figure><img src="../../../.gitbook/assets/image (359).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 2**: Giao diện tạo **New Agent Backup Job** hiện ra, tại tab **Job Mode**, người dùng chọn Mode " **Managed by backup server**", sau đó nhấn **Next**.

<figure><img src="../../../.gitbook/assets/image (360).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 3:** Tại tab **Name**, người dùng đặt tên cho Job, sau đó nhấn **Next.**

<figure><img src="../../../.gitbook/assets/image (361).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 4**:  Tại tab **Computer**, người dùng có thể chọn computer muốn thực hiện backup.Sau đó nhấn **Next**.

<figure><img src="../../../.gitbook/assets/image (362).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 5**: Tại tab **Backup Mode**, người dùng chọn mode "**File level backup (slower)**" để backup chỉ những file hay folder được chọn, còn nếu back up toàn bộ computer thì chọn mode "Entire computer". Sau đó nhấn **Next**.

<figure><img src="../../../.gitbook/assets/image (364).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 6**: Nếu chọn mode "File level backup (slower)" ở bước 5 thì tab **Object** hiện ra để chọn đối tượng cần backup, người dùng chọn tùy chọn "**The following file system objects:**", sau đó ấn "Add" điền đường dẫn folder muốn backup, sau đó nhấn "OK" và cuối cùng nhấn **Next**.

\*Nếu bước 5 chọn mode "Entire computer", thì bỏ qua bước 6 này.&#x20;

<figure><img src="../../../.gitbook/assets/image (365).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 7:** Tại tab **Storage**, người dùng chọn **Backup Repository** đã tạo trước đó, sau đó nhấn **Next**. Hệ thống sẽ kiểm tra file backup.&#x20;

<figure><img src="../../../.gitbook/assets/image (366).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 8**: Sau khi hệ thống kiểm tra xong thì điều hướng đến tới tab **Guest Processing**, người dùng **bỏ tùy chọn đầu tiên "Enable application-aware processing"**. Nếu người dùng muốn đảm bảo sao lưu nhất quán cho các ứng dụng chạy máy chủ ảo bằng các tương tác với chúng và sử dụng Microsoft VSS ,thì có thể vẫn bật thì Veeam sẽ phải thực hiện các tác vụ trước và sau khi sao lưu.&#x20;

Sau đó nhấn **Next**.

<figure><img src="../../../.gitbook/assets/image (368).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 9**: Tại tab **Schedule**, người dùng có thể cài đặt lịch tự động chạy job tự động, nếu chạy bằng tay thì nhấn **Next**.

<figure><img src="../../../.gitbook/assets/image (369).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 10:** Tại tab Summary, người dùng có thể thấy tổng kết thông tin của Job sẽ tạo, chọn "**Run the job when I click Finish**" sau đó nhấn **Finish** để hệ thống bắt đầu tạo Job.

<figure><img src="../../../.gitbook/assets/image (370).png" alt="" width="563"><figcaption></figcaption></figure>

**Bước 11:** Sau khi job được tạo xong, người dùng có thể kiểm tra bằng cách: vào mục Home, chọn Jobs/Backup, chọn Job đã tạo nếu thấy status là Success thì job đã tạo, người dùng có thể thực hiện backup.

<figure><img src="../../../.gitbook/assets/image (371).png" alt="" width="563"><figcaption></figcaption></figure>

Hoàn tất quá trình tạo Job để backup dữ liệu.
