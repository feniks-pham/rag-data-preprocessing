# Quản lý định danh và truy cập (IAM) cho vServer

Quản lý định danh và truy cập (IAM) cho máy ảo là một hệ thống quản lý và kiểm soát quyền truy cập vào các máy ảo (VM) và tài nguyên của chúng trong môi trường điện toán đám mây. Nó cung cấp một cách để kiểm soát ai có thể truy cập máy ảo và những hành động họ có thể thực hiện trên đó. Trước tiên, chúng tôi khuyên bạn nên xem lại các chủ đề giới thiệu các khái niệm cơ bản và các tùy chọn có sẵn để bạn quản lý quyền truy cập vào tài nguyên vServer của mình. Để biết thêm thông tin, hãy xem [IAM - Identity and Access Management](../../../identity-and-access-management-iam.md).

IAM dành cho máy ảo thường bao gồm các chức năng như quản lý định danh, xác thực, ủy quyền và kiểm tra. Nó cho phép quản trị viên xác định các chính sách chỉ định ai có thể truy cập máy ảo và những hành động họ có thể thực hiện trên máy ảo, chẳng hạn như khởi động, dừng hoặc sửa đổi máy ảo.

Trong môi trường điện toán đám mây, IAM dành cho máy ảo là một biện pháp kiểm soát bảo mật quan trọng vì máy ảo thường được sử dụng để lưu trữ dữ liệu nhạy cảm và chạy các ứng dụng kinh doanh quan trọng. Bằng cách kiểm soát quyền truy cập vào các tài nguyên này, IAM dành cho máy ảo giúp đảm bảo tính bảo mật, tính toàn vẹn và tính khả dụng của dữ liệu và dịch vụ của một tổ chức.&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59802235/image2023-5-17_17-31-9.png?version=1&#x26;modificationDate=1684319623000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

### Tổng quan <a href="#quanlydinhdanhvatruycap-iam-chovserver-tongquan" id="quanlydinhdanhvatruycap-iam-chovserver-tongquan"></a>

Bạn cần hoàn tất các bước sau để có thể sử dụng dịch vụ IAM cho sản phẩm vServer của chúng tôi:

***

### **Bước 1: Xác định yêu cầu của bạn:** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc1-xacdinhyeucaucuaban" id="quanlydinhdanhvatruycap-iam-chovserver-buoc1-xacdinhyeucaucuaban"></a>

* Xác định mức độ kiểm soát truy cập bạn cần cho máy chủ và các tài nguyên của mình.
* Xác định vai trò và trách nhiệm của những người dùng hoặc nhóm người dùng khác nhau.
* Xác định các quyền và đặc quyền cần thiết cho từng vai trò hoặc nhóm người dùng.

***

### **Bước 2: Chọn giải pháp và lập kế hoạch chiến lược IAM phù hợp** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc2-chongiaiphapvalapkehoachchienluociamphuhop" id="quanlydinhdanhvatruycap-iam-chovserver-buoc2-chongiaiphapvalapkehoachchienluociamphuhop"></a>

* Nghiên cứu và chọn giải pháp IAM đáp ứng yêu cầu của bạn.
* Tạo một kế hoạch để triển khai IAM trên máy chủ và tài nguyên của bạn
* Xác định các chính sách để xác thực và ủy quyền người dùng.

***

### **Bước 3: Tạo tài khoản người dùng (User account) trên hệ thống IAM** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc3-taotaikhoannguoidung-useraccount-trenhethongiam" id="quanlydinhdanhvatruycap-iam-chovserver-buoc3-taotaikhoannguoidung-useraccount-trenhethongiam"></a>

Sau khi thiết lập kế hoạch chiến lược IAM, bạn cần tạo Tạo tài khoản **người dùng cá nhân (User account)** trên trang chủ **IAM** của chúng tôi từ tài khoản **Root user account** của bạn cho từng người cần truy cập vào máy chủ:

