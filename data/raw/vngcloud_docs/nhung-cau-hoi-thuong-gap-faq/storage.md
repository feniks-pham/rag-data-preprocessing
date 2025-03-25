# vStorage

### \[vStorage] Token là gì?

Token là chuỗi ký tự được dùng để xác thực trong các yêu cầu (request) thực hiện tính năng trên hệ thống vStorage sử dụng giao thức HTTP, được truyền bên trong mỗi yêu cầu (request) dạng Restful API với header như sau “X-Auth-Token: gAAAAABjsYvUCXdVOkJ…“

### \[vStorage] Lấy token để làm gì?

Các client tool, SDK, Restful API lấy token để tái sử dụng nhiều lần, giúp yêu cầu xuất phát từ các công cụ phía người dùng client tool, SDK, Restful API nhanh hơn khi phải lấy token mới mỗi lần cần thực hiện yêu cầu (request).

### \[vStorage] Quyền hạn token như thế nào? Hiệu lực trong bao lâu?

Token là đại diện cho Username/ Password trên toàn bộ vStorage project nên có toàn quyền trên project và có hiệu lực trong 1 giờ, sau mỗi giờ bạn cần lấy lại token mới để tiếp tục sử dụng dịch vụ vStorage.

### \[vStorage] Tôi muốn khôi phục (recovery) một project của dịch vụ vStorage thì làm như thế nào?

Quý khách vui lòng xem tài liệu theo Link hướng dẫn [Gia hạn project](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-project/gia-han-project.md).

### \[vStorage] Tôi không tải được object từ dịch vụ lưu trữ vStorage, báo lỗi 400

Khi thực hiện tải object từ dịch vụ lưu trữ vStorage về, nếu quý khách gặp lỗi với mã lỗi HTTP 400, quý khách vui lòng kiểm tra lại tính chính xác của URI (object path) của object trên vStorage, các tham số truyền vào header/ params trong request tải object. Bên cạnh đó, quý khách vui lòng kiểm tra việc encode/ decode của URI khi tải file lên dịch vụ vStorage và tải object về. Cần đảm bảo sử dụng cùng phương thức để encode/ decode URI. Nếu vẫn gặp lỗi, quý khách vui lòng cung cấp chính xác cách thức đang sử dụng để tải object về để chúng tôi kiểm tra và hỗ trợ.

