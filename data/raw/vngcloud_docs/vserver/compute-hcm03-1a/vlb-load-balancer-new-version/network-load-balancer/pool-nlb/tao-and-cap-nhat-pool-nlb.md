# Tạo & cập nhật Pool (NLB)

Sử dụng hướng dẫn này để thêm mới/cập nhật một Pool vào một Network Load Balancer có sẵn.

#### 1. Cách thêm mới Pool <a href="#add-and-updateapool-nlb-1.cachthemmoipool" id="add-and-updateapool-nlb-1.cachthemmoipool"></a>

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần thêm mới Pool.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.**
4. **Nhấn chọn nút "Thêm mới Pool", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Pool**
5. **Tại cửa sổ thêm mới, cấu hình các thông tin như:**
   * **Tên Pool:** Lưu ý rằng tên Pool không thể thay đổi sau khi khởi tạo
   * **Giao thức: TCP / Proxy / UDP**
   * **Chọn thuật toán cân bằng tải:** Tham khảo thêm các thuật toán cân bằng tải [Pool's algorithm (NLB)](../../application-load-balancer/pool/pools-algorithm.md)
   * **Cài đặt Health Check:** Tham khảo hướng dẫn cài đặt Health Check NLB tại [Config health check setting (NLB)](../../application-load-balancer/pool/config-health-check-setting.md)
   * **Thêm Pool Member:** Tham khảo hướng dẫn [Attach Pool Member (NLB)](https://docs.vngcloud.vn/pages/viewpage.action?pageId=64553815)
6. **Nhấn nút "Thêm" tại góc dưới bên phải của cửa sổ thêm mới để hoàn tất việc thêm Pool**

#### 2. Cách cập nhật thông tin Pool <a href="#add-and-updateapool-nlb-2.cachcapnhatthongtinpool" id="add-and-updateapool-nlb-2.cachcapnhatthongtinpool"></a>

1. **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
2. **Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.**
3. **Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.**
4. **Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.**
5. **Một cửa sổ bật lên cho phép chỉnh sửa Pool, các thông tin được phép cập nhật**
   * **Thuật toán cân bằng tải**
   * **Cấu hình health check nâng cao**
6. **Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất việc cập nhập Pool**
