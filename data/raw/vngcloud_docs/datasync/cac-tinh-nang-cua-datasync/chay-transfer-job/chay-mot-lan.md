# Chạy một lần

Trong hệ thống DataSync, chế độ chạy transfer job một lần tại một thời điểm được chỉ định trước (one-time scheduled transfer job) hoạt động theo cách sau:

**Bước 1: Xác định và cấu hình thời điểm Chạy Transfer Job**:

* Bạn cần xác định thời điểm cụ thể mà bạn muốn transfer job bắt đầu chạy. Thời điểm này có thể được cấu hình dưới dạng ngày giờ cụ thể với điều kiện lớn hơn thời điểm hiện tại (**current datetime**)

**Bước 2: Chạy Transfer Job:**

* Đến thời điểm đã chỉ định, hệ thống DataSync sẽ tự động kích hoạt transfer job và bắt đầu quá trình transfer dữ liệu từ nguồn đến đích theo các thông số đã cấu hình.

**Ví dụ**

Giả sử bạn muốn transfer dữ liệu từ một bucket trên cloud provider A sang một container trên vstorage vào lúc 3h sáng ngày 20 tháng 5 năm 2024. Quy trình sẽ như sau:

1. **Xác định thời điểm**: 3:00 AM, 20/05/2024.
2. **Cấu hình job**:

* **Chọn thời điểm chạy job**:&#x20;
  * Chọn phương án **Chạy một lần**
  * Chọn ngày 20/05/2024, nhập thời điểm 03:00.

Hệ thống sẽ tự động bắt đầu job vào lúc 3:00 AM, 20/05/2024.

{% hint style="info" %}
**Chú ý:**

* Nếu bạn thay đổi thông số ngày giờ chạy của một transfer job trong hệ thống DataSync, hệ thống sẽ chạy job theo thời gian mới mà bạn đã chỉ định. Cụ thể nếu bạn thay đổi ngày giờ thành:
  * **Thời Điểm Tương Lai**: Nếu thời điểm mới là trong tương lai, job sẽ được chạy vào đúng thời điểm đó mà không cần thêm bất kỳ hành động nào từ phía bạn.
  * **Thời Điểm Đã Qua**: Nếu bạn thay đổi thời gian chạy job sang một thời điểm đã qua, hệ thống có thể không tự động chạy job. Trong trường hợp này, bạn cần phải thiết lập lại thời gian sang một thời điểm hợp lý hoặc kích hoạt job thủ công.
{% endhint %}
