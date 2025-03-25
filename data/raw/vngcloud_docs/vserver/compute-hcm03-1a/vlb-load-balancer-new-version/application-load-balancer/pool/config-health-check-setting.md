# Config health check setting

Tính năng **Health Check Setting** là một yếu tố quan trọng trong việc đảm bảo tính ổn định và khả dụng của ứng dụng trên Application Load Balancer. Khi tính năng này được kích hoạt, Load Balancer sẽ thực hiện kiểm tra sức khỏe của máy chủ backend và tự động điều chỉnh luồng lưu lượng truy cập để đảm bảo rằng chỉ có các máy chủ khỏe mạnh được phục vụ yêu cầu từ máy khách. Đối với Application Load Balancer

**Cách hoạt động**

* Application Load Balancer sẽ định kỳ gửi các yêu cầu kiểm tra sức khỏe đến các máy chủ backend, thông qua các tùy chọn được cấu hình.
* Nếu máy chủ backend trả lời với mã trạng thái hoặc nội dung không đúng, Load Balancer sẽ coi máy chủ đó là không khỏe và ngừng gửi yêu cầu đến nó.
* Các yêu cầu từ máy khách sẽ chỉ được chuyển tiếp đến các máy chủ được xem là khỏe mạnh.
* Các cài đặt Health Check phổ biến đối với Application Load Balancer: **Heath Check TCP và Health Check HTTP**

**Lợi ích khi cài đặt Health check cho Load Balancer**

* **Tăng Khả Dụng**: Health Check Setting giúp cải thiện tính khả dụng của ứng dụng bằng cách loại bỏ máy chủ không hoạt động khỏi dịch vụ.
* **Tối Ưu Hóa Hiệu Năng**: Nó giúp Load Balancer chuyển tiếp yêu cầu đến các máy chủ hoạt động tốt, tối ưu hóa hiệu suất hệ thống.
* **Giảm Thiểu Các Lỗi Trong Ứng Dụng**: Sự theo dõi và kiểm tra sức khỏe định kỳ giúp giảm thiểu sự cố và lỗi trong ứng dụng.

**Các loại cấu hình Health check ALB**

* Hướng dẫn cấu hình **Health Check TCP** khi khởi tạo Pool.
* Hướng dẫn cấu hình **Health Check HTTP** khi khởi tạo Pool.

#### 1. Hướng dẫn cấu hình Health Check TCP khi khởi tạo Pool <a href="#confighealthchecksetting-1.huongdancauhinhhealthchecktcpkhikhoitaopool" id="confighealthchecksetting-1.huongdancauhinhhealthchecktcpkhikhoitaopool"></a>

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

#### 2. Hướng dẫn cấu hình Health Check HTTP khi khởi tạo Pool <a href="#confighealthchecksetting-2.huongdancauhinhhealthcheckhttpkhikhoitaopool" id="confighealthchecksetting-2.huongdancauhinhhealthcheckhttpkhikhoitaopool"></a>

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

\
