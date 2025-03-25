# Quản lý sao lưu MDS Instance (Backup)

Giao diện quản lý Backup cho bạn cái nhìn tổng quan về tất cả các bản Backup hiện có cũng như thông chi tiết cho từng bản Backup. Truy cập giao diện quản lý Backup tại đây: [https://vdb.console.vngcloud.vn/memorystore/backup](https://vdb.console.vngcloud.vn/memorystore/backup)\
Bạn có thể tạo mới bản **Manual Backup**, **Restore** (khôi phục lại một DB Instance mới dựa trên bản Backup), **Delete** (xóa bản Backup). Tham khảo các hướng dẫn dưới đây về các tính năng quản lý Backup

* [A. Sao lưu theo nhu cầu (On-demand backup hay Manual backup)](sao-luu-mds-instance.md#saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup)
* [B. Sao lưu tự động theo ngày (Auto-Daily Backup)](sao-luu-mds-instance.md#saoluumdsinstance-b.saoluutudongtheongay-auto-dailybackup)
* [C. Khôi phục MDS Instance từ bản Backup](sao-luu-mds-instance.md#saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup-1)
* [D. Xóa bản Backup](sao-luu-mds-instance.md#saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup-2)

### A. Sao lưu theo nhu cầu (On-demand backup hay Manual backup) <a href="#saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup" id="saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup"></a>

Khi bạn có nhu cầu tạo bản backup, bạn truy cập dịch vụ VNG Cloud và chọn đến màn hình quản lý backup. Màn hình này sẽ liệt kê tất cả các bản backup (manual & auto) của tất cả các DB Instance có trong tài khoản của bạn.

**Cách 1: Bạn nhấn vào nút Create Backup. Tại màn hình Create Backup, bạn lần lượt lựa chọn các thông tin sau**

* **Backup Name**: đặt tên cho bản backup này.
* **Database Instance Name**: chọn DB Instance mà bạn muốn thực hiện backup.
* **Backup Type**: với MemoryStore bạn có option thực hiện Full Backup.
* Sau khi chắc chắn mọi thông tin đều chính xác, bạn nhấn **Create**.
* Nếu hệ thống tiếp nhận thành công, một bản backup sẽ xuất hiện với **Status** là **NEW**. Khi được tạo thành công, bản backup sẽ đổi sang **Status** là **COMPLETED**.

**Cách 2: Ngoài màn hình quản lý Backup, bạn còn có thể tạo bản Manual Backup ngay tại màn hình quản lý Database.**&#x20;

* Nhấn chọn một DB Instance cần tạo Backup, khi đó bạn sẽ được chuyển tới trang chi tiết DB Instance.
* Tại đây, bạn chuyển tới thẻ **Backup** và cuộn xuống danh sách **Backup list**. Ở đây sẽ liệt kê tất cả các bản backup (manual & auto) tương ứng với DB Instance này. Bạn có thể nhấn **Create Backup** để tiến hành tạo bản **Manual Backup** ngay tại đây.
* Thao tác tiếp theo hoàn toàn tương tự như hướng dẫn ở cách 1.

### **B. Sao lưu tự động theo ngày (Auto-Daily Backup)** <a href="#saoluumdsinstance-b.saoluutudongtheongay-auto-dailybackup" id="saoluumdsinstance-b.saoluutudongtheongay-auto-dailybackup"></a>

vDBaaS hỗ trợ tính năng tự động sao lưu theo ngày tại thời điểm do bạn ấn định.

**Để xem một DB Instance đã được cấu hình tính năng này chưa, thao tác như sau:**

* Nhấn chọn một DB Instance cần kiểm tra, khi đó bạn sẽ được chuyển tới trang chi tiết DB Instance.
* Sau đó, chọn thẻ **Backup** và tìm đến mục **Backup Information**. Nếu **Automatic backup** là **Enabled** tức là bạn đã cấu hình tự động sao lưu hàng ngày cho DB Instance này vào thời điểm **Backup Time** trong ngày.

**Để cấu hình tính năng này, bạn có hai phương án:**

* Cách 1: Cấu hình luôn trong lúc khởi tạo DB Instance. Đối với phương án đầu, mời bạn xem lại hướng dẫn Khởi tạo DB Instance tại [Hướng dẫn khởi tạo MDS Instance](khoi-tao-mds-instance.md).
* Cách 2: Thay đổi tại giao diện quản lý Database.
  *   Bạn truy cập màn hình quản lý Database, click chọn DB Instance muốn cấu hình. Sau đó, bạn click chọn **Edit DB Setting**.&#x20;

      <figure><img src="../../.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt=""><figcaption></figcaption></figure>
  * Tại đây, bạn kéo xuống mục **Backup settings** và bạn có thể cấu hình các thông tin:
    * **Automatic daily backup:** bật tắt tính năng Automatic daily backup.
    * **Backup retention period:** xác định thời gian lưu trữ bản automatic backup. Nhằm giúp bạn tiết kiệm không gian lưu trữ, các bản automatic backup đã quá khoảng thời gian này sẽ bị xóa.
    * **Backup time:** thời điểm quá trình tạo automatic backup diễn ra. VNG Cloud khuyến nghị bạn chọn thời điểm này vào khoảng thời gian thấp điểm nhất đối với hệ thống của bạn.
  * Sau khi chắc chắn rằng các thông tin đã chính xác, bạn nhấn nút **Save** ở góc trên bên phải và chờ một lát để quá trình thay đổi được thực thi.

### C. Khôi phục MDS Instance từ bản Backup <a href="#saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup" id="saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup"></a>

vDB MemoryStore hỗ trợ bạn **khôi phục (Restore)** lại một MDS Instance mới từ bản sao lưu (Backup) trước đó. Quá trình khôi phục này không phụ thuộc vào cách tạo ra bản backup đó (Manual Backup hay Automactic Daily Backup).

Để thực hiện tiến trình khôi phục, bạn truy cập màn hình quản lý Backup [tại đây](https://vdb.console.vngcloud.vn/memorystore/backup) và làm theo hướng dẫn sau:&#x20;

*   Nhấn chọn vào bản Backup mà bạn muốn khôi phục, chọn Action **Restore**. Quá trình Restore cũng gần tương tự như quá trình Tạo một MDS Instance mới.&#x20;

    <figure><img src="../../.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt=""><figcaption></figcaption></figure>
* Tại màn hình khôi phục MDS Instance, bạn cũng có thể lựa chọn các thông tin về cấu hình MDS Instance mới tại các thông tin **Instance flavor, DB instance setting, Network & Security, DB Option và Backup setting.**
* Sau khi chắc chắn các thông tin đã chính xác, bạn nhấp nút **Restore** ở góc phải trên.
* Sau đó, bạn quay lại màn hình quản lý Database, sẽ thấy xuất hiện một MDS Instance đang được khởi tạo. Trạng trái của MDS Instance mới này cũng sẽ thay đổi từ **Building/Build** sang **Active** nếu thành công.

### D. Xóa bản Backup <a href="#saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup" id="saoluumdsinstance-a.saoluutheonhucau-on-demandbackuphaymanualbackup"></a>
