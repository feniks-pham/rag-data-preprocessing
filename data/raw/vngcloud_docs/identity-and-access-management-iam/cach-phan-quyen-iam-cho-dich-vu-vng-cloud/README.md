# Cách phân quyền IAM cho dịch vụ VNG Cloud

#### 1. Cách IAM hoạt động <a href="#howiamsupportsvngcloudservices-1.cachiamhoatdong" id="howiamsupportsvngcloudservices-1.cachiamhoatdong"></a>

IAM hoạt động bằng cách xác thực danh tính của người dùng và sau đó ủy quyền quyền truy cập dựa trên các Policies liên kết với IAM User Accounts, User Groups và Service Accounts. Khi người dùng gửi yêu cầu truy cập vào tài nguyên cụ thể hoặc thực hiện một hành động, IAM kiểm tra các chính sách liên kết để xác định xem người dùng được phép thực hiện hành động đó hay không.

Nguyên tắc đặc quyền tối thiểu là yếu tố cơ bản trong IAM, đảm bảo rằng người dùng và dịch vụ chỉ có các quyền tối thiểu cần thiết để thực hiện nhiệm vụ của họ, giảm thiểu nguy cơ truy cập trái phép. Tiếp cận tập trung của IAM tối ưu hóa quản lý truy cập, tăng cường bảo mật và giúp các tổ chức tuân thủ các yêu cầu quy định trong môi trường tính toán đám mây.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806582/image2023-5-17_17-31-9.png?version=1&#x26;modificationDate=1689932521000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Model quản lý truy cập này bao gồm năm phần chính:

**1. Principal**

Một thực thể (principal) đề cập đến một đối tượng có thể yêu cầu quyền truy cập vào tài nguyên trong hệ thống VNG Cloud. Thực thể có thể đại diện cho các loại đối tượng khác nhau như User Account, Service Account và IDP (Identity Provider).

* **User Account:** IAM User Account đại diện cho các danh tính riêng lẻ liên kết với Root User Account. Mỗi người dùng có một tập hợp duy nhất các thông tin chứng thực bảo mật như tên người dùng và mật khẩu hoặc khóa truy cập. Người dùng được xác thực để truy cập vào các tài nguyên và dịch vụ đám mây.
* **Service Account:** Service Account là một danh tính bạn có thể tạo trong tài khoản Root User của mình với các quyền cụ thể. Khác với User Account, Service Account là các danh tính được ứng dụng hoặc máy tính sử dụng, không phải là người dùng, để thực hiện các cuộc gọi API được ủy quyền và truy cập vào các tài nguyên cụ thể.
* **IDP:** Identity Provider phép bạn quản lý tài nguyên trên VNG Cloud với tập người dùng trên hệ thống xác thực của doanh nghiệp, giúp doanh nghiệp quản lý tập trung user và không cần phải tạo thêm các IAM User Accounts trên VNG Cloud
* **User Group:** User Group là tập hợp các User Account có yêu cầu truy cập tương tự. Việc nhóm hóa User Account giúp đơn giản hóa quản lý quyền bằng cách cấp quyền cho một nhóm thay vì từng User Account riêng lẻ. Điều này cải thiện tính nhất quán và hiệu quả trong kiểm soát truy cập.

**2. Request**

Khái niệm "**Request**" liên quan đến các yêu cầu hoạt động cụ thể mà một thực thể đang cố gắng thực hiện trên các tài nguyên trong hệ thống. Mỗi request bao gồm các phần chính: "**Actions**" (Hành động), "**Resources**" (Tài nguyên), "**Principal**" (Thực thể) và "**Request Information**" (Thông tin yêu cầu).

* **Actions**: Đây là các hoạt động cụ thể mà thực thể có thể thực hiện trên tài nguyên. Các hành động có thể là tương tác với tài nguyên như đọc, ghi, cập nhật, xóa và nhiều hành động khác.
* **Resources**: Đây là các đối tượng hoặc tài sản bị ảnh hưởng bởi các actions trên. Tài nguyên có thể là các dịch vụ cụ thể như server, load balancer, metric,... hoặc bất kỳ tài sản số nào khác trong hệ thống. Việc định nghĩa tài nguyên xác định phạm vi mà hành động có thể tác động.
* **Principal:** Khi một thực thể khởi tạo một yêu cầu, hệ thống sẽ kiểm tra xem hành động được yêu cầu có được phép hay không dựa trên các **Policies** được liên kết với thực thể đó và tài nguyên. Nếu các **Policies** cho phép, yêu cầu sẽ được thực hiện; nếu không, yêu cầu sẽ bị từ chối. Điều này giúp đảm bảo rằng truy cập đến các tài nguyên được kiểm soát và bảo mật theo cách tối ưu nhất.
* **Request information:** Đây là các thông tin liên quan đến yêu cầu mà thực thể đang thực hiện. Thông tin này có thể bao gồm các thông tin như địa chỉ IP của người yêu cầu, thời gian yêu cầu được gửi và các dữ liệu thêm khác liên quan đến ngữ cảnh của yêu cầu.

