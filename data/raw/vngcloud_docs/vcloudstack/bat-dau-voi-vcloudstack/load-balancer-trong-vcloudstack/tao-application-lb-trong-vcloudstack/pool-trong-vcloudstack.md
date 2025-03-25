# Pool trong vCloudstack

Pool (Nhóm máy chủ) là một thành phần quan trọng trong hệ thống Load Balancing, chịu trách nhiệm phân phối lưu lượng truy cập đến các máy chủ backend để cải thiện hiệu suất, tính khả dụng và độ tin cậy của dịch vụ.

Mục tiêu chính của Pool là cân bằng tải (Load Balancing). Pool đảm bảo rằng lưu lượng truy cập được phân phối đều đặn và hiệu quả đến các máy chủ backend. Điều này ngăn máy chủ nào bị quá tải trong khi máy chủ khác không hoạt động.

Pool bao gồm các máy chủ backend, được gọi là "Pool Members." Các Pool Members phục vụ các yêu cầu và trả lời cho người dùng hoặc thiết bị thông qua Load Balancer.

***

## Cách thêm mới Pool <a href="#add-and-updateapool-1.cachthemmoipool" id="add-and-updateapool-1.cachthemmoipool"></a>

* Truy cập vào mụcLoad Balancers;
* Tại Load Balancer, click chọn Load Balancer cần thêm mới Pool.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
* Nhấn chọn nút "Thêm mới Pool", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Pool
* Tại cửa sổ thêm mới, cấu hình các thông tin như:
  * Tên Pool: Lưu ý rằng tên Pool không thể thay đổi sau khi khởi tạo
  * Giao thức HTTP
  * Chọn thuật toán cân bằng tải: Tham khảo thêm các thuật toán cân bằng tải [Pool's algorithm](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/pools-algorithm.md)
  * Enable/Bật Stick Session: Tham khảo thêm tại [Enable sticky session](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/enable-sticky-session.md)
  * Enable/Bật TLS Encryption: Tham khảo thêm tại [Enable TLS encryption](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/enable-tls-encryption.md)
  * Cài đặt Health Check: Tham khảo hướng dẫn cài đặt Health Check giao thức TCP/HTTP tại [Config health check setting](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/config-health-check-setting.md)
  * Thêm Pool Member: Tham khảo hướng dẫn [Attach pool members](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/pool-members/attach-pool-members.md)
* Nhấn nút "Thêm" tại góc dưới bên phải của cửa sổ thêm mới để hoàn tất việc thêm Pool

***

## Cách cập nhật thông tin Pool <a href="#add-and-updateapool-2.cachcapnhatthongtinpool" id="add-and-updateapool-2.cachcapnhatthongtinpool"></a>

* Truy cập vào trang chủ Load Balancer;
* Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
* Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.
* Một cửa sổ bật lên cho phép chỉnh sửa Pool, các thông tin được phép cập nhật
  * Thuật toán cân bằng tải
  * Cấu hình health check nâng cao
* Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất việc cập nhập Pool

***

## Pool Members

Pool Member là thành viên trong một nhóm máy chủ (Pool) trên Load Balancer, và chúng chịu trách nhiệm phục vụ các yêu cầu từ người dùng hoặc các thiết bị khác thông qua Load Balancer. Dưới đây là giải thích về cơ chế hoạt động của Pool Member và các thuộc tính quan trọng:

**Weight**

* **Giải thích**: Trọng số quy định mức độ ưu tiên của mỗi Pool Member trong việc xử lý các yêu cầu. Các Member có trọng số cao sẽ nhận được nhiều yêu cầu hơn so với các Member có trọng số thấp.
* **Ví dụ**: Nếu bạn có hai Member với trọng số 3 và 1, Member có trọng số 3 sẽ nhận được khoảng 75% yêu cầu, trong khi Member có trọng số 1 chỉ nhận được khoảng 25%.

**Port**

* **Giải thích**: Port mà Member sẽ lắng nghe để xử lý các yêu cầu đến. Port này thường liên quan đến dịch vụ cụ thể mà Member cung cấp.
* **Ví dụ**: Nếu bạn có một ứng dụng web chạy trên Member, bạn có thể sử dụng cổng 80 cho HTTP và cổng 443 cho HTTPS.

**Monitor Port**

* **Giải thích**: Đây là Port mà Load Balancer sử dụng để kiểm tra sức khỏe của Member. Load Balancer sẽ gửi các yêu cầu kiểm tra đến Port này để đảm bảo rằng Member đang hoạt động đúng cách. Nếu không chỉ định cụ thể Monitor Port, thì mặc định Monitor Port = Port dùng để nhận request đến.
* **Ví dụ**: Nếu bạn muốn kiểm tra sức khỏe của một máy chủ web, bạn có thể sử dụng cổng 80 hoặc 443 để kiểm tra tính khả dụng.

**Backup Role**

* **Giải thích**: Thuộc tính này xác định vai trò của Member trong một Pool. Có hai vai trò chính: Primary (Chính) và Backup (Sao lưu). Member Chính nhận các yêu cầu chính thức từ người dùng, trong khi Member Sao lưu chỉ nhận yêu cầu khi Member Chính không khả dụng.
* **Ví dụ**: Nếu bạn có hai Member trong một Pool, Member A có vai trò Chính và Member B có vai trò Sao lưu, yêu cầu sẽ được gửi đến Member A trước. Nếu Member A không khả dụng, Load Balancer sẽ chuyển yêu cầu đến Member B.

Nhìn chung, cơ chế này cho phép bạn tùy chỉnh cách Load Balancer phân phối lưu lượng truy cập giữa các Member trong một Pool. Bằng cách sử dụng trọng số, bạn có thể cân nhắc sự phân phối của lưu lượng. Đồng thời, vai trò Sao lưu giúp đảm bảo tính khả dụng và độ tin cậy của hệ thống khi Member Chính gặp sự cố.

## Attach pool members

Sử dụng tài liệu này như là một hướng dẫn về cách thêm Member vào một Pool trên Load Balancer. Về cơ bản, giao diện quản trị hỗ trợ việc thêm Member vào Pool theo hai cách:

* **Qua Instance** (Member là các máy ảo hoặc máy chủ cụ thể)
* **Qua địa chỉ IP** (Member là các địa chỉ IP Public hoặc IP thuộc subnet của Load Balancer)

**1. Đính kèm/Cập nhật Member là các máy chủ khả dụng**

* Truy cập vào mục Load Balancers​
* Tại Load Balancers, click chọn Load Balancer cần cấu hình. Tại phần thông tin chi tiết Load Balancer, chọn tab Pool. Tại phần danh sách Pool, nhấn chọn Pool cần đính kèm/chỉnh sửa Member.
* Tại phần thông tin chi tiết Pool bên trái, kéo xuống mục Thông tin Member, nhấn nút "Chỉnh sửa Pool members / Edit Pool member".
* Tại cửa sổ giao diện "Chỉnh sửa Pool Member", phần "Máy chủ khả dụng / Available instances" sẽ hiện lên danh sách máy chủ backend khả dụng thuộc subnet Load Balancer.
* Chọn máy chủ khả dụng từ danh sách.
* Điền các thông tin về thông số Weight, Port, Monitor Port và Backup role.
* Nhấn chọn nút "Attach / Gắn" để thêm máy chủ backend làm Pool Member.
* Xem lại danh sách Pool Member tại mục "Máy chủ & Instance đính kèm / Attach server & instances".
* Nhấn nút "Save / Lưu" để hoàn tất chỉnh sửa Pool Member.

**2. Đính kèm/Cập nhật Member là các địa chỉ IP**

Ngoài việc đính kèm các Pool member thông qua các máy chủ backend, người dùng còn có thể đính kèm các địa chỉ IP như là các Pool Member, tham khảo hướng dẫn dưới đây để thực hiện việc đính kèm.

* Truy cập vào mục Load Balancers;​
* Tại Load Balancers, click chọn Load Balancer cần cấu hình. Tại phần thông tin chi tiết Load Balancer, chọn tab Pool. Tại phần danh sách Pool, nhấn chọn Pool cần đính kèm/chỉnh sửa Member.
* Tại phần thông tin chi tiết Pool bên trái, kéo xuống mục Thông tin Member, nhấn nút "Chỉnh sửa Pool members / Edit Pool member".
*   Tại cửa sổ giao diện "Chỉnh sửa Pool Member", tại phần "Custom Instances / Instances tùy chỉnh" thực hiện đính kèm địa chỉ IP vào Pool theo hướng dẫn sau:

    1/ Nhập địa chỉ IP: Các địa chỉ IP phải là IP Public hoặc thuộc Load Balancer subnet

    2/ Nhấn nút Add để thêm các địa chỉ IP vào danh sách Custom Instance

    3/ Chọn IP Address cần đính kèm từ danh sách Custom Instance

    4/ Điền các thông tin về thông số Weight, Port, Monitor Port và Backup role.

    5/ Nhấn nút "Attach / Gắn"

    6/ Xem lại danh sách Pool Member tại mục "Máy chủ & Instance đính kèm / Attach server & instances".

    7/ Nhấn nút "Save / Lưu" để hoàn tất chỉnh sửa Pool Member.

***

## Config health check setting

Tính năng Health Check Setting là một yếu tố quan trọng trong việc đảm bảo tính ổn định và khả dụng của ứng dụng trên Application Load Balancer. Khi tính năng này được kích hoạt, Load Balancer sẽ thực hiện kiểm tra sức khỏe của máy chủ backend và tự động điều chỉnh luồng lưu lượng truy cập để đảm bảo rằng chỉ có các máy chủ khỏe mạnh được phục vụ yêu cầu từ máy khách. Đối với Application Load Balancer

**Cách hoạt động**

* Application Load Balancer sẽ định kỳ gửi các yêu cầu kiểm tra sức khỏe đến các máy chủ backend, thông qua các tùy chọn được cấu hình.
* Nếu máy chủ backend trả lời với mã trạng thái hoặc nội dung không đúng, Load Balancer sẽ coi máy chủ đó là không khỏe và ngừng gửi yêu cầu đến nó.
* Các yêu cầu từ máy khách sẽ chỉ được chuyển tiếp đến các máy chủ được xem là khỏe mạnh.
* Các cài đặt Health Check phổ biến đối với Application Load Balancer: Heath Check TCP và Health Check HTTP

**Lợi ích khi cài đặt Health check cho Load Balancer**

* Tăng Khả Dụng: Health Check Setting giúp cải thiện tính khả dụng của ứng dụng bằng cách loại bỏ máy chủ không hoạt động khỏi dịch vụ.
* Tối Ưu Hóa Hiệu Năng: Nó giúp Load Balancer chuyển tiếp yêu cầu đến các máy chủ hoạt động tốt, tối ưu hóa hiệu suất hệ thống.
* Giảm Thiểu Các Lỗi Trong Ứng Dụng: Sự theo dõi và kiểm tra sức khỏe định kỳ giúp giảm thiểu sự cố và lỗi trong ứng dụng.

**Các loại cấu hình Health check ALB**

* Hướng dẫn cấu hình Health Check TCP khi khởi tạo Pool.
* Hướng dẫn cấu hình Health Check HTTP khi khởi tạo Pool.

**1. Hướng dẫn cấu hình Health Check TCP khi khởi tạo Pool**

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

1/ Chọn giao thức TCP.

2/ Cài đặt cấu hình nâng cao:

* **Healthy Threshold**
  * Giải thích: Health Threshold là số lần kiểm tra sức khỏe liên tiếp phải thành công để một máy chủ backend được xem là khỏe mạnh.
  * Ví dụ: Nếu bạn đặt Health Threshold là 3, máy chủ backend phải trả lời thành công cho 3 lần kiểm tra sức khỏe liên tiếp trước khi được coi là khỏe mạnh.
* **Unhealthy threshold**
  * Giải thích: Unhealthy Threshold là số lần kiểm tra sức khỏe liên tiếp thất bại trước khi một máy chủ backend được đánh dấu là không khỏe mạnh.
  * Ví dụ: Nếu bạn đặt Unhealthy Threshold là 2, máy chủ backend sẽ bị đánh dấu là không khỏe mạnh nếu có 2 yêu cầu kiểm tra sức khỏe liên tiếp thất bại.
* **Timeout**
  * Giải thích: Timeout là thời gian tối đa cho một yêu cầu kiểm tra sức khỏe được gửi đến máy chủ backend trước khi được coi là thất bại. Nếu máy chủ không trả lời trong thời gian này, yêu cầu kiểm tra sẽ được xem là thất bại.
  * Ví dụ: Nếu bạn đặt Timeout là 5 giây, và máy chủ backend không trả lời trong vòng 5 giây, yêu cầu kiểm tra sẽ bị đánh dấu là thất bại.
* **Interval**
  * Giải thích: Interval là khoảng thời gian giữa các lần kiểm tra sức khỏe được gửi đến máy chủ backend. Nó xác định tần suất kiểm tra sức khỏe của máy chủ.
  * Ví dụ: Nếu bạn đặt Interval là 30 giây, Load Balancer sẽ gửi yêu cầu kiểm tra sức khỏe đến máy chủ backend mỗi 30 giây.

**2. Hướng dẫn cấu hình Health Check HTTP khi khởi tạo Pool**

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

1/ Chọn giao thức HTTP.

2/ Cài đặt cấu hình nâng cao:

* **Path / Đường dẫn**
  * Giải thích: Path xác định URL đường dẫn cụ thể trên máy chủ backend mà Load Balancer sẽ thực hiện kiểm tra sức khỏe. Thông qua thuộc tính này, bạn có thể chỉ định một tài nguyên cụ thể trên máy chủ backend mà bạn muốn kiểm tra.
  * Ví dụ: Nếu bạn đặt Path là "/health", Load Balancer sẽ gửi yêu cầu kiểm tra sức khỏe đến URL "[http://backend-server/health](http://backend-server/health)".
* **HTTP Method / Phương thức HTTP**
  * Giải thích: HTTP Method xác định phương thức HTTP mà Load Balancer sử dụng khi gửi yêu cầu kiểm tra sức khỏe đến máy chủ backend. Điều này cho phép bạn xác định liệu kiểm tra sức khỏe nên sử dụng GET, POST hay PUT.
  * Ví dụ: Nếu bạn đặt HTTP Method là GET, Load Balancer sẽ gửi yêu cầu kiểm tra sức khỏe bằng phương thức GET.
* **Success Code**
  * Giải thích: Success Code là mã trạng thái HTTP mà máy chủ backend phải trả về trong phản hồi để được coi là khỏe mạnh. Nếu phản hồi từ máy chủ backend có mã trạng thái khớp với Success Code, thì yêu cầu kiểm tra sức khỏe được xem là thành công.
  * Ví dụ: Nếu bạn đặt Success Code là 200, máy chủ backend phải trả về mã trạng thái 200 OK để kiểm tra sức khỏe được coi là thành công.
* **Healthy Threshold**
  * Giải thích: Health Threshold là số lần kiểm tra sức khỏe liên tiếp phải thành công để một máy chủ backend được xem là khỏe mạnh.
  * Ví dụ: Nếu bạn đặt Health Threshold là 3, máy chủ backend phải trả lời thành công cho 3 lần kiểm tra sức khỏe liên tiếp trước khi được coi là khỏe mạnh.
* **Unhealthy threshold**
  * Giải thích: Unhealthy Threshold là số lần kiểm tra sức khỏe liên tiếp thất bại trước khi một máy chủ backend được đánh dấu là không khỏe mạnh.
  * Ví dụ: Nếu bạn đặt Unhealthy Threshold là 2, máy chủ backend sẽ bị đánh dấu là không khỏe mạnh nếu có 2 yêu cầu kiểm tra sức khỏe liên tiếp thất bại.
* **Timeout**
  * Giải thích: Timeout là thời gian tối đa cho một yêu cầu kiểm tra sức khỏe được gửi đến máy chủ backend trước khi được coi là thất bại. Nếu máy chủ không trả lời trong thời gian này, yêu cầu kiểm tra sẽ được xem là thất bại.
  * Ví dụ: Nếu bạn đặt Timeout là 5 giây, và máy chủ backend không trả lời trong vòng 5 giây, yêu cầu kiểm tra sẽ bị đánh dấu là thất bại.
* **Interval**
  * Giải thích: Interval là khoảng thời gian giữa các lần kiểm tra sức khỏe được gửi đến máy chủ backend. Nó xác định tần suất kiểm tra sức khỏe của máy chủ.
  * Ví dụ: Nếu bạn đặt Interval là 30 giây, Load Balancer sẽ gửi yêu cầu kiểm tra sức khỏe đến máy chủ backend mỗi 30 giây.
* **Tên Domain**
  * Giải thích: Tên domain là tên miền hoặc địa chỉ IP mà bạn sử dụng để truy cập máy chủ backend khi thực hiện kiểm tra sức khỏe.
  * Ví dụ: Nếu bạn đặt Tên Domain là "[backend-server.example.com](http://backend-server.example.com/)", Load Balancer sẽ sử dụng tên miền này để gửi yêu cầu kiểm tra sức khỏe đến máy chủ backend.

***

## Enable sticky session

Như chúng ta biết HTTP là Stateless (request sau không phụ thuộc vào kết quả request trước), vì vậy để lưu trữ dữ liệu giữa các page với nhau người ta sử dụng session.Ví dụ phổ biến nhất là token authentication được lưu vào session để xác nhận người dùng đã đăng nhập vào hệ thống. Thông tin authentication của user được lưu trong session, lúc này Session lại được lưu trữ trong một server nào đó và không được đồng bộ giữa các server web với nhau. Đây là nguyên nhân khiến cho người dùng đã đăng nhập bị đăng xuất ra khi request của họ bị điều hướng sang server web khác với server nhận request đăng nhập của họ.

**Để giải quyết vấn đề trên có thể sử dụng cách như:**

* Sử dụng Cluster cho ứng dụng web server, với session sẽ được lưu trữ ở một nơi mà tất cả các server đều truy cập được.
* Lưu trữ thông tin session vào một Database chung hoặc một file system server trên application server.
* Nhược điểm: Việc xây dựng một hệ thống Cluster hay một Database đòi hỏi phải có nhiều kinh nghiệm về system.

Chính lẽ đó vCloudStack đã cung cấp tính năng **Sticky Session** giúp chuyển tất cả request của user trong một phiên làm việc vào một server nhất định, đơn giản hóa cho người dùng.

**1. Giới thiệu tính năng Enable Sticky Session**

Tính năng **Enable Sticky Session** là một phần quan trọng của Load Balancer, cho phép bạn duy trì tính liên tục cho các phiên làm việc của máy khách trên ứng dụng của bạn. Khi tính năng này được kích hoạt, Load Balancer sẽ đảm bảo rằng các yêu cầu từ cùng một máy khách sẽ luôn được chuyển tiếp đến cùng một máy chủ backend trong một khoảng thời gian nhất định.**Cách hoạt động**

* Khi một máy khách kết nối đến ứng dụng của bạn thông qua Load Balancer, Load Balancer sẽ theo dõi thông tin để xác định máy khách đó (thường dựa trên thông tin trong cookie hoặc IP address).
* Các yêu cầu tiếp theo từ cùng một máy khách sẽ được chuyển tiếp đến cùng một máy chủ backend trong một khoảng thời gian được xác định trước.
* Điều này giúp đảm bảo rằng trạng thái và thông tin của máy khách được duy trì liên tục trong suốt phiên làm việc.

**Lợi ích của việc Enable Sticky Session**

* **Nâng Cao Trải Nghiệm Khách Hàng**: Sticky Session giúp cải thiện trải nghiệm của người dùng cuối bằng cách duy trì trạng thái phiên làm việc liên tục, ngăn việc mất dữ liệu hoặc đăng nhập lại.
* **Hỗ Trợ Ứng Dụng Yêu Cầu Trạng Thái**: Các ứng dụng yêu cầu trạng thái hoặc giỏ hàng mua sắm trực tuyến có lợi từ tính năng này.

**2. Hướng dẫn bật/tắt tính năng Sticky Session**

* Truy cập vào mục Load Balancer.​
* Tại Load Balancer, click chọn Load Balancer cần cấu hình.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
* Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.
* Một cửa sổ bật lên cho phép chỉnh sửa Pool.
* Tại phần thông tin Pool, tìm đến check box Bật sticky session/Enable sticky session, check/uncheck để bật/tắt tính năng Sticky Session.
* Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất chỉnh sửa.

***

## Enable TLS encryption

Tính năng **Enable TLS Encryption** là một yếu tố quan trọng của bảo mật mạng, cho phép bạn bảo vệ dữ liệu truyền tải từ Load Balancer đến máy chủ backend. Khi tính năng này được kích hoạt, dữ liệu truyền tải sẽ được mã hóa và bảo vệ trong suốt quá trình truyền tải.**Cách hoạt động**

* Khi một máy khách kết nối đến Load Balancer và yêu cầu truy cập trang web hoặc ứng dụng của bạn, dữ liệu truyền tải giữa máy khách và Load Balancer sẽ được mã hóa bằng một giao thức bảo mật TLS (Transport Layer Security), trước khi nó được chuyển tiếp đến máy chủ backend.
* Máy chủ backend cũng cần hỗ trợ TLS để có thể giải mã dữ liệu được gửi từ Load Balancer.
* Quá trình này đảm bảo rằng dữ liệu truyền tải không thể bị đánh cắp hoặc hiểu được trong trường hợp nó bị bắt gặp trên đường truyền.

**Lợi ích khi bật tính năng TLS Encryption**

* **Bảo Mật Cao**: TLS Encryption đảm bảo mức độ bảo mật cao cho dữ liệu của bạn, giúp ngăn chặn các cuộc tấn công trung gian và đánh cắp dữ liệu.
* **Tích Hợp An Toàn**: Nó cho phép bạn cung cấp một trải nghiệm an toàn cho khách hàng của mình bằng cách bảo vệ thông tin cá nhân và tài khoản của họ khi dữ liệu được truyền đến Load Balancer.
* **Độ Tin Cậy**: TLS Encryption cung cấp độ tin cậy trong việc truyền tải dữ liệu trên mạng, giúp đảm bảo rằng dữ liệu không bị thất lạc hoặc bị sửa đổi trong quá trình truyền từ Load Balancer đến máy chủ backend.
* **Cho phép sử dụng Self-signed Certificate**: Tính năng TLS Encryption hỗ trợ cả HTTP và HTTPS. Đối với HTTPS, khi bật tính năng này, Load Balancer sẽ không xác minh tính đúng đắn của SSL/TLS Certificate. Việc này giúp bạn có thể sử dụng cả các self-signed certificate trên máy chủ thành viên.

**Hướng dẫn bật tính năng TLS Encryption**

* Truy cập vào mục Load Balancer.​
* Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
* Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.
* Một cửa sổ bật lên cho phép chỉnh sửa Pool.
* Tại phần thông tin Pool, tìm đến check box Bật mã hóa TLS/Enable TLS Encryption, check/uncheck để bật/tắt tính năng mã hóa TLS.
* Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất chỉnh sửa.

***

## Pool's algorithm

Load balancing hay "Cân bằng tải" là một trong những tính năng chính của dịch vụ Load Balancer (vLB) của VNG CLOUD. Nó là quá trình nhận yêu cầu của khách hàng ở Listener và phân phối chúng cho một số Member (server) theo các thuật toán đã được thiết lập. Nhờ vào tính năng này dịch vụ của người dùng được gia tăng năng lực xử lý với việc tạo nhiều hoặc một cụm server đứng sau LB.Thuật toán Cân bằng tải sẽ xác định Member (server) nào được chọn khi cân bằng tải. Load Balancer của VNG CLOUD cung cấp ba loại thuật toán Cân bằng tải như sau:

* **Round Robin**
* **Least Connection**
* **Source IP**

**1. Round Robin**

Round Robin là thuật toán lựa chọn các Member (server) theo trình tự. Theo đó, Load Balancer sẽ bắt đầu đi từ Member (server) số 1 trong danh sách của nó ứng với yêu cầu đầu tiên. Tiếp đó, nó sẽ di chuyển dần xuống trong danh sách theo thứ tự và bắt đầu lại ở đầu trang khi đến Member (server) cuối cùng.

**2. Least Connection**

Các request sẽ được chuyển vào server có ít kết nối (active connection) nhất trong hệ thống tại thời điểm hiện tại. Thuật toán này được coi như thuật toán động, vì nó phải đếm số kết nối đang hoạt động của server.**Cách hoạt động**Ví dụ: Chúng ta có 5 client gửi kết nối tới 2 server, thì khi có thêm request từ client thứ 6, request sẽ được điều phối như thế nào?

* Trường hợp 1: Nếu không có client nào ngắt kết nối, client 6 sẽ được gửi sang Server 2 do tỉ lệ connection giữa hai Server đang là 3:2. Xem hình minh họa bên dưới.
* Trường hợp 2: Nếu client 1 & 3 ngắt kết nối trước khi client 6 gửi request, thì khi gửi request, client 6 sẽ được gửi sang Server 1 do tỉ lệ connection giữa hai Server đang là 1:2. Xem hình minh họa bên dưới

**3. Source IP**

Thuật toán này kết hợp địa chỉ IP nguồn và đích của client và server để tạo ra hash key duy nhất. Key này được sử dụng để phân bổ client đến một server cụ thể, và nó có thể được tạo lại nếu session bị timeout hay ngắt kết nối do một lý do nào đó. Khi đó request của client vẫn được chuyển đến cùng một server mà nó đã sử dụng trước đó. Đây là một phương pháp để đảm bảo rằng người dùng sẽ kết nối với cùng một server. Ví dụ: để giữ lại các mặt hàng trong giỏ hàng giữa các phiên.
