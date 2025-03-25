# Kiến Trúc Mạng

Kiến trúc giải pháp CDN của VNG Cloud được xây dựng theo kiến trúc CDN 3.0 của mô hình CDN thế giới, multi-tier để có khả năng mở rộng dễ dàng nhất và đáp ứng các mô hình kinh doanh phức tạp nhất của các nhà cung cấp nội dung và các nhà khai thác kinh doanh dịch vụ giá trị gia tăng trên nền internet, ví dụ bán sỉ CDN (whole sale CDN) hay các nhà khai thác mạng tận dụng mạng CDN để tối ưu hóa traffic, kiểm soát an ninh an toàn mạng ngoài các tính năng chính của CDN được thiết kế là truyền tải nội dung chất lượng cao trên nền internet.\
Kiến trúc CDN 3.0 được áp dụng với các ứng dụng module hóa tiêu chuẩn và đặc biệt tập trung vào xu hướng phân tích big-data và hệ thống portal quản trị khách hàng thông minh, cho phép sự tương tác ở mức độ cao nhất cho khách hàng trong việc quản trị và giám sát chất lượng của dịch vụ CDN của mình\
Mô hình CDN được chia làm 3 phân hệ từ Add-On Site, Central Site, Edge Site và tạo kết nối đến các nguồn dữ liệu bên ngoài của khách hàng cũng như truyền dữ liệu đến điểm truy cập cuối của thuê bao (clients):

* **Content Source:** là nguồn dữ liệu gốc của khách hàng sử dụng dịch vụ CDN. Các nguồn này có thể là:\
  &#x20;         o      Tín hiệu live trực tiếp từ vệ tinh đã được chuyển đổi thành tín hiệu có thể truyền tải trên internet.\
  &#x20;         o      Storage chứa file lưu trữ các nội dung VoD.\
  &#x20;         o      Server chứa nội dung trang web gốc của khách hàng.\
  &#x20; &#x20;
* **Add-on Site**: là các dịch vụ ngoài hệ thống chức năng chính của CDN (phân phối nội dung) bao gồm các khối chức năng (số lượng add-on services sẽ được phát triển thêm trong tương lai) như:\
  &#x20;         o      Content Store nơi lưu trữ Origin của nội dung dữ liệu của khách hàng.\
  &#x20;         o      Transcoding: Chuyển đổi định dạng, chất lượng nội dung cho cả VoD và Live.\
  &#x20;         o      Các module hỗ trợ tích hợp với các 3rd services trên internet hiện nay như Google, AWS.\
  &#x20;         o      Các dịch vụ khác phát sinh theo nhu cầu khách hàng về sau đều sẽ được đưa vào nhóm Add-on site.\
  &#x20; &#x20;
* **Central Site**: là khối chịu trách nhiệm phân tải và kiểm soát toàn bộ hoạt động và chuẩn hóa dữ liệu trước khi phục vụ khách hàng đầu cuối. Nhờ vào thiết kế modular nên dễ dàng hỗ trợ mô hình mở rộng ở mọi cấp độ theo yêu cầu của khách hàng.
* **Edge Site**: là lớp truyền tài nội dung trực tiếp đến khách hàng cuối với nhiệm vụ hoạt động ở hiệu suất cực cao và độ sẵn sàng cao nhất. Đặc biệt với tính năng Edge Cache Sharing (ECS), các server Edge trong cùng một PoP sẽ chia sẽ dữ liệu caching lẫn nhau nhằm tối ưu tối đa dung lượng cache trên toàn hệ thống.
* **Khối khách hàng cuối kết nối vào hệ thống** hỗ trợ tất cả các mô hình, từ connected TV, đến Set-top-box và các ứng dụng OTT kết cuối như flash hay smartphone, tablet, PC, v.v.\
  Kiến trúc được áp dụng với các ứng dụng module hóa tiêu chuẩn và đặc biệt tập trung vào xu hướng phân tích fast-data cho phép dữ liệu được cung cấp trên hệ thống gần như tức thời cùng với hệ thống portal quản trị khách hàng thông minh, cho phép sự tương tác ở mức độ cao nhất cho khách hàng trong việc quản trị và giám sát chất lượng của dịch vụ CDN của mình.

Hiện tại vCDN đã cung cấp độ phủ tại 2 điểm chính là Thành Phố Hồ Chí Minh và Hà Nội với số lượng POP là 10, tọa lại tại 4 ISP lớn nhất của Việt Nam là Viettel, VNPT, FPT, Mobifone. Cụ thể như sau:

* **TP. Hồ Chí Minh:**\
  &#x20;         o      FPT Tân Thuận.\
  &#x20;         o      VNPT Trạm 2 137 Pastuer. Điểm mạng lõi cho kết nối toàn bộ miền Nam của VNPT.\
  &#x20;         o      Viettel IDC Hoàng Hoa Thám.\
  &#x20;         o      Vinadata DC Công Viên Phần Mềm Quang Trung.
* **Hà Nội:**\
  &#x20;         o      FPT DC Phạm Hùng.\
  &#x20;         o      VNPT Nam Thăng Long.\
  &#x20;         o      Viettel IDC Hòa Lạc.

Với tổng băng thông hiện tại lên đến gần 2Tbps và kế hoạch mở rộng thêm đến hơn 5Tbps trong năm 2025.
