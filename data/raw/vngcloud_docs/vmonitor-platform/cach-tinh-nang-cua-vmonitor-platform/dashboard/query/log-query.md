# Log query

Khi bạn tạo **Widget** cho dữ liệu **logs**, trong phần **Graph your data**, tạo câu lệnh truy vấn dữ liệu của bạn bằng cách chọn **Add a query**. Mỗi câu lệnh truy vấn sẽ được thể hiện bởi một line, bar, stacked area, pie, number, table hoặc một giao diện log search trên biểu đồ. Các thành phần tạo nên câu lệnh truy vấn đối với dữ liệu logs bao gồm:&#x20;

<figure><img src="../../../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

Trong đó:

### 1. Ẩn/ hiện query

Biểu tượng đánh dấu kết quả câu truy vấn đang được ẩn/ hiện trên biểu đồ. Để ẩn hiện kết quả câu truy vấn trên biểu đồ, bạn chỉ cần chọn vào biểu tượng này. Khi biểu tượng có màu xanh (giống a trong ảnh) tức là kết quả câu truy vấn đang được hiển thị trên biểu đồ. Khi biểu tượng có màu xám tức là kết quả câu truy vấn không được hiển thị trên biểu đồ.

### 2. Color

**Color**: chọn màu sắc cho biểu đồ vẽ trên kết quả câu truy vấn.

### 3. Loại query

**Loại query**: khung chọn loại dữ liệu. Để vẽ biểu đồ cho **logs** thì bạn cần chọn **Log** tại đây.&#x20;

### 4. Log project

**Log project**: lựa chọn **log project** bằng cách tìm kiếm và chọn từ danh sách log project. Danh sách **log project** này bạn có thể xem tại mục **Log/ Log project**, chi tiết tham khảo tại [Làm việc với Log Project](../../logs/lam-viec-voi-log-project/).

### 5. Search log

**Search log**: nơi bạn có thể thực hiện tìm kiếm dữ liệu logs theo điều kiện mà bạn mong muốn. Để biết cách search log, chi tiết tham khảo tại [Log search](../widget/log-search.md).

### 6. Alias

**Alias**: tên gợi nhớ dễ hiểu widget hơn. Hệ thống của chúng tôi sẽ tự động tạo Alias cho biểu đồ của bạn, nếu bạn muốn tự tạo Alias cho riêng mình, hãy chỉnh sửa trường thông tin này.

### 7. Statistics

**Statistics**: phép toán để tổng hợp dữ liệu. Có 7 cách tổng hợp mà bạn có thể sử dụng để kết hợp dữ liệu logs của mình trong mỗi nhóm thời gian: count, count unique, sum, avg, min, max, percentiles được mô tả ở bảng bên dưới:&#x20;

<table data-header-hidden><thead><tr><th width="210"></th><th></th></tr></thead><tbody><tr><td><strong>Phép toán</strong></td><td><strong>Ý nghĩa</strong></td></tr><tr><td>count</td><td>Đếm số lượng bản ghi logs sinh ra.</td></tr><tr><td>count unique</td><td>Đếm số lượng bản ghi logs duy nhất sinh ra dựa trên field được chọn</td></tr><tr><td>sum</td><td>Tổng các giá trị số của một field được chọn trên kết quả logs sinh ra.</td></tr><tr><td>min</td><td>Giá trị nhỏ nhất trong các giá trị số của một field được chọn trên kết quả logs sinh ra.</td></tr><tr><td>max</td><td>Giá trị lớn nhất trong các giá trị số của một field được chọn trên kết quả logs sinh ra.</td></tr><tr><td>percentiles</td><td>Tính phân vị cho một giá trị số của một field được chọn trên kết quả logs sinh ra.</td></tr></tbody></table>

### 8. Statistics field

**Field**: chọn trường thông tin muốn thực hiện phép toán. Đối với phép toán **Count** thì không cần chọn bất kì field nào. Đối với các phép toán còn lại, bạn phải chọn một field có kiểu dữ liệu là **Number** có trong log project để thực hiện phép toán trên giá trị đó.

### 9. Group by

**Group by**: bạn có thể nhóm dữ liệu theo các trường thông tin có trong log project.

### 10. Interval

**Interval**: thuộc tính để bạn xác định khoảng thời gian mà widget sẽ hiển thị giá trị (độ mọn dữ liệu). Bạn có thể chọn các giá trị Second, Minute, Day, v.v. từ các giá trị chúng tôi cung cấp sẵn hoặc bạn cũng có thể nhập trực tiếp giá trị Interval mà bạn mong muốn.

Bạn có thể thêm nhiều câu truy vấn vào một biểu đồ, chúng tôi hỗ trợ bạn tạo tối đa 10 câu truy vấn cho một biểu đồ. Nếu bạn có nhiều hơn 2 câu truy vấn trong một biểu đồ, hãy đảm bảo mỗi truy vấn được chọn một màu sắc riêng biệt và khoảng cách dữ liệu giữa các truy vấn không quá chênh lệch. Điều này sẽ giúp biểu đồ của bạn trở nên sinh động hơn.&#x20;

Bạn có thể tham khảo cách tạo một graph với logs dựa trên video bên dưới

<figure><img src="../../../../.gitbook/assets/1.gif" alt=""><figcaption></figcaption></figure>

\
