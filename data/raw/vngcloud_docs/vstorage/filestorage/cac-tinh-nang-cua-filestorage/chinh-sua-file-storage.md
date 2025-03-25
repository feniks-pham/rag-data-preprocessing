# Chỉnh sửa File Storage

Trên mỗi file storage, bạn có thể thực hiện chỉnh sửa một số thông số, cụ thể:

* **Đối với file storage NFS**: Cho phép chỉnh sửa quyền truy cập (ACL) trực tiếp trên file bằng cách chọn **Edit** trên file storage bạn muốn chỉnh sửa. Tuy nhiên, việc chỉnh sửa ACL có thể gây gián đoạn cho File storage này lên đến **10 giây**. <mark style="color:red;">**Thực hiện hành động này thường xuyên sẽ gây gián đoạn cho File storage của bạn.**</mark>

<figure><img src="../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Đối với file storage SMB sử dụng Basic Authentication**: Cho phép thực hiện các thao tác như thêm mới tài khoản, vô hiệu hóa, thay đổi mật khẩu, hoặc xóa các tài khoản authentication đã tạo.

<figure><img src="../../../.gitbook/assets/image (911).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (912).png" alt=""><figcaption></figcaption></figure>

* **Đối với file storage SMB sử dụng AD Authentication**: Không cho phép thay đổi thông tin của Active Directory; nếu cần thay đổi, <mark style="color:red;">**nên tạo một file storage mới để đảm bảo tính ổn định của hệ thống.**</mark>
