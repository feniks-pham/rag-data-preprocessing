# Danh sách Metrics hỗ trợ

### Linux/ Windows metrics <a href="#danhsachmetricshotro-linux-windowsmetrics" id="danhsachmetricshotro-linux-windowsmetrics"></a>

Metric Agent của vMonitor Platform được xây dựng dựa trên phần mêm mã nguồn mỡ Telegraf, mặc định khi cài đặt Metric Agent, chúng tôi sẽ mở sẵn các input plugin như:&#x20;

* system
* disk
* kernel
* net
* diskio
* mem
* processes
* swap
* cpu

Bạn có thể xem thông tin chi tiết các Metric, Unit của các plugin trên tại [đây](https://github.com/influxdata/telegraf/tree/master/plugins/inputs), đồng thời bạn có thể mở thêm các input plugin để đẩy thêm Metric về vMonitor.

***

### Product metrics <a href="#danhsachmetricshotro-productmetrics" id="danhsachmetricshotro-productmetrics"></a>

Khi các Resource trên VNG Cloud được tạo, mặc định sẽ có 2 loại monitor: Basic và Detail

<table data-header-hidden><thead><tr><th width="204"></th><th></th></tr></thead><tbody><tr><td><strong>Monitoring type</strong></td><td><strong>Mô tả</strong></td></tr><tr><td><p><strong>Basic monitoring</strong></p><p>(Mặc định)</p></td><td><ul><li>Ở chế độ này, sẽ có một số lượng metric mặc định được đẩy về và lưu trữ trên hệ thống vMonitor Platform. Chi tiết tham khảo bảng thông số chi tiết bên dưới.</li><li>Dữ liệu có sẵn tự động trong khoảng thời gian 1 phút.</li></ul></td></tr><tr><td><p><strong>Detailed monitoring</strong></p><p>(Nâng cao)</p></td><td><ul><li>Ở chế độ này, tất cả các metric đang có trên Resource được đẩy về và lưu trữ trên hệ thống vMonitor Platform. Chi tiết tham khảo bảng thông số chi tiết bên dưới.</li><li>Dữ liệu có sẵn tự động trong khoảng thời gian 1 phút.</li></ul></td></tr></tbody></table>

Để biết mỗi loại monitoring bạn có thể làm những gì, vui lòng tham khảo tại [Danh sách Metrics hỗ trợ](danh-sach-metrics-cua-host.md).
