# Backup trong vCloudStack

## Tổng quan

Backup là chức năng sao lưu toàn phần của VNG Cloud, được mang vào dịch vụ vCloudStack giúp bảo vệ dữ liệu của doanh nghiệp, cho phép tự động hoá sao lưu ổ đĩa trên máy chủ ảo và lưu trữ chúng. Khi sử dụng Backup, bạn có thể cấu hình tập trung các chính sách sao lưu và giám sát hoạt động sao lưu cho tài nguyên bao gồm việc tạo các bản sao lưu tự động hàng ngày, hàng tuần và hàng tháng. Mỗi bản sao lưu là một ảnh chụp nhanh dựa trên tệp đầy đủ về ổ đĩa của bạn được thực hiện trong khung thời gian đã lên lịch ưa thích dựa trên các chính sách của bạn trong khi máy chủ ảo vẫn đang chạy. Điều này có nghĩa là dịch vụ Sao lưu không gây gián đoạn và cung cấp cho bạn một số tùy chọn khôi phục hoàn chỉnh. Chức năng Backup tự động hóa và hợp nhất các tác vụ sao lưu từng dịch vụ đã thực hiện trước đó, loại bỏ nhu cầu tạo tập lệnh tùy chỉnh và quy trình thủ công tốn nhiều thời gian, cho phép bạn đáp ứng các yêu cầu tuân thủ về sao lưu theo quy định và kinh doanh của mình.

Dịch vụ vBackup cung cấp cho bạn các chức năng chính bao gồm:

* **Backup:** Tạo bản sao lưu cho các ổ đĩa trên máy chủ ảo của bạn;
* **Restore:** Thực hiện khôi phục từ file backup của máy chủ ảo lên một máy chủ mới tại thời điểm tạo file backup.

{% hint style="info" %}
vCloudStack cung cấp chức năng backup cho phép sao lưu dữ liệu cả trên 2 môi trường:

* Sao lưu trên Cloud (vStorage)
* Sao lưu trên Local (Worker) - đang cập nhật
{% endhint %}

***

### **Tạo bản sao lưu lên vStorage theo bộ lịch Policy**  <a href="#taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicytaigiaodienvbackup" id="taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicytaigiaodienvbackup"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Backup.

**Bước 2:** Chọn **Create Backup Server**;

**Bước 3:** Chọn loại tài nguyên bạn muốn sao lưu, ở đây là danh sách Server và Volume đính kèm với nó

