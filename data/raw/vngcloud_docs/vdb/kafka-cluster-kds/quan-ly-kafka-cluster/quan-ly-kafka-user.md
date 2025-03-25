# Quản lý Kafka User

## Kafka User là gì?

Kafka user là một thành phần quan trọng trong việc bảo mật và kiểm soát truy cập vào cụm Kafka. Mỗi user đại diện cho một ứng dụng hoặc dịch vụ kết nối đến Kafka để sản xuất hoặc tiêu thụ dữ liệu. Việc quản lý Kafka user cho phép bạn xác định quyền truy cập của từng user vào các topic cụ thể, đảm bảo rằng dữ liệu chỉ được truy cập bởi các ứng dụng được ủy quyền.

**Chức năng và hoạt động của Kafka User**

* **Xác thực (Authentication):** Kafka user cung cấp cơ chế xác thực để xác minh danh tính của ứng dụng hoặc dịch vụ kết nối đến cụm Kafka. Quá trình xác thực thường sử dụng các phương thức như mTLS (Mutual TLS) hoặc SASL (Simple Authentication and Security Layer).
* **Ủy quyền (Authorization):** Sau khi xác thực thành công, Kafka user được cấp quyền truy cập vào các topic cụ thể dựa trên các quyền được gán cho user đó. Các quyền truy cập thông thường bao gồm:
  * **Produce:** Quyền ghi dữ liệu vào một topic.
  * **Consume:** Quyền đọc dữ liệu từ một topic.

## Quản lý Kafka User

vDB Kafka Cluster cung cấp các tính năng quản lý Kafka user toàn diện, giúp bạn dễ dàng tạo, cập nhật quyền, xóa và quản lý chứng chỉ cho các user.

**1. Chọn Cụm Kafka**

* Đăng nhập vào giao diện vDB Kafka Cluster tại đây:
* Từ danh sách các cụm Kafka, chọn cụm mà bạn muốn quản lý user.

**2. Truy cập Phần "Users"**

* Sau khi chọn cụm Kafka, tìm và điều hướng đến phần "Users" trong giao diện quản lý.

**3. Tạo User**

1. Nhấp vào nút "Tạo User".
2. Điền các thông tin sau:
   * **Tên người dùng:** Đặt tên cho Kafka user mới. Tên này nên duy nhất và mô tả rõ ràng ứng dụng hoặc dịch vụ mà user đại diện.
   * **Phân quyền trên topics:** Chọn các topic mà user này có quyền truy cập và cấp các quyền tương ứng (Produce, Consume).
   * **Phương thức truy cập cụm Kafka:** Chọn phương thức xác thực (mTLS hoặc SASL) phù hợp với cấu hình bảo mật của cụm Kafka.
3. Nhấp vào nút "Tạo" để tạo user. Hệ thống sẽ tự động tạo chứng chỉ tương ứng để user sử dụng khi kết nối đến cụm Kafka.
4. Truy cập vào phần chi tiết của user để tải về chứng chỉ.

**4. Cập nhật Quyền (Update Permission)**

1. Trong danh sách các user, tìm user mà bạn muốn cập nhật quyền.
2. Nhấp vào biểu tượng hoặc liên kết "Cập nhật Quyền" tương ứng với user đó.
3. Thêm, xóa hoặc thay đổi các quyền truy cập vào các topic cho user.
4. Nhấp vào nút "Lưu" để áp dụng các thay đổi.

**5. Xóa User**

1. Trong danh sách các user, tìm user mà bạn muốn xóa.
2. Nhấp vào biểu tượng hoặc liên kết "Xóa" tương ứng với user đó.
3. Xác nhận thao tác xóa. Lưu ý rằng việc xóa user sẽ thu hồi tất cả quyền truy cập của user đó vào cụm Kafka.

**6. Tạo lại Chứng chỉ (Re-Generate Certificate)**

1. Trong danh sách các user, tìm user mà bạn muốn tạo lại chứng chỉ.
2. Nhấp vào biểu tượng hoặc liên kết "Tạo lại Chứng chỉ" tương ứng với user đó.
3. Xác nhận thao tác và tải về chứng chỉ mới. Lưu ý rằng chứng chỉ cũ sẽ không còn hiệu lực sau khi tạo lại chứng chỉ mới.

**Kết luận**

Quản lý Kafka user là một phần quan trọng trong việc bảo mật và kiểm soát truy cập vào cụm Kafka của bạn. Bằng cách sử dụng các tính năng quản lý user trong vDB Kafka Cluster, bạn có thể dễ dàng tạo, cập nhật quyền, xóa và quản lý chứng chỉ cho các user, đảm bảo rằng dữ liệu của bạn được bảo vệ và chỉ được truy cập bởi các ứng dụng được ủy quyền.
