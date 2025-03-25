# Volume trong vCloudStack

## Tổng quan

Volume là đối tượng trong môi trường ảo hoá chịu trách nhiệm cung cấp lưu trữ dạng khối (block) cho các Server với tính sẵn sàng và hiệu năng cao. Bạn có thể sử dụng Volume để lưu trữ dữ liệu và các ứng dụng hoặc có thể đính kèm một hoặc nhiều Volume vào một Server trong khi tạo Server hoặc sau đó khi Server đang chạy, ngoài ra bạn cũng có thể gỡ bỏ nó ra khỏi Server và gắn vào một Server khác.

### **Thông tin cơ bản** <a href="#volume-thongtincoban" id="volume-thongtincoban"></a>

Khi sử dụng volume, các thông tin cần lưu ý sau:

* Dung lượng tối đa cho một volume là 1TB
* Một volume nếu không có thuộc tính multi-attach chỉ có thể được gắn vào một máy chủ ảo tại bất kỳ thời điểm nào. Một volume có thuộc tính multi-attach có thể gắn vào nhiều máy chủ ảo đồng thời. Thuộc tính multi-attach có thể được chọn lúc tạo volume
* Boot volume không thể bị gỡ khỏi máy chủ ảo
* Data volume có thể được thao tác gắn vào hoặc gỡ khỏi các máy chủ ảo khác nhau
* Bạn có thể chọn mức QoS cho volume theo thông tin Volume Type để giới hạn băng thông và IOPS
* Bạn có thể lựa chọn chức năng mã hóa khi tạo volume để bảo vệ dữ liệu. VNG Cloud hỗ trợ mã hóa aes-xts-plan64 (128 bits)

***

## Tạo Volume

Có 2 loại mục đích cho volume là boot volume và data volume. Với boot volume, bạn có thể tạo đồng thời trong quá trình tạo máy chủ ảo. Data volume có thể được tạo trong quá trình tạo máy chủ hoặc thao tác tạo độc lập từ trang quản lý volume.

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Volume.

**Bước 2:** Tạo data volume, cung cấp các thông tin cần thiết như name, dung lượng (size), IOPS, các lựa chọn multi-attach và mã hóa.

**Bước 3:** Bạn có thể kiểm tra thông số ở bên phải, sau đó nhấn **Create Volume.**

***

## Gắn Volume vào VM Instance <a href="#volume-ganvolumevaovminstance" id="volume-ganvolumevaovminstance"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Volume.

**Bước 2**: Chọn data volume cần gắn, vào menu action ở bên phải, chọn **Attach.**

**Bước 3:** Chọn máy chủ ảo cần gắn volume, sau khi gắn bạn cần thao tác từ trong máy chủ ảo như tạo partition, format và mount.

***

## Tháo gỡ volume khỏi VM Instance <a href="#volume-thaogovolumekhoivminstance" id="volume-thaogovolumekhoivminstance"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Volume.

**Bước 2:** Chọn data volume cần gỡ, vào menu action ở bên phải, chọn **Detach.**

**Bước 3**: Chọn máy chủ ảo cần tháo gỡ volume.

***

## Xóa volume <a href="#volume-xoavolume" id="volume-xoavolume"></a>

**Bước 1:** Truy cập vào giao diện vServer với Region là vCloudstack, đến trang Volume.

**Bước 2:** Chọn data volume cần xóa, vào menu action ở bên phải, chọn **Delete**

{% hint style="info" %}
**Lưu ý:** Chỉ volume ở trạng thái Available mới có thể xóa.
{% endhint %}



***
