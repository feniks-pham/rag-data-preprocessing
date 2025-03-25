# Bắt đầu với Metrics

### Bước 1: Khởi tạo Metric quota <a href="#batdauvoimetrics-buoc1-khoitaometricquota" id="batdauvoimetrics-buoc1-khoitaometricquota"></a>

Bắt đầu sử dụng dịch vụ, bạn cần tạo một Metric quota. Một Metric quota là một thuật ngữ trên vMonitor Platform thể hiện một gói giám sát Metric với số lượng Resource và thời gian lưu trữ cụ thể mà bạn thực hiện mua trên VNG Cloud. Tại một thời điểm bạn có thể sở hữu một Metric quota và sử dụng chúng để phân tích số liệu từ hệ thống của bạn.

Thực hiện mua Metric Quota theo các bước bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn **Quota & Usage**.
3. Chọn **Buy metric quota.**
4. Chọn **Class** mà bạn có nhu cầu sử dụn&#x67;**.** Chúng tôi cung cấp cho bạn chọn 1 trong 2 class bao gồm: Basic, Pro.
5. Nếu bạn chọn class **Basic**, bạn sẽ không thể thực hiện tùy chỉnh cấu hình gói. Nếu bạn chọn class **Pro**, bạn có thể lựa chọn số lượng host mong muốn bằng cách kéo thả hoặc nhập con số resources bạn mong muốn tại ô Number of resources. dụng. Để biết thêm thông tin chi tiết về thông tin các class, hãy xem [Metric Quota Class](../vmonitor-platform-la-gi/vmonitor-platform-metric-la-gi/metric-quota-class.md).
6. Chọn **Buy Metric Quota**.
7. Chọn **Chu kỳ** nếu bạn là người dùng trả trước. Chúng tôi cung cấp các chu kỳ trả trước bao gồm: 1 tháng, 3 tháng, 6 tháng, 12 tháng, 24 tháng, 36 tháng.
8. Chọn **Continue.**
9. Thực hiện các bước **Thanh toán** giỏ hàng và sau khi thanh toán thành công **Metric quota** sẽ được khởi tạo.

Cách tính chi phí cho mỗi gói metric quota được chúng tôi công khai trên trang chủ của VNG Cloud, hãy xem tại [Cách tính phí](../../vstorage/object-storage/vstorage-hcm03/cach-tinh-phi/).

***

### Bước 2: Khởi tạo Service Account <a href="#batdauvoimetrics-buoc2-khoitaoserviceaccount" id="batdauvoimetrics-buoc2-khoitaoserviceaccount"></a>

**Tạo Service Account và gắn policy:&#x20;**<mark style="color:red;">**vMonitorMetricPush**</mark>**&#x20;để có đủ quyền đẩy Metric về vMonitor (Có thể bỏ qua bước này nếu đã tạo trước đó)**

