# Tự động gia hạn tài nguyên - Chính sách và điều khoản

Sử dụng tài liệu này để hiểu thêm về tính năng tự động gia hạn tài nguyên. Tài liệu sẽ mô tả chi tiết các bước xử lý liên quan đến việc **tự động gia hạn tài nguyên và chi phí phát sinh** khi tự động gia hạn tài nguyên. Các bước khác sẽ giản lược bớt và chỉ đề cập đến như một phần của quy trình.&#x20;

#### 1. Chính sách tự động gia hạn tài nguyên chỉ áp dụng đối với: <a href="#tudonggiahantainguyen-chinhsachvadieukhoan-1.chinhsachtudonggiahantainguyenchiapdungdoivoi" id="tudonggiahantainguyen-chinhsachvadieukhoan-1.chinhsachtudonggiahantainguyenchiapdungdoivoi"></a>

* **Đối tượng:** Người dùng trả trước
* **Tài nguyên**: Tất cả các tài nguyên cho phép tự động gia hạn và đang trong thời gian sử dụng
* **Nguồn tiền**: VNG Cloud Credit

#### **2. Hướng dẫn bật/tắt tính năng "Tự động gia hạn"** <a href="#tudonggiahantainguyen-chinhsachvadieukhoan-2.huongdanbat-tattinhnang-tudonggiahan" id="tudonggiahantainguyen-chinhsachvadieukhoan-2.huongdanbat-tattinhnang-tudonggiahan"></a>

**2.1 Đối với các sản phẩm dịch vụ vStorage:** [**https://docs.vngcloud.vn/pages/viewpage.action?pageId=49649654**](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49649654)

**2.2 Đối với các sản phẩm, dịch vụ vServer**

*   **Bật "Tự động gia hạn" khi khởi tạo**

    * Bước 1: Cấu hình thông tin dịch vụ tại trang sản phẩm → Nhấn "**Khởi tạo**" để chuyển đến trang thanh toán
    * Bước 2: Tại trang thanh toán, tick vào "**Auto-renew**" để bật tính năng tự động gia hạn

    <figure><img src="../../../../.gitbook/assets/image (919).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="https://docs.vngcloud.vn/download/attachments/49649295/image2023-12-12_10-49-53.png?version=1&#x26;modificationDate=1702352993000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
* **Bật/Tắt trong quá trình sử dụng dịch vụ**\

  * Bước 1: Điều hướng đến trang Resource Billing trong dịch vụ vServer: [https://hcm-3.console.vngcloud.vn/vserver/billing](https://hcm-3.console.vngcloud.vn/vserver/billing)
  * Bước 2: Nhấn vào biểu tượng ba chấm tại vị trí tài nguyên cần thực hiện thay đổi. Xem hình bên dưới
    * Chọn **"Tự động gia hạn"** để bật tính năng tự động gia hạn nếu chưa bật khi khởi tạo
    * Chọn **"Cập nhật tự động gia hạn"** để điều chỉnh thời gian sử dụng tài nguyên được áp dụng khi hệ thống thực hiện tự động gia hạn
    * Chọn **"Tắt tự động gia hạn"** để tắt tính năng tự động gia hạn nếu không có nhu cầu

<figure><img src="../../../../.gitbook/assets/image (920).png" alt=""><figcaption></figcaption></figure>

**2.3 Đối với sản phẩm, dịch vụ vMonitor**

* **Bật "Tự động gia hạn" khi khởi tạo**
  * Bước 1: Cấu hình thông tin dịch vụ tại trang sản phẩm → Nhấn "Khởi tạo" để chuyển đến trang thanh toán
  * Bước 2: Tại trang thanh toán, tick vào "Auto-renew" để bật tính năng tự động gia hạn

<figure><img src="../../../../.gitbook/assets/image (921).png" alt=""><figcaption></figcaption></figure>

_Lưu ý: Hiện tại các dịch vụ trong sản phẩm vMonitor chưa hỗ trợ tắt tự động gia hạn khi người dùng bật lúc khởi tạo. Để tắt tự động gia hạn khi không có nhu cầu, vui lòng liên hệ đội ngũ 247 để hỗ trợ thêm._

#### **3. Quy trình tự động gia hạn tài nguyên** <a href="#tudonggiahantainguyen-chinhsachvadieukhoan-3.quytrinhtudonggiahantainguyen" id="tudonggiahantainguyen-chinhsachvadieukhoan-3.quytrinhtudonggiahantainguyen"></a>

Tự động gia hạn tài nguyên là **tính năng của hệ thống**, giúp quá trình sử dụng tài nguyên của người dùng không bị gián đoạn tại thời điểm kết thúc tài nguyên (người dùng có nhu cầu tiếp tục sử dụng nhưng quên không thực hiện gia hạn trên hệ thống vì lý do nào đó).

**Điều khoản áp dụng dành cho tính năng "Tự động gia hạn" trên VNG Cloud như sau:**

* Gửi mail thông báo các tài nguyên cần **trước 7 ngày**, tính từ thời điểm kết thúc tài nguyên. Mục đích để người dùng chuẩn bị đủ số dư credit
* Tài nguyên được mặc định **gia hạn thêm 1 tháng**, kể từ thời điểm kết thúc
* Người dùng cần chuẩn bị đủ số dư credit khả dụng theo như thông báo để hệ thống có thể tiến hành gia hạn
* Hệ thống chính thức thực hiện **gia hạn trước 3 ngày**, tính từ thời điểm kết thúc tài nguyên
  * Cách tính giá khi hệ thống tự động gia hạn không khác biệt so với việc người dùng chủ động gia hạn tài nguyên, tham khảo thêm [tại đây](gia-han-tai-nguyen.md)
  * Hệ thống gửi thông tin tài nguyên được gia hạn thành công/thất bại đến người dùng
  * Hệ thống phát sinh hóa đơn tương ứng với khoảng thời gian được gia hạn thêm
* Với các tài nguyên đã kết thúc sẽ không áp dụng tự động gia hạn. Có nghĩa khi tài nguyên được bật tự động gia hạn, nhưng quá trình tự động gia hạn thất bại do thiếu credit, dẫn đến việc tài nguyên bị hết hạn, trong trường hợp này người dùng cần chủ động thực hiện khôi phục tài nguyên để tiếp tục sử dụng dịch vụ. Tham khảo hướng dẫn [Khôi phục tài nguyên](khoi-phuc-tai-nguyen.md)
