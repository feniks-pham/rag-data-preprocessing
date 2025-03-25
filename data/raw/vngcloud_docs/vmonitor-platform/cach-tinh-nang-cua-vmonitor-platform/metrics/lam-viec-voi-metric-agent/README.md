# Làm việc với Metric Agent

### Tổng quan

Để đẩy Metric về vMonitor, bạn cần cài đặt Metric Agent trên server, vMonitor sử dụng Telegraf Agent để đẩy metric về hệ thống, hiện tại Telegraf Agent hỗ trợ Service Account của IAM để xác thực và phân quyền, bạn thực hiện các bước bên dưới để thiết lập Telegraf Agent đẩy metrics về vMonitor

***

### Cài đặt Metric Agent trên Server

* [Linux OS](cai-dat-metric-agent-tren-server/linux-os.md)
* [Linux OS có giới hạn kết nối Internet](cai-dat-metric-agent-tren-server/linux-os-co-gioi-han-ket-noi-internet.md)
* [Window OS](cai-dat-metric-agent-tren-server/window-os.md)

***

### Xem thông tin Host được thiết lập thành công Metric Agent

Những server cài đặt Metric Agent được gọi là **Host**, sau khi cài đặt thành công trên các Server, bạn có thể thấy danh sách các Host đang đẩy Metric về tại trang Infrastructure List/Host bằng cách:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Infrastructure list.**
3. Chọn **Host.**
4. Hệ thống hiển thị thông tin các host mà bạn đã thiết lập đẩy metrics thành công. Thông tin hiển thị bao gồm:

* **Status**: trạng thái của server có đang đẩy dữ liệu về hay không, nếu có sẽ là UP, nếu không sẽ là Undertermine
* **Memory Available**: thông tin bộ nhớ có sẵn tại thời điểm hiện tại.
* **CPU Usage**: thông tin dung lượng CPU đang sử dụng tại thời điểm hiện tại.
* **Load**: thông tin Load tại thời điểm hiện tại.
* **Apps**: danh sách các plugin mà Metric Agent đang bật.
* **Billing** **Status**: trạng thái monitor của Host.

Bạn có thể thiết lập nhiều host cùng đẩy metrics về hệ thống vMonitor Platform bằng cách sử dụng chung một Service Account khi thiết lập Metric Agent. Ví dụ 2 thiết bị LAPTOP-01 và LAPTOP-02 cùng sử dụng một Service Account để đẩy metrics về vMonitor Platform. Số lượng host này được chúng tôi định nghĩa là số lượng resource khi bạn thực hiện mua gói Metric quota.

Khi nhấn vào khung của 1 Host, sẽ có trang xem chi tiết về Host đó, quy tắc đặt tên dashboard cho Host sẽ là hostname của Host:

Đồng thời nhấn vào tên của Host, bạn sẽ được chuyển sang trang Dashboard, và xem default dashboard của Host này.

{% hint style="info" %}
**Chú ý:**

* Hệ thống vMonitor sẽ mất 1 khoảng thời gian trung bình dưới 1 phút (có thể có trường hợp tệ nhất 5 phút) để cập nhập Host mới sau khi bạn cài Metric Agent.
{% endhint %}

***

### Vô hiệu hóa Host đã thiết lập thành công Metric Agent

Sau khi bạn thiết lập thành công Metric Agent trên Server, bạn có một số lượng host nhất định đã được đẩy metric về hệ thống vMonitor Platform. Lúc này bạn muốn tắt tạm thời việc đẩy metric từ một host về hệ thống của chúng tôi mà không muốn xoá Metric Agent trên host đó, tính năng Vô hiệu hóa host sẽ giúp bạn làm điều này. Để thực hiện vô hiệu hóa host đã thiết lập thành công Metric Agent, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Infrastructure list.**
3. Chọn **Host.**
4. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (112).png" alt="" data-size="line"> tại **host** bạn muốn thực hiện vô hiệu quá.
5. Màn hình xác nhận vô hiệu quá host hiển thị, chọn **Disable**.
6. Khi biểu tượng này trở thành <img src="../../../../.gitbook/assets/image (111).png" alt="" data-size="line">tức là host đã được vô hiệu hóa thành công.&#x20;

Khi bạn thực hiện vô hiệu quá một host, cấu hình Metric Agent của host được giữ nguyên, bạn có thể bật lại việc giám sát host bất kỳ lúc nào theo hướng dẫn tại Khôi phục Host đang bị vô hiệu hóa. Kể từ thời điểm bạn thực hiện vô hiệu quá host, các thông số metric của host sẽ không được đẩy về và host sẽ không bị ghi nhận là 1 resource trên cấu hình gói Metric quota. Nếu bạn không có nhu cầu giám sát dữ liệu metric trên một host nào đó, bạn cũng có thể thực hiện xóa hoàn toàn thông tin host theo hướng dẫn tại Xóa thông tin Host đã thiết lập thành công Metric Agent.

***

### Khôi phục Host đang bị vô hiệu hóa

Bạn đã vô hiệu quá một host trong việc đẩy metric về hệ thống của chúng tôi và các thông số metric của host đã bị tạm dừng đẩy về kể từ thời điểm vô hiệu hóa. Hiện tại, bạn có nhu cầu giám sát trở lại các thông số metric này, để thực hiện khôi phục lại host đang bị vô hiệu quá, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Infrastructure list.**
3. Chọn **Host.**
4. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (111).png" alt="" data-size="line">tại **host** bạn muốn thực hiện khôi phục.
5. Màn hình xác nhận khôi phục host hiển thị, chọn **Enable**.
6. Khi biểu tượng này trở thành <img src="../../../../.gitbook/assets/image (112).png" alt="" data-size="line">tức là host đã được khôi phục thành công. Kể từ thời điểm này, metrics lại tiếp tục được đẩy về.

***

### Xóa thông tin Host đã thiết lập thành công Metric Agent

Để **xóa** một **host**, bạn có thể:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Infrastructure list.**
3. Chọn **Host.**
4. Tại host bạn muốn thực hiện xóa, chọn **Delete.**
5. Tại màn hình xác nhận xóa host, chọn **Delete**.

{% hint style="info" %}
**Chú ý:**

* Sau khi bạn bạn thực hiện xóa host thì host bị tạm thời bị xóa khỏi danh sách host của bạn tuy nhiên nếu bạn không gỡ Metric Agent trên Server, thì bản ghi monitor Host này sẽ tự động sinh ra ở lần kế tiếp.
{% endhint %}

Để xem danh sách metrics tương ứng của mỗi product này, hãy xem tại [Danh sách Metrics hỗ trợ](../danh-sach-metrics-ho-tro/).
