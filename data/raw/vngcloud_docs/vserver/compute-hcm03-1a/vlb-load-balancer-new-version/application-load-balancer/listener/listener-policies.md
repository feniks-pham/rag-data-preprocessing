# Listener Policies

Trong HTTP/HTTPS Listener, Policies là các thành phần quan trọng giúp bạn kiểm soát và định tuyến lưu lượng truy cập đến các máy chủ backend. Policies là bộ quy tắc bao gồm hai thành phần chính:

* **Điều kiện**: Điều kiện kiểm tra các request đến
* **Hành động**: Một khi các request đến khớp với các Điều kiện trên, thì Hành động tương ứng sẽ được áp dụng trong việc điều phối yêu cầu.

**Cách Hoạt Động**

* Khi một yêu cầu truy cập đến Listener, hệ thống sẽ kiểm tra các Policies một cách tuần tự để xác định xem quy tắc nào sẽ được áp dụng.
* Nếu một request đến khớp với **điều kiện** (ví dụ: kiểm tra host, path của request đến), thì **hành động** liên quan đến **điều kiện** đó sẽ được áp dụng.

Nhìn chung, Policies quyết định cách Load Balancer, cụ thể là Listener sẽ xử lý yêu cầu, chẳng hạn như định tuyến đến máy chủ backend, thực hiện chuyển hướng, và nhiều tính năng khác.

#### 1. Thêm Policy <a href="#listenerpolicies-1.thempolicy" id="listenerpolicies-1.thempolicy"></a>

Để thêm 1 Policy vào Listener, bạn thực hiện theo các hướng dẫn dưới đây

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn chọn Listener cần thêm Policy.**
5. **Tại phần thông tin chi tiết Listener tương ứng phía bên trái, kéo đến mục Thông tin Policy.**
6. **Nhấn nút "Thêm Policy" tại góc trên bên phải của phần Thông tin Policy.**
7. **Một cửa sổ giao diện bật lên cho phép bạn cấu hình Policy với các thông tin như**
   * **Tên Policy**
   * **Điều kiện Nếu (IF):**
     * Kiểm tra request đến dựa vào **HOST/PATH**
     * Cách kiểm tra request đến dựa vào HOST/PATH: **CONTAINS** (có chứa 1 giá trị cụ thể) / **EQUAL** (chứa chính xác 1 giá trị cụ thể)
     * Nhập vào giá trị HOST/PATH cần kiểm tra
   * **Hành động Thì (THEN):** Khi thỏa điều kiện bên trên, bạn cần cấu hình thêm hành động thực hiện điều phối request, hiện đang hỗ trợ các hành động điều phối như sau
     * **Forward to pool:** Khi thỏa điều kiện, request đến sẽ được đẩy vào pool được chọn, do đó cần **chọn một Pool từ danh sách Pool thuộc Load Balancer** được hiển thị để điều hướng request đến.
     * **Redirect to Url:** Nhập URL bạn muốn chuyển request đến khi thỏa điều kiện.
8. **Nhấn nút "Thêm" để hoàn tất việc thêm mới**

#### 2. Cập nhật Policy <a href="#listenerpolicies-2.capnhatpolicy" id="listenerpolicies-2.capnhatpolicy"></a>

Để cập nhật bộ điều kiện & hành động của một Policy, bạn làm theo hướng dẫn dưới đây

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn chọn Listener cần cập nhật Policy.**
5. **Tại phần thông tin chi tiết Listener tương ứng phía bên trái, kéo đến mục Thông tin Policy.**
6. **Tại phần danh sách Policy, nhấn vào biểu tượng Edit tại Policy cần cập nhật**
7. **Một cửa sổ giao diện bật lên cho phép bạn chỉnh sửa Policy với các thông tin về Điều kiện Nếu (IF) & Hành động Thì (THEN)**
8. **Nhấn nút "Thêm" để hoàn tất việc thêm mới**

#### 3. Sắp xếp Policy <a href="#listenerpolicies-3.sapxeppolicy" id="listenerpolicies-3.sapxeppolicy"></a>

Việc sắp xếp các Policy trên một Listener trong Load Balancer rất quan trọng vì nó ảnh hưởng trực tiếp đến cách các quy tắc và hành vi được áp dụng cho lưu lượng truy cập. Các Policy được áp dụng theo thứ tự từ trên xuống dưới trên một Listener. Điều này có nghĩa là Policy ở phía trên sẽ có ưu tiên hơn Policy ở phía dưới. Việc sắp xếp có thể cho phép bạn ưu tiên việc áp dụng các quy tắc quan trọng hơn trước.

Để sắp xếp các Policy theo thứ tự mong muốn, bạn làm theo hướng dẫn dưới đây

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Listener.**
4. **Nhấn chọn Listener cần thêm Policy.**
5. **Tại phần thông tin chi tiết Listener tương ứng phía bên trái, kéo đến mục Thông tin Policy.**
6. **Nhấn nút "Sắp xếp lại / Reorder" tại góc trên bên phải của phần Thông tin Policy, kế bên nút Thêm Policy.**
7. **Tại đây, bạn có thể kéo/thả các Policy theo độ ưu tiên mong muốn**
8. **Nhấn nút "Save" để hoàn tất việc sắp xếp Policy tại vị trí nút "Sắp xếp lại /Reorder" ban đầu.**
