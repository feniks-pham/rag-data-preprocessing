# CentOS

Trước khi thực hiện cài đặt agent trên các hệ điều hành mà chúng tôi hỗ trợ bên dưới, bạn cần phải tải xuống certificate theo hướng dẫn tại [Khởi tạo Certificate](../khoi-tao-certificate.md). Thông tin hướng dẫn thiết lập agent nằm trong file readme, các script hướng dẫn cũng nằm trong tệp tin certificate được tải về. Sử dụng thông tin này với các hướng dẫn bên dưới để hoàn thành việc thiết lập Agent for Log.

#### Cài đặt

Xác định một loại agent mà mình muốn cài và làm theo hưỡng dẫn của agent đó dưới đây:



{% tabs %}
{% tab title="Filebeat" %}
* Nếu sử dụng script chuẩn bị sẵn trong thư mục tải về, chạy lệnh

| <pre><code>sudo chmod +x filebeat.sh
sudo ./filebeat.sh &#x3C;path-to-file-log>
</code></pre> |
| --------------------------------------------------------------------------------------------- |

* Nếu cài thủ công, chạy lệnh

| <pre><code>Tải tệp tin rpm: curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.7.1-x86_64.rpm
Install filebeat: sudo rpm -vi filebeat-8.7.1-x86_64.rpm
</code></pre> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

\

{% endtab %}

{% tab title="Logstash" %}
* Nếu sử dụng script chuẩn bị sẵn trong thư mục tải về, chạy lệnh \


| <pre><code>sudo chmod +x logstash.sh
sudo ./logstash.sh &#x3C;path-to-file-log>
</code></pre> |
| --------------------------------------------------------------------------------------------- |

* Nếu cài thủ công, chạy lệnh\


| <pre><code>Cài java (>8): sudo yum install jre-1.8.0-openjdk -y
Cài Logstash: sudo rpm -ivh https://artifacts.elastic.co/downloads/logstash/logstash-8.6.0-x86_64.rpm
</code></pre> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
{% endtab %}
{% endtabs %}



Tiếp theo bạn cần cấu hình agent log. Các file cấu hình dưới đều đã được chúng tôi chuẩn bị sẵn tại script khi tải certificate về, mô tả dưới đây giúp người đọc hình dung được nếu tạo manual sẽ thế nào.

#### Cấu hình



{% tabs %}
{% tab title="Filebeat" %}


| <ul><li>File <code>/etc/filebeat/filebeat.yml</code>. Cấu hình dưới đây sẽ lấy tất cả log trong file <code>/var/log/app.log</code> đẩy về vMonitor Platform:</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>filebeat.inputs:
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
</code></pre></td></tr></tbody></table><ul><li><p>Trong đó<br>Tại input đường dẫn tới file log</p><p>Tại output , các biến cần điền bạn lấy từ bước tải certicate ở trên:</p><ul><li><code>$BOOTSTRAP_SERVERS, $TOPIC</code> lấy trong file <a href="http://info.md/">info.md</a></li><li><code>$PATH_FILE_VNG_TRUST_PEM, $PATH_FILE_USER_CER_PEM, $PATH_FILE_USER_KEY_PEM</code> là đường dẫn tới file VNG.trust.pem user.cer.pem user.key.pem</li></ul></li><li>Đọc thêm cấu hình nâng cao khác tại <a href="https://www.elastic.co/guide/en/beats/filebeat/current/configuring-howto-filebeat.html"><img src="https://www.elastic.co/favicon-16x16.png" alt="">Configure Filebeat | Filebeat Reference [8.8] | Elastic</a></li></ul> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>filebeat.inputs:
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
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
{% endtab %}

{% tab title="Logstash" %}


| <ul><li>File <code>/etc/logstash/conf.d/logstash.conf.</code> Cấu hình dưới đây sẽ lấy tất cả log trong file <code>/var/log/app.log</code> đẩy về vMonitor Platform:</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>input {
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
</code></pre></td></tr></tbody></table><ul><li>Trong đó: tại <code>input</code> , nếu như muốn lấy thêm log tại các file khác, cấu hình thêm như sau</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>input {
    file {
        start_position => "beginning"
        path => [ "/var/log/app.log" , "/var/log/backend.log", "/var/log/cmd/*.log"]
    }
}
</code></pre></td></tr></tbody></table><ul><li><p>Tại <code>output</code> , các biến cần điền bạn lấy từ bước tải certicate ở trên:</p><ul><li><code>$BOOTSTRAP_SERVERS $TOPIC $TRUTSTORE_PASS , $USER_PASS</code> lấy trong file <a href="http://info.md/">info.md</a></li><li><code>$PATH_FILE_VNG_TRUST $PATH_FILE_USER_KEY</code>  là đường dẫn tới file VNG.trust, user.key</li></ul></li><li>Đọc thêm cấu hình nâng cao khác tại <a href="https://www.elastic.co/guide/en/logstash/current/setup-logstash.html"><img src="https://www.elastic.co/favicon-16x16.png" alt="">Setting Up and Running Logstash | Logstash Reference [8.8] | Elastic</a></li></ul> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>input {
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
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <pre><code>input {
    file {
        start_position => "beginning"
        path => [ "/var/log/app.log" , "/var/log/backend.log", "/var/log/cmd/*.log"]
    }
}
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
{% endtab %}
{% endtabs %}

***

#### Quản trị



{% tabs %}
{% tab title="Logstash" %}


| <ul><li>Start</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl start logstash
</code></pre></td></tr></tbody></table><ul><li>Enable</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl enable logstash
</code></pre></td></tr></tbody></table><ul><li>Stop</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl stop logstash
</code></pre></td></tr></tbody></table><ul><li>Reload</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl reload logstash
</code></pre></td></tr></tbody></table><ul><li>Restart</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl restart logstash
</code></pre></td></tr></tbody></table><ul><li>Observe</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl status logstash
journalctl -f --unit logstash
tail -f /var/log/logstash
</code></pre></td></tr></tbody></table><ul><li>Uninstall</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>yum remove logstash
</code></pre></td></tr></tbody></table><p><br></p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>systemctl start logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <pre><code>systemctl enable logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <pre><code>systemctl stop logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <pre><code>systemctl reload logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <pre><code>systemctl restart logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <pre><code>systemctl status logstash
journalctl -f --unit logstash
tail -f /var/log/logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <pre><code>yum remove logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
{% endtab %}

{% tab title="Filebeat" %}


| <ul><li>Start</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl start filebeat
</code></pre></td></tr></tbody></table><ul><li>Enable</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl enable filebeat
</code></pre></td></tr></tbody></table><ul><li>Stop</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl stop filebeat
</code></pre></td></tr></tbody></table><ul><li>Reload</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl reload filebeat
</code></pre></td></tr></tbody></table><ul><li>Restart</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl restart filebeat
</code></pre></td></tr></tbody></table><ul><li>Observe</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>systemctl status filebeat
journalctl -f --unit filebeat
tail -f /var/log/filebeat
</code></pre></td></tr></tbody></table><ul><li>Uninstall</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>yum remove filebeat
</code></pre></td></tr></tbody></table><p><br></p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>systemctl start filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <pre><code>systemctl enable filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <pre><code>systemctl stop filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <pre><code>systemctl reload filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <pre><code>systemctl restart filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <pre><code>systemctl status filebeat
journalctl -f --unit filebeat
tail -f /var/log/filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <pre><code>yum remove filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
{% endtab %}
{% endtabs %}

***

\
