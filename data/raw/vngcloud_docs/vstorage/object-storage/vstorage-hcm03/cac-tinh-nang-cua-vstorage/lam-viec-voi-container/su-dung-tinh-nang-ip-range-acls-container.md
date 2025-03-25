# Sử dụng tính năng IP range ACLs container

IP Range ACLs là tính năng cho phép người dùng có thể chủ động kích hoạt chế độ an toàn ở mức network internet - giới hạn khả năng truy cập vào project hoặc container của vStorage từ một số nguồn địa chỉ IP được xác định thông qua danh sách IP/ Subnet thiết lập trên metadata ở cấp project hoặc container hoặc cả hai cấp.

Hiện tại, vStorage chỉ hỗ trợ tính năng IP range ACLs cho IPv4, chưa hỗ trợ cho IPv6. Tất cả các đề cập liên quan đến IP bên dưới sẽ được hiểu là IPv4.

Tính năng IP range ACLs hỗ trợ cho cả giao thức S3 và HTTP.



{% tabs %}
{% tab title=" Sử dụng vStorage Portal" %}
Để thiết lập IP range ACLs cho một container, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **project** sau đó chọn![](https://docs.vngcloud.vn/download/thumbnails/59802032/image2023-5-24\_9-5-19.png?version=1\&modificationDate=1684893919000\&api=v2)tại **container** bạn muốn thiết lập IP range ACLs.
3. Tại mục IP range ACLS, chọn **Thiết lập IP range ACLs**. Để biết số lượng IP/ Subnet bạn có thể thiết lập trên một container, vui lòng xem [Hạn mức tài nguyên](../../han-muc-tai-nguyen.md).
4. Mặc định container mà bạn chọn sẽ được thiết lập trạng thái truy cập là **Tất cả IP/Subnet**. Nếu bạn muốn giới hạn số lượng địa chỉ IP có thể truy cập vào tài nguyên của bạn, hãy chọn **IP/Subnet cụ thể.**
5. Nếu bạn chọn **IP/Subnet cụ thể**, hãy nhập địa chỉ **IP** hoặc **Subnet** (CIDR) (ví dụ: 125.212.100.101 hoặc 125.212.100.0/24) sau đó chọn **Thêm**. Chi tiết tham khảo tại IP address và CIDR ([https://en.wikipedia.org/wiki/Classless\_Inter-Domain\_Routing](https://en.wikipedia.org/wiki/Classless\_Inter-Domain\_Routing)).
6. **IP/ Subnet** bạn vừa thêm được hiển thị ở danh sách, nếu bạn muốn bỏ **IP/ Subnet** này khỏi danh sách, hãy chọn ![](https://docs.vngcloud.vn/download/thumbnails/59802032/image2023-5-9\_13-17-46.png?version=1\&modificationDate=1683613236000\&api=v2).
7. Chọn **Cập nhật**.

Sau khi thực hiện 7 bước bên trên, bạn đã thiết lập thành công IP range ACLs cho một container. Lúc này nếu bạn sử dụng địa chỉ IP Portal hoặc IP thuộc danh sách IP/ Subnet đã được thêm vào container thì bạn sẽ có quyền truy cập vào tất cả tài nguyên của container (bao gồm container và các directory và object thuộc container đó). **Container sẽ được thừa hưởng những IP range ACLs của project mà container đó thuộc về.**&#x20;

Nếu bạn muốn tắt thiết lập IP range ACLs cho container của bạn, tức là mọi người dùng có quyền đều có thể truy cập vào tài nguyên mà không cần quan tâm tới địa chỉ IP, hãy lựa chọn **Tất cả IP/Subnet** khi thiết lập IP range ACLs.

Sau khi thiết lập IP range ACLs, các yêu cầu S3/ HTTP (bao gồm các yêu cầu TempURL) đến container từ các IP/ Subnet không hợp lệ sẽ bị từ chối với mã lỗi trả về 403.

<figure><img src="../../../../../.gitbook/assets/Su_dung_tinh_nang_IP_range_ACLs_Container.gif" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}
