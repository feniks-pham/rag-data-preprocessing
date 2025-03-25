# Listener cho Network LB

## T**hêm mới TCP Listener**

1/ Truy cập vào mục Load Balancers;

2/ Tại  Load Balancers, click chọn Load Balancer cần thêm mới Listener.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn chọn nút "Thêm mới Listener", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Listener

5/ Tại cửa sổ thêm mới, cấu hình các thông tin như:

* **Tên Listener:** Lưu ý rằng tên Listener không thể thay đổi sau khi khởi tạo
* **Chọn Giao thức TCP và Port** (mặc định hiển thị Port 80 và tăng dần nếu các Port nhỏ hơn đã được sử dụng)
* **Cấu hình Pool mặc định và hành động:** Trong trường các request đến Load Balancer mà không phù hợp với bất kỳ pool cụ thể nào, NLB sẽ chuyển hướng lưu lượng đó đến pool mặc định.&#x20;
* **Cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
  * [Config timeout](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-timeout.md)
  * [Config IP whitelist to load balancer](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-ip-whitelist-to-load-balancer.md)

***

## **Thêm mới UDP Listener**

1/ Truy cập vào mục Load Balancers

2/ Tại trang chủ Load Balancers, click chọn Load Balancer cần thêm mới Listener.

3/ Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.

4/ Nhấn chọn nút "Thêm mới Listener", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Listener

5/ Tại cửa sổ thêm mới, cấu hình các thông tin như:

* **Tên Listener:** Lưu ý rằng tên Listener không thể thay đổi sau khi khởi tạo
* **Chọn Giao thức UDP và Port** (mặc định hiển thị Port 53 và tăng dần nếu các Port nhỏ hơn đã được sử dụng)
* **Cấu hình Pool mặc định và hành động:** Trong trường các request đến Load Balancer mà không phù hợp với bất kỳ pool cụ thể nào, NLB sẽ chuyển hướng lưu lượng đó đến pool mặc định.&#x20;
* **Cấu hình nâng cao:** Tham khảo thêm các hướng dẫn cấu hình nâng cao theo tính năng như bên dưới
  * [Config timeout](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-timeout.md)
  * [Config IP whitelist to load balancer](../../../../vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/listener/config-ip-whitelist-to-load-balancer.md)

**Lưu ý:** Lưu ý rằng bạn chỉ có thể chọn Pool với giao thức UDP để chỉ định làm Pool mặc định cho UDP Listener

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

## Cấu hình IP Whitelist to Load Balancer (NLB)

Tính năng **cấu hình Whitelist IP Source** cho Load Balancer là một phần quan trọng của bảo mật mạng, cho phép bạn xác định các địa chỉ IP nguồn cụ thể mà Load Balancer sẽ chấp nhận lưu lượng từ. Các địa chỉ IP không nằm trong dải IP cho phép sẽ bị từ chối truy cập.**Cách hoạt động**

* Khi một yêu cầu truy cập đến Load Balancer, hệ thống sẽ kiểm tra địa chỉ IP nguồn của yêu cầu.
* Nếu địa chỉ IP nguồn nằm trong dải CIDRs cho phép, yêu cầu sẽ được chấp nhận và tiếp tục đến máy chủ backend.
* Nếu địa chỉ IP nguồn không nằm trong dải CIDRs cho phép, yêu cầu sẽ bị từ chối và không được chuyển tiếp.

**Tại sao cần cấu hình IP Whitelist đến Load Balancer**

* **Bảo Mật Tăng Cao**: Tính năng này tăng cường bảo mật bằng cách kiểm soát chặt chẽ quyền truy cập từ các địa chỉ IP nguồn không xác định.
* **Phòng Chống Tấn Công**: Nó giúp ngăn chặn các tấn công từ các địa chỉ IP đáng ngờ hoặc không mong muốn.
* **Quản Lý Quyền Truy Cập**: Whitelist IP Source cho phép bạn quản lý quyền truy cập vào Load Balancer một cách chi tiết và hiệu quả.

**Hướng dẫn cấu hình**

