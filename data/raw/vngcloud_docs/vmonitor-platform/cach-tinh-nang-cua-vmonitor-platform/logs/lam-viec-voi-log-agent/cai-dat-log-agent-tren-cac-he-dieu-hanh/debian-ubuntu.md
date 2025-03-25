# Debian/ Ubuntu

Trước khi thực hiện cài đặt agent trên các hệ điều hành mà chúng tôi hỗ trợ bên dưới, bạn cần phải tải xuống certificate theo hướng dẫn tại [Khởi tạo Certificate](../khoi-tao-certificate.md). Thông tin hướng dẫn thiết lập agent nằm trong file readme, các script hướng dẫn cũng nằm trong tệp tin certificate được tải về. Sử dụng thông tin này với các hướng dẫn bên dưới để hoàn thành việc thiết lập Agent for Log.

#### Cài đặt

Xác định một loại agent mà mình muốn cài và làm theo hưỡng dẫn của agent đó dưới đây:

{% tabs %}
{% tab title="Filebeat" %}
Nếu sử dụng script chuẩn bị sẵn trong thư mục tải về, chạy lệnh

```
sudo chmod +x filebeat.sh
sudo ./filebeat.sh <path-to-file-log>

```

Nếu cài thủ công, chạy lệnh

```
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.7.1-amd64.deb
sudo dpkg -i filebeat-8.7.1-amd64.deb
```
{% endtab %}

{% tab title="Logstash" %}
Nếu sử dụng script chuẩn bị sẵn trong thư mục tải về, chạy lệnh

| <pre><code>sudo chmod +x logstash.sh
sudo ./logstash.sh &#x3C;path-to-file-log>
</code></pre> |
| --------------------------------------------------------------------------------------------- |

Nếu cài thủ công, chạy lệnh

| <pre><code>Cài java (>8): sudo apt-get install openjdk-8-jre-headless -y
Cài Logstash: curl -LO  https://artifacts.elastic.co/downloads/logstash/logstash-8.6.2-amd64.deb 
			  sudo dpkg -i logstash-8.6.2-amd64.deb
</code></pre> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
{% endtab %}
{% endtabs %}

***

Tiếp theo bạn cần cấu hình agent log. Các file cấu hình dưới đều đã được chúng tôi chuẩn bị sẵn tại script khi tải certificate về, mô tả dưới đây giúp người đọc hình dung được nếu tạo manual sẽ thế nào.

#### Cấu hình

{% tabs %}
{% tab title="Filebeat" %}
File `/etc/filebeat/filebeat.yml.` Cấu hình dưới đây sẽ lấy tất cả log trong file `/var/log/app.log` đẩy về vMonitor Platform:

```
filebeat.inputs:
- type: log
  paths:
    - /var/log/app.log

output.kafka:
  hosts: ["$BOOTSTRAP_SERVERS"]
  topic: "$TOPIC"
  partition.round_robin:
    reachable_only: false
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
  ssl.certificate_authorities:
    - $PATH_FILE_VNG_TRUST_PEM
  ssl.certificate: "$PATH_FILE_USER_CER_PEM"
  ssl.key: "$PATH_FILE_USER_KEY_PEM"
  ssl.verification_mode: "none"
logging.level: info
logging.to_files: true
logging.files:
  path: /var/log/filebeat
  name: filebeat
  keepfiles: 7
  permissions: 0644
```

