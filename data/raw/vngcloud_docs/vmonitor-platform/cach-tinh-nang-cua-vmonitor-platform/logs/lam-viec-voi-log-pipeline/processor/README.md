# Processor

### Tổng quan

Processor: là những thư viện hỗ trợ bạn parse và enrich dữ liệu, nằm trong Processor Group.

***

### Khởi tạo Processor

Để tạo một processor, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor/).
2. Chọn thư mục **Log**, sau đó chọn menu **Log pipeline**.
3. Chọn một **Log pipeline** đang tồn tại.
4. Tại **Processor group** đang tồn tại và có cấu hình Source và Destination Log project đúng theo mong muốn parser dữ liệu của bạn, chọn **Create a processor.**
5. Tại mục nhập **Processor information**:
   * Nhập **Processor name**. Tên Processor phải tuân thủ theo quy định của chúng tôi, chi tiết tham khảo tại Phạm vi giới hạn Log pipeline.
   * Chọn **Processor type**. Chúng tôi cung cấp cho bạn 6 loại processor type bao gồm:&#x20;
     * [Grok Parser](grok-parser/)
     * [JSON Parser](json-parser.md)
     * [CSV Parser](csv-parser.md)
     * [Field Remapper](field-remapper.md)
     * [Date Parser](date-parser.md)
     * [GEO IP Parser](geo-ip-parser.md)
     * [User-agent Parser](user-agent-parser.md)
   * Nhập **Filter** cho log nếu có. Bạn có thể nhập điều kiện lọc cho log bằng một trong 2 cách: **Suggestion mode** hoặc **Editor mode**. Cách sử dụng 2 phương thức này và chuyển đổi qua lại giữa 2 phương thức đã được chúng tôi mô tả ở các tính năng bên trên, để biết thêm thông tin hãy xem tại [Search logs](../../lam-viec-voi-log-search/search-logs.md).

6\. Tại mục nhập **Parsing rule**, với mỗi Processor type mà bạn lựa chọn hãy làm theo hướng dẫn cụ thể ở mỗi trang bên dưới.

7\. Chọn **Create**.

***

### Chỉnh sửa Processor

Để chỉnh sửa Processor trong Log pipeline, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Log.**
3. Chọn **Log pipeline.**
4. Trong danh sách log pipeline đang có, chọn **Log pipeline** chứa **Processor group và Processor** mà bạn muốn chỉnh sửa.
5. Tại **Processor** mà bạn muốn chỉnh sửa, chọn <img src="../../../../../.gitbook/assets/image (320).png" alt="" data-size="line">
6. Chọn **Edit processor**.
7. Chỉnh sửa các thông số cho **Processor** mà bạn mong muốn. Bạn có thể chỉnh sửa tất cả các trường thông tin trong cấu hình một Processor. Việc chỉnh sửa này tương tự như khi bạn thực hiện tạo mới một Processor theo hướng dẫn bên trên.
8. Chọn **Save.**

***

### Xóa processor

Khi bạn không có nhu cầu sử dụng một Processor tùy chỉnh nữa, bạn có thể thực hiện xóa Processor khỏi hệ thống theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Log.**
3. Chọn **Log pipeline** chứa Processor group và Processor mà bạn muốn thực hiện xóa.
4. Chọn **Processor.**
5. Tại **Processor** mà bạn muốn xóa, chọn <img src="../../../../../.gitbook/assets/image (321).png" alt="" data-size="line">
6. Chọn **Delete**.
7. Tại màn hình xác nhận xóa Processor, chọn **Delete**.

Sau khi bạn thực hiện xóa thành công thì Processor của bạn sẽ bị xóa hoàn toàn khỏi hệ thống của chúng tôi. Bạn không thể khôi phục lại Processor đã xóa nên hãy lưu ý cẩn thận khi sử dụng tính năng này.&#x20;
