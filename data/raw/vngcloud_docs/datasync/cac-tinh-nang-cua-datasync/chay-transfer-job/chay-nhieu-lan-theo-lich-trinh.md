# Chạy nhiều lần theo lịch trình

Trong hệ thống DataSync, cơ chế chạy lập lịch định kỳ cho các transfer job theo ngày, tuần, hoặc tháng giúp tự động hóa và đảm bảo các tác vụ transfer dữ liệu được thực hiện đều đặn theo một chu kỳ nhất định. Dưới đây là cách hoạt động của các chế độ lập lịch định kỳ này:

**Bước 1: Xác định và cấu hình thời điểm Chạy Transfer Job**:

* Bạn cần xác định thời điểm cụ thể mà bạn muốn transfer job bắt đầu chạy. Thời điểm này có thể được cấu hình dưới dạng ngày giờ cụ thể với điều kiện lớn hơn thời điểm hiện tại (**current datetime**)

**Bước 2: Chạy Transfer Job:**

* Đến thời điểm đã chỉ định, hệ thống DataSync sẽ tự động kích hoạt transfer job và bắt đầu quá trình transfer dữ liệu từ nguồn đến đích theo các thông số đã cấu hình.

### Lập lịch chạy định kỳ theo Ngày

* Transfer job sẽ chạy vào một thời điểm cụ thể hàng ngày.

**Ví dụ**

Giả sử bạn muốn thiết lập một transfer job thực hiện transfer dữ liệu từ một bucket trên cloud provider A tới container B trên vStorage theo chu kỳ hằng ngày bắt đầu từ 01/05/2024 tới 30/05/2024 vào lúc 03:00. Quy trình sẽ như sau:

1. **Xác định thời điểm**: 3:00 AM, từ ngày 01/05/2025 tới 30/05/2024.
2. **Cấu hình job**:

* **Chọn thời điểm chạy job**:
  * Chọn phương án **Chạy lập lịch**
  * Chu kỳ **Daily**
  * Chọn **Ngày bắt đầu** là 01/05/2024, nhập thời điểm 03:00.
  * Chọn **Ngày kết thúc** là 30/05/2024

3. Hằng ngày tính từ 01/05/2024, vào lúc 03:00 hệ thống sẽ thực hiện chạy transfer job của bạn.

{% hint style="info" %}
**Chú ý:**

Nếu bạn thay đổi chu kỳ chạy của một transfer job trong hệ thống DataSync, thì:

* Thời điểm chạy kế tiếp (next run time) sẽ không thay đổi khi bạn thực hiện cập nhật.
* Sau khi lần chạy kế tiếp này đã thực hiện, thì lần chạy kế tiếp sẽ dựa theo chu kỳ mới mà bạn chỉnh sửa cho transfer job của bạn.

**Ví dụ:**

* Hiện tại, bạn đang thiết lập chạy transfer job với các thông số:
  * Ngày bắt đầu: 01/05/2024 , 03:00
  * Ngày kết thúc: 30/05/2024
  * Chu kỳ: Daily

\=> tính tới thời điểm hiện tại trước khi chỉnh sửa, lần run transfer job kế tiếp sẽ là vào lúc **22/05/2024 03:00**

* Giả sử, bạn thực hiện thay đổi thông tin này vào ngày 21/05/2024 với thông số như sau:
  * Ngày bắt đầu: 01/05/2024 , 03:00
  * Ngày kết thúc: 30/05/2024
  * Chu kỳ: Weekly

\=> Lúc này, thời điểm chạy kế tiếp vẫn sẽ là **22/05/2024 03:00**

\=> Sau lần chạy này, lần chạy kế tiếp sẽ được tính theo chu kỳ mới là **22/05/2024 03:00 + 7 ngày = 29/05/2024 03:00**
{% endhint %}

### **Lập lịch chạy định kỳ theo Tuần**

* Transfer job sẽ chạy định kỳ 7 ngày một lần.

**Ví dụ**

Giả sử bạn muốn thiết lập một transfer job thực hiện transfer dữ liệu từ một bucket trên cloud provider A tới container B trên vStorage theo chu kỳ 7 ngày 1 lần bắt đầu từ 01/05/2024 tới 30/05/2024 vào lúc 03:00. Quy trình sẽ như sau:

1. **Xác định thời điểm**: 3:00 AM, từ ngày 01/05/2025 tới 30/05/2024.
2. **Cấu hình job**:

