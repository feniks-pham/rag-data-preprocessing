# Khởi tạo và sử dụng Storage Gateway

#### Hướng dẫn khởi tạo storage gateway <a href="#khoitaovasudungstoragegateway-1.taostoragegateway" id="khoitaovasudungstoragegateway-1.taostoragegateway"></a>

1. Truy cập trang chủ VNGCloud tại [đây](https://dashboard.console.vngcloud.vn/). Chọn Service: **vStorage**, sau đó chọn **Storage Gateway**:

<figure><img src="../../../../.gitbook/assets/image (555).png" alt=""><figcaption></figcaption></figure>

2. Tại trang vMarketplace, chọn **Launch on Computer Engine**

<figure><img src="../../../../.gitbook/assets/image (556).png" alt=""><figcaption></figcaption></figure>

3. Bạn nhập thông tin App mong muốn, lựa chọn Instance phù hợp, lựa chọn loại ổ đĩa và kích thước phù hợp, sau đó chọn network, security mong muốn và chọn **Launch Application**

<figure><img src="../../../../.gitbook/assets/image (557).png" alt=""><figcaption></figcaption></figure>

Sau khi bạn Launch Application thành công, hệ thống sẽ thực hiện khởi tạo một server tương ứng. Sau khi VM được tạo thành công, bạn hãy truy cập vào địa chỉ External IP của VM và thực hiện đăng nhập với thông tin đăng nhập đã được gửi về email của bạn (lần đăng nhập đầu tiên sẽ đổi lại password mặc định).

<figure><img src="../../../../.gitbook/assets/image (561).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

Security Groups cần mở thêm các port sau để share được dữ liệu:

* port web: 80,443&#x20;
* port share:
  * port 445,139: nếu sử dụng SMB
  * port 111,2049,34567: nếu sử dụng NFS
{% endhint %}

***

#### Hướng dẫn tạo file share  <a href="#khoitaovasudungstoragegateway-2.taofileshare" id="khoitaovasudungstoragegateway-2.taofileshare"></a>

1. **Tạo credential**

Tại mục **Credential** chọn C**reate credentials:**&#x20;

Trong đó:&#x20;

* Credential name: nhập tên credential mong muốn.
* Region: chọn Region chứa project mà bạn muốn thực hiện lưu trữ trên vStorage.
* Project ID
* Provider: bạn có thể chọn sử dụng S3 key hoặc Swift user tùy chọn.
  * Nếu dùng Swift, bạn cần nhập username và password.
  * Nếu dùng S3 key, bạn cần nhập Access key và Secret key.

Những thông tin này bạn có thể tạo cũng như lấy thông tin trên vStorage Portal và IAM Portal.&#x20;

2. **Tạo file share**

Chọn **file share** rồi chọn C**reate file share**

Trong đó:

* Volume Information:
  * vStorage Credential: chọn credential đã tạo bên trên.
  * Container: chọn một container trong danh sách container trong project đã được khai báo sử dụng.
* Permission:
  * nfs: phân quyền theo IP, chúng tôi sẽ sử dụng IP để phân quyền, bạn cần nhập IP và chọn quyền tương ứng
  * smb: phân quyền theo User, chúng tôi sẽ sử dụng User để phân quyền, bạn cần chọn User và chọn quyền tương ứng

Chọn **Create** và đợi hoàn tất việc tạo File Share. Bạn cũng có thể xem thêm thông tin mount trong mục **Mount**

<figure><img src="../../../../.gitbook/assets/image (562).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (565).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (564).png" alt=""><figcaption></figcaption></figure>

#### 3. Client kết nối và sử dụng file share <a href="#khoitaovasudungstoragegateway-3.clientketnoivasudungfileshare" id="khoitaovasudungstoragegateway-3.clientketnoivasudungfileshare"></a>

**3.1 Client nfs**

Trên máy linux, mở terminal gõ lệnh: _apt install nfs-common_

Trên UI gateway File Share -> Show Commands -> nfs -> copy -> dán lệnh vào terminal client

**3.2 Client smb**

Trên window: Trên UI gateway **File Share -> Show Commands -> smb -> window -> copy -> dán vào search của window -> nhập user/password**

Trên máy linhx, cài dặt client:  _apt install cifs-utils_&#x20;

Trên UI gateway **File Share -> Show Commands -> smb -> window -> copy -> dán vào terminal -> nhập user/password**
