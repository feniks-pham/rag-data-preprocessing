# Theo dõi kết quả chạy Transfer Job

Khi Transfer Job của bạn đang chạy hoặc đã chạy hoàn thành, bạn có thể xem chi tiết các thông số của Transfer Job bằng cách:&#x20;

**Bước 1:** Truy cập vào [https://datasync.console.vngcloud.vn/](https://datasync.console.vngcloud.vn/transfer-job/list)

**Bước 2:** Tại menu bên trái, chọn mục **Transfer Job**.&#x20;

**Bước 3:** Trên danh sách các transfer job đã chạy hoặc đang chạy, hãy chọn một **Transfer Job** mà bạn muốn chạy.&#x20;

**Bước 4:** Lúc này, màn hình thông tin chi tiết Transfer Job hiển thị, trong đó:&#x20;

**Bước 4.1: Kiểm tra thông tin tại General information**

1. **Job ID:** ID của job.
2. **Job Description:** mô tả job
3. **Job Schedule:** cấu hình chạy một lần/ lập lịch định kỳ của job.
4. **Source Information:** thông tin nguồn gửi dữ liệu.
5. **Destination Infomation:** thông tin đích nhận dữ liệu.

**Bước 4.2: Kiểm tra thông tin tại Operation**

1. Hiển thị lịch sử các lần chạy của Transfer Job, bao gồm:
   1. **Lastest run**: lần chạy gần nhất trong quá khứ nếu transfer job đang không được chạy hoặc kết quả realtime của lần chạy hiện tại. Trong phần này, bạn có thể xem các thông số bao gồm:
      1. **Status**: trạng thái của lần chạy Transfer Job.&#x20;
      2. **Duration**: tổng thời gian chạy job.
      3. **Start time**: thời gian bắt đầu chạy job.
      4. **End time**: thời gian kết thúc chạy job.
      5. **Progress**: tiến trình chạy job, thông số này sẽ thay đổi realtime theo kết quả thực tế mà transfer job đang chạy.
      6. **Data transferred**: tổng số byte và số file đã thực hiện transfer bởi hệ thống DataSync. Lưu ý: không phải tất cả số byte/ file này đều transfer thành công, trong quá trình transfer có thể xảy ra lỗi tại một hoặc nhiều file. Bạn có thể xem danh sách này tại mục bên dưới.
      7. **Error**: tổng số byte và số file bị lỗi trong quá trình transfer. Bạn có thể thực hiện chạy lại transfer job với danh sách file này theo hướng dẫn tại [Chạy lại Transfer Job](chay-lai-transfer-job.md).
      8. **Data skipper**: tổng số file bị bỏ qua trong quá trình transfer.&#x20;
      9. **Average speed estimate**: băng thông trung bình của hệ thống trong quá trình transfer.
   2. **Run history:** kết quả của những lần chạy trong quá khứ của transfer job. Bạn có thể chọn vào biểu tượng <img src="http://docs.vngcloud.vn/download/thumbnails/73761255/image2024-3-14_10-21-27.png?version=1&#x26;modificationDate=1710386487732&#x26;api=v2" alt="" data-size="line">tại mỗi lần chạy để xem chi tiết kết quả của lần chạy đó. Các thông số hiển thị tương tự như mục Lastest run đã đề cập bên trên.

**Bước 4.3: Kiểm tra thông tin tại Monitor**

1. Hiển thị biểu đồ thống kê về tiến trình transfer dữ liệu. Cứ mỗi 60s thì chúng tôi sẽ thu thập các metric thành 1 điểm dữ liệu, chi tiết bạn có thể thao khảo tại [Làm việc với Metric Information](../../vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/metrics/lam-viec-voi-metruc-information.md) để biết thêm cách làm việc với chúng. Hoặc bạn có thể chọn các khung thời gian để xem biểu đồ tại vùng <img src="http://docs.vngcloud.vn/download/thumbnails/73761255/image2024-3-14_10-26-31.png?version=1&#x26;modificationDate=1710386792108&#x26;api=v2" alt="" data-size="original">.Trên VNG Cloud DataSync, các metric được hiển thị thông qua biểu đồ bao gồm:&#x20;
   * **Data throughput** (byte/s): số byte được truyền tải trên mỗi giây.
   * **File throughput** (file/s): số file được truyền tải trên mỗi giây.
   * **Object transfer error** (file): số file bị lỗi trong quá trình transfer.

**Bước 4.4: Kiểm tra thông tin tại Configuration**

1. Hiển thị thông tin cấu hình của Transfer Job, bao gồm:
   * **Source**: thông tin chi tiết của source bao gồm: Source type, Region, Project name, Bucket name, Endpoint, Folder path, Access key.
   * **Destination**: thông tin chi tiết của destination bao gồm: Destination type, Region, Project name, Container name, Folder path, Access key
   * **Job condition**: Có/ không bật Copy object metadata, Có/ không bật Overwrite, các Tag, Metadata, nơi lưu Job Report, nơi nhận Log, và email nhận Notification của bạn đã thiết lập trên Transfer Job.
