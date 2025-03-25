# Quản lý người dùng

## Tổng quan

Việc quản trị người dùng truy cập và sử dụng hệ thống mạng là cực kỳ nhạy cảm và bảo mật, điều này càng quan trọng với hệ thống nội bộ cung cấp cho đối tượng là nhân viên của doanh nghiệp.&#x20;

Do đó, màn hình Quản lý người dùng (User Management) sẽ mô tả đầy đủ thông tin của người dùng đang sử dụng và vận hành vCloudStack, bao gồm các thông tin:

* **User ID**: mã định danh ID của người dùng trên vCloudStack;
* **Email**: email của người dùng;
* **Status**: Trạng thái hoạt động của người dùng:
  * "_Active_" là trạng thái người dùng đang hoạt động và vận hành trên vCloudStack;
  * "_Inactive_" là trạng thái người dùng bị tạm ngừng (deactive) sử dụng vCloudStack;
* **Roles**: vai trò của người dùng trên vCloudStack;
* **Created at**: Ngày thêm mới người dùng;
* **Updated at**: ngày cập nhật thông tin người dùng.

Với vai trò là người quản trị người dùng, tại giao diện này cho phép thực hiện các chức năng:

* <mark style="color:blue;">Mời người dùng mới</mark> (Invite User)
* <mark style="color:blue;">Thiết lập giới hạn sử dụng</mark> (Limit Quota)
* <mark style="color:blue;">Tạm ngừng tài khoản người dùng</mark> (Deactive)

Chi tiết thực hiện các chức năng được mô tả ngay bên dưới.

***

## Mời người dùng mới vào vCloudStack (Invite User)

Thực hiện các bước như sau:

Bước 1: Người quản trị truy cập vào Admin Site trong vCloudStack;

Bước 2: Chọn đến màn hình Quản trị người dùng;

Bước 3: Chọn vào nút "Mời" (Invite User);

Bước 4: Điền email của người dùng muốn mời vào sử dụng vCloudStack;

Bước 5: Chọn Roles vai trò của người dùng được mời vào;

Bước 6: Click nút invite để xác nhận mời người dùng mới.

{% hint style="info" %}
**Lưu ý:**&#x20;

* Tài khoản (Email) của người dùng được mời vào vCloudStack, phải là tài khoản đã đăng ký vào VNG Cloud trước đó.
* Mặc định vai trò mời sử dụng vCloudStack là "User". Với vai trò này thì người dùng có thể vào vCloudStack User Site để tạo và vận hành. Nếu muốn truy cập vào vCloudstack Admin Site thì người quản trị phải chọn role là Admin trở lên.
{% endhint %}

***

## Thiết lập giới hạn sử dụng tài nguyên (Limit quota)

Thực hiện các bước như sau:

Bước 1: Người quản trị truy cập vào Admin Site trong vCloudStack;

Bước 2: Chọn đến màn hình Quản trị người dùng;

Bước 3: Tìm đến tài khoản người dùng muốn thiết lập giới hạn sử dụng, tại cột Hành động (Action), bạn chọn "Chỉnh sửa quota" (Edit quota)

Bước 4: Người quản trị thay đổi giá trị giới hạn ở cột "Current limit" để thay đổi giới hạn sử dụng cho tùy vào tiêu chí giới hạn.

Bước 5: Nhấn Save để lưu giới hạn sử dụng đã thiết lập.

{% hint style="info" %}
**Lưu ý:**

* Chỉ người dùng đã truy cập vào vCloudStack User site để hệ thống kích hoạt tài khoản vCloudStack thì người quản trị mới thiết lập được giới hạn sử dụng tài nguyên.
* Chỉ áp dụng cho các người dùng có trạng thái là có trạng thái Đang hoạt động (Active)
{% endhint %}

***

## Tạm ngừng tài khoản người dùng (Deactive)

Thực hiện các bước như sau:

Bước 1: Người quản trị truy cập vào Admin Site trong vCloudStack;

Bước 2: Chọn đến màn hình Quản trị người dùng;

Bước 3: Tìm đến tài khoản người dùng muốncho tạm ngừng sử dụng vCloudStack, tại cột Hành động (Action), bạn chọn "Deactive".

Bước 4: Màn hình pop-up yêu cầu xác nhận tạm ngừng hoạt động, chọn nút Deactive để xác nhận.

{% hint style="info" %}
**Lưu ý:**&#x20;

* Sau khi tài khoản người dùng bị deactive thì trạng thái sẽ là Inactive;
* Tài khoản người dùng Inactive thì sẽ không được phép truy cập vào vCloudStack User Site và Admin Site.&#x20;
{% endhint %}

