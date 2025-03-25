# Metric query

i bạn tạo **Widget** cho dữ liệu **metric**, trong phần **Graph your data**, tạo câu lệnh truy vấn dữ liệu của bạn bằng cách chọn **Add a query**. Mỗi câu lệnh truy vấn sẽ được thể hiện bởi một line, một stacked hoặc một number trên biểu đồ. Các thành phần tạo nên câu lệnh truy vấn đối với dữ liệu metric bao gồm:&#x20;

<figure><img src="../../../../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>

Trong đó:

#### 1. Ẩn/ hiện query

Biểu tượng đánh dấu kết quả câu truy vấn đang được ẩn/ hiện trên biểu đồ. Để ẩn hiện kết quả câu truy vấn trên biểu đồ, bạn chỉ cần chọn vào biểu tượng này. Khi biểu tượng có màu xanh (giống a trong ảnh) tức là kết quả câu truy vấn đang được hiển thị trên biểu đồ. Khi biểu tượng có màu xám tức là kết quả câu truy vấn không được hiển thị trên biểu đồ.

#### 2. Color

**Color**: chọn màu sắc cho biểu đồ vẽ trên kết quả câu truy vấn.

#### 3. Loại query

Loại query: khung chọn loại dữ liệu. Để vẽ biểu đồ cho metric thì bạn cần chọn Metric tại đây.

#### 4. Metric name

**Metric**: lựa chọn **metric** bằng cách tìm kiếm và chọn từ danh sách metric. Danh sách **metric** này bạn có thể xem tại mục **Metric Information**, chi tiết tham khảo tại [Làm việc với Metric Information](../../metrics/lam-viec-voi-metruc-information.md).

#### 5. Filter

**Filter**: metric mà bạn lựa chọn có thể được filter bởi các **dimensions** (ví dụ host,device,...) từ danh sách **dimensions** được hiển thị, bạn có thể chọn nhiều **dimensions** tại đây. Ngoài việc chọn các dimensions có giá trị cố định của metric, tại đây bạn có thể sử dụng các **variable** để filter linh động hơn. Các **variable** này đã được bạn định nghĩa tại **Dashboard** mà bạn đang muốn tạo **Widget**. Để tìm hiểu thêm về **variable**, vui lòng tham khảo tại [Variable, Save Querying and View](../variable-save-querying-and-view.md). Ví dụ như ảnh bên dưới, chúng tôi chọn metric win\_swap.Percent\_Usage và chọn điều kiện lọc theo 2 dimension bao gồm: host = ThuyVT2-PC và objectname = Paging\_File.&#x20;

<figure><img src="../../../../.gitbook/assets/2.gif" alt=""><figcaption></figcaption></figure>

#### 6. Statistics

**Statistics**: phép toán để tổng hợp dữ liệu. Hệ thống vMonitor Platform lưu trữ một lượng lớn điểm dữ liệu và trong hầu hết các trường hợp đều không thể hiển thị tất cả chúng trên biểu đồ do đó chúng tôi sử dụng tính năng tổng hợp dữ liệu theo thời gian để giải quyết vấn đề này bằng cách kết hợp các điểm dữ liệu vào các nhóm thời gian, gọi là độ mịn dữ liệu. Độ mịn dữ liệu được chúng tôi tự động tính toán dựa trên time range mà bạn chọn, quy tắt tự động tính toán như bên dưới ( hoặc page). Có 5 cách tổng hợp mà bạn có thể sử dụng để kết hợp dữ liệu của mình trong mỗi nhóm thời gian: avg, count, max, min, sum được mô tả ở bảng bên dưới:&#x20;

