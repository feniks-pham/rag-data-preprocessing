# Transfer dữ liệu từ vStorage tới vStorage khác account

#### Tổng quan <a href="#transferdulieutuvstoragetoivstoragekhacaccount-tongquan" id="transferdulieutuvstoragetoivstoragekhacaccount-tongquan"></a>

Giả sử ban đầu tôi đang sử dụng account1 trên vStorage, nơi lưu trữ dữ liệu chính của tôi là region HCM03. Hiện tại tôi đã tạo một account2 tại region region HAN01 và tôi muốn chuyển dữ liệu này về region HAN01 để việc truy xuất dữ liệu hiệu quả hơn. Việc dữ liệu sẽ diễn ra một lần theo thời điểm tôi nhấn chạy Transfer Job.&#x20;

* **Source** information: vStorage
  * Account: account01
  * Region: HCM03
  * Endpoint: [https://hcm03.vstorage.vngcloud.vn](https://hcm03.vstorage.vngcloud.vn/)
  * Project: project01
  * Bucket: container01
  * Access key: accesskeysource
  * Secret key: secretkeysource
* **Destination** information: vStorage
  * Account: account02
  * Region: HAN01
  * Endpoint: [https://han01.vstorage.vngcloud.vn](https://han01.vstorage.vngcloud.vn/)
  * Project: project02
  * Bucket: container02
  * Folder path: backup/fromregionhcm03
  * Access key: accesskeydestination
  * Secret key: secretkeydestination

***

#### Điều kiện cần <a href="#transferdulieutuvstoragetoivstoragekhacaccount-dieukiencan" id="transferdulieutuvstoragetoivstoragekhacaccount-dieukiencan"></a>

Để đảm bảo việc transfer dữ liệu thành công, bạn cần đảm bảo các thông tin Source và Destination hợp lệ, trong đó:&#x20;

* **Access key và Secret key** tại Source phải có tối thiểu quyền đọc dữ liệu.
* **Access key và Secret key** tại Destination phải có tối thiểu quyền đọc và ghi dữ liệu.

***

#### Tạo Transfer Job <a href="#transferdulieutuvstoragetoivstoragekhacaccount-taotransferjob" id="transferdulieutuvstoragetoivstoragekhacaccount-taotransferjob"></a>

**Bước 1:** Đăng nhập vào [https://datasync.console.vngcloud.vn/](https://datasync.console.vngcloud.vn/). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [đây](https://register.vngcloud.vn/signup). **Lưu ý: bạn cần đăng nhập với account02 để có thể transfer dữ liệu từ account01 sang account02.**

**Bước 2:** Nhấp vào nút **Create a transfer job** để bắt đầu tạo job chuyển đổi dữ liệu.

**Bước 3:** Nhập **Basic configuration,** bao gồm:&#x20;

1. Nhập **Job name.**
2. Chọn **Source Type** là S3 compatible object storage.

**Bước 4:** Nhập **Source configuration**, bao gồm:&#x20;

* Nhập **Region**: HCM03.
* Nhập **Bucket**: container01.
* Nhập **Endpoint**: [https://hcm03.vstorage.vngcloud.vn](https://hcm03.vstorage.vngcloud.vn/)
* Nhập **Access Key:** accesskeysource
* Nhập **Secret Key:** secretkeysource
* Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 5:** Nhập **Destination configuration**, bao gồm:

* Chọn **Region**: HAN01.
* Chọn **Project**: project02.
* Chọn **Container**: container02.
* Chọn **Folder**: backup/fromregionhcm03
* Nhập **Access key**: accesskeydestination
* Nhập **Secret key**: secretkeydestination
* Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 7:** Chọn **Create Transfer Job.**

**Bước 8:** Tại thời điểm bạn mong muốn, chọn **Run** job.
