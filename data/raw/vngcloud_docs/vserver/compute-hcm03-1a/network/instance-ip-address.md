# Instance IP Address

Địa chỉ IP là kỹ thuật được dùng để kết nối tới máy chủ. Có 2 loại địa chỉ IP đang được sử dụng cho máy chủ ảo tại VNG Cloud: private IP và public IP

### **Private IP address** <a href="#instanceipaddress-privateipaddress" id="instanceipaddress-privateipaddress"></a>

Mỗi máy chủ ảo vServer trong VPC đều được gán một địa chỉ IP private nằm trong dãy CIDR đã được định nghĩa trước đó của VPC và Subnet thuộc VPC đó.

Địa chỉ IP private có thể được sử dụng trong các trường hợp sau:

* Giao tiếp mạng nội bộ giữa các máy chủ ảo trong cùng VPC
* Giao tiếp mạng nội bộ giữa các máy chủ và các dịch vụ khác như vLB, vDB trong cùng VPC

Địa chỉ IP private được gán tự động qua dịch vụ DHCP và được gán cố định cho máy chủ ảo cho đến khi máy chủ được xóa đi.

### **Public IP address** <a href="#instanceipaddress-publicipaddress" id="instanceipaddress-publicipaddress"></a>

Máy chủ ảo trong VPC tại VNG Cloud hỗ trợ 2 loại địa chỉ IP public sau đây:

* Địa chỉ Floating IP: đây là địa chỉ IP public được gán cho máy chủ bằng kỹ thuật NAT 1:1 tại VNG Cloud gateway
* External Interface: đây là địa chỉ IP public được dùng bằng cách gắn trực tiếp interface đó vào máy chủ ảo.

Bảng tóm tắt sau mô tả những khác biệt chính của 2 loại địa chỉ IP public trên:

| Item                                          | Floating IP                                                                                                                                                                                        | External Interface                                                                                                                                                                                                                |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kịch bản sử dụng                              | Nếu bạn không muốn gắn trực tiếp interface đó vào máy chủ                                                                                                                                          | Nếu bạn muốn gắn trực tiếp interface đó vào máy chủ                                                                                                                                                                               |
| Mô tả                                         | Nếu bạn chọn Floating IP khi tạo máy chủ, VNG Cloud sẽ cấp 1 địa chỉ IP public được cấu hình NAT đến máy chủ của bạn                                                                               | Sau khi 1 External Interface được tạo ra, nó có thể được gắn trực tiếp vào máy chủ ảo, điều kiện là máy chủ này đang không dùng Floating IP                                                                                       |
| Phương pháp quản lý địa chỉ MAC và địa chỉ IP | Bạn không thể nhìn thấy hoặc tương tác trực tiếp Floating IP từ bên trong máy chủ ảo vì đây là cấu hình NAT tại VNG Cloud gateway.                                                                 | <p>Vì đây là interface được gắn trực tiếp vào máy chủ ảo, bạn có thể nhìn thấy và thao tác từ bên trong máy chủ.</p><p>Bạn phải cấu hình IP bên trong máy chủ để sử dụng được External Interface (cấu hình IP tĩnh hoặc DHCP)</p> |
| <p>Phương pháp tháo gỡ IP</p><p><br></p>      | <p>Sau khi Floating IP đc gán cho 1 máy chủ ảo, bạn chỉ có thể tháo gỡ bằng cách thao tác tại tầng quản lý của VNG Cloud.</p><p>Chi phí cho Floating IP tùy thuộc vào nhu cầu giữ Floating IP.</p> | <p>Sau khi External Interface được gắn vào 1 máy chủ ảo, bạn chỉ có thể thao gỡ bằng cách thao tác tại tầng quản lý của VNG Cloud</p><p>Chi phí cho External Interface vẫn tiếp tục cho đến khi thực hiện hủy.</p>                |
| Phương pháp hủy đăng ký IP                    | Sau khi Floating IP được tháo gỡ gỏi máy chủ ảo, bạn mới có thể xóa đi.                                                                                                                            | Sau khi External Interface được rút khỏi máy chủ ảo, bạn mới có thể xóa đi.                                                                                                                                                       |
