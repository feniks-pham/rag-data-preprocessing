# Attach pool members

Sử dụng tài liệu này như là một hướng dẫn về cách thêm Member vào một Pool trên Load Balancer. Về cơ bản, giao diện quản trị hỗ trợ việc thêm Member vào Pool theo hai cách:

* **Qua Instance** (Member là các máy ảo hoặc máy chủ cụ thể)
* **Qua địa chỉ IP** (Member là các địa chỉ IP Public hoặc IP thuộc subnet của Load Balancer)

#### 1. Đính kèm/Cập nhật Member là các máy chủ khả dụng <a href="#attachpoolmembers-1.dinhkem-capnhatmemberlacacmaychukhadung" id="attachpoolmembers-1.dinhkem-capnhatmemberlacacmaychukhadung"></a>

* Truy cập vào trang chủ Load Balancer tại đây: [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
* Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình. Tại phần thông tin chi tiết Load Balancer, chọn tab Pool. Tại phần danh sách Pool, nhấn chọn Pool cần đính kèm/chỉnh sửa Member.
* Tại phần thông tin chi tiết Pool bên trái, kéo xuống mục Thông tin Member, nhấn nút "Chỉnh sửa Pool members / Edit Pool member".
* Tại cửa sổ giao diện "Chỉnh sửa Pool Member", phần "Máy chủ khả dụng / Available instances" sẽ hiện lên danh sách máy chủ backend khả dụng thuộc subnet Load Balancer.
* Chọn máy chủ khả dụng từ danh sách.
* Điền các thông tin về thông số Weight, Port, Monitor Port và Backup role.
* Nhấn chọn nút "Attach / Gắn" để thêm máy chủ backend làm Pool Member.
* Xem lại danh sách Pool Member tại mục "Máy chủ & Instance đính kèm / Attach server & instances".
* Nhấn nút "Save / Lưu" để hoàn tất chỉnh sửa Pool Member.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553412/image2023-9-6_17-28-22.png?version=1&#x26;modificationDate=1693996103000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

#### 2. Đính kèm/Cập nhật Member là các địa chỉ IP <a href="#attachpoolmembers-2.dinhkem-capnhatmemberlacacdiachiip" id="attachpoolmembers-2.dinhkem-capnhatmemberlacacdiachiip"></a>

Ngoài việc đính kèm các Pool member thông qua các máy chủ backend, người dùng còn có thể đính kèm các địa chỉ IP như là các Pool Member, tham khảo hướng dẫn dưới đây để thực hiện việc đính kèm.

* Truy cập vào trang chủ Load Balancer tại đây: [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
* Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình. Tại phần thông tin chi tiết Load Balancer, chọn tab Pool. Tại phần danh sách Pool, nhấn chọn Pool cần đính kèm/chỉnh sửa Member.
* Tại phần thông tin chi tiết Pool bên trái, kéo xuống mục Thông tin Member, nhấn nút "Chỉnh sửa Pool members / Edit Pool member".
* Tại cửa sổ giao diện "Chỉnh sửa Pool Member", tại phần "Custom Instances / Instances tùy chỉnh" thực hiện đính kèm địa chỉ IP vào Pool theo hướng dẫn sau:
  1. **Nhập địa chỉ IP:** Các địa chỉ IP phải là IP Public hoặc thuộc Load Balancer subnet
  2. Nhấn nút Add để thêm các địa chỉ IP vào danh sách Custom Instance
  3. Chọn IP Address cần đính kèm từ danh sách Custom Instance
  4. Điền các thông tin về thông số Weight, Port, Monitor Port và Backup role.
  5. Nhấn nút "Attach / Gắn"
  6. **Xem lại danh sách Pool Member tại mục "Máy chủ & Instance đính kèm / Attach server & instances".**
  7. **Nhấn nút "Save / Lưu" để hoàn tất chỉnh sửa Pool Member.**

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553412/image2023-9-6_17-44-54.png?version=1&#x26;modificationDate=1693997095000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
