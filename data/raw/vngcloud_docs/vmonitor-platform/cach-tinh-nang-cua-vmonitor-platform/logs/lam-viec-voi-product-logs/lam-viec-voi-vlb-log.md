# Làm việc với vLB-Log

Để xem được logs của vLB bạn truy cập vào vMonitor Platform tại [link](https://hcm-3.console.vngcloud.vn/vmonitor), sau đó vào mục **Infrastructure list/vLB Log.** Tại đây, bạn có thể xem danh sách tất cả vLB trên HCM03 của bạn. Tại màn hình này, bạn sẽ thấy các cột thông tin cơ bản như:

* **vLB Project**: tên của vLB.
* **Log Project**: log project sẽ chứa logs của vLB khi bạn enable "Detailed Monitoring".
* **Log Project Usage**: thông tin về mức độ sử dụng của Log Project mà bạn đã gắn vào vLB này.
* **Monitoring Status**: trạng thái monitoring của vLB. Nếu chưa enable "Detailed Monitoring" thì trạng thái sẽ là INACTIVE, nếu đã enable thì trạng thái là ACTIVE, còn nếu vLB đã bị xóa thì sẽ là DELETED.
* **Detailed Monitoring**: kích hoạt hay hủy theo dõi Logs của vLB này.

<figure><img src="../../../../.gitbook/assets/image (332).png" alt=""><figcaption></figcaption></figure>

Để kích hoạt theo dõi, bạn cần nhấn **enable** tại cột **Detailed Monitoring.**&#x20;

Hệ thống sẽ hiển thị Popup và bạn cần **chọn Log Project** để chứa logs của vLB này, sau đó nhấn "**enable**".  Nếu bạn chưa có bất kì Log Project nào, bạn có thể nhấn "Create a log project" ở popup hoặc qua tab Quota & Usage để tạo Log Project trước.

Sau khi enable bạn sẽ thấy status của vLB  này chuyển thành **ACTIVE**, và bạn có thể truy cập vào Log Project vừa chọn để xem logs.

Nếu có nhu cầu thay đổi Log Project chứa Logs, bạn có thể chọn nút 3 chấm và chọn "**Edit Log Project**" để thay đổi.

Nếu không còn nhu cầu để xem logs của vLB  thì bạn có thể **disable** ở cột **Detailed Monitoring**.

***

## Các fields dữ liệu: <a href="#lamviecvoivlb-log-cacfieldsdulieu" id="lamviecvoivlb-log-cacfieldsdulieu"></a>

Đối với Application Load Balancer, bạn sẽ xem được HTTP Access Logs với các fields:

* httpRequest.clientIp
* httpRequest.clientPort
* httpRequest.requestMethod
* httpRequest.requestUrl
* httpRequest.requestSize
* httpRequest.responseSize
* httpRequest.status
* httpRequest.latency
* httpRequest.userAgent
* httpRequest.referer

Đối với Network Load Balancer, bạn sẽ xem được TCP Connection Logs với các fields:

* jsonPayload.connection.clientIp
* jsonPayload.connection.clientPort
* jsonPayload.connection.requestSize
* jsonPayload.connection.responseSize
* jsonPayload.connection.rtt

***

### Một số chú ý: <a href="#lamviecvoivlb-log-motsochuy" id="lamviecvoivlb-log-motsochuy"></a>

* vLB sau khi được tạo sẽ mất khoảng vào phút (tối đa 10 phút) để có thể đồng bộ về vMonitor Platform.
