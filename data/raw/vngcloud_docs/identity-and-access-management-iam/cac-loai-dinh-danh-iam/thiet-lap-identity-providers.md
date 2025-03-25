# Thiết lập Identity Providers

Identity Provider là tính năng cho phép bạn quản lý tài nguyên trên VNG Cloud với tập người dùng trên hệ thống xác thực của doanh nghiệp, giúp doanh nghiệp quản lý tập trung user và không cần phải tạo thêm các IAM user accounts trên VNG Cloud.  IAM hỗ trợ giao thức SAML2.0 để giao tiếp với các hệ thống xác thực, hiện tại mới chỉ hỗ trợ với Azure AD.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/Identities-IDP.drawio%20(1).png?version=1&#x26;modificationDate=1691474720000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

### **Tại sao cần sử dụng Identity Provider?** <a href="#identityproviders-taisaocansudungidentityprovider" id="identityproviders-taisaocansudungidentityprovider"></a>

Để hiểu rõ hơn về cách hoạt động cũng như lợi ích của việc sử dụng IAM Identity Provider trong doanh nghiệp, chúng tôi đưa ra tình huống cụ thể giúp người dùng có cái nhìn chi tiết hơn như sau:

**Ngữ cảnh**

* **Doanh nghiệp A** có 10 nhân viên, được quản lý thông qua tài khoản microsoft với tên **nhanvien1 → nhanvien10.**
* **Doanh nghiệp A** được cơ cấu thành 3 phòng ban, bao gồm: **Phòng Hành Chính - Kế Toán, Phòng IT và Phòng Kinh Doanh.**
* **Doanh nghiệp A** có sử dụng dịch vụ điện toán đám mây của VNG Clou&#x64;**,** bao gồ&#x6D;**: vServer, vStorage và vMonitor.**

**Nhu cầu**

**Nhu cầu Single Sign-On:** Đơn giản hóa việc truy cập vào hệ thống VNG Cloud bằng việc sử dụng duy nhất tài khoản doanh nghiệp

**Giải pháp**

Với nhu cầu trên, việc sử dụng tính năng **Identity Provider** do chúng tôi cung cấp sẽ giúp quý doanh nghiệp tiết kiệm thời gian, cũng như đơn giản hóa việc quản lý quyền hạn và định danh nhân viên trên hệ thống VNG Cloud. Tham khảo hướng dẫn dưới đây trong việc giải quyết nhu cầu trên của quý doanh nghiệp

### **Sử dụng Identity Provider như thế nào?** <a href="#identityproviders-sudungidentityprovidernhuthenao" id="identityproviders-sudungidentityprovidernhuthenao"></a>

Để sử dụng Identity Provider bạn cần thực hiện các bước sau:

1. Thiết lập Identity Provider từ bên đối tác **(Azure AD)**
2. Thiết lập kết nối Identity Provider từ **VNG Cloud**
3. Truy cập **Azure AD** để thiết lập kết nối từ Identity Provider tới VNG Cloud IAM bằng việc sử dụng thông tin SAML entity ID và Reply URL
4. Hoàn tất thiết lập, sử dụng Login URL tại IAM để **đăng nhập vào VNG Cloud** bằng **tài khoản trên Azure AD** của quý doanh nghiệp

#### 1. Thiết lập Identity Provider từ bên đối tác (Azure AD) <a href="#identityproviders-1.thietlapidentityprovidertubendoitac-azuread" id="identityproviders-1.thietlapidentityprovidertubendoitac-azuread"></a>

Hiện tại IAM VNG Cloud chỉ hỗ trợ Azure AD với giao thức SAML 2.0, để thiết lập Identity Provider giữa VNG Cloud và Azure ID, bạn cần làm theo các hướng dẫn sau đây:

