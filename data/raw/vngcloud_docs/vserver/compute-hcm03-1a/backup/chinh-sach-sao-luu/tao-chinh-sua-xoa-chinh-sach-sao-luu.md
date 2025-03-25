# Tạo, chỉnh sửa, xóa chính sách sao lưu

Để có thể tạo bản sao lưu cho tài nguyên của mình bạn cần tạo mới chính sách.

Khi yêu cầu sao lưu thay đổi bạn có thể cập nhật lại các chính sách hiện có.

Khi bạn không cần chính sách đó nữa, bạn cần tách chính sách đó ra khỏi các tài nguyên sao lưu và bạn có thể xóa chính sách đó.

***

### **Tạo chính sách sao lưu** <a href="#tao-chinhsua-xoachinhsachsaoluu-taochinhsachsaoluu" id="tao-chinhsua-xoachinhsachsaoluu-taochinhsachsaoluu"></a>

{% hint style="info" %}
**Quan trọng**

Hãy đảm bảo rằng các quy luật trong chính sách sao lưu bạn tạo đáp ứng đầy đủ nhu cầu sử dụng nhưng không quá dư thừa, vì điều đó sẽ dẫn đến tiêu tốn chi phí và tài nguyên hệ thống.
{% endhint %}

Bạn có thể tạo chính sách trong Bảng điều khiển quản lý vServer bằng trình chỉnh sửa trực quan cho phép bạn chọn các tùy chọn tạo các chính sách cho bạn. Đó là một cách tuyệt vời để tạo các chính sách đầu tiên của bạn và cảm thấy thoải mái khi sử dụng chúng.

**Quy trình tạo chính sách sao lưu:**

1. Mở bảng điều khiển vBackup tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-policy](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-policy)
2. Tại thanh menu điều hướng, chọn Tab **Backup Policy**
3. Chọn **Tạo Backup Policy**
4. Tại trang tạo Policy, nhập thông tin **Tên Policy** tại mục **Thông tin cơ bản**
5. Sau đó tại mục **Cài đặt chính sách**, lựa chọn **thời gian** và **múi giờ** mà hệ thống sẽ thực hiện sao lưu
6. Chọn **tần suất sao lưu** phù hợp với nhu cầu sử dụng của bạn theo Hàng Ngày, Hàng Tuần, Hàng Tháng. Lưu ý rằng bạn có thể kết hợp cả 3 với nhau để tạo ra bộ lịch hoàn hảo nhất
7. Nhập **số bản lưu** mà hệ thống sẽ lưu giữ các bản sao lưu gần nhất
8. Ngoài ra bạn có thể lựa chọn **tự động sao lưu** cho các **ổ đĩa** được thêm vào máy ảo sau này
9. Chọn **Tạo Backup Policy**
10. Sau đó bạn có thể xem thông tin chính sách sao lưu vừa tạo tại màn hình danh sách

{% hint style="info" %}
**Cách hoạt động của chính sách sao lưu**

Một chính sách sao lưu được lựa chọn tần suất sao lưu theo **Hàng Ngày** lúc **12:00** và số bản lưu **4**. Vào mỗi ngày lúc 12:00 trưa, hệ thống theo khung giờ trên sẽ tạo bản sao lưu cho máy chủ ảo, với lần sao lưu đầu tiên sẽ là bản sao lưu đầy đủ cho máy chủ ảo, vào ngày tiếp theo sẽ sao lưu các phần thay đổi của máy ảo kể từ lần sao lưu cuối của ngày hôm qua, số bản lưu giữ sẽ là 4 bản theo 4 ngày gần nhất.
{% endhint %}

### **Chỉnh sửa chính sách sao lưu** <a href="#tao-chinhsua-xoachinhsachsaoluu-chinhsuachinhsachsaoluu" id="tao-chinhsua-xoachinhsachsaoluu-chinhsuachinhsachsaoluu"></a>

Khi chính sách sao lưu không còn phù hợp với yêu cầu kinh doanh hay quy mô dữ liệu hoặc thời gian phục hồi được yêu cầu nhanh hơn bạn cần chỉnh sửa lại các thông số của chính sách sao lưu

**Quy trình chỉnh sửa chính sách sao lưu:**

1. Mở bảng điều khiển vBackup tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-policy](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-policy)
2. Tại thanh menu điều hướng, chọn Tab **Backup Policy**
3. Chọn **Chỉnh sửa Backup Policy**
4. Bạn có thể nhập lại tên chính sách, cũng như thay đổi tất cả các thông số về thời gian, múi giờ sao lưu, cũng như bộ lịch sao lưu, số bản lưu của Chính sách sao lưu mà bạn muốn cập nhật
5. Sau khi cập nhật xong chính sách hay chọn **Lưu** để thay đổi

### **Xóa chính sách sao lưu** <a href="#tao-chinhsua-xoachinhsachsaoluu-xoachinhsachsaoluu" id="tao-chinhsua-xoachinhsachsaoluu-xoachinhsachsaoluu"></a>

Bạn có thể xóa chính sách sao lưu nếu không còn nhu cầu sử dụng nó, nhưng cần lưu ý rằng, bạn không thể xóa chính sách sao lưu mặc định được tạo bởi hệ thống.

**Quy trình xóa chính sách sao lưu:**

1. Mở bảng điều khiển vBackup tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-policy](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-policy)
2. Tại thanh menu điều hướng, chọn Tab **Backup Policy**
3. Chọn **Xóa Backup Policy**
4. Sau khi xóa xong chính sách sao lưu sẽ mất khỏi trang danh sách

\


\
