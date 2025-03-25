# Log mapping

Việc tập trung log từ các công nghệ và ứng dụng khác nhau có thể tạo ra hàng chục hoặc hàng trăm thuộc tính khác nhau trong môi trường quản lý log đặc biệt là khi nhiều team đang cùng làm việc trong một môi trường.

Chẳng hạn như thông tin tên máy chủ Host có thể có nhiều tên khác như beat.hostname, hostname, host, syslog.hostname,...

Để thống nhất tên gọi cho các thuộc tính này, hãy sử dụng Log mapping. Log mapping được chúng tôi định nghĩa sẵn thông qua các thuộc tính thường gặp bao gồm:

<table data-header-hidden><thead><tr><th width="211"></th><th></th></tr></thead><tbody><tr><td><strong>Portal reserved attributes</strong></td><td><strong>System fields</strong></td></tr><tr><td>Content</td><td>message, request.body</td></tr><tr><td>Date</td><td>date, Timestamp, @timestamp, syslog.timestamp, eventTime, published_date, _timestamp, timestamp</td></tr><tr><td>Host</td><td>beat.hostname, hostname, host, syslog.hostname</td></tr><tr><td>Service</td><td>fields.service, service, syslog.appname</td></tr></tbody></table>

Nếu bạn muốn thêm mapping cho một thuộc tính nào đó, hãy liên hệ với chúng tôi. Việc thêm thuộc tính Log mapping này có thể được chúng tôi đáp ứng nếu thuộc tính mapping của bạn là hợp lý thông qua sự xem xét của chúng tôi.

\
