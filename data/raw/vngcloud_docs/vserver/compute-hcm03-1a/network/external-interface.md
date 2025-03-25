# External Interface

### **Các trường hợp sử dụng External Interface** <a href="#externalinterface-cactruonghopsudungexternalinterface" id="externalinterface-cactruonghopsudungexternalinterface"></a>

Việc gắn trực tiếp External Interface vào máy chủ ảo sẽ hữu ích trong các trường hợp sau:

* Cần nhìn thấy IP trực tiếp của interface đối với 1 số giao thức đặc biệt (Ví dụ: như giao thức SIP)
* Tự xây dựng chức năng firewall hoặc VPN gateway bằng máy chủ ảo có 2 interface, trong mạng nội bộ và ngoài mạng public
* Tự xây dựng giải pháp HA với chi phí thấp

### **Tổng quan về External Interface** <a href="#externalinterface-tongquanveexternalinterface" id="externalinterface-tongquanveexternalinterface"></a>

Bạn có thể tạo External Interface, gắn nó vào máy chủ ảo, gỡ nó khỏi máy chủ ảo và gắn vào máy chủ ảo khác. Khi bạn chuyển External Interface từ máy chủ ảo này sang máy chủ ảo khác, đường đi của mạng cũng sẽ chuyển đến máy chủ ảo mới.

Bạn cần cấu hình địa chỉ IP cho External Interface từ trong hệ điều hành của máy chủ ảo, cấu hình IP tĩnh hoặc DHCP đều đc chấp nhận. Bạn chỉ có thể gắn External Interface vào máy chủ không có Floating IP.

***

### **Làm việc với External Interface** <a href="#externalinterface-lamviecvoiexternalinterface" id="externalinterface-lamviecvoiexternalinterface"></a>

#### Tạo External Interface <a href="#externalinterface-taoexternalinterface" id="externalinterface-taoexternalinterface"></a>

1. Vào trang VNG Cloud portal console, đến trang External Interface
2. Tạo External Interface, bạn có thể xem chi phí ở bên phải
3. Sau khi tạo xong bạn sẽ có thông tin của IP, netmask và gateway được cấp cho External Interface, những thông tin này cần thiết cho việc cấu hình IP trong hệ điều hành sau này

#### Gắn/Tháo gỡ trên máy chủ ảo <a href="#externalinterface-gan-thaogotrenmaychuao" id="externalinterface-gan-thaogotrenmaychuao"></a>

1. Vào trang VNG Cloud portal console, đến trang Instance
2. Đi đến trang chi tiết của máy chủ ảo cần thao tác External Interface, đi đến tab Network Interface
3. Nhấn **Attach an Interface** và chọn External Interface mà bạn đã mua trước đó. Khi tháo gỡ, bạn chỉ việc chọn xác nhận sau khi nhấn **Detach an Interface**
4. Sau khi gắn External Interface, bạn cần phải cấu hình IP từ trong hệ điều hành của máy chủ để sử dụng

#### Xóa External Interface <a href="#externalinterface-xoaexternalinterface" id="externalinterface-xoaexternalinterface"></a>

1. Vào trang VNG Cloud portal console, đến trang External Interface
2. Chọn External Interface cần delete, nhấn **Delete** ở bên phải
