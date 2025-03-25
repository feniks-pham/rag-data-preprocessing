# Cài đặt Log Agent trên các hệ điều hành

#### Chuẩn bị kết nối cài agent

* Nếu bạn có đầy đủ kết nối ra internet là cách tốt nhất để khi cài cài đặt agent đỡ gặp lỗi.
* Nếu phải cài qua proxy hoặc firewall. Mở policy cho phép kết nối tới các địa chỉ sau:

| <pre><code># filebeat / logstash 
https://artifacts.elastic.co
# fluentd 
https://toolbelt.treasuredata.com 
https://packages.treasuredata.com
# fluentbit
https://packages.fluentbit.io
# vector
https://repositories.timber.io
</code></pre> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* Nếu phải cài hoàn toàn offline, chúng tôi khuyên bạn tải filebeat. Các agent khác như fluentbit, fluentd, logstash, … có thể cần thêm các gói phụ thuộc phức tạp. Tải sẵn filebeat về máy tại địa chỉ:

| <pre><code># debian, ubuntu
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.6.0-amd64.deb
# fedora, centos
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.6.0-x86_64.rpm
# windows
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.7.0-windows-x86_64.msi
</code></pre> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* Sau khi tải agent xong, kết nối này có thể đóng. Bạn vẫn cần duy trì kết nối đẩy log.
