# Sử dụng tính năng IP range ACLs project

IP Range ACLs là tính năng cho phép người dùng có thể chủ động kích hoạt chế độ an toàn ở mức network internet - giới hạn khả năng truy cập vào project hoặc container của vStorage từ một số nguồn địa chỉ IP được xác định thông qua danh sách IP/ Subnet thiết lập trên metadata ở cấp project hoặc container hoặc cả hai cấp.

Hiện tại, vStorage chỉ hỗ trợ tính năng IP range ACLs cho IPv4, chưa hỗ trợ cho IPv6. Tất cả các đề cập liên quan đến IP bên dưới sẽ được hiểu là IPv4.

Tính năng IP range ACLs hỗ trợ cho cả giao thức S3 và HTTP.

Để thiết lập IP range ACLs cho một project, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

&#x20;Sử dụng vStorage Portal

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/59802027/image2023-5-9\_13-12-33.png?version=1\&modificationDate=1683612754000\&api=v2) tại **project** bạn muốn thiết lập IP range ACLs.
3. Chọn mục **IP range ACLs**.
4. Chọn **Thiết lập IP range ACLs**.
5. Mặc định project mà bạn chọn sẽ được thiết lập trạng thái truy cập là **Tất cả IP/Subnet**. Nếu bạn muốn giới hạn số lượng địa chỉ IP/ Subnet có thể truy cập vào tài nguyên của bạn, hãy chọn **IP/Subnet cụ thể.** Để biết số lượng IP/ Subnet bạn có thể thiết lập trên một project, vui lòng xem [Hạn mức tài nguyên](../../han-muc-tai-nguyen.md).
6. Nếu bạn chọn **IP/Subnet cụ thể**, hãy nhập địa chỉ **IP** hoặc **Subnet** (CIDR) (ví dụ: 125.212.100.101 hoặc 125.212.100.0/24) sau đó chọn **Thêm**. Chi tiết tham khảo tại IP address và CIDR ([https://en.wikipedia.org/wiki/Classless\_Inter-Domain\_Routing](https://en.wikipedia.org/wiki/Classless\_Inter-Domain\_Routing)).
7. **IP/ Subnet** bạn vừa thêm được hiển thị ở danh sách, nếu bạn muốn bỏ **IP/ Subnet** này khỏi danh sách, hãy chọn ![](https://docs.vngcloud.vn/download/thumbnails/59802027/image2023-5-9\_13-17-46.png?version=1\&modificationDate=1683613066000\&api=v2).
8. Chọn **Cập nhật**.

Sau khi thực hiện 8 bước bên trên, bạn đã thiết lập thành công IP range ACLs cho một project. Lúc này nếu bạn sử dụng địa chỉ **IP Portal** hoặc IP thuộc danh sách IP/ Subnet đã được thêm vào project thì bạn sẽ có quyền truy cập vào tất cả tài nguyên của project (bao gồm project và các container thuộc project đó).

Nếu bạn muốn tắt thiết lập IP range ACLs cho project của bạn, tức là mọi người dùng có quyền đều có thể truy cập vào tài nguyên mà không cần quan tâm tới địa chỉ IP, hãy lựa chọn **Tất cả IP/Subnet** khi thiết lập IP range ACLs.

Sau khi thiết lập IP range ACLs, các yêu cầu S3/ HTTP (bao gồm các yêu cầu TempURL) đến project từ các IP/ Subnet không hợp lệ sẽ bị từ chối với mã lỗi trả về 403.&#x20;

<figure><img src="../../../../../.gitbook/assets/Su_dung_IPRange_ACLs.gif" alt=""><figcaption></figcaption></figure>