1. Truy cập vào Azure Home page với URL: [https://portal.azure.com/#home](https://portal.azure.com/#home)
2. Nhấn chọn **"Azure Active Directory"** tại thanh Menu bên trái. Lưu ý rằng bạn cần có quyền để truy cập vào Azure AD của doanh nghiệp mình
3.  Chọn **New application** tại tab **Enterprise Application,** sau đó chọn **Create your own application**, đặt tên cho app và nhấn **Create** tương tự hình hướng dẫn bên dưới:

    Lưu ý

    * Ứng dụng được khởi tạo sẽ tương ứng với **phòng IT của doanh nghiệp**
    * Cần thêm các nhân viên thuộc phòng IT vào ứng dụng, bao gồm: **nhanvien1 và nhanvien2**

    <figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/image2023-6-13_17-16-29.png?version=1&#x26;modificationDate=1690515611000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
4.  Khi hoàn tất khởi tạo ứng dụng, truy cập vào mục **Single sign-on**, chọn giao thức **SAML**:

    <figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/image2023-6-13_17-18-2.png?version=1&#x26;modificationDate=1690516829000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
5. Tiếp theo, **sao chép đường dẫn Login** (như hình bên dưới) và tiếp tục thiết lập kết nối từ phía VNG Cloud tới Azure AD (hướng dẫn tại mục số 2)

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/image2023-6-13_17-19-17.png?version=1&#x26;modificationDate=1690517088000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

#### 2. Thiết lập kết nối Identity Provider từ VNG Cloud <a href="#identityproviders-2.thietlapketnoiidentityprovidertuvngcloud" id="identityproviders-2.thietlapketnoiidentityprovidertuvngcloud"></a>

Sau khi có được thông tin Login URL từ Azure AD, bạn tiếp tục thiết lập kết nối với các bước như bên dưới:

1. Truy cập đến IAM Identity Provider với URL: [https://hcm-3.console.vngcloud.vn/iam/identity-providers](https://hcm-3.console.vngcloud.vn/iam/identity-providers)
2. Chọn **Add an Identity Provider**
3. Điền các thông tin cho Identity Provider bao gồm:&#x20;
   * **Provider Name:** tên của Identity Provider
   * **Provider Type:** để mặc định, hiện tại chỉ hỗ trợ SAML
   * **Vendor:** để mặc định, hiện tại chỉ hỗ trợ Azure AD
   * **Login URL:** là thông tin Login URL lấy từ app mà bạn đã có từ bước 1.5
4. Nhấn nút **Create** để tạo Identity Provider
5. Khi tạo xong bạn sẽ lấy 2 thông tin **SAML entity ID** và **Reply URL** như hình bên dưới và tiến hành bước 3 (Thiết lập kết nối từ Identity Provider đến VNG Cloud IAM)

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/image2023-6-13_15-40-49.png?version=1&#x26;modificationDate=1690517552000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

#### 3. **Thiết lập kết nối từ Identity Provider tới VNG Cloud IAM sử dụng thông tin SAML entity ID và Reply URL** <a href="#identityproviders-3.thietlapketnoituidentityprovidertoivngcloudiamsudungthongtinsamlentityidvareplyu" id="identityproviders-3.thietlapketnoituidentityprovidertoivngcloudiamsudungthongtinsamlentityidvareplyu"></a>

Khi đã có 2 thông tin: **SAML entity ID** và **Reply URL,** bạn quay trở lại Azure AD để thiết lập kế nối, và làm theo các hướng dẫn bên dưới:

1.  Truy cập vào Apps đã khởi tạo trước đó, vào mục **Single-sign on,** chọn **Edit** tại mục **Basic SAML Configuration** như hình bên dưới:

    <figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/image2023-6-13_17-21-29.png?version=1&#x26;modificationDate=1690518028000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
2. Điền thông tin **SAML entity ID** và **Reply URL đã có từ bước 2** vào các trường phù hợp như bên dưới và chọn **Save**

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/image2023-6-13_17-23-47.png?version=1&#x26;modificationDate=1690518979000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Thông báo

* Sau khi thực hiện từ bước 1 đến bước 3, bạn đã hoàn thành việc kết nối giữa Azure AD và VNG Cloud IAM.
* Tiếp tục làm theo hướng dẫn tại **bước số 4** để sử dụng Login URL tại IAM (bỏ qua nếu đã biết cách sử dụng tính năng này)

#### 4. **Sử dụng Login URL tại IAM để đăng nhập vào VNG Cloud bằng user trên Azure AD của quý doanh nghiệp** <a href="#identityproviders-4.sudungloginurltaiiamdedangnhapvaovngcloudbangusertrenazureadcuaquydoanhnghiep" id="identityproviders-4.sudungloginurltaiiamdedangnhapvaovngcloudbangusertrenazureadcuaquydoanhnghiep"></a>

Sau khi tạo xong, tài khoản doanh nghiệp có thể **sử dụng đường link tại VNG Login URL** (như hình bên dưới) để thực hiện đăng nhập vào VNG Cloud bằng user trên Azure AD của doanh nghiệp, hệ thống IAM sẽ tự động tạo user sau khi bạn đăng nhập, và **mặc định sẽ không có quyền gì như các IAM user account khác**.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806696/image2023-6-13_14-35-57.png?version=1&#x26;modificationDate=1690519768000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}


Lưu ý

* **nhanvien1 và nhanvien2** chỉ có thể đăng nhập vào hệ thống VNG Cloud thông qua URL đăng nhập.
* **nhanvien1 và nhanvien2** cần đăng nhập lần đầu tiên vào hệ thống VNG Cloud thông qua URL để hệ thống tự động khởi tạo các IAM User Accounts với tên tương ứng.
* **IAM User Account** được khởi tạo tương ứng với **nhanvien1 và nhanvien2** mặc định sẽ không có quyền gì trên hệ thống VNG Cloud. Do đó, Root User Account đại diện cho doanh nghiệp cần truy cập vào IAM Console để tiến hành phân quyền truy cập cho 2 IAM User Account này.
* Sau khi phân quyền thành công, nhanvien1 và nhanvien2 có thể truy cập vào hệ thống **VNG Cloud (vServer, vStorage và vMonitor)**
{% endhint %}

