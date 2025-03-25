# Xem báo cáo tóm tắt trên toàn bộ các region

Sau khi bạn đã tạo các project để lưu trữ dữ liệu. Chúng tôi cung cấp cho bạn các báo cáo thống kê các chỉ số thuộc project, từ đó bạn có thể quản lý, kiểm soát và đánh giá hiệu quả việc sử dụng đơn vị lưu trữ hợp lý. Các thuộc tính được chúng tôi sử dụng xuyên suốt các báo cáo bao gồm:&#x20;

* Quota
* Lưu lượng
* Dung lượng sử dụng
* Số lượng request

Để báo cáo tóm tắt trên toàn bộ các region, bạn có thể:&#x20;

&#x20;Sử dụng vStorage portal

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **Báo cáo**, sau đó chọn khoảng thời gian mong muốn tổng hợp dữ liệu trên báo cáo. Mặc định chúng tôi sẽ hiển thị báo cáo trong ngày. Bạn có thể điều chỉnh khoảng thời gian xem báo cáo lên tới 3 tháng thông qua

* Chọn một phương án mà chúng tôi cung cấp sẵn tại mục **Nhanh**.
* Nhập khoảng thời gian tương đối mà bạn mong muốn xem dữ liệu (thường theo mốc giờ, phút, giây) tại mục **Tương đối**.
* Chọn thời gian bắt đầu và thời gian kết thúc chính xác mà bạn muốn xem dữ liệu (thường theo mốc ngày, giờ, phút) tại mục **Chính xác.**

3\. Trên trang báo cáo các thông số chi tiết của tất cả các **project** thuộc mọi **region,** bạn có thể xem các thuộc tính cho project bao gồm:&#x20;

* **Thông tin chung**: cung cấp các thông tin chung bao gồm:
  * Region.
  * Số lượng project được sử dụng trong mỗi region.
  * Tổng quota của các project trong mỗi region.
  * Tổng dung lượng sử dụng của các project trong mỗi region.
  * Dung lượng sử dụng lớn nhất: dung lượng sử dụng lớn nhất trong khoảng thời gian mà bạn chọn.
  * Tổng lưu lượng: tổng lưu lượng truy cập trong khoảng thời gian mà bạn chọn.
  * Quota lớn nhất: giá trị quota lớn nhất mà bạn thực hiện mua trong khoảng thời gian mà bạn chọn.
  * Tổng số lượng request: bao gồm tổng số request ở các loại HET, HEAD, PUT, POST, DELETE trong khoảng thời gian mà bạn chọn.
* **Thông tin chi tiết**: cung cấp các thông tin bao gồm:
  * Dung lượng sử dụng chi theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.
  * Lưu lượng truy cập chia theo lưu lượng nội bộ, lưu lượng quốc tế, lưu lượng nội địa trong khoảng thời gian mà bạn chọn.
  * Số lượng request kiểu GET/ HEAD chia theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.
  * Số lượng request kiểu PUT/ POST/ DELETE chia theo từng gói lưu trữ Gold, Silver, Archive trong khoảng thời gian mà bạn chọn.

{% hint style="info" %}
**Chú ý:**&#x20;



* Các thông số của mỗi project được tổng hợp vào các báo cáo được chúng tôi thực hiện tổng hợp 2 lần mỗi ngày vào 2 khung giờ cố định: 7:00 AM và 12:00 PM. Ví dụ: khi bạn tạo một project, tạo container, tải tệp tệp tin hay thực hiện các hành động PUT/ DELETE object vào khung thời gian 04:00 PM ngày 01/01/2023 thì sau 12:00 PM cùng ngày, các dữ liệu này sẽ được cập nhật. Tức là từ ngày 02/01/2023 các thông số này sẽ được cập nhật đầy đủ trên các báo cáo.
* Để cung cấp góc nhìn dài hạn cho báo cáo của bạn, chúng tôi hỗ trợ bạn có thể xem các báo cáo này với chu kỳ 3 tháng. Ví dụ bạn có thể chọn xem dữ liệu báo cáo từ ngày 01/01/2023 tới 31/03/2023.&#x20;
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/Xem_bao_cao_tom_tat.gif" alt=""><figcaption></figcaption></figure>
