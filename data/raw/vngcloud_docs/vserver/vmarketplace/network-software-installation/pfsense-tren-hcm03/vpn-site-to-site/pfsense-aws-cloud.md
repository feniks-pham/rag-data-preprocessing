# PFsense - AWS Cloud

### **AWS** <a href="#pfsense-awscloud-aws" id="pfsense-awscloud-aws"></a>

1. Đăng nhập vào tài khoản AWS của bạn và truy cập vào **VPC** trong Console
2. Trong thanh bên, dưới phần Kết nối VPN, vào mục **Customer Gateways**
   1. Nhấn nút **Create Customer Gateway**&#x20;
      * Nhập tên cho Gateway (e.g., Seattle Office)
      * Đổi **Routing** thành **Dynamic**
      * Nhập số **BGP ASN của bạn** (Nếu bạn không có số công cộng, hãy chọn bất kỳ số nào từ 64512-65534. Đây là các số ASN riêng tư). Ghi nhớ số này để sử dụng sau.
      * Nhập **Public IP của pfSense box** của bạn
      * Nhấn chọn **Yes, Create**
3. Bên dưới VPN Connections, chọn đến **Virtual Private Gateways**
   1. Nhấn chọn nút **Create Virtual Private Gateway**
      * Điền tên Virtual Private Gateway (ví dụ Office VPN)
      * Nhấn **Yes, Create**
   2.  **Chọn vào VPG** vừa tạo và nhấn chọn **Attach to VPC**&#x20;

       * **Chọn VPC** và nhấn **Yes, Attach**



       <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-2.53.09-PM-1024x366.png" alt=""><figcaption></figcaption></figure>
4. Bên dưới Virtual Private Cloud, chọn tới **Route Tables**
   1. Tại mỗi Route Table trong VPC:
      * Chọn Route Table
      * Chọn Tab **Route Propagation** ở bảng bên dưới&#x20;
      * Bạn thấy danh sách Virtual Private Gateway
      * Chọn nút **Edit** và  chọn vào ô **Propagate Checkbox** và sau đó chọn **Save**
5. Bên dưới VPN Connections, chọn tới **VPN Connections**
   1.  Nhấn chọn nút  **Create VPN Connection**

       * Điền tên kết nối VPN (ví dụ Seattle Office VPN)
       * Chọn **Virtual Private Gateway** đã tạo.
       * Chọn **Existing Customer Gateway** và chọn CGW đã tạo trước .
       * Chọn **Dynamic (requires BGP)**
       * Chọn **Yes, Create**

       <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-2.54.38-PM-1024x643.png" alt=""><figcaption></figcaption></figure>
   2.  Chọn VPN vừa tạo VPN sau đó nhấn chọn nút **Download Configuration**.

       * Trường **Vendor** chọn **Generic**
       * Nhấn chọn **Download**



       <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-2.55.09-PM-1024x571.png" alt=""><figcaption></figcaption></figure>

       * Chọn  **Cancel** để đóng
6. **Mở** tệp tin cấu hình đã tải về. Ta sẽ dùng những thông tin chứa trong tệp tin để cấu hình pfSense. Điều này sẽ  có 2 kết nối VPN. Bất cứ kết nố nào bạn chọn, đảm bảo thực hiện nhất quán để chắc nhắn rằng bạn đang nhập đúng trong pfSense.
7.

    <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.16.54-PM-1024x522.png" alt=""><figcaption></figcaption></figure>

### **pfSense** <a href="#pfsense-awscloud-pfsense" id="pfsense-awscloud-pfsense"></a>

1. Đăng nhập pfSense và điều hướng đến màn hình **System -> Package Manager**
   * Chọn **Available Packages**
   * Tìm kiếm từ khóa “bgp”
   * Tìm gói **OpenBGPD** và chọn **Install**, sau đó chọn **Confirm**
   * Đợi  đến khi cài đặt xong.
2.  Đến màn hình **Firewall -> Virtual IPs**

    1. Chọn **Add**
    2. Chọn Type: **IP Alias**
    3. Chọn Interface: **Localhost**
    4. Chọn Address: **(your inside IP address)/30**
       *   Trong tệp tin cấu hình bạn tải từ AWS, cuộn tìm đến **Inside IP Addresses**  và tìm IP **Customer Gateway**.  Đây là Virtual IP ta đặt vào pfSense. đừng quên điền /30!\


           <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.15.51-PM-1024x312.png" alt=""><figcaption></figcaption></figure>
    5. Thêm mô tả nếu bạn muốn ( ví dụ AWS VPN Inside Address);
    6. Có thể để mọi thông tin ở dạng mặc định;
    7. Chọn **Save** sau đó chọn **Apply Changes**\


    <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.13.23-PM-1024x634.png" alt=""><figcaption></figcaption></figure>