1. Truy cập vào trang chủ IAM: [tại đây](https://hcm-3.console.vngcloud.vn/iam/)
2. Mở tab User account
3. Chọn **Create a user account.**
4. Ở mục **Account user name ,** hãy nhập **Tên** cho User account của bạn. Tên User account phải dài từ 5 đến 50 ký tự và chỉ được chứa chữ cái, chữ số, dấu gạch dưới (\_), dấu chấm (.), dấu gạch ngang (-).
5. Nhập mật khẩu cho User account tại mục **Account password** (Mật khẩu phải dài từ 8 đến 50 ký tự. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 số, 1 ký tự đặc biệt), cần thiết lập mật khẩu mạnh và duy nhất cho mỗi tài khoản người dùng.

***

### **Bước 4: Thiết lập nhóm người dùng (Group)** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc4-thietlapnhomnguoidung-group" id="quanlydinhdanhvatruycap-iam-chovserver-buoc4-thietlapnhomnguoidung-group"></a>

Tiếp theo bạn cần Tạo nhóm người (Group) dùng dựa trên vai trò hoặc trách nhiệm chung:

1. Mở tab Group tại [https://hcm-3.console.vngcloud.vn/iam/user-groups](https://hcm-3.console.vngcloud.vn/iam/user-groups).
2. Chọn **Create a group.**
3. Nhập tên Group vào mục **Name** (Tên phải dài từ 1 đến 50 ký tự và chỉ có thể bao gồm các chữ cái, số, dấu gạch dưới (\_), dấu chấm (.), dấu gạch nối (-) và dấu cách), sau đó nhập thông tin ghi chú tại mục **Description.**
4. Chuyển sang bước kế tiếp và gán chính sách (Policy) phù hợp cho nhóm người dùng tại mục **Policy (**&#x4E;ếu chưa có Policy cần tạo Policy theo hướng dẫn **Bước 5)**, sau đó chỉ định người dùng thích hợp vào nhóm tại mục **User**, với các User được thêm vào nhóm sẽ có quyền trên Policy đã chọn trong Group

***

### **Bước 5: Xác định chính sách truy cập (Policies)** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc5-xacdinhchinhsachtruycap-policies" id="quanlydinhdanhvatruycap-iam-chovserver-buoc5-xacdinhchinhsachtruycap-policies"></a>

Tạo chính sách truy cập chỉ định những hành động mà mỗi nhóm người dùng hoặc vai trò có thể thực hiện, hãy xác định chi tiết các quyền để hạn chế truy cập không cần thiết và thường xuyên xem xét và cập nhật các chính sách truy cập khi cần thiết:

1. Mở tab Policy tại [https://hcm-3.console.vngcloud.vn/iam/policies](https://hcm-3.console.vngcloud.vn/iam/policies).
2. Chọn **Create a Policy.**
3. Nhập tên Policy vào mục **Name** (Tên phải dài từ 1 đến 50 ký tự và chỉ có thể bao gồm các chữ cái, số, dấu gạch dưới (\_), dấu chấm (.), dấu gạch nối (-) và dấu cách), sau đó nhập thông tin ghi chú tại mục **Description.**
4. Chuyển sang bước kế tiếp, chọn sản phẩm **vserver** tại mục **Product**, sau đó chọn danh sách các quyền cho chính sách của bạn tại mục **Action.** Lưu ý rằng nếu tùy chọn **Allow permissions** được bật mang ý nghĩa người dùng được cấp phép sử dụng các quyền được chọn trong chính sách, nếu Allow permission ở chế độ tắt (**Deny permissions**) người dùng sẽ bị từ chối trên các quyền được chọn trong chính sách.
5. Tiếp tục chọn các tài nguyên bạn muốn áp dụng cho các quyền đã chọn ở danh sách phía trên tại mục **Resource**, tại đây có thể tùy chọn cho tất cả tài nguyên hoặc tài nguyên riêng biệt được chỉ định
6. Chọn các điều kiện cần để thực hiện các quyền trên tại mục **Request conditions**
7. **Tạo chính sách Policy**

Quan trọng

Để xem thông tin chi tiết và ý nghĩa của hành động (Action), tài nguyên (Resource), và điều kiện cần (Request conditions) nhằm thiết lập bộ chính sách truy cập (Policies) hoàn chỉnh, vui lòng xem nội dung tại [trang cấu hình Policies](cac-hanh-dong-tai-nguyen-va-dieu-kien-can-cho-phan-quyen-truy-cap-vserver.md)

***

### **Bước 5.1: Tạo Service account (Cho việc sử dụng Terraform)** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc5.1-taoserviceaccount-choviecsudungterraform" id="quanlydinhdanhvatruycap-iam-chovserver-buoc5.1-taoserviceaccount-choviecsudungterraform"></a>

Các bước trên chỉ cho phép chúng ta khởi tạo User account để đăng nhập vào trình điều khiển vServer và trực tiếp khởi tạo tài nguyên tại đó, trường hợp bạn muốn khởi tạo các tài nguyên thuộc đám mây của VNG Cloud bằng **Terraform**, bạn cần phải khởi tạo một **Service Account**:

1. Mở tab Service account tại [https://hcm-3.console.vngcloud.vn/iam/service-accounts](https://hcm-3.console.vngcloud.vn/iam/service-accounts)
2. Chọn **Create a service account**
3. Nhập tên Service account vào mục **Name** (Tên phải dài từ 1 đến 50 ký tự và chỉ có thể bao gồm các chữ cái, số, dấu gạch dưới (\_), dấu chấm (.), dấu gạch nối (-) và dấu cách), sau đó nhập thông tin ghi chú tại mục **Description.**
4. Có thể tùy chọn thêm Root user account vào mục **Trusted relationship** (Không bắt buộc)
5. Gán chính sách Policy phù hợp&#x20;
6. Chọn **Create service account**
7. **Cần** lưu lại thông tin **Client ID & Client Secret** để sử dụng cho việc quản lý các tài nguyên bằng Terraform sau này

***

### **Bước 6: Gán chính sách (Policy) vào User account / Group/ Service account** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc6-ganchinhsach-policy-vaouseraccount-group-serviceaccount" id="quanlydinhdanhvatruycap-iam-chovserver-buoc6-ganchinhsach-policy-vaouseraccount-group-serviceaccount"></a>

Sau khi tạo chính sách với các quyền phù hợp, người dùng cần gán chính sách đã tạo cho **User account/ Group/ Service account** phù hợp với các chức năng hoặc trách nhiệm công việc, chỉ định người dùng cho các vai trò dựa trên chức năng công việc của họ, từ đó có thể nhóm các **User account** có quyền giống nhau vào **Group:**

1. **Mở tab User account tại:** [**https://hcm-3.console.vngcloud.vn/iam/user-accounts**](https://hcm-3.console.vngcloud.vn/iam/user-accounts)
2. Chọn User account muốn gán quyền, sau đó tại trang chi tiết User account chọn **Attach Policies** và lựa chọn chính sách Policy muốn gán cho User account phù hợp với nhu cầu của bạn
3. Tương tự ta có thể gán quyền cho **Group/ Service account** tại trang chi tiết hoặc gán Policy khi khởi tạo chúng

***

### **Bước 7: Truy cập vào vServer sử dụng IAM account (User account)** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc7-truycapvaovserversudungiamaccount-useraccount" id="quanlydinhdanhvatruycap-iam-chovserver-buoc7-truycapvaovserversudungiamaccount-useraccount"></a>

Bước cuối cùng là sử dụng **IAM User Account** truy cập vào tài nguyên vServer qua vServer portal:

1. Truy cập vào đường dẫn: [https://dashboard.console.vngcloud.vn/](https://dashboard.console.vngcloud.vn/)
2. Nếu trước đây bạn chưa đăng nhập bằng trình duyệt này, trang đăng nhập chính sẽ xuất hiện. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**.
3. Nhập địa chỉ **email** của người dùng Root khi đăng ký tài khoản VNG Cloud.
4. Nhập **tên người dùng** và **mật khẩu** của tài khoản IAM user account (User account) được tạo trên hệ thống IAM.
5. Chọn **ĐĂNG NHẬP VỚI IAM USER ACCOUNT**.\
   Nếu trước đó bạn đã đăng nhập với tư cách người dùng IAM user account trong trình duyệt này, thì trình duyệt của bạn có thể nhớ địa chỉ tài khoản IAM user account. Nếu vậy, bạn sẽ thấy màn hình hiển thị ở bước 3. \
   Sau khi đăng nhập thành công với IAM user account, trên màn hình chính của vServer sẽ thể hiện loại user mà bạn đang sử dụng để đăng nhập (Root user account hay IAM user account). Bạn có thể truy nhập vào tài nguyên đã được phân quyền theo Policy để sử dụng các chức năng của chúng.

***

### **Bước 8: Thường xuyên xem xét và kiểm tra quyền truy cập** <a href="#quanlydinhdanhvatruycap-iam-chovserver-buoc8-thuongxuyenxemxetvakiemtraquyentruycap" id="quanlydinhdanhvatruycap-iam-chovserver-buoc8-thuongxuyenxemxetvakiemtraquyentruycap"></a>

* Tiến hành kiểm tra định kỳ quyền truy cập và quyền của người dùng.
* Xóa mọi đặc quyền truy cập không cần thiết.
* Thường xuyên xem xét tài khoản người dùng và chính sách truy cập và thay đổi nếu cần thiết để đảm bảo chúng phù hợp với các yêu cầu hiện tại.
