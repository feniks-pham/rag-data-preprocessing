# Quản lý truy cập

Bài viết hướng dẫn cách thêm user và phân quyền để sử dụng dịch vụ vCloudStack:

* [Thêm nhiều user với Identity Provider (Azure AD)](quan-ly-truy-cap.md#id-1-them-nhieu-user-voi-identity-provider-azure-a-d)
* [Thêm một user sử dụng vCloudStack](quan-ly-truy-cap.md#id-2-them-mot-user-su-dung-vcloudstack)
* [Phân quyền user sử dụng vCloudStack](quan-ly-truy-cap.md#id-3-phan-quyen-user-su-dung-vcloudstack)

***

## <mark style="color:blue;">1/ Thêm nhiều user với Identity Provider (Azure AD)</mark>

Để thêm nhiều User có thể sử dụng hệ thống dịch vụ vCloudStack, người quản trị (admin) cần thực hiện các bước như sau:

**Bước 1:** Quản trị viên truy cập vào trang chủ của VNG Cloud ([dashboard.console.vngcloud.vn](https://dashboard.console.vngcloud.vn/))

**Bước 2:** Chọn đến trang **IAM Portal** của IAM;

**Bước 3:** Tại thanh điều hướng bên trái, chọn mục **Identity Provider**;

**Bước 4:** Để tạo một dịch vụ tích hợp Single-Sign-On, đồng bộ thông tin các user để đăng nhập vào vCloudStack, nhấn chọn "Add an Identity Provider"

**Bước 5:** Điền các trường thông tin cần đề tạo dịch vụ đồng bộ:

* **Provider Name**: Điền tên nhận diện dịch vụ đồng bộ thông tin đăng nhập;
* **Provider Type:** Chọn **SAML**
* **Vendor:** Chọn **Azure AD**
* **Login URL**: Điền **link Login URL từ Microsoft Entra ID** (trước là Azure Active Directory)

{% hint style="success" %}
_Những lưu ý để cách lấy link Login URL tại Microsoft Entra ID:_

* Đề tạo link cần thực hiện admin thực hiện ở trang [portal.azure.com](https://portal.azure.com/#home) với app Microsoft Entra ID.
* Tạo "New Application" trong mục Enterprise Application, chọn option "Integrate any other application you don't find in the gallery (Non-gallery)" để hỗ trợ Single-Sign-On với SAML.
* Thêm những users muốn dùng vCloudstack ở mục Users/Group trong app
* Vào mục Single-Sign-On, chọn phương thức SAML và từ đó có **được link Login URL**.
{% endhint %}

**Bước 5:** Sau khi điền thông tin link Login URL , nhấn **Save**;

**Bước 6**: Hệ thống sẽ tạo ra:

* Entity URL;
* Reply URL;
* Login URL;

Admin dùng Entity URL và Reply URL  vừa tạo, sau đó quay lại app **Microsoft Entra ID,** dán Entity URL và Reply URL tại "Setup Single-Sign-On with SAML" và xác nhận (admin có thể test đồng bộ sau khi điền các URL).

**Bước 7:** Khi việc Test thử nghiệm đồng bộ thành công, thì xem như Admin có thể sử dụng Link Login URL gửi cho User để có thể tiến hành truy cập và xác thực bởi Azure, nếu xác thực thành công, User có thể được điều hướng (re-direct) tới màn hình User Site của vCloudStack.

{% hint style="info" %}
**Lưu ý:** Sau khi truy cập thành công vào User Page, có thể user vẫn chưa được phân quyền sử dụng dịch vụ vCloudStack vì chưa được phân quyền chức năng sử dụng. Admin cần thực hiện việc [Phân quyền user sử dụng vCloudStack](quan-ly-truy-cap.md#id-3-phan-quyen-user-su-dung-vcloudstack) theo hướng dẫn bên dưới.
{% endhint %}

***

## <mark style="color:blue;">2/ Thêm một user sử dụng vCloudStack</mark>

Để thêm 01 user có thể sử dụng hệ thống dịch vụ vCloudStack, người quản trị (admin) cần thực hiện các bước như sau:

**Bước 1:** Quản trị viên truy cập vào trang chủ của VNG Cloud ([dashboard.console.vngcloud.vn](https://dashboard.console.vngcloud.vn/))

**Bước 2:** Chọn đến trang **IAM Portal** của IAM;

**Bước 3:** Tại thanh điều hướng bên trái, chọn mục **User Account,** màn hình hiện danh sách IAM user ;

**Bước 4:** Để tạo thêm user, nhấn chọn **Create an user Account**;

**Bước 5:** Điền tên đăng nhập "Account User";

**Bước 6:** Điền mật khẩu muốn thiết lập cho Account User (hoặc nhấn auto generate để hệ thống tự tạo ra mật khẩu);

**Bước 7:** Nhấn "**Create User Account**" để xác nhận tạo thêm user.

{% hint style="info" %}
**Lưu ý:**&#x20;

* Sau khi truy cập thành công vào User Page, có thể user vẫn chưa được phân quyền sử dụng dịch vụ vCloudStack vì chưa được phân quyền chức năng sử dụng. Admin cần thực hiện việc [Phân quyền user sử dụng vCloudStack](quan-ly-truy-cap.md#id-3-phan-quyen-user-su-dung-vcloudstack) theo hướng dẫn bên dưới.
* Với những user tạo tài khoản ở màn hình User account, chỉ có thể [thực hiện gán policy ](quan-ly-truy-cap.md#id-3-phan-quyen-user-su-dung-vcloudstack)phân quyền bước 8 - cách 2&#x20;
{% endhint %}

***

## <mark style="color:blue;">3/ Phân quyền user sử dụng vCloudStack</mark>

Để Phân quyền (**Policy**) cho User có thể sử dụng hệ thống dịch vụ vCloudStack ở portal User Site và Admin Site, người quản trị (admin) cần thực hiện các bước như sau:

**Bước 1:** Quản trị viên truy cập vào trang chủ của VNG Cloud ([dashboard.console.vngcloud.vn](https://dashboard.console.vngcloud.vn/))

**Bước 2:** Chọn đến trang **IAM Portal** của IAM;

**Bước 3:** Tại thanh điều hướng bên trái, chọn mục **Policy**;

**Bước 4:** Tại màn hình danh sách Policy, để tạo policy cho user sử dụng vCloudStack, nhấn nút "**Create a Policy**";

**Bước 5:** Điền tên Policy và mô tả để nhận diện bộ Policy cho user, sau đó nhấn **Next**;

**Bước 6:** Admin tiến hành **cấu hình policy** theo Product, Action, Resource, Condition.

**Bước 7:** nhấn **Create Policy** để hoàn tất việc tạo policy

{% hint style="info" %}
**Lưu ý:**

* Nếu muốn phân quyền cho user sử dụng các chức năng tại màn hình User Site: hãy chọn Product _<mark style="color:blue;">`vcloudstack`</mark>_;
* Nếu muốn phân quyền cho user sử dụng các chức năng tại màn hình Admin Site: hãy chọn Product _<mark style="color:blue;">`vcloudstack-admin`</mark>_;
{% endhint %}

**Bước 8:** Sau khi đã tạo policy, có 02 cách để gán policy vào user:

* **Cách 1:** Tại màn hình danh sách **Policy**
  * Chọn vào policy muốn gán cho user;
  * Chọn tab **Policy usage**;
  * Nhấn nút **"Attach**";
  * Chọn những User, sau đó nhấn **Add** để thêm các user vừa chọn.
* **Cách 2:** Tại màn hình User Account
  * Chọn user muốn áp dụng policy vừa tạo;
  * Tại tab **Permission**, hiển thị các policy áp dụng cho user này;
  * Để thêm policy áp dụng, nhấn "**Attach Policies**";
  * Chọn những Policies, sau đó nhấn **Attach** để áp dụng policy cho user.
