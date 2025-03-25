# Làm việc với Log Agent

Chúng tôi sử dụng giao thức nhận log chuẩn **Kafka** đối với vMonitor Platform Logs. Do đó chúng tôi hỗ trợ bạn cấu hình đẩy logs từ tất cả các agent logs phổ biến hiện có như filebeat, fluentd, logstash, rsyslog, vector,… Nếu bạn còn phân vân, lời khuyên chúng tôi là cài **Filebeat** - nhẹ và hiệu năng cao, hoặc **Logstash** - với nhu cầu parse log phức tạp hơn.

<table data-header-hidden><thead><tr><th width="154"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Môi trường</strong></td><td><strong>Phiên bản (Version)</strong></td><td><strong>Phiên bản logstash VNG đã kiểm tra tương thích</strong></td><td>Phiên bản filebeat <strong>VNG đã kiểm tra</strong> tương thích</td></tr><tr><td>Centos </td><td>7, 8</td><td>logstash-8.6.2</td><td>filebeat-8.7</td></tr><tr><td>Debian </td><td>7,8,9</td><td>logstash-8.6.2</td><td>filebeat-8.7</td></tr><tr><td>Ubuntu </td><td>14,16,18,20,22</td><td>logstash-8.6.2</td><td>filebeat-8.7</td></tr><tr><td>Docker </td><td>Từ 18 trở lên</td><td>logstash-8.6.2</td><td>filebeat-8.7</td></tr><tr><td>Kubernetes</td><td>Từ 1.18 trở lên</td><td>logstash-8.6.2</td><td>filebeat-8.7</td></tr><tr><td>Windows </td><td>2016, 2019, 2022</td><td>logstash-8.6.2</td><td>filebeat-8.7</td></tr></tbody></table>

Để làm việc với Log Agent, bạn cần thực hiện theo các bước:

* [Chuẩn bị kết nối đẩy log](chuan-bi-ket-noi-day-log.md)
* [Khởi tạo Certificate](broken-reference)
* [Cài đặt Log Agent trên các hệ điều hành](cai-dat-log-agent-tren-cac-he-dieu-hanh/)
* [Cài đặt Log Agent trên docker](cai-dat-log-agent-tren-cac-he-dieu-hanh/)
* [Cài đặt Log Agent trên kubernetes](cai-dat-log-agent-tren-kubernetes.md)

```
```