**3. Policy**

IAM Policy là các tài liệu JSON xác định các quyền và quy tắc truy cập tài nguyên. Policy được gắn kèm vào các thực thể để kiểm soát hành động mà họ có thể thực hiện trên các tài nguyên cụ thể. Các Policies này tuân thủ nguyên tắc "cho phép" hoặc "từ chối" và quy định các hành động được cho phép hoặc từ chối đối với một thực thể cụ thể.

**4. Authentication**

Authentication (Xác thực) là quá trình xác thực thực thể bằng thông tin đăng nhập của nó để gửi yêu cầu tới VNG Cloud . Thực thể cần cung cấp thông tin xác thực, chẳng hạn như tên đăng nhập và mật khẩu, để chứng minh danh tính của họ. Thông tin xác thực cần cung cấp để xác thực từ phía IAM Console đối với từng đối tượng bao gồm:

* **Root User Account**: Địa chỉ email và mật khẩu
* **IAM User Account**: Tên định danh và mật khẩu
* **Service Account:** Client ID và Secret key
* **IDP:** Đăng nhập thông qua đường dẫn và được cấp quyền truy cập tương tự như một IAM User Account

**5. Authorization**

Sau khi xác thực thành công, hệ thống tiến hành quá trình ủy quyền, hay quyết định xem thực thể có quyền thực hiện hành động đặc biệt nào đó trên tài nguyên cụ thể hay không. Quá trình này đảm bảo rằng chỉ những thực thể được ủy quyền mới có thể thực hiện các hành động trên tài nguyên.

* **Root User Account**: Mặc định có đầy đủ (không giới hạn) quyền truy cập vào tất cả các sản phẩm/dịch vụ và các tài nguyên thuộc các sản phẩm/dịch vụ đó.
* **IAM User Account**: Mặc định không có quyền (từ chối truy cập) trên các tài nguyên thuộc sản phẩm/dịch vụ VNG Cloud. Đối tượng phải được ủy quyền dựa trên tập Policies được gắn kèm để thực hiện hành động cụ thể trên các tài nguyên cụ thể.
* **Service Account:** Tương tự như IAM User Account, Service Account mặc định không có quyền (từ chối truy cập) trên các tài nguyên thuộc sản phẩm/dịch vụ VNG Cloud. Đối tượng phải được ủy quyền dựa trên tập Policies được gắn kèm để thực hiện hành động cụ thể trên các tài nguyên cụ thể.
* **IDP:** Khi thiết lập Identity thành công giữa VNG Cloud (Service Provider) và bên thứ 3 (Identity Providers), đối tượng có thể truy cập vào hệ thống VNG Clound thông qua đường dẫn đăng nhập. Đối tượng truy cập được xem như là các IAM User Account và mặc định không có quyền (từ chối truy cập) trên các tài nguyên thuộc sản phẩm/dịch vụ VNG Cloud. Đối tượng phải được ủy quyền dựa trên tập Policies được gắn kèm để thực hiện hành động cụ thể trên các tài nguyên cụ thể.

#### 2. Các Dịch vụ trong hệ thống VNG Cloud <a href="#howiamsupportsvngcloudservices-2.cacdichvutronghethongvngcloud" id="howiamsupportsvngcloudservices-2.cacdichvutronghethongvngcloud"></a>

Có ba dòng sản phẩm chính trong hệ thống VNG Cloud, hãy điều hướng đến hướng dẫn chi tiết để biết cách áp dụng IAM với các sản phẩm cụ thể:

1. **vServer:** [IAM cho vServer](iam-cho-vserver.md)
2. **vStorage:**[ IAM cho vStorage](iam-cho-vstorage.md)
3. **vMonitor:** [IAM cho vMonitor](iam-cho-vmonitor.md)
