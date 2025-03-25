# Gói Bandwidth Pay As You Go

Gói bandwidth Pay As You Go là gói bandwidth mà bạn cần chi trả tiền cho lượng lượng băng thông sử dụng vượt quá gói băng thông miễn phí (VNG Dedicated). Gói Pay As You Go này sẽ bao gồm 3 gói cụ thể:

* **PAYG-ALL**: Gói này cho phép bạn sử dụng băng thông không giới hạn cho cả lưu lượng trong nước và quốc tế. Bạn sẽ trả tiền cho tổng lượng băng thông sử dụng vượt quá mức miễn phí, bất kể lưu lượng đó là trong nước hay quốc tế.
* **PAYG-DOMESTIC**: Gói này sẽ áp dụng cho băng thông sử dụng trong nước. Bạn sẽ trả tiền cho lượng băng thông sử dụng vượt quá mức miễn phí dành riêng cho lưu lượng **nội địa**. Tại gói này, lưu lượng **quốc tế sẽ theo cấu hình gói mặc định.**
* **PAYG-INTERNATIONAL**: Gói này sẽ áp dụng cho băng thông sử dụng quốc tế. Bạn sẽ trả tiền cho lượng băng thông sử dụng vượt quá mức miễn phí dành riêng cho lưu lượng quốc tế. Tại gói này, lưu lượng **trong nước sẽ theo cấu hình gói mặc định.**

### Xem thông tin chi tiết gói

**Bước 1**: Đăng nhập vào tài khoản VNG Cloud của bạn và truy cập vào [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)

**Bước 2**: Trên danh sách menu bên trái, tại mục **Network**, chọn **Bandwidth**.

**Bước 3**: Trên danh sách các gói bandwidth có sẵn, chọn vào gói **Pay As You Go.**

**Bước 4**: Lúc này, bạn có thể xem chi tiết gói bandwidth này. Tại màn hình này, bạn có thể:

* Thêm IP cho gói: bằng cách chọn vào biểu tượng **Thêm IP**, bạn có thể lựa chọn IP mà bạn muốn thêm vào gói bandwidth này. Chi tiết bạn có thể tham khảo ở mục bên dưới.
* Thêm tag cho gói: bằng cách nhập **Key, Value** và chọn biểu tượng **Thêm**, bạn có thể thêm tag đánh dầu cho gói bandwidth này.

{% hint style="info" %}
**Chú ý:**

* Đây là gói bandwidth mặc định được chúng tôi tự động tạo và thêm sẵn vào gói dịch vụ cho bạn, bạn không thể thực hiện xóa gói này hoặc thay đổi cấu hình gói này.
{% endhint %}

***

### Thêm địa chỉ IP cho gói

{% hint style="info" %}
**Chú ý:**

* Các IP có trạng thái ATTACHED có ý nghĩa là các IP này đã được gán vào 1 gói bandwidth bất kỳ nào đó. Khi bạn thực hiện thêm các IP có trạng thái ATTACHED này vào gói bandwidth của bạn, các IP này sẽ được gỡ khỏi gói cũ và gán lại vào gói mới này. **Điều này nhằm đảm bảo tại một thời điểm, một địa chỉ IP chỉ có thể được gán vào một gói bandwidth.**
{% endhint %}

Để thêm địa chỉ IP cho gói, bạn có thể thực hiện theo các bước:&#x20;

**Bước 1**: Đăng nhập vào tài khoản VNG Cloud của bạn và truy cập vào [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)

**Bước 2**: Trên danh sách menu bên trái, tại mục **Network**, chọn **Bandwidth**.

**Bước 3**: Trên danh sách các gói bandwidth có sẵn, chọn vào gói **PAYG-ALL, PAYG-DOMESTIC, PAYG-INTERNATIONAL** tùy theo nhu cầu sử dụng của bạn.

**Bước 4**: Chọn biểu tượng <img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">sau đó chọn **Thêm IP** hoặc ở màn hình chi tiết gói, tại mục **Danh sách IP**, chọn biểu tượng **Thêm IP.**&#x20;

**Bước 5:** Màn hình **Thêm IP** được hiển thị, bạn có thể lọc danh sách IP theo từng loại bằng cách chọn một trong các phương án tại ô **Loại resource**. Hiện tại chúng tôi đang cung cấp cho bạn các loại resource bao gồm: **K8S, Floating IP, External Interface, vLB.**

**Bước 6**: Chọn một hoặc nhiều IP bằng cách chọn biểu tượng <img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">và chọn **Thêm**. tượng **Thêm IP.**&#x20;

***

### Bỏ chọn địa chỉ IP cho gói

Để thêm địa chỉ IP cho gói, bạn có thể thực hiện theo các bước:&#x20;

**Bước 1**: Đăng nhập vào tài khoản VNG Cloud của bạn và truy cập vào [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)

**Bước 2**: Trên danh sách menu bên trái, tại mục **Network**, chọn **Bandwidth**.

**Bước 3**: Trên danh sách các gói bandwidth có sẵn, chọn vào gói **PAYG-ALL, PAYG-DOMESTIC, PAYG-INTERNATIONAL** tùy theo nhu cầu sử dụng của bạn.

**Bước 4**: Tại mục **Danh sách IP**, chọn biểu tượng <img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">tại địa chỉ IP bạn muốn bỏ khỏi gói và chọn biểu tượng <img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">.

**Bước 5:** Tại màn hình xác nhận xóa IP, chọn **Xóa**.

{% hint style="info" %}
**Chú ý:**

* Khi bạn xóa một địa chỉ IP khỏi gói Pay As You Go, địa chỉ IP này sẽ được gán lại vào gói bandwidth mặc định miễn phí **VNG Dedicated**.
{% endhint %}
