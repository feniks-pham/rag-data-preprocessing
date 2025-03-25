# Listener cho Application LB

## Thêm mới HTTP Listener

1/ Truy cập vào mục Load Balancers;

2/ Tại Load Balancers, click chọn Load Balancer cần thêm mới Listener.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn chọn nút "Thêm mới Listener", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Listener

5/ Tại cửa sổ thêm mới, cấu hình các thông tin như:

* **Tên Listener:** Lưu ý rằng tên Listener không thể thay đổi sau khi khởi tạo
* **Chọn Giao thức HTTP và Port** (mặc định hiển thị Port 80 và tăng dần nếu các Port nhỏ hơn đã được sử dụng)
* **Cấu hình request Header** tại phần cấu hình nâng cao: Mặc định điền sẵn X-Fowarded-For, X-Forwarded-Proto, X-Fowarded-Port, có thể bỏ chọn Header nếu không có nhu cầu.
* **Cấu hình Pool mặc định và hành động:** Trong trường các request đến Listener nằm ngoài danh sách Policies được cấu hình, các request này sẽ được chuyển hướng đến Pool mặc định để xử lý.
* **Cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
  * [Config timeout](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-timeout.md)
  * [Config IP whitelist to load balancer](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-ip-whitelist-to-load-balancer.md)

***

## Thêm mới HTTPS Listener

1/ Truy cập vào mục Load Balancers;

2/ Tại Load Balancers, click chọn Load Balancer cần thêm mới Listener.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn chọn nút "Thêm mới Listener", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Listener

5/ Tại cửa sổ thêm mới, cấu hình các thông tin như:

* **Tên Listener:** Lưu ý rằng tên Listener không thể thay đổi sau khi khởi tạo
* **Chọn Giao thức HTTPS và Port** (mặc định hiển thị Port 443 và tăng dần nếu các Port nhỏ hơn đã được sử dụng)
* **Chọn Certificate mặc định**
* **Chọn danh sách Certificate sử dụng như là SNI:** Lưu ý rằng bạn không thể gỡ bỏ/thay đổi các Certificate dùng cho tính năng SNI một khi hoàn tất khởi tạo HTTPS Listener
* **Cấu hình request Header** tại phần cấu hình nâng cao: Mặc định điền sẵn X-Fowarded-For, X-Forwarded-Proto, X-Fowarded-Port, có thể bỏ chọn Header nếu không có nhu cầu.
* **Bật tính năng Client Certificate Authentication:** Client CA là tính năng bảo mật nâng cao của Load Balancer, giúp xác thực ứng dụng khách bằng cách sử dụng Certificate. Tìm hiểu thêm về tính năng [Client Certificate Authentication](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/client-certificate-authentication.md)
* **Cấu hình Pool mặc định và hành động:** Trong trường các request đến Listener nằm ngoài danh sách Policies được cấu hình, các request này sẽ được chuyển hướng đến Pool mặc định để xử lý.
* **Cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
  * [Config timeout](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-timeout.md)
  * [Config IP whitelist to load balancer](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-ip-whitelist-to-load-balancer.md)

***

## Thay đổi thông tin Listener <a href="#update-and-deletelistener-nlb-thaydoithongtinlistener" id="update-and-deletelistener-nlb-thaydoithongtinlistener"></a>

1/ Truy cập vào mục Load Balancers

2/ Tại trang chủ Load Balancers, click chọn Load Balancer cần chỉnh sửa Listener.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Tại danh sách Listener, rê chuột đến Listener cần chỉnh sửa, một biểu tượng "Edit" sẽ hiện lên, nhấn vào biểu tượng đó để bắt đầu chỉnh sửa Listener.

5/ Một cửa sổ giao diện chỉnh sửa xuất hiện, người dùng có thể chỉnh sửa các thông tin sau:

* **Thay đổi Pool mặc định:** Trong trường các request đến Load Balancer mà không phù hợp với bất kỳ pool cụ thể nào, NLB sẽ chuyển hướng lưu lượng đó đến pool mặc định.
* **Thay đổi cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
  * [Config timeout](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-timeout.md)
  * [Config IP whitelist to load balancer](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-ip-whitelist-to-load-balancer.md)

6/ Nhấn nút "Lưu" để hoàn tất chỉnh sửa

***

## Xóa Listener <a href="#update-and-deletelistener-nlb-xoalistener" id="update-and-deletelistener-nlb-xoalistener"></a>

1/ Truy cập vào mục Load Balancer

