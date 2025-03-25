# Linux OS có giới hạn kết nối Internet

Hướng dẫn [Cài đặt agent tự động](./) yêu cầu kết nối internet HTTPS đến một vài endpoint để tải về các tài nguyên cần thiết cho việc cài đặt, do đó việc cài đặt có thể không thành công tại server bị giới hạn kết nối internet.

{% hint style="info" %}
**Chú ý:**

* Lưu ý bạn cần có Quota Metric, nếu chưa có bạn cần thực hiện mua Quota Metric tại [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=31555658).
{% endhint %}

### **Trường hợp server bị giới hạn kết nối ra ngoài internet**

#### **1. Kiểm tra và đảm bảo kết nối đến vMonitor Site**

{% hint style="info" %}
**Allow by Endpoints:**

* [https://iamapis.vngcloud.vn/accounts-api/v2/auth/token](https://iamapis.vngcloud.vn/accounts-api/v2/auth/token)
* [https://monitoring-agent.vngcloud.vn/\*](https://monitoring-agent.vngcloud.vn/\*)

**Allow by IP and Port:**

* IP: 116.118.93.14, Port: 443 - Protocol: HTTPS ( [iamapis.vngcloud.vn](http://iamapis.vngcloud.vn) )
* IP: 116.118.93.158, Port: 443 - Protocol: HTTPS ( [monitoring-agent.vngcloud.vn](http://monitoring-agent.vngcloud.vn) )
{% endhint %}

#### **2. Tạo Service Account**&#x20;

Bạn cần tạo một Service Account và gắn policy: vMonitorMetricPush để có đủ quyền đẩy Metric về vMonitor (Có thể bỏ qua bước này nếu đã tạo trước đó)

Để tạo service account bạn truy cập tại [đây](https://hcm-3.console.vngcloud.vn/iam/service-accounts),

* Chọn "**Create a Service Account**", điền tên cho Service Account và nhấn **Next Step** để gắn quyền cho Service Account
* Tìm và chọn **Policy:** **vMonitorMetricPush,** sau đó nhấn "**Create a Service Account**" để tạo Service Account, Policy: vMonitorMetricPush do VNG Cloud tạo ra chỉ chứa chính xác quyền đẩy metric về hệ thống
* Sau khi tạo thành công bạn cần phải lưu lại Client\_ID và Secret\_Key để thực hiện bước tiếp theo

#### **3. Tiến hành cài đặt:**

3.1 Tải về package cài đặt từ một server khác: Chọn một trong những package sau đây tùy vào OS

* RPM package: [https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.2/telegraf-nightly.x86\_64.rpm](https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.2/telegraf-nightly.x86\_64.rpm)
* Deb package: [https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.2/telegraf\_nightly\_amd64.deb](https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.2/telegraf\_nightly\_amd64.deb)

3.2 Chuyển package cài đặt đến server: Có thể sử dụng những tool để chuyển hoặc copy package cài đặt đến server (ví dụ: scp, rsync ....)

3.3 Tạo thông tin xác thực

```
echo -e "IAM_CLIENT_ID=YOUR_IAM_CLIENT_ID_XXXXXXXX\nIAM_CLIENT_SECRET=YOUR_IAM_CLIENT_SECRET_XXXXXXXX\nIAM_URL=https://iamapis.vngcloud.vn/accounts-api/v2/auth/token\nVMONITOR_SITE=monitoring-agent.vngcloud.vn" | sudo tee /etc/default/telegraf
```

3.4 Thực hiện cài đặt package: Chạy command sau tùy vào OS

* OS: **Centos** - **yum** package manager

```
sudo yum localinstall /<path_to_file>/telegraf-nightly.x86_64.rpm 
```

* OS: **Ubuntu, Debian** - **apt** or **dpkg** package manager

```
# Sử dụng 1 trong 2 command sau
sudo apt install /<path_to_file>/telegraf_nightly_amd64.deb
# Hoặc
sudo dpkg -i /<path_to_file>/telegraf_nightly_amd64.deb

```

3.5 Start metric agent

* **SystemD** service manager

```
sudo systemctl restart telegraf
```

* **SysVInit** is the classic initialization process

```
sudo service telegraf restart
```

.
