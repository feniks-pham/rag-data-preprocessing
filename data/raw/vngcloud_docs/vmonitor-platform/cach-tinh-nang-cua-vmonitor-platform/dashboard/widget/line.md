# Line

### Tổng quan

**Line chart** (biểu đồ đường) là một loại biểu đồ được sử dụng để thể hiện thông tin dữ liệu thay đổi theo thời gian. Line chart được tạo bằng cách vẽ một loạt các điểm và nối chúng với nhau bằng các đoạn thẳng.

<figure><img src="../../../../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

***

### Cấu hình biểu đồ

<figure><img src="../../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 1. Choose graph style&#x20;

Đối với biểu đồ dạng line, tại mục này bạn chọn Style là **Line**

<figure><img src="../../../../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

Để thay đổi đường nét và độ mờ của line, bạn có thể điều chỉnh theo các option sau đây:

| **Parameter** | **Options**         |
| ------------- | ------------------- |
| Style         | Solid, Dot, Dash    |
| Stroke        | Normal, Thin, Thick |

#### 2. Graph your data

Chọn loại dữ liệu để vẽ Widget:

* Metrics: xem [Metric Query](../query/metric-query.md) để cấu hình cho loại dữ liệu Metrics.
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
