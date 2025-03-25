# API Test với Ping

API Ping tests cho phép bạn gửi ICMP packet tới server hay các thiết bị của bạn, cho phép bạn theo dõi tính sẵn sàng của server hay các thiết bị và chuẩn đoán về các sự cố về mạng.

**Để thực hiện tạo API Test với phương thức Ping, hãy làm theo hướng dẫn bên dưới:**

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Synthetic test.**
3. Chọn **API test.**
4. Chọn **Create an API test.**
5. Nhập các thông tin bao gồm:

* **Test Information: định nghĩa các thông tin cơ bản, chọn Ping method và chỉ định hostname cần kiểm tra**
  * **Test name:** tên của API test
  * **Test type**: giao thức kiểm tra, bạn chọn Ping
  * **Hostname:** lựa chọn server hay thiết bị bạn cần kiểm tra, có thể là tên miền hay địa chỉ IP

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59803717/image2022-8-29_17-11-57.png?version=1&#x26;modificationDate=1686544467000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Sau khi điền các Test Information bạn có thể chọn **Run Test hoặc Test Again** nếu bạn đã Test trước đó để kiểm tra, bạn có thể thấy các thông tin trả về như Ping có thành công hay không, tỉ lệ packet loss hay packet latency

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59803717/image2022-8-29_17-13-38.png?version=1&#x26;modificationDate=1686544467000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Test Assertion**
  * Assertion định nghĩa những gì bạn kì vọng về kết quả API Test, nếu kết quả trả về thoả những gì bạn định nghĩa API Test sẽ thể hiện hostname bạn đang kiểm tra là thành công, và ngược lại API Test sẽ thể hiện hostname bạn đang kiểm tra là thất bại. Hệ thống sẽ tự động thêm Assertion status code cho bạn sau khi bạn Run test, bạn cần định nghĩa ít nhất một Assertion cho API test

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59803717/image2022-8-29_17-19-32.png?version=1&#x26;modificationDate=1686544468000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


* **Location**&#x20;
  * Lựa chọn Location mà ở đó sẽ chạy các Ping Test tới hostname của bạn. Ping tests có thể chạy từ cả Public Locations (do VNG Cloud quản lý) và Private Locations (do khách hàng tự cài đặt và quản lý) dựa trên nhu cầu của bạn cho việc chạy test từ bên ngoài (internet) hay bên trong mạng của bạn. Public Locations do VNG Cloud quản lý hiện tại có 2 locations là HCM và HN.

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59803717/image2022-8-29_16-42-28.png?version=1&#x26;modificationDate=1686544468000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Alarm conditions:** Thiết lập điều kiện cảnh báo để xác định các trường hợp mà bạn muốn kiểm tra không thành công và kích hoạt cảnh báo.
  * **Interval**: bao lâu API Test sẽ kiểm tra một lần, mặc định sẽ là 1p
  * **Time of failure**: bao nhiêu lần thất bại liên tiếp sẽ cảnh báo
  * **Locations with failure**: bao nhiêu location thất bại mới cảnh báo
  * Ví dụ khi bạn chọn Time of failure: 1 và Locations with failure: 2, sẽ được hiểu là: bạn sẽ được cảnh báo nếu Test thất bại 1 lần liên tiếp từ 2 trên 2 locations.
  * **Notifications**: bạn chọn các kênh thông báo khi chuyển qua các trạng thái In-alarm, Up hay Undertermine, Hệ thống sẽ thông báo theo danh sách này.

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59803717/image2022-8-29_16-51-21.png?version=1&#x26;modificationDate=1686544468000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


6\. Sau đó nhấn nút "**Create**" để khởi tạo API test. Sau khi tạo xong bạn sẽ thấy API test đang ở trạng thái Undertermine, cho đến khi inteval tiếp theo API Test sẽ được cập nhập trạng thái chính xác

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59803717/image2022-8-29_17-24-38.png?version=1&#x26;modificationDate=1686544468000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* API Test đã chuyển thành trạng thái Up khi hostname đang hoạt động bình thường

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59803717/image2022-8-29_17-26-16.png?version=1&#x26;modificationDate=1686544468000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
