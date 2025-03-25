# Cách tạo Repository

Tham khảo hướng dẫn sau để tiến hành khởi tạo Repository của bạn.

**Cách khởi tạo Repository**

1. Tại trang chủ Container Registry, nhấn vào **menu "Repository"** phía bên tay phải để truy cập đến danh sách Repository, nhấn nút **"Create a repository"** để bắt đầu tạo mới một Repository.
2. Một popup **"Create Repository"** hiển thị cho phép bạn điền các thông tin như:
   * **Repository name (optional)**: Tên của Repository, trường hợp không điền tên, hệ thống sẽ tự động sinh ra tên tương ứng. Lưu ý tên sau khi điền/sinh tự động sẽ được add thêm prefix {AccountID} tương ứng với tài khoản VNG Cloud đang đăng nhập.
   * **Access level:** Khả năng truy cập đến Repository (Public / Private).&#x20;
     * Public: Là các Repository mà tại đó, người dùng có thể Pull/Push thoải mái mà không thông qua Repository User
     * Private: Là các Repository mà tại đó, người dùng phải cung cấp đinh danh (username/password) để có thể truy cập đến các Images được quản lý tại Repository này.
   * **Quota Limit:** Dung lượng lưu trữ tối đa mà Repository có thể lưu trữ. Ví dụ bạn điền 20GB, thì Repository của bạn chỉ có thể lưu trữ tối đa 20GB dung lượng. Tuy nhiên, bạn hoàn toàn có thể thay đổi con số này tùy thuộc với nhu cầu tế sau khi khởi tạo.
3. Nhấn **"Create"** để hoàn tất quá trình khởi tạo.
4. Kiểm tra thông tin Repository vừa khởi tạo tại danh sách.

\
