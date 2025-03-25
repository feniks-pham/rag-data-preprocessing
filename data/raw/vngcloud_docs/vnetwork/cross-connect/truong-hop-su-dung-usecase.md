# Trường hợp sử dụng (Use Case)

Giả sử một Doanh nghiệp có hai chi nhánh, một chi nhánh tại Hồ Chí Minh, một chi nhánh tại Hà Nội, hệ thống sẵn có VPC ở region Hồ Chí Minh và VPC ở region Hà Nội, để cho phép hai chi nhánh này giao tiếp với nhau thông qua kết nối mạng riêng, nên khi đó kết nối Cross Connect sẽ liên kết hai VPC của hai chi nhánh Hồ Chí Minh và Hà Nội với nhau.

### Giải pháp thực hiện

1. Tại mỗi chi nhánh có VPC riêng (nếu chưa có thì cần phải tạo ít nhất một VPC ở mỗi chi nhánh)
2. Tạo kết nối Cross Connect giữa Hồ Chí Minh và Hà Nội;
3. Chọn và mua gói băng thông phù hợp liên kết giữa 2 vùng;
4. Tạo liên kết hai VPC thông qua kết nối Cross Connect;
5. Thiết lập kết nối giao tiếp thông qua hai VPC của Cross Connect.

### Ưu điểm

* Dễ dàng sử dụng: với vài bước đơn giản, doanh nghiệp có thể thiết lập kết nối liên vùng giữa các VPC;
* Hiệu suất cao: Cross Connect tận dụng cơ sở hạ tầng mạng toàn cầu của VNG Cloud để cung cấp kết nối chất lượng cao, độ trễ thấp với băng thông có thể điều chỉnh linh hoạt để đáp ứng với nhu cầu kinh doanh thay đổi.

### Hạn chế

* Một kết nối Cross Connect không thể tạo ra giữa các VPC có trùng CIDR với nhau.
* Sự điều chỉnh băng thông kết nối giữa các vùng được giới hạn tùy vào sự kết nối giữa vùng region .

