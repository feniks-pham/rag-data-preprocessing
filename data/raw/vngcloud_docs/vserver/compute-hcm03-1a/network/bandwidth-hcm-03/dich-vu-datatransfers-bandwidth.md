# Gói Bandwidth VNG Dedicated

Gói bandwidth VNG Dedicated là gói bandwidth miễn phí mặc định với tốc độ tiêu chuẩn dành cho tất cả khách hàng. Ở gói này, chúng tôi sẽ cung cấp cho bạn băng thông trong nước lên tới 300Mbps và băng thông quốc tế lên tới 5Mbps. **Mặc định, tất cả IP của bạn sẽ được áp dụng tiêu chuẩn bandwidth của gói này.**&#x20;

### Xem thông tin chi tiết gói

**Bước 1**: Đăng nhập vào tài khoản VNG Cloud của bạn và truy cập vào [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)

**Bước 2**: Trên danh sách menu bên trái, tại mục **Network**, chọn **Bandwidth**.

**Bước 3**: Trên danh sách các gói bandwidth có sẵn, chọn vào gói **VNG Dedicated.**

**Bước 4**: Lúc này, bạn có thể xem chi tiết gói bandwidth này. Tại màn hình này, bạn có thể:

* Thêm IP cho gói: bằng cách chọn vào biểu tượng **Thêm IP**, bạn có thể lựa chọn IP mà bạn muốn thêm vào gói bandwidth này. Chi tiết bạn có thể tham khảo ở mục bên dưới.
* Thêm tag cho gói: bằng cách nhập **Key, Value** và chọn biểu tượng **Thêm**, bạn có thể thêm tag đánh dầu cho gói bandwidth này.

{% hint style="info" %}
**Chú ý:**

* Đây là gói bandwidth mặc định được chúng tôi tự động tạo và thêm sẵn vào gói dịch vụ cho bạn, bạn không thể thực hiện xóa gói này hoặc thay đổi cấu hình gói này.
* Kể từ thời điểm bạn tạo một resource mới, khoảng sau 1 phút thì các địa chỉ IP này sẽ tự động được gán vào gói bandwidth **VNG Dedicated.**&#x20;
{% endhint %}

***

### Thêm địa chỉ IP cho gói

{% hint style="info" %}
**Chú ý:**&#x20;

* Bạn chỉ có thể thêm các IP vào gói bandwidth này nhưng bạn không thể thực hiện xóa các IP có bandwidth mặc định.
* Các IP có trạng thái ATTACHED có ý nghĩa là các IP này đã được gán vào 1 gói bandwidth bất kỳ nào đó. Khi bạn thực hiện thêm các IP có trạng thái ATTACHED này vào gói bandwidth của bạn, các IP này sẽ được gỡ khỏi gói cũ và gán lại vào gói mới này. **Điều này nhằm đảm bảo tại một thời điểm, một địa chỉ IP chỉ có thể được gán vào một gói bandwidth.**
{% endhint %}

Để thêm địa chỉ IP cho gói, bạn có thể thực hiện theo các bước:&#x20;

**Bước 1**: Đăng nhập vào tài khoản VNG Cloud của bạn và truy cập vào [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)

**Bước 2**: Trên danh sách menu bên trái, tại mục **Network**, chọn **Bandwidth**.

**Bước 3**: Trên danh sách các gói bandwidth có sẵn, chọn vào gói **VNG Dedicated.**

**Bước 4**: Chọn biểu tượng <img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">sau đó chọn Thêm IP hoặc ở màn hình chi tiết gói, tại mục **Danh sách IP**, chọn biểu tượng **Thêm IP.**&#x20;

**Bước 5:** Màn hình **Thêm IP** được hiển thị, bạn có thể lọc danh sách IP theo từng loại bằng cách chọn một trong các phương án tại ô **Loại resource**. Hiện tại chúng tôi đang cung cấp cho bạn các loại resource bao gồm: **K8S, Floating IP, External Interface, vLB.**

**Bước 6**: Chọn một hoặc nhiều IP bằng cách chọn biểu tượng <img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">và chọn **Thêm**.&#x20;
