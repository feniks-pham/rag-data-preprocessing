# Làm việc với Log2metric

### Tổng quan <a href="#lamviecvoilog2metric-tongquan" id="lamviecvoilog2metric-tongquan"></a>

Log2metric là một tính năng cho phép bạn tạo metric theo thời gian thực từ logs. Cách tiếp cận này giúp bạn tối ưu hóa việc lưu trữ log mà không phải hy sinh bất kỳ dữ liệu quan trọng nào. Vì vậy, chi phí của bạn sẽ được giảm.\
Bạn có thể bắt đầu sử dụng tính năng log2metric bằng cách thiết lập một truy vấn đơn giản và chúng tôi sẽ đánh giá giá trị sau mỗi <mark style="color:red;">**60**</mark> giây. Ví dụ: bạn muốn đếm số lượng dòng logs có trạng thái lỗi hoặc bạn muốn biết thời gian phản hồi yêu cầu trung bình trong logs của máy chủ web, chỉ cần sử dụng Log2metric. Các metric đầu ra này tương tự như các metric khác, bạn có thể sử dụng để vẽ dashboard và tạo alarm.

***

### Phạm vi giới hạn Log2metric <a href="#lamviecvoilog2metric-phamvigioihanlog2metric" id="lamviecvoilog2metric-phamvigioihanlog2metric"></a>

#### Quy tắc đặt tên Metric name: <a href="#lamviecvoilog2metric-quytacdattenmetricname" id="lamviecvoilog2metric-quytacdattenmetricname"></a>

Các quy tắc sau áp dụng cho việc đặt tên metric trong vStorage:

* Tên metric phải dài từ 3 (tối thiểu) đến 50 (tối đa) ký tự.
* Tên metric phải có ký tự đầu là kiểu alphanumerics (a-z, A-Z) hoặc dấu underscores (\_). Các ký tự tiếp theo là kiểu alphanumerics (a-z, 0-9), dấu underscores (\_), dấu minuses (-), dấu periods (.) hoặc dấu slashes ( / ).
* Tên metric không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...).
* Tên metric phải là duy nhất trên một tài khoản VNG Cloud cho đến khi metric đó bị xóa.&#x20;

#### Ví dụ minh họa <a href="#lamviecvoilog2metric-viduminhhoa" id="lamviecvoilog2metric-viduminhhoa"></a>

* Các tên metric ví dụ sau đây hợp lệ và tuân theo các nguyên tắc đặt tên được đề xuất:
  * cpu.time\_system
  * mem.active
  * disk.free
  * ...

***

### Khởi tạo metric <a href="#lamviecvoilog2metric-khoitaometric" id="lamviecvoilog2metric-khoitaometric"></a>

Để khởi tạo một metric từ log của bạn, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor/).
2. Chọn thư mục **Log**, sau đó chọn menu **Log2metric**.
3. Chọn **Create a Metric**.
4. Nhập **Metric name**. Tên metric phải tuân thủ theo quy định của chúng tôi, chi tiết được mô tả bên trên.
5. Tạo **Query Definition** bằng cách:&#x20;
   * Tìm kiếm và chọn một **Log** **Project** bạn muốn thực hiện chuyển đổi log qua metric. Màn hình sẽ hiển thị các log ở **Log project** trong vòng 15 phút để bạn xem trước.
   * Tạo **Log Filter** tìm kiếm log, chọn phép toán (**Operator**), chọn điều kiện nhóm dữ liệu (**Group by**), chi tiết tham khảo tại [Search logs](lam-viec-voi-log-search/search-logs.md).
6. Chọn **Advanced query** nếu bạn mong muốn thiết lập nâng cao cho metric bao gồm: **Event timestamp field, Event timestamp format, Default metric value** trong đó:&#x20;
   * Chọn **Event timestamp field**: field này dùng để đọc thời điểm **event** xảy ra, nếu bạn không chọn thì chúng tôi sẽ lấy thời điểm **processing time**.
   * Chọn **Event timestamp format**: nếu bạn đã chọn **Event timestamp field** trước đó thì field này dùng để định dạng thời gian tương ứng của **Event timestamp field**. Nếu bạn chọn **Event timestamp format** không đúng với loại dữ liệu của **Event timestamp field** thì kết quả **metric** có thể sẽ không đúng.
   * Nhập **Default metric value**: nhập giá trị mặc định của **metric** nếu không có dữ liệu tính toán dựa trên các điều kiện đã nhập phía trên. Bạn có thể nhập số thực từ 0 tới 100.000.000.000.000.

