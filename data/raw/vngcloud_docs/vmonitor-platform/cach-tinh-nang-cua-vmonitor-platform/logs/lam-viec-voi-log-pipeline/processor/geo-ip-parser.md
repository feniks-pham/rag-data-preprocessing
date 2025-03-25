# GEO IP Parser

### Tổng quan

GEO IP Parser là một bộ phân tích và xác định vị trí địa lý của một địa chỉ IP. GEO IP Parser có thể cung cấp cho bạn các thông tin như quốc gia, thành phố, kinh độ, vĩ độ, nhà cung cấp dịch vụ Internet (ISP), tên miền, múi giờ, và các thông tin khác của một địa chỉ IP.

***

### Cấu hình GEO IP Parser

Để cáu hình GEO IP Parser, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Tại mục **Processor information**, nhập các thông tin chung cho một processor theo hướng dẫn tại [Processor](./). Trong nội dung này thì bạn sẽ chọn **Processor type** là **GEO IP Parser**.
2. Tại mục **Parsing rule**, nhập các thông tin sau đây:

* Nhập **Source field**: field chứa logs sẽ cần parse.
* Nhập **Database type:** nguồn và định dạng của cơ sở dữ liệu địa chỉ IP và vị trí địa lý. Mặc định hệ thống sẽ chọn **City**, tức là bạn cần phân tích vị trí địa chỉ ở mức độ thành phố. Nếu bạn chọn **ASN** tức là là cơ sở dữ liệu địa chỉ IP và vị trí địa lý dựa trên số hiệu hệ thống tự trị (Autonomous System Number - ASN)
* Nhập **Target field**: field sẽ được ghi đè bên destination log project, thông thường bạn sẽ không cần nhập thông tin này.

Ví dụ:&#x20;

<table data-full-width="true"><thead><tr><th>Source log project</th><th>Destination log project</th><th>Client_IP (field logs mà chúng tôi thực hiện parser)</th><th>Kết quả parser</th></tr></thead><tbody><tr><td>webserver</td><td>webserver-parse</td><td>"client_ip: "31.184.238.22"</td><td>"client_ip_parse": { "ip": "182.34.27.162", "latitude": 36.0986, "longitude": 120.3719, "country_name": "China", "location": { "lat": 36.0986, "lon": 120.3719 }, "continent_code": "AS", "region_name": "Shandong", "country_code2": "CN", "timezone": "Asia/Shanghai", "country_code3": "CN", "region_code": "SD" },</td></tr></tbody></table>

<figure><img src="../../../../../.gitbook/assets/image (328).png" alt=""><figcaption></figcaption></figure>

***

### Lưu trữ và tái sử dụng Parsing rule

* Bạn có thể lưu trữ một parsing rule bằng cách tích chọn vào **Save this rule**, sau đó nhập tên gợi nhớ cho parsing rule mà bạn muốn lưu trữ. Tên gợi nhớ có chiều dài tối thiểu là 5 ký tự, chiều dài tối đa là 255 ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Sau khi parsing rule đã được lưu trữ, trong các lần tạo processor kế tiếp bạn có thể tái sử dụng rule này bằng cách chọn **Rule presets** tại mục Pasing rule.&#x20;