* **Chọn thời điểm chạy job**:
  * Chọn phương án **Chạy lập lịch**
  * Chu kỳ **Weekly**
  * Chọn **Ngày bắt đầu** là 01/05/2024, nhập thời điểm 03:00.
  * Chọn **Ngày kết thúc** là 30/05/2024

3. Vào các ngày 01/05/2024, 08/05/2024, 15/05/2024, 22/05/2024, 29/05/2024 lúc 03:00 hệ thống sẽ thực hiện chạy transfer job của bạn.

{% hint style="info" %}
**Chú ý:**

Nếu bạn thay đổi chu kỳ chạy của một transfer job trong hệ thống DataSync, thì:

* Thời điểm chạy kế tiếp (next run time) sẽ không thay đổi khi bạn thực hiện cập nhật.
* Sau khi lần chạy kế tiếp này đã thực hiện, thì lần chạy kế tiếp sẽ dựa theo chu kỳ mới mà bạn chỉnh sửa cho transfer job của bạn.

**Ví dụ:**

* Hiện tại: bạn đang thiết lập chạy transfer job với các thông số:
  * Ngày bắt đầu: 01/05/2024 , 03:00
  * Ngày kết thúc: 30/05/2024
  * Chu kỳ: Weekly

\=> tính tới thời điểm hiện tại trước khi chỉnh sửa, lần run transfer job kế tiếp sẽ là vào lúc  **22/05/2024 03:00**

* Giả sử, bạn thực hiện thay đổi thông tin này vào ngày 21/05/2024 với thông số như sau:
  * Ngày bắt đầu: 01/05/2024 , 03:00
  * Ngày kết thúc: 30/05/2024
  * Chu kỳ: Daily

\=> Lúc này, thời điểm chạy kế tiếp vẫn sẽ là **22/05/2024 03:00**

\=> Sau lần chạy này, lần chạy kế tiếp sẽ được tính theo chu kỳ mới là **22/05/2024 03:00 + 1 ngày = 23/05/2024 03:00**
{% endhint %}

### **Lập lịch chạy định kỳ theo Tháng**

* Transfer job sẽ chạy định kỳ 1 tháng một lần.

**Ví dụ**

Giả sử bạn muốn thiết lập một transfer job thực hiện transfer dữ liệu từ một bucket trên cloud provider A tới container B trên vStorage theo chu kỳ 1 tháng 1 lần bắt đầu từ 01/01/2024 tới 30/06/2024 vào lúc 03:00. Quy trình sẽ như sau:

1. **Xác định thời điểm**: 3:00 AM, từ ngày 01/01/2025 tới 30/06/2024.
2. **Cấu hình job**:

* **Chọn thời điểm chạy job**:
  * Chọn phương án **Chạy lập lịch**
  * Chu kỳ **Monthly**
  * Chọn **Ngày bắt đầu** là 01/01/2024, nhập thời điểm 03:00.
  * Chọn **Ngày kết thúc** là 30/06/2024

3. Vào các ngày 01/01/2024, 01/02/2024, 01/03/2024, 01/04/2024, 01/05/2024, 01/06/2024 lúc 03:00 hệ thống sẽ thực hiện chạy transfer job của bạn.

{% hint style="info" %}
**Chú ý:**

Nếu bạn thay đổi chu kỳ chạy của một transfer job trong hệ thống DataSync, thì:

* Thời điểm chạy kế tiếp (next run time) sẽ không thay đổi khi bạn thực hiện cập nhật.
* Sau khi lần chạy kế tiếp này đã thực hiện, thì lần chạy kế tiếp sẽ dựa theo chu kỳ mới mà bạn chỉnh sửa cho transfer job của bạn.

**Ví dụ:**

* Hiện tại: bạn đang thiết lập chạy transfer job với các thông số:
  * Ngày bắt đầu: 01/05/2024 , 03:00
  * Ngày kết thúc: 30/06/2024
  * Chu kỳ: Monthly

\=> tính tới thời điểm hiện tại trước khi chỉnh sửa, lần run transfer job kế tiếp sẽ là vào lúc  **01/06/2024 03:00**

* Giả sử, bạn thực hiện thay đổi thông tin này vào ngày 21/05/2024 với thông số như sau:
  * Ngày bắt đầu: 01/05/2024 , 03:00
  * Ngày kết thúc: 30/06/2024
  * Chu kỳ: Weekly

\=> Lúc này, thời điểm chạy kế tiếp vẫn sẽ là **01/06/2024 03:00**

\=> Sau lần chạy này, lần chạy kế tiếp sẽ được tính theo chu kỳ mới là **01/06/2024 03:00 + 7 ngày = 08/06/2024 03:00**
{% endhint %}
