# Các trường hợp sử dụng IAM

Bài viết sau đây mô tả về một trường hợp sử dụng kinh doanh đơn giản cho IAM có thể giúp bạn hiểu cách triển khai dịch vụ để kiểm soát quyền truy cập của người dùng vào các dịch vụ VNG Cloud mà bạn sử dụng. Ví dụ này mô tả hai cách thức mà công ty Example có thể áp dụng IAM, bao gồm việc sử dụng VNG Cloud vServer.

***

## **Thiết lập ban đầu** <a href="#cactruonghopsudungiam-thietlapbandau" id="cactruonghopsudungiam-thietlapbandau"></a>

Sasha Nguyen và Alex Thompson những người đồng sáng lập Công ty Example. Khi thành lập công ty, họ hiểu tầm quan trọng của hệ thống quản lý truy cập danh tính mạnh mẽ để bảo vệ tài nguyên của mình. Họ đã quyết định triển khai Quản lý truy cập danh tính (IAM) cho tổ chức của mình để đảm bảo rằng chỉ những người có quyền truy cập cần thiết mới có thể truy cập vào các tài nguyên và dịch vụ của công ty.

Đầu tiên Sasha và Alex đã tạo tài khoản VNG Cloud (Root user account). Sau đó, họ dùng tài khoản này truy cập vào dịch vụ IAM. Tài khoản này của họ và được đính kèm với các chính sách từ bộ quyền (Policy) AdministratorAccess, đồng nghĩa với việc sở hữu Root user account họ sẽ có toàn quyền trên tất cả tài nguyên và dịch vụ của Công ty.

Khi Công ty mở rộng, Sasha và Alex bắt đầu thuê nhân viên với nhiều vị trí trong Công ty. Sasha nhận trách nhiệm giám sát hoạt động của công ty, trong khi Alex quản lý các nhóm kỹ sư. Tuy nhiên họ không thể cấp quyền sử dụng Root user account cho các nhân viên này, vì điều đó đồng nghĩa với việc một số thứ sẽ vượt quá quyền hạn của từng vị trí công việc, lúc này điều cần làm là họ phải cấp cho nhân viên tài khoản User account từ Root user account trên trang chủ IAM với quyền hạn chuyên biệt để truy cập vào tài nguyên và sử dụng chúng.&#x20;

Đầu tiên, họ xác định các vai trò khác nhau trong công ty. Ví dụ, họ có vai trò cho các nhà phát triển, quản trị viên mạng, quản trị viên cơ sở dữ liệu và nhân viên hỗ trợ. Mỗi vai trò này sẽ có quyền truy cập khác nhau vào các tài nguyên và dịch vụ của công ty. Sau đó, Sasha và Alex tạo ra các User account nhóm người dùng (Group) tương ứng với từng vai trò. Nhóm người dùng này sẽ chứa các nhân viên có cùng quyền truy cập và vai trò, bằng cách này họ có thể dễ dàng quản lý quyền truy cập cho từng nhóm.

Để quản lý quyền truy cập, Sasha và Alex sử dụng các chính sách IAM. Họ định rõ những gì mà mỗi vai trò và nhóm người dùng có thể làm và không thể làm. Họ phải chỉ định các nhóm quyền và vai trò cho các nhóm khác nhau để cung cấp cho người dùng cấp truy cập chính xác vào tài nguyên VNG Cloud. Họ sử dụng các chính sách do VNG Cloud quản lý cho các chức năng công việc trong Bảng điều khiển quản lý IAM để tạo các nhóm quyền sau:

* _Administrator_
* _Billing_
* _Developers_
* _Network administrators_
* _Database administrators_
* _System administrators_
* _Support users_

Sau đó họ gán các chính sách này cho các User account hoặc Group với vai trò tương ứng và cấp Username & password của User account cho nhân viên để tiến hành truy cập sử dụng các dịch vụ và tài nguyên.

