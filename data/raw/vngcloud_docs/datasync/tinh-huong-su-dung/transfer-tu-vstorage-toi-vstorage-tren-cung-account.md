# Transfer từ vStorage tới vStorage trên cùng account

#### Tổng quan <a href="#transferdulieutuvstoragetoivstoragetrencungaccount-tongquan" id="transferdulieutuvstoragetoivstoragetrencungaccount-tongquan"></a>

Giả sử tôi đang sử dụng vStorage, nơi lưu trữ dữ liệu chính của tôi là region HCM03. Do các dữ liệu này quan trọng nên tôi cần backup dữ liệu này từ region HCM03 về một project khác trên region HAN01 trên cùng account của tôi. Việc transfer dữ liệu sẽ diễn ra mỗi tháng trong năm vào lúc 09:30 AM từ ngày 01/01/2024 đến 31/12/2024, log sẽ được lưu tại log project "Mylogproject", thông báo khi chạy transfer job thành công được gửi tới [example@gmail.com](mailto:example@gmail.com)[.](mailto:myemail@gmail.com.) Chi tiết:&#x20;

* **Source** information: vStorage
  * Region: HCM03
  * Endpoint: [https://hcm03.vstorage.vngcloud.vn](https://hcm03.vstorage.vngcloud.vn/)
  * Project: project01
  * Bucket: container01
  * Access key: accesskeysource
  * Secret key: secretkeysource
* **Destination** information: vStorage
  * Region: HAN01
  * Endpoint: [https://han01.vstorage.vngcloud.vn](https://han01.vstorage.vngcloud.vn/)
  * Project: project02
  * Bucket: container02
  * Folder path: backup/fromregionhcm03
  * Access key: accesskeydestination
  * Secret key: secretkeydestination
* **Run**: Daily on 09:00 AM từ 01/01/2024 đến 31/12/2024
* **Email** **notification**: [example@gmail.com](mailto:example@gmail.com).

***

#### Điều kiện cần <a href="#transferdulieutuvstoragetoivstoragetrencungaccount-dieukiencan" id="transferdulieutuvstoragetoivstoragetrencungaccount-dieukiencan"></a>

Để đảm bảo việc transfer dữ liệu thành công, bạn cần đảm bảo các thông tin Source và Destination hợp lệ, trong đó:&#x20;

* **Access key và Secret key** tại Source phải có tối thiểu quyền đọc dữ liệu.
* **Access key và Secret key** tại Destination phải có tối thiểu quyền đọc và ghi dữ liệu.

***

#### Tạo Transfer Job <a href="#transferdulieutuvstoragetoivstoragetrencungaccount-taotransferjob" id="transferdulieutuvstoragetoivstoragetrencungaccount-taotransferjob"></a>

**Bước 1:** Đăng nhập vào [https://datasync.console.vngcloud.vn/](https://datasync.console.vngcloud.vn/). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [đây](https://register.vngcloud.vn/signup).

**Bước 2:** Nhấp vào nút **Create a transfer job** để bắt đầu tạo job chuyển đổi dữ liệu.

**Bước 3:** Nhập **Basic configuration,** bao gồm:&#x20;

1. Nhập **Job name.**&#x56;í dụ: Transfercungaccount
2. Chọn **Source Type** là vStorage.

**Bước 4:** Nhập **Source configuration**, bao gồm:&#x20;

* Chọn **Region**: HCM03.
* Chọn **Project**: project01.
* Chọn **Container**: container01.
* Nhập **Access key**: accesskeysource.
* Nhập **Secret key**: secretkeysource
* Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 5:** Nhập **Destination configuration**, bao gồm:

* Chọn **Region**: HAN01.
* Chọn **Project**: project02.
* Chọn **Container**: container02.
* Chọn **Folder**: backup/fromregionhcm03
* Nhập **Access key**: accesskeydestination
* Nhập **Secret key**: secretkeydestination
* Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 6:** Nhập **Job condition**, bao gồm:

* Chọn **Run schedule (Chạy lập lịch):**
  * Chọn **Start date**: 01/01/2024 09:00
  * Chọn **End date**: 31/12/2024
  * Chọn **Period**: Monthly.
* Chọn **Notification Option.** Nhập [example@gmail.com](mailto:example@gmail.com) sau đó nhấn Add.

**Bước 7:** Chọn **Create Transfer Job.**
