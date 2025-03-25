# Tích hợp vStorage API

Để xem hướng dẫn tích hợp vStorage API, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn thư mục **Tích hợp.**
3. Chọn biểu tượng **vStorage API**.
4. Tại mục **Cấp quyền**, bạn cần điền thông tin cần thiết để cấu hình vStorage API của bạn bao gồm:
   1. Nhập **Client ID**. Một **Client ID** là một chuỗi ký tự được sử dụng bởi Service API để định danh ứng dụng, đồng thời cũng được dùng để xây dựng "authorization URL" hiển thị phía người dùng. Bạn có thể tạo và quản lý **Client ID** thông qua hệ thống vIAM. **Client ID** sẽ được tự động sinh ra khi bạn tạo mới một **Service Account**. Chi tiết tham khảo tại [Khởi tạo tài khoản Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md).
   2. Nhập **Client Secret** tương ứng của **Client ID** vừa nhập. Cặp Client ID và Client Secret được bạn tạo và quản lý thông qua hệ thống vIAM. Bạn có thể chọn [Click here to manage your Client ID.](https://hcm-3.console.vngcloud.vn/iam/service-accounts) để chúng tôi điều hướng bạn tới hệ thống vIAM và chi tiết là các màn hình quản lý Service Account. Chi tiết tham khảo tại [Khởi tạo tài khoản Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md).
5. Sau khi hoàn tất chọn cấu hình **Cấp quyền**, chọn **Xác thực** để chuyển tới màn hình **Cấu hình**. Bạn luôn có thể quay lại đây để thay đổi thông tin **Cấp quyền** của mình, sau đó chọn lại **Xác thực** để cập nhật danh sách S3 Rest API theo thông số mới của bạn.&#x20;

<figure><img src="../../../../../.gitbook/assets/Tich_hop_vStorage_API.gif" alt=""><figcaption></figcaption></figure>

#### Trải nghiệm vStorage API ngay trên vStorage Portal <a href="#tichhopvstorageapi-trainghiemvstorageapingaytrenvstorageportal" id="tichhopvstorageapi-trainghiemvstorageapingaytrenvstorageportal"></a>

Để trải nghiệm sử dụng vStorage API, bạn cần có ít nhất 1 Client ID, Client Secret( thông tin này lấy tại Service Account). Để tạo Service Account, tham khảo thêm tại [Khởi tạo tài khoản Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md). Bạn có thể sử dụng Service Account này để tạo (hoặc xóa) nhiều container, container như một đơn vị lưu trữ (giống như một thư mục), trong mỗi container khách hàng có thể upload, get, delete nhiều object tương ứng (object ở đây được hiểu như một file, hoặc một folder con trong container).

Quy trình cơ bản: Xác thực -> Tạo project ->Tạo container -> Upload Object

Chúng tôi cung cấp cho bạn một giao diện thao tác nhanh với vStorage API, sau khi bạn thực hiện tích hợp theo hướng dẫn tại [Tích hợp vStorage API](tich-hop-vstorage-api.md), hãy tiếp tục làm theo hướng dẫn:&#x20;

1. Chọn **Try it out**.
2. Nhập **đầu vào** cho mỗi API.
3. Chọn **Execute**
4. Kiểm tra **kết quả** trả về.

Bên dưới là ví dụ về 4 vStorage API cơ bản nhất mà bạn có thể trải nghiệm:

**1. Tạo project**

Điều kiện cần:

* Người dùng trả sau

Kết quả thực hiện:

* Project được khởi tạo với các thuộc tính:&#x20;
  * Project type: Gold class.
  * Region: HCM01.

<figure><img src="../../../../../.gitbook/assets/image (549).png" alt=""><figcaption></figcaption></figure>

**2. Tạo container**

API bên dưới sử dụng để bạn có thể khởi tạo một container trong một project.

<figure><img src="../../../../../.gitbook/assets/image (550).png" alt=""><figcaption></figcaption></figure>

**3. Xóa một container**

API bên dưới sử dụng để bạn có thể xóa một container trong một project.

<figure><img src="../../../../../.gitbook/assets/image (551).png" alt=""><figcaption></figcaption></figure>

**4. Xóa một object**

API bên dưới sử dụng để bạn có thể xóa một object trong một container.

<figure><img src="../../../../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

Ngoài cách sử dụng nhanh trên vStorage Portal, bạn có thể sử dụng vStorage API tại thiết bị cá nhân theo hướng dẫn tại [Sử dụng vStorage API](su-dung-vstorage-api.md).
