# Bắt đầu với Synthetic

### Bước 1: Khởi tạo Synthetic Test quota <a href="#batdauvoisynthetics-buoc1-khoitaosynthetictestquota" id="batdauvoisynthetics-buoc1-khoitaosynthetictestquota"></a>

Bắt đầu sử dụng dịch vụ, bạn cần tạo một Synthetic Test quota. Một Synthetic Test quota là một thuật ngữ trên vMonitor Platform thể hiện một gói giám sát vận hành với số lượng bài kiểm tra cụ thể mà bạn thực hiện mua trên VNG Cloud. Tại một thời điểm bạn có thể sở hữu một Synthetic Test quota và sử dụng chúng để kiểm tra hoạt động hệ thống của bạn.

Thực hiện tạo project theo các bước bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn **Quota & Usage**.
3. Chọn **Mua Synthetic test quota.**
4. Chọn **Class** mà bạn có nhu cầu sử dụn&#x67;**.** Hiện tại chúng tôi chỉ cung cấp class Basic để bạn trải nghiệm
5. Nếu bạn chọn class **Basic**, bạn sẽ không thể thực hiện tùy chỉnh cấu hình gói. Để biết thêm thông tin chi tiết về thông tin các class, hãy xem [Synthetic Test Quota Class](../vmonitor-platform-la-gi/vmonitor-platform-synthetic-la-gi/synthetic-test-quota-class.md).
6. Chọn **Buy Synthetic Test Quota**.
7. Thực hiện các bước **Thanh toán** giỏ hàng và sau khi thanh toán thành công **Synthetic test quota** sẽ được khởi tạo.

Cách tính chi phí cho mỗi gói Synthetic Test quota được chúng tôi công khai trên trang chủ của VNG Cloud, hãy xem tại [Cách tính phí](../../vstorage/object-storage/vstorage-hcm03/cach-tinh-phi/).

***

### Bước 2: Cài đặt API Test với HTTP(s) <a href="#batdauvoisynthetics-buoc2-caidatapitestvoihttp-s" id="batdauvoisynthetics-buoc2-caidatapitestvoihttp-s"></a>

API HTTP tests cho phép bạn gửi HTTP(s) requests tới dịch vụ hay ứng dụng của bạn để **xác minh phản hồi hay các điều kiện xác định** như "status code, header hay body content" mà bạn đã thiết lập khi tạo API test

**Để thực hiện tạo API Test với phương thức HTTP(s), hãy làm theo hướng dẫn bên dưới:**

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Synthetic test.**
3. Chọn **API test.**
4. Chọn **Create an API test.**
5. Nhập các thông tin bao gồm:

* **Test Information: định nghĩa các thông tin cơ bản, chọn HTTP method và chỉ định URL cần kiểm tra**
  * **Test name:** tên của API test
  * **Test type**: giao thức kiểm tra, bạn chọn HTTP(s)
  * **Verify** ssl: lựa chọn có kiểm tra ssl hay không (True hay False)
  * **Method:** lựa chọn method sẽ kiểm tra endpoint của bạn (Get, Post, Put, Delete)
  * **URL**: điền thông tin dịch vụ bạn muốn kiểm tra, ví dụ [https://google.com](https://google.com/)

<figure><img src="../../.gitbook/assets/image (38) (1).png" alt=""><figcaption></figcaption></figure>

* Sau khi điền các Test Information bạn có thể chọn **Run Test hoặc Test Again** nếu bạn đã Test trước đó để kiểm tra, bạn có thể thấy các thông tin trả về như status code, header và body:

<figure><img src="../../.gitbook/assets/image (39) (1).png" alt=""><figcaption></figcaption></figure>

* **Test Assertion**
  * Assertion định nghĩa những gì bạn kì vọng về kết quả API Test, nếu kết quả trả về thoả những gì bạn định nghĩa API Test sẽ thể hiện URL bạn đang kiểm tra là thành công, và ngược lại API Test sẽ thể hiện URL bạn đang kiểm tra là thất bại. Hệ thống sẽ tự động thêm Assertion status code cho bạn sau khi bạn Run test, bạn cần định nghĩa ít nhất một Assertion cho API test. Ngoài Assertion status code hệ thống tự thêm, bạn có thể thêm bất kì các Assertion khác mà chúng tôi hỗ trợ như bên dưới: Response time, Header, Body, Certificate

<figure><img src="../../.gitbook/assets/image (40) (1).png" alt=""><figcaption></figcaption></figure>

* **Location**&#x20;
  * Lựa chọn Location mà ở đó sẽ chạy các HTTP Test tới URL của bạn. HTTP tests có thể chạy từ cả Public Locations (do VNG Cloud quản lý) và Private Locations (do khách hàng tự cài đặt và quản lý) dựa trên nhu cầu của bạn cho việc chạy test từ bên ngoài (internet) hay bên trong mạng của bạn. Public Locations do VNG Cloud quản lý hiện tại có 2 locations là HCM và HN.

<figure><img src="../../.gitbook/assets/image (41) (1).png" alt=""><figcaption></figcaption></figure>

* **Alarm conditions:** Thiết lập điều kiện cảnh báo để xác định các trường hợp mà bạn muốn kiểm tra không thành công và kích hoạt cảnh báo.
  * **Interval**: bao lâu API Test sẽ kiểm tra một lần, mặc định sẽ là 1p
  * **Time of failure**: bao nhiêu lần thất bại liên tiếp sẽ cảnh báo
  * **Locations with failure**: bao nhiêu location thất bại mới cảnh báo
  * Ví dụ khi bạn chọn Time of failure: 1 và Locations with failure: 2, sẽ được hiểu là: bạn sẽ được cảnh báo nếu Test thất bại 1 lần liên tiếp từ 2 trên 2 locations.
  * **Notifications**: bạn chọn các kênh thông báo khi chuyển qua các trạng thái In-alarm, Up hay Undertermine, Hệ thống sẽ thông báo theo danh sách này.

<figure><img src="../../.gitbook/assets/image (42) (1).png" alt=""><figcaption></figcaption></figure>

6\. Sau đó nhấn nút "**Create**" để khởi tạo API test. Sau khi tạo xong bạn sẽ thấy API test đang ở trạng thái Undertermine, cho đến khi inteval tiếp theo API Test sẽ được cập nhập trạng thái chính xác:

<figure><img src="../../.gitbook/assets/image (43) (1).png" alt=""><figcaption></figcaption></figure>

* API Test đã chuyển thành trạng thái Up khi URL đang hoạt động bình thường

<figure><img src="../../.gitbook/assets/image (44) (1).png" alt=""><figcaption></figcaption></figure>

* Bạn có thể xem chi tiết về API Test:

<figure><img src="../../.gitbook/assets/image (45) (1).png" alt=""><figcaption></figcaption></figure>
