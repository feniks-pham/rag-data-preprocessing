# Cấu hình health check (NLB)

Health Check (kiểm tra sức khỏe) là một tính năng quan trọng của Network Load Balancer (NLB) được sử dụng để đảm bảo tính khả dụng và hiệu suất của các máy chủ hoặc các đối tượng trong cụm máy chủ. Health Check cho phép NLB tự động phát hiện máy chủ hoặc dịch vụ nào đang hoạt động cùng với việc tự động loại bỏ các máy chủ hoặc dịch vụ không khả dụng khỏi Load Balancer.

**Cách hoạt động**

* **Kiểm tra sức khỏe định kỳ**: NLB sẽ thực hiện các kiểm tra sức khỏe định kỳ trên các máy chủ hoặc đối tượng trong pool. Các kiểm tra này có thể là Ping, HTTP GET request, hoặc kiểm tra tùy chỉnh khác.
* **Xác định máy chủ/sự cố không khả dụng**: Nếu máy chủ hoặc đối tượng không phản hồi kiểm tra sức khỏe hoặc trả về lỗi, NLB sẽ xem xét máy chủ hoặc đối tượng đó là không khả dụng.
* **Loại bỏ máy chủ/sự cố không khả dụng**: Sau khi xác định máy chủ hoặc đối tượng không khả dụng, NLB sẽ ngừng chuyển hướng lưu lượng đến máy chủ đó trong một thời gian. Điều này giúp ngăn lưu lượng bị gửi đến máy chủ không hoạt động, đảm bảo tính khả dụng của dịch vụ.

**Lợi ích khi cài đặt Health check cho Load Balancer**

* **Tăng tính khả dụng**: Health Check giúp đảm bảo rằng chỉ những máy chủ hoặc dịch vụ khả dụng mới nhận lưu lượng truy cập. Điều này giúp tăng tính khả dụng của dịch vụ và tránh trường hợp máy chủ không hoạt động nhận lưu lượng.
* **Tối ưu hóa hiệu suất**: NLB có thể tự động điều chỉnh tải trọng cân bằng bằng cách loại bỏ máy chủ không hoạt động. Điều này giúp tối ưu hóa hiệu suất hệ thống và ngăn máy chủ quá tải.
* **Tự động quản lý**: Health Check giúp tự động quản lý tính khả dụng của máy chủ hoặc dịch vụ, giảm thiểu sự can thiệp thủ công.
* **Bảo mật**: NLB có thể loại bỏ máy chủ không hoạt động để đảm bảo rằng lưu lượng không được gửi đến các máy chủ không an toàn hoặc không hoạt động.

**Các loại cấu hình Health check NLB**

* Hướng dẫn cấu hình **Health Check TCP** khi khởi tạo Pool giao thức TCP/Proxy.
* Hướng dẫn cấu hình **Health Check HTTP/HTTPS** khi khởi tạo Pool giao thức TCP/Proxy.
* Hướng dẫn cấu hình **Health Check PING-UDP** khi khởi tạo Pool giao thức UDP.

#### 1. Hướng dẫn cấu hình Health Check TCP khi khởi tạo Pool giao thức TCP/Proxy <a href="#confighealthchecksetting-nlb-1.huongdancauhinhhealthchecktcpkhikhoitaopoolgiaothuctcp-proxy" id="confighealthchecksetting-nlb-1.huongdancauhinhhealthchecktcpkhikhoitaopoolgiaothuctcp-proxy"></a>

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

1. **Chọn giao thức TCP.**
2. **Cài đặt cấu hình nâng cao:**
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

#### 2. Hướng dẫn cấu hình Health Check HTTP/HTTPS khi khởi tạo Pool giao thức TCP/Proxy <a href="#confighealthchecksetting-nlb-2.huongdancauhinhhealthcheckhttp-httpskhikhoitaopoolgiaothuctcp-proxy" id="confighealthchecksetting-nlb-2.huongdancauhinhhealthcheckhttp-httpskhikhoitaopoolgiaothuctcp-proxy"></a>

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

1. **Chọn giao thức HTTP.**
2. **Cài đặt cấu hình nâng cao:**
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

#### 3. Hướng dẫn cấu hình Health Check PING-UDP khi khởi tạo Pool giao thức UDP <a href="#confighealthchecksetting-nlb-3.huongdancauhinhhealthcheckping-udpkhikhoitaopoolgiaothucudp" id="confighealthchecksetting-nlb-3.huongdancauhinhhealthcheckping-udpkhikhoitaopoolgiaothucudp"></a>

Tại cửa sổ giao diện "Thêm Pool", kéo đến phần "Cài đặt Health Check" và tiến hành cài đặt các thông tin sau:

1. **Chọn giao thức HTTP.**
2. **Cài đặt cấu hình nâng cao:**
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
