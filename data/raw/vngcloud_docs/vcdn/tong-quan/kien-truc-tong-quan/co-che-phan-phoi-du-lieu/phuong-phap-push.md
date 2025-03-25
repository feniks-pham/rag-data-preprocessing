# Phương Pháp PUSH

**Tín hiệu đầu vào**:

* Khởi tạo một Live Entrypoint nhận tín hiệu. Live Entrypoint hỗ trợ nhiều điểm nhận tại các DC khác nhau và hoạt động theo cơ chế Active-Backup.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

***

**Tín hiệu đầu ra**:

* **Hỗ trợ giao thức HTTPS**: mặc định tất cả CDN được tạo ra trên hệ thống đều hỗ trợ SSL trên domain của CDN. Tuy nhiên khách hàng có thể sử dụng tự upload Certificate của riêng mình để sử dụng với tên bất kì (tham khảo tại phần quản lý certificate).
* **Streaming thông qua HLS** với định dạng: https:// \<CDN Domain>/\<tên kênh>/index.m3u8.
* **Hỗ trợ tín năng Adaptive Bitrate**: Hệ thống packaging tự động gộp các kênh có cùng tên với chất lượng khác nhau thành kênh ABR. Khách hàng có thể tạo nhiều Live Entrypoint và quản lý thông qua giao diện portal.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>
