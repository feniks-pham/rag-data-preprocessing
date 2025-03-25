# Kết nối nhiều đám mây (Multicloud-connection)

VNG Cloud sử dụng các kênh thuê riêng do đối tác cung cấp để thiết lập kết nối giữa VNG Cloud và một nhà cung cấp dịch vụ đám mây khác. Điều này cho phép quản lý dữ liệu tập trung trên nhiều nhà cung cấp dịch vụ đám mây và triển khai kết nối giữa các đám mây.

***

### **Tổng quan** <a href="#ketnoinhieudammay-multicloud-connection-tongquan" id="ketnoinhieudammay-multicloud-connection-tongquan"></a>

Dịch vụ kinh doanh điện toán đám mây tại Việt Nam và trên thế giới đang ngày càng phát triển theo hướng tích cực và mạnh mẽ trong nhiều năm qua, vì thế ngoài việc sử dụng dịch vụ đám mây tại Việt Nam, các tổ chức doanh nghiệp còn sử dụng các dịch vụ điện toán đám mây như Amazon Web Services (AWS). Trong một số trường hợp, điều này đòi hỏi họ phải thực hiện việc đồng bộ hóa, truy cập, và di chuyển một lượng lớn dữ liệu giữa môi trường Đám mây trong nước và AWS."

Tính năng kết nối nhiều đám mây do VNG Cloud cung cấp giúp bạn thiết lập đường dây thuê riêng giữa VNG Cloud và một nhà cung cấp dịch vụ đám mây khác. Bằng cách này, VNG Cloud có thể được kết nối với một nhà cung cấp dịch vụ đám mây khác. Điều này đáp ứng yêu cầu truy cập kinh doanh giữa nhiều nhà cung cấp dịch vụ đám mây, giúp nâng cao khả năng kết nối kinh doanh và đảm bảo kết nối giữa các đám mây.

VNG Cloud cung cấp quy trình từ đầu đến cuối để định cấu hình tài nguyên. Bạn chỉ cần đặt hàng tại trang web chính thức của VNG Cloud để kích hoạt khả năng kết nối nhiều đám mây. Bằng cách này, quyền truy cập giữa nhiều nhà cung cấp dịch vụ đám mây được triển khai.

Việc sử dụng các đường truyền thuê riêng giúp loại bỏ nhu cầu sử dụng Internet để truyền tải. Điều này đảm bảo an ninh truyền tải cho dữ liệu doanh nghiệp.

***

### **Các thành phần** <a href="#ketnoinhieudammay-multicloud-connection-cacthanhphan" id="ketnoinhieudammay-multicloud-connection-cacthanhphan"></a>

AWS được sử dụng trong ví dụ được kết nối với Đám mây VNG bằng cách sử dụng tính năng kết nối nhiều đám mây. Kiến trúc của giải pháp kết nối đa đám mây bao gồm các thành phần sau:

* Phiên bản kết nối nhiều đám mây: thực thể logic được sử dụng để kết nối Đám mây VNG Cloud với AWS.
* Bộ định tuyến viền ảo (VBR): bộ định tuyến viền kết nối Cloud Enterprise Network do VNG Cloud phát triển. VBR đóng vai trò là cầu nối để truyền dữ liệu từ trung tâm dữ liệu VNG Cloud sang AWS.

Interconnect: cho phép bạn thiết lập kết nối mạng để kết nối Amazon Virtual Private Cloud (VPC) với VNG Cloud. Interconnect đóng vai trò là cầu nối để truyền dữ liệu từ trung tâm dữ liệu AWS sang Đám mây của VNG.

***

### **Các đám Mây được hỗ trợ kết nối** <a href="#ketnoinhieudammay-multicloud-connection-cacdammayduochotroketnoi" id="ketnoinhieudammay-multicloud-connection-cacdammayduochotroketnoi"></a>

Hiện chúng tôi đang hỗ trợ kết nối tới đám mây của AWS

***

### **Những lợi ích** <a href="#ketnoinhieudammay-multicloud-connection-nhungloiich" id="ketnoinhieudammay-multicloud-connection-nhungloiich"></a>

#### Tương tác giữa nhiều đám mây <a href="#ketnoinhieudammay-multicloud-connection-tuongtacgiuanhieudammay" id="ketnoinhieudammay-multicloud-connection-tuongtacgiuanhieudammay"></a>

Giải pháp kết nối đa đám mây do VNG Cloud cung cấp cho phép các nhà cung cấp dịch vụ đám mây khác truyền dữ liệu sang Alibaba Cloud. Bằng cách này, tài nguyên có thể được truy cập giữa các nhà cung cấp dịch vụ đám mây khác nhau và trên các khu vực khác nhau.

#### Tính ổn định và hiệu quả cao <a href="#ketnoinhieudammay-multicloud-connection-tinhondinhvahieuquacao" id="ketnoinhieudammay-multicloud-connection-tinhondinhvahieuquacao"></a>

Việc sử dụng đường truyền thuê riêng để kết nối Đám mây VNG Cloud với nhà cung cấp dịch vụ đám mây khác giúp loại bỏ nhu cầu sử dụng Internet để truyền tải. Điều này mang lại độ trễ ngắn và băng thông cao như truyền thông qua mạng nội bộ.

#### Bảo mật và độ tin cậy <a href="#ketnoinhieudammay-multicloud-connection-baomatvadotincay" id="ketnoinhieudammay-multicloud-connection-baomatvadotincay"></a>

Đường dây thuê riêng cung cấp các kết nối đầu cuối. Điều này đảm bảo tính bảo mật và độ tin cậy cho việc truyền dữ liệu qua mạng.
