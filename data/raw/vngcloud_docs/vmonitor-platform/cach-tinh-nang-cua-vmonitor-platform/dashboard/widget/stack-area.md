# Stack area

### Tổng quan

**Stacked area** (biểu đồ xếp chồng) là một loại biểu đồ thể hiện sự thay đổi của một giá trị theo thời gian thông qua các vùng được xếp chồng lên nhau. Stacked area thường bao gồm nhiều vùng và mỗi vùng có một màu sắc khác nhau. Chiều cao xếp chồng của đường trên cùng sẽ tương ứng với tổng giá giá trị khi cộng lại của tất cả các nhóm được xếp chồng.

<figure><img src="../../../../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

***

### Cấu hình biểu đồ

<figure><img src="../../../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

#### 1. Choose graph style&#x20;

Đối với biểu đồ dạng stacked area, tại mục này bạn chọn Style là **Stacked area**

<figure><img src="../../../../.gitbook/assets/image (63).png" alt="" width="563"><figcaption></figcaption></figure>

#### 2. Graph your data

Chọn loại dữ liệu để vẽ Widget:

* Metrics: xem [Metric query](../query/metric-query.md) để cấu hình cho loại dữ liệu Metrics.
* Logs: xem [Log Query](../query/log-query.md) để cấu hình cho loại dữ liệu Logs.

Alias: Bạn có thể đặt Alias cho mỗi câu query, alias này sẽ được hiển thị trên graph và legend, điều này rất hữu ích cho những tên metric, logs hay những câu query có filter (bộ lọc) dài.&#x20;

#### 3. Fixed time range&#x20;

Khung thời gian cố định là một thuộc tính của Widget mà bạn có thể thiết lập để lọc dữ liệu trên Widget theo một khung thời gian cố định mà không phụ thuộc với khung thời gian (time range) của Dashboard. Mỗi Widget đều có thể thiết lập Fixed time range riêng biệt, bạn có thể chọn một trong các khung thời gian được mô tả ở bảng bên dưới. Ví dụ: nếu bạn chọn Global time thì khoảng thời gian lấy dữ liệu trên Widget được hiển thị sẽ được bằng khoảng thời gian mà bạn chọn trên Dashboard. Tức là khi thay đổi thời gian lấy dữ liệu trên Dashboard thì thời gian lấy dữ liệu của Widget sẽ thay đổi theo. Khuyến khích sử dụng lựa chọn này. Nếu bạn chọn Pass N minutes (N = 5,10,...) thì khoảng thời gian lấy dữ liệu trên Widget cố định (không thay đổi) luôn là 5, 10,...phút trước.&#x20;

#### 4. Configure graph

Ở mỗi loại biểu đồ Line, Bar, Stacked Area, Pie bạn cần chọn thuộc tính biểu đồ tương ứng. Các thuộc tính được chúng tôi mô tả ở bảng bên dưới:&#x20;

| **Parameter**     | **Options**                      |
| ----------------- | -------------------------------- |
| Graph legend      | Hidden, Top, Bottom, Left, Right |
| Connect nulls     | Enable, Disable                  |
| Y-axis lable      | Custom value                     |
| Y-axis scale type | Linear, Logarithmic              |
| Y-axis Max value  | Custom value                     |
| Y-axis Max value  | Custom value                     |

Chọn **Create** để tạo Widget, nếu có nhu cầu thay đổi tên widget thì bạn có thể thực hiện chỉnh sửa tại **Widget name**.
