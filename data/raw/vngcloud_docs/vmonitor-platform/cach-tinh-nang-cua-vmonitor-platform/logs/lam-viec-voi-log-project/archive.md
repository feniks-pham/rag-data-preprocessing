# Archive

Mặc định khi mua gói Log Project, tuỳ vào gói mà bạn mua sẽ có Log Retention khác nhau như: 1 ngày, 7 ngày, 14 ngày, 30 ngày hoặc 90 ngày. Log Retention được chúng tôi định nghĩa là thời hạn lưu trữ log, nếu dòng log có thời gian nằm ngoài Log Retention sẽ được hệ thống chúng tôi xoá đi.

Nếu bạn có nhu cầu lưu trữ dữ liệu log lâu dài hơn những thời gian này, bạn có thể sử dụng tính năng Log Archive để đồng bộ dữ liệu sang vStorage để lưu trữ lâu dài. bạn có thể theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Log**.
3. Chọn **Log project.**
4. Chọn tên **log project** mà bạn muốn thực hiện **Archive**.
5. Tại màn hình hiển thị thông tin **Log** **project**, tại tab **Archive**, chọn **Archive**.
6. Nhập **Archive name** theo quy định của chúng tôi. **Tên Archive** phải dài từ 1 (tối thiểu) tới 63 (tối đa) ký tự. **Tên Archive** có thể bao gồm chữ cái in hoa, in thường (a-z, A-Z), chữ số (0-9) hoặc dấu gạch ngang. **Tên Archive** phải bắt đầu bởi một chữ cái và kết thúc bởi một chữ cái hoặc một chữ số.

<figure><img src="../../../../.gitbook/assets/image (159).png" alt=""><figcaption></figcaption></figure>

7\. Nhập **Filter** cho log nếu bạn có nhu cầu chỉ đồng bộ những dữ liệu mà thoả mãn điều kiện này, còn không chúng tôi sẽ đồng bộ tất cả Log của Log Project đang chọn. Bạn có thể nhập điều kiện lọc cho log bằng một trong 2 cách: **Suggestion mode** hoặc **Editor mode**. Cách sử dụng 2 phương thức này và chuyển đổi qua lại giữa 2 phương thức đã được chúng tôi mô tả ở các tính năng bên trên, để biết thêm thông tin hãy xem tại [Log search](../../dashboard/widget/log-search.md).

8\. Chọn **Destination**. Bạn có thể chọn 1 trong 2 nơi dữ liệu log được archive bao gồm: **vStorage container** hoặc **S3 compatible**.&#x20;

<figure><img src="../../../../.gitbook/assets/image (160).png" alt=""><figcaption></figcaption></figure>

* **Select a vStorage container**

<details>

<summary>My container</summary>

9\. Chọn **My container** nếu bạn muốn chọn vStorage container đang thuộc sở hữu của tài khoản hiện tại. Hoặc chọn **Custom container** nếu bạn muốn chọn vStorage container không thuộc sở hữu của tài khoản hiện tại.

10\. Chọn một **Region**. Nếu bạn muốn xem lại thông tin **Region** và các **vStorage project** cũng như **vStorage container** bạn đang có trên hệ thống vStorage, hãy chọn tại **Click here to visit vStorage.**

11\. Chọn một **vStorage project** trong danh sách các project mà bạn đang có tại **Region** đã chọn trước đó trên hệ thống vStorage. Nếu cần cập nhập danh sách vStorage project hiện tại, hãy chọn **Reload** để cập nhập mới nhất.

12\. Chọn một **vStorage container** trong danh sách các container mà bạn đang có tại **project** đã chọn trước đó trên hệ thống vStorage. Nếu cần cập nhập danh sách vStorage container hiện tại, hãy chọn **Reload** để cập nhập mới nhất.

13\. Nhập **Access key** và **Secret key** để xác thực thông tin kết nối tới hệ thống vStorage. Bạn có thể tìm thấy **Access key** và **Secret key** theo hướng dẫn tại [Service Account](../../../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/) và [Truy cập tài nguyên sử dụng tài khoản Service Account](../../../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-truy-cap-tai-nguyen-vstorage/truy-cap-tai-nguyen-su-dung-tai-khoan-service-account.md).

14\. Chọn **Select**.

<img src="../../../../.gitbook/assets/image (309).png" alt="" data-size="original">

</details>

<details>

<summary>Custom container</summary>



</details>
