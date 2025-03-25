# Tạo Repository User

Tham khảo hướng dẫn sau để tiến hành khởi tạo Repository User của bạn.

**Cách khởi tạo Repository User**

1. Tại trang chủ Container Registry, nhấn vào **menu "Repository User"** phía bên tay phải để truy cập đến danh sách Repository User, nhấn nút **"CreateRepository User"** để bắt đầu tạo mới một Repository User.
2. Một popup **"Create Repository"** hiển thị cho phép bạn điền các thông tin như:
   * **User Name (optional)**: Tên của Repository User, trường hợp không điền tên, hệ thống sẽ tự động sinh ra tên tương ứng. Lưu ý tên sau khi điền/sinh tự động sẽ được add thêm prefix {AccountID} tương ứng với tài khoản VNG Cloud đang đăng nhập.
   * **Expiration Date:** Ngày hết hạn của User. Có 3 chế độ như sau:
     * Để trống: Đồng nghĩa với việc user này không có thời gian expired
     * Điền ngày cụ thể: User này sẽ expired tại thời điểm được chọn. Đối với user bị expired, hệ thống sẽ tạm khóa toàn bộ các tính năng có liên quan đối với Repository User này cho đến khi user được gia hạn thêm thời gian
   * **Description (optional):** Thông tin thêm về Repository User
   * **Repositories (required):** Đính kèm các Repository và cài đặt Permission tương ứng
     * Tìm Repository cần attach theo repository name
     * Nhấn nút "Add"
     * Tại danh sách Repository được thêm vào bên dưới, cài đặt permission tương ứng Push\&Pull/Pull Only
3. Nhấn nút **"Create"** để hoàn tất việc khởi tạo
4. Kiểm tra thông tin Repository vừa khởi tạo tại danh sách

\
