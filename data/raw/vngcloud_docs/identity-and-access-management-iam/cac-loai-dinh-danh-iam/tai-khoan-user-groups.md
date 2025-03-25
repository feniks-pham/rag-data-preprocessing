# Tài khoản User Groups

#### Quản lý User Group <a href="#usergroups-quanlyusergroup" id="usergroups-quanlyusergroup"></a>

IAM User Group là một tập hợp các IAM User Account. IAM User Group giúp đơn giản hóa việc quản lý quyền bằng cách cho phép bạn cấp, thay đổi và gỡ bỏ quyền cho nhiều IAM User Account cùng một lúc. Ví dụ, bạn có thể tạo một IAM User Group có tên là "Quản trị viên" và cấp quyền quản trị cho nhóm đó. Bất kỳ IAM User Account nào trong nhóm đều tự động có các quyền được gán cho nhóm.

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/63766769/Identities-User%20Group.drawio%20(1).png?version=1&#x26;modificationDate=1691474619000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**1. Cách tạo một IAM User Group?**

Để tạo một IAM User Group mới:

1. Truy cập vào IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Nhấp vào "**Group**" trong menu bên trái.
3. Nhấp vào "**Create a group**".
4. Cung cấp tên nhóm và mô tả tùy chọn.
5. Gán các IAM Policies liên quan cho nhóm để xác định các quyền của nhóm.
6. Xem lại các thiết lập và nhấp vào "**Create group**".

**2. Cách gán Quyền cho IAM User Group?**

Bạn có thể gán Policies cho một Group trong quá trình tạo IAM User Group mới, hoặc gán Policies cho một IAM User Group đã tồn tại. Để gán Policies cho một Group đã tồn tại:

1. Truy cập vào IAM Console - Trang Group với URL: [https://hcm-3.console.vngcloud.vn/iam/user-groups](https://hcm-3.console.vngcloud.vn/iam/user-groups)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Tìm kiếm IAM User Group bằng cách nhập tên của nó vào ô tìm kiếm và chọn IAM User Group đúng trong kết quả tìm kiếm.
4. Mặc định, bạn sẽ thấy tab "**Permission**" tại trang thông tin chi tiết của IAM User Group.
5. Nhấp vào nút "**Attach Policies**", sau đó bạn sẽ thấy một cửa sổ xuất hiện chứa tất cả Policies.
6. Tìm kiếm các Policies cần gán bằng cách nhập tên chính xác củaPolicies vào ô tìm kiếm.
7. Chọn Policies cần gán tại kết quả tìm kiếm và nhấn nút "**Attach**" ở góc dưới bên phải của popup.
8. Bây giờ, IAM User Group của bạn sẽ có tất cả các quyền chứa trong các Policies đã gán và đảm bảo rằng tất cả IAM User Account trong Groups đều kế thừa tất cả các Quyền này.

**3. Cách gán IAM User Account vào IAM User Group?**

Bạn có thể gán IAM User Account vào một IAM User Group trong quá trình tạo IAM User Group mới, hoặc gán IAM User Account vào một IAM User Group đã tồn tại. Để gán IAM User Account vào một IAM User Group đã tồn tại:

1. Truy cập vào IAM Console - Trang Group với URL: [https://hcm-3.console.vngcloud.vn/iam/user-groups](https://hcm-3.console.vngcloud.vn/iam/user-groups)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Tìm kiếm IAM User Group bằng cách nhập tên của nó vào ô tìm kiếm và chọn IAM User Group đúng trong kết quả tìm kiếm.
4. Nhấp vào tab **"User"** tại trang thông tin chi tiết của IAM User Group.
5. Nhấp vào nút "**Add user**", sau đó bạn sẽ thấy một cửa sổ xuất hiện chứa tất cả IAM User Account của bạn.
6. Chọn IAM User Account và nhấp vào nút "**Add**" ở góc dưới bên phải của popup.
7. Bây giờ, các IAM User Account của bạn sẽ kế thừa tất cả các Quyền của Group.

**4. Xóa IAM User Group?**

Bạn có thể xóa IAM User Group bằng cách thực hiện 2 tùy chọn sau:

1. **Xóa nhiều IAM User Group cùng một lúc:**&#x20;
   1. Truy cập vào IAM Console với tài khoản Root hoặc IAM User Account được cấp quyền truy cập
   2. Nhấp vào "Group" trong menu bên trái.
   3. Chọn IAM User Group mà bạn muốn xóa (một nút "**Delete**" sẽ được bật ở góc trên bên phải khi bạn chọn ít nhất một nhóm).
   4. Nhấp vào nút "**Delete**", một cửa sổ xác nhận sẽ xuất hiện để đảm bảo bạn không xóa nhầm Group, sau đó nhấp vào nút "**Confirm**" để hoàn tất quy trình.
2. **Xóa một IAM User Group:** Chúng tôi đề xuất bạn nên truy cập vào chi tiết của IAM User Group và sau đó thực hiện xóa nó để đảm bảo bạn không xóa nhầm Group.

{% hint style="info" %}
**Note**

* Nhớ rằng khi bạn xác nhận việc xóa IAM User Group, thì Group đó không thể khôi phục lại được.
* Hãy xem xét và gán các Policies mới cho các IAM User Account thuộc về những IAM User Group đã bị xóa, để đảm bảo rằng các IAM User Account vẫn hoạt động đúng cách.
{% endhint %}



\