3. Đến màn hình **VPN -> IPSec**
   1. chọn **Add P1** (Add Phase 1) _( Lưu ý:_ Những thông tin tiếp theo sẽ được tìm thấy trong tệp cấu hình mà bạn đã tải về từ AWS)
      1. Trọng pfSense, thiết lập **Remote Gateway** với IP tìm thấy trong tệp tin cấu hình:
         * Trọng tệp tin cấu hình mà bạn đã tải xuống từ AWS, cuộn xuống tới khi tìm thấy **Outside IP Addresses** và tìm IP **Virtual Private Gateway** . Đậy là IP Public ta muốn đưa vào pfSense cho Remote Gateway.
      2.  Trọng tệp tin cấu hình, tìm đến đoạn nói về **#1: Internet Key Exchange Configuration**. Bạn cần kiểm tra lại các thuật toán vì chúng có thể thay đổi, nhưng phần còn lại nên giống nhau.

          * Trong pfSense, thiết lập **Pre-Shared Key** với key được tìm thấy trong tệp tin cấu hình.
          * Với thuật toán  **Encryption Algorithm** chọn **AES** và **128 bits**
          * Đảm bảo thuật toán **Hash Algorithm** được thiết lập là **SHA1**, **DH Group** được thiết lập là **2 (1024 bit)** và **Lifetime (Seconds)được thiết lập là** **28800**
          * Thêm mô tả nếu bạn muốn (ví dụ, AWS VPN Tunnel #1)
          * Có thể để mọi thông tin ở dạng mặc định và chọn **Save**



          <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.17.27-PM-1024x530.png" alt=""><figcaption></figcaption></figure>
   2. Trong pfSense, bên dưới  chỗ VPN vừa tạo, chọn **Show Phase 2 Entries** sau đó chọn **Add P2**
      1. Đối với **Local Network**, chọn  **Network** và điền **Inside IP Address** vào phần **Customer Gateway** mà được tìm thấy ở đoạn **#3: Tunnel Interface Configuration** của tệp tin đã tải về, đừng quên điền /30.
      2. Đối với **Remote Network**, chọn **Network** và điền **Inside IP Address** vào phần **Virtual Private Gateway** mà được tìm thấy ở đoạn **#3: Tunnel Interface Configuration** của tệp tin đã tải về, đừng quên điền /30.
      3. Thêm mô tả nếu bạn muốn  (ví dụ AWS VPN Tunnel #1 Phase 2)
      4. Kiểm tra lại nhưng cài đặt có giống với đoạn **#2: IPSec Configuration** trong tệp tin đã tải hay không:
         * Đảm bảo **Protocol** được thiết lập là **ESP**
         * Với thuật toán **Encryption Algorithms**,đảm bảo chỉ **AES được chọn** và thiết lập **128 bits**
         * Với thuật toán **Hash Algorithms**, đảm bảo **SHA1 được chọn**
         * Với **PFS key group**, thiết lập **2 (1024 bit)**. Điều này tương ứng với phần Perfect Forward Secrecy của tập tin cấu hình.
         * Đảm bảo **Lifetime** thiết lập **3600** giây
      5.  Chọn **Save**\


          <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.19.13-PM-1024x924.png" alt=""><figcaption></figcaption></figure>
   3.  Trong pfSense, bên dưới chỗ kết nối VPN connection, chọn **Show Phase 2 Entries** và sua đó chọn lại **Add P2**&#x20;

       1. Chọn **Local Network là** **LAN subnet**
       2. Đối với **Remote Network** điền **VPC CIDR Block** (ví dụ 172.31.0.0/16)
       3. Thêm mô tả nếu bạn muốn  (ví dụAWS VPN Tunnel #1 VPC Subnet)
       4. Đảm bảo tất cả thiết lập **Phase 2 Proposal** giống với những các trong Phase 2 ta đã thêm.
          * Đảm bảo **Protocol** thiết lập **ESP**
          * Đối với thuật toán **Encryption Algorithms**, đảm bảo chỉ **AES được chọn** và thiết lập là **128 bits**
          * Đối với thuật toán **Hash Algorithms**, đảm bảo chỉ **SHA1 được chọn**
          * Đối với **PFS key group**, thiết lập **2 (1024 bit)**. Điều này tương ứng với  Perfect Forward Secrecy của tập tin cấu hình.
          * Đảm bảo **Lifetime** thiết lập **3600** giây
       5. chọn **Save** và sau đ1o chọn **Apply Changes**



       <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.21.07-PM-1024x923.png" alt=""><figcaption></figcaption></figure>
4. Đến màn hình **Firewall -> Rules**&#x20;
   1. Chọn  **IPSec** và chọn **Add** (không quan trọng nút nào)
      * Để như mặc định, ngoại trừ **Protocol** đổi thành **Any**
      * Chọn **Save** và **Apply Changes**
5. Đến màn hình **Services -> OpenBGPD** _( Tất cả thông tin sau có thể được tìm thấy ở đoạn   #4 Border Gateway Protocol (BGP) Configuration section của tệp tin cấu hình đã tải)._
   1. &#x20;Dưới chỗ **Settings** thiết lập như sau:
      1.  Số Autonomous System (AS): **(Số mà bạn đã thiết lập Customer Gateway iở AWS)**\


          <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.22.28-PM-1024x421.png" alt=""><figcaption></figcaption></figure>
      2. Thiết lập Holdtime: **30**
      3. Điền IP: **(địa chỉ IP trong Customer Gateway)**
         * Ta **không** cần /30 ở đây
      4. Điền Networks: **(Your local subnet, e.g., 192.168.1.0/24)**
         * Nếu bạn muốn thêm nhiều mạng con cục bộ hơn để được phát tán đến AWS, hãy nhấp vào nút **Add** cho bao nhiêu mạng bạn có và nhập vào các mạng con (subnets) bổ sung của bạn.
      5.  Chọn **Save**\


          <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.24.33-PM-1024x823.png" alt=""><figcaption></figcaption></figure>
   2.  Chọn **Groups**

       1. Chọn **Add**
       2. Đặt tên ( ví dụ AWS\_VPC)
       3. Điền số **Remote AS** trong tệp tin cấu hình ( ví dụ 7224)
       4. Điền mô tả nếu cần
       5. Chọn **Save** và sau đó chọn **Save** một lần nữa



       <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.23.07-PM-1024x587.png" alt=""><figcaption></figcaption></figure>
   3. Chọn **Neighbors**
      1. Chọn **Add**
      2. Điền mô tả nếu cần ( ví dụ AWS VPC Neighbor)
      3. Đối với **Neighbor**, điền địa chỉ **Neighbor IP Address**  trọng tệp tin cấu hình
      4. Đảm bảo **Group** đươc thiết lập theo tên nhóm của bước trước
      5.  Để các cấu hình như mặc định và chọn  **Save**\
          \


          <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.23.34-PM-1024x627.png" alt=""><figcaption></figcaption></figure>
6.  Đến màn hình **Status -> IPsec**

    1. Nếu VPN chưa sẳn sàng kết nối, chọn **Connect**
    2. Sau vài giây, làm mới lại trang và đảm bảo trạng thái VPN  là **ESTABLISHED**. Nếu là  CONNECTING, hãy kiểm tra thiết lập lại một lần nữa.



    <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.37.13-PM-1024x499.png" alt=""><figcaption></figcaption></figure>
7. Đến màn hình **Services -> OpenBGPD**
   1. Chọn **Status**
   2.

       <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.25.08-PM-1024x540.png" alt=""><figcaption></figcaption></figure>
   3. Nếu mọi thức hoạt động đúng, ta thấy được thời gian kết nối ở cột Up/Down của bảng  OpenBGPD Summary và thông tin theo đó được thay đổi.
   4.

       <figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.25.23-PM-1024x348.png" alt=""><figcaption></figcaption></figure>

### **Kiểm tra sự kết nối** <a href="#pfsense-awscloud-testingconnectivity" id="pfsense-awscloud-testingconnectivity"></a>

<figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.25.57-PM-1024x350.png" alt=""><figcaption></figcaption></figure>

Trở lại AWS, chúng ta có thể kiểm tra các bảng định tuyến cho VPC của mình. Trong bảng điều khiển, kiểm tra một bảng định tuyến. Khi bạn nhấp vào tab **Routes** , bạn nên thấy các định tuyến từ pfSense được phát tán đến AWS.

Trên các máy ảo EC2 của bạn, nếu các nhóm bảo mật (Security Groups) của bạn được cấu hình để cho phép ICMP và/hoặc SSH từ mạng nội bộ của bạn, bạn sẽ có thể ping và/hoặc SSH giữa các thực thể trong mạng nội bộ của bạn và AWS VPC.\


<figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.28.03-PM-300x139.png" alt=""><figcaption></figcaption></figure>

Trong ví dụ , ta có một máy ảo Ubuntu đang chạy trong mạng VNG Cloud của tôi và một máy ảo EC2 đang chạy trong VPC . Sau khi cấu hình các nhóm bảo mật, ta có thể ping thành công giữa hai máy này!\


<figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.28.48-PM-300x104.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://s3-us-west-2.amazonaws.com/1s-blog/pfsense-vpn-screenshots/Screen-Shot-2017-08-21-at-3.31.45-PM-300x127.png" alt=""><figcaption></figcaption></figure>