Để hướng dẫn việc triển khai Trung tâm nhận dạng IAM, Sasha và Alex đã tham khảo phần "[Bắt đầu](./)" toàn diện trong Hướng dẫn sử dụng Trung tâm nhận dạng VNG Cloud IAM. Hướng dẫn từng bước này cung cấp cho họ hướng dẫn chi tiết về cấu hình ban đầu. Ngoài ra, họ đã tham khảo phần "[Danh sách phân quyền vào tài khoản VNG Cloud](cac-hanh-dong-tai-nguyen-va-dieu-kien-can-cho-phan-quyen-truy-cap-vserver.md)" của hướng dẫn sử dụng để hiểu rõ hơn về việc cung cấp quyền truy cập của người dùng trong Trung tâm nhận dạng IAM.

Khi Công ty đổi mới tiếp tục phát triển, Sasha và Alex vẫn thận trọng trong việc xem xét và cập nhật quyền truy cập cho từng nhân viên. Họ thường xuyên điều chỉnh quyền và cấp độ truy cập để đảm bảo rằng nhân viên có đặc quyền truy cập phù hợp với vai trò và trách nhiệm của họ trong tổ chức hoặc thu hồi lại nếu cần thiết.

***

## **Trường hợp sử dụng IAM với vServer** <a href="#cactruonghopsudungiam-truonghopsudungiamvoivserver" id="cactruonghopsudungiam-truonghopsudungiamvoivserver"></a>

Một công ty như Example thường sử dụng IAM để tương tác với các dịch vụ như VNG Cloud vServer. Để hiểu phần này của trường hợp sử dụng, bạn cần có hiểu biết cơ bản về VNG Cloud vServer. Để biết thêm thông tin về VNG Cloud vServer, hãy xem [Hướng dẫn sử dụng vServer](../trai-nghiem-san-pham-vserver/).

### **Quyền vServer cho nhóm người dùng** <a href="#cactruonghopsudungiam-quyenvserverchonhomnguoidung" id="cactruonghopsudungiam-quyenvserverchonhomnguoidung"></a>

Tại Example, các nhóm người dùng khác nhau yêu cầu các quyền khác nhau:

<table data-header-hidden><thead><tr><th width="166"></th><th width="181"></th><th></th></tr></thead><tbody><tr><td><strong>Nhóm quyền</strong></td><td><strong>Phân quyền</strong></td><td><strong>Mô tả</strong></td></tr><tr><td><strong>System Administrator</strong></td><td>vServerFullAccess</td><td>Nhóm người dùng này thường yêu cầu nhiều quyền để quản lý tất cả các khía cạnh của tài nguyên. Họ có thể cần quyền để tạo và quản lý tài nguyên, định cấu hình mạng, thiết lập kiểm soát bảo mật cũng như quản lý chính sách và vai trò IAM. Vì thế họ cần có quyền để tạo và quản lý Image, Server, VPC, Volume, Security Group, v.v. Alex đính kèm chính sách được quản lý vServerFullAccess cho nhóm người dùng <em>Quản trị viên hệ thống</em> để cấp cho các thành viên của nhóm quyền sử dụng tất cả các hành động của vServer.</td></tr><tr><td><strong>Developer</strong></td><td>ListServer, GetServer, StartServer, StopServer, RebootServer</td><td>Chỉ cần khả năng làm việc với các Server đó. Do đó, Alex tạo và đính kèm một chính sách cho nhóm người dùng Nhà phát triển cho phép các nhà phát triển gọi các quyền sau: ListServer, GetServer, StartServer, StopServer, RebootServer</td></tr><tr><td><strong>Support</strong></td><td>vServerReadOnlyAccess</td><td>Không thể thực hiện bất kỳ hành động nào của vServer ngoại trừ liệt kê các tài nguyên vServer hiện có. Do đó, Alex tạo và đính kèm một chính sách cho nhóm người dùng Hỗ trợ chỉ cho phép họ gọi vServerReadOnlyAccess.</td></tr></tbody></table>

