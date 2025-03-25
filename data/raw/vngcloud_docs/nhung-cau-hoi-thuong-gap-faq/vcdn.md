# vCDN

### \[vCDN] Tôi tạo CDN như thế nào?

Quý khách vui lòng xem tài liệu theo Link hướng dẫn: [Hướng dẫn khởi tạo](../vcdn/loai-hinh-dich-vu.md)

### \[vCDN] CDN/Live-Stream tính tiền như thế nào, khi hết Volume thì có bị disable CDN ngay luôn không?

Quý khách mua volume CDN để sử dụng, nếu hết dung lượng domain sẽ bị disable, thông tin volume còn lại được thể hiện ở CDN Remain.

### \[vCDN] Làm sao để sử dụng livestreaming?

Quý khách vui lòng xem tài liệu theo Link hướng dẫn [tại đây](../vcdn/loai-hinh-dich-vu/live-streaming.md)

### \[vCDN] Tôi có thể xem traffic sử dụng CDN của tôi không?

VNGCloud cung cấp chart theo từng domain để xem traffic đang sử dụng. Click chọn vào từng domain để xem chi tiết

### \[vCDN] Làm sao tôi xóa cache trên CDN?

Trên portal có purge cache cho từng domain riêng, quý khách có thể vào để xóa cache trên CDN

### \[vCDN] Làm thế nào để xóa CDN domain?

Quý khách không thể xóa CDN domain mà quý khách chỉ có thể edit lại.

### \[vCDN] Tôi muốn biết Range IP tương ứng với 2 domain (bskjv7x1zq.vcdn.com.vn và ggkiz9mkp.vcdn.com.vn)

Hệ thống CDN của VNGCloud bao gồm nhiều range IP, để đảm bảo tính sẵn sàng cũng như dự phòng các vùng khác nhau phục vụ cho CDN, vì vậy không tồn tại một số range IP cụ thể cho riêng domain CDN nào.

### \[vCDN] \[CDN/Live-Stream] tính tiền như thế nào, khi hết \[Volume] thì có bị \[disable] \[CDN] ngay luôn không?

User mua volume CDN để sử dụng, nếu hết dung lượng domain sẽ bị disable, thông tin volume còn lại được thể hiện ở CDN Remain.

### \[vCDN] Tôi có thể xem traffic sử dụng \[CDN] của tôi không ?

Hiện tại VNG Cloud có cung cấp từng chart theo từng domain để xem traffic đang sử dụng. Click chọn vào từng domain để xem chi tiết [tại đây](../vcdn/bao-cao.md).

### \[vCDN] Làm sao tôi \[xóa cache] trên \[CDN]?

Trên portal có nút purge cache cho từng domain riêng, có thể vào để xóa cache trên CDN

### \[vCDN] Làm thế nào để xóa CDN domain?

Hiện tại VNG Cloud không hỗ trợ xóa các CDN domain. Nếu anh chị không có nhu cầu sử dụng thì có thể disable domain đó đi.

### \[vCDN] Hướng dẫn tôi sử dụng SSL

