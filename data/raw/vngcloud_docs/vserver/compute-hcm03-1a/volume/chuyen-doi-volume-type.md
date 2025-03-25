# Chuyển đổi Volume Type

Tính năng này cho phép người dùng chuyển đổi loại volume từ SSD (Solid State Drive) sang NVME (Non-Volatile Memory Express) và ngược lại, nhằm tối ưu hóa hiệu suất lưu trữ dữ liệu trên hệ thống.&#x20;

## Mục đích sử dụng

Việc chuyển đổi giữa 2 loại volume trên nhằm mục đích:

### **Chuyển từ SSD sang NVMe**

1. **Tăng Tốc Độ Truy Cập Dữ Liệu:** Khi ứng dụng hoặc các công việc yêu cầu tốc độ truy cập dữ liệu cao, chuyển từ SSD sang NVMe có thể cải thiện hiệu suất và giảm thời gian đáp ứng.
2. **Cần Xử Lý Dữ Liệu Lớn:** Khi bạn làm việc với các tập tin dữ liệu lớn hoặc phải xử lý dữ liệu trong thời gian ngắn, NVMe có thể cung cấp tốc độ đọc/ghi dữ liệu nhanh hơn, giúp tăng cường hiệu suất làm việc.
3. **Yêu Cầu Cao Về Latency:** Các ứng dụng như cơ sở dữ liệu, máy chủ ảo, hoặc các ứng dụng yêu cầu thời gian đáp ứng thấp hơn có thể được hưởng lợi từ việc sử dụng NVMe.

### **Chuyển từ NVMe sang SSD**

1. **Giảm Chi Phí:** Trong một số trường hợp, sử dụng SSD thay vì NVMe có thể giúp giảm chi phí vận hành hệ thống mà vẫn đảm bảo hiệu suất lưu trữ đủ đáng tin cậy.
2. **Ứng Dụng Không Yêu Cầu Tốc Độ Cao:** Khi các ứng dụng hoặc công việc không đòi hỏi tốc độ truy cập dữ liệu cực kỳ cao, việc chuyển từ NVMe sang SSD có thể không làm ảnh hưởng đến hiệu suất làm việc mà vẫn giảm chi phí.
3. **Dự Phòng Dữ Liệu:** Sử dụng SSD thay vì NVMe trong các tình huống không đòi hỏi tốc độ cực cao cũng có thể giúp dự phòng dữ liệu với chi phí thấp hơn.

## Tình huống sử dụng

Trước khi bắt đầu, người dùng cần điểm qua một vài lưu ý quan trọng như sau:

* Quá trình chuyển đổi có thể mất một khoảng thời gian nhất định tùy thuộc vào kích thước và trạng thái của volume.
* Quá trình chuyển đổi sẽ gồm 4 bước, yêu cầu sự tương tác giữa người dùng giữa các bước. Do đó, vui lòng chú ý thực hiện mọi hành động cần thiết giữa các bước để tiếp tục việc chuyển đổi volume.

### **Chuyển từ SSD sang NVMe**

Tham khảo hướng dẫn chi tiết bên dưới để thực hiện chuyển đổi ổ đĩa từ SSD sang NVMe

**Bước 0: Cấu hình các thông tin cần chuyển đổi:**