***

### **Phân quyền System Administrator cho nhóm người dùng** <a href="#cactruonghopsudungiam-phanquyensystemadministratorchonhomnguoidung" id="cactruonghopsudungiam-phanquyensystemadministratorchonhomnguoidung"></a>

Taylor Smith được tuyển dụng với vị trí của người quản lý dự án, vì thế anh ấy cần có quyền truy cập vào tất cả các tài nguyên của công ty để quản lý quyền truy cập và triển khai các dự án công nghệ thông tin liên quan đến hạ tầng VNG Cloud vì thế Alex đã cấp cho Taylor User account với quyền vServerFullAccess theo các bước thực hiện bên dưới:

#### **Bước 1: Tạo tài khoản người dùng (User account) trên hệ thống IAM** <a href="#cactruonghopsudungiam-buoc1-taotaikhoannguoidung-useraccount-trenhethongiam" id="cactruonghopsudungiam-buoc1-taotaikhoannguoidung-useraccount-trenhethongiam"></a>

1. Alex tạo tài khoản VNG Cloud tại trang chủ: [https://sso.vngcloud.vn/cas/login?service=https%3A%2F%2Fportal3.vngcloud.vn%2F](https://sso.vngcloud.vn/cas/login?service=https%3A%2F%2Fportal3.vngcloud.vn%2F) \
   với thông tin Root user account: **Admin@vngcloud.vn**, password: **12345678@!**
2. Điều hướng sang trang chủ IAM tại: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) sử dụng thông tin Root user account để đăng nhập
3. Mở tab User account.
4. Chọn **Create a user account.**
5. Ở mục **Account user name,** Alex nhập **Tên** cho User account là **Sysad01**
6. Nhập mật khẩu cho User account tại mục **Account password**
7. Sau đó nhấn **Create User Account**.\
   Tại đây **Alex** tạo User account riêng biệt cho **Taylor** bao gồm các thông tin sa&#x75;**:**\
   **User account:** Username: **Sysad01 ;** Pasword: **Asddehj**\


#### **Bước 2: Tạo nhóm người dùng Group**  <a href="#cactruonghopsudungiam-buoc2-taonhomnguoidunggroup" id="cactruonghopsudungiam-buoc2-taonhomnguoidunggroup"></a>

Sau khi tạo User account, Alex tiếp tục tạo nhóm người dùng **Group:**

