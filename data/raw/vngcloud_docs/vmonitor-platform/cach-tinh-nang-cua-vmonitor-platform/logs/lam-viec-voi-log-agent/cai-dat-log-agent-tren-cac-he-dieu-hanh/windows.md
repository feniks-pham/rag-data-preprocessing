# Windows

Trước khi thực hiện cài đặt agent trên các hệ điều hành mà chúng tôi hỗ trợ bên dưới, bạn cần phải tải xuống certificate theo hướng dẫn tại [Khởi tạo Certificate](../khoi-tao-certificate.md). Trong tệp tải xuống sẽ chứa các certificate được sử dụng để xác thực với hệ thống vMonitor Logs. Sử dụng thông tin này với các hướng dẫn bên dưới để hoàn thành việc thiết lập Agent for Log.

#### Cài đặt

Xác định một loại agent mà mình muốn cài và làm theo hướng dẫn của agent đó dưới đây:

{% tabs %}
{% tab title="Filebeat" %}
| <ul><li>Tải filebeat tại <a href="https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.7.1-windows-x86_64.zip">https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.7.1-windows-x86_64.zip</a></li><li>Giải nén thư mục filebeat vừa tải xuống</li><li>Sao chép các file user.cer.pem, user.key.pem, VNG.trust.pem từ thư mục certificate vào thư mục filebeat đã giải nén. giả sử dưới đây chúng tôi đã giải nén filebeat vào thư mục <code>C:\filebeat-8.7.1-windows-x86_64</code></li><li>Chạy thủ công câu lệnh bên dưới với PowerShell</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>cd C:\filebeat-8.7.1-windows-x86_64
.\filebeat.exe -c .\filebeat.yml
</code></pre></td></tr></tbody></table><ul><li>Trong đó:<br>Trong file filebeat.yml, chúng tôi đã thiết lập ví dụ trong thư mục certificate tải về như dưới để đẩy nội dung file C:\agent.log về hệ thống.</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>filebeat.inputs:
- type: log
  paths:
    - C:\agent.log

output.kafka:
  hosts: ["$BOOTSTRAP_SERVERS"]
  topic: $TOPIC
  partition.round_robin:
    reachable_only: false
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
  ssl.certificate_authorities:
    - $PATH_FILE_VNG_TRUST_PEM
  ssl.certificate: $PATH_FILE_USER_CER_PEM
  ssl.key: $PATH_FILE_USER_KEY_PEM
  ssl.verification_mode: "none"
logging.level: info
logging.to_files: true
logging.files:
  path: /var/log/filebeat
  name: filebeat
  keepfiles: 7
  permissions: 0644
</code></pre></td></tr></tbody></table><p>Trong đó:</p><ul><li>Tại <code>input</code> đường dẫn tới file log</li><li><p>Tại <code>output</code> , các biến cần điền bạn lấy từ bước tải certicate ở trên:</p><ul><li><code>$BOOTSTRAP_SERVERS, $TOPIC</code> lấy trong file <a href="http://info.md/">info.md</a></li><li><code>$PATH_FILE_VNG_TRUST_PEM,$PATH_FILE_USER_CER_PEM,$PATH_FILE_USER_KEY_PEM</code> là đường dẫn tới file VNG.trust.pem user.cer.pem user.key.pem</li></ul></li></ul><p>Cài đặt service chạy background:</p><p>Trên powershell khi đã vào đường dẫn filebeat</p><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>.\install-service-filebeat.ps1
</code></pre></td></tr></tbody></table><p>Chúng tôi khuyên bạn nên thử chạy thủ công thành công trước để xác định vấn đề nếu có.</p> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
{% endtab %}

{% tab title="Logstash" %}


| <ul><li>Tải <a href="https://learn.microsoft.com/en-us/java/openjdk/download">Download the Microsoft Build of OpenJDK</a> file zip và giải nén . Tối thiểu yêu cầu jdk11.</li><li>Sau khi cài xong, thêm biến môi trường LS_JAVA_HOME . Mở powershell với quyền administrator chạy lệnh dưới ( giả sử bước trên bạn đã giải nén vào C:\Program Files (x86)\Java\ ) :</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>SETX /m PATH "$env:PATH;C:\Program Files (x86)\Java\jdk-11.0.3\bin;"
SETX /m LS_JAVA_HOME "C:\Program Files (x86)\Java\jdk-11.0.3"

## In some environments you must replace "Program Files (x86)" by progra~2, like: 
## SETX /m LS_JAVA_HOME "C:\progra~2\Java\jdk"
</code></pre></td></tr></tbody></table><ul><li>Kiểm tra</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>Java --verison

java version "11.0.3" 2019-04-16 LTS
Java(TM) SE Runtime Environment 18.9 (build 11.0.3+12-LTS)
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.3+12-LTS, mixed mode)
</code></pre></td></tr></tbody></table><p>Cài logstash:</p><ul><li>Tải <a href="https://www.elastic.co/downloads/past-releases/logstash-8-6-2"><img src="https://www.elastic.co/favicon-16x16.png" alt="">Logstash 8.6.2</a> và giải nén.</li><li>Coppy các file logstash.conf, user.key, VNG.trust từ thư mục certificate vào thư mục config vừa giải nén. giả sử dưới đây chúng tôi đã giải nén logstash vào thư mục <code>C:\logstash-8.6.2</code></li><li>Chạy thủ công , mở PowerShell</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>cd C:\logstash-8.6.2
.\bin\logstash.bat -f .\config\logstash.conf
</code></pre></td></tr></tbody></table><ul><li>Trong đó:<br>Trong file logstash.conf, chúng tôi đã thiết lập ví dụ như dưới để đẩy nội dung file C:\install.log về hệ thống.</li></ul><table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><pre><code>input {
    file {
        path => ["C:/install.log"]		
	}
	stdin{}
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
</code></pre></td></tr></tbody></table><ul><li>Chạy ngầm bằng Task Scheduler</li></ul><p>Chúng tôi khuyên bạn nên thử chạy thủ công thành công trước để xác định vấn đề nếu có. Tham khảo thêm tại <a href="https://www.elastic.co/guide/en/logstash/8.6/running-logstash-windows.html#running-logstash-windows-scheduledtask">Running Logstash on Windows | Logstash Reference [8.6] | Elastic</a>.</p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
{% endtab %}
{% endtabs %}

***

\
