# Làm việc với Log search

### Tổng quan <a href="#lamviecvoilogsearch-tongquan" id="lamviecvoilogsearch-tongquan"></a>

Log Search là nơi để bạn tìm kiếm và phân tích trên dữ liệu của bạn. Với Log search, chúng tôi cung cấp cho bạn các tính năng bao gồm:&#x20;

* Tìm kiếm, lọc, trực quan hóa và phân tích logs từ tất cả các dịch vụ, ứng dụng cũng như hệ thống của bạn. (Search logs)
* Xuất dữ liệu logs. (Export logs)

***

### Tìm kiếm và phân tích logs <a href="#lamviecvoilogsearch-timkiemvaphantichlogs" id="lamviecvoilogsearch-timkiemvaphantichlogs"></a>

Để thực hiện tìm kiếm và phân tích log, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Chọn **Log.**
2. Chọn **Log search**.
3. Chọn **Log project** nào bạn cần xem và phân tích logs. Vị trí chọn log project được hiển thị như hình bên dưới:

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/49649959/image2023-8-2_16-5-28.png?version=1&#x26;modificationDate=1690967129000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Trong đó:&#x20;

<table><thead><tr><th width="96">Vùng</th><th>Mô tả</th><th>Ví dụ minh họa</th></tr></thead><tbody><tr><td>1</td><td><p>Vùng chọn Log project mà bạn muốn tìm kiếm và phân tích logs.</p><ul><li>Chọn hoặc tìm kiếm <strong>Log project</strong> mà bạn muốn xem chi tiết logs.</li></ul></td><td><img src="https://docs-admin.vngcloud.vn/download/thumbnails/49649959/image2023-8-7_13-52-3.png?version=1&#x26;modificationDate=1691391124000&#x26;api=v2" alt="" data-size="original"></td></tr><tr><td>2</td><td>Vùng tìm kiếm logs, chi tiết cách tạo câu lệnh xem tại <a href="https://docs-admin.vngcloud.vn/display/VPV/Search+logs">Search logs</a>.</td><td><br></td></tr><tr><td>3</td><td><p>Vùng chọn điều kiện lọc logs theo thời gian</p><ul><li>Chọn điều kiện lọc logs theo thời gian bởi 1 trong 3 cách: <strong>Quick time, Relative time, Absolute time</strong>.</li><li>Biểu tượng Refresh logs: bạn có thể sử dụng để làm mới danh sách logs hiển thị theo điều kiện đã chọn. </li><li>Ngoài cách chọn Refresh thủ công, bạn có thể thiết lập Refresh tự động dữ liệu logs sau mỗi khoảng thời gian 10s, 2 minute,... mà chúng tôi cung cấp.</li></ul></td><td><p><img src="https://docs-admin.vngcloud.vn/download/thumbnails/49649959/image2023-8-7_13-54-33.png?version=1&#x26;modificationDate=1691391273000&#x26;api=v2" alt="" data-size="original"></p><p><img src="https://docs-admin.vngcloud.vn/download/thumbnails/49649959/image2023-8-7_13-57-22.png?version=1&#x26;modificationDate=1691391443000&#x26;api=v2" alt="" data-size="original"></p></td></tr><tr><td>4</td><td><p>Vùng thêm danh sách các fields của log</p><ul><li><strong>Dislayed fields</strong>: danh sách những field mặc định và những field bạn chọn để hiển thị Log ở khung nội dung. </li><li>Nếu muốn hiển thị thêm các fields, bạn tick chọn các fields được liệt kê ở <strong>Available fields</strong>.</li><li>Ngoài ra bạn còn có thể sắp xếp lại thứ tự các fields hiển thị bằng cách kéo thả biểu tượng 3 chấm ở các fields.</li></ul></td><td><img src="https://docs-admin.vngcloud.vn/download/thumbnails/49649959/image2023-8-7_13-59-32.png?version=1&#x26;modificationDate=1691391572000&#x26;api=v2" alt=""><img src="https://docs-admin.vngcloud.vn/download/thumbnails/49649959/image2023-8-7_14-0-31.png?version=1&#x26;modificationDate=1691391632000&#x26;api=v2" alt=""></td></tr><tr><td>5</td><td>Vùng hiển thị biểu đồ.</td><td><img src="https://docs-admin.vngcloud.vn/download/thumbnails/49649959/image2023-8-7_14-1-12.png?version=1&#x26;modificationDate=1691391673000&#x26;api=v2" alt=""></td></tr><tr><td>6</td><td><p>Vùng hiển thị dữ liệu logs: </p><p>Tại khung ở giữa hệ thống sẽ trả về các dòng Log theo sự lựa chọn của bạn với 3 yếu tố</p><ul><li>Chỉ hiển thị những Logs thoả mãn điều kiện của khung search và filter ỏ <strong>Vùng 2</strong>.</li><li>Chỉ hiện thị những dòng Log nằm trong khung thời gian được chọn ở <strong>Vùng 3.</strong></li><li>Hiển thị những giá trị của các field nằm trong Displayed field ở <strong>Vùng 4,</strong> để xem đẩy đủ dòng Logs bạn nhấn vào dòng Logs để xem chi tiết.</li></ul><p>Khi có quá nhiều Log trả về, hệ thống sẽ hiển thị 1 phần và lazy load khi bạn kéo chuột xuống.</p></td><td><br></td></tr><tr><td>7</td><td>Vùng để bạn export logs, tham khảo tại <a href="https://docs-admin.vngcloud.vn/display/VPV/Export+logs">Export logs</a></td><td><br></td></tr></tbody></table>

&#x20;     4\. Tiếp tục thực hiện **tìm kiếm và phân tích logs**.

\