Để tạo service account bạn truy cập tại [đây](https://hcm-3.console.vngcloud.vn/iam/service-accounts)

1. Chọn "**Create a Service Account**", điền tên cho Service Account và nhấn **Next Step** để gắn quyền cho Service Account.
2. Tìm và chọn **Policy:** **vMonitorMetricPush,** sau đó nhấn "**Create a Service Account**" để tạo Service Account, Policy: vMonitorMetricPush do VNG Cloud tạo ra chỉ chứa chính xác quyền đẩy metric về hệ thống.
3. Sau khi tạo thành công bạn cần phải lưu lại Client\_ID và Secret\_Key để thực hiện bước tiếp theo

***

### Bước 3: Cài đặt Metric Agent trên Linux OS Server <a href="#batdauvoimetrics-buoc3-caidatmetricagenttrenlinuxosserver" id="batdauvoimetrics-buoc3-caidatmetricagenttrenlinuxosserver"></a>

Để đẩy Metric về vMonitor, bạn cần cài đặt Metric Agent trên server, vMonitor Platform sử dụng Telegraf Agent để đẩy metric về hệ thống, hiện tại Telegraf Agent hỗ trợ Service Account của IAM để xác thực và phân quyền, bạn thực hiện các bước bên dưới để thiết lập Telegraf Agent đẩy metrics về vMonitor.

Sau khi khởi tạo thành công Service Account và đã lưu trữ thông tin Client\_ID, Secret\_key, hãy tiếp tục:

**Thay thế Client\_ID, Secret\_Key vào câu lệnh bên dưới và chạy trên server để cài đặt**

Bạn sử dụng Client\_ID và Secret\_Key đã sao chép ở trên, thay thế theo thứ tự vào các trường **$IAM\_CLIENT\_ID** và **$IAM\_CLIENT\_SECRET** của câu lệnh bên dưới và chạy trên server cần được monitor, lưu ý bạn cần chạy với quyền **root user** của server (nếu không bạn phải thêm sudo ở trước câu lệnh)

```
VMONITOR_SITE=monitoring-agent.vngcloud.vn \
IAM_CLIENT_ID=$IAM_CLIENT_ID \
IAM_CLIENT_SECRET=$IAM_CLIENT_SECRET \
IAM_URL=https://iamapis.vngcloud.vn/accounts-api/v2/auth/token \bash -c "$(curl -L 
https://raw.githubusercontent.com/vngcloud/vmonitor-metrics-agent/main/install.sh)"
```

***

### Bước 4: Xem thông tin Metric thông qua Dashboard <a href="#batdauvoimetrics-buoc4-xemthongtinmetricthongquadashboard" id="batdauvoimetrics-buoc4-xemthongtinmetricthongquadashboard"></a>

Sau khi cài đặt Metric Agent theo hướng dẫn tại **Bước 3: Cài đặt Metric Agent trên Server** để đẩy metric về vMonitor Platform, chúng tôi sẽ tự động tạo **Dashboard mặc định** cho **Host** này. Để xem Dashboard mặc định này, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Chọn **Infrastructure List/ Host.**

<figure><img src="../../.gitbook/assets/image (35) (1).png" alt=""><figcaption></figcaption></figure>

2. Chọn tên **Hostname**. Ví dụ thiết bị **LAP15839** được thiết lập Metric Agent thành công tới hệ thống vMonitor Platform thì dashboard mặc định sẽ có tên: **LAP15839**, bạn chọn dashboard sẽ hiển thị như ảnh:

<figure><img src="../../.gitbook/assets/image (36) (1).png" alt=""><figcaption></figcaption></figure>

Với Dashboard Mặc định này, bạn sẽ có thể xem được các thông tin metric mà chúng tôi đã vẽ trước cho bạn bao gồm các biểu đồ về thông tin CPU, Memory, Load Avg, Disk, Network. Cũng trên **Dashboard mặc định** này bạn không thể thêm widget hay tuỳ chỉnh dashboard. Để thực hiện thay đổi hay tùy chỉnh Dashboard, bạn cần tạo dashboard mới hoặc **Tạo bản sao** từ **Dashboard mặc định** này ra và Chỉnh sửa. Để tạo bản sao Dashboard, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Chọn **Dashboard.**
2. Trên **Dashboard Mặc định** muốn tạo bản sao, chọn <img src="https://docs.vngcloud.vn/download/thumbnails/49649936/image2023-4-18_11-33-12.png?version=1&#x26;modificationDate=1691483173000&#x26;api=v2" alt="" data-size="line">, sau đó chọn **Tạo bản sao Dashboard**.
3. Nhập **Tên Dashboard.** Theo quy định của chúng tôi, tên Dashboard phải dài từ 1 (tối thiểu) đến 50 (tối đa) ký tự. Tên Dashboard có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-), ký tự (@), ký tự (/).
4. Chọn **Tạo bản sao**.

Sau khi bản sao của **Dashboard mặc định** được tạo, bạn có thể thêm hoặc xoá, hoặc tùy chỉnh, thay đổi vị trí Widget trong Dashboard bản sao này. Để biết thêm về cách làm việc với Metric nói chung và Metric Dashboard nói chung, hãy xem tại [Metrics](../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/giam-sat-hoat-dong-lb/metrics.md).