* 0.1: Truy cập danh sách volume từ portal [tại đây.](https://hcm-3.console.vngcloud.vn/vserver/block-store/volumes)
* 0.2: Điều hướng tới volume cần chuyển đổi, nhấn chọn **biểu tượng ba chấm** tại cột **Hành động** ![](<../../../.gitbook/assets/image (286).png>)
* 0.3: Tiếp tục nhấn chọn **Migrate Volume**
* 0.4: Tại của sổ chọn thông tin để Migrate, chọn các thông tin sau:
  * Loại: mặc định chọn NVME
  * Kích thước: Dung lượng hiện tại, không được phép thay đổi
  * IOPS: Cho phép thay đổi, chọn IOPS theo nhu cầu.
* 0.5: Nhấn xác nhận đồng ý xóa các bản snapshot của volume được chuyển đổi sau khi thành công. Sau đó nhấn **Migrate.**

**Bước 1: Khởi tạo quá trình Migrate (không downtime)**

* Hệ thống tạo một volume mới với cấu hình đã chọn ở bước 0.4, sau đó sao lưu dữ liệu từ volume hiện tại sang volume mới.&#x20;
* Thời gian xử lý tùy vào kích thước và cấu hình từng volume. Ở bước này, người dùng vẫn có thể ghi dữ liệu trên volume mà không hề xảy ra downtime.&#x20;

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 2: Khởi tạo diff Migrate (Có downtime)**

_Mục đích của bước này là để sao lưu dữ liệu được ghi mới/thay đổi trong khoảng thời gian thực hiện bước 1._

* 2.1: Sau khi hoàn tất bước 1, giao diện thực hiện sẽ chuyển sang bước 2/4, và yêu cầu người dùng tương tác. Tham khảo hình minh họa sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 2.2: Nhấn chọn **Yêu cầu hành động** để tiếp tục quá trình Migrate. Một cửa sổ Migrate volume sẽ hiển thị, nhấn **Tiếp tục** để xác nhận thực hiện. Quá trình này sẽ gây gián đoạn dịch vụ trên volume hiện tại, thời gian gián đoạn sẽ tùy thuộc vào độ lớn dữ liệu thay đổi trong khoảng thời gian thực hiện bước 1. Trạng thái Migrate sẽ hiển thị như sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

_<mark style="color:orange;">**Trường hợp volume đang được sử dụng trong máy ảo (server), người dùng buộc phải thực hiện Tắt Server để có thể nhấn chon Tiếp tục Migrate.**</mark>_&#x20;

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 3: Xác nhận sử dụng volume hoàn tất chuyển đổi**

* 3.1: Sau khi hoàn tất bước 1, giao diện thực hiện sẽ chuyển sang bước 3/4, và yêu cầu người dùng tương tác. Tham khảo hình minh họa sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 3.2: Nhấn chọn **Yêu cầu hành động,** một cửa sổ Migrate volume sẽ hiển thị, cho phép người dùng xác nhận 2 hành động sau:
  * 3.2.1: **Xóa volume cũ**: Hệ thống sẽ hoàn tất cập nhật volume mới, các dịch vụ trên volume hoạt động lại như thường. Lưu ý rằng các bản snapshot liên quan tới volume trước khi cập nhật sẽ bị xóa vĩnh viễn.
  * 3.2.2: **Phục hồi**: Khôi phục lại trạng thái volume như trước khi migrate. Dữ liệu trên volume sẽ được cập nhật đến thời điểm trước khi khởi tạo diff migrate (bước 2).

### **Chuyển từ NVMe sang SSD**

Tham khảo hướng dẫn chi tiết bên dưới để thực hiện chuyển đổi ổ đĩa từ NVMe sang SSD

**Bước 0: Cấu hình các thông tin cần chuyển đổi:**

* 0.1: Truy cập danh sách volume từ portal [tại đây.](https://hcm-3.console.vngcloud.vn/vserver/block-store/volumes)
* 0.2: Điều hướng tới volume cần chuyển đổi, nhấn chọn **biểu tượng ba chấm** tại cột **Hành động** ![](<../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)
* 0.3: Tiếp tục nhấn chọn **Migrate Volume**&#x20;
* 0.4: Tại của sổ chọn thông tin để Migrate, chọn các thông tin sau:
  * Loại: mặc định chọn NVME
    * Kích thước: Dung lượng hiện tại, không được phép thay đổi
    * IOPS: Cho phép thay đổi, chọn IOPS theo nhu cầu.
* 0.5: Nhấn xác nhận đồng ý xóa các bản snapshot của volume được chuyển đổi sau khi thành công. Sau đó nhấn **Migrate.**

**Bước 1: Khởi tạo quá trình Migrate (không downtime)**

* Hệ thống tạo một volume mới với cấu hình đã chọn ở bước 0.4, sau đó sao lưu dữ liệu từ volume hiện tại sang volume mới.&#x20;
* Thời gian xử lý tùy vào kích thước và cấu hình từng volume. Ở bước này, người dùng vẫn có thể ghi dữ liệu trên volume mà không hề xảy ra downtime.&#x20;

<figure><img src="../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 2: Khởi tạo diff Migrate (Có downtime)**

_Mục đích của bước này là để sao lưu dữ liệu được ghi mới/thay đổi trong khoảng thời gian thực hiện bước 1._

* 2.1: Sau khi hoàn tất bước 1, giao diện thực hiện sẽ chuyển sang bước 2/4, và yêu cầu người dùng tương tác. Tham khảo hình minh họa sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 2.2: Nhấn chọn **Yêu cầu hành động** để tiếp tục quá trình Migrate. Một cửa sổ Migrate volume sẽ hiển thị, nhấn **Tiếp tục** để xác nhận thực hiện. Quá trình này sẽ gây gián đoạn dịch vụ trên volume hiện tại, thời gian gián đoạn sẽ tùy thuộc vào độ lớn dữ liệu thay đổi trong khoảng thời gian thực hiện bước 1. Trạng thái Migrate sẽ hiển thị như sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

_<mark style="color:orange;">**Trường hợp volume đang được sử dụng trong máy ảo (server), người dùng buộc phải thực hiện Tắt Server để có thể nhấn chon Tiếp tục Migrate.**</mark>_&#x20;

<figure><img src="../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 3: Xác nhận sử dụng volume hoàn tất chuyển đổi**

* 3.1: Sau khi hoàn tất bước 1, giao diện thực hiện sẽ chuyển sang bước 3/4, và yêu cầu người dùng tương tác. Tham khảo hình minh họa sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (436).png" alt=""><figcaption></figcaption></figure>

* 3.2: Nhấn chọn **Yêu cầu hành động,** một cửa sổ Migrate volume sẽ hiển thị, cho phép người dùng xác nhận 2 hành động sau:
  * 3.2.1: **Xóa volume cũ**: Hệ thống sẽ hoàn tất cập nhật volume mới, các dịch vụ trên volume hoạt động lại như thường. Lưu ý rằng các bản snapshot liên quan tới volume trước khi cập nhật sẽ bị xóa vĩnh viễn.
  * 3.2.2: **Phục hồi**: Khôi phục lại trạng thái volume như trước khi migrate. Dữ liệu trên volume sẽ được cập nhật đến thời điểm trước khi khởi tạo diff migrate (bước 2).
