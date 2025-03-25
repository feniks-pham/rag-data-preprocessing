# Giám sát DataSync thông qua Metric

#### Metric là gì? <a href="#giamsatdatasyncthongquametric-metriclagi" id="giamsatdatasyncthongquametric-metriclagi"></a>

Metric (hay được gọi là chỉ số) là các điểm dữ liệu chúng ta thu được nhờ vào việc đo lường, bằng cách thiết lập các phép đo đạc, theo dõi, đánh giá hoạt động nào đó trong ngữ cảnh.

***

#### Tại sao metric lại hữu ích? <a href="#giamsatdatasyncthongquametric-taisaometriclaihuuich" id="giamsatdatasyncthongquametric-taisaometriclaihuuich"></a>

Metric cung cấp một bức tranh tổng thể về hệ thống của bạn. Bạn có thể sử dụng chúng để đánh giá tình trạng hệ thống của bạn ngay tại thời điểm hiện tại. Đối với DataSync, metric có thể giúp bạn điều chỉnh quy mô lưu trữ, khả năng đáp ứng từ đó bạn có thể điều chỉnh nhu cầu cùng như xác định chính xác lượng tài nguyên bạn cần tiêu thụ để có thể giúp bạn tiết kiệm tiền hoặc cải thiện hiệu suất.

***

#### Giám sát DataSync thông qua DataSync metric trên hệ thống vMonitor Platform <a href="#giamsatdatasyncthongquametric-giamsatdatasyncthongquadatasyncmetrictrenhethongvmonitorplatform" id="giamsatdatasyncthongquametric-giamsatdatasyncthongquadatasyncmetrictrenhethongvmonitorplatform"></a>

Giám sát DataSync thông qua metric thật dễ dàng khi bạn sử dụng hệ thống vMonitor Platform. Chúng tôi đã chuyển các thông số metric từ DataSync qua vMonitor Platform đều đặn theo chu kỳ 5 phút. Hãy yên tâm là vMonitor Platform cũng là một sản phẩm thuộc hệ sinh thái của VNG Cloud. Bạn có thể sử dụng vMonitor Platform để cấu hình các tính năng giám sát dựa trên các thông số này. Dĩ nhiên để có thể thực hiện giám sát được thì bạn cần mua gói metric quota của dịch vụ vMonitor Platform. Chi tiết bạn có thể tham khảo tại [vMonitor Platform](../../vmonitor/). Dưới đây là danh sách DataSync metric mà chúng tôi đã cung cấp cho mục đích giám sát:

<table data-header-hidden><thead><tr><th width="85"></th><th width="283"></th><th width="344"></th><th></th></tr></thead><tbody><tr><td>STT</td><td>Metric</td><td>Mô tả</td><td>Interval</td></tr><tr><td>1</td><td>datasync_bytes_transferred_total</td><td>Tổng số byte transfer.</td><td>1 phút</td></tr><tr><td>2</td><td>datasync_checked_files_total</td><td>Tổng số file được kiểm tra.</td><td>1 phút</td></tr><tr><td>3</td><td>datasync_dirs_deleted_total</td><td>Tổng số thư mục bị xóa.</td><td>1 phút</td></tr><tr><td>4</td><td>datasync_errors_total</td><td>Tổng số file error được ghi nhận.</td><td>1 phút</td></tr><tr><td>5</td><td>datasync_fatal_error</td><td>Tổng số lỗi xảy ra.</td><td>1 phút</td></tr><tr><td>6</td><td>datasync_files_deleted_total</td><td>Tổng số file bị xóa.</td><td>1 phút</td></tr><tr><td>7</td><td>datasync_files_renamed_total</td><td>Tổng số file bị rename.</td><td>1 phút</td></tr><tr><td>8</td><td>datasync_files_transferred_total</td><td>Tổng số file được transfer.</td><td>1 phút</td></tr><tr><td>9</td><td>datasync_http_status_code</td><td>Số lượng trạng thái xảy ra của quá trình transfer dữ liệu.</td><td>1 phút</td></tr><tr><td>10</td><td>datasync_retry_error</td><td>Tổng số lượng file bị lỗi trong quá trình retry.</td><td>1 phút</td></tr><tr><td>11</td><td>datasync_speed</td><td>Tốc độ trung bình tính bằng byte trên giây kể từ khi bắt đầu quá trình transfer dữ liệu.</td><td>1 phút</td></tr></tbody></table>
