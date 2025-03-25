# Thay đổi kích thước máy chủ ảo

Trong trường hợp tài nguyên của máy chủ không đáp ứng được nhu cầu của dịch vụ, người dùng có thể thay đổi cấu hình tài nguyên như vCPU và bộ nhớ bằng cách thay đổi cấu hình flavor cho máy chủ ảo.

### **Thay đổi Flavor** <a href="#thaydoikichthuocmaychuao-thaydoiflavor" id="thaydoikichthuocmaychuao-thaydoiflavor"></a>

Flavor là một thông số cấu hình định nghĩa tài nguyên vCPU và bộ nhớ cho 1 máy chủ ảo. Khi cần thay đổi Flavor cho máy chủ ảo, người dùng sẽ chọn flavor mới từ danh sách Flavor có sẵn.

Cần stop máy chủ trước khi thực hiện thay đổi cấu hình Flavor. Quá trình thay đổi Flavor này chỉ thay đổi cấu hình tài nguyên vCPU và bộ nhớ, nếu người dùng cần thay đổi dung lượng lưu trữ của máy chủ thì phải chuyển qua chức năng mở rộng Volume.

Chi phí và cách tính toán theo cấu hình mới sẽ xuất hiện bên phải màn hình khi người dùng thực hiện thay đổi Flavor.

### **Cách thực hiện** <a href="#thaydoikichthuocmaychuao-cachthuchien" id="thaydoikichthuocmaychuao-cachthuchien"></a>

Trước khi thực hiện thay đổi flavor cho máy chủ ảo, bạn cần xác định trước flavor cũng như tìm hiểu các thuộc tính về nó như loại máy chủ, công nghệ CPU… Xem thêm tại [{Trang Flavor}](flavor.md).

1. Đăng nhập vào VNG Cloud portal và đi đến trang dịch vụ vServer tại đường link: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Tại trang Cloud Server, xác định máy chủ ảo cần thay đổi cấu hình, cần đảm bảo máy chủ đã stop trước khi thực hiện thay đổi. Vào danh sách Menu bên phải và chọn Resize
3. Chọn flavor mong muốn
4. Bạn có thể xem tóm tắt chi phí phát sinh mới hoặc chi phí được trả lại trong trường hợp thay đổi cấu hình nhỏ hơn, nhấn nút **Resize Server** để hoàn thành
5. Bạn cần chờ cho đến khi trạng thái của máy chủ ảo trở về lại Stop

\
