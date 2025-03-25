# Làm việc với Log pipeline

### Tổng quan <a href="#lamviecvoilogpipeline-tongquan" id="lamviecvoilogpipeline-tongquan"></a>

Log Pipeline là tính năng cho phép bạn thực hiện parse hay enrich dữ liệu từ dữ liệu không có cấu trúc, không có ý nghĩa (raw log) thành dữ liệu log có ý nghĩa có cấu trúc (ví dụ Json format). Dữ liệu log sẽ được chạy thông qua một chuỗi các Processor Group và Processor. Nếu log đó thoả điều kiện filter ở Processor Group và Processor thì Processor sẽ được thực thi trên các log đó một cách tuần tự cho tới khi kết thúc.

**Thành phần**

* Log Pipeline: chứa các Processor Group cho phép parse hay enrich dữ liệu từ dữ liệu không có cấu trúc, không có ý nghĩa (raw log) thành dữ liệu log có ý nghĩa có cấu trúc (ví dụ Json format)
* Processor Group: cho phép bạn chỉ định nơi lấy dữ liệu log (source log project), nơi lưu trữ dữ liệu đã parse (destination log project) và những log nào sẽ được parse khi thoả mãn filter
* Processor: là những thư viện hỗ trợ bạn parse và enrich dữ liệu, nằm trong Processor Group.

***

### **Mô hình mô tả Log Pipeline**

**Log Pipeline 1**: mô hình cơ bản nhất chỉ có 1 source log project và 1 destination log project với các thông tin như bên dưới, dành cho nhu cầu là raw logs chỉ chứa 1 loại dữ liệu logs và bạn chỉ muốn parse tới 1 destination log project

* Source Log Project: là nơi chứa raw logs, những dữ liệu chưa có cấu trúc mà bạn có nhu cầu cần parse
* Destination Log Project: là nơi chứa structured logs, những dữ liệu đã parse thành có cấu trúc sau khi chạy qua hệ thống Log Pipeline
* Log Pipeline chứa chỉ 1 Processor Group với Filter là source:nginx, nghĩa là với những logs có trường source:nginx thì mới chạy qua hệ thống Processor Group để parse.
* Processor Group chứa 3 Processor để parse log thành dữ liệu có cấu trúc và lưu vào destination log project.

<figure><img src="../../../../.gitbook/assets/image (314).png" alt=""><figcaption></figcaption></figure>

**Log Pipeline 2**: mô hình phức tạp hơn có 1 source log project nhưng dữ liệu parse ra 2 destination log project với các thông tin như bên dưới, dành cho nhu cầu là raw logs của bạn chứa nhiều loại dữ liệu logs khác nhau và bạn muốn parse và lưu trữ ở nhiều destination log project khác nhau

* Source Log Project: là nơi chứa raw logs, những dữ liệu chưa có cấu trúc mà bạn có nhu cầu cần parse
* Destination Log Project: là nơi chứa structured logs, những dữ liệu đã parse thành có cấu trúc sau khi chạy qua hệ thống Log Pipeline, ở đây có 2 destination log project để nhận các log khác nhau ví dụ: destination log project 1 thì nhận dữ liệu nginx logs đã parse, destination log project 2 thì nhận dữ liệu apache logs đã parse
* Log Pipeline chứa 2 Processor Group với Filter là source:nginx và source:apache, tương ứng với dòng logs nào phù hợp với Filter của Group thì sẽ được parse tương ứng với Group đó
* Processor Group: có 2 Processor Groups tương ứng để parse đúng logs về lưu trữ vào 2 destination log project khác nhau.

<figure><img src="../../../../.gitbook/assets/image (315).png" alt=""><figcaption></figcaption></figure>

***

### Phạm vi giới hạn Log pipeline <a href="#lamviecvoilogpipeline-phamvigioihanlogpipeline" id="lamviecvoilogpipeline-phamvigioihanlogpipeline"></a>

#### Quy tắc đặt tên Log pipeline <a href="#lamviecvoilogpipeline-quytacdattenlogpipeline" id="lamviecvoilogpipeline-quytacdattenlogpipeline"></a>

Các quy tắc sau áp dụng cho việc đặt tên Log pipeline trong vMonitor Platform:

