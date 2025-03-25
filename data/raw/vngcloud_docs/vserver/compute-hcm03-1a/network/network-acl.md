# Network ACL

### **Tổng quan** <a href="#networkacl-tongquan" id="networkacl-tongquan"></a>

Network ACL là tính năng giúp bạn kiểm soát lưu lượng truy cập mạng đến và đi (lưu lượng truy cập (traffic) in/ out) từ các subnet trong VPC của bạn. Đơn giản hơn, Network ACL chính là tầng security của subnet, nó sẽ được gắn vào subnet, mọi lưu lượng truy cập (traffic) đi vào hay ra subnet đều phải qua sự kiểm duyệt của **Network ACL**. Cụ thể:&#x20;

* Khi lưu lượng truy cập (traffic) đi từ internet vào **vServer instance**, nó phải đi qua **Network ACL** trước rồi mới đến **Security Group**.
* Khi lưu lượng truy cập (traffic) đi từ **vServer instance**, nó phải đi qua **Security Group** trước rồi mới đến **Network ACL**.

***

### **Kiến thức cơ bản về Network ACL:** <a href="#networkacl-kienthuccobanvenetworkacl" id="networkacl-kienthuccobanvenetworkacl"></a>

* Mỗi VPC sau khi tạo mới sẽ không có sẵn Network ACL nào.
* Bạn có thể tạo một Network ACL mới và gắn nó với một hoặc nhiều subnet trong VPC của bạn. Chúng tôi cung cấp cho bạn các inbound rule có sẵn, bạn có thể thêm các rule mong muốn theo hướng dẫn bên dưới.
* Một Network ACL có thể được gắn với nhiều subnet, nhưng một subnet chỉ có thể gắn với một Network ACL tại một thời điểm.
* Một Network ACL có các rule cho phép (Allow) và từ chối (Deny) lưu lượng. Mỗi rule này được đánh dấu bởi một priority duy nhất.
* Khi quyết định cho phép hoặc từ chối lưu lượng, chúng tôi sẽ đánh giá các rule theo thứ tự, bắt đầu từ rule có số thấp nhất.
* rule Network ACL chỉ được áp dụng khi lưu lượng đi vào hoặc rời khỏi subnet, không áp dụng cho lưu lượng trong subnet hoặc lưu lượng NAT từ Floating IP.
* Có giới hạn về số lượng Network ACL trên mỗi VPC và số lượng rule trên mỗi Network ACL.

***

### **Phân biệt giữa Security Group và Network ACL** <a href="#networkacl-phanbietgiuasecuritygroupvanetworkacl" id="networkacl-phanbietgiuasecuritygroupvanetworkacl"></a>

Tham khảo bảng bên dưới để phân biệt giữa Security Group và Network ACL.

<table data-header-hidden><thead><tr><th width="174"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Tính năng</strong></td><td><strong>Security Group</strong></td><td><strong>Network ACL</strong></td></tr><tr><td>Mức hoạt động</td><td>Mức instance</td><td>Mức subnet</td></tr><tr><td>Áp dụng cho</td><td>Chỉ áp dụng cho instance được gắn với security group đó.</td><td>Áp dụng cho tất cả các instance được triển khai trong subnet được gắn với Network ACL đó.</td></tr><tr><td>Rule</td><td>Chỉ hỗ trợ rule cho phép (Allow) lưu lượng truy cập (traffic) từ <strong>public</strong>.</td><td>Hỗ trợ cả rule cho phép và từ chối (Allow and Deny) lưu lượng truy cập (traffic) trong <strong>internal</strong>.</td></tr><tr><td>Đánh giá rule</td><td>Đánh giá tất cả rule trước khi quyết định cho phép lưu lượng</td><td>Đánh giá theo thứ tự, bắt đầu từ rule có số thấp nhất</td></tr><tr><td>Trạng thái</td><td><p><strong>Stateful:</strong> </p><ul><li>Cho phép <strong>traffic</strong> cụ thể đến instance ở <strong>inbound rule</strong> thì ở <strong>outbound rule</strong> cũng được tự động cho phép traffic đi ra khỏi instance, và ngược lại.</li></ul></td><td><p><strong>Stateless</strong>: </p><ul><li>Cho phép <strong>traffic</strong> cụ thể đến subnet ở <strong>inbound rule</strong> thì ở <strong>outbound rule</strong> sẽ không được tự động cho phép traffic đi ra khỏi subnet, và ngược lại.</li></ul></td></tr></tbody></table>

***

### **Các phần của một rule Network ACL:** <a href="#networkacl-cacphancuamotrulenetworkacl" id="networkacl-cacphancuamotrulenetworkacl"></a>

