# Pool (NLB) trong vCloudStack

Pool (Nhóm máy chủ) là một thành phần quan trọng trong hệ thống Load Balancing, chịu trách nhiệm phân phối lưu lượng truy cập đến các máy chủ backend để cải thiện hiệu suất, tính khả dụng và độ tin cậy của dịch vụ.

Mục tiêu chính của Pool là cân bằng tải (Load Balancing). Pool đảm bảo rằng lưu lượng truy cập được phân phối đều đặn và hiệu quả đến các máy chủ backend. Điều này ngăn máy chủ nào bị quá tải trong khi máy chủ khác không hoạt động.

Pool bao gồm các máy chủ backend, được gọi là "Pool Members." Các Pool Members phục vụ các yêu cầu và trả lời cho người dùng hoặc thiết bị thông qua Load Balancer.

***

## Cách thêm mới Pool <a href="#add-and-updateapool-nlb-1.cachthemmoipool" id="add-and-updateapool-nlb-1.cachthemmoipool"></a>

* Truy cập vào trang chủ Load Balancers.
* Tại Load Balancers, click chọn Load Balancer cần thêm mới Pool.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
* Nhấn chọn nút "Thêm mới Pool", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Pool
* Tại cửa sổ thêm mới, cấu hình các thông tin như:
  * Tên Pool: Lưu ý rằng tên Pool không thể thay đổi sau khi khởi tạo
  * Giao thức: TCP / Proxy / UDP
  * Chọn thuật toán cân bằng tải: Tham khảo thêm các thuật toán cân bằng tải [Pool's algorithm (NLB)](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/pools-algorithm.md)
  * Cài đặt Health Check: Tham khảo hướng dẫn cài đặt Health Check NLB tại [Config health check setting (NLB)](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/config-health-check-setting.md)
  * Thêm Pool Member: Tham khảo hướng dẫn [Attach Pool Member (NLB)](https://docs.vngcloud.vn/pages/viewpage.action?pageId=64553815)
* Nhấn nút "Thêm" tại góc dưới bên phải của cửa sổ thêm mới để hoàn tất việc thêm Pool

***

## &#x20;Cách cập nhật thông tin Pool <a href="#add-and-updateapool-nlb-2.cachcapnhatthongtinpool" id="add-and-updateapool-nlb-2.cachcapnhatthongtinpool"></a>

* Truy cập vào mục Load Balancers.
* Tại Load Balancer, click chọn Load Balancer cần cấu hình.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.
* Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.
* Một cửa sổ bật lên cho phép chỉnh sửa Pool, các thông tin được phép cập nhật
  * Thuật toán cân bằng tải
  * Cấu hình health check nâng cao
* Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất việc cập nhập Pool

***

## Pool Member (NLB)

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

***

## Cấu hình health check (NLB)

Health Check (kiểm tra sức khỏe) là một tính năng quan trọng của Network Load Balancer (NLB) được sử dụng để đảm bảo tính khả dụng và hiệu suất của các máy chủ hoặc các đối tượng trong cụm máy chủ. Health Check cho phép NLB tự động phát hiện máy chủ hoặc dịch vụ nào đang hoạt động cùng với việc tự động loại bỏ các máy chủ hoặc dịch vụ không khả dụng khỏi Load Balancer.

**Cách hoạt động**

* Kiểm tra sức khỏe định kỳ: NLB sẽ thực hiện các kiểm tra sức khỏe định kỳ trên các máy chủ hoặc đối tượng trong pool. Các kiểm tra này có thể là Ping, HTTP GET request, hoặc kiểm tra tùy chỉnh khác.
* Xác định máy chủ/sự cố không khả dụng: Nếu máy chủ hoặc đối tượng không phản hồi kiểm tra sức khỏe hoặc trả về lỗi, NLB sẽ xem xét máy chủ hoặc đối tượng đó là không khả dụng.
* Loại bỏ máy chủ/sự cố không khả dụng: Sau khi xác định máy chủ hoặc đối tượng không khả dụng, NLB sẽ ngừng chuyển hướng lưu lượng đến máy chủ đó trong một thời gian. Điều này giúp ngăn lưu lượng bị gửi đến máy chủ không hoạt động, đảm bảo tính khả dụng của dịch vụ.

**Lợi ích khi cài đặt Health check cho Load Balancer**

* Tăng tính khả dụng: Health Check giúp đảm bảo rằng chỉ những máy chủ hoặc dịch vụ khả dụng mới nhận lưu lượng truy cập. Điều này giúp tăng tính khả dụng của dịch vụ và tránh trường hợp máy chủ không hoạt động nhận lưu lượng.
* Tối ưu hóa hiệu suất: NLB có thể tự động điều chỉnh tải trọng cân bằng bằng cách loại bỏ máy chủ không hoạt động. Điều này giúp tối ưu hóa hiệu suất hệ thống và ngăn máy chủ quá tải.
* Tự động quản lý: Health Check giúp tự động quản lý tính khả dụng của máy chủ hoặc dịch vụ, giảm thiểu sự can thiệp thủ công.
* Bảo mật: NLB có thể loại bỏ máy chủ không hoạt động để đảm bảo rằng lưu lượng không được gửi đến các máy chủ không an toàn hoặc không hoạt động.

**Các loại cấu hình Health check NLB**

* Hướng dẫn cấu hình Health Check TCP khi khởi tạo Pool giao thức TCP/Proxy.
* Hướng dẫn cấu hình Health Check HTTP/HTTPS khi khởi tạo Pool giao thức TCP/Proxy.
* Hướng dẫn cấu hình Health Check PING-UDP khi khởi tạo Pool giao thức UDP.

**1. Hướng dẫn cấu hình Health Check TCP khi khởi tạo Pool giao thức TCP/Proxy**

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

**1/ Chọn giao thức TCP.**

**2/ Cài đặt cấu hình nâng cao:**

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

**2. Hướng dẫn cấu hình Health Check HTTP/HTTPS khi khởi tạo Pool giao thức TCP/Proxy**

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

**1/ Chọn giao thức HTTP.**

**2/ Cài đặt cấu hình nâng cao:**

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

**3. Hướng dẫn cấu hình Health Check PING-UDP khi khởi tạo Pool giao thức UDP**

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

**1/ Chọn giao thức HTTP.**

**2/ Cài đặt cấu hình nâng cao:**

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

***

## Pool's algorithm (NLB)

Load balancing hay "Cân bằng tải" là một trong những tính năng chính của dịch vụ Load Balancer (vLB) của VNG CLOUD. Nó là quá trình nhận yêu cầu của khách hàng ở Listener và phân phối chúng cho một số Member (server) theo các thuật toán đã được thiết lập. Nhờ vào tính năng này dịch vụ của người dùng được gia tăng năng lực xử lý với việc tạo nhiều hoặc một cụm server đứng sau LB.Thuật toán Cân bằng tải sẽ xác định Member (server) nào được chọn khi cân bằng tải. Load Balancer của VNG CLOUD cung cấp ba loại thuật toán Cân bằng tải như sau:

* **Round Robin**
* **Least Connection**
* **Source IP**

#### **1. Round Robin** <a href="#poolsalgorithm-nlb-1.roundrobin" id="poolsalgorithm-nlb-1.roundrobin"></a>

Round Robin là thuật toán lựa chọn các Member (server) theo trình tự. Theo đó, Load Balancer sẽ bắt đầu đi từ Member (server) số 1 trong danh sách của nó ứng với yêu cầu đầu tiên. Tiếp đó, nó sẽ di chuyển dần xuống trong danh sách theo thứ tự và bắt đầu lại ở đầu trang khi đến Member (server) cuối cùng.

#### **2. Least Connection** <a href="#poolsalgorithm-nlb-2.leastconnection" id="poolsalgorithm-nlb-2.leastconnection"></a>

Các request sẽ được chuyển vào server có ít kết nối (active connection) nhất trong hệ thống tại thời điểm hiện tại. Thuật toán này được coi như thuật toán động, vì nó phải đếm số kết nối đang hoạt động của server.**Cách hoạt động**Ví dụ: Chúng ta có 5 client gửi kết nối tới 2 server, thì khi có thêm request từ client thứ 6, request sẽ được điều phối như thế nào?

* Trường hợp 1: Nếu không có client nào ngắt kết nối, client 6 sẽ được gửi sang Server 2 do tỉ lệ connection giữa hai Server đang là 3:2. Xem hình minh họa bên dưới.
* Trường hợp 2: Nếu client 1 & 3 ngắt kết nối trước khi client 6 gửi request, thì khi gửi request, client 6 sẽ được gửi sang Server 1 do tỉ lệ connection giữa hai Server đang là 1:2. Xem hình minh họa bên dưới.

#### **3. Source IP** <a href="#poolsalgorithm-nlb-3.sourceip" id="poolsalgorithm-nlb-3.sourceip"></a>

Thuật toán này kết hợp địa chỉ IP nguồn và đích của client và server để tạo ra hash key duy nhất. Key này được sử dụng để phân bổ client đến một server cụ thể, và nó có thể được tạo lại nếu session bị timeout hay ngắt kết nối do một lý do nào đó. Khi đó request của client vẫn được chuyển đến cùng một server mà nó đã sử dụng trước đó. Đây là một phương pháp để đảm bảo rằng người dùng sẽ kết nối với cùng một server. Ví dụ: để giữ lại các mặt hàng trong giỏ hàng giữa các phiên.