<table data-header-hidden><thead><tr><th width="135"></th><th width="183"></th><th></th></tr></thead><tbody><tr><td><strong>Phép toán</strong></td><td><strong>Ý nghĩa</strong></td><td><strong>Ví dụ minh họa</strong></td></tr><tr><td>avg</td><td>Giá trị trung bình của kết quả metric sinh ra.</td><td><p>Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới:</p><ul><li>01-01-2023 07:00:00 value = 1</li><li>01-01-2023 07:00:30 value = 2</li><li>01-01-2023 07:01:00 value = 1</li><li>01-01-2023 07:01:30 value = 3</li></ul><p>Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán avg là:</p><ul><li>01-01-2023 07:01:00 value = 1.5</li><li>01-01-2023 07:02:00 value = 2</li></ul></td></tr><tr><td>count</td><td>Đếm số lượng kết quả metric sinh ra.</td><td><p>Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới:</p><ul><li>01-01-2023 07:00:00 value = 1</li><li>01-01-2023 07:00:30 value = 2</li><li>01-01-2023 07:01:00 value = 1</li><li>01-01-2023 07:01:30 value = 3</li></ul><p>Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán count là:</p><ul><li>01-01-2023 07:01:00 value = 2</li><li>01-01-2023 07:02:00 value = 2</li></ul></td></tr><tr><td>max</td><td>Giá trị lớn nhất của kết quả metric sinh ra.</td><td><p>Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới:</p><ul><li>01-01-2023 07:00:00 value = 1</li><li>01-01-2023 07:00:30 value = 2</li><li>01-01-2023 07:01:00 value = 1</li><li>01-01-2023 07:01:30 value = 3</li></ul><p>Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán max là:</p><ul><li>01-01-2023 07:01:00 value = 2</li><li>01-01-2023 07:02:00 value = 3</li></ul></td></tr><tr><td>min</td><td>Giá trị nhỏ nhất của kết quả metric sinh ra.</td><td><p>Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới:</p><ul><li>01-01-2023 07:00:00 value = 1</li><li>01-01-2023 07:00:30 value = 2</li><li>01-01-2023 07:01:00 value = 1</li><li>01-01-2023 07:01:30 value = 3</li></ul><p>Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán min là:</p><ul><li>01-01-2023 07:01:00 value = 1</li><li>01-01-2023 07:02:00 value = 1</li></ul></td></tr><tr><td>sum</td><td>Tổng các giá trị của kết quả metric sinh ra.</td><td><p>Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới:</p><ul><li>01-01-2023 07:00:00 value = 1</li><li>01-01-2023 07:00:30 value = 2</li><li>01-01-2023 07:01:00 value = 1</li><li>01-01-2023 07:01:30 value = 3</li></ul><p>Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán sum là:</p><ul><li>01-01-2023 07:01:00 value = 3</li><li>01-01-2023 07:02:00 value = 4</li></ul></td></tr></tbody></table>

#### 7. Group by

**Group by**: bạn có thể nhóm dữ liệu theo các dimension tương ứng của metric. Ví dụ khi bạn chọn dimension host, nếu metric của bạn đang có 5 hosts khác nhau, hệ thống sẽ tự động vẽ ra 5 dòng tương ứng với 5 hosts trên Widget.

#### 8. Limit to

**Limit to**: giới hạn số series hiển thị trên biểu đồ theo nhóm Top hoặc Bottom. Ví dụ khi bạn sử dụng tính năng group by nếu Metric của bạn đang có 10 hosts khác nhau, hệ thống sẽ tự động vẽ ra 10 dòng tương ứng với 10 hosts trên widget. Nếu bạn tiếp tục sử dụng Top 5, hệ thống chỉ vẽ ra 5 dòng có điểm dữ liệu lớn nhất trong thời điểm đó.&#x20;

#### 9. Alias

**Alias**: tên gợi nhớ dễ hiểu widget hơn. Nếu bạn không nhập Alias, chúng tôi tự động sinh ra tên query là **Statistic:metricname(dimension)**. Khi có thêm timeshift 5 phút thì Alias sẽ là **timeshift(statistic:metricname{dimension}, 5 minutes)**. Khi bạn có chọn group by thì Alias chỉ hiện thị dimension thôi, ví dụ bạn có một query với điều kiện group by cpu, thì Alias sẽ là cpu0, cpu1,...

Bạn có thể tham khảo cách tạo một graph với metric dựa trên video bên dưới

<figure><img src="../../../../.gitbook/assets/3 (1).gif" alt=""><figcaption></figcaption></figure>