Hiện tại VNg Cloud có hỗ trợ chọn SSL certificate:\
\- Default CDN certificate (\*.[vcdn.com.vn](http://vcdn.com.vn/)): Anh chị sử dụng certificate của VNG Cloud.\
\- Custom SSL certificate: anh chị tự upload cert và key của mình lên để xài. SSL certificate anh chị có thể liên hệ các website bán trên mạng hoặc nơi khách hàng mua domain.\
Ngoài ra anh chị cso thể kiểm tra cert và key đúng chưa tại link sau :\
[https://www.sslchecker.com/matcher](https://www.sslchecker.com/matcher) )

### \[vCDN] "Tôi cần hỗ trợ cung cấp dải IP CDN của VNG Cloud

Dưới đây là danh sách các dải IP của CDN của VNG Cloud : 113.164.15.32/28 113.164.15.80/29; 113.164.241.176/28 113.164.14.192/27 171.244.128.0/27 171.244.16.224/27 42.115.221.64/27 43.239.149.128/28 118.69.83.64/27 118.69.83.160/28 118.69.84.64/28 210.245.38.64/27 210.245.26.0/24 42.115.221.128/27 14.225.2.32/28 14.225.10.64/28 171.244.28.64/27 61.28.226.48/28 14.225.10.64/28 171.244.28.64/27 61.28.231.126/32

### \[vCDN]Thay đổi thông số manifest file CDN

Hiện tại VNG Cloud có hỗ trợ thay đổi thông số manifest file CDN

### \[vCDN] Tôi sử dụng vCDN để upload VOD lên web nhưng lại bị lỗi 404

Nhờ khách hàng kiểm tra lại nguồn phát Video, đây là lỗi không tìm thấy nguồn phát. Có thể khách hàng đã upload sai key hoặc nguồn phát.

### \[vCDN] vCDN có hỗ trợ API để upload file lên CDN tương tự như AWS S3 không?

Khách hàng có thể tham khảo thêm dịch vụ vStorage để sử dụng kết hợp với vCDN, tương tự như AWS S3.

### \[vCDN] "Tôi vừa cài đặt xong chứng chỉ SSL trên máy chủ của tôi. Làm thế nào để tôi kiểm tra ngày hết hạn của SSL và các thông tin khác? "

Quý khách hàng lên 1 trong các trang bên dưới để check:\
Digicert: [http://www.digicert.com/help/](http://www.digicert.com/help/)\
Thawte: [https://search.thawte.com/support/ssl-digital-certificates/index?page=content\&id=SO9555](https://search.thawte.com/support/ssl-digital-certificates/index?page=content\&id=SO9555)\
Verisign: [https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content\&id=AR1130](https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content\&id=AR1130)\
RapidSSL: [https://knowledge.rapidssl.com/support/ssl-certificate-support/index?page=content\&id=SO9556](https://knowledge.rapidssl.com/support/ssl-certificate-support/index?page=content\&id=SO9556)\
GeoTrust: [https://knowledge.geotrust.com/support/knowledge-base/index?page=content\&id=SO9557](https://knowledge.geotrust.com/support/knowledge-base/index?page=content\&id=SO9557)

### \[vCDN] Tôi muốn dùng thử CDN thì có cần tốn phí gì không?

Khi đăng ký account VNG Cloud và dùng thử thì quý khách được mặc định miễn phí 100GB để sử dụng CDN ngoài ra sẽ không bị tốn thêm phí. Lưu ý account trial thì chỉ tạo được 1 domain CDN.

### \[vCDN] Tôi đang sử dụng tài khoản trial CDN remaind của tôi còn 5000GB không biết khi tắt trial thì CDN remaind của tôi có bị mất không?

Khi tắt trial thì CDN remain của Khách hàng sẽ vẫn còn nguyên không thay đổi . Chỉ mất 100GB CDN tặng khi sử dụng ban đầu.

### \[vCDN] Tại sao tôi chỉ có thể tạo 1 domain CDN?

Anh chị vui lòng kiểm tra lại portal của mình có phải đang ở trạng thái là trial không? Nếu trial thì VNG Cloud chỉ hỗ trợ tạo 1 domain CDN thôi ạ

### \[vCDN] Tại sao tôi cấu hình xong CDN nhưng khi chạy trên web thì báo lỗi 502?

Anh/chị vui lòng kiểm tra link original của anh/chị và kiểm tra link CND xem có được không . Nếu 2 link đều giống nhau thì CDN trả về đúng còn khác nhau thì anh/chị vui lòng kiểm tra lại dã clear cache chưa. Nếu bị lỗi 502 thì nhờ anh/chị vui lòng allow list range IP : 113.164.15.32/28 113.164.15.80/29; 113.164.241.176/28 113.164.14.192/27 171.244.128.0/27 171.244.16.224/27 42.115.221.64/27 43.239.149.128/28 118.69.83.64/27 118.69.83.160/28 118.69.84.64/28 210.245.38.64/27 210.245.26.0/24 42.115.221.128/27 14.225.2.32/28 14.225.10.64/28 171.244.28.64/27 61.28.226.48/28 14.225.10.64/28 171.244.28.64/27 61.28.231.126/32 Sau khi allow xong thì kiểm tra lại link CDN xem đã được chưa.
