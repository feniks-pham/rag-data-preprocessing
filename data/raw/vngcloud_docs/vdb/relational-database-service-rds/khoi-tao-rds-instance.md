# Khởi tạo RDS Instance

Để khởi tạo RDS Instacne, bạn có thể tham khảo chi tiết các bước làm trong hướng dẫn bên dưới đây.

## Truy cập vDB Portal

Đầu tiên, bạn truy cập đến giao diện dịch vụ vDB qua 2 cách như sau:

* Cách 1: Truy cập trang chủ VNG Cloud tại đường dẫn: [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/). Tại giao diện chính, bạn tìm đến dịch vụ **vServer** và chọn dịch vụ **vDB Relational** trong danh sách sản phẩm/dịch vụ vServer.
* Cách 2: Truy cập trực tiếp đến trang chủ vDB Relational tại đường dẫn: [https://vdb.console.vngcloud.vn/relational/database](https://vdb.console.vngcloud.vn/relational/database)

## Khởi tạo RDS instance

Tại giao diện quản lý Database, bạn click chọn **Create Database**. Quá trình khởi tạo sẽ trải qua 6 phần như hướng dẫn bên dưới:

* **Bước 1 Cấu hình cơ bản:** Bạn chọn **Tên Database** và **Database Engine** mong muốn.
* **Bước 2 Thông số kỹ thuật:** Bạn có thể tùy chỉnh các thông tin cấu hình, engine license, engine version như sau
  * **Engine License**: giấy phép sử dụng database, có thể là phiên bản community hoặc enterprise (tùy từng loại database).
  * **Engine Version**: phiên bản database.
  * **Flavor**: cấu hình RDS Instance, bao gồm số core, lượng RAM và đi kèm dung lượng Free Backup. Lưu ý: nếu tổng dung lượng tất cả các bản backup của bạn vượt quá quota này, bạn sẽ phải trả thêm chi phí cho phần dung lượng backup vượt quá quota.
  * **Storage type**: loại ổ cứng lưu trữ.
  * **Storage Size**: kích cỡ ổ cứng lưu trữ dữ liệu (bao gồm data và log của database).
* **Bước 3 Cài đặt phiên bản DB:** bạn lựa chọn
  * **Master username**: bạn sẽ dùng user này để quản trị database instance.
  * **Master password**: password của master user. VNG Cloud khuyến nghị bạn đặt password đủ mạnh và lưu trữ password này tại nơi an toàn. Để đảm bảo an toàn thông tin, password cần thỏa tất cả yêu cầu tối thiểu như sau:
    * Password phải có độ dài trong khoảng 8-32 kí tự.
      * Các kí tự được cho phép bao gồm: A-Z, a-z, 0-9 và các kí tự đặc biệt.
      * Các kí tự đặc biệt được cho phép bao gồm: !#$%&()\*+-.:<=>?@\[]^\_{|}\~
      * Password phải bắt đầu bằng kí tự chữ cái: A-Z hoặc a-z.
      * Password không được bắt đầu hay kết thúc bằng các kí tự đặc biệt.
* **Bước 4 Mạng và bảo mật:**&#x54;ại mục **Network & Security**, bạn lựa chọn&#x20;
  * **Cloud Network (VPC & Subnet)** sẽ sử dụng cho RDS Instance này. Mọi RDS Instance đều phải kết nối với một Cloud Network. Nếu chưa có Cloud Network nào, bạn có thể tạo một Cloud Network mới với hướng dẫn[ tại đây](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/).
  * **Truy cập công khai:** Nếu bạn muốn RDS Instance có IP Public và có thể truy cập từ ngoài Internet, bạn cần bật tính năng **Truy cập công khai** (**Public Accessbility)**, nếu bạn muốn RDS Instance chỉ có IP Private và chỉ những Cloud Servers mới có thể truy cập được thì bạn cần tắt tính năng Public Accessibility.

**Lưu ý**: việc lựa chọn có hay không Public Accessibility chỉ được lựa chọn một lần duy nhất tại thời điểm khởi tạo này. Bạn không thể thay đổi thiết lập này về sau. Để tăng cường bảo mật, VNG Cloud cho phép bạn giới hạn các địa chỉ IP tin cậy được phép truy cập vào mỗi RDS Instance thông qua **Security Group Rules**.

* **Bước 5 Tùy chọn DB:** Tại mục **DB Options**, bạn có thể cấu hình
  * **Tên cơ sở dữ liệu/Database Name**: Chọn tên database sẽ được khởi tạo tự động.
  * **Nhóm cấu hình/DB configuration group** (optional): Chọn Configuration Group sẽ được áp dụng cho RDS Instance này, nếu bạn chưa có nhu cầu tùy chỉnh cấu hình thì có thể bỏ qua trường này.
* **Bước 6 Cài đặt sao lưu:** Tại mục **Backup**, bạn có thể cấu hình:
  * **Automatic daily backup**: bật/tắt tính năng tự động tạo backup hàng ngày với thời điểm được lựa chọn trước.
  * **Backup retention period**: khoảng thời gian lưu trữ các bản backup tự động. Các bản backup tự động được lưu trữ quá thời gian này sẽ được tự động xóa khỏi hệ thống. Thông số này không ảnh huởng đến vòng đời của các bản backup được bạn tạo bằng tay.
  * **Backup time**: thời điểm tiến hành tạo bản backup tự động. VNG Cloud khuyến nghị bạn cấu hình thời điểm này vào thời điểm có lượng truy cập hệ thống thấp nhất trong ngày, thường là từ 12AM - 5AM.

Sau khi cấu hình xong,tại mục **Tóm tắt/Summary** bên tay phải, bạn rà soát lại các thông tin, khi mọi thông tin đều đã chính xác, bạn nhấn **Create Database** để hoàn tất quá trìn&#x68;**.** Trong quá trình khởi tạo, RDS Instance sẽ có trạng thái **Building** hay **Build**. Nếu khởi tạo thành công, RDS Instance sẽ có trạng thái **Active**.

**Lưu ý**:

Mặc định, RDS Instance tạo ra sẽ có sẵn 3 user:

* 2 user hệ thống là root@localhost & [os\_admin@127.0.0.1](mailto:os_admin@127.0.0.1).
* 1 master user giúp bạn có thể truy cập và quản lý RDS Instance.

Hai user hệ thống được tạo ra để VNG Cloud phục vụ các tác vụ tự động như tạo backup, cấu hình replication, restore… và bạn không cần phải quan tâm những user này. Tuy nhiên, việc bạn xóa 2 user hệ thống này sẽ gây ra lỗi hệ thống cho RDS Instance và khiến các tính năng trên mất tác dụng. VNG Cloud sẽ không chịu trách nhiệm nếu bạn tìm cách xóa 2 user hệ thống nhưng vẫn sẽ hỗ trợ tốt nhất có thể để khôi phục cho bạn cho bạn.

