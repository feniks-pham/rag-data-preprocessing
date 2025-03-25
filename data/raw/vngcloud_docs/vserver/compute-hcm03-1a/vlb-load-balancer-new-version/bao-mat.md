# Bảo mật

Load Balancers đóng vai trò then chốt trong việc quản lý và phân phối lưu lượng mạng, là thành phần quan trọng của hệ thống của bạn. Tuy nhiên, việc ưu tiên an ninh cho Load Balancer là điều cực kỳ quan trọng để bảo vệ cơ sở hạ tầng của bạn trước những mối đe dọa tiềm ẩn. Dưới đây là một số điều cần xem xét về an ninh và các tính năng/dịch vụ mà VNG Cloud cung cấp để hỗ trợ khách hàng triển khai bảo mật cho hạ tầng Load Balancers của mình:

1. **Kiểm Soát Truy Cập:** Hạn chế truy cập vào cấu hình và giao diện quản lý của Load Balancer. Sử dụng các phương pháp xác thực và phân quyền mạnh như:
   * Xác thực 2 bước (2FA): Tham khảo thêm tại [Thiết lập xác thực 2 lớp](../../../huong-dan-su-dung-kenh-partner-portal/thiet-lap-chiet-khau-cho-khach-hang.md)
   * Hạn chế truy cập chỉ cho những người được ủy quyền: Tham khảo thêm tại [Identity and Access Management (IAM)](../../../identity-and-access-management-iam.md)
2. **Cập Nhật và Khắc Phục Lỗi Portal Thường Xuyên:**&#x20;
   * VNG Cloud khuyến nghị quý khách hàng luôn chú ý đến các cập nhật mới cho Load Balancer.
   * Các bản cập nhật sẽ là bản nâng cấp về cả tính năng, bảo mật và UI/UX cho Load Balancer
3. **Mã Hóa:** Sử dụng các phương pháp mã hóa như SSL/TLS để bảo vệ dữ liệu được truyền qua Load Balancer. Điều này đảm bảo thông tin nhạy cảm được bảo vệ khỏi việc nghe trộm và chặn bắt. Các tính năng này đã được hỗ trợ tại dịch vụ Load Balancer của VNG Cloud, cùng tìm hiểu thêm tại:
   * Bật sticky session: [Enable sticky session](application-load-balancer/pool/enable-sticky-session.md)
   * Bật mã hóa TLS: [Enable TLS encryption](application-load-balancer/pool/enable-tls-encryption.md)
4. **Giám Sát và Ghi Log:** Triển khai các cơ chế giám sát và ghi log toàn diện để theo dõi mô hình lưu lượng, phát hiện bất thường và xác định các vi phạm an ninh tiềm ẩn kịp thời. Tìm hiểu thêm tại:
   * Giám sát Load balancers: [Monitor your load balancers](application-load-balancer/quan-ly-vlb.md)
5. **Quy Tắc Tường Lửa:** Cấu hình quy tắc tường lửa và kiểm soát truy cập để lọc lưu lượng vào và ra. Tạo ra các quy tắc để chỉ cho phép lưu lượng cần thiết thông qua Load Balancer. VNG Cloud cũng đã cung cấp các tính năng hỗ trợ cho việc kiểm soát và lọc truy cập thông qua việc:
   * Cài đặt yêu cầu, điều kiện tiếp nhận và điều hướng lưu lượng: [Listener Policies](application-load-balancer/listener/listener-policies.md)
   * Cho phép truy cập từ địa chỉ IP nguồn được xác định trước: [Config IP whitelist to load balancer](application-load-balancer/listener/config-ip-whitelist-to-load-balancer.md)
6. **Kiểm Tra An Ninh Thường Xuyên:** Tiến hành các kiểm tra và đánh giá an ninh định kỳ để đánh giá tình hình an ninh của Load Balancer và xác định các điểm cần cải thiện.&#x20;
   * Đội ngũ VNG Cloud luôn tiến hành và kiểm tra an nình định kỳ trên các dịch vụ/tài nguyên của quý khách hàng để đảm bảo tính bảo mật cũng như an toàn thông tin.
   * VNG Cloud cũng khuyến nghi quý khách hàng nên có sự chủ động trong việc kiểm tra an nình thường xuyên trên các dịch vụ/tài nguyên đang sử dụng tại VNG cloud.

Bằng việc chú ý đến các biện pháp an ninh này, quý khách hàng có thể nâng cao đáng kể bảo vệ cho Load Balancer và củng cố an ninh mạng tổng thể.

\
