# Enable sticky session

Như chúng ta biết HTTP là Stateless (request sau không phụ thuộc vào kết quả request trước), vì vậy để lưu trữ dữ liệu giữa các page với nhau người ta sử dụng session.

Ví dụ phổ biến nhất là token authentication được lưu vào session để xác nhận người dùng đã đăng nhập vào hệ thống. Thông tin authentication của user được lưu trong session, lúc này Session lại được lưu trữ trong một server nào đó và không được đồng bộ giữa các server web với nhau. Đây là nguyên nhân khiến cho người dùng đã đăng nhập bị đăng xuất ra khi request của họ bị điều hướng sang server web khác với server nhận request đăng nhập của họ.

**Để giải quyết vấn đề trên có thể sử dụng cách như:**

* Sử dụng Cluster cho ứng dụng web server, với session sẽ được lưu trữ ở một nơi mà tất cả các server đều truy cập được.
* Lưu trữ thông tin session vào một Database chung hoặc một file system server trên application server.
* Nhược điểm: Việc xây dựng một hệ thống Cluster hay một Database đòi hỏi phải có nhiều kinh nghiệm về system.

Chính lẽ đó VNG CLOUD đã cung cấp tính năng **Sticky Session** giúp chuyển tất cả request của user trong một phiên làm việc vào một server nhất định, đơn giản hóa cho người dùng.

#### 1. Giới thiệu tính năng Enable Sticky Session <a href="#enablestickysession-1.gioithieutinhnangenablestickysession" id="enablestickysession-1.gioithieutinhnangenablestickysession"></a>

Tính năng **Enable Sticky Session** là một phần quan trọng của Load Balancer, cho phép bạn duy trì tính liên tục cho các phiên làm việc của máy khách trên ứng dụng của bạn. Khi tính năng này được kích hoạt, Load Balancer sẽ đảm bảo rằng các yêu cầu từ cùng một máy khách sẽ luôn được chuyển tiếp đến cùng một máy chủ backend trong một khoảng thời gian nhất định.

**Cách hoạt động**

* Khi một máy khách kết nối đến ứng dụng của bạn thông qua Load Balancer, Load Balancer sẽ theo dõi thông tin để xác định máy khách đó (thường dựa trên thông tin trong cookie hoặc IP address).
* Các yêu cầu tiếp theo từ cùng một máy khách sẽ được chuyển tiếp đến cùng một máy chủ backend trong một khoảng thời gian được xác định trước.
* Điều này giúp đảm bảo rằng trạng thái và thông tin của máy khách được duy trì liên tục trong suốt phiên làm việc.

**Lợi ích của việc Enable Sticky Session**

* **Nâng Cao Trải Nghiệm Khách Hàng**: Sticky Session giúp cải thiện trải nghiệm của người dùng cuối bằng cách duy trì trạng thái phiên làm việc liên tục, ngăn việc mất dữ liệu hoặc đăng nhập lại.
* **Hỗ Trợ Ứng Dụng Yêu Cầu Trạng Thái**: Các ứng dụng yêu cầu trạng thái hoặc giỏ hàng mua sắm trực tuyến có lợi từ tính năng này.

#### 2. Hướng dẫn bật/tắt tính năng Sticky Session <a href="#enablestickysession-2.huongdanbat-tattinhnangstickysession" id="enablestickysession-2.huongdanbat-tattinhnangstickysession"></a>

* Truy cập vào trang chủ Load Balancer tại đây: [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
* Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
* Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.
* Một cửa sổ bật lên cho phép chỉnh sửa Pool.
* Tại phần thông tin Pool, tìm đến check box Bật sticky session/Enable sticky session, check/uncheck để bật/tắt tính năng Sticky Session.
* Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất chỉnh sửa.
