# HTTP Origin

## Tổng quan

Hiện tại, vCDN đang hỗ trợ HTTP Origin với các Thuật toán kết nối: **Round Robin, Least Connection, IP Hash và tự động chạy fail-over.**&#x20;

## Chi tiết

Khi bạn tạo một Web Accelerator, Object Download hoặc Video On Demand, màn hình khởi tạo CDN sẽ bao gồm các thông tin sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (9) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Trong đó:

* **Fail-Over Error Code:** Danh sách các mã lỗi HTTP (ví dụ: 500, 502, 503, 504), dựa vào các mã lỗi này hệ thống sẽ nhận biết và điều phối khách hàng qua các Server Origin khác trong pool.
* **Origin Load Balancing:** Cơ chế cân bằng tải giữa các Origin Server được chỉ định. Cụ thể:&#x20;
  * **Round Robin**: Hệ thống sẽ tự động điều phối traffic xuống Server Origin của khách hàng với phương thức xoay vòng – đều nhau giữa các servers.
  * **Least Connected:** Hệ thống sẽ chọn Server Origin có lượng connected thấp nhất để điều phối traffic xuống.
  * **IP Hashing:** Hệ thống sẽ dựa vào IP Client để điều phối và duy trì kết nối xuống Server Origin.
* **Origin Host Header:** Header được sử dụng khi gửi yêu cầu từ vCDN đến Origin Server.
* **IP Address:** Địa chỉ IP của Origin Server (ví dụ: IPv4 như 1.1.1.1 hoặc IPv6).
* **Weight:** Độ ưu tiên (weight) của Server Origin, nhập “0” để thiết lập Server Origin này ở chế độ Backup/Standy, số càng cao độ ưu tiên càng cao.

Sau khi nhập xong thông tin Server Origin và chọn **Add Server**, màn hình sẽ hiện ra danh sách các địa chỉ IP Server Origin và thông tin như hình sau:

_\* Khi khách hàng nhập thông tin domain chính, hệ thống sẽ tự động thêm các Server Origin dựa theo các bản ghi DNS có sẳn của tên miền vào khung số như hình bên dưới._

<figure><img src="../../../.gitbook/assets/image (239).png" alt=""><figcaption></figcaption></figure>

Trong đó:&#x20;

* **Priority** – thể hiện mức độ ưu tiên (weight) của Server Origin, số càng cao, độ ưu tiên càng cao.
* **Value**: Địa chỉ IPv4 của Origin Servers.
* **Algorithms**: Thuật toán phân tải traffic cho Origin Servers.
* **Status**: Thể hiện trạng thái <img src="../../../.gitbook/assets/image (240).png" alt="" data-size="line"> (**Active**) và  <img src="../../../.gitbook/assets/image (241).png" alt="" data-size="line">(**Disabled**)
  * **Active**: Origin Server sẽ được đưa vào Pool Origin Servers.
  * **Disabled**: Origin Server sẽ bị loại bỏ khỏi Pool Origin Servers.
* Hỗ trợ cấu hình các loại mã lỗi để hệ thống tự động thực hiện Fail-Over .
* **Origin:** cho phép khách hàng tự chỉ định các loại mã lỗi khi chạy theo mode Fail-Over.
