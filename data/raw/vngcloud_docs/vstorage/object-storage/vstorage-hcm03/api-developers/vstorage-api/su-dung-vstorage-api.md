# Sử dụng vStorage API

Để sử dụng vStorage API, bạn cần có ít nhất 1 Client ID, Client Secret( thông tin này lấy tại Service Account). Để tạo Service Account, tham khảo thêm tại [Khởi tạo tài khoản Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md). Bạn có thể sử dụng Service Account này để tạo (hoặc xóa) nhiều container, container như một đơn vị lưu trữ (giống như một thư mục), trong mỗi container khách hàng có thể upload, get, delete nhiều object tương ứng (object ở đây được hiểu như một file, hoặc một folder con trong container).

**Quy trình cơ bản**: Xác thực -> Tạo project ->Tạo container -> Upload Object

Chi tiết danh sách vStorage API được chúng tôi mô tả tại [https://docs.api.vngcloud.vn/service-docs/vstorage-api.html#tag/containers](https://docs.api.vngcloud.vn/service-docs/vstorage-api.html#tag/containers).

Bên dưới là ví dụ với vStorage API tạo mới một container trên một project:

<figure><img src="../../../../../.gitbook/assets/image (553).png" alt=""><figcaption></figcaption></figure>

**Trong đó:**&#x20;

* Vùng số 1: vùng tìm kiếm nhanh API theo tên hoặc key words của API.
* Vùng số 2: vùng hiển thị danh sách API theo từng nhóm chức năng.
* Vùng số 3: vùng hiển thị chi tiết thông tin đầu vào, đầu ra đối với mỗi trường hợp của API.
* Vùng số 4: vùng chọn các ngôn ngữ khá nhau tương ứng cho đầu vào, đầu ra của API đang được lựa chọn.
* Vùng số 5: vùng hiển thị đầu vào, đầu ra của API theo ngôn ngữ đang được lựa chọn tại Vùng 4.
