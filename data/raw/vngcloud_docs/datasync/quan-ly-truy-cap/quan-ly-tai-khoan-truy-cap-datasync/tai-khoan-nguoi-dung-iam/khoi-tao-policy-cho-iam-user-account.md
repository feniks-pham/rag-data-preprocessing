# Khởi tạo policy cho IAM User Account

Để khởi tạo một policy sử dụng để truy cập vào tài nguyên DataSync, hãy làm theo các bước bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **Policy**.&#x20;
3. Chọn **Create a Policy**.
4. Nhập **Name** và **Description** nếu cho cho Policy.
5. Chọn **Next step**.
6. Chọn **Product là DataSync**.
7. Chọn **Actions**:
   1. Chọn **Allow permissions**: mặc định hệ thống vIAM sẽ luôn bật tức là cho phép quyền hạn được áp dụng trên policy. Nếu bạn tắt mode này thì hệ thống sẽ từ chối (đảo chiều) quyền hạn tương ứng.
      1. **Allow permissions**: cho phép truy cập theo action đã chọn.&#x20;
      2. **Deny permissions**: từ chối truy cập theo action đã chọn.
   2. Chọn **All DataSync actions** nếu muốn tạo policy có quyền thực hiện tất cả các hành động trên DataSync. Chi tiết ý nghĩa của các action vui lòng tham khảo tại [Tính năng, tài nguyên DataSync và quyền truy cập](../../quan-ly-truy-cap-tai-nguyen-datasync/tinh-nang-tai-nguyen-datasync-va-quyen-truy-cap.md).
8. Chọn **Resources**:
   1. Chọn **All resources** nếu muốn quyền truy cập đã chọn bên trên được phép truy cập vào mọi tài nguyên trên tài khoản SSO account của bạn.&#x20;
   2. Chọn **Specify resources**: chọn project, container, object cụ thể mà bạn muốn cho phép truy cập tới. Bạn có thể nhập thông tin cho mỗi loại resources này bằng 1 trong những cách sau:&#x20;
      1. **Nhập \*** nếu bạn muốn chọn tất cả tài nguyên.
      2. **Nhập cụ thể ID của project, tên của container, tên của object** nếu bạn muốn chỉ định tới chính xác project, container, object đó.&#x20;
      3. **Nhập tiền tố (prefix)** nếu bạn muốn chỉ định tới một tập project, container, object được bắt đầu bằng tiền tố đã khai báo.&#x20;
   3. Bạn cũng có thể chọn **Any** để cho phép truy cập tới mọi project, container, object trong tài khoản SSO account của bạn.&#x20;
   4. Chọn **Request conditions:** nhập điều kiện đặc biệt cho policy nếu có.&#x20;

Sau khi bạn thực hiện 8 bước bên trên, policy cho DataSync đã được khởi tạo. Tiếp theo, bạn hãy gán nó vào IAM User Account theo hướng dẫn tại [Liên kết tài khoản IAM User Account với policy tương ứng](../../../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-nguoi-dung-iam/lien-ket-tai-khoan-iam-user-account-voi-policy-tuong-ung.md).

Ngoài các bước tạo policy đặc thù cho riêng bạn như trên, chúng tôi cũng cung cấp cho bạn một tập các policy mặc định với các quyền hạn đa dạng. Bạn có thể sử dụng tập policy này và liên kết trực tiếp chúng tới tài khoản IAM User Account. Để biết thêm thông tin về danh sách policy mặc định, tham khảo tại [Tính năng, tài nguyên DataSync và quyền truy cập](../../quan-ly-truy-cap-tai-nguyen-datasync/tinh-nang-tai-nguyen-datasync-va-quyen-truy-cap.md).
