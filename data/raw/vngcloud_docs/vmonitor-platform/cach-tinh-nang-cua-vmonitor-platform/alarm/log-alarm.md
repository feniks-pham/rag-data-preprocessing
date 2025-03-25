# Log Alarm

Khi bạn tạo **Alarm** cho dữ liệu **logs**, trong phần **Set Alarm Conditions.** Các thành phần tạo nên câu lệnh truy vấn đối với dữ liệu logs bao gồm:&#x20;

<figure><img src="../../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

Trong đó

### 1. Log project

**Log project**: lựa chọn **log project** bằng cách tìm kiếm và chọn từ danh sách log project. Danh sách **log project** này bạn có thể xem tại mục **Log/ Log project**, chi tiết tham khảo tại [Làm việc với Log Project](../logs/lam-viec-voi-log-project/).

### 2. Save query

Save query: nơi bạn có thể chọn và tái sử dụng các query mà bạn đã tạo và lưu trước đó, chi tiết tham khảo tại [Variable, Save Querying and View](../dashboard/variable-save-querying-and-view.md).

### 3. Search log

**Search log**: nơi bạn có thể thực hiện tìm kiếm dữ liệu logs theo điều kiện mà bạn mong muốn. Để biết cách search log, chi tiết tham khảo tại [Log search](../dashboard/widget/log-search.md).

### 4. Statistics

**Statistics**: phép toán để tổng hợp dữ liệu.

* Đối với Alarm type loại Frequency và Flatline, chúng tôi hỗ trợ bạn sử dụng phép toán count - tức đếm số lượng bản ghi logs sinh ra.
* Đối với Alarm type loại logs Aggregation, chúng tôi hỗ trợ bạn sử dụng 1 trong 5 phép toán: count unique, sum, avg, min, max - để đếm số lượng bản ghi log duy nhất, tính tổng các giá trị, tính trung bình các giá trị, lấy giá trị nhỏ nhất, lấy giá trị lớn nhất của field logs được chọn.

### 5. Statistics field

**Field**: chọn trường thông tin muốn thực hiện phép toán.

* Đối với phép toán count thì bạn không cần chọn bất kì field nào.
* Đối với các phép toán count unique, sum, avg, min, max thì bạn cần chọn 1 field dữ liệu mà bạn muốn tổng hợp.

### 6. Alarm type

**Alarm type**: đối với logs, chúng tôi cung cấp cho bạn 2 lựa chọn là Frequency và Flatline

* Frequency: thoả mãn khi có ít nhất X event trong khoảng thời gian Y.
* Flatline: thoả mãn khi có ít hơn X event trong khoảng thời gian Y.
* logs Aggregation: giá trị của một chỉ số cụ thể của logs trong khung thời gian cao hơn hoặc thấp hơn ngưỡng.

### 7. Alarm condition

**Alarm condition:** điều kiện phép toán. **Alarm condition** sẽ đc điều chỉnh theo **Alarm type** lựa chọn:

* Đối với Alarm type Frequency thì condition sẽ là Greater (> ngưỡng).
* Đối với Alarm type Flatline thì condition sẽ là Lower (< ngưỡng).

### 8. Threshold value

**Threshold value**: giá trị ngưỡng mà bạn muốn đặt cảnh báo.&#x20;

### 9. Time frame

**Time frame**: khoảng thời gian mà dữ liệu sẽ được alarm đánh giá.
