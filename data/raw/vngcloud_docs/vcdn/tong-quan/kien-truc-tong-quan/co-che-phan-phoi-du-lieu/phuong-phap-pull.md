# Phương Pháp PULL

**Tín hiệu đầu vào:**

* Hệ thống Media Preparation của VNGCloud sẽ kéo nội dung streaming dưới định dạng HLS/MpegDash đã được packaging trước từ server của khách hàng. Bao gồm cả định dạng hỗ trợ ABR và Multiple Audio.
* Hệ thống sẽ đưa nội dung đến tất cả các edge trong mạng lưới chủ động để luôn sẵn sàng khi user gọi đến.
* Người dùng cuối sẽ lấy nội dung với định dạng HLS/MpegDash từ server Edge.

***

**Tín hiệu đầu ra:**

* Hỗ trợ giao thức HTTPS: mặc định tất cả CDN được tạo ra trên hệ thống đều hỗ trợ SSL trên domain của CDN. Tuy nhiên khách hàng có thể sử dụng tự upload Certificate của riêng mình để sử dụng với tên bất kì (tham khảo tại phần quản lý certificate).
