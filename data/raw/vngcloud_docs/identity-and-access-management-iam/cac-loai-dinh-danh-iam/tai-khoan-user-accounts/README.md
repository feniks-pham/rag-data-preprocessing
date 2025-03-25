# Tài khoản User Accounts

Trong VNG Cloud Services, việc tạo tài khoản người dùng IAM và nhóm là một quy trình dễ dàng thông qua giao diện điều khiển quản lý IAM. Nó nhằm cấp quyền truy cập vào các dịch vụ và tài nguyên trên tài khoản của bạn mà không chia sẻ thông tin bảo mật nhạy cảm.

#### Quản lý User Account <a href="#useraccounts-quanlyuseraccount" id="useraccounts-quanlyuseraccount"></a>

* **Root User Account:** Một tài khoản Root là một thực thể bạn tạo đầu tiên trong VNG Cloud và nó có đầy đủ quyền truy cập vào tất cả các dịch vụ và tài nguyên của VNG Cloud.
* **IAM User Account:** IAM User Account là một thực thể đại diện cho người sử dụng nó tương tác với VNG Cloud trên giao diện Portal. Một IAM User Account trong VNG Cloud bao gồm các thông tin đăng nhập (tên người dùng, mật khẩu) và mặc định bị từ chối quyền truy cập. IAM User Account không phải là các tài khoản riêng biệt; chúng là người dùng trong cùng một tài khoản Root và không cần phải có phương thức thanh toán được lưu trữ trong VNG Cloud. Bất kỳ hoạt động nào được thực hiện bởi các IAM User Account trong tài khoản Root của bạn sẽ được tính phí cho tài khoản Root.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806682/Identities-User%20Account.drawio%20(1).png?version=1&#x26;modificationDate=1691474639000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**1. Cách tạo IAM User Account?**

Để tạo các tài khoản người dùng IAM mới:

1. Truy cập vào IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Nhấp vào **"User account"** trong menu bên trái.
3. Nhấp vào **"Create a user account".**
4. Nhập thông tin tài khoản người dùng, bao gồm tên người dùng và mật khẩu.
5. Xem lại các cài đặt và nhấp vào **"Create user account"** ở góc trên bên phải.

**2. Gán Quyền cho IAM User Account**

Một IAM User Account cần được gắn vào ít nhất một Policy hoặc thuộc ít nhất một IAM User Group đã có ít nhất một Policy gắn vào để đảm bảo IAM User Account hoạt động đúng. Để gắn Policy cho IAM User Account:

