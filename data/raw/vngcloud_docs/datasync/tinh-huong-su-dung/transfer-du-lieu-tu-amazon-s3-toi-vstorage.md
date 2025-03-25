# Transfer dữ liệu từ Amazon S3 tới vStorage

#### Tổng quan <a href="#transferdulieutuamazons3toivstorage.-tongquan" id="transferdulieutuamazons3toivstorage.-tongquan"></a>

Giả sử tôi đang sử dụng Amazon S3 làm nơi lưu trữ dữ liệu, hiện tại tôi cần chuyển dữ liệu này về vStorage. Việc transfer dữ liệu sẽ diễn ra mỗi ngày trong tuần vào lúc 09:30 AM từ ngày 01/01/2024 đến 10/01/2024, các object được transfer sẽ được gắn tag "froms3", thông báo khi chạy transfer job thành công được gửi tới [example@gmail.com](mailto:example@gmail.com)[.](mailto:myemail@gmail.com.) Chi tiết:&#x20;

* **Source** information: Amazon S3
  * Region: ap-southeast-1
  * Endpoint: https://[s3.amazonaws.com](http://s3.amazonaws.com/)
  * Bucket: bucket-source
  * Access key: accesskeysource
  * Secret key: secretkeysource
* **Destination** information: vStorage
  * Region: HCM03
  * Endpoint: [https://hcm03.vstorage.vngcloud.vn](https://hcm03.vstorage.vngcloud.vn/)
  * Project: project01
  * Bucket: container01
  * Access key: accesskeydestination
  * Secret key: secretkeydestination
* **Run**: Daily on 09:00 AM từ 01/01/2024 đến 10/01/2024
* **Tag**: fromS3
* **Email** **notification**: example@gmail.com.

***

#### Điều kiện cần <a href="#transferdulieutuamazons3toivstorage.-dieukiencan" id="transferdulieutuamazons3toivstorage.-dieukiencan"></a>

Để đảm bảo việc transfer dữ liệu thành công, bạn cần đảm bảo các thông tin Source và Destination hợp lệ, trong đó:&#x20;

* **Access key và Secret key** tại Source phải có tối thiểu quyền đọc dữ liệu.
* **Access key và Secret key** tại Destination phải có tối thiểu quyền đọc và ghi dữ liệu.

***

#### Tạo Transfer Job <a href="#transferdulieutuamazons3toivstorage.-taotransferjob" id="transferdulieutuamazons3toivstorage.-taotransferjob"></a>

**Bước 1:** Đăng nhập vào [https://datasync.console.vngcloud.vn/](https://datasync.console.vngcloud.vn/). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [đây](https://register.vngcloud.vn/signup).

**Bước 2:** Nhấp vào nút **Create a transfer job** để bắt đầu tạo job chuyển đổi dữ liệu.

**Bước 3:** Nhập **Basic configuration,** bao gồm:&#x20;

1. Nhập **Job name.**&#x56;í dụ: Transfer from S3
2. Chọn **Source Type** là Amazon S3.

**Bước 4:** Nhập **Source configuration**, bao gồm:&#x20;

* Chọn **Region:** ap-southeast-1.
* Nhập **Bucket**: bucket-source.
* Nhập **Access Key:** accesskeysource
* Nhập **Secret Key**: secretkeysource
* Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 5:** Nhập **Destination configuration**, bao gồm:

* Chọn **Region**: HCM03.
* Chọn **Project**: project01.
* Chọn **Container**: container01.
* Nhập **Access key**: accesskeydestination
* Nhập **Secret key**: secretkeydestination
* Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 6:** Nhập **Job condition**, bao gồm:

* Chọn **Advanced configuration.** Nhập froms3 sau đó chọn **Add.**
* Chọn **Run schedule (Chạy lập lịch):**
  * **Chọn Start date: 01/01/2024 09:00**
  * **Chọn End date: 10/01/2024**
  * **Chọn Period: Daily.**
* Chọn **Notification Option.** Nhập [example@gmail.com](mailto:example@gmail.com) sau đó nhấn Add.

**Bước 7:** Chọn **Create Transfer Job.**
