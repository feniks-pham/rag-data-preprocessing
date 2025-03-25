# Khởi tạo Transfer Job

Nếu bạn chưa sử dụng bất kỳ dịch vụ nào của VNG Cloud (chưa đăng ký tài khoản sử dụng với VNG Cloud), bạn cần đăng ký tài khoản với VNG Cloud Service [tại đây](https://register.vngcloud.vn/signup) để truy cập đến VNGCloud DataSync.

Bắt đầu sử dụng dịch vụ, bạn cần tạo một transfer job. Trong DataSync, transfer job là một nhiệm vụ được cấu hình để transfer dữ liệu giữa nguồn và đích. Tại một thời điểm bạn có thể sở hữu một hoặc nhiều Transfer job song song và sử dụng chúng với các mục đích khác nhau.

**Để sử dụng DataSync, bạn cần thực hiện các bước sau:**

**Bước 1:** Đăng nhập vào [https://datasync.console.vngcloud.vn/](https://datasync.console.vngcloud.vn/). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [đây](https://register.vngcloud.vn/signup).

**Bước 2:** Nhấp vào nút **Create a transfer job** để bắt đầu tạo job chuyển đổi dữ liệu.

**Bước 3:** Nhập **Basic configuration,** bao gồm:&#x20;

1. Nhập **Job name.** Tên job là duy nhất trên một SSO User Account và tên job có thể dài từ tối thiểu 5 tới 50 ký tự.
2. Nhập **Job description**: mô tả ngắn gọn về job.&#x20;
3. Chọn **Source Type** bạn muốn chuyển dữ liệu. VNG Cloud DataSync hiện hỗ trợ 4 loại nguồn:
   * Amazon S3
   * Google Cloud Storage
   * S3 compatible object storage
   * vStorage
4. **Destination type**: hiện tại chúng tôi chỉ hỗ trợ 1 loại đích nhận dữ liệu là vStorage.

**Bước 4:** Nhập **Source configuration**, bao gồm:&#x20;

**Bước 4.1:** Tại ô **Source Information**, bấm **Chọn**. Nếu bạn chọn **Source type** là **vStorage** thì bạn có thể chọn thông tin nguồn trong danh sách được hiển thị sẵn mà chúng tôi cung cấp, nếu khác loại này thì phải nhập thông tin. Cụ thể, với loại nguồn:

1. **Amazon S3**, bạn cần:
   1. Chọn một **Region** trong danh sách Region đang được hỗ trợ bởi Amazon.
   2. Nhập **Bucket**: nhập tên bucket nguồn của bạn trên Amazon S3.
   3. Nhập **Folder path**: nếu bạn chỉ muốn chuyển dữ liệu của một folder trong bucket, hãy nhập đường dẫn folder vào mục này. Ví dụ:
      * Để chuyển dữ liệu từ bucket01/folder01/subfolder02 tới vStorage, bạn cần nhập folder01/subfolder02.
      * Để chuyển toàn bộ dữ liệu trong bucket01, hãy để mục này trống.
   4. Nhập **Access Key/ Secret Key**: nhập access key và secret key của bạn.&#x20;
2. **Google Cloud Storage**, bạn cần:
   1. Nhập **Bucket**: nhập tên bucket nguồn của bạn trên Google Cloud Storage.
   2. Nhập **Folder path**: nếu bạn chỉ muốn chuyển dữ liệu của một folder trong bucket, hãy nhập đường dẫn folder vào mục này. Ví dụ:
      * Để chuyển dữ liệu từ bucket01/folder01/subfolder02 tới vStorage, bạn cần nhập folder01/subfolder02.
      * Để chuyển toàn bộ dữ liệu trong bucket01, hãy để mục này trống.
   3. Nhập **Access Key/ Secret Key:** nhập access key và secret key của bạn.&#x20;
3. **S3 compatible Object Storage**, bạn cần:
   1. Nhập **Region**: nơi chứa bucket của bạn. Ví dụ: ap-southeast-1 (Singapore), us-east-1 (Ohio), v.v.
   2. Nhập **Bucket**: tên bucket nguồn của bạn trên S3 compatible Object Storage.
   3. Nhập **Endpoint**: endpoint của S3 compatible Object Storage bạn đang sử dụng. Ví dụ: [https://s3.example.com](https://s3.example.com/).
   4. Nhập **Folder path**: nếu bạn chỉ muốn chuyển dữ liệu của một folder trong bucket, hãy nhập đường dẫn folder vào mục này. Ví dụ:
      * Để chuyển dữ liệu từ bucket01/folder01/subfolder02 tới vStorage, bạn cần nhập folder01/subfolder02.
      * Để chuyển toàn bộ dữ liệu trong bucket01, hãy để mục này trống.
   5. Nhập **Access Key/ Secret Key**: nhập access key và secret key của bạn.
4. **vStorage**, bạn cần:
   1. Chọn **Region**: nơi chứa container của bạn. Ví dụ: HCM03, HAN01
   2. Chọn **Project**: project chứa container mà bạn muốn transfer dữ liệu.&#x20;
   3. Chọn **Container**: tên container nguồn của bạn trên vStorage.
   4. Chọn **Folder path**: nếu bạn chỉ muốn chuyển dữ liệu của một folder trong container, hãy chọn folder bạn muốn transfer dữ liệu tại mục này. Ví dụ:
      * Để chuyển dữ liệu từ container01/folder01/subfolder02 tới vStorage, bạn cần chọn folder01 sau đó chọn tiếp tới subfolder02.
      * Để chuyển toàn bộ dữ liệu trong container01, hãy để mục này trống.
   5. Nhập **Access Key/ Secret Key**: nhập access key và secret key của bạn. Cặp S3 key này được tạo và quản lý thông qua IAM, vui lòng tham khảo tại [IAM cho vStorage](../../identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/iam-cho-vstorage.md).

**Bước 4.1:** Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 4.3:** Tại **Data Filtering**. Nhấn vào từng ô để chọn kiểu lọc dữ liệu bạn mong muốn. Việc filter nhằm mục đích chỉ di chuyển những object bạn thực sự cần cũng như Tiết kiệm thời gian và băng thông và tránh di chuyển những object không mong muốn. Hiện tại, chúng tôi cung cấp hai loại filter để bạn có thể chọn lọc object muốn di chuyển:

1. Filter Exclude Prefix (**Chọn object không được transfer dựa trên prefix**): loại trừ những object **không phù hợp** với các điều kiện được chỉ định khỏi quá trình di chuyển.
2. Filter Include Prefix (**Chọn object được transfer dựa trên prefix**): chỉ di chuyển những object **phù hợp** với các điều kiện được chỉ định.

**Bước 5:** Nhập **Destination configuration**, bao gồm:

**Bước 5.1:** Tại ô **Destination Information**, bấm Chọn. Nhập Cấu hình đích, bao gồm: &#x20;

1. Chọn **Region**: nơi chứa container của bạn. Ví dụ: HCM03, HAN01
2. Chọn **Project**: project chứa container mà bạn muốn transfer dữ liệu.&#x20;
3. Chọn **Container**: tên container nguồn của bạn trên vStorage.
4. Chọn **Folder path**: nếu bạn chỉ muốn chuyển dữ liệu của một folder trong container, hãy chọn folder bạn muốn transfer dữ liệu tại mục này. Ví dụ:
   * Để chuyển dữ liệu từ container01/folder01/subfolder02 tới vStorage, bạn cần chọn folder01 sau đó chọn tiếp tới subfolder02.
   * Để chuyển toàn bộ dữ liệu trong container01, hãy để mục này trống.
5. Nhập **Access Key/ Secret Key**: nhập access key và secret key của bạn. Cặp S3 key này được tạo và quản lý thông qua IAM, vui lòng tham khảo tại [IAM cho vStorage](../../identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/iam-cho-vstorage.md).

**Bước 5.2:** Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 6:** Nhập **Job condition**, bao gồm:

**Bước 6.1: Copy metadata, Add new tag hoặc Add new metdata**

1. Tại **Copy Metadata** của object: chọn nếu bạn muốn giữ nguyên thông tin mô tả, thuộc tính của dữ liệu.
2. Hoặc bạn có thể gắn tag hoặc metadata mới cho toàn bộ dữ liệu di chuyển bằng cách chọn **Advanced configuration.**
   1. **Trường hợp 1: Gắn thêm tag**: bạn cần nhập tag bạn muốn gán cho cho toàn bộ object được transfer sau đó chọn **Add**. Lặp lại bước trên để gán nhiều tag vào các object nàỳ.
   2. **Trường hợp 2: Gắn thêm metadata**: bạn cần nhập metadata theo cấu trúc key:value mà bạn muốn gán cho cho toàn bộ object được transfer sau đó chọn **Add**. Trong đó:
      1. **Default key (Key mặc định)**: thực hiện chọn key trong danh sách key có sẵn mà chúng tôi cung cấp.
      2. **Custom key (Key tùy chỉnh)**: thực hiện tự tạo key tùy chỉnh theo nhu cầu của bạn với tiền tố X-Object-Meta-Vng-.Thêm metadata: chọn 1 trong 2 loại key.
      3. Bạn nhập giá trị **Value** tương ứng với **Key** được chọn hoặc được tạo. Chọn **biểu tượng Add.**

**Bước 6.2:** Tại **Choose when to overwrite**: xác định hành động khi dữ liệu đích đã tồn tại:

1. Không chọn **Overwrite file**: Giữ nguyên dữ liệu đích.
2. Có chọn **Overwrite file**: Thay thế dữ liệu đích bằng dữ liệu nguồn.

**Bước 6.3:** Tại **Choose when to run**: chọn 1 trong 2 phương án

1. **One time (Chạy một lần)**: bạn chọn 1 ngày giờ cụ thể trong tương lai để thực hiện chạy transfer job.
2. **Run schedule (Chạy lập lịch): bạn chọn thời gian bắt đầu, thời gian kết thúc và chu kỳ chạy lập lịch. Cụ thể:**
   1. Chọn **Daily** và nhập thời gian bắt đầu, thời gian kết thúc. Ví dụ bạn chọn ngày bắt đầu là 01/01/2024 08:00 và ngày kết thúc là 31/01/2024 thì hằng ngày vào 08:00 transfer job sẽ được chạy. Để đảm bảo dữ liệu chính xác, chỉ chạy transfer job ngày hôm sau khi transfer job chạy ngày hôm trước đã hoàn thành.
   2. Chọn **Weekly** và nhập thời gian bắt đầu, thời gian kết thúc. Ví dụ bạn chọn ngày bắt đầu là 01/01/2024 08:00 và ngày kết thúc là 31/01/2024 thì định kỳ vào 08:00 các ngày 01/01/2024, 08/01/2024, 15/01/2024, 22/01/2024, 29/01/2024 transfer job sẽ được chạy. Để đảm bảo dữ liệu chính xác, chỉ chạy transfer job tuần kế tiếp khi transfer job chạy ngày tuần trước đó đã hoàn thành.
   3. Chọn **Monthly** và nhập thời gian bắt đầu, thời gian kết thúc. Ví dụ bạn chọn ngày bắt đầu là 01/01/2024 08:00 và ngày kết thúc là 31/03/2024 thì định kỳ vào 08:00 các ngày 01/01/2024, 01/02/2024, 01/03/2024 transfer job sẽ được chạy. Để đảm bảo dữ liệu chính xác, chỉ chạy transfer job tuần kế tiếp khi transfer job chạy ngày tuần trước đó đã hoàn thành.

**Bước 6.4:** Tại **Job Report**: xem báo cáo chi tiết về quá trình transfer dữ liệu:

1. **Report type**: **Summary** hoặc **Standard**
   1. Nếu bạn chọn **Report type** là Summary thì bạn không cần chọn **Report level.**
   2. Nếu bạn chọn **Report type** là **Standard** thì bạn có thể chọn **Report level** là **Successful**, **Failed** hoặc cả **Successful và Failed.**
2. Chọn Container chứa các report: mặc định là container đích nhận dữ liệu di chuyển của bạn. Bạn có thể thay đổi sang các container khác bằng cách
   1. Chọn **Region**: nơi chứa container của bạn. Ví dụ: HCM03, HAN01
   2. Chọn **Project**: project chứa container mà bạn muốn transfer dữ liệu.&#x20;
   3. Chọn **Container**: tên container nguồn của bạn trên vStorage.
   4. **Access Key/ Secret Key**: nhập access key và secret key của bạn. Cặp S3 key này được tạo và quản lý thông qua IAM, vui lòng tham khảo tại [IAM cho vStorage](../../identity-and-access-management-iam/cach-phan-quyen-iam-cho-dich-vu-vng-cloud/iam-cho-vstorage.md).
3. Sau khi nhập đẩy đủ thông tin tại các mục bên trên, bạn có thể chọn kiểm tra kết nối bằng cách nhấn vào nút **Test connection**. Lúc này, hệ thống của chúng tôi sẽ kiểm tra tính hợp lệ của thông tin và hiển thị kết quả. Nếu kết nối thành công, bạn sẽ nhận được thông báo "**Connection successful**". Nếu kết nối thất bại, bạn sẽ nhận được thông báo lỗi và mô tả chi tiết về lỗi.

**Bước 6.5:** Chọn **Logging Option** nếu bạn muốn đẩy log transfer về hệ thống vMonitor Platform. Để có thể thực hiện đẩy log, bạn cần tối thiểu 1 log project trên hệ thống vMonitor Platform. Chi tiết tham khảo tại [Làm việc với Log Project](../../vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/logs/lam-viec-voi-log-project/).

**Bước 6.6:** Chọn **Notification Option** để gửi thông báo tới Email bạn mong muốn khi một transfer job chạy hoàn thành. Bạn có thể nhập email theo đúng định dạng và chọn biểu tượng **Add**.

**Bước 7:** Chọn **Create Transfer Job.**

{% hint style="info" %}
**Chú ý:**

* Nếu bạn gặp lỗi khi kết nối, vui lòng kiểm tra lại thông tin S3 key và endpoint của bạn.
* Tham khảo tài liệu hướng dẫn của nhà cung cấp S3 compatible Object Storage để lấy thông tin chi tiết về cách thiết lập quyền truy cập cho cặp S3 key.
* Bạn có thể sử dụng kết hợp cả filter include và filter exclude để lọc object.
* Thứ tự ưu tiên: Filter include được áp dụng trước filter exclude.\

{% endhint %}
