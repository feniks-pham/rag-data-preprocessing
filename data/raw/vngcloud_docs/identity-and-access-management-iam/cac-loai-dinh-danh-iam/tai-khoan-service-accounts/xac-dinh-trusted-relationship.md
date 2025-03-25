# Xác định Trusted Relationship

Trusted Relationship là tính năng chia sẻ quyền giữa các **Root User Accounts** khác nhau, cho phép việc ủy quyền truy cập được điều chỉnh và bảo mật trên các thực thể quản trị riêng biệt. Với tính năng này, các **Root User Accounts** khác nhau có thể hợp tác trong khi vẫn duy trì tính riêng tư và ranh giới bảo mật. Tính năng này đặc biệt hữu ích trong các tình huống khi nhiều tổ chức hoặc nhóm cần làm việc cùng nhau trên các tài nguyên chia sẻ, đảm bảo sự hợp tác hiệu quả mà không đánh đổi tính bảo mật.

Để thiết lập Trusted Relationship giữa các Root User Account, bạn cần thực hiện các bước chính sau đây:

1. Thêm Trusted Relationships cho Service Account
2. Phân quyền Impersonate (mạo danh tài khoản) cho IAM User Account
3. IAM User Account thực hiện Impersonate (mạo danh tài khoản)

#### 1. Thêm Trusted Relationship cho Service Account <a href="#trustedrelationship-1.themtrustedrelationshipchoserviceaccount" id="trustedrelationship-1.themtrustedrelationshipchoserviceaccount"></a>

Trusted relationships giữa các Root User Account được thiết lập thông qua Service Account, điều đầu tiên cần làm là thêm **Trusted Relationships** (là các **Root User Account** được chia sẻ quyền) cho Service Account. Một ví dụ cụ thể là khi **Root User Account A** muốn thêm **Root User Account B** như là một **Trusted Partner** thông qua **Service Account** của nó.

1. Truy cập vào IAM bằng Root User Account A hoặc IAM User Account của Root A đã được phân quyền.
2. Thêm **Root User Account B là Trusted Partner** cho **Service Account**, theo 1 trong 2 cách sau đây:
   1.  Thêm khi tạo mới Service Account: điền ID của Root User Account vào field như hình bên dưới

       <figure><img src="https://docs.vngcloud.vn/download/attachments/63766845/image2023-7-27_15-13-9.png?version=1&#x26;modificationDate=1691054186000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
   2. Thêm cho một Service Account đã có: **Truy cập vào Service Account** cần chỉnh sửa → Truy cập vào tab **"Trusted Relationships"** → Nhấp vào nút **"Add trusted relationships"** → Điền **ID của Root User Account B**![](https://docs.vngcloud.vn/download/attachments/63766845/image2023-7-27\_15-19-27.png?version=1\&modificationDate=1691054186000\&api=v2)
3. Như vậy, bạn đã **thành công ủy quyền truy cập cho Root User Account B** thông qua một Service Account

\


**Tiếp theo, Root User Account B cần tiến hành ủy quyền truy cập đến một hoặc nhiều IAM User Account cụ thể của mình, theo dõi hướng dẫn bên dưới để biết thêm chi tiết.**

#### 2. Phân quyền Impersonate (mạo danh tài khoản) cho IAM User Account <a href="#trustedrelationship-2.phanquyenimpersonate-maodanhtaikhoan-choiamuseraccount" id="trustedrelationship-2.phanquyenimpersonate-maodanhtaikhoan-choiamuseraccount"></a>

Đầu tiên, chúng tôi khuyến nghị bạn nên tìm hiểu cách [**Quản lý Truy cập (Access Management)**](../../quan-ly-truy-cap-iam/chinh-sach-vng-managed-policy.md) thông qua **Chính sách (Policy)** trước khi đi sâu vào hướng dẫn bên dưới.

**Để phân quyền Impersonate (mạo danh tài khoản) cho IAM User Account:**

1. Truy cập vào IAM Root User Account B hoặc IAM User Account đã được cấp quyền.
2. **Tạo một Policy mới** chứa Quyền **Impersonate a Service account** với các thông tin như sau:
   1. **Product** là IAM.
   2. **Action** (Effect Allow Permission) phải bao gồm **ImpersionateServiceAccount.**
   3. Chọn **Resource** áp dụng là **Tất cả / Các Service Account Cụ thể** (là Service Account được Root User Account A chia sẻ trước đó).
3. **Gán Policy vừa tạo** cho các IAM User Account được ủy quyền.
4. Bây giờ, các IAM User Account được ủy quyền thuộc Root User Account B có thể đại diện cho Service Account (chia sẻ bởi Root User Account A) và kế thừa tất cả quyền hạn từ Service Account này.

**Tiếp theo, làm thế nào để các IAM User Account được ủy quyền có thể mạo danh Service Account và truy cập đến các tài nguyên được cấp phép của Root User Account A, tham khảo hướng dẫn bên dưới để biết thêm chi tiết**

#### 3. IAM User Account thực hiện Impersonate (mạo danh tài khoản) <a href="#trustedrelationship-3.iamuseraccountthuchienimpersonate-maodanhtaikhoan" id="trustedrelationship-3.iamuseraccountthuchienimpersonate-maodanhtaikhoan"></a>

1. Truy cập vào IAM bằng IAM User Account của Root B (tài khoản được ủy quyền ở Bước 2).
2.  Nhấp vào "**Impersonate service account**" trong danh sách thả xuống như hình ảnh dưới đây.

    <figure><img src="https://docs.vngcloud.vn/download/thumbnails/63766845/image2023-7-27_16-59-34.png?version=1&#x26;modificationDate=1691054186000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
3.  Nhập **ID của Service Account** được chia sẻ bởi Root User Account A (ở bước 1) và Tên hiển thị. Sau đó, nhấn vào nút "**Go**" để hoàn tất quy trình. Dưới đây là hình ảnh hướng dẫn:

    <figure><img src="https://docs.vngcloud.vn/download/thumbnails/63766845/image2023-7-27_17-6-36.png?version=1&#x26;modificationDate=1691054186000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
4. Sau khi thành công trong việc mạo danh, IAM User Account của Root B có thể thực hiện tất cả các quyền giống như Service Account được chia sẻ bởi Root A. Điều này cho phép IAM User Account được ủy quyền này truy cập vào các tài nguyên và dịch vụ cụ thể mà Service Account được cấp quyền bởi Root A.
