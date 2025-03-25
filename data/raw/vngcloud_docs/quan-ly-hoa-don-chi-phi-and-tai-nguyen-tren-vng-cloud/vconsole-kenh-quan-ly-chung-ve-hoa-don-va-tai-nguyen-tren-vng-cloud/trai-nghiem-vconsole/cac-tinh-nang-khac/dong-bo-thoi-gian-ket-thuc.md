# Đồng bộ thời gian kết thúc

Với tính năng đồng bộ ngày kết thúc, bạn có thể quản lý tất cả các dịch vụ của mình một cách dễ dàng và hiệu quả, không còn lo lắng về việc quên gia hạn. Chỉ với vài cú click, bạn có thể thiết lập ngày hết hạn cho tất cả tài khoản của mình, giúp tiết kiệm thời gian và công sức.

#### **Các bước thực hiện:**

1. **Đăng nhập vào tài khoản:**
   * Truy cập vào trang vConsole để thực hiện theo đường dẫn: [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/).
   * Làm theo hướng dẫn sau để đăng nhập vào tài khoản VNG Cloud [tại đây](../../../../identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md).
2. **Truy cập vào trang quản lý tài nguyên:**
   * Tìm và chọn mục "Thống kê tài nguyên" hoặc thông qua đường dẫn sau: [https://dashboard.console.vngcloud.vn/resource](https://dashboard.console.vngcloud.vn/resource).
   * Bạn sẽ thấy danh sách các tài nguyên đang sử dụng của tất cả các dịch vụ.
3. **Chọn các tài nguyên cần điều chỉnh:**
   * **Bước 1: Tìm tài nguyên cần điều chỉnh**
     * Lọc theo Product, Resource Type thuộc product
     * Lọc theo Renewal Type:
       * Manual: Các tài nguyên không bật auto renewal
       * Auto-Renewal: Các tài nguyên đã bật tự động gia hạn
     * Lọc theo Billing Status
       * Good: Tài nguyên có thời hạn sử dụng lớn hơn 15 ngày
       * Warning: Tài nguyên có thời hạn sử dụng từ 5 ngày đến 15 ngày
       * Alerted: Tài nguyên có thời hạn sử dụng nhỏ hơn 5 ngày
       * Expired: Tài nguyên đã hết hạn đang chờ xóa
   * **Bước 2: Tích vào ô bên cạnh tên của từng tài nguyên bạn muốn điều chỉnh.**
     * Hoặc, bạn có thể chọn "Chọn tất cả" để điều chỉnh cho toàn bộ tài nguyên.
   *   **Bước 3: Nhấn chọn hành động Match end time / Đồng bộ thời gian kết thúc**&#x20;

       <figure><img src="../../../../.gitbook/assets/image (21) (1) (1).png" alt=""><figcaption></figcaption></figure>
4. **Thiết lập ngày kết thúc mới:**
   * Bước 1: Chọn ngày và giờ hết hạn mới cần áp dụng cho các tài nguyên
   * Bước 2: Xem lại các chi phí phát sinh cho từng tài nguyên, tương ứng với thời gian hạn thêm
   *   Bước 3: Nhấn Match end time / Đồng bộ gia hạn để xác nhận thực hiện gia hạn

       <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
5. **Thực hiện thanh toán tại trang thanh toán để hoàn tất quá trình:**

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### **Lưu ý:**

* **Loại tài nguyên:** Tính năng này áp dụng cho các loại tài nguyên sau: Tài nguyên có Billing = Prepaid
* **Phí phát sinh:** Việc điều chỉnh ngày kết thúc sẽ có chi phí phát sinh tương tự như khi gia hạn tài nguyên
