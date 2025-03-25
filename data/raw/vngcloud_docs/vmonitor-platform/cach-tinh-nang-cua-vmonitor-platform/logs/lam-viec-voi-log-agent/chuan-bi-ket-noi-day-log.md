# Chuẩn bị kết nối đẩy log

#### Kết nối từ máy đẩy log tới hệ thống vMontior Platform.

<table data-header-hidden><thead><tr><th width="182"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Nguồn</strong></td><td><strong>Đích</strong></td><td><strong>Port</strong></td></tr><tr><td>IP máy đẩy log</td><td>Dải subnet:<br>116.118.93.130/28, tức<br>116.118.93.128 -> 116.118.93.143</td><td>10092 TCP</td></tr><tr><td>IP máy đẩy log</td><td>Domain:<br><a href="http://hcm01-loghub01.vngcloud.vn">hcm01-loghub01.vngcloud.vn</a> <a href="http://hcm02-loghub01.vngcloud.vn">hcm02-loghub01.vngcloud.vn</a> <a href="http://hcm03-loghub01.vngcloud.vn">hcm03-loghub01.vngcloud.vn</a></td><td>10092 TCP</td></tr></tbody></table>

* Kết nối trên cần mở trong suốt quá trình agent đẩy log

Nếu các máy cần thu thập log có máy không thể mở kết nối trực tiếp trên. Tham khảo sử dụng mô hình [collector](https://opentelemetry.io/docs/collector/) để đẩy qua một host trung gian.

***

#### Phân giải domain

Do dữ liệu kênh truyền được **bảo mật** bằng chuẩn mã hóa SSL. Nếu máy đẩy log có khả năng truy vấn DNS public thì không vấn đề gì. Tuy nhiên nếu không (có thể gặp trong môi trường on-premise) thì bạn cần thêm phân giải domain theo bảng sau:

| <pre><code># IP---------------| Domain
116.118.93.131      hcm01-loghub01.vngcloud.vn 
116.118.93.132      hcm02-loghub01.vngcloud.vn 
116.118.93.133      hcm03-loghub01.vngcloud.vn
116.118.93.134      hcm04-loghub01.vngcloud.vn
116.118.93.135      hcm05-loghub01.vngcloud.vn
116.118.93.136      hcm06-loghub01.vngcloud.vn
</code></pre> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

\