2/ Tại Load Balancers, click chọn Load Balancer cần xóa Listener.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Tại danh sách Listener, nhấn chọn biểu tượng "Xóa" tại hàng Listener cần xóa.

5/ Một cửa sổ giao diện sẽ xuất hiện để xác nhận xóa, nhấn nút "Xóa" để hoàn tất.

***

## Listener Policies

Nhìn chung, Policies quyết định cách Load Balancer, cụ thể là Listener sẽ xử lý yêu cầu, chẳng hạn như định tuyến đến máy chủ backend, thực hiện chuyển hướng, và nhiều tính năng khác.

### 1. Thêm Policy <a href="#listenerpolicies-1.thempolicy" id="listenerpolicies-1.thempolicy"></a>

Để thêm 1 Policy vào Listener, bạn thực hiện theo các hướng dẫn dưới đây

1/ Truy cập vào mục Load Balancers;

2/ Tại Load Balancers, click chọn Load Balancer cần cấu hình.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn chọn Listener cần thêm Policy.

5/ Tại phần thông tin chi tiết Listener tương ứng phía bên trái, kéo đến mục Thông tin Policy.

6/ Nhấn nút "Thêm Policy" tại góc trên bên phải của phần Thông tin Policy.

7/ Một cửa sổ giao diện bật lên cho phép bạn cấu hình Policy với các thông tin như

* **Tên Policy**
* **Điều kiện Nếu (IF):**
  * Kiểm tra request đến dựa vào **HOST/PATH**
  * Cách kiểm tra request đến dựa vào HOST/PATH: **CONTAINS** (có chứa 1 giá trị cụ thể) / **EQUAL** (chứa chính xác 1 giá trị cụ thể)
  * Nhập vào giá trị HOST/PATH cần kiểm tra
* **Hành động Thì (THEN):** Khi thỏa điều kiện bên trên, bạn cần cấu hình thêm hành động thực hiện điều phối request, hiện đang hỗ trợ các hành động điều phối như sau
  * **Forward to pool:** Khi thỏa điều kiện, request đến sẽ được đẩy vào pool được chọn, do đó cần **chọn một Pool từ danh sách Pool thuộc Load Balancer** được hiển thị để điều hướng request đến.
  * **Redirect to Url:** Nhập URL bạn muốn chuyển request đến khi thỏa điều kiện.

8/ Nhấn nút "Thêm" để hoàn tất việc thêm mới

### 2. Cập nhật Policy <a href="#listenerpolicies-2.capnhatpolicy" id="listenerpolicies-2.capnhatpolicy"></a>

Để cập nhật bộ điều kiện & hành động của một Policy, bạn làm theo hướng dẫn dưới đây

1/ Truy cập vào mục Load Balancer;

2/ Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn chọn Listener cần cập nhật Policy.

5/ Tại phần thông tin chi tiết Listener tương ứng phía bên trái, kéo đến mục Thông tin Policy.

6/ Tại phần danh sách Policy, nhấn vào biểu tượng Edit tại Policy cần cập nhật

7/ Một cửa sổ giao diện bật lên cho phép bạn chỉnh sửa Policy với các thông tin về Điều kiện Nếu (IF) & Hành động Thì (THEN)

8/ Nhấn nút "Thêm" để hoàn tất việc thêm mới

### 3. Sắp xếp Policy <a href="#listenerpolicies-3.sapxeppolicy" id="listenerpolicies-3.sapxeppolicy"></a>

Việc sắp xếp các Policy trên một Listener trong Load Balancer rất quan trọng vì nó ảnh hưởng trực tiếp đến cách các quy tắc và hành vi được áp dụng cho lưu lượng truy cập. Các Policy được áp dụng theo thứ tự từ trên xuống dưới trên một Listener. Điều này có nghĩa là Policy ở phía trên sẽ có ưu tiên hơn Policy ở phía dưới. Việc sắp xếp có thể cho phép bạn ưu tiên việc áp dụng các quy tắc quan trọng hơn trước.

Để sắp xếp các Policy theo thứ tự mong muốn, bạn làm theo hướng dẫn dưới đây

1/ Truy cập vào mục Load Balancer ;

2/ Tại Load Balancers, click chọn Load Balancer cần cấu hình.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn chọn Listener cần thêm Policy.

5/ Tại phần thông tin chi tiết Listener tương ứng phía bên trái, kéo đến mục Thông tin Policy.

6/ Nhấn nút "Sắp xếp lại / Reorder" tại góc trên bên phải của phần Thông tin Policy, kế bên nút Thêm Policy.

