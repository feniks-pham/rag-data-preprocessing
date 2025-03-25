# Sử dụng tính năng Versioning

Versioning là một tính năng hỗ trợ lưu trữ nhiều phiên bản quá khứ của các object được lưu trữ trong một bucket. Với tính năng versioning, bạn có thể dễ dàng quản lý lịch sử các thay đổi của dữ liệu và bảo vệ dữ liệu khỏi mất mát do thao tác nhầm. Bật versioning là một phương pháp hiệu quả để kiểm soát và khôi phục dữ liệu trong các tình huống khẩn cấp.

Để sử dụng tính năng versioning, vui lòng thực hiện theo các bước sau:&#x20;

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** chứa **bucket** bạn muốn thiết lập versioning.

3\. Chọn biểu tượng **Action** và chọn **Configure versioning**

<figure><img src="../../../../../../.gitbook/assets/image (801).png" alt=""><figcaption></figcaption></figure>

4\. Tại màn hình xác nhận bật versioning, vui lòng chọn **Enable versioning**.

<figure><img src="../../../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Sau khi bật versioning, mỗi khi tải lên một object với cùng tên, vStorage sẽ tạo một phiên bản mới cho object đó, và phiên bản cũ vẫn được lưu lại. Bạn có thể chọn Show versions để xem thông tin các version của object

<figure><img src="../../../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

&#x20;Các thao tác phổ biến với versioning bao gồm:

* **Tải lên phiên bản mới của object**: Khi bạn tải lên một file với cùng tên vào bucket đã bật versioning, vStorage sẽ giữ lại các phiên bản trước đó của file này.
* **Xóa phiên bản cụ thể**:
  * Trong bucket đã bật versioning, mỗi object có một "version ID". Để xóa một phiên bản cụ thể, bạn chỉ cần tìm đúng phiên bản của object và chọn xóa.
  * Nếu bạn xóa phiên bản "current", vStorage sẽ giữ lại một bản "delete marker", đánh dấu object là đã xóa nhưng không xóa hẳn các phiên bản cũ.
* **Restore một object version cũ thành current version**: bạn có thể chọn Restore tại version mà bạn muốn restore để đưa phiên bản object này thành phiên bản mới nhất của object.
  * Khôi phục phiên bản cũ không xóa phiên bản hiện tại hoặc bất kỳ phiên bản nào khác.
  * Phiên bản bạn muốn khôi phục sẽ được sao chép làm phiên bản mới nhất, giúp bảo toàn mọi phiên bản trong bucket.
{% endhint %}
