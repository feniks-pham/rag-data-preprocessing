# Quản lý truy cập qua Policy

IAM Policy là các tài liệu JSON xác định các quyền và quy tắc truy cập tài nguyên.  Policy này được gắn kèm với IAM User Account, User Group và Service Account để kiểm soát hành động mà họ có thể thực hiện trên các tài nguyên cụ thể. IAM Policy tuân thủ nguyên tắc "cho phép" hoặc "từ chối", tức là chúng rõ ràng cấp quyền hoặc từ chối truy cập tài nguyên và hành động.

#### 1. Tạo Chính Sách (Policy) <a href="#customermanagedpolicy-1.taochinhsach-policy" id="customermanagedpolicy-1.taochinhsach-policy"></a>

**Để khởi tạo Chính Sách (Policy), bạn cần thực hiện các hướng dẫn sau:**

1. Truy cập IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Nhấp vào **"Policy"** trong menu bên trái.
3. Nhấp vào **"Create a policy."**
4. Cung cấp tên chính sách và mô tả tùy chọn.
5. Nhấp vào **"Next step"** để tiếp tục cấu hình quyền.
6. Mặc định, giao diện sẽ hiển thị tab **"Visual editor."** Sử dụng tính năng Visual editor để tiếp tục quá trình khởi tạo.
7. Chọn một **Product** cụ thể trong hệ thống VNG Cloud cần cấu hình.
8. Chỉ định các **Actions** được phép trên tài nguyên của sản phẩm.
9. Chọn các tài nguyên áp dụng các hành động **(Tất cả các tài nguyên / Tài nguyên cụ thể**).
10. Cung cấp các **điều kiện tùy chọn** khi áp dụng.
11. Để thêm tập Actions mới áp dụng trên tập Resource mới trong cùng 1 Policy, bạn nhấn chọn **"Add Rule"** như hình bên dưới, và tiếp tục thực hiện các hướng dẫn từ bước 6 → 9.

    <figure><img src="https://docs.vngcloud.vn/download/attachments/59806947/image2023-8-1_14-12-28.png?version=1&#x26;modificationDate=1690873949000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
12. Xem lại các thiết lập và nhấp vào **"Create policy."**

{% hint style="info" %}
**Lưu ý**

Để các Policies hoạt động đúng chức năng của nó, bạn cần gán chúng vào một đối tượng cụ thể (IAM user account, Service account, Group), tham khảo hướng dẫn dưới đây cho việc quản lý sử dụng Policy.
{% endhint %}

#### 2. Tạo và Chỉnh sửa Policy với JSON <a href="#customermanagedpolicy-2.taovachinhsuapolicyvoijson" id="customermanagedpolicy-2.taovachinhsuapolicyvoijson"></a>

**Bên cạnh việc khởi tạo và chỉnh sửa Policy với Visual editor, bạn cũng có thể sử dụng tab "JSON" để khởi tạo/chỉnh sửa Policy . Sử dụng hướng dẫn dưới đây để biết thêm chi tiết:**

* Dưới đây là JSON mẫu tương ứng khi chọn:
  * **Product:** vMonitor
  * **Effect:** Allow Permission
  * **Action:** All vMonitor actions
  * **Resource:** All resources
  * **Request conditions:** Không cài đặt

Example JSON Expand source

&#x20;**Giải thích JSON Attribute**

* **Statement: Policy**
* Mỗi object trong Statement tương ứng với **1 Rule**, bao gồm:\

  * **Effect:** Allow / Deny Permission
  * **Action:** Danh sách Action được cấp phép/từ chối trên Resource
  * **Resource:** Danh sách Resource sẽ áp dụng các Actions ở trên
  * **Conditon:** Request conditions



Mối quan hệ giữa Visual editor và JSON

* **Visual editor** và **JSON** là 2 trình cỉnh sửa Policy, được cung cấp bởi IAM VNG Cloud Services.
* Một khi Tạo/Chỉnh sửa policy từ Visual editor/JSON thì dữ liệu đề được tự động cập nhật giữa 2 tab.
* Để rút gọn quá trình **khởi tạo/chỉnh sửa Policy**, bạn có thể sử dụng qua lại giữa 2 tính năng **Visual editor/JSON**
* Lưu ý rằng mọi hành động/chỉnh sửa từ 2 tab đều được đồng bộ với tab còn lại.

#### 3. Quản lý sử dụng Policy <a href="#customermanagedpolicy-3.quanlysudungpolicy" id="customermanagedpolicy-3.quanlysudungpolicy"></a>

**Để gán Policy cho IAM user account, Group và Service Account, bạn cần làm theo các hướng dẫn sau:**

1. Truy cập vào Policy cần quản lý
2. Tại trang thông tin chi tiết của Policy, nhấn chọn tab **"Policy usage".**
3. Để gán Policy vào các đối tượng cần áp dụng, nhấn nút **"Attach"** ngay phía trên bên phải, một popup sẽ hiện ra cho phép bạn chọn các đối tượng cần áp dụng.
4. Tại popup, thực hiện:
   1. Nhấn tab **"User"** và Chọn các IAM User Accounts sẽ áp dụng Policy này.
   2. Nhấn tab **"Group"** và Chọn các User Group sẽ áp dụng Policy này.
   3. Nhấn tab **"Service Account"** và Chọn các Service Account sẽ áp dụng Poliy này.
5. Xem lại các đối tượng áp dụng và nhấn nút **"Add"** để hoàn tất quá trình.
6. Bạn có thể xem lại danh sách các đối tượng vừa được gán bằng cách nhấn vào tab **"User", "Group", "Service Account".**

#### **4. Xóa Policy** <a href="#customermanagedpolicy-4.xoapolicy" id="customermanagedpolicy-4.xoapolicy"></a>

**Bạn có thể xóa Policy bằng cách tuân theo 2 tùy chọn dưới đây:**

1. **Xóa nhiều Policy cùng một lúc:**
   * Truy cập vào IAM với Root User Account / IAM User Account.
   * Nhấp vào **"Policy"** trong menu bên trái.
   * Chọn các Policies mà bạn muốn xóa (một nút "**Delete**" sẽ được bật ở góc trên bên phải khi bạn chọn ít nhất một Policy).
   * Nhấp vào nút "**Delete**" (Xóa), một hộp thoại xác nhận sẽ xuất hiện để đảm bảo bạn không xóa nhầm tài khoản, sau đó nhấp vào nút "**Confirm**" (Xác nhận) để hoàn tất quy trình.
2. **Xóa một Policy:** Chúng tôi khuyến nghị bạn nên truy cập vào thông tin chi tiết của Policy và xem lại phần thông tin **"Policy usage"** trước khi thực hiện xóa, để đảm bảo bạn không xóa nhầm Policy.

{% hint style="info" %}
**Lưu ý**

Để hạn chế việc xóa nhầm Policy đang sử dụng bới các đối tượng IAM, chúng tôi khuyên bạn nên gỡ đính kèm Policy khỏi các đối tượng IAM thay vì xóa trực tiếp. Vì một khi Policy bị xóa sẽ không thể khôi phục lại được.
{% endhint %}