Một Network ACL bao gồm các thành phần cơ bản sau:&#x20;

* Tên Network ACL.
* VPC
* Inbound rules/ Outbound rules:
  * Priority: trọng số của rule. Rule được đánh giá theo trọng số này, bắt đầu từ rule có số thấp nhất.
  * Protocol: giao thức truy cập. ví dụ: TCP, UDP, ICMP,...
  * Port range: số port hoặc phạm vi port bắt đầu và kết thúc.
  * Source: IP hoặc dải IP/ CIDR mong muốn cho phép/ từ chối truy cập theo Inbound rules.
  * Destination: IP hoặc dải IP/ CIDR mong muốn cho phép/ từ chối truy cập theo Outbound rules.
  * Allow/ Deny: cho phép hoặc từ chối lưu lượng được chỉ định.
* Subnet

Mỗi Network ACL đều có một 2 inbound rules (1 rule allow và 1 rule deny) và 2 outbound rules (1 rule allow và 1 rule deny) mặc định. <mark style="color:red;">**Bạn không thể sửa đổi hoặc xóa rule deny mặc định này.**</mark>

* **Inbound rules:**

| Priority  |         | Protocol | Port range | Source    | Allow/Deny | Ghi chú                             |
| --------- | ------- | -------- | ---------- | --------- | ---------- | ----------------------------------- |
| 0         | Inbound | ANY      | 0-65535    | 0.0.0.0/0 | Allow      | Có thể Xóa/ Chỉnh sửa rule.         |
| 2000      | Inbound | ANY      | 0-65535    | 0.0.0.0/0 | Deny       | Không cho phép Xóa/ Chỉnh sửa rule. |

* **Outbound rules:**

| Priority | Type     | Protocol | Port range | Destination | Allow/Deny | Ghi chú                             |
| -------- | -------- | -------- | ---------- | ----------- | ---------- | ----------------------------------- |
| 0        | Outbound | ANY      | 0-65535    | 0.0.0.0/0   | Allow      | Có thể Xóa/ Chỉnh sửa rule.         |
| 2000     | Outbound | ANY      | 0-65535    | 0.0.0.0/0   | Deny       | Không cho phép Xóa/ Chỉnh sửa rule. |

***

### **Làm việc với Network ACLs** <a href="#networkacl-lamviecvoinetworkacls" id="networkacl-lamviecvoinetworkacls"></a>

#### **Khởi tạo một Network ACL** <a href="#networkacl-khoitaomotnetworkacl" id="networkacl-khoitaomotnetworkacl"></a>

Bạn có thể tạo một Network ACL tùy chỉnh cho VPC của mình. Mặc định, Network ACL bạn tạo sẽ chặn (Deny) tất cả lưu lượng đến và đi cho đến khi bạn thêm các rule, và nó không được liên kết với subnet nào cho đến khi bạn liên kết nó rõ ràng với một subnet.

Để tạo một Network ACL, hãy làm theo các bước bên dưới:&#x20;

1. Truy cập vào trang chủ của dịch vụ vServer tại đường dẫn: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
2. Trong menu bên trái, chọn **Network**, sau đó chọn **Network ACLs**.
3. Chọn **Create Network ACL**.
4. Nhập **Tên** gợi nhớ và chọn **1 VPC đang hoạt động** mà bạn mong muốn tạo Network ACL. Lưu ý: Tên Network ACL chỉ cho phép các chữ cái (a-z, A-Z, 0-9, '\_', '-') và độ dài dữ liệu đầu vào của bạn phải từ 5 đến 50.
5. Chọn **Create**.

Lúc này, Network ACL của bạn được tạo với thông tin Inbound rule, Outbound rule mặc định được mô tả ở bảng bên trên. Tiếp tục sử dụng hướng dẫn bên dưới để chỉnh sửa Inbound rule, Outbound rule cũng như liên kết Subnet với Network ACL vừa tạo.

***

#### Chỉnh sửa danh sách Inbound rules <a href="#networkacl-chinhsuadanhsachinboundrules" id="networkacl-chinhsuadanhsachinboundrules"></a>

Để chỉnh sửa danh sách Inbound rule (các rule cho phép đi vào), hãy làm theo các bước bên dưới:&#x20;