1. Mở tab Group tại [https://hcm-3.console.vngcloud.vn/iam/user-groups](https://hcm-3.console.vngcloud.vn/iam/user-groups).
2. Chọn **Create a group.**
3. Alex nhập tên Group là **SysAd** vào mục **Name,** sau đó nhập thông tin ghi chú tại mục **Description.**
4. Chuyển sang bước kế tiếp. Tại mục **User, Alex** chọn User account **Sysad01** thêm vào **Group**
5. Sau đó nhấn **Create a Group**\
   Một Group tên **SysAd** sẽ được tạo bao gồm User account: **Sysad01**

#### **Bước 3: Gán quyền vào nhóm người dùng**  <a href="#cactruonghopsudungiam-buoc3-ganquyenvaonhomnguoidung" id="cactruonghopsudungiam-buoc3-ganquyenvaonhomnguoidung"></a>

Hiện nay IAM cung cấp một số bộ quyền mặc định giúp người dùng có thể thiết lập phân quyền truy cập một cách nhanh chóng và hiệu quả, vì thế với nhóm người dùng SysAd, Alex đã thực hiện thêm vào bộ quyền **vServerFullAccess** theo hướng dẫn bên dưới:

1. Mở tab Policy tại [https://hcm-3.console.vngcloud.vn/iam/policies](https://hcm-3.console.vngcloud.vn/iam/policies).
2. Nhấn vào xem chi tiết bộ quyền **vServerFullAccess** tại trang danh sách
3. Sau đó tại menu **Policy usage,** nhấn **Attach**
4. Tại **Tab Group, Alex** chọn nhóm **SysAd** và nhấn **Add**\
   Sau khi thực hiện thành công, chúng ta sẽ có nhóm SysAd bao gồm User account Sysad01 với bộ quyền vServerFullAccess

#### **Bước 4: Truy cập vào tài nguyên sử dụng IAM account (User account)** <a href="#cactruonghopsudungiam-buoc4-truycapvaotainguyensudungiamaccount-useraccount" id="cactruonghopsudungiam-buoc4-truycapvaotainguyensudungiamaccount-useraccount"></a>

Sau khi tạo User account: Sysad01, Alex đã cấp quyền sử dụng account này cho Taylor, anh ấy đã sử dụng để truy cập vào tài nguyên của Công ty và sử dụng chúng:

1. Truy cập vào bảng điều khiển vServer tại: [**https://hcm-3.console.vngcloud.vn/vserver/**](https://hcm-3.console.vngcloud.vn/vserver/)
2. Tại màn hình **Đăng nhập:** chọn **SIGNIN WITH IAM USER ACCOUNT**
3. Nhập thông tin **Root email: Admin@vngcloud.vn, User name: Sysad01, Password: Asddehj**
4. Màn hình sẽ điều hướng sang trang quản lý vServer, tại đây có thể thao tác vào các tài nguyên được cấp quyền trong Policy đã gán với User account

***

### **Phân quyền Developer cho nhóm người dùng** <a href="#cactruonghopsudungiam-phanquyendeveloperchonhomnguoidung" id="cactruonghopsudungiam-phanquyendeveloperchonhomnguoidung"></a>

Nhân viên Johnson Miles và Scott Enzi gia nhập công ty với tư cách một Developer, vì thế họ cần có quyền để làm việc với các Server như xem danh sách, khởi chạy hay dừng Server, tuy nhên họ không thể tạo hoặc thay đổi cấu hình Server và xem các thông tin thanh toán của chúng , do đó Alex đã cấp cho họ tài khoản User account thuộc nhóm người dùng Devs với bộ quyền Developer. Sau đó Johnson và Scott có thể dùng tên đăng nhập và mật khẩu của User account để truy cập và sử dụng vào tài nguyên được cấp quyền:

#### **Bước 1: Tạo tài khoản người dùng (User account) trên hệ thống IAM** <a href="#cactruonghopsudungiam-buoc1-taotaikhoannguoidung-useraccount-trenhethongiam.1" id="cactruonghopsudungiam-buoc1-taotaikhoannguoidung-useraccount-trenhethongiam.1"></a>

1. Truy cập trang chủ IAM tại: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/).
2. Sau đó mở tab User account.
3. Chọn **Create a user account.**
4. Ở mục **Account user name,** Alex nhập **Tên** cho User account là **Dev01**
5. Nhập mật khẩu cho User account tại mục **Account password**
6. Sau đó nhấn **Create User Account**.\
   Tại đây **Alex** tạo 2 User account riêng biệt cho **Johnson Miles** và **Scott Enzi** bao gồm các thông tin sa&#x75;**:**\
   **User account 1:** Username: **Dev01 ;** Pasword: **Asddehj1**\
   **User account 2:** Username: **Dev02 ;** Pasword: **Aseeeghe2**

#### **Bước 2: Tạo nhóm người dùng Group**  <a href="#cactruonghopsudungiam-buoc2-taonhomnguoidunggroup.1" id="cactruonghopsudungiam-buoc2-taonhomnguoidunggroup.1"></a>

Sau khi tạo User account, Alex tiếp tục tạo nhóm người dùng **Group:**

1. Mở tab Group tại [https://hcm-3.console.vngcloud.vn/iam/user-groups](https://hcm-3.console.vngcloud.vn/iam/user-groups).
2. Chọn **Create a group.**
3. Alex nhập tên Group là **DevGroup** vào mục **Name,** sau đó nhập thông tin ghi chú tại mục **Description.**
4. Chuyển sang bước kế tiếp. Tại mục **User, Alex** chọn 2 User account **Dev01** và **Dev02** thêm vào **Group**
5. Sau đó nhấn **Create a Group**\
   Một Group tên **DevGroup** sẽ được tạo bao gồm 2 User account: **Dev01** và **Dev02**

#### **Bước 3: Gán quyền vào nhóm người dùng**  <a href="#cactruonghopsudungiam-buoc3-ganquyenvaonhomnguoidung.1" id="cactruonghopsudungiam-buoc3-ganquyenvaonhomnguoidung.1"></a>

Sau khi tạo Group, cần tạo chính sách Policy để gán vào Group:

1. Mở tab Policy tại [https://hcm-3.console.vngcloud.vn/iam/policies](https://hcm-3.console.vngcloud.vn/iam/policies).
2. Tạo mới Policy bằng cách nhấn **Create a Policy**
3. Tại màn hình Information, ở mục **Name,** Alex nhập tên Policy là **Developers**
4. Chuyển sang bước **Permissions,** Alex chọn **Product: vServer**
5. Tại mục **Action,** Alex chọn quyền: **ListServer, GetServer, StartServer, StopServer, RebootServer**
6. Vì hiện tại Alex cấp cho nhóm Developer quyền vào tất cả Server nên sẽ chọn **All Resources** tại mục **Resource**
7. Sau đó nhấn **Create Policy** để tạo mới
8. Sau đó tại trang danh sách Policy, nhấn chọn Policy: Developers vừa khởi tạo
9. Tại trang chi tiết Policy, chọn **Tab** **Policy usage,** và nhấn **Attach**
10. Tại **Tab Group, Alex** chọn nhóm **DevGroup** và nhấn **Add**\
    Sau khi thực hiện thành công, chúng ta sẽ có nhóm **SysAd** bao gồm 2 User account **Dev01** và **Dev02** với bộ quyền Policy **Developers**

#### **Bước 4: Truy cập vào tài nguyên sử dụng IAM account (User account)** <a href="#cactruonghopsudungiam-buoc4-truycapvaotainguyensudungiamaccount-useraccount-.1" id="cactruonghopsudungiam-buoc4-truycapvaotainguyensudungiamaccount-useraccount-.1"></a>

Sau khi tạo 2 User account: Dev01, Dev02, Alex đã cấp quyền sử dụng account này cho Johnson và Scott, họ  đã sử dụng để truy cập vào tài nguyên của Công ty và sử dụng chúng:

1. Truy cập vào bảng điều khiển vServer tại: [**https://hcm-3.console.vngcloud.vn/vserver/**](https://hcm-3.console.vngcloud.vn/vserver/)
2. Tại màn hình **Đăng nhập:** chọn **SIGNIN WITH IAM USER ACCOUNT**
3. Nhập thông tin **Root email:** [**Admin@vngcloud.vn**](mailto:Admin@vngcloud.vn)**,** Username: **Dev01 ;** Pasword: **Asddehj1 /** Username: **Dev02 ;** Pasword: **Aseeeghe2**
4. Màn hình sẽ điều hướng sang trang quản lý vServer, tại đây có thể thao tác vào các tài nguyên được cấp quyền trong Policy đã gán với User account

***

### **Phân quyền Support cho nhóm người dùng** <a href="#cactruonghopsudungiam-phanquyensupportchonhomnguoidung" id="cactruonghopsudungiam-phanquyensupportchonhomnguoidung"></a>

#### **Bước 1: Tạo tài khoản người dùng (User account) trên hệ thống IAM** <a href="#cactruonghopsudungiam-buoc1-taotaikhoannguoidung-useraccount-trenhethongiam.2" id="cactruonghopsudungiam-buoc1-taotaikhoannguoidung-useraccount-trenhethongiam.2"></a>

1. Truy cập trang chủ IAM tại: [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/).
2. Sau đó mở tab User account.
3. Chọn **Create a user account.**
4. Ở mục **Account user name,** Alex nhập **Tên** cho User account là **Supo01**
5. Nhập mật khẩu cho User account tại mục **Account password**
6. Sau đó nhấn **Create User Account**.\
   Tại đây **Alex** tạo User account riêng biệt cho **Taylor** bao gồm các thông tin sa&#x75;**:**\
   **User account:** Username: **Supo01 ;** Pasword: **Asddehj3**

#### **Bước 2: Tạo nhóm người dùng Group**  <a href="#cactruonghopsudungiam-buoc2-taonhomnguoidunggroup.2" id="cactruonghopsudungiam-buoc2-taonhomnguoidunggroup.2"></a>

Sau khi tạo User account, Alex tiếp tục tạo nhóm người dùng **Group:**

1. Mở tab Group tại [https://hcm-3.console.vngcloud.vn/iam/user-groups](https://hcm-3.console.vngcloud.vn/iam/user-groups).
2. Chọn **Create a group.**
3. Alex nhập tên Group là **SupportGroup** vào mục **Name,** sau đó nhập thông tin ghi chú tại mục **Description.**
4. Chuyển sang bước kế tiếp. Tại mục **User, Alex** chọn User account **Supo01** thêm vào **Group**
5. Sau đó nhấn **Create a Group**\
   Một Group tên **SupportGroup** sẽ được tạo bao gồm User account: **Supo01**

#### **Bước 3: Gán quyền vào nhóm người dùng**  <a href="#cactruonghopsudungiam-buoc3-ganquyenvaonhomnguoidung.2" id="cactruonghopsudungiam-buoc3-ganquyenvaonhomnguoidung.2"></a>

Hiện nay IAM cung cấp một số bộ quyền mặc định giúp người dùng có thể thiết lập phân quyền truy cập một cách nhanh chóng và hiệu quả, vì thế với nhóm người dùng SupportGroup, Alex đã thực hiện thêm vào bộ quyền **vServerReadOnlyAccess** theo hướng dẫn bên dưới:

1. Mở tab Policy tại [https://hcm-3.console.vngcloud.vn/iam/policies](https://hcm-3.console.vngcloud.vn/iam/policies).
2. Nhấn vào xem chi tiết bộ quyền **vServerReadOnlyAccess** tại trang danh sách
3. Sau đó tại menu **Policy usage,** nhấn **Attach**
4. Tại **Tab Group, Alex** chọn nhóm **SupportGroup** và nhấn **Add**\
   Sau khi thực hiện thành công, chúng ta sẽ có nhóm SupportGroup bao gồm User account Supo01 với bộ quyền vServerReadOnlyAccess

#### **Bước 4: Truy cập vào tài nguyên sử dụng IAM account (User account)** <a href="#cactruonghopsudungiam-buoc4-truycapvaotainguyensudungiamaccount-useraccount-.2" id="cactruonghopsudungiam-buoc4-truycapvaotainguyensudungiamaccount-useraccount-.2"></a>

Sau khi tạo User account: Sysad01, Alex đã cấp quyền sử dụng account này cho Taylor, anh ấy đã sử dụng để truy cập vào tài nguyên của Công ty và sử dụng chúng:

1. Truy cập vào bảng điều khiển vServer tại: [**https://hcm-3.console.vngcloud.vn/vserver/**](https://hcm-3.console.vngcloud.vn/vserver/)
2. Tại màn hình **Đăng nhập:** chọn **SIGNIN WITH IAM USER ACCOUNT**
3. Nhập thông tin **Root email:** [**Admin@vngcloud.vn**](mailto:Admin@vngcloud.vn)**, User name: Supo01, Password: Asddehj3**
4. Màn hình sẽ điều hướng sang trang quản lý vServer, tại đây có thể thao tác vào các tài nguyên được cấp quyền trong Policy đã gán với User account

\
