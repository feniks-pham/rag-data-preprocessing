# Khởi tạo MDS Instance

## Truy cập vDB Portal

Đầu tiên, bạn truy cập đến giao diện dịch vụ vDB qua 2 cách như sau:

* Cách 1: Truy cập trang chủ VNG Cloud tại đường dẫn: [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/). Tại giao diện chính, bạn tìm đến dịch vụ **vServer** và chọn dịch vụ **vDB MemoryStore** trong danh sách sản phẩm/dịch vụ vServer.
* Cách 2: Truy cập trực tiếp đến trang chủ **vDB MemoryStore** tại đường dẫn: [https://vdb.console.vngcloud.vn/memorystore/database](https://vdb.console.vngcloud.vn/memorystore/database)

## Khởi tạo MDS instance

Tại giao diện quản lý Database, bạn click chọn **Create Database**. Quá trình khởi tạo sẽ trải qua 6 phần như hướng dẫn bên dưới:

* **Bước 1 Cấu hình cơ bản:** Bạn chọn **Tên Database** và **Database Engine** mong muốn.
* **Bước 2 Thông số kỹ thuật:** Bạn có thể tùy chỉnh các thông tin cấu hình, engine license, engine version như sau
  * **Engine License**: giấy phép sử dụng database, có thể là phiên bản community hoặc enterprise (tùy từng loại database).
  * **Engine Version**: phiên bản database.
  * **Flavor**: cấu hình MDS Instance, bao gồm số core, lượng RAM và đi kèm dung lượng Free Backup. Lưu ý: nếu tổng dung lượng tất cả các bản backup của bạn vượt quá quota này, bạn sẽ phải trả thêm chi phí cho phần dung lượng backup vượt quá quota.
* **Bước 3 Cài đặt phiên bản DB:** bạn lựa chọn
  * **Yêu cầu mật khẩu**: bật yêu cầu mật khẩu để quản trị database instance này nếu muốn.
  * **Mật khẩu**: Trường hợp bật yêu cầu mật khẩu, bần cần nhập vào mật khẩu của mình. VNG Cloud khuyến nghị bạn đặt password đủ mạnh và lưu trữ password này tại nơi an toàn. Để đảm bảo an toàn thông tin, password cần thỏa tất cả yêu cầu tối thiểu độ dài, ký tự cho phép, ký tự đặc biệt,...
* **Bước 4 Mạng và bảo mật:**&#x54;ại mục **Network & Security**, bạn lựa chọn&#x20;
  * **Cloud Network (VPC & Subnet)** sẽ sử dụng cho MDS Instance này. Mọi RDS Instance đều phải kết nối với một Cloud Network. Nếu chưa có Cloud Network nào, bạn có thể tạo một Cloud Network mới với hướng dẫn[ tại đây](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/).
  * **Truy cập công khai:** Nếu bạn muốn MDS Instance có IP Public và có thể truy cập từ ngoài Internet, bạn cần bật tính năng **Truy cập công khai** (**Public Accessbility)**, nếu bạn muốn MDS Instance chỉ có IP Private và chỉ những Cloud Servers mới có thể truy cập được thì bạn cần tắt tính năng Public Accessibility.

**Lưu ý**: Để tăng cường bảo mật, VNG Cloud cho phép bạn giới hạn các địa chỉ IP tin cậy được phép truy cập vào mỗi MDS Instance thông qua **Security Group Rules**.

* **Bước 5 Tùy chọn DB:** Tại mục **DB Options**, bạn có thể cấu hình
  * **Nhóm cấu hình/DB configuration group** (optional): Chọn Configuration Group sẽ được áp dụng cho MDS Instance này, nếu bạn chưa có nhu cầu tùy chỉnh cấu hình thì có thể bỏ qua trường này.
* **Bước 6 Cài đặt sao lưu:** Tại mục **Backup**, bạn có thể cấu hình:
  * **Automatic daily backup**: bật/tắt tính năng tự động tạo backup hàng ngày với thời điểm được lựa chọn trước.
  * **Backup retention period**: khoảng thời gian lưu trữ các bản backup tự động. Các bản backup tự động được lưu trữ quá thời gian này sẽ được tự động xóa khỏi hệ thống. Thông số này không ảnh huởng đến vòng đời của các bản backup được bạn tạo bằng tay.
  * **Backup time**: thời điểm tiến hành tạo bản backup tự động. VNG Cloud khuyến nghị bạn cấu hình thời điểm này vào thời điểm có lượng truy cập hệ thống thấp nhất trong ngày, thường là từ 12AM - 5AM.

Sau khi cấu hình xong,tại mục **Tóm tắt/Summary** bên tay phải, bạn rà soát lại các thông tin, khi mọi thông tin đều đã chính xác, bạn nhấn **Create Database** để hoàn tất quá trìn&#x68;**.** Trong quá trình khởi tạo, MDS Instance sẽ có trạng thái **Building** hay **Build**. Nếu khởi tạo thành công, MDS Instance sẽ có trạng thái **Active**.

Chúc mừng bạn đã khởi tạo thành công DB Instance trên hệ thống VNG Cloud. Mời bạn đến hướng dẫn [kết nối MDS Instance](ket-noi-mds-instance.md) để bắt đầu sử dụng cơ sở dữ liệu.