* Trong đó:
  * Tại `input` đường dẫn tới file log
  * Tại `output` , các biến cần điền bạn lấy từ bước tải certicate ở trên:
    * `$BOOTSTRAP_SERVERS, $TOPIC` lấy trong file [info.md](http://info.md/)
    * `$PATH_FILE_VNG_TRUST_PEM,$PATH_FILE_USER_CER_PEM,$PATH_FILE_USER_KEY_PEM` là đường dẫn tới file VNG.trust.pem user.cer.pem user.key.pem
* Đọc thêm cấu hình nâng cao khác tại [![](https://www.elastic.co/favicon-16x16.png)Configure Filebeat | Filebeat Reference \[8.8\] | Elastic](https://www.elastic.co/guide/en/beats/filebeat/current/configuring-howto-filebeat.html)
{% endtab %}

{% tab title="Logstash" %}
File `/etc/logstash/conf.d/logstash.conf.` Cấu hình dưới đây sẽ lấy tất cả log trong file `/var/log/app.log` đẩy về vMonitor Platform:

```
input {
    file {
        start_position => "beginning"
        path => [ "/var/log/app.log" ]
    }
}

output {
      kafka {
        codec => json
        bootstrap_servers => "$BOOTSTRAP_SERVERS"
        topic_id => "$TOPIC"
        security_protocol => "SSL"
        ssl_truststore_location => "$PATH_FILE_VNG_TRUST"
        ssl_truststore_password => "$TRUTSTORE_PASS"
        ssl_keystore_location => "$PATH_FILE_USER_KEY"
        ssl_keystore_password => "$USER_PASS"
        ssl_key_password => "$USER_PASS"
        ssl_endpoint_identification_algorithm => ""
      }
}
```

Trong đó:&#x20;

* Tại `input` , nếu như muốn lấy thêm log tại các file khác, cấu hình thêm như sau
* Tại `output` , các biến cần điền bạn lấy từ bước tải certicate ở trên:
  * `$BOOTSTRAP_SERVERS, $TOPIC, $TRUTSTORE_PASS, $USER_PASS` lấy trong file [info.md](http://info.md/)
  * `$PATH_FILE_VNG_TRUST, $PATH_FILE_USER_KEY` là đường dẫn tới file VNG.trust, user.key
* Đọc thêm cấu hình nâng cao khác tại [![](https://www.elastic.co/favicon-16x16.png)Setting Up and Running Logstash | Logstash Reference \[8.8\] | Elastic](https://www.elastic.co/guide/en/logstash/current/setup-logstash.html)
{% endtab %}
{% endtabs %}

***

#### Quản trị

Nếu cài thủ công, mặc định agent log sau khi cài sẽ **không** tự động bật, bạn kiểm tra việc khởi động (start) và enable (tự khởi động cùng máy) cho chúng.

{% tabs %}
{% tab title="Filebeat" %}


|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>Start</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl start filebeat
</code></pre></td></tr></tbody></table><ul><li>Enable</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl enable filebeat
</code></pre></td></tr></tbody></table><ul><li>Stop</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl stop filebeat
</code></pre></td></tr></tbody></table><ul><li>Reload</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl reload filebeat
</code></pre></td></tr></tbody></table><ul><li>Restart</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl restart filebeat
</code></pre></td></tr></tbody></table><ul><li>Observe</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl status filebeat
journalctl -f --unit filebeat
tail -f /var/log/filebeat
</code></pre></td></tr></tbody></table><ul><li>Uninstall</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>tapt remove --purge filebeat
</code></pre></td></tr></tbody></table><p><br></p> |
{% endtab %}

{% tab title="Logstash" %}


| <ul><li>Start</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl start logstash
</code></pre></td></tr></tbody></table><ul><li>Enable</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl enable logstash
</code></pre></td></tr></tbody></table><ul><li>Stop</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl stop logstash
</code></pre></td></tr></tbody></table><ul><li>Reload</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl reload logstash
</code></pre></td></tr></tbody></table><ul><li>Restart</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl restart logstash
</code></pre></td></tr></tbody></table><ul><li>Observe</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl status logstash
journalctl -f --unit logstash
tail -f /var/log/logstash
</code></pre></td></tr></tbody></table><ul><li>Uninstall</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>apt remove --purge logstash
</code></pre></td></tr></tbody></table><p><br></p> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>systemctl start logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <pre><code>systemctl enable logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <pre><code>systemctl stop logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <pre><code>systemctl reload logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <pre><code>systemctl restart logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <pre><code>systemctl status logstash
journalctl -f --unit logstash
tail -f /var/log/logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <pre><code>apt remove --purge logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
{% endtab %}
{% endtabs %}

***

\