6\. Chọn **Tạo mới**. **Metric** được tạo ra với metric name và **log** dựa trên điều kiện tạo mới mà bạn đã chọn/ nhập. Khi trạng thái của log2metric là **ACTIVE**, lúc này bạn có thể tiếp tục sử dụng **metric** tạo ra này tại [Dashboard](../dashboard/) và [Metric Alarm](../alarm/metric-alarm.md).

Các **điểm dữ liệu** cho Log2metric vừa tạo được định kỳ tạo ra trong khoảng thời gian 60&#x73;**.** Bạn có thể tạo nhiều **metric** cho một **log project** với các **metric name** khác nhau. Trong lần đầu tiên khởi tạo metric từ log, tiến trình khởi tạo có thể sẽ mất một chút thời gian do chúng tôi cần thiết lập nhiều cấu hình cần thiết. Đừng lo lắng vì từ các lần khởi tạo metric tiếp theo, tiến trình này sẽ nhanh hơn rất nhiều.

***

### Chỉnh sửa metric <a href="#lamviecvoilog2metric-chinhsuametric" id="lamviecvoilog2metric-chinhsuametric"></a>

Để chỉnh sửa metric đã được tạo từ logs trước đó, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào vMonitor Platform [tại đây.](https://hcm-3.console.vngcloud.vn/vmonitor)&#x20;
2. Chọn thư mục **Log**, sau đó chọn menu **Log2metric**.
3. Tại **Metric** mà bạn muốn chỉnh sửa, chọn **Edit**.
4. Chỉnh sửa các thông số cho biểu đồ mà bạn mong muốn. Các thông số mà bạn có thể chỉnh sửa bao gồm: **Log filter, Advanced query**. Việc chỉnh sửa này tương tự như khi bạn thực hiện tạo mới một Widget.
5. Chọn **Save.**

***

### Xóa metric <a href="#lamviecvoilog2metric-xoametric" id="lamviecvoilog2metric-xoametric"></a>

Bạn đã khởi tạo một metric từ một log project tương ứng. Metric này đã được bạn sử dụng tại vMonitor Dashboard, vMonitor Alarm. Hiện tại bạn không có nhu cầu sử dụng metric này. Chúng tôi khuyến khích bạn nên xóa metric này để tối ưu chi phí cho Metric quota.

Để xóa một project, bạn hãy làm theo hướng dẫn:&#x20;

1\. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor/).

2\. Chọn thư mục **Log**, sau đó chọn menu **Log2metric**.

3\. Trong danh sách **metric** đang tồn tại, chọn <img src="../../../.gitbook/assets/image (331).png" alt="" data-size="line">  tại **metric** muốn thực hiện xóa sau đó chọn **Delete**.

4\. Chọn **Delete**.

Sau khi bạn thực hiện 4 bước bên trên để xóa metric thì chúng tôi bắt đầu chạy tiến trình xóa metric của bạn. Trạng thái của metric lúc này là Đang xóa. Tại thời điểm này, metric vẫn chưa được cập nhật xóa ở vMonitor Dashboard cũng như vMonitor Alarm. Tới thời điểm chúng tôi thông báo cho bạn metric đã xóa thành công, thì lúc này metric sẽ bị xóa ở phía Log2Metric nhưng metric name đó vẫn tồn tại phía hệ thống vMonitor Platform - Metric. Do đó nếu Widget đang sử dụng metric bị xóa thì biểu đồ được vẽ từ metric sẽ không có dữ liệu mới (biểu đồ vẫn giữ nguyên hiện trạng, tính năng và dữ liệu cũ trước thời điểm xóa metric) và bạn vẫn có thể thêm mới Widget khác với metric đã bị xóa này.

\
