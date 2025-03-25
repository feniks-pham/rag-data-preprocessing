# Sử dụng Deny permission để từ chối truy cập

Khi có nhu cầu phân quyền truy cập cho phép tất cả action chỉ trừ một vài action cụ thể, bạn cần tạo Policy và sử dụng Deny Permission để đơn giản hoá trong việc phân quyền . Ở hướng dẫn này chúng tôi sẽ hướng dẫn bạn **phân quyền cho phép User: System1 được thực hiện tất cả action của vServer (Full Access), nhưng không cho phép thực hiện action:Delete trên Resource:server**, **để đảm bảo User: System1 không xoá bất kì servers nào**. Mô hình sẽ như bên dưới:

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/iam-deny-permission.drawio%20(2).png?version=1&#x26;modificationDate=1689158267000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Để thiết lập IAM theo mô hình trên chúng ta sẽ có các bước như sau:

**Bước 1**: Tạo User: System1 nếu chưa có User Account (lưu ý rằng nếu đã có sẵn User: System1, cần đảo bảo User: System1 không có quyền gì hoặc không có các quyền chồng lấn với hướng dẫn)

**Bước 2**: Tạo Policy với tên vServerFullAccessExceptDeleteServer cho phép truy cập toàn bộ Resource của vServer, nhưng không cho phép Delete Server&#x20;

**Bước 3**: Gắn Policy: vServerFullAccessExceptDeleteServer cho User: System1

**Bước 4**: Đăng nhập và kiểm tra quyền của User: System1

Chi tiết các bước như sau

**Bước 1: Tạo User: System1 nếu chưa có User Account (lưu ý rằng nếu đã có sẵn User: System1, cần đảo bảo User: System1 không có quyền gì hoặc không có các quyền chồng lấn với hướng dẫn)**

Tiến hành tạo User Account bằng cách truy cập vào tab User Account ở trang quản lý IAM tại [đây](https://hcm-3.console.vngcloud.vn/iam/user-accounts), nhấn **Create a User Account,** điền thông tin Username và Password, sau đó nhấn **Create User Account**&#x20;

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_15-18-33.png?version=1&#x26;modificationDate=1689158368000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Sau khi tạo thành công User Account, sẽ được liệt kê ở trang User Account như bên dưới

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_15-19-37.png?version=1&#x26;modificationDate=1689158368000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


**Bước 2: Tạo Policy với tên vServerFullAccessExceptDeleteServer cho phép truy cập toàn bộ Resource của vServer, nhưng không cho phép Delete Server**&#x20;

Để tạo Policy bạn qua tab Policy ở trang IAM tại [đây](https://hcm-3.console.vngcloud.vn/iam/policies), nhấn **Create a Policy**, **đặt tên** cho Policy: **vServerFullAccessExceptDeleteServer** và nhấn **Next step**

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-40-24.png?version=1&#x26;modificationDate=1689158425000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Nhấn chọn JSON để chuyển sang chế độ JSON và tạo Policy với đoạn JSON có sẵn

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-45-7.png?version=1&#x26;modificationDate=1689158708000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Sử dụng đoạn JSON dưới đây và sao chép vào Policy

| `{  "statements": [    {      "effect": "allow",      "actions": [        "vserver:*"      ],      "resources": [        "*"      ],      "condition": {}    },    {      "effect": "deny",      "actions": [        "vserver:DeleteServer"      ],      "resources": [        "*"      ],      "condition": {}    }  ]}` |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Nhấn **Create policy** để tạo Policy

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-48-53.png?version=1&#x26;modificationDate=1689158934000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Bước 3**: Gắn Policy: vServerFullAccessExceptDeleteServer cho User: System1

Sau khi tạo thành công Policy: vServerFullAccessExceptDeleteServer, bạn tiến hành gắn Policy này cho User: System1, bạn có thể thực hiện ở User Account hoặc Policy, ở đây chúng tôi sẽ hướng dẫn ở Policy, **nhấn vào tên của Policy** để vào trang chi tiết Policy:

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-50-46.png?version=1&#x26;modificationDate=1689159047000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Chọn tab Policy usage** và **nhấn Attach** để thêm User: System1

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-51-59.png?version=1&#x26;modificationDate=1689159120000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Chọn User: System1** và **nhấn Add**

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-52-32.png?version=1&#x26;modificationDate=1689159153000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Sau khi thêm User: System1 vào Policy: vServerFullAccessExceptDeleteServer, bạn sẽ thấy thông tin như bên dưới

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-53-7.png?version=1&#x26;modificationDate=1689159188000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Bước 4**: Đăng nhập và kiểm tra quyền của User: System1

Lúc này bạn có thể đăng nhập vào User: System1 để kiểm tra quyền

Truy cập vào vServer tại [đây](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server), khi chưa đăng nhập bất kì tài khoản nào bạn sẽ được chuyển hướng sang trang sign-in chọn "**Sign-in With IAM User Account**"

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_13-48-49.png?version=1&#x26;modificationDate=1689158370000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Điền thông tin root user account email mà User: System1 trước đó đã được tạo, thông tin IAM username và password của User: System1, nhấn **Sign-in with IAM User Account**

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_15-56-13.png?version=1&#x26;modificationDate=1689158370000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Lúc này bạn sẽ thấy User: System1 sẽ có toàn quyền trên vServer nhưng không thể xoá được bất kì Resource: server nào

Truy cập trang chi tiết của web1-server thành công

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_15-58-35.png?version=1&#x26;modificationDate=1689158370000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Thực hiện tắt server web1-server thành công:

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_15-59-35.png?version=1&#x26;modificationDate=1689158370000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Nhưng không thể xoá server web1-server

\


<figure><img src="https://docs.vngcloud.vn/download/attachments/59805245/image2023-7-12_17-55-8.png?version=1&#x26;modificationDate=1689159309000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


Như vậy là bạn đã hoàn thành việc phân quyền cho phép User: System1 được thực hiện tất cả action của vServer (Full Access), nhưng không cho phép thực hiện action:Delete trên Resource:server, để đảm bảo User: System1 không xoá bất kì servers nào.

\