**Bước 4:** Chọn **Policy** bạn muốn áp dụng cho bản sao lưu. Lưu ý bạn cần tạo một Policy để có thể thêm vào cho bản Backup Server của mình. Xem hướng dẫn [tạo chính sách Policy](backup-trong-vcloudstack.md#tao-chinh-sach-policy-sao-luu) ngay bên dưới

**Bước 5:** Nơi lưu trữ mặc định (Backup Location) sẽ nằm tại **vStorage;**

{% hint style="info" %}
**Lưu ý:**

* Khi thực hiện thao tác chọn tài nguyên để tạo bản sao lưu, hệ thống sẽ tính toán và đưa ra kết quả **dự đoán về dung lượng tạo bản sao lưu**, để việc tạo không bị gián đoạn và gặp sự cố cần đảm bảo rằng dung lượng nơi lưu trữ của bạn tại vStorage là đủ dùng.
* Sử dụng dịch vụ vBackup. Trong lần đầu tiên, chúng tôi sẽ tự động tạo một nơi lưu trữ mặc định tại vStorage với dung lượng **miễn phí 50 GB và thời hạn sử dụng 1 tháng**, tuy nhiên để có thể lưu trữ với dung lượng lớn hơn, bạn cần phải mua thêm dung lượng lưu trữ.&#x20;
* Nếu chưa có Backup Location, bạn có thể tạo nơi lưu trữ mặc định tại vStorage bằng cách vào mục Backup Location chọn **Create backup location**, hệ thống se tự động tạo.
{% endhint %}

**Bước 6:** Nhập thông tin **ghi chú** cho các bản sao lưu của bạn để tạo sự gợi nhớ&#x20;

**Bước 7:** Chọn nút **Tạo**&#x20;

**Bước 8:** Sau đó bạn có thể xem thông tin công việc sao lưu vừa tạo tại màn hình danh sách, chọn Backup Server để xem các thông tin về máy ảo được bảo vệ và ổ đĩa đính kèm, chính sách, nơi lưu trữ và kích thước bản sao lưu cũng như thời gian sao lưu gần nhất.

***

## Tạo chính sách policy sao lưu

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack;

**Bước 2**: Tại thanh menu điều hướng, chọn Tab **Backup Policy**

**Bước 3:** Chọn **Tạo Backup Policy**

**Bước 4:** Tại trang tạo Policy, nhập thông tin **Tên Policy** tại mục **Thông tin cơ bản**

**Bước 5:** Sau đó tại mục **Cài đặt chính sách (Policy Configuration)**, lựa chọn **thời gian** và **múi giờ** mà hệ thống sẽ thực hiện sao lưu.

**Bước 6**: Chọn **tần suất sao lưu** phù hợp với nhu cầu sử dụng của bạn theo Hàng Ngày, Hàng Tuần, Hàng Tháng. Lưu ý rằng bạn có thể kết hợp cả 3 với nhau để tạo ra bộ lịch hoàn hảo nhất

**Bước 7**: Nhập **số bản lưu** (Retention) mà hệ thống sẽ lưu giữ các bản sao lưu gần nhất

**Bước 8:** Ngoài ra bạn có thể lựa chọn **tự động sao lưu** cho các **ổ đĩa** được thêm vào máy ảo sau này

**Bước 9:** Chọn **Tạo** , sau đó hệ thống sẽ khởi tạo policy mới bạn vừa tạo

{% hint style="info" %}
**Cách hoạt động của chính sách sao lưu**

Một chính sách sao lưu được lựa chọn tần suất sao lưu theo **Hàng Ngày** lúc **12:00** và số bản lưu **4**. Vào mỗi ngày lúc 12:00 trưa, hệ thống theo khung giờ trên sẽ tạo bản sao lưu cho máy chủ ảo, với lần sao lưu đầu tiên sẽ là bản sao lưu đầy đủ cho máy chủ ảo, vào ngày tiếp theo sẽ sao lưu các phần thay đổi của máy ảo kể từ lần sao lưu cuối của ngày hôm qua, số bản lưu giữ sẽ là 4 bản theo 4 ngày gần nhất.
{% endhint %}

## **Chỉnh sửa chính sách sao lưu** <a href="#tao-chinhsua-xoachinhsachsaoluu-chinhsuachinhsachsaoluu" id="tao-chinhsua-xoachinhsachsaoluu-chinhsuachinhsachsaoluu"></a>

Khi chính sách sao lưu không còn phù hợp với yêu cầu kinh doanh hay quy mô dữ liệu hoặc thời gian phục hồi được yêu cầu nhanh hơn bạn cần chỉnh sửa lại các thông số của chính sách sao lưu

**Quy trình chỉnh sửa chính sách sao lưu:**

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack;

**Bước 2:** Tại thanh menu điều hướng, chọn Tab **Backup Policy**

**Bước 3**: Chọn **Chỉnh sửa Backup Policy**

**Bước 4:** Bạn có thể nhập lại tên chính sách, cũng như thay đổi tất cả các thông số về thời gian, múi giờ sao lưu, cũng như bộ lịch sao lưu, số bản lưu của Chính sách sao lưu mà bạn muốn cập nhật

**Bước 5:** Sau khi cập nhật xong chính sách hay chọn **Lưu** để thay đổi

## **Xóa chính sách sao lưu** <a href="#tao-chinhsua-xoachinhsachsaoluu-xoachinhsachsaoluu" id="tao-chinhsua-xoachinhsachsaoluu-xoachinhsachsaoluu"></a>

Bạn có thể xóa chính sách sao lưu nếu không còn nhu cầu sử dụng nó, nhưng cần lưu ý rằng, bạn không thể xóa chính sách sao lưu mặc định được tạo bởi hệ thống.

**Quy trình xóa chính sách sao lưu:**

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack;

**Bước 2:** Tại thanh menu điều hướng, chọn Tab **Backup Policy**

**Bước 3:** Chọn **Xóa Backup Policy**

**Bước 4:** Sau khi xóa xong chính sách sao lưu sẽ mất khỏi trang danh sách.

***

## Khôi phục bản sao lưu

Sau khi một tài nguyên đã được sao lưu ít nhất một lần, tài nguyên đó được coi là đã được bảo vệ và có sẵn để khôi phục.

Nếu bạn đang khôi phục máy ảo, bạn có thể thực hiện Khôi phục hoàn toàn để khôi phục toàn bộ hệ thống của máy ảo lên một máy ảo mới. Hoặc, bạn có thể khôi phục các ổ đĩa cụ thể thuộc một máy ảo. Làm theo các bước dưới đây để hoàn thực hiện việc khôi phục một máy ảo hoặc ổ đĩa của bạn:

### **Quy trình khôi phục máy chủ ảo** <a href="#khoiphucbansaoluu-quytrinhkhoiphucmaychuao" id="khoiphucbansaoluu-quytrinhkhoiphucmaychuao"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack;

**Bước 2**: Chọn mục Backup

**Bước 3:** Chọn máy chủ ảo được sao lưu và nhấn vào **Restore**

**Bước 4:** Trang tạo mới máy chủ ảo sẽ hiển thị với cấu hình của bản sao lưu, bạn cần chọn các thông số còn lại để hoàn tất việc khôi phục bản sao lưu lên một máy ảo

**Bước 5:** Chọn **tạo mới máy ảo**&#x20;

**Bước 6:** Một máy chủ ảo sẽ tạo ra ở trạng thái **Shutdown** với cấu hình của bản sao lưu mà bạn đã chọn trước đó

### **Quy trình khôi phục ổ đĩa** <a href="#khoiphucbansaoluu-quytrinhkhoiphucodia" id="khoiphucbansaoluu-quytrinhkhoiphucodia"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack;

**Bước 2**: Chọn mục Backup

**Bước 3:** Xem chi tiết máy chủ ảo được sao lưu

**Bước 4:** Tại danh sách ổ đĩa đính kèm với máy ảo, chọn ổ đĩa bạn được sao lưu và nhấn vào **Restore**

**Bước 5:** Trang tạo mới ổ đĩa sẽ hiển thị với cấu hình của bản sao lưu, bạn cần chọn các thông số còn lại để hoàn tất việc khôi phục bản sao lưu lên một ổ đĩa

**Bước 6:** Chọn **tạo mới ổ đĩa**

**Bước 7:** Một ổ đĩa mới được tạo ra với cấu hình của bản sao lưu mà bạn đã chọn trước đó

{% hint style="info" %}
**Lưu ý**

Bất kể bạn thực hiện khôi phục một máy ảo hay ổ đĩa, mỗi lần khôi phục sẽ đều sẽ tạo mới. Nếu bạn thử khôi phục nhiều lần cho cùng một tài nguyên, có thể tồn tại nhiều mục trùng nhau cho tài nguyên đó.
{% endhint %}