7/ Tại đây, bạn có thể kéo/thả các Policy theo độ ưu tiên mong muốn

8/ Nhấn nút "Save" để hoàn tất việc sắp xếp Policy tại vị trí nút "Sắp xếp lại /Reorder" ban đầu.

***

## Client Certificate Authentication

Tính năng "**Client Certificate Authentication**" là một phần quan trọng của hệ thống bảo mật mạng và ứng dụng. Nó cho phép bạn đảm bảo rằng chỉ những khách hàng hoặc thiết bị nào có chứng chỉ xác thực hợp lệ mới có thể truy cập vào ứng dụng hoặc dịch vụ của bạn.**Cơ chế hoạt động**

* Khi một khách hàng hoặc thiết bị truy cập vào ứng dụng của bạn, hệ thống yêu cầu họ cung cấp một chứng chỉ số học xác thực riêng biệt.
* Chứng chỉ này thường được tạo và quản lý bởi một tổ chức chứng thực hoặc PKI (Public Key Infrastructure).
* Hệ thống sau đó kiểm tra chứng chỉ này để đảm bảo rằng nó hợp lệ và có thể xác định khách hàng hoặc thiết bị.
* Nếu chứng chỉ hợp lệ, khách hàng hoặc thiết bị được cho phép truy cập vào ứng dụng hoặc dịch vụ.

**Lợi ích**

* **Bảo Mật Tăng Cao**: Xác thực chứng chỉ tạo ra một lớp bảo mật mạnh mẽ bằng cách đảm bảo rằng chỉ có những người dùng hoặc thiết bị được xác định và có quyền truy cập.
* **Quản Lý Truy Cập Chi Tiết**: Bạn có thể quản lý truy cập của từng khách hàng hoặc thiết bị dựa trên chứng chỉ riêng biệt.
* **Tuân Thủ Bảo Mật**: Nó giúp bạn tuân thủ các quy tắc và tiêu chuẩn bảo mật nghiêm ngặt.

**Cách bật/tắt tính năng Client Certificate Authentication**

Đối với HTTPS Listener, người dùng có thể chủ động bật/tắt tính năng Client Certificate bất kỳ lúc nào.**Hướng dẫn bật/tắt Client Certificate Authentication**

1/ Truy cập vào mục Load Balancer;​

2/ Tại Load Balancer, click chọn Load Balancer cần chỉnh sửa.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn biểu tượng Edit tại HTTPS Listener cần bật/tắt tính năng Client CA.

5/ Một cửa sổ giao diện sẽ hiện ra, tại phần thông tin Listener, tìm đến Cài đặt nâng cao.

6/ Tại phần Cài đặt nâng cao, check/uncheck vào check box Bật Client CA. Trường hợp Bật Client CA, người dùng cần chọn một Certificate từ danh sách Certificate trên hệ thống.

7/ Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.

***

## Config IP whitelist to load balancer

Tính năng **cấu hình Whitelist IP Source** cho Load Balancer là một phần quan trọng của bảo mật mạng, cho phép bạn xác định các địa chỉ IP nguồn cụ thể mà Load Balancer sẽ chấp nhận lưu lượng từ. Các địa chỉ IP không nằm trong dải IP cho phép sẽ bị từ chối truy cập.**Cách hoạt động**

* Khi một yêu cầu truy cập đến Load Balancer, hệ thống sẽ kiểm tra địa chỉ IP nguồn của yêu cầu.
* Nếu địa chỉ IP nguồn nằm trong dải CIDRs cho phép, yêu cầu sẽ được chấp nhận và tiếp tục đến máy chủ backend.
* Nếu địa chỉ IP nguồn không nằm trong dải CIDRs cho phép, yêu cầu sẽ bị từ chối và không được chuyển tiếp.

**Tại sao cần cấu hình IP Whitelist đến Load Balancer**

* **Bảo Mật Tăng Cao**: Tính năng này tăng cường bảo mật bằng cách kiểm soát chặt chẽ quyền truy cập từ các địa chỉ IP nguồn không xác định.
* **Phòng Chống Tấn Công**: Nó giúp ngăn chặn các tấn công từ các địa chỉ IP đáng ngờ hoặc không mong muốn.
* **Quản Lý Quyền Truy Cập**: Whitelist IP Source cho phép bạn quản lý quyền truy cập vào Load Balancer một cách chi tiết và hiệu quả.

**Hướng dẫn cấu hình**

1/ Truy cập vào mục Load Balancers;​