1. Truy cập vào IAM Console - Trang User account với URL: [https://hcm-3.console.vngcloud.vn/iam/user-accounts](https://hcm-3.console.vngcloud.vn/iam/user-accounts)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Tìm kiếm IAM User Account bằng cách nhập tên người dùng vào hộp tìm kiếm và chọn tài khoản đúng trong kết quả tìm kiếm.
4. Mặc định, bạn sẽ thấy tab **"Permission"** tại trang thông tin chi tiết của IAM User Account. Nhấp vào nút "**Attach Policies**" và sau đó bạn sẽ thấy một cửa sổ xuất hiện chứa tất cả các Policies.
5. Tìm kiếm Policies bằng cách nhập tên Policies vào ô tìm kiếm.
6. Tick chọn Policies trong kết quả tìm kiếm và nhấp vào nút **"Attach"** ở phía dưới bên phải của cửa sổ xuất hiện.
7. Bây giờ, IAM User Account của bạn sẽ có tất cả các quyền hạn có trong các Policies được gắn kèm.

**3. Thêm IAM User Account vào User Group**

IAM User Account cần được gắn vào ít nhất một Policy hoặc thuộc một User Group đã có ít nhất một Policy gắn kèm để đảm bảo IAM User Account hoạt động đúng. Để thêm IAM User Account vào một User Group:

1. Truy cập vào IAM Console - Trang User account với URL: [https://hcm-3.console.vngcloud.vn/iam/user-accounts](https://hcm-3.console.vngcloud.vn/iam/user-accounts)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Tìm kiếm IAM User Account bằng cách nhập tên người dùng vào hộp tìm kiếm và chọn tài khoản đúng trong kết quả tìm kiếm.
4. Nhấp vào tab "**Group**" tại trang thông tin chi tiết của IAM User Account.
5. Nhấp vào nút "**Add users to Group**" và sau đó bạn sẽ thấy một cửa sổ xuất hiện chứa tất cả các User Groups.
6. Tick chọn các Groups trong bảng danh sách và nhấp vào nút "**Add to Groups**" ở phía dưới bên phải của cửa sổ xuất hiện.
7. Bây giờ, IAM User Account của bạn đã được thêm vào các Group và thừa hưởng toàn bộ Quyền hạn gắn kèm từ các Group đó.

**4. Quản lý thông tin đăng nhập của IAM User Account**

Một IAM User Account bao gồm thông tin đăng nhập (tên người dùng, mật khẩu). Bạn có thể thay đổi mật khẩu của IAM User Account bằng cách làm theo các bước hướng dẫn dưới đây:

1. Truy cập vào IAM Console - Trang User account với URL: [https://hcm-3.console.vngcloud.vn/iam/user-accounts](https://hcm-3.console.vngcloud.vn/iam/user-accounts)
2. Đăng nhập với tư cách là tài khoản Người dùng Gốc (Root User Account) hoặc User Account được cấp quyền truy cập. Bạn cần cung cấp tên người dùng/email và mật khẩu khi đăng nhập.
3. Tìm kiếm IAM User Account bằng cách nhập tên người dùng vào hộp tìm kiếm và chọn tài khoản đúng trong kết quả tìm kiếm.
4. Nhấp vào tab "**Security credentials**" tại trang thông tin chi tiết của IAM User Account.
5.  Nhấp vào nút "**Edit**" như hình dưới đây.

    <figure><img src="https://docs.vngcloud.vn/download/attachments/59806682/Screenshot%202023-07-25%20144222.png?version=1&#x26;modificationDate=1690270959000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
6. Một cửa sổ xuất hiện cho phép "**Chỉnh sửa mật khẩu**" để nhập mật khẩu mới hoặc nhấp vào nút "**Auto generate**" để tạo một mật khẩu ngẫu nhiên.
7. Nhấp vào nút "**Save**" sau khi hoàn tất để lưu mật khẩu mới.

**5. Xóa IAM User Account?**

Bạn có thể xóa IAM User Account bằng cách làm theo 2 lựa chọn dưới đây:

1. **Xóa nhiều IAM User Account cùng một lúc:**
   1. Truy cập vào IAM Console với tư cách Root User Account hoặc IAM User Account được cấp quyền truy cập.
   2. Nhấp vào "User account" trong menu bên trái.
   3. Chọn IAM User Account mà bạn muốn xóa (một nút "**Delete**" sẽ được kích hoạt ở góc trên bên phải khi bạn chọn ít nhất một tài khoản).
   4. Nhấp vào nút "**Delete**", một cửa sổ xuất hiện để xác nhận rằng bạn không xóa nhầm tài khoản, sau đó nhấp vào nút "**Confirm**" để hoàn tất quá trình.
2. **Xóa một IAM User Account:** Chúng tôi khuyên bạn nên truy cập vào chi tiết của IAM User Account và sau đó tiến hành xóa để đảm bảo bạn không xóa nhầm người dùng sai.

Note

Lưu ý rằng một khi đã xóa, các IAM User Account sẽ không thể khôi phục lại được



***

In VNG Cloud Services, creating IAM user accounts and groups is a straightforward process using the IAM management console. It aims to grant additional users access to services and resources on your account without sharing sensitive security information.

#### User Accounts Management <a href="#useraccounts-useraccountsmanagement" id="useraccounts-useraccountsmanagement"></a>

* **Root user account:** A root user account is an entity that you first create in VNG Cloud and use that has complete access to all VNG Cloud services and resources in the account.
* **IAM user account:** A user account or IAM user account is an entity that represents the person that uses it to interact with VNG Cloud on Portal UI. A user account in VNG Cloud consists of credentials (username, password) and is denied access by default. User accounts are not separate accounts; they are users within the same root user account and they don't need to have a payment method on file with VNG Cloud. Any activity performed by user accounts in your account is billed to your root user account.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806682/image2022-6-16_16-52-35.png?version=1&#x26;modificationDate=1690267390000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**1. How to Create IAM Users?**

To create new IAM user accounts:

1. Navigate to the IAM Console: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/)
2. Click on **"User account"** in the left-hand menu.
3. Click on **"Create a User account."**
4. Enter the user account details, including the _username and password_.
5. Review the settings and click **"Create User Account"** at the top right corner.

**2. Assign Permission to an IAM user account**

An IAM User Account needs to be attached to at least one Policy or under one Group, which already has at least one attached Policy to ensure the IAM User Account works in the correct concept. To attach Policies to an IAM User Account:&#x20;

1. Access the IAM Console - User Account page with the URL: [https://hcm-3.console.vngcloud.vn/iam/user-accounts](https://hcm-3.console.vngcloud.vn/iam/user-accounts)
2. Sign in as a **Root user account**. You may need to provide a username and password or use other authentication methods like single sign-on (SSO) if configured.
3. **Search the IAM user account** by entering its username into the search box, and **select the correct one** in the search result.
4. By default, you will see the **Permission** tab on the IAM user account's detailed information.
5. Click on the button **"Attach policies"**, and then you will see an appearing popup that contains all Policies.
6. **Search the existing Policies** by entering the Policies' exact names into the search box.
7. **Check on the records** in the search result and click on the button **"Attach"** at the bottom right of the popup.
8. Now, your IAM User Account will have all the permissions contained in the attached Policies

**3. Assign an IAM user account to a Group**

An IAM User Account needs to be attached to at least one Policy or under one Group, which already has at least one attached Policy to ensure the IAM User Account works in the correct concept. To assign an IAM User Account to User Groups:

1. Access the IAM Console - User Account page with the URL: [https://hcm-3.console.vngcloud.vn/iam/user-accounts](https://hcm-3.console.vngcloud.vn/iam/user-accounts)
2. Sign in as a **Root user account**. You may need to provide a username and password or use other authentication methods like single sign-on (SSO) if configured.
3. **Search the IAM user account** by entering its username into the search box, and **select the correct one** in the search result.
4. Click on the **Group** tab on the IAM user account's detailed information.
5. Click on the button **"Add user to groups"**, and then you will see an appearing popup that contains all Groups.
6. **Check on the records** in the table of the Group list and click on the button **"Add to groups"** at the bottom right of the popup.
7. Now, your IAM User Account has already been assigned to the Group(s) and inherited all attached Permission from the Group(s).

**4. Manage IAM User Account Credentials**

A user account consists of credentials (username, password). You can change your IAM user account's password by following the steps of instruction below:

1. Access the IAM Console - User Account page with the URL: [https://hcm-3.console.vngcloud.vn/iam/user-accounts](https://hcm-3.console.vngcloud.vn/iam/user-accounts)
2. Sign in as a **Root user account**. You may need to provide a username and password or use other authentication methods like single sign-on (SSO) if configured.
3. **Search the IAM user account** by entering its username into the search box, and **select the correct one** in the search result.
4. Click on the **"Security credentials"** tab on the IAM user account's detailed information.
5.  Click on the **"Edit"** button as in the image below&#x20;



    <figure><img src="https://docs.vngcloud.vn/download/attachments/59806682/Screenshot%202023-07-25%20144222.png?version=1&#x26;modificationDate=1690270959000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
6. An **"Edit password" popup** will be shown for **entering a new one** or clicking on the **"Auto generate"** button to generate a random one.
7. Click on the **"Save"** button after finishing reviewing the new password to save the new one.

**5. How to delete IAM User Accounts?**

You can delete IAM User Account(s) by following 2 options below:

1. **Delete multi IAM User Accounts at once time:**&#x20;
   1. Access to IAM Console as Root User Account
   2. Click on **"User account"** in the left-hand menu.
   3. Select IAM User Account(s) that you want to delete (a **"Delete" button** will be enabled at the top right corner when you select at least one record)
   4. Click on the **"Delete"** button, a confirm popup will appear to ensure that you don't delete the wrong user(s), then Click on the **"Confirm"** button to complete the process.
2. **Delete an IAM User Account:** We recommend that you should access the detail of the IAM User Account, and then conduct deletion on it to make sure you don't delete the wrong user.

\
