# Pfsense trên HCM03

Một giải pháp bảo mật mã nguồn mở với một kernel tùy chỉnh dựa trên hệ điều hành FreeBSD. [pfSense ](https://www.pfsense.org/)là một trong những tường lửa mạng hàng đầu với các tính năng ở mức độ thương mại.\
pfSense có sẵn dưới dạng thiết bị phần cứng, thiết bị ảo và tệp nhị phân có thể tải về (phiên bản cộng đồng).

[Tài liệu chi tiết](https://docs.netgate.com/pfsense/en/latest/index.html) của họ, được giải thích rõ ràng và dễ theo dõi. Ở mức độ cao, một số tính năng đáng chú ý của pfSense bao gồm:

* **Firewall** – Lọc IP/port , giới hạn kết nối, hỗ trợ lớp 2, làm sạch thông tin.
* **Bảng trạng thái (State table)** – theo mặc định tất cả các quy tắc đều có trạng thái, có nhiều cấu hình khác nhau cho việc xử lý trạng thái.
* **Cân bằng tải máy chủ** – tích hợp LB để [phân phối tải ](https://geekflare.com/open-source-load-balancer/)giữa nhiều máy chủ phía sau
* **NAT** (Network address translation) – chuyển tiếp cổng, phản chiếu
* **HA** (High-availability) – chuyển đổi sang thứ cấp nếu thứ cấp chính thất bại
* **Multi-WAN** (wide area network) – sử dụng nhiều kết nối internet
* **VPN** (a virtual private network) – hỗ trợ IPsec và OpenVPN
* **Báo cáo (Reporting)** – Giữ thông tin sử dụng tài nguyên lịch sử
* **Giám sát (Monitoring)** – giám sát thời gian thực
* **DNS Động**– bao gồm nhiều máy client DNS
* **DHCP** & **Relay** sẳn sàng

Nhiều hơn các tính năng của tường lửa thương mại mà bạn có được MIỄN PHÍ.

Thật tuyệt vời, phải không?

Không chỉ vậy, bạn còn có tùy chọn cài đặt các gói chỉ với một cú nhấp chuột..

Ví dụ:

* **Security** – a stunner, snort, tinc, [nmap](https://geekflare.com/port-scanner-server/), arpwatch
* **Monitoring** – iftop, ntopng, softflowd, urlsnarf, darkstat, mailreport
* **Networking** – netio, nut, Avahi
* **Routing** – frr, olsrd, routed, OpenBGPD
* **Services** – iperf, widentd, syslog-ng, bind, acme, imspector, git, dns-server

pfSense trông rất hứa hẹn và đáng để thử. Kiểm tra [Kamatera](https://www.kamatera.com/services/pfsense/?tcampaign=35166\_477840\&bta=35166\&nci=5445) nếu đang tìm kiếm dịch vụ hosting cho pfSense.
