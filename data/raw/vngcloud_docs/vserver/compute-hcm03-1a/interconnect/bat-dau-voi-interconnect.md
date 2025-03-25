# Bắt đầu với Interconnect

VNG Cloud Interconnect cung cấp kết nối mạng Layer 3 trực tiếp. Kết nối Interconnect không sử dụng internet công cộng. Thay vào đó, chúng tôi cung cấp các kết nối trực tiếp có thể mang lại độ tin cậy cao hơn, tốc độ nhanh hơn và ổn định hơn cũng như mức độ bảo mật cao hơn.

***

### **Ý chính** <a href="#batdauvoiinterconnect-ychinh" id="batdauvoiinterconnect-ychinh"></a>

Interconnect tạo kết nối mạng Lớp 3 (Layer 3) giữa mạng tại chỗ của bạn và mạng VNG Cloud thông qua đối tác nhà cung cấp kết nối.\
Định tuyến động được thực hiện bằng Giao thức cổng biên (BGP) tiêu chuẩn ngành.\
Bạn phải xem xét và chọn một phương án về khả năng phục hồi để đảm bảo bạn sử dụng phương pháp tiếp cận phù hợp với nhu cầu về khả năng phục hồi của mình. Tùy chọn bạn chọn sẽ ảnh hưởng đến Thỏa thuận cấp độ dịch vụ (SLA) về thời gian hoạt động kết nối của bạn.\
Khả năng kết nối được cung cấp bằng cách sử dụng kết nối chéo giữa thiết bị do VNG Cloud sở hữu và thiết bị do khách hàng sở hữu.

<figure><img src="https://docs.vngcloud.vn/download/attachments/64553619/image2023-9-8_14-30-47.png?version=1&#x26;modificationDate=1694158248000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Nếu bạn muốn kết nối từ cơ sở của mình, bạn cần làm việc với chúng tôi để lựa chọn cấu hình kết nối hợp lý và sau đó bạn sẽ cần phải ký hợp đồng trực tiếp để yêu cầu kết nối Interconnect.&#x20;

Khi thực hiện triển khai, chúng tôi sẽ thực hiện dựa trên:

**Kết nối chuyên dụng (Dedicated)**: Quyền truy cập độc quyền vào kết nối chéo, cung cấp các tùy chọn băng thông 1 Gbps, 10 Gbps (tùy thuộc vào băng thông sẵn có tại vị trí Direct Connect của bạn). Có thể tạo nhiều giao diện ảo logic cho mỗi kết nối vật lý tại các vị trí Interconnect được chọn.

Tiếp theo, thiết lập loại kết nối ảo theo một trong những cách bên dưới:

**Giao diện ảo chuyển tuyến:** Nên sử dụng giao diện ảo chuyển tuyến để truy cập một hoặc nhiều Cổng chuyển tuyến VNG Cloud được liên kết với cổng Direct Connect. Bạn có thể sử dụng giao diện ảo chuyển tuyến với bất kỳ kết nối của VNG Cloud Interconnect ở bất kỳ tốc độ nào.\
**Giao diện ảo công cộng:** Giao diện ảo công cộng có thể truy cập các dịch vụ công cộng VNG Cloud bằng địa chỉ IP công cộng.\
**Giao diện ảo riêng tư:** Nên sử dụng giao diện ảo riêng tư để truy cập VNG Cloud VPC bằng địa chỉ IP riêng tư.

***

### **Tạo kết nối Interconnect** <a href="#batdauvoiinterconnect-taoketnoiinterconnect" id="batdauvoiinterconnect-taoketnoiinterconnect"></a>

Thực hiện các bước sau đây để tiến hành tạo kết nối Interconnect đến địa điểm sử dụng của bạn:

**Bước 1: Chọn vị trí Interconnect của bạn:**

Quyết định vị trí Interconnect của bạn, số lượng kết nối bạn muốn sử dụng và kích thước cổng. Nhiều cổng có thể được sử dụng đồng thời để tăng băng thông hoặc dự phòng.

**Bước 2: Chọn loại kết nối vật lý của bạn:**

Chọn giữa kết nối chuyên dụng hoặc kết nối được lưu trữ. Kết nối chuyên dụng cung cấp cho bạn quyền truy cập độc quyền vào kết nối chéo và cung cấp nhiều giao diện ảo. Với kết nối được lưu trữ, các đối tác chia sẻ kết nối chéo với nhiều khách hàng và chỉ cung cấp một giao diện ảo duy nhất. Tuy nhiên hiện nay chúng tôi chỉ đang hỗ trợ kết nối chuyên dụng cho các khách hàng của mình.

**Bước 3: Chọn băng thông**

Tuỳ thuộc vào nhu cầu sử dụng mà bạn có thể lựa chọn băng thông cho kết nối Interconnect của mình. Hiện tại, chúng tôi đang cung cấp hai tùy chọn băng thông: 1Gb và 10Gb.

**Bước 4: Chọn loại kết nối Interconnect**

Hiện nay, ngoài việc cung cấp dạng kết nối Direct Connect cơ bản, chúng tôi còn triển khai thêm một số loại hình kết nối khác như: Multicloud Connect, Hybrid Cloud Interconnect, VPN Interconnect để giúp bạn giải quyết các vấn đề về quản lý dữ liệu đa dạng. Để biết thêm thông tin chi tiết, xin vui lòng xem tại [Các tính năng của Interconnect](cac-tinh-nang-interconnect.md).

**Bước 5: Tạo kết nối Interconnect**

Tính năng tạo Interconnect chưa được triển khai trên giao diện người dùng, để thực hiện thao tác tạo, xin vui lòng gởi yêu cầu cho chúng tôi tại địa chỉ: [https://support.vngcloud.vn/#/app/dashboard](https://support.vngcloud.vn/#/app/dashboard) kèm các thông tin ở Bước 1, 2, 3. Sau đó chúng tôi sẽ giúp bạn thực hiện các bước tiếp theo để hoàn thành việc kết nối.