1. Truy cập vào trang chủ của dịch vụ vServer tại đường dẫn: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
2. Trong menu bên trái, chọn **Network**, sau đó chọn **Network ACLs**.
3. Tại danh sách các Network ACL đã tạo, chọn vào một **Network ACL**.
4. Tại mục Inbound rules, chọn **Chỉnh sửa Inbound rules.**
5. Chọn **Thêm rule** nếu bạn muốn tạo một rule mới, hoặc chọn biểu tượng <img src="https://docs.vngcloud.vn/download/thumbnails/71729277/image2024-2-24_17-45-8.png?version=1&#x26;modificationDate=1708921940000&#x26;api=v2" alt="" data-size="line">nếu bạn muốn **xóa rule** vừa tạo.
6. Chỉnh sửa **Priority**: nhập trọng số (độ ưu tiên) cho rule. Trọng số của rule không được trùng với số đã có trong Network ACL. Chúng tôi xử lý các rule theo trọng số, bắt đầu từ số thấp nhất tới số cao nhất mà không phân biệt Allow hay Deny. Trọng số tối đa bạn có thể thiết lập là **32766**.
7. Chỉnh sửa **Protocol**: thêm giao thức truy cập mà bạn mong muốn cho phép/ từ chối đi vào Subnet. Chúng tôi đang cung cấp cho bạn lựa chọn 1 trong 4 phương án: ANY, TCP, UDP, ICMP.
8. Chỉnh sửa **Port range**: số port hoặc phạm vi port bắt đầu và kết thúc.
9. Chỉnh sửa **Source**: IP hoặc dải IP/ CIDR mong muốn cho phép/ từ chối truy cập theo Inbound rules.
10. Chỉnh sửa **Allow**/ **Deny**: cho phép hoặc từ chối lưu lượng được chỉ định.
11. Nếu bạn muốn thêm nhiều **Inbound rules** khác, tiếp tục chọn **Thêm rule** và thực hiện lặp lại các bước từ số 6, 7, 8, 9,10.&#x20;
12. Nếu bạn muốn xóa nhiều Inbound rules khác, tiếp tục chọn biểu tượng <img src="https://docs.vngcloud.vn/download/thumbnails/71729277/image2024-2-24_17-45-8.png?version=1&#x26;modificationDate=1708921940000&#x26;api=v2" alt="" data-size="line">tại các rule cần xóa. <mark style="color:red;">**Lưu ý: Bạn không thể sửa đổi hoặc xóa Inbound rule deny mặc định được tạo bởi chúng tôi.**</mark>
13. Chọn **Lưu** để lưu lại các chỉnh sửa đã nhập/ chọn hoặc chọn **Hủy bỏ** để hủy bỏ thay đổi việc chỉnh sửa.

***

#### Chỉnh sửa danh sách Outbound rules <a href="#networkacl-chinhsuadanhsachoutboundrules" id="networkacl-chinhsuadanhsachoutboundrules"></a>

Để chỉnh sửa danh sách Outbound rule (các rule cho phép đi ra), hãy làm theo các bước bên dưới:&#x20;

1. Truy cập vào trang chủ của dịch vụ vServer tại đường dẫn: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
2. Trong menu bên trái, chọn **Network**, sau đó chọn **Network ACLs**.
3. Tại danh sách các Network ACL đã tạo, chọn vào một **Network ACL**.
4. Tại mục Inbound rules, chọn **Chỉnh sửa Outbound rules.**
5. Chọn **Thêm rule** nếu bạn muốn tạo một rule mới, hoặc chọn biểu tượng <img src="https://docs.vngcloud.vn/download/thumbnails/71729277/image2024-2-24_17-45-8.png?version=1&#x26;modificationDate=1708921940000&#x26;api=v2" alt="" data-size="line">nếu bạn muốn **xóa rule** vừa tạo.
6. Chỉnh sửa **Priority**: nhập trọng số (độ ưu tiên) cho rule. Trọng số của rule không được trùng với số đã có trong Network ACL. Chúng tôi xử lý các rule theo trọng số, bắt đầu từ số thấp nhất tới số cao nhất mà không phân biệt Allow hay Deny. Trọng số tối đa bạn có thể thiết lập là **32766**.
7. Chỉnh sửa **Protocol**: thêm giao thức truy cập mà bạn mong muốn cho phép/ từ chối đi ra khỏi Subnet. Chúng tôi đang cung cấp cho bạn lựa chọn 1 trong 4 phương án: ANY, TCP, UDP, ICMP.
8. Chỉnh sửa **Port range**: số port hoặc phạm vi port bắt đầu và kết thúc.
9. Chỉnh sửa **Destination**: IP hoặc dải IP/ CIDR mong muốn cho phép/ từ chối truy cập theo Outbound rules.
10. Chỉnh sửa **Allow**/ **Deny**: cho phép hoặc từ chối lưu lượng được chỉ định.
11. Nếu bạn muốn thêm nhiều **Outbound rules** khác, tiếp tục chọn **Thêm rule** và thực hiện lặp lại các bước từ số 6, 7, 8, 9,10.&#x20;
12. Nếu bạn muốn xóa nhiều Outbound rules khác, tiếp tục chọn biểu tượng  <img src="https://docs.vngcloud.vn/download/thumbnails/71729277/image2024-2-24_17-45-8.png?version=1&#x26;modificationDate=1708921940000&#x26;api=v2" alt="" data-size="line">tại các rule cần xóa. <mark style="color:red;">**Lưu ý: Bạn không thể sửa đổi hoặc xóa Outbound rule deny mặc định được tạo bởi chúng tôi.**</mark>
13. Chọn **Lưu** để lưu lại các chỉnh sửa đã nhập/ chọn hoặc chọn **Hủy bỏ** để hủy bỏ thay đổi việc chỉnh sửa.

