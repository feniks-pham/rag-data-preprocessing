# UserData

Dữ liệu người dùng (**UserData**) là nội dung thông tin tùy chỉnh của người dùng được cung cấp cho Server trên hạ tầng cloud hiện đang được triển khai và chạy trên Server đó.

Mục đích là cung cấp thêm dữ liệu cho Server để tùy chỉnh nhiều nhất có thể theo nhu cầu của ta, hạ tầng cloud vServer có hỗ trợ tình năng này.

&#x20;VNG Cloud cho phép sử dụng các loại dữ liệu nhiều cách khác nhau, Mỗi loại dữ liệu sẽ được xử lý thường là dòng đầu tiên.

* Batch
* PowerShell
* Bash
* Python
* Cloud config
* Khởi tạo UserData khi kích hoạt vServer
* Gợi ý điền câu lệnh cho UserData

## **Batch** <a href="#userdata-batch" id="userdata-batch"></a>

***

**rem cmd**

File được thực thi ở cmd.exe (có thể được thay bằng biến môi trường COMSPEC.

## **PowerShell** <a href="#userdata-powershell" id="userdata-powershell"></a>

***

**#ps1** or **#ps1\_sysnative** (system native)

**#ps1\_x86** (Windows On Windows 32bit)

Câu lệnh PowerShell sử dụng để thực thi như mong muốn.

## **Bash** <a href="#userdata-bash" id="userdata-bash"></a>

***

**#!/bin/bash**

Để sử dụng tính năng này, ta cần cài đặt Bash Shell trên hệ thống và sẵn có trên hệ thống môi trường _PATH_.

## **Python** <a href="#userdata-python" id="userdata-python"></a>

***

**#!/usr/bin/env python**

Mặc dù Python đã có sẵn theo mặc định khi cài đặt, nhưng nó cũng phải có trong hệ thống môi trường PATH.

## **Cloud config** <a href="#userdata-cloudconfig" id="userdata-cloudconfig"></a>

***

**#cloud-config**

Cấu hình Cloud config được hổ trợ, không bao gồm các nội dung riêng cho Linux. Các hướng dẫn cho việc cấu hình được hỗ trợ như sau:

* **write\_files:** Xác định một tập hợp các file mà sẽ được tạo ra trên hệ thống file nội bộ. Nó có thể là một danh sách các mục hoặc chỉ một mục, với các thuộc tính sau:

1. **path**:  Đường dẫn chính xác tuyệt đối trên ổ đĩa, nơi mà nội dung sẽ được ghi lên.
2. **content**: Nội dung mà sẽ được viết vào file đã cho.
3. **permissions**:  số nguyên đại diện cho quyền truy cập file.
4. **encoding**: Mã hóa của dữ liệu trong nội dung . Các mã hóa được hỗ trợ là:
   1. b64, base64 dành cho các nội dung được mã hóa base64;
   2. gz,gzip dành cho các nội dung được én gzip;
   3. gz+b64,gz+base64,gzip+b64,gzip+base64 danh cho các nội dung gzip được mã hóa base64.

Ví dụ:

<pre><code>#cloud-config
write_files:   
    encoding: b64   
    content: NDI=   
<strong>    path: C:\test   
</strong><strong>    permissions: '0o466'
</strong></code></pre>

```
#cloud-config
write_files:   
-   encoding: b64       
    content: NDI=       
    path: C:\b64       
    permissions: '0644'   
-   encoding: base64       
    content: NDI=       
    path: C:\b64_1       
    permissions: '0644'   
-   encoding: gzip       
    content: !!binary |           
        H4sIAGUfoFQC/zMxAgCIsCQyAgAAAA==       
    path: C:\gzip       
    permissions: '0644'
```

* **set\_timezone**: Thay đổi Múi giờ hệ thống

Ví dụ:

```
#cloud-config
set_timezone: Asia/Tbilisi
```

* **set\_hostname**: Thay đổi Tên máy chủ

Ví dụ:

```
#cloud-config
set_hostname: newhostname
```

* **groups**: Tạo nhóm nội bộ và thêm những user đang tồn tại vào các nhóm đó.

Yêu cầu định dạng của khi tạo nhóm như sau:

\<group\_name>: \[\<user1>,\<user2>]

Danh sách user có thể để trống, nên có thể tạo một nhóm mà không có user nào.

Ví dụ:

```
groups:  
- windows-group: [user1, user2]  
- cloud-users
```

* **users**: Tạo và cấu hình user nội bộ.

Những user được xác định là một danh sách, mỗi thành phần trong danh sách là đại diện cho một user. Mỗi user có thể được xác định bởi những thuộc tính sau:

1. **name:** (chuỗi bắt buộc điền): Đây là tên đăng nhập username;
2. **gecos**: Mô tả ngắn gọn về user;
3. **primary\_group**: Nhóm chính của user;
4. **groups**: Danh sách nhóm của user. Trên Windows, primary\_group và groups được ràng buộc nhau.
5. **passwd**: Mật khẩu của user. Trên Linux, mật khẩu được lưu trữ ở dạng chuỗi băm, trong khi đó trên Windows thì mật khẩu được lưu trữ dưới dạng văn bản thuần. Nếu không xác định được mật khẩu, hệ thống sẽ đặt mật khẩu ngẫu nhiên.&#x20;
6. **inactive**: giá trị Boolean (true/false) cho biết trạng thái hoạt động của user, mặc định là False. Nếu thiết lập là True, user sẽ bị vô hiệu quá.
7. **expiredate**: Ngày hết hạn của tài khoản user, định dạng là chuỗi \<year>-\<month>-\<day>. Ví dụ: 2020-10-01.
8. ssh\_authorized\_keys: Danh sách các public keySSH mà sẽ được thiết lập trong ở \~/.ssh/authorized\_keys cho phép user đó đăng nhập bằng SSH.

Ví dụ:



```
users:  
-    name: Admin  
-    name: brian    
gecos: 'Brian Cohen'    
primary_group: Users    
groups: cloud-users    
passwd: StrongPassw0rd    
inactive: False    
expiredate: 2020-10-01    
ssh_authorized_keys:      
- ssh-rsa AAAB...byV      
- ssh-rsa AAAB...ctV
```

* **ntp**: Cấu hình NTP Server, (Network Time Protocol), được định nghĩa với các thuộc tính sau:

1. enabled: Giá trị Boolean (True/False), mặc định là True, để cấu hình tắt bật NTP;
2. servers: Danh sách các máy chủ NTP;
3. pools: Danh sách các nhóm máy chủ NTP;

Server và pools được gộp chung lại, server là được ưu tiên trước trong danh sách. Trên Windows, không có khác biệt giữa một NTP pool hay server

Ví dụ:

```
#cloud-config
ntp:  
enabled: True  
servers: ['my.ntp.server.local', '192.168.23.2']  
pools: ['0.company.pool.ntp.org', '1.company.pool.ntp.org']
```

* **runcmd**: Được chỉ dẫn là nơi có thể chứa danh sách các câu lệnh mà sẽ được thực thi, theo thứ tự được xác định.

Một câu lệnh có thể được xác định là một chuỗi ký tự hay một danh sách chuỗi ký tự, với phần tử đầu tiênlà đường dẫn đến tập tin thực thi.

Trên Windows, các dòng lệnh được tập hợp lại trong một file và được thực thi với cmd.exe.&#x20;

Ví dụ:

```
#cloud-config
runcmd:  
- 'dir C:\\'  
- ['echo', '1']
```

| `#cloud-configruncmd:  - 'dir C:\\'  - ['echo', '1']` |
| ----------------------------------------------------- |

Theo chỉ thị, cloud config được thực thi theo thứ tự mặc định như sau:

1. write\_files: Tạo và ghi nội dung vào file được xác định;
2. set\_timezone: Cài đặt múi giờ;
3. set\_hostname: Thay đổi tên máy chủ của Server;
4. ntp: Cấu hình mấy chủ NTP để đồng bộ hóa thời gian
5. groups: Tạo vả quản lý nhóm user nội bộ;
6. users: Tạo và cấu hình tài khoản người dùng nội bộ;
7. runcmd: Cahy5 các lệnh được cung cấp trong quá trình khởi tạo

Có thể dùng tùy chọn là  _cloud\_config\_plugins_ để lọc hoặc thay đổi thứ tự các plugin cloud-config.

Việc thực thi việc đổi tên máy chủ _set\_hostname_ hay chạy các câu lệnh _runcmd_ có thể cần được khổi động lại Server nếu cần. Việc khởi động lại sẽ được thực hiện **sau** khi tất cả các chỉ thị được thực thi.

\


## **Khởi tạo UserData khi kích hoạt vServer** <a href="#userdata-khoitaouserdatakhikichhoatvservercreateuserdataserver" id="userdata-khoitaouserdatakhikichhoatvservercreateuserdataserver"></a>

***

Để nhập các dòng lệnh để thực hiện việc cung cấp UserData cho Server thì bạn có thể thực hiện ở bước Khởi tạo Server (Bước 4 ở Trải nghiệm sản phẩm vServer ở [**đây**](./)) như sau:

* Tại bước cấu hình "**Network setting**" để thực hiện việc cấu hình nhập UserData thì ta sẽ chọn tùy chọn "**UserData**" như hình bên dưới.

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761115/image2024-3-12_10-31-40.png?version=1&#x26;modificationDate=1710214301000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* Ta có thể tải lên (upload) file hoặc **điền những câu lệnh vào field nội dung** để thực thi việc cung cấp thông tin user vào Server. Tham khảo ở bên dưới mục "[Gợi ý điền câu lệnh cho UserData](userdata.md#userdata-goiydiencaulenhchouserdatasuggestscriptuserdata)", VNG Cloud cung cấp gợi ý mặc định câu lệnh scripts để tiện việc cấu hình UserData.
* Nếu thông tin người dùng UserData ở các tools đang sử dụng đã được mã hóa Base64 thì ta sẽ chọn vào "**User Data is base64 encoded**".

## **Gợi ý điền câu lệnh cho UserData** <a href="#userdata-goiydiencaulenhchouserdatasuggestscriptuserdata" id="userdata-goiydiencaulenhchouserdatasuggestscriptuserdata"></a>

***

Khi tạo Server Windows, VNG Cloud cung cấp đoạn câu lệnh mặc định (Default Scripts) ngay tại trường User Data, bao gồm cả thông tin bản quyền hệ điều hành Windows mà ta có thể sử dụng ngay:

> `#ps1`
>
> `net user stackops VngP@ssword2` `/logonpasswordchg:yes  /y`
>
> `net localgroup administrators stackops /add`
>
> `Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal*Server\WinStations\RDP-TCP\" -Name PortNumber -Value 3490`
>
> `net stop TermService /y`
>
> `net start TermService /y`
>
> `netsh advfirewall firewall add rule name="RDP-3490"` `dir=in action=allow protocol=TCP localport=3490`
>
> `w32tm /config /syncfromflags:manual /manualpeerlist:time.windows.com`
>
> `w32tm /config /update`
>
> `w32tm /resync /nowait`
>
> `cscript.exe slmgr.vbs /ipk N69G4-B89J2-4G8F4-WWYCC-J464C`
>
> `cscript.exe slmgr.vbs /skms kms.vngcloud.vn`
>
> `cscript.exe slmgr.vbs /ato`

Trong đó với các thông tin:

* **stackops VngP@ssword2** : là Username và password của OS;
* **N69G4-B89J2-4G8F4-WWYCC-J464C** : là key kích hoạt bản quyền (activation key) của OS, hệ thống sẽ tự động tham chiếu (mapping) theo key và OS tương ứng:

```
{  
"Windows Server 2016 Standard": "WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY",
"Windows Server 2019 Standard": "N69G4-B89J2-4G8F4-WWYCC-J464C",  
"Windows Server 2012 Server Standard": "XC9B7-NBPP2-83J2H-RHMBY-92BT4",  
"Windows Server 2012 R2 Server Standard": "D2N9P-3P6X9-2R39C-7RTCD-MDVJX",  
"Windows Server 2022 Standard": "VDYBN-27WPP-V4HQT-9VMD4-VMK7H"
  }
```

Kết quả hiển thị sẽ được hiển thị mặc định như sau trên giao diện người dùng:

<figure><img src="https://docs.vngcloud.vn/download/attachments/73761115/image2024-3-13_16-54-33.png?version=1&#x26;modificationDate=1710323674000&#x26;api=v2&#x26;effects=border-simple,blur-border" alt=""><figcaption></figcaption></figure>

Lưu ý

Việc sử dụng license của Windows được xác thực theo IP mà VM đã mua license, từ đó hệ thống sẽ kích hoạt bản quyền.
