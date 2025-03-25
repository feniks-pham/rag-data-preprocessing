# Lưu ý & hạn chế cho Pfsense

## Default MTU: <a href="#luuy-and-hanchechopfsense-defaultmtu" id="luuy-and-hanchechopfsense-defaultmtu"></a>

Default MTU của Pfsense là **1500**. Bạn cần chỉnh thông số này cho phù hợp cấu hình của VNG Cloud là **1450**.

* **Bước 1:** Truy cập vào giao diện quản lý của pfsense, chọn tab interfaces và cấu hình lần lượt cho mạng WAN (hoặc LAN đang sử dụng).

<figure><img src="../../../../.gitbook/assets/image (685).png" alt=""><figcaption></figcaption></figure>

* **Bước 2:** Tại mục MTU, bạn điền thông số 1450.

Cuối cùng, nhấn _**Save**_ để lưu lại cấu hình.

Bạn thực hiện lần lượt cho các Interfaces đang sử dụng.

Nếu có khó khăn trong quá trình sử dụng, vui lòng liên hệ VNGCloud Support.
