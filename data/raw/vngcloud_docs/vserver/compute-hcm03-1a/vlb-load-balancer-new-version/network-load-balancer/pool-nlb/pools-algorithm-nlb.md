# Pool's algorithm (NLB)

Load balancing hay "Cân bằng tải" là một trong những tính năng chính của dịch vụ Load Balancer (vLB) của VNG CLOUD. Nó là quá trình nhận yêu cầu của khách hàng ở Listener và phân phối chúng cho một số Member (server) theo các thuật toán đã được thiết lập. Nhờ vào tính năng này dịch vụ của người dùng được gia tăng năng lực xử lý với việc tạo nhiều hoặc một cụm server đứng sau LB.

Thuật toán Cân bằng tải sẽ xác định Member (server) nào được chọn khi cân bằng tải. Load Balancer của VNG CLOUD cung cấp ba loại thuật toán Cân bằng tải như sau:

* **Round Robin**
* **Least Connection**
* **Source IP**

### **1. Round Robin** <a href="#poolsalgorithm-nlb-1.roundrobin" id="poolsalgorithm-nlb-1.roundrobin"></a>

Round Robin là thuật toán lựa chọn các Member (server) theo trình tự. Theo đó, Load Balancer sẽ bắt đầu đi từ Member (server) số 1 trong danh sách của nó ứng với yêu cầu đầu tiên. Tiếp đó, nó sẽ di chuyển dần xuống trong danh sách theo thứ tự và bắt đầu lại ở đầu trang khi đến Member (server) cuối cùng.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553887/image2020-5-24_22-18-14.png?version=1&#x26;modificationDate=1694660193000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

### **2. Least Connection** <a href="#poolsalgorithm-nlb-2.leastconnection" id="poolsalgorithm-nlb-2.leastconnection"></a>

Các request sẽ được chuyển vào server có ít kết nối (active connection) nhất trong hệ thống tại thời điểm hiện tại. Thuật toán này được coi như thuật toán động, vì nó phải đếm số kết nối đang hoạt động của server.

**Cách hoạt động**

Ví dụ: Chúng ta có 5 client gửi kết nối tới 2 server, thì khi có thêm request từ client thứ 6, request sẽ được điều phối như thế nào?

* Trường hợp 1: Nếu không có client nào ngắt kết nối, client 6 sẽ được gửi sang Server 2 do tỉ lệ connection giữa hai Server đang là 3:2. Xem hình minh họa bên dưới.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553887/image2020-5-24_22-19-20.png?version=1&#x26;modificationDate=1694660193000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Trường hợp 2: Nếu client 1 & 3 ngắt kết nối trước khi client 6 gửi request, thì khi gửi request, client 6 sẽ được gửi sang Server 1 do tỉ lệ connection giữa hai Server đang là 1:2. Xem hình minh họa bên dưới

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553887/image2020-5-24_22-25-23.png?version=1&#x26;modificationDate=1694660193000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

### **3. Source IP** <a href="#poolsalgorithm-nlb-3.sourceip" id="poolsalgorithm-nlb-3.sourceip"></a>

Thuật toán này kết hợp địa chỉ IP nguồn và đích của client và server để tạo ra hash key duy nhất. Key này được sử dụng để phân bổ client đến một server cụ thể, và nó có thể được tạo lại nếu session bị timeout hay ngắt kết nối do một lý do nào đó. Khi đó request của client vẫn được chuyển đến cùng một server mà nó đã sử dụng trước đó. Đây là một phương pháp để đảm bảo rằng người dùng sẽ kết nối với cùng một server. Ví dụ: để giữ lại các mặt hàng trong giỏ hàng giữa các phiên.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553887/image2020-5-24_22-34-57.png?version=1&#x26;modificationDate=1694660194000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\
