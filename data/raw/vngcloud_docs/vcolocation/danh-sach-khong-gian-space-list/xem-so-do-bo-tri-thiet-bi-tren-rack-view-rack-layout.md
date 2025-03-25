# Xem sơ đồ bố trí thiết bị trên rack (View rack layout)

Bạn có thể xem Rack layout (sơ đồ bố trí thiết bị trên rack) bằng cách chọn tủ rack cần xem và bấm nút “View rack layout“ phía trên đầu của danh sách (ứng dụng hỗ trợ xem rack layout của 10 tủ rack cùng một lúc).

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### **Trong giao diện Rack layout, bạn có thể:** <a href="#xemsodobotrithietbitrenrack-viewracklayout-tronggiaodienracklayout-bancothe" id="xemsodobotrithietbitrenrack-viewracklayout-tronggiaodienracklayout-bancothe"></a>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### **Xem vị trí lắp đặt của thiết bị trên tủ rack** <a href="#xemsodobotrithietbitrenrack-viewracklayout-xemvitrilapdatcuathietbitrenturack" id="xemsodobotrithietbitrenrack-viewracklayout-xemvitrilapdatcuathietbitrenturack"></a>

Biết vị trí chính xác của thiết bị trên tủ rack, các thiết bị được phân biệt bởi các màu sắc khác nhau theo loại thiết bị: Server, Network device, Data panel, Sheve và Other (loại thiết bị khác).

#### **Xem trạng thái sở hữu của các Rack Unit** <a href="#xemsodobotrithietbitrenrack-viewracklayout-xemtrangthaisohuucuacacrackunit" id="xemsodobotrithietbitrenrack-viewracklayout-xemtrangthaisohuucuacacrackunit"></a>

Cho phép bạn phân biệt các Rack Unit theo trạng thái sở hữu của chúng:

* **Unused:** là các Rack unit thuộc quyền sở hữu của bạn, nhưng chưa có thiết bị lắp đặt trên đó.
* **Reserved**: là các Rack unit được để dành cho bạn
* **Occupied**: là các Rack unit được sở hữu bởi khách hàng khác
* **Available**: là các Rack unit chưa được để dành hoặc cho ai thuê

#### **Xem thông tin tổng quan của tủ Rack** <a href="#xemsodobotrithietbitrenrack-viewracklayout-xemthongtintongquancuaturack" id="xemsodobotrithietbitrenrack-viewracklayout-xemthongtintongquancuaturack"></a>

Bạn có thể xem thông tin tổng quan của từng tủ Rack tại giao diện này, bao gồm:

* Vị trí Rack: Site, Floor, Room, Cage
* RU height: chiều cao tính theo U của tủ
* Used/Free Front/Rear RU: số lượng RU đã sử dụng/còn trống
* Thông tin về công suất nguồn (R/B/M), trong đó:
  * R = Rated power, công suất thiết kế của tủ rack
  * B = Budgeted power, công suất cho phép của tủ
  * M = Measure power, công suất đo được tức thời của tủ
* Thông tin nhiệt độ, độ ẩm tức thời
* Max load (kg): khả năng chịu tải (cân nặng) của tủ
* Total weight (kg): tổng cân nặng của các thiết bị đặt trên tủ
* Total device: tổng số thiết bị đang đặt trên tủ

#### **Xem thông số của các thanh RPDU** <a href="#xemsodobotrithietbitrenrack-viewracklayout-xemthongsocuacacthanhrpdu" id="xemsodobotrithietbitrenrack-viewracklayout-xemthongsocuacacthanhrpdu"></a>

Bạn có thể xem thông số của từng thanh rPDU theo vị trí lắp đặt của chúng (L1, L2, L3, R1, R2, R3)

* rPDU ID: mã định danh của thanh rPDU
* rPDU type: loại rPDU (1PH: 1 pha, 3PH: 3 pha)
* Vendor: tên nhà sản xuất
* Model: model của rPDU
* Rack: tủ rack chứa rPDU
* Position: vị trí của rPDU trong tủ rack (L1, L2, L3, R1, R2, R3)
* Thống kê số lượng socket nguồn trên thanh rPDU: total/free (tổng số socket/số socket chưa cắm nguồn)
* Thông số nguồn điện của thanh rPDU:
  * Power (R/B/M) (kW): Rated/Budgeted/Measured
  * V (R/B/M): điện áp Danh định/Cho phép/Đo được
  * PF (R/B/M): hệ số công suất Danh định/Cho phép/Đo được
  * I (R/B/M): cường độ dòng điện Danh định/Cho phép/Đo được

#### **Tìm kiếm vị trí lắp đặt thiết bị theo số serial number của thiết bị** <a href="#xemsodobotrithietbitrenrack-viewracklayout-timkiemvitrilapdatthietbitheososerialnumbercuathietbi" id="xemsodobotrithietbitrenrack-viewracklayout-timkiemvitrilapdatthietbitheososerialnumbercuathietbi"></a>

Bạn có thể dễ dàng xác định vị trí của thiết bị trên tủ rack bằng cách sử dụng tính năng tìm kiếm theo Serial number của thiết bị

{% hint style="info" %}
**Lưu ý**

Một số thông tin sẽ không hiển thị đối với các tủ rack thuê lẻ từng Rack Unit
{% endhint %}

***

Các tính năng có trong Space list:

* [Xem sơ đồ bố trí thiết bị trên rack (View rack layout)](xem-so-do-bo-tri-thiet-bi-tren-rack-view-rack-layout.md)
* [Xem thông tin chi tiết của tủ rack (View details)](xem-thong-tin-chi-tiet-cua-tu-rack.md)
* [Lọc danh sách](loc-danh-sach.md)
