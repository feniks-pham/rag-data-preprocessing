# Tag tài nguyên

## Tổng quan

**Tại sao cần đánh tag tài nguyên?**

* **Tổ chức và quản lý tài nguyên hiệu quả:** Việc gắn tag cho các tài nguyên giúp bạn phân loại, nhóm các tài nguyên theo nhiều tiêu chí khác nhau như: bộ phận sở hữu, mục đích sử dụng, môi trường (dev, test, prod),...
* **Tìm kiếm và lọc tài nguyên dễ dàng:** Thay vì phải tìm kiếm thủ công từng tài nguyên, bạn có thể sử dụng các tag để lọc và tìm kiếm nhanh chóng các tài nguyên đáp ứng các tiêu chí nhất định.
* **Tự động hóa các tác vụ:** Bạn có thể sử dụng các tag để tự động hóa các tác vụ quản lý tài nguyên như: sao lưu, xóa, hoặc áp dụng các chính sách bảo mật khác nhau cho các nhóm tài nguyên khác nhau.
* **Phân bổ chi phí:** Dựa trên các tag, bạn có thể phân bổ chi phí sử dụng tài nguyên cho các bộ phận hoặc dự án khác nhau.

**Lợi ích khi sử dụng tính năng Tag tài nguyên:**

* **Nâng cao hiệu quả làm việc:** Giảm thời gian tìm kiếm và quản lý tài nguyên.
* **Tăng tính chính xác:** Giảm thiểu rủi ro do quản lý tài nguyên thủ công.
* **Tối ưu hóa chi phí:** Phân bổ chi phí sử dụng tài nguyên hợp lý.
* **Đảm bảo tính bảo mật:** Áp dụng các chính sách bảo mật phù hợp cho từng nhóm tài nguyên.

## Tính năng

### **1. Gắn tag cho tài nguyên**

**Bước 1:** Truy cập vào trang thống kê tài nguyên tại đây: [https://dashboard.console.vngcloud.vn/resource](https://dashboard.console.vngcloud.vn/resource)

**Bước 2:** Chọn một hoặc nhiều tài nguyên bạn muốn gắn tag (hình bên dưới)

<figure><img src="../../../../.gitbook/assets/image (13) (2).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Nhấn vào nút "Quản lý thẻ" hoặc biểu tượng thẻ tại phần table header.

Một cửa sổ giao diện sẽ mở ra cho phép bạn thêm hoặc xóa thông tin thẻ của tài nguyên, cụ thể như sau:

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

1. **Tag mặc định:** Tài nguyên sẽ được tự động gắn tag `vng.createdBy` với giá trị là định danh của IAM User hoặc Root User đã tạo tài nguyên và không được phép xóa tag này.
2. **Tag tùy chỉnh:**
   * **Chọn loại tag:** Bạn có thể chọn từ các loại tag đã được định nghĩa sẵn như `Assignee`, `Company,Department`, `Environment`.
   * **Nhập giá trị:** Nhập giá trị cụ thể cho tag đó (ví dụ: `Assignee=Sultu`, `Department=Engineering`). Nhấn nút "Thêm" để xác nhận thêm tag

**Bước 4:** Nhấp vào nút "Lưu" hoặc "Áp dụng" để hoàn tất việc gắn tag.

### **2. Tìm kiếm tài nguyên theo tag**

**Bước 1:** Truy cập vào trang thống kê tài nguyên tại đây: [https://dashboard.console.vngcloud.vn/resource](https://dashboard.console.vngcloud.vn/resource)

**Bước 2:** Tìm đến ô tìm kiếm như hình bên dưới:

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Nhập giá trị của tag mà bạn muốn tìm kiếm (ví dụ: `Sultu`).

**Bước 4:** Hệ thống sẽ hiển thị danh sách các tài nguyên có chứa tag mang giá trị là Sultu.

**Lưu ý:**

* **Giá trị tag:** Giá trị tag phải chính xác và tuân theo định dạng đã được quy định.
* **Phần quyền:** Chỉ có Root User mới có thể thêm mới, chỉnh sửa trên tag tài nguyên. IAM User chỉ được phép xem.

### 3. Đồng bộ thông tin tag vào hóa đơn

Tính năng đồng bộ thông tin tag vào hóa đơn giúp liên kết chặt chẽ giữa thông tin tài nguyên và thông tin thanh toán. Cụ thể:

* **Mục đích:** Đảm bảo sự nhất quán giữa thông tin tài nguyên và hóa đơn, giúp cho việc theo dõi, quản lý chi phí và phân bổ chi phí được chính xác hơn.
* **Cách thức hoạt động:**
  * Khi tạo mới một tài nguyên, hệ thống sẽ tự động tạo một hóa đơn tương ứng.
  * Khi bạn gắn tag cho tài nguyên, thông tin tag này sẽ **không được đồng bộ ngay lập tức** vào hóa đơn.
  * **Cuối kỳ đối soát:** Hệ thống sẽ tiến hành đồng bộ thông tin tag từ tài nguyên sang hóa đơn tương ứng một lần duy nhất.
  * **Lưu ý:** Chỉ những tag được gắn vào tài nguyên **trước khi kết thúc kỳ đối soát** mới được đồng bộ. Các tag được chỉnh sửa sau đó sẽ không được cập nhật trên hóa đơn.

**Để xem thông tin tag trên hóa đơn:**

1. **Truy cập vào trang thống kê hóa đơn:** [https://dashboard.console.vngcloud.vn/billing-report](https://dashboard.console.vngcloud.vn/billing-report)
2.  **Xuất hóa đơn:** Click vào nút "Xuất hóa đơn" để tải về bản sao hóa đơn đầy đủ.&#x20;

    <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. **Kiểm tra thông tin tag:** Trong bản sao hóa đơn đã xuất, bạn sẽ tìm thấy một phần liệt kê các tag đã được gắn cho các tài nguyên liên quan đến hóa đơn đó.

**Lưu ý:**

* **Thời điểm đồng bộ:** Thông tin tag sẽ được đồng bộ vào cuối kỳ đối soát của hóa đơn.
* **Dữ liệu được đồng bộ:** Chỉ có thông tin tag của tài nguyên tại thời điểm kết thúc kỳ đối soát mới được đồng bộ.
* **Mục đích sử dụng thông tin tag trên hóa đơn:**
  * **Phân tích chi phí:** Dựa trên các tag, bạn có thể phân tích chi phí sử dụng tài nguyên theo các tiêu chí như bộ phận, dự án,...
  * **Theo dõi tài sản:** Dễ dàng xác định các tài nguyên liên quan đến một hóa đơn cụ thể.
  * **Kiểm toán:** Cung cấp thông tin chi tiết để phục vụ cho công tác kiểm toán.
