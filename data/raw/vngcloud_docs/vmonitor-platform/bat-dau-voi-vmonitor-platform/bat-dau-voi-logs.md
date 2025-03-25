# Bắt đầu với Logs

### Bước 1: Khởi tạo Log project <a href="#batdauvoilogs-buoc1-khoitaologproject" id="batdauvoilogs-buoc1-khoitaologproject"></a>

Bắt đầu sử dụng dịch vụ, bạn cần tạo một Log project. Một Log project là một thuật ngữ trên vMonitor Platform thể hiện một gói giám sát Logs với dung lượng và thời gian cụ thể mà bạn thực hiện mua trên VNG Cloud. Tại một thời điểm bạn có thể sở hữu một hoặc nhiều Log project song song và sử dụng chúng như một cách tổ chức tài nguyên cho các nhóm hay phòng ban sử dụng với mục đích khác nhau.

Thực hiện tạo project theo các bước bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn **Quota & Usage**.
3. Chọn **Mua một log project.**
4. Nhập **Tên Log project.** Theo quy định của chúng tôi, **Tên Log project** phải dài từ 1 (tối thiểu) đến 63 (tối đa) ký tự. **Tên Log project** có thể bao gồm các chữ cái viết thường (a-z), số (0-9), dấu gạch ngang (-). **Tên Log project** phải bắt đầu bằng một chữ cái viết thường và kết thúc bằng một chữ cái viết thường hoặc một chữ số.
5. Nhập **Mô tả** log project nếu có. Theo quy định của chúng tôi, **Mô tả** có thể dài từ 0 (tối thiểu) đến 300 (tối đa) ký tự. **Mô tả** có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), khoảng trắng ( ) hoặc dấu gạch ngang (-).
6. Chọn **Class** mà bạn có nhu cầu sử dụn&#x67;**.** Chúng tôi cung cấp cho bạn chọn 1 trong 2 class bao gồm: Basic, Pro.
7. Nếu bạn chọn class **Basic**, bạn sẽ không thể thực hiện tùy chỉnh cấu hình gói. Nếu bạn chọn class **Pro**, bạn có thể lựa chọn retiontion day và lựa chọn cấu hình log size per day mong muốn bằng cách kéo thả hoặc nhập con số dung lượng bạn mong muốn tại ô Log size per day. dụng. Để biết thêm thông tin chi tiết về thông tin các class, hãy xem [Log Project Class](../vmonitor-platform-la-gi/vmonitor-platform-log-la-gi/log-project-class.md).
8. Chọn **Buy Log Quota.**
9. Thực hiện các bước **Thanh toán** giỏ hàng và sau khi thanh toán thành công **Log project** sẽ được khởi tạo.

Cách tính chi phí cho mỗi gói log project được chúng tôi công khai trên trang chủ của VNG Cloud, hãy xem tại [Cách tính phí](../../vstorage/object-storage/vstorage-hcm03/cach-tinh-phi/).

***

### Bước 2: Tải xuống Certificate và cài đặt Log Agent trên Server <a href="#batdauvoilogs-buoc2-certificatevacaidatlogagenttrenserver" id="batdauvoilogs-buoc2-certificatevacaidatlogagenttrenserver"></a>

Sau khi mua Log Project, hệ thống sẽ tự động sinh ra certificate cho từng Log Project, certificate này dùng để xác thực Log Agent với hệ thống vMonitor Platform.

Thực hiện các bước bên dưới để tải certificate và các scitps cài đặt

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Chọn **Integration.**
2. Chọn **Certificate.**
3. Chọn **Tải xuống** để tải thông tin certificate về server mà bạn muốn đẩy logs về.

Sau khi tải xuống, thư mục sẽ chứa các thông tin hướng dẫn thiết lập agent nằm trong file readme, các script hướng dẫn cũng nằm trong tệp tin certificate được tải về. Sử dụng thông tin này với các hướng dẫn bên dưới để hoàn thành việc thiết lập Agent for Log.

**Cài đặt**

Xác định một loại agent mà mình muốn cài và làm theo hưỡng dẫn của agent đó dưới đây, ở đây chúng tôi hướng dẫn cài đặt Filebeat agent:

* Nếu sử dụng script chuẩn bị sẵn trong thư mục tải về, chạy lệnh

```
sudo chmod +x filebeat.sh
sudo ./filebeat.sh <path-to-file-log>
```

***

### Bước 3: Xem thông tin Log thông qua Log search <a href="#batdauvoilogs-buoc3-xemthongtinlogthongqualogsearch" id="batdauvoilogs-buoc3-xemthongtinlogthongqualogsearch"></a>

Để thực hiện tìm kiếm và phân tích log, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Chọn **Log.**
2. Chọn **Log search**.
3. Chọn **Log project** nào bạn cần xem và phân tích logs. Vị trí chọn log project được hiển thị như hình bên dưới:

<figure><img src="../../.gitbook/assets/image (37) (1).png" alt=""><figcaption></figcaption></figure>

4. Tiếp tục thực hiện **tìm kiếm và phân tích logs**.