Liên quan đến encode/ decode URI, quý khách có thể tham khảo các link sau:\
[https://www.urlencoder.io/java/](https://www.urlencoder.io/java/)\
[https://www.urlencoder.io/php/](https://www.urlencoder.io/php/)

### \[vStorage] Tôi đang sử dụng vStorage tôi thấy website còn hạn chế tôi muốn tool sử dụng kết nối tới storage để upload file và tạo folder được không?

Hiện tại vStorage tương thích với các công cụ phía người dùng như:&#x20;

* SDK S3 AWS ​
* SDK SWIFT ​
* Công cụ phía người dùng dạng GUI: Cyberduck, S3 Browser.​
* Công cụ phía người dùng dạng CLI: Swift CLI, Rclone, S3cmd, Duplicity.&#x20;

Quý khách vui lòng xem tài liệu hướng dẫn làm việc với 3rd party softwares tại [3rd party softwares](../vstorage/object-storage/vstorage-hcm03/3rd-party-softwares/).

### \[vStorage] Tại sao tôi kiểm tra vStorage thì thấy bị mất project?

Quý khách kiểm tra lại đã đúng region mà quý khách khởi tạo project chưa, có thể nếu khác region sẽ không thấy được project khởi tạo ở region đó.

### \[vStorage] Tại sao tôi truy cập vào storage file tôi upload lên lại báo lỗi Unauthorized?

Quý khách vui lòng kiểm tra xem mình đã public container chưa. Nếu chưa nhờ quý khách truy cập vào project có chứa container cần upload file, sau đó thực hiện chuyển chế độ công khai container theo hướng dẫn tại [Chuyển chế độ công khai container](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-container/chuyen-che-do-cong-khai-container.md) và [Chuyển chế độ riêng tư container](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-container/chuyen-che-do-rieng-tu-container.md).

### \[vStorage] Tôi muốn connect dùng vCDN và vStorage thì làm thế nào?

Quý khách hãy thực hiện kết nối trên cấu hình vCDN dùng giao thức S3 Origin theo hướng dẫn tại [vCDN](../vcdn/).

### \[vStorage] Tôi muốn xóa không sử dụng storage nữa thì làm thế nào?

Quý khách vui lòng truy cập vào trang quản trị và xóa project không có nhu cầu sử dụng. Nếu tài khoản của quý khách là tài khoản trả trước và project vẫn còn thời hạn sử dụng thì khi thực hiện xóa project, quý khách sẽ được hoàn trả lại số tiền chưa sử dụng tính trên số ngày thực tế không sử dụng project của quý khách trên chu kỳ lưu trữ của project mà quý khách thực hiện mua ban đầu. Số tiền hoàn lại này được chúng tôi cộng vào số dư ví credit của quý khách, chi tiết tham khảo tại [Xóa project](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-project/xoa-project.md).

### \[vStorage] Tôi upload file lên Storage của tôi thì bị lỗi, không xem được file Mp4. Những file dưới 10mb lại xem được.

Có nhiều nguyên nhân có thể gây ra lỗi này nhưng chúng tôi gợi ý cách nhanh nhất để quý khách xử lý lỗi là quý khách thực hiện xóa file lỗi sau đó tải lên lại các file mà quý khách mong muốn.

### \[vStorage] Mình mới tạo storage trên vngcloud, giờ làm sao để upload file hoặc folder lên

Quý khách vui lòng tham khảo link hướng dẫn tải lên file tại [Tải lên tệp tin](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-directory-va-object/tai-len-tep-tin.md) và hướng dẫn làm việc với folder tại [Tạo folder](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-directory-va-object/lam-viec-voi-directory.md).

### \[vStorage] Truy cập API bị báo lỗi 404

Có nhiều nguyên nhân có thể gây ra lỗi 404 trong đó sai Auth-URL có thể là 1 nguyên nhân, quý khách vui lòng kiểm tra lại auth-url của mình nhé.

### \[vStorage] vStorage có những hỗ trợ nào để kiểm soát định danh truy cập vào tài nguyên?

Hiện tại, vStorage đã hỗ trợ các cách thức quản lý truy cập vào tài nguyên như sau:

* Quản lý truy cập vào tài nguyên trên dịch vụ lưu trữ vStorage thông qua tài khoản người dùng Root. Chi tiết tham khảo tại [Tài khoản người dùng Root](../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-nguoi-dung-root.md).
* Quản lý truy cập vào tài nguyên trên dịch vụ lưu trữ vStorage thông qua tài khoản người dùng IAM. Chi tiết tham khảo tại [Quản lý truy cập](../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/).

IAM (giới hạn quyền truy cập vào vStorage thông qua hệ thống vIAM theo policy được chỉ định), IP range ACLs (giới hạn khả năng truy cập vào project hoặc container của vStorage từ một số nguồn địa chỉ IP được xác định thông qua danh sách IP/Subnet thiết lập trên metadata ở cấp project hoặc container hoặc cả hai cấp) và vStorage Credentials (cho phép tạo các cặp key mà bạn có thể sử dụng chúng thông qua các 3rd party software để truy cập vStorage project/container). Chi tiết tham khảo tại [Quản lý truy cập](../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/).

### \[vStorage] Khi phân quyền tôi có thể thực hiện phân quyền trên từng directory, trên từng object, hay bắt buộc tôi phải phân quyền trên tất cả các object trong một container?

Bạn có thể phân quyền với các cấp độ object/ directory/ container thông qua tính năng vStorage IAM. Chi tiết tham khảo tính năng phân quyền truy cập cho vStorage tại đây [Phân quyền truy cập thông qua vIAM](../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-truy-cap-tai-nguyen-vstorage/phan-quyen-truy-cap-va-lam-viec-thong-qua-iam/).

### \[vStorage] Có thể mount vStorage thành 1 ổ cứng trên vServer để sử dụng như 1 ổ volume data được không?

Bạn có thể sử dụng các 3rd party software như Rclone / S3cmd có thể thiết lập mount vStorage để sử dụng như ổ mạng. Chi tiết xem hướng dẫn [tại đây](../vstorage/object-storage/vstorage-hcm03/tinh-huong-su-dung-use-case/migrate-du-lieu-migrate-data/rclone-mount-vstorage-len-window-server.md)  hoặc [tại đây](../vstorage/object-storage/vstorage-hcm03/tinh-huong-su-dung-use-case/migrate-du-lieu-migrate-data/rclone-mount-vstorage-thanh-local-drive-tren-linux.md) nếu bạn sử dụng Linux.

### \[vStorage] Tôi có thể xem traffic và request sử dụng thực tế hằng tháng ở đâu? Có hỗ trợ xem realtime không?

Bạn có thể có thể xem traffic và request theo hướng dẫn tại [Xem thông tin project](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-project/xem-thong-tin-project.md).

### \[vStorage] Những loại traffic nào thì được tính là traffic quốc tế trong dịch vụ vStorage?

Traffic đi ra khỏi lãnh thổ Việt Nam được tính là traffic quốc tế (international traffic). Bạn có thể xem thông tin traffic theo hướng dẫn tại [Xem thông tin project](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-project/xem-thong-tin-project.md).

### \[vStorage] Cách tính phí request của vStorage được tính theo cách nào?

Đối với các storage class loại Silver / Archive, sẽ có phát sinh request khi bạn tương tác với object. Khi lượng request này vượt khỏi mốc miễn phí (mốc được thiết lập sẵn bởi chúng tôi và được thể hiện trên giao diện khi bạn [Khởi tạo project](../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-project/khoi-tao-project.md)) thì lượng request vượt mức này sẽ được thống kê và tính phí bổ sung trên 1 bill phí vượt mức vào cuối tháng. \
Các hành động tính phí theo request bao gồm:

* GET: được sử dụng để lấy thông tin từ server theo URL đã cung cấp. Ví dụ lấy thông tin metadata của danh sách accounts, containers, objects... hay lấy về nội dung (content) của objects.
* HEAD: giống với GET nhưng response trả về không có body, chỉ có header của HTTP. Ví dụ Content-Type, Accept-Encoding, Accept-Charset.
* POST: gửi thông tin metadata, nội dung của đối tượng (dữ liệu) tới server. Ví dụ, upload 1 file đến server.
* PUT: ghi đè tất cả thông tin của đối tượng với những gì được gửi lên server. Ví dụ như ghi đè nội dung của 1 object đã được upload lên server trước đó.
* DELETE: xóa đối tượng khỏi server. Ví dụ như xóa 1 object đã được upload lên trước đó khỏi vStorage.

Bạn cũng có thể tham khảo cách tính phí của chúng tôi tại [Quản lý hóa đơn, chi phí & tài nguyên trên VNG Cloud](../quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/).