***

#### Liên kết/ Bỏ liên kết Subnet vào Network ACL <a href="#networkacl-lienket-bolienketsubnetvaonetworkacl" id="networkacl-lienket-bolienketsubnetvaonetworkacl"></a>

Để áp dụng các rule của Network ACL cho một subnet cụ thể, bạn cần liên kết subnet đó với Network ACL. Bạn có thể liên kết một Network ACL với nhiều subnet, nhưng một subnet chỉ có thể liên kết với một Network ACL tại một thời điểm.&#x20;

Để liên kết một subnet với một Network ACL, hãy làm theo các bước bên dưới:

1. Truy cập vào trang chủ của dịch vụ vServer tại đường dẫn: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
2. Trong menu bên trái, chọn **Network**, sau đó chọn **Network ACLs**.
3. Tại danh sách các Network ACL đã tạo, chọn vào một **Network ACL**.
4. Tại mục Subnet association, chọn **Chỉnh sửa Subnet Association.**
5. Tại màn hình **Chỉnh sửa Subnet Association, bạn có thể liên kết/ bỏ liên kết Subnet vào Network ACL bằng cách:**&#x20;
   1. Tại mục **Các Subnet** có sẵn, bạn có thể chọn một hoặc nhiều **Subnet** mong muốn liên kết thông qua biểu tượng  ![](https://docs.vngcloud.vn/download/thumbnails/71729277/image2024-2-24\_18-9-10.png?version=1\&modificationDate=1708921940000\&api=v2).
   2. Tại mục **Subnet liên kết**, bạn có thể bỏ liên kết một **Subnet** với **Network ACL** bằng cách chọn vào Subnet muốn bỏ.&#x20;
6. Chọn **Lưu** để lưu lại các chỉnh sửa đã nhập/ chọn hoặc chọn **Hủy bỏ** để hủy bỏ thay đổi việc chỉnh sửa.

{% hint style="info" %}
**Chú ý:**

* Khi bạn liên kết một subnet với một Network ACL mới, các Inbound rules và Outbound rules của Network ACL mới sẽ bắt đầu áp dụng cho lưu lượng đến và đi từ subnet đó.
* Bạn có thể liên kết một subnet với một Network ACL khác bất cứ lúc nào. Lúc này, chúng tôi sẽ ngắt liên kết cũ và thực hiện liên kết mới theo chỉnh sửa của bạn đảm bảo tại 1 thời điểm một subnet chỉ có thể gắn với một Network ACL. Việc thay đổi liên kết subnet có thể ảnh hưởng đến lưu lượng đến và đi từ subnet đó.
{% endhint %}

***

#### **Xóa một Network ACL** <a href="#networkacl-xoamotnetworkacl" id="networkacl-xoamotnetworkacl"></a>

Bạn chỉ có thể xóa Network ACL nếu không có subnet nào được liên kết với nó. Nếu Network ACL bạn muốn xóa vẫn còn Subnet được liên kết, hãy thực hiện theo hướng dẫn bên trên để **Bỏ liên kết Subnet vào Network ACL** trước khi thực hiện xóa Network ACL đó.

Để xóa một Network ACL, hãy làm theo các bước bên dưới:&#x20;

1. Truy cập vào trang chủ của dịch vụ vServer tại đường dẫn: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
2. Trong menu bên trái, chọn **Network**, sau đó chọn **Network ACLs**.
3. Tại Network ACL muốn xóa, chọn biểu tượng  <img src="https://docs.vngcloud.vn/download/thumbnails/71729277/image2024-2-24_18-17-12.png?version=1&#x26;modificationDate=1708921940000&#x26;api=v2" alt="" data-size="line">.
4. Tại màn hình xác nhận xóa, chọn **Xóa** nếu bạn chắc chắn muốn xóa Network ACLs này hoặc **Hủy bỏ** nếu muốn hủy bỏ việc xóa.