* Tên Log pipeline phải dài từ 1 (tối thiểu) đến 63 (tối đa) ký tự.
* Tên Log pipeline chỉ có thể bao gồm các chữ cái viết thường (a-z,), số (0-9), dấu gạch ngang (-).
* Tên Log pipeline phải bắt đầu bởi một chữ cái và kết thúc bởi một chữ cái hoặc một chữ số.
* Tên Log pipeline không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...).&#x20;
* Tên Log pipeline phải là duy nhất trong một tài khoản VNG Cloud cho đến khi Log pipeline đó bị xóa.&#x20;

#### Quy tắc đặt tên Processor group <a href="#lamviecvoilogpipeline-quytacdattenprocessorgroup" id="lamviecvoilogpipeline-quytacdattenprocessorgroup"></a>

Các quy tắc sau áp dụng cho việc đặt tên Processor group trong vMonitor Platform:

* Tên Processor group phải dài từ 1 (tối thiểu) đến 63 (tối đa) ký tự.
* Tên Processor group chỉ có thể bao gồm các chữ cái viết thường (a-z,), số (0-9), dấu gạch ngang (-).
* Tên Processor group phải bắt đầu bởi một chữ cái và kết thúc bởi một chữ cái hoặc một chữ số.
* Tên Processor group không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...).&#x20;
* Tên Processor group phải là duy nhất trong một tài khoản VNG Cloud cho đến khi Processor group đó bị xóa.&#x20;

#### Quy tắc đặt tên Processor <a href="#lamviecvoilogpipeline-quytacdattenprocessor" id="lamviecvoilogpipeline-quytacdattenprocessor"></a>

Các quy tắc sau áp dụng cho việc đặt tên Processor trong vMonitor Platform:

* Tên Processor phải dài từ 1 (tối thiểu) đến 63 (tối đa) ký tự.
* Tên Processor chỉ có thể bao gồm các chữ cái viết thường (a-z,), số (0-9), dấu gạch ngang (-).
* Tên Processor phải bắt đầu bởi một chữ cái và kết thúc bởi một chữ cái hoặc một chữ số.
* Tên Processor không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...).&#x20;
* Tên Processor phải là duy nhất trong một tài khoản VNG Cloud cho đến khi Processor đó bị xóa.&#x20;

***

### Khởi tạo Log pipeline <a href="#lamviecvoilogpipeline-khoitaologpipeline" id="lamviecvoilogpipeline-khoitaologpipeline"></a>

Để tạo một log pipeline, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor/).
2. Chọn thư mục **Log**, sau đó chọn menu **Log pipeline**.
3. Chọn **Create a Log pipeline**.
4. Nhập **Pipeline name**. Tên pipeline phải tuân thủ theo quy định của chúng tôi được mô tả phía trên.
5. Nhập **Pipeline description** nếu có.
6. Chọn **Create.**

***

### Chỉnh sửa Log pipeline <a href="#lamviecvoilogpipeline-chinhsualogpipeline" id="lamviecvoilogpipeline-chinhsualogpipeline"></a>

Để chỉnh sửa một log pipeline, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Log.**
3. Chọn **Log pipeline.**
4. Trong danh sách log pipeline đang có, tại **Log pipeline** mà bạn muốn chỉnh sửa, chọn <img src="../../../../.gitbook/assets/image (316).png" alt="" data-size="line">.
5. Chọn **Edit pipeline**.
6. Chỉnh sửa các thông số cho **Log pipeline** mà bạn mong muốn. Bạn có thể chỉnh sửa tất cả các trường thông tin trong cấu hình một Log pipeline. Việc chỉnh sửa này tương tự như khi bạn thực hiện tạo mới một Log pipeline theo hướng dẫn bên trên.
7. Chọn **Save.**

***

### Xóa Log pipeline <a href="#lamviecvoilogpipeline-xoalogpipeline" id="lamviecvoilogpipeline-xoalogpipeline"></a>

Khi bạn không có nhu cầu sử dụng một Log pipeline tùy chỉnh nữa, bạn có thể thực hiện xóa Log pipeline khỏi hệ thống theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Log.**
3. Tại **Log pipeline** bạn muốn thực hiện xóa, chọn <img src="../../../../.gitbook/assets/image (317).png" alt="" data-size="line">
4. Chọn **Delete**.
5. Tại màn hình xác nhận xóa Log pipeline, chọn **Delete**.

Sau khi bạn thực hiện xóa thành công thì Log pipeline của bạn sẽ bị xóa hoàn toàn khỏi hệ thống của chúng tôi. Bạn không thể khôi phục lại Log pipeline đã xóa nên hãy lưu ý cẩn thận khi sử dụng tính năng này.&#x20;