* Truy cập vào trang chủ Load Balancers .​
* Tại Load Balancers, click chọn Load Balancer cần cấu hình.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.
* Nhấn biểu tượng Edit tại Listener cần cấu hình.
* Một cửa sổ giao diện sẽ hiện ra, tìm đến phần Cấu hình nâng cao ở phía dưới cùng của cửa sổ.
* Tại phần Allowed CIDRs (Cho phép CIDRs), người dùng có thể cấu hình dải IP được phép truy cập.
  * Ví dụ người dùng nhâp "192.168.0.0/24, 172.16.0.0/24" có nghĩa là chỉ những địa chỉ IP thuộc 2 dải IP Range này mới có quyền truy cập.
* Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.

***

## Cấu hình timeout (NLB)

Tính năng **cấu hình timeout** cho Load Balancer cho phép bạn định rõ thời gian tối đa mà một kết nối hoặc yêu cầu có thể tồn tại trước khi bị đóng. Điều này quan trọng để quản lý tài nguyên và đảm bảo hiệu suất ổn định của hệ thống.**Cách hoạt động**

* Khi một kết nối hoặc yêu cầu được gửi đến Load Balancer, hệ thống bắt đầu tính toán thời gian cho phép kết nối đó tồn tại.
* Nếu kết nối không hoàn thành hoặc yêu cầu không được phản hồi trong khoảng thời gian này, nó sẽ bị đóng.
* Việc cấu hình Timeout giúp tránh tình trạng kết nối hoặc yêu cầu bị treo và tiêu tốn tài nguyên.

**Tại sao cần cấu hình Timeout cho Load Balancer**

* **Quản Lý Tài Nguyên**: Timeout cấu hình giúp quản lý hiệu quả tài nguyên hệ thống bằng cách đảm bảo rằng các kết nối hoặc yêu cầu không cần thiết không tiêu tốn tài nguyên.
* **Bảo Đảm Hiệu Suất**: Điều này giúp đảm bảo rằng Load Balancer luôn hoạt động hiệu quả và không bị kẹt trong các kết nối hoặc yêu cầu không đáp ứng.

**Hướng dẫn cấu hình timeout cho Load Balancer**

* **T**ruy cập vào mục Load Balancer.​
* Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.
* Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.
* Nhấn biểu tượng Edit tại Listener cần cấu hình Timeout.
* Một cửa sổ giao diện sẽ hiện ra, tìm đến phần Cấu hình nâng cao ở phía dưới cùng của cửa sổ.
* Tại phần Idle Timeout, người dùng có thể cấu hình Timeout dựa trên các thuộc tính sau
  * Client Timeout (Timeout của Khách hàng):
    * Giải thích: Client Timeout là thời gian tối đa mà Load Balancer cho phép một khách hàng (client) duy trì kết nối đến nó mà không thực hiện bất kỳ yêu cầu (request) nào. Nếu trong khoảng thời gian này không có hoạt động nào từ phía khách hàng, kết nối sẽ bị đóng.
    * Lợi ích: Điều này giúp giải phóng tài nguyên máy chủ backend và Load Balancer, đảm bảo rằng không có kết nối không cần thiết tiêu tốn tài nguyên.
  * Member Timeout (Timeout của Member):
    * **Giải thích**: Member Timeout là thời gian tối đa mà Load Balancer cho phép một máy chủ thành viên (member) trong nhóm máy chủ backend duy trì một kết nối mở mà không nhận được dữ liệu từ nó. Nếu máy chủ thành viên không gửi dữ liệu trong khoảng thời gian này, kết nối sẽ bị đóng.
    * **Lợi ích**: Điều này giúp đảm bảo rằng máy chủ thành viên không tiêu tốn tài nguyên bằng cách duy trì các kết nối không hoạt động.
    * **Connection Timeout (Timeout Kết nối):**
      * **Giải thích**: Connection Timeout là thời gian tối đa mà Load Balancer cho phép một kết nối mạng giữa nó và một máy chủ backend tồn tại trước khi bị đóng. Thời gian này bắt đầu tính từ khi kết nối được thiết lập. Nếu trong khoảng thời gian này không có hoạt động gì trên kết nối (bao gồm cả truyền dữ liệu), kết nối sẽ bị đóng.
      * **Lợi ích**: Điều này giúp đảm bảo rằng kết nối không cần thiết sẽ bị đóng, giải phóng tài nguyên và đảm bảo hiệu suất mạng ổn định.
* Nhấn nút "Lưu" tại góc dưới bên phải của cửa sổ để hoàn tất việc cập nhật.
