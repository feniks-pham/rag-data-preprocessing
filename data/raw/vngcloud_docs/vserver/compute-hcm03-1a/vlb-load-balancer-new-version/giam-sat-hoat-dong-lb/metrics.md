# Metrics

### **vLB - Metric** <a href="#metrics-vlb-metric" id="metrics-vlb-metric"></a>

Hiện tại, vMonitor Platform cho phép bạn xem metric của tất cả vLB Instance bằng default dashboard (dashboard được hệ thống tự động vẽ sẵn với tập metric giới hạn) và retention 1 ngày hoàn toàn miễn phí. Để có thể vẽ các dashboard với số lượng metric không giới hạn, xem metric với retention dài hơn, tạo các alarm cảnh báo khi các chỉ số connections, response 5xx, response 4xx,... đạt ngưỡng nguy hiểm, bạn cần Enable detailed Monitoring. Việc này yêu cầu bạn cần đăng kí gói (Quota) với vMonitor Platform. <mark style="color:orange;">Bạn tham khảo tại:</mark> [<mark style="color:orange;">Quota & Usage: Mua gói Metric</mark>](../../../../vmonitor-platform/bat-dau-voi-vmonitor-platform/bat-dau-voi-metrics.md)<mark style="color:orange;">.</mark>

<mark style="color:orange;">Sau khi Enable detailed Monitoring, bạn có thể Clone default dashboard ra và vẽ thêm các Widget khác theo nhu cầu hoặc tạo các dashboard mới.</mark> [<mark style="color:orange;">Tạo Dashboard và Widget mới</mark>](../../../../vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/dashboard/)<mark style="color:orange;">.</mark>

Lúc này, bạn có thể chọn các metric của vLB với format: vlb.\<tên\_metric>. VD: vlb.listener.bin, vlb.listener.bout, vlb.listener.hrsp\_5xx,...

**Các metric của vLB hỗ trợ tập dimension sau giúp bạn filter metric của từng vLB Instance theo ID, tên, layer, listener, pool,...phù hợp:**

* loadbalancer\_id: ID của vLB Instance.
* loadbalancer\_name: Name của vLB Instance.
* layer: 4 hoặc 7, tương ứng Network Load balancer hoặc Application Load Balancer.
* role: Standalone (nếu vLB bạn thuộc Gen cũ), Master/Backup (nếu vLB bạn thuộc Gen mới).
* zone: Zone của resource như HCM-03.
* listener\_id: ID của Listener
* listener\_name: Name của Listener
* pool\_id: ID của pool
* pool\_name: Name của pool.
* member\_id: ID của member

<mark style="color:orange;">Bạn cũng có thể tạo các alarm với các metric này.</mark> [<mark style="color:orange;">Thiết lập cảnh báo cho Metric</mark>](../../../../vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/alarm/metric-alarm.md)

