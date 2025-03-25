# Giám sát hoạt động vDB bằng vMonitor Platform

Giám sát hoạt động (monitoring) là một nhu cầu bắt buộc đối với mọi hệ thống. Tại VNG Cloud, bạn có thể giám sát vDB bằng cách sử dụng dịch vụ vMonitor Platform.

vMonitor Platform là một dịch vụ Monitoring as a Service giúp thu thập các chỉ số sức khỏe (metric), bản ghi hoạt động (log) của các resource trên VNG Cloud (hoặc ngoài VNG Cloud). Bên cạnh đó, bạn có thể vẽ các dashboard trực quan, thiết lập cảnh báo (alarm) và gửi thông báo (notification) khi xảy ra sự cố. Chi tiết về dịch vụ này bạn có thể tham khảo tại: [vMonitor Platform](../../vmonitor/).

Để bắt đầu sử dụng, bạn truy cập vMonitor Platform, mục Infrastructure List, tab vDB tại link: [vMonitor Infrastructure List > vDB.](https://hcm-3.console.vngcloud.vn/vmonitor/infrastructure/vdb) Bạn tham khảo mô tả tại: [Làm việc với vDB - Metric](../../vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/metrics/lam-viec-voi-product-metric/lam-viec-voi-vdb-metric.md)

Hiện tại, vMonitor Platform cho phép bạn xem metric của tất cả vDB Instance bằng default dashboard (dashboard được hệ thống tự động vẽ sẵn với tập metric giới hạn) và retention 1 ngày hoàn toàn miễn phí. Để có thể vẽ các dashboard với số lượng metric không giới hạn, xem metric với retention dài hơn, tạo các alarm cảnh báo khi mức độ sử dụng (resource usage) cpu, memory, disk, connections, buffer,... đạt ngưỡng nguy hiểm, bạn cần Enable detailed Monitoring. Việc này yêu cầu bạn cần đăng kí gói (Quota) với vMonitor Platform. Bạn tham khảo tại: [Làm việc với Metric Quota](../../vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/metrics/lam-viec-voi-metric-quota.md).

\


Sau khi Enable detailed Monitoring, bạn có thể Clone default dashboard ra và vẽ thêm các Widget khác theo nhu cầu hoặc tạo các dashboard mới. [Dashboard](../../vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/dashboard/).

Lúc này, bạn có thể chọn các metric của vDB với format: vdb.\<tên\_engine>.\<tên\_metric>. VD: vdb.cpu.percent, [vdb.mysql.net](http://vdb.mysql.net/).threads\_connected,vdb.postgresql.rows\_inserted,...

Các metric của vDB hỗ trợ tập dimension sau giúp bạn filter metric của từng vDB Instance theo ID, tên, loại Engine, phiên bản phù hợp:

* database\_id: ID của vDB Instance.
* database\_name: Name của vDB Instance.
* engine: loại engine như MySQL, Mariadb, Postgresql, Redis.
* version: phiên bản của Engine.
* zone: Zone của resource như HCM-03.

\


Bạn cũng có thể tạo các alarm với các metric này. [Thiết lập cảnh báo cho Metric](https://docs.vngcloud.vn/pages/viewpage.action?pageId=31555671)

Đối với các vDB quan trọng, VNG Cloud khuyến khích bạn tạo tối thiểu các alarm sau:&#x20;

* Cpu usage: mức độ % sử dụng CPU của vDB Instance. Sử dụng metric vdb.cpu.percent , ngưỡng cảnh báo tham khảo: >80%, >90%, >100%.
* Memory usable: mức độ % Memory khả dụng của vDB Instance. Sử dụng metric vdb.mem.usable\_perc, ngưỡng cảnh báo tham khảo: <20%, <10%
* Disk usage: mức độ % sử dụng Disk của vDB Instance. Sử dụng metric vdb.disk.space\_used\_perc, ngưỡng cảnh báo tham khảo: >80%, >90%, >100%.

\