2/ Tại Load Balancers, click chọn Load Balancer cần cấu hình.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn biểu tượng Edit tại Listener cần cấu hình.

5/ Một cửa sổ giao diện sẽ hiện ra, tìm đến phần Cấu hình nâng cao ở phía dưới cùng của cửa sổ.

6/ Tại phần Allowed CIDRs (Cho phép CIDRs), người dùng có thể cấu hình dải IP được phép truy cập.

* Ví dụ người dùng nhâp "192.168.0.0/24, 172.16.0.0/24" có nghĩa là chỉ những địa chỉ IP thuộc 2 dải IP Range này mới có quyền truy cập.

7/ Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.

***

## Config timeout

Tính năng **cấu hình timeout** cho Load Balancer cho phép bạn định rõ thời gian tối đa mà một kết nối hoặc yêu cầu có thể tồn tại trước khi bị đóng. Điều này quan trọng để quản lý tài nguyên và đảm bảo hiệu suất ổn định của hệ thống.

**Cách hoạt động**

* Khi một kết nối hoặc yêu cầu được gửi đến Load Balancer, hệ thống bắt đầu tính toán thời gian cho phép kết nối đó tồn tại.
* Nếu kết nối không hoàn thành hoặc yêu cầu không được phản hồi trong khoảng thời gian này, nó sẽ bị đóng.
* Việc cấu hình Timeout giúp tránh tình trạng kết nối hoặc yêu cầu bị treo và tiêu tốn tài nguyên.

**Tại sao cần cấu hình Timeout cho Load Balancer**

* **Quản Lý Tài Nguyên**: Timeout cấu hình giúp quản lý hiệu quả tài nguyên hệ thống bằng cách đảm bảo rằng các kết nối hoặc yêu cầu không cần thiết không tiêu tốn tài nguyên.
* **Bảo Đảm Hiệu Suất**: Điều này giúp đảm bảo rằng Load Balancer luôn hoạt động hiệu quả và không bị kẹt trong các kết nối hoặc yêu cầu không đáp ứng.

#### Hướng dẫn cấu hình timeout cho Load Balancer <a href="#configtimeout-huongdancauhinhtimeoutcholoadbalancer" id="configtimeout-huongdancauhinhtimeoutcholoadbalancer"></a>

1/ Truy cập vào trang chủ Load Balancer&#x20;

2/ Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn biểu tượng Edit tại Listener cần cấu hình Timeout.

5/ Một cửa sổ giao diện sẽ hiện ra, tìm đến phần Cấu hình nâng cao ở phía dưới cùng của cửa sổ.

6/ Tại phần Idle Timeout, người dùng có thể cấu hình Timeout dựa trên các thuộc tính sau

* **Client Timeout (Timeout của Khách hàng):**
  * **Giải thích**: Client Timeout là thời gian tối đa mà Load Balancer cho phép một khách hàng (client) duy trì kết nối đến nó mà không thực hiện bất kỳ yêu cầu (request) nào. Nếu trong khoảng thời gian này không có hoạt động nào từ phía khách hàng, kết nối sẽ bị đóng.
  * **Lợi ích**: Điều này giúp giải phóng tài nguyên máy chủ backend và Load Balancer, đảm bảo rằng không có kết nối không cần thiết tiêu tốn tài nguyên.
* **Member Timeout (Timeout của Member):**
  * **Giải thích**: Member Timeout là thời gian tối đa mà Load Balancer cho phép một máy chủ thành viên (member) trong nhóm máy chủ backend duy trì một kết nối mở mà không nhận được dữ liệu từ nó. Nếu máy chủ thành viên không gửi dữ liệu trong khoảng thời gian này, kết nối sẽ bị đóng.
  * **Lợi ích**: Điều này giúp đảm bảo rằng máy chủ thành viên không tiêu tốn tài nguyên bằng cách duy trì các kết nối không hoạt động.
* **Connection Timeout (Timeout Kết nối):**
  * **Giải thích**: Connection Timeout là thời gian tối đa mà Load Balancer cho phép một kết nối mạng giữa nó và một máy chủ backend tồn tại trước khi bị đóng. Thời gian này bắt đầu tính từ khi kết nối được thiết lập. Nếu trong khoảng thời gian này không có hoạt động gì trên kết nối (bao gồm cả truyền dữ liệu), kết nối sẽ bị đóng.
  * **Lợi ích**: Điều này giúp đảm bảo rằng kết nối không cần thiết sẽ bị đóng, giải phóng tài nguyên và đảm bảo hiệu suất mạng ổn định.

7/ Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.
