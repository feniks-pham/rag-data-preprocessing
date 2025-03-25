# Làm việc với báo cáo

vStorage cung cấp cho bạn các báo cáo thống kê lưu trữ và họa động của project, bạn có thể xem các thông tin này trong từng khoảng thời gian mong muốn qua các dạng biểu đồ khác nhau mà chúng tôi cung cấp.

{% hint style="info" %}
**Chú ý:**

* Các thông số của mỗi project được tổng hợp vào các báo cáo được chúng tôi thực hiện tổng hợp 2 lần mỗi ngày vào 2 khung giờ cố định: 7:00 AM và 12:00 PM. Ví dụ: khi bạn tạo một project, tạo bucket, tải tệp tệp tin hay thực hiện các hành động PUT/ DELETE object vào khung thời gian 04:00 PM ngày 01/01/2023 thì sau 12:00 PM cùng ngày, các dữ liệu này sẽ được cập nhật. Tức là từ ngày 02/01/2023 các thông số này sẽ được cập nhật đầy đủ trên các báo cáo.
* Để cung cấp góc nhìn dài hạn cho báo cáo của bạn, chúng tôi hỗ trợ bạn có thể xem các báo cáo này với chu kỳ 3 tháng. Ví dụ bạn có thể chọn xem dữ liệu báo cáo từ ngày 01/01/2023 tới 31/03/2023.
{% endhint %}

## Xem báo cáo tóm tắt trên một region cụ thể

Để báo cáo tóm tắt các project trên 1 region cụ thể, bạn có thể:

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **Region** cần xem báo cáo**.**

3\. Chọn **Time range** (khoảng thời gian) mong muốn tổng hợp dữ liệu trên báo cáo. Mặc định chúng tôi sẽ hiển thị báo cáo trong tháng. Bạn có thể điều chỉnh khoảng thời gian xem báo cáo lên tới 3 tháng thông qua

* Chọn một phương án mà chúng tôi cung cấp sẵn tại mục **Quick**.
* Nhập khoảng thời gian tương đối mà bạn mong muốn xem dữ liệu (thường theo mốc giờ, phút, giây) tại mục **Relative**.
* Chọn thời gian bắt đầu và thời gian kết thúc chính xác mà bạn muốn xem dữ liệu (thường theo mốc ngày, giờ, phút) tại mục **Absolute.**

4\. Trên trang báo cáo các thông số chi tiết của tất cả các **project** thuộc một **region,** bạn có thể xem các thuộc tính cho project bao gồm:

* **Thông tin chung**: cung cấp các thông tin chung bao gồm:
  * **Max Usage**: dung lượng sử dụng lớn nhất trong khoảng thời gian mà bạn chọn.
  * **Total Traffic**: tổng lưu lượng truy cập trong khoảng thời gian mà bạn chọn.
  * **Max Quota**: giá trị quota lớn nhất mà bạn thực hiện mua trong khoảng thời gian mà bạn chọn.
  * **Total requests**: bao gồm tổng số request ở các loại HET, HEAD, PUT, POST, DELETE trong khoảng thời gian mà bạn chọn.
* **Thông tin chi tiết**: cung cấp các thông tin bao gồm:
  * Usage chi theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.
  * Traffic chia theo lưu lượng nội bộ, lưu lượng quốc tế, lưu lượng nội địa trong khoảng thời gian mà bạn chọn.
  * Số lượng request kiểu GET/ HEAD chia theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.
  * Số lượng request kiểu PUT/ POST/ DELETE chia theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.

## Xem báo cáo tóm tắt trên một project cụ thể

Để báo cáo tóm tắt các project trên 1 region cụ thể, bạn có thể:

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **Region** cần xem báo cáo**.**

3\. Chọn **Project** cần xem báo cáo**.**

3\. Chọn **Time range** (khoảng thời gian) mong muốn tổng hợp dữ liệu trên báo cáo. Mặc định chúng tôi sẽ hiển thị báo cáo trong tháng. Bạn có thể điều chỉnh khoảng thời gian xem báo cáo lên tới 3 tháng thông qua

* Chọn một phương án mà chúng tôi cung cấp sẵn tại mục **Quick**.
* Nhập khoảng thời gian tương đối mà bạn mong muốn xem dữ liệu (thường theo mốc giờ, phút, giây) tại mục **Relative**.
* Chọn thời gian bắt đầu và thời gian kết thúc chính xác mà bạn muốn xem dữ liệu (thường theo mốc ngày, giờ, phút) tại mục **Absolute.**

4\. Trên trang báo cáo các thông số chi tiết của một **project** thuộc một **region,** bạn có thể xem các thuộc tính cho project bao gồm:

* **Thông tin chung**: cung cấp các thông tin chung bao gồm:
  * **Max Usage**: dung lượng sử dụng lớn nhất trong khoảng thời gian mà bạn chọn.
  * **Total Traffic**: tổng lưu lượng truy cập trong khoảng thời gian mà bạn chọn.
  * **Max Quota**: giá trị quota lớn nhất mà bạn thực hiện mua trong khoảng thời gian mà bạn chọn.
  * **Total Requests**: bao gồm tổng số request ở các loại HET, HEAD, PUT, POST, DELETE trong khoảng thời gian mà bạn chọn.
  * Usage chi theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.
  * Traffic chia theo lưu lượng nội bộ, lưu lượng quốc tế, lưu lượng nội địa trong khoảng thời gian mà bạn chọn.
  * Số lượng request kiểu GET/ HEAD chia theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.
  * Số lượng request kiểu PUT/ POST/ DELETE chia theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.
* **Thông tin chi tiết**: cung cấp các thông tin bao gồm:
  * **Traffic Report**: chia theo lưu lượng nội bộ, lưu lượng quốc tế, lưu lượng nội địa trong khoảng thời gian mà bạn chọn. Bên cạnh đó chúng tôi hỗ trợ bạn theo dõi lưu lượng truy cập theo từng ngày thông qua biểu đồ đường, cột và bảng dữ liệu.
  * **Request Report**: chia theo số lượng request ở các loại HET, HEAD, PUT, POST, DELETE trong khoảng thời gian mà bạn chọn. Bên cạnh đó chúng tôi hỗ trợ bạn theo dõi số lượng request theo từng ngày thông qua biểu đồ đường, cột và bảng dữ liệu.
  * **Usage Report**: chia theo từng gói lưu trữ ở các loại Gold, Silver, Archive trong khoảng thời gian mà bạn chọn. Bên cạnh đó chúng tôi hỗ trợ bạn theo dõi dung lượng lưu trữ theo từng ngày thông qua biểu đồ đường, cột và bảng dữ liệu.
  * **Quota Report**: giá trị quota hiện tại của project. Bên cạnh đó chúng tôi hỗ trợ bạn theo dõi quota theo từng ngày thông qua biểu đồ đường, cột và bảng dữ liệu.
