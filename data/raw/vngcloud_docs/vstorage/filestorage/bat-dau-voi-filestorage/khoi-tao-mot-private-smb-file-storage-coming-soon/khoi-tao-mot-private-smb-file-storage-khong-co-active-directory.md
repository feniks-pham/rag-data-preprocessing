# Khởi tạo một Private SMB File Storage không có Active Directory

Để khởi tạo một SMB (Server Message Block) không có Active Directory trên hệ thống File Storage, bạn có thể làm theo các bước sau:

## Khởi tạo Windows server on vServer

Dưới đây là hướng dẫn cơ bản cho việc khởi tạo Windows server trên vServer, nếu bạn đã có sẵn server, hãy bỏ qua bước này.&#x20;

<details>

<summary>Hướng dẫn tạo Windows server</summary>

Trước khi có thể thực hiện khởi tạo Windows server, hãy đảm bảo bạn khởi tạo VPC, Subnet trên hệ thống vServer. Tiếp theo, thực hiện các bước theo hướng dẫn bên dưới để khởi tạo Windows server:&#x20;

1. Đăng nhập vào vServer tại [https://hcm-03.console.vngcloud.tech/vserver](https://hcm-03.console.vngcloud.tech/vserver/v-server/create-server).
2. Tiếp tục chọn mục **Servers**.
3. Chọn **Create a Server.**
4. Ở mục **Basic Configuration**, nhập **Server name** để mô tả tên cho Server của bạn. Tên Server có thể bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào nằm trong khoảng từ 5 đến 50. Nó không được bao gồm khoảng trắng ở đầu hoặc ở cuối và tên Server name phải khác với Username
5. Lựa chọn **Zone** mà bạn mong muốn tạo server.
6. Nhập thông tin **Tag** bao gồm **Key**/ **Value** cho server và click **Add** để thêm tag này nếu bạn có nhu cầu.
7. Lựa chọn **OS Images: Windows,** tiếp tục chọn **Window version** tùy thuộc theo nhu cầu sử dụng của bạn.
8. Dưới mục **Instance type,** là danh sách các cấu hình Flavor, bạn có thể chọn cấu hình Flavor mong muốn cho Server của mình theo. **iot.v1.small1x1** được chúng tôi đề xuất như một cấu hình cơ bản mặc định để khởi tạo Server
9. Ở mục **Volume Settings**, nhập cấu hình cho Boot OS Volume (Root) gồm **Size GB**, **Volume Type SSD** và **IOPS**, sau đó chọn **Next**
10. Ngoài ra bạn có thể thêm **Data Volume** vào Server trong quá trình khởi tạo bằng cách chọn **Add Data volume,** sau đó **n**hập cấu hình cho Data Volume gồm **Volume name**, **Size GB**, **Volume Type SSD** và **IOPS**, chọn **Next**
11. Kế tiếp chọn thông số mục **Network settings:** Tại đây có thể chọn **VPC** để cấp Private IP cho Server và **Subnet** từ danh sách bạn đã tạo trước đó, hoặc có thể nhấn vào [**đây**](https://hcm-3.console.vngcloud.vn/vserver/network/vpc) để tạo mới VPC và Subnet, cần lưu ý ràng sau khi tạo VPC và Subnet, nó sẽ hiển thị tại trang danh sách cho phép bạn chọn trong quá trình khởi tạo Server:
    1. Tích vào ô Floating IP để gán Public IP cho Server (Nhấn vào [**đây**](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/network/floating-ip) để xem hướng dẫn attach/ detach Floating IP)
    2. **Security group** để quản lý bộ ACL - Access Control List cho Server. (Nhấp vào [**đây**](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/security/security-groups) để xem hướng dẫn tạo và quản lý Security group)
12. Nhập thông tin **Authentication**: Empty: hệ thống sẽ tự động tạo và gắn password hoặc user tự tinh chỉnh và enable hay disable việc bỏ qua change password lần đầu.
13. Ở mục **Other Settings**, có thể tùy chọn server Group hoặc không theo nhu cầu sử dụng. Bạn có thể gán Server vào các Group trước đó đã tạo (Với các thuộc tính như cùng Compute Host hay khác Compute Host)
14. Chọn **Launch Server** và thực hiện các bước thanh toán để hoàn thành việc khởi tạo server

<img src="../../../../.gitbook/assets/image (21) (2).png" alt="" data-size="original">

</details>

{% hint style="info" %}
**Chú ý:**&#x20;

Security Groups trên Windows server cần mở thêm các port sau để share được dữ liệu:

* Với File Storage NFS: mở thêm port **2049**
* Với File Storage SMB có Basic Authentication: mở thêm port **445**
* Với File Storage SMB Có Active Directory Authentication: mở thêm list port để có thể kết nối được từ File Storage đến AD.
{% endhint %}

***

## Kết nối tới Windows server vừa khởi tạo

Dưới đây là hướng dẫn cơ bản cho việc kết nối tới Windows server trên vServer, nếu bạn đã sử dụng Console trực tiếp trên vServer Portal, vui lòng bỏ qua bước này.

<details>

<summary>Kết nối tới Windows server </summary>

**Để có thể kết nối vào máy chủ Window, trước tiên, bạn cần cài đặt RDP:** Theo mặc định, Windows sẽ bao gồm RDP Client. Để xác minh, hãy nhập **mstsc** tại cửa sổ Command Prompt. Nếu máy tính của bạn không nhận ra lệnh này, hãy xem trang chủ Windows và tìm kiếm bản tải xuống cho ứng dụng[ Microsoft Remote Desktop](https://www.microsoft.com/vi-vn/windows).

1. Truy cập vào trang quản lý Server tại trình điều khiển của chúng tôi tại: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Chọn **Server** cần kết nối, sau đó chọn **Action, tiếp tục chọn Connect**
3. Trên trang **Connect to Server**, chọn tab **RDP (Window)**

<img src="../../../../.gitbook/assets/image (894).png" alt="" data-size="original">

4. Chọn **Download RDP File**. Trình duyệt của bạn sẽ nhắc bạn mở hoặc lưu tệp RDP. Khi bạn đã hoàn tất tải xuống tệp, hãy chọn **Done** để quay lại trang máy chủ:
5. Thực hiện mở tệp tin đã tải xuống để thực hiện remote tới Windows server. Chọn **Connect** để tiếp tục kết nối với máy chủ của bạn

<img src="../../../../.gitbook/assets/image (895).png" alt="" data-size="original">

6. Tài khoản quản trị viên được chọn theo mặc định. Bạn cần sao chép và dán mật khẩu mà bạn đã lưu trước đó vào pop-up đăng nhập (Thông tin này lấy từ email), trong đó nhập thông tin **InstanceLogin** vào **Username**, **InstancePassword** vào **Password.**
7. Chọn **OK.** Do tính chất của chứng chỉ tự ký, bạn có thể nhận được cảnh báo rằng chứng chỉ bảo mật không thể được xác thực. Sử dụng các bước sau để xác minh danh tính của máy tính từ xa hoặc chỉ cần chọn **Yes** (Windows) hoặc **Continue** (Mac OS X) nếu bạn tin cậy chứng chỉ.

<img src="https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252FNH1l2utiMi3RJxfBoknu%252Fimage.png%3Falt%3Dmedia%26token%3Db50838b8-d830-4273-a67f-6ccfe237ccf4&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f64057f4&#x26;sv=2" alt="" data-size="original">

8. Màn hình sẽ hiển thị đang kết nối đến máy chủ **Window** thành công

<img src="../../../../.gitbook/assets/image (896).png" alt="" data-size="original">

</details>

Sau khi bạn đã kết nối được vào Windows server, bạn cần đảm bảo Windows server của bạn đã có địa chỉ IP tĩnh, bạn có thể kiểm tra và cấu hình IP tĩnh theo hướng dẫn sau:&#x20;

* **Kiểm tra cấu hình mạng của VM bằng cách:**
  * Truy cập **Control Panel > Network & Internet > Network Connections**.
  * Chọn **Ethernet adapter**, nhấp chuột phải và chọn **Properties**.
* **Thiết lập địa chỉ IP tĩnh (Static IP):**
  * Trong màn hình **Properties**, chọn **Internet Protocol Version 4 (TCP/IPv4)** rồi bấm nút **Properties**.
  * Chọn **Use the following IP address** để thiết lập địa chỉ IP tĩnh.
  * Cung cấp thông tin địa chỉ:
    * **IP Address:** địa chỉ IP tĩnh của VM.
    * **Subnet Mask:** Subnet tương ứng, ví dụ: 255.0.0.0

<figure><img src="../../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

***

## Khởi tạo File Storage

**Bước 1:** Truy cập vào [https://efs.console.vngcloud.vn/overview](https://efs.console.vngcloud.vn/overview)

**Bước 2:** Chọn mục **File Storage** sau đó chọn **Create a File storage.**

**Bước 3:** Tại màn hình khởi tạo File Storage, bạn cần nhập/ chọn:&#x20;

* **File Storage name:** tên gợi nhớ của file storage. Tên file cần dài từ 5 tới 50 ký tự và có thể bao gồm các ký tự a-z, A-Z, 0-9, '-', '\_'
* **Description**: nhập mô tả cho file storage.
* **File storage type:** chọn loại ổ đĩa mà bạn mong muốn sử dụng. Hiện tại chúng tôi chỉ cung cấp loại ổ đĩa **Standard HDD.**
* **Protocol:** chọn NFS và version NFS mà bạn mong muốn
* **Tag:** bạn có thể thêm các tag để đánh dầu file storage theo nhu cầu.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* **File Storage Max quota:** trong bước khởi tạo file storage, bạn cần đặt một giới hạn quota tối đa cho file storage đó. Quota này có ý nghĩa chính là giới hạn dung lượng lưu trữ mà file storage có thể sử dụng, giúp quản lý tài nguyên hiệu quả. <mark style="color:red;">**Mức quota tối thiểu bạn cần chọn là 1 TB và mức quota tối đa chúng tôi cung cấp là 50 TB.**</mark> Nếu bạn có nhu cấu sử dụng nhiều hơn 50 TB cho một file storage, vui lòng liên hệ với chúng tôi.
* **Network type**: đối với loại file SMB, network type bắt buộc phải là Private. Lúc này, bạn cần chọn **VPC**, **Subnet** mà bạn đã khởi tạo từ vServer Portal.

<figure><img src="../../../../.gitbook/assets/image (904).png" alt=""><figcaption></figcaption></figure>

* **Window Authentication: c**ấu hình quyền truy cập thông qua **Basic Authentication**
  * **Basic Authentication:** Nếu Windows server của bạn không có Active Directory hoặc bạn muốn quản lý quyền truy cập đơn giản thông qua username và password, bạn có thể sử dụng Basic authentication, chúng tôi hỗ trợ bạn tạo tối đa 10 tài khoản username/password để truy cập file storage.

<figure><img src="../../../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

**Bước 5:** Chọn **Create File Storage.**

**Bước 6:** Sau khi hệ thống khởi tạo xong File Storage SMB, bạn có thể lấy thông tin **File Storage IP Address** tại phần thông tin chi tiết của File Storage và tiếp tục thực hiện các bước bên dưới

<figure><img src="../../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

***

## Map File Storage vừa khởi tạo tới Windows server&#x20;

Trên Windows Server, bạn có thể map file storage SMB thông qua giao diện hoặc dòng lệnh.

### **Qua giao diện**

1. **Mở File Explorer.**
2. Nhấp chuột phải vào **This PC** và chọn **Map network drive**.
3. Trong cửa sổ **Map Network Drive**:
   1. **Drive letter**: Chọn một ký tự ổ đĩa (VD: `Z:`).
   2. **Folder**: Nhập đường dẫn SMB share, ví dụ: `\\<File Storage IP Address>\<File Storage Name>`. Ví dụ `\\10.50.3.8\demo-smb`.
   3. Chọn **Finish**, sau khi hoàn tất, bạn có thể kiểm tra trong **File Explorer** để thấy ổ đĩa được map.

<figure><img src="../../../../.gitbook/assets/image (22).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (23).png" alt="" width="501"><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Để tự động map file storage SMB mỗi lần khởi động Windows Server, bạn có thể lưu thông tin khi map qua giao diện bằng cách tích vào ô **Reconnect at sign-in** trước khi nhấn **Finish**.
{% endhint %}

### **Qua dòng lệnh**

Sử dụng lệnh sau trong **Command Prompt** hoặc **PowerShell**:

```cmd
net use Z: \\<File Storage IP Address>\<File Storage Name> 
```

* **Z:**: Là ký tự ổ đĩa mà bạn muốn gắn.
* **\\\\\<File Storage IP Address>\\\<File Storage Name>**: Đường dẫn File Storage SMB.

Ví dụ:

```cmd
net use Z: \\10.50.3.8\demo-smb
```

### Qua trực tiếp File Explorer

Đơn giản hơn, bạn cũng có thể truy cập trực tiếp tới File Storage SMB qua File Explorer qua các bước:

1. Mở **File Explorer**: Nhấn tổ hợp phím **Windows + E** hoặc nhấp vào biểu tượng File Explorer.
2. Nhập **UNC Path**: Trên thanh địa chỉ, nhập đường dẫn UNC đến file share. Ví dụ:

```
\\10.50.3.8\demo-smb
```

3. Nhấn **Enter**.

***

## Write data tới File Storage

Sau khi bạn đã **map File Storage SMB** vào Windows Server thành công, bạn có thể thực hiện việc ghi dữ liệu (write data) tới File Storage như sau:

1. **Mở trình soạn thảo văn bản (Notepad):**
   * Trên Windows Server, mở **Notepad** bằng cách:
     * Nhấn **Start** và gõ **Notepad**, sau đó nhấn **Enter**.
   * Hoặc, nhấn tổ hợp phím **Windows + R**, nhập `notepad` và nhấn **Enter**.
2. **Viết nội dung vào file:**
   *   Trong Notepad, nhập một nội dung đơn giản, ví dụ:

       ```
       Đây là file test ghi vào SMB share.
       ```
   * Hoặc nhập bất kỳ nội dung nào bạn muốn.
3. **Lưu file vào file storage SMB:**
   * Nhấn **File > Save As...**.
   * Trong hộp thoại **Save As**, điều hướng đến ổ đĩa mà bạn đã map SMB share (VD: `Z:`).
   * Đặt tên file (VD: `testfile.txt`).
   * Nhấn **Save** để lưu file.
4. **Kiểm tra file trong SMB share:**
   * Mở **File Explorer** (phím tắt: **Windows + E**).
   * Điều hướng đến ổ đĩa SMB (VD: `Z:`).
   * Tìm và mở file `testfile.txt` mà bạn vừa lưu để xác minh nội dung
