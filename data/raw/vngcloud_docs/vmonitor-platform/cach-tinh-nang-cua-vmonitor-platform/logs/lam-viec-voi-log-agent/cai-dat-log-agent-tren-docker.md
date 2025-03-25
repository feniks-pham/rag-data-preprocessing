# Cài đặt Log Agent trên Docker

Trước khi thực hiện cài đặt agent trên các hệ điều hành mà chúng tôi hỗ trợ bên dưới, bạn cần phải tải xuống certificate theo hướng dẫn tại [Khởi tạo Certificate](khoi-tao-certificate.md). Thông tin hướng dẫn thiết lập agent nằm trong file readme, các script hướng dẫn cũng nằm trong tệp tin certificate được tải về. Sử dụng thông tin này với các hướng dẫn bên dưới để hoàn thành việc thiết lập Agent for Log.

#### Cài đặt

{% tabs %}
{% tab title="Filebeat" %}
* Tải image

| <pre><code>docker pull docker.elastic.co/beats/filebeat:8.7.0
</code></pre> |
| --------------------------------------------------------------------------- |

***

* [Tải certificate ](https://vngctech.atlassian.net/wiki/spaces/VP/pages/847970312)lấy thông tin xác thực user
* Nếu sử dụng script chuẩn bị sẵn trong thư mục tải về, chạy lệnh:
  * Trong ví dụ thiết lập dưới dây chúng tôi sẽ mount `/var/log/app.log` vào agent cài bằng docker để đẩy log về hệ thống

| <pre><code>docker compose up -d -f docker-compose.yml
</code></pre> |
| ------------------------------------------------------------------- |

Các file cấu hình dưới đều đã được chúng tôi chuẩn bị sẵn tại script khi tải certificate về, mô tả dưới đây giúp người đọc hình dung được nếu tạo manual sẽ thế nào.

#### Cấu hình

| <ul><li>File <code>docker-compose.yml</code></li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>version: "3"
services:
  filebeat-agent-vmonitor:
    image: docker.elastic.co/beats/filebeat:8.7.0
    container_name: filebeat-agent-vmonitor
    restart: always
    env_file:
      - container.env
    volumes:
      -  $PWD/filebeat.yml:/usr/share/filebeat/filebeat.yml
      -  $PWD/VNG.trust.pem:/usr/share/filebeat/VNG.trust:rw
      -  $PWD/user.cer.pem:/usr/share/filebeat/user.cer.pem:rw
      -  $PWD/user.key.pem:/usr/share/filebeat/user.key.pem:rw
      -  /var/log/app.log:/var/log/app.log:ro
      -  /var/log/filebeat/:/var/log/filebeat/
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
    deploy:
      resources:
         limits:
           cpus: '1'
           memory: 2G
</code></pre></td></tr></tbody></table><ul><li>File <code>filebeat.yml</code> . Cấu hình dưới đây sẽ lấy tất cả log được ghi vào file <code>/var/log/app.log</code> về vMonitor Platform:</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>filebeat.inputs:
- type: log
  paths:
    - /var/log/app.log

output.kafka:
  hosts: ${BOOTSTRAP_SERVERS}
  topic: ${TOPIC}
  partition.round_robin:
    reachable_only: false
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
  ssl.certificate_authorities:
    - /usr/share/filebeat/VNG.trust
  ssl.certificate: /usr/share/filebeat/user.cer.pem
  ssl.key: /usr/share/filebeat/user.key.pem
  ssl.verification_mode: "none"
logging.level: info
logging.to_files: true
logging.files:
  path: /var/log/filebeat
  name: filebeat
  keepfiles: 7
  permissions: 0644
</code></pre></td></tr></tbody></table><ul><li>Note : các biến $<code>BOOTSTRAP_SERVERS, $TOPIC</code> ở trên đã nằm sẵn trong <code>container.env</code> file tại thư mục certificate tải về.</li></ul> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>version: "3"
services:
  filebeat-agent-vmonitor:
    image: docker.elastic.co/beats/filebeat:8.7.0
    container_name: filebeat-agent-vmonitor
    restart: always
    env_file:
      - container.env
    volumes:
      -  $PWD/filebeat.yml:/usr/share/filebeat/filebeat.yml
      -  $PWD/VNG.trust.pem:/usr/share/filebeat/VNG.trust:rw
      -  $PWD/user.cer.pem:/usr/share/filebeat/user.cer.pem:rw
      -  $PWD/user.key.pem:/usr/share/filebeat/user.key.pem:rw
      -  /var/log/app.log:/var/log/app.log:ro
      -  /var/log/filebeat/:/var/log/filebeat/
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
    deploy:
      resources:
         limits:
           cpus: '1'
           memory: 2G
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <pre><code>filebeat.inputs:
- type: log
  paths:
    - /var/log/app.log

output.kafka:
  hosts: ${BOOTSTRAP_SERVERS}
  topic: ${TOPIC}
  partition.round_robin:
    reachable_only: false
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
  ssl.certificate_authorities:
    - /usr/share/filebeat/VNG.trust
  ssl.certificate: /usr/share/filebeat/user.cer.pem
  ssl.key: /usr/share/filebeat/user.key.pem
  ssl.verification_mode: "none"
logging.level: info
logging.to_files: true
logging.files:
  path: /var/log/filebeat
  name: filebeat
  keepfiles: 7
  permissions: 0644
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
{% endtab %}

{% tab title="Logstash" %}
* Tải image

| <pre><code><strong>docker pull docker.elastic.co/logstash/logstash-oss:8.6.2
</strong></code></pre> |
| --------------------------------------------------------------------------------------------------- |

| <ul><li>File <code>docker-compose.yml</code></li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>version: "3"
services:
  logstash-agent-vmonitor:
    image: docker.elastic.co/logstash/logstash-oss:8.6.2
    container_name: logstash-agent-vmonitor
    restart: always
    env_file:
      - container.env
    volumes:
      -  $PWD/logstash.conf:/usr/share/logstash/pipeline/logstash.conf
      -  $PWD/VNG.trust:/usr/share/logstash/VNG.trust
      -  $PWD/user.key:/usr/share/logstash/user.key
      -  /var/log/app.log://var/log/app.log:ro
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
    deploy:
      resources:
         limits:
           cpus: '1'
           memory: 2G
</code></pre></td></tr></tbody></table><ul><li>File <code>logstash.conf</code> . Cấu hình dưới đây sẽ lấy tất cả log được ghi vào file <code>/var/log/app.log</code> về vMonitor Platform:</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>input {
    file {
        start_position => "beginning"
        path => [ "/var/log/app.log" ]
    }
}

output {
      kafka {
        codec => json
        bootstrap_servers => "${BOOTSTRAP_SERVERS}"
        topic_id => "${TOPIC}"
        security_protocol => "SSL"
        ssl_truststore_location => "/usr/share/logstash/VNG.trust"
        ssl_truststore_password => "${TRUTSTORE_PASS}"
        ssl_keystore_location => "/usr/share/logstash/user.key"
        ssl_keystore_password => "${KEYSTORE_PASS}"
        ssl_key_password => "${KEYSTORE_PASS}"
        ssl_endpoint_identification_algorithm => ""
      }
}
</code></pre></td></tr></tbody></table><ul><li>Note : các biến <code>$BOOTSTRAP_SERVERS, $TOPIC, $TRUTSTORE_PASS, $USER_PASS</code> ở trên đã nằm sẵn trong container.env file tại thư mục certificate tải về.</li></ul> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>version: "3"
services:
  logstash-agent-vmonitor:
    image: docker.elastic.co/logstash/logstash-oss:8.6.2
    container_name: logstash-agent-vmonitor
    restart: always
    env_file:
      - container.env
    volumes:
      -  $PWD/logstash.conf:/usr/share/logstash/pipeline/logstash.conf
      -  $PWD/VNG.trust:/usr/share/logstash/VNG.trust
      -  $PWD/user.key:/usr/share/logstash/user.key
      -  /var/log/app.log://var/log/app.log:ro
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
    deploy:
      resources:
         limits:
           cpus: '1'
           memory: 2G
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <pre><code>input {
    file {
        start_position => "beginning"
        path => [ "/var/log/app.log" ]
    }
}

output {
      kafka {
        codec => json
        bootstrap_servers => "${BOOTSTRAP_SERVERS}"
        topic_id => "${TOPIC}"
        security_protocol => "SSL"
        ssl_truststore_location => "/usr/share/logstash/VNG.trust"
        ssl_truststore_password => "${TRUTSTORE_PASS}"
        ssl_keystore_location => "/usr/share/logstash/user.key"
        ssl_keystore_password => "${KEYSTORE_PASS}"
        ssl_key_password => "${KEYSTORE_PASS}"
        ssl_endpoint_identification_algorithm => ""
      }
}
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
{% endtab %}
{% endtabs %}

***

#### Quản trị

{% tabs %}
{% tab title="Filebeat" %}


| <ul><li>Stop</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker stop filebeat
</code></pre></td></tr></tbody></table><ul><li>Reload</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker kill --signal=HUP filebeat
</code></pre></td></tr></tbody></table><ul><li>Restart</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker restart filebeat
</code></pre></td></tr></tbody></table><ul><li>Observe</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker logs --tail 100 -f filebeat
</code></pre></td></tr></tbody></table><ul><li>Uninstall</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker rm filebeat
</code></pre></td></tr></tbody></table><p><br></p> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>docker stop filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <pre><code>docker kill --signal=HUP filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <pre><code>docker restart filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <pre><code>docker logs --tail 100 -f filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <pre><code>docker rm filebeat
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
{% endtab %}

{% tab title="Logstash" %}


| <ul><li>Stop</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker stop logstash
</code></pre></td></tr></tbody></table><ul><li>Reload</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker kill --signal=HUP logstash
</code></pre></td></tr></tbody></table><ul><li>Restart</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker restart logstash
</code></pre></td></tr></tbody></table><ul><li>Observe</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker logs --tail 100 -f logstash
</code></pre></td></tr></tbody></table><ul><li>Uninstall</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>docker rm logstash
</code></pre></td></tr></tbody></table><p><br></p> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre><code>docker stop logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <pre><code>docker kill --signal=HUP logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <pre><code>docker restart logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <pre><code>docker logs --tail 100 -f logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <pre><code>docker rm logstash
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
{% endtab %}
{% endtabs %}

***

Trước khi thực hiện cài đặt tác nhân trên các hệ điều hành mà chúng tôi hỗ trợ bên dưới, bạn cần [khoi-tao-certificate.md](khoi-tao-certificate.md "mention"). Thông báo hướng dẫn tác nhân thiết lập nằm trong tệp readme, hướng dẫn tập lệnh cũng nằm trong tệp tin chứng chỉ được tải về. Sử dụng thông tin này với các hướng dẫn bên dưới để hoàn thành việc thiết lập Agent for Log.
