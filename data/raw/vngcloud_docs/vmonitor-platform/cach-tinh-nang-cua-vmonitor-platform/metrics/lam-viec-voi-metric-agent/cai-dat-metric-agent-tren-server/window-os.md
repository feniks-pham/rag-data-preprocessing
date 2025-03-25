# Window OS

Để đẩy Metric về vMonitor, bạn cần cài đặt Metric Agent trên server, vMonitor sử dụng Telegraf Agent để đẩy metric về hệ thống, hiện tại Telegraf Agent hỗ trợ Service Account của IAM để xác thực và phân quyền, bạn thực hiện các bước bên dưới để thiết lập Telegraf Agent đẩy metrics về vMonitor

### **Telegraf Agent với Service Account** <a href="#windowos-telegrafagentvoiserviceaccount" id="windowos-telegrafagentvoiserviceaccount"></a>

1. **Tạo Service Account và gắn policy: vMonitorMetricPush để có đủ quyền đẩy Metric về vMonitor**

Để tạo service account bạn truy cập tại [đây](https://hcm-3.console.vngcloud.vn/iam/service-accounts):

* Chọn "**Create a Service Account**", điền tên cho Service Account và nhấn **Next Step** để gắn quyền cho Service Account
* Tìm và chọn **Policy:** **vMonitorMetricPush,** sau đó nhấn "**Create a Service Account**" để tạo Service Account, Policy: vMonitorMetricPush do VNG Cloud tạo ra chỉ chứa chính xác quyền đẩy metric về hệ thống
* Sau khi tạo thành công bạn cần phải lưu lại Client\_ID và Secret\_Key để thực hiện bước tiếp theo

2\. **Tải bản cài  Agent Installer cho Windows**

* Truy cập vào link để thực hiện tải agent installer cho Windows : [https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.1/telegraf-nightly\_windows\_amd64.exe](https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.1/telegraf-nightly\_windows\_amd64.exe)

3\. **Cài đặt installer với Client\_ID và Secret\_Key đã sao chép ở trên**

* Chạy agent installer đã tải ở trên
* Sau khi nhận thông báo, chọn **More Info**

<figure><img src="../../../../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

* Sau đó chọn **Run anyway**, để bắt đầu cài agent

<figure><img src="../../../../../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

* Chọn **Next** để tiếp tục

<figure><img src="../../../../../.gitbook/assets/image (117).png" alt=""><figcaption></figcaption></figure>

* Nhập 2 thông tin **Client\_ID** và **Secret\_Key** đã sao chép ở trên vào 2 trường: **IAM\_CLIENT\_ID** và **IAM\_CLIENT\_SECRET**:&#x20;

<figure><img src="../../../../../.gitbook/assets/image (118).png" alt=""><figcaption></figcaption></figure>

* Để mặc định, chọn Next để tiếp tục, hoặc nếu bạn muốn thay đổi thư mục cài đặt thì thực hiện thay đổi

<figure><img src="../../../../../.gitbook/assets/image (119).png" alt=""><figcaption></figcaption></figure>

* Chọn **Accept the license,** sau đó chọn **Next** để tiếp tục

<figure><img src="../../../../../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>

* Để mặc định, chọn **Next** để tiếp tục, hoặc bạn có thể tùy chỉnh shortcut menu name cho agent

<figure><img src="../../../../../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

* Chọn **Install** để thực hiện cài đặt

<figure><img src="../../../../../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

* Chọn **Yes** để thực hiện grant quyền cho agent hoạt động

<figure><img src="../../../../../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

* Sau khi quá trình cài đặt hoàn tất, chọn **Finish**

<figure><img src="../../../../../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

4\. **Sau khi cài đặt thành công bạn sẽ thấy server ở trang Infrastructure List/Host**&#x20;

<figure><img src="../../../../../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

### **Telegraf Agent với API\_KEY (deprecated**) <a href="#windowos-telegrafagentvoiapi_key-deprecated-khongkhuyencaosudung-saptoisedunghotrovoiphuongthucnay" id="windowos-telegrafagentvoiapi_key-deprecated-khongkhuyencaosudung-saptoisedunghotrovoiphuongthucnay"></a>

{% hint style="info" %}
**Chú ý:**

* Chúng tôi khuyến cáo bạn không sử dụng phương thức này, trong thời gian sắp tới hệ thống của chúng tôi sẽ dừng hỗ trợ các API Key này.
{% endhint %}

B1: Tạo API Key (nếu chưa thực hiện tạo bất kỳ API Key nào trước đó )

* Truy cập vào portal vMonitor Platform Product: [https://hcm-3.console.vngcloud.vn/vmonitor/](https://hcm-3.console.vngcloud.vn/vmonitor/)
* Chọn **Intergration** => sau đó chọn phần **API Key**

<figure><img src="../../../../../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

* Chọn **Create an API Key**, để thực hiện tạo mới (nếu chưa tạo bất kỳ API Key nào trước đó)

<figure><img src="../../../../../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

B2: Download Agent Installer

* Truy cập vào link để thực hiện tải agent installer: [https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.23.0-1.4.0/telegraf-nightly\_windows\_amd64.exe](https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.23.0-1.4.0/telegraf-nightly\_windows\_amd64.exe)

B3: Install Agent

* Chạy agent installer
* Sau khi nhận thông báo, chọn **More Info**

<figure><img src="../../../../../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

* Sau đó chọn **Run anyway**, để bắt đầu install agent

<figure><img src="../../../../../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>

* Chọn **Next** để tiếp tục

<figure><img src="../../../../../.gitbook/assets/image (132).png" alt=""><figcaption></figcaption></figure>

* Quay về Portal vMonitor Platform, ở phần API Key, **chọn** **biểu** **tượng copy**, để copy thông tin API Key

<figure><img src="../../../../../.gitbook/assets/image (133).png" alt=""><figcaption></figcaption></figure>

* Paste thông tin API Key vào phần nhập **Credentials**

<figure><img src="../../../../../.gitbook/assets/image (134).png" alt=""><figcaption></figcaption></figure>

* Có thể tùy chỉnh installation folder

<figure><img src="../../../../../.gitbook/assets/image (135).png" alt=""><figcaption></figcaption></figure>

* Chọn **Accept the license,** sau đó chọn **Next** để tiếp tục

<figure><img src="../../../../../.gitbook/assets/image (137).png" alt=""><figcaption></figcaption></figure>

* Có thể tùy chỉnh shortcut menu name cho agent, sau đó chọn **Next** để tiếp tục

<figure><img src="../../../../../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>

* Chọn **Install** để thực hiện cài đặt

<figure><img src="../../../../../.gitbook/assets/image (139).png" alt=""><figcaption></figcaption></figure>

* Chọn Yes để thực hiện grant quyền cho agent hoạt động

<figure><img src="../../../../../.gitbook/assets/image (140).png" alt=""><figcaption></figcaption></figure>

* Sau khi quá trình cài đặt hoàn tất, chọn **Finish**

<figure><img src="../../../../../.gitbook/assets/image (141).png" alt=""><figcaption></figcaption></figure>

#### B4: Kiểm tra agent đã hoạt động <a href="#windowos-b4-kiemtraagentdahoatdong" id="windowos-b4-kiemtraagentdahoatdong"></a>

* Truy cập vào portal vMonitor Platform, chọn **Infrastructure list** => chọn **Host,** sau đó kiểm tra hostname của VM đã xuất hiện trong danh sách

<figure><img src="../../../../../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

* Chọn vào tên **Hostname**, để kiểm tra dashboard monitor

<figure><img src="../../../../../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>
