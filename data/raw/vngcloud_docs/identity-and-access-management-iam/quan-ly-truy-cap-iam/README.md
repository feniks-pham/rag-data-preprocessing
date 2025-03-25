# Quản lý Truy cập IAM

Quản lý Truy cập IAM cho phép bạn kiểm soát người có thể truy cập các nguồn tài nguyên đám mây của bạn và các hành động họ có thể thực hiện trên các tài nguyên đó. IAM Policies là các tài liệu JSON xác định các quyền và quy tắc truy cập tài nguyên cho các định danh IAM (IAM User Account, User Group và Service Account). Hướng dẫn này sẽ hướng dẫn bạn tạo và quản lý IAM Policies để kiểm soát truy cập vào tài nguyên của bạn một cách hiệu quả.

#### Khái niệm và Thuật ngữ <a href="#iamaccessmanagement-khainiemvathuatngu" id="iamaccessmanagement-khainiemvathuatngu"></a>

* **Permission và Policy:** Quyền xác định các hành động cụ thể mà một thân nhận được phép thực hiện trên tài nguyên. Chính sách là các tập hợp quyền được biểu thị dưới dạng tài liệu JSON. Những chính sách này được gắn kết với các tài khoản người dùng IAM, nhóm và tài khoản dịch vụ để cấp hoặc từ chối quyền truy cập vào các tài nguyên khác nhau. Mỗi chính sách chứa các khai báo xác định các hành động được phép hoặc từ chối, tài nguyên và các điều kiện tùy chọn.
* **Access control:** Kiểm soát truy cập là việc thực hiện các quyền dựa trên chính sách. Khi một thân nhận khởi tạo một yêu cầu thực hiện một hành động, hệ thống sẽ kiểm tra các chính sách liên quan để xác định xem hành động được yêu cầu có được phép hay không. Nếu các chính sách cấp quyền cho các quyền cần thiết, hành động sẽ được ủy quyền; nếu không, nó sẽ bị từ chối.
* **Resource-Based Authorization:** Trong IAM, ủy quyền thường liên quan đến tài nguyên, có nghĩa là quyền được định nghĩa liên quan đến các tài nguyên cụ thể. Các tài nguyên này có thể là dịch vụ cụ thể, thùng, cơ sở dữ liệu, tệp hoặc bất kỳ tài sản số nào khác trong hệ thống. Ủy quyền dựa trên tài nguyên đảm bảo rằng các thân nhận chỉ có thể truy cập tài nguyên mà họ đã được cấp quyền một cách rõ ràng.
* **Granular Control:** IAM cung cấp kiểm soát chi tiết về việc ủy quyền. Người quản trị có thể xác định các Permission và Policy cụ thể, không chỉ loại hành động mà thực thể có thể thực hiện mà còn các điều kiện mà hành động đó được phép thực hiện trong trường hợp cụ thể.
* **Dynamic Authorization:** Các Permissions và Policies có thể được điều chỉnh linh hoạt để thích ứng với các yêu cầu và tình huống thay đổi. Điều này cho phép người quản trị dễ dàng cấp hoặc thu hồi quyền truy cập khi cần, mà không cần sự can thiệp thủ công phức tạp.
* **Least Privilege Principle:** Nguyên tắc đặc quyền tối thiểu là một khái niệm cơ bản trong ủy quyền IAM. Nó khẳng định rằng các thực thể chỉ nên được cấp quyền tối thiểu cần thiết để thực hiện các hành động của họ. Điều này giảm thiểu tác động tiềm năng của các vi phạm bảo mật và giới hạn việc tiết lộ tài nguyên nhạy cảm.

#### Hiểu về IAM Policy <a href="#iamaccessmanagement-hieuveiampolicy" id="iamaccessmanagement-hieuveiampolicy"></a>

Mỗi chính sách bao gồm một hoặc nhiều câu lệnh, và mỗi câu lệnh chứa các phần tử "Effect" (Cho phép hoặc Từ chối), "Action" (Các hành động trên Resource), "Resource" (Các tài nguyên VNG Cloud) và các phần tử "Condition" tùy chọn.

**Product/Service**

Việc chỉ định Product/Service khi khởi tạo một Policy là bắt buộc, giúp bạn giới hạn tập quyền lên một nhóm Resources thuộc một Prodcut/Service nhất định, giúp việc vận hành hoạt động một cách mượt mà và an toàn.

Các sản phẩm/service thuộc VNG Cloud như: vServer, vStorage, vMonitor, vLB, vConsole, IAM,...

**Action**

Tại mục Action, bạn có thể chỉ định các hành động (**được cấp phép** hoặc **từ chối truy cập**) trên các tài nguyên được áp dụng:

* Để **cấp phép truy cập** các Action trên Resource, chọn **Allow Permission**

![](https://docs.vngcloud.vn/download/attachments/59806592/image2023-8-3\_9-40-43.png?version=1\&modificationDate=1691030444000\&api=v2)

* Để **từ chối truy cập** các Action trên Resource, chọn **Deny Permission**

![](https://docs.vngcloud.vn/download/attachments/59806592/image2023-8-3\_9-41-42.png?version=1\&modificationDate=1691030503000\&api=v2)

**Có ba loại cấp độ truy cập, bao gồm:**

* **List:** Cấp độ này liệt kê tất cả các quyền liên quan đến xem danh sách tài nguyên thuộc Product đã chọn. Bạn có thể chọn **Tất cả / các hành động cụ thể**.
* **Write**: Cấp độ này liệt kê tất cả các quyền liên quan đến các hành động thay đổi tài nguyên thuộc Product đã chọn, chẳng hạn như Tạo, Cập nhật, Tải lên, Gia hạn và các hành động khác. Bạn có thể chọn tất cả / các hành động cụ thể ở cấp độ này.
* **Read**: Cấp độ này liệt kê tất cả các quyền liên quan đến xem thông tin chi tiết của tài nguyên thuộc Product đã chọn. Bạn có thể chọn tất cả / các hành động cụ thể ở cấp độ này.

**Resource**

Có một số cách linh hoạt để bạn chỉ định các tài nguyên được áp dụng các Action (được cấp phép hoặc từ chối truy cập), bao gồm:

* Tất cả các tài nguyên
* Các tài nguyên cụ thể: Đối với mỗi loại tài nguyên thuộc Product đã chọn, bạn có thể chọn tất cả / các tài nguyên cụ thể (dựa trên ID tài nguyên) thuộc loại đó.

**Request conditions**

Các Request conditions trong Policy là các điều kiện tùy chọn mà bạn có thể đặt để quy định Policy đó sẽ áp dụng như thế nào cho trên các đối tượng (IAM User Account, Service Account, Group). Có nhiều loại điều kiện bạn có thể cài đặt để áp dụng lên Policy của mình, và điều chỉnh thời gian áp dụng chính sách là một trong số đó. Điều này cho phép bạn điều chỉnh khi nào chính sách sẽ có hiệu lực và khi nào nó sẽ bị hủy bỏ đối với một hoặc nhiều hành động cụ thể mà người dùng hoặc dịch vụ đang thực hiện.

Ví dụ, bạn có thể sử dụng Request conditions để quy định rằng một chính sách chỉ sẽ áp dụng vào các ngày cụ thể hoặc chỉ trong khoảng thời gian nhất định. Điều này có thể hữu ích trong việc quản lý quyền truy cập dựa trên thời gian, ngày lễ, sự kiện đặc biệt hoặc các tình huống cụ thể khác mà bạn muốn kiểm soát.

**Rules**

Một chính sách (Policies) sẽ bao gồm nhiều Rule. Mỗi Rule sẽ bao gồm đầy đủ các thành phần như Product, Action, Resource và Request conditions. Việc có nhiều Rule trong một Policy giúp bạn áp dụng các tập quyền hạn khác nhau, lên từng tập resource khác nhau.

#### Phân loại Chính Sách (Policy) <a href="#iamaccessmanagement-phanloaichinhsach-policy" id="iamaccessmanagement-phanloaichinhsach-policy"></a>

Tại VNG Cloud Service, chúng tôi hỗ trợ 2 loại Chính Sách (Policy), bao gồm:

* **VNG Managed Policy:** Là các Chính Sách IAM (IAM Policy) được tạo mặc định bởi hệ thống IAM VNG Cloud. Các Chính Sách này được quản lý bởi chính VNG Cloud nhằm mục đích hỗ trợ người dùng trong việc cài đặt nhanh chóng các quyền truy cập cần thiết cho các tài khoản người dùng IAM đối với các tài nguyên của từng Product cụ thể
* **Customer Policy:** Là các Chính Sách IAM (IAM Policy) được tạo bởi Root user (hoặc IAM user nếu có quyền). Các Chính Sách này được quản lý trực tiếp bởi người dùng và có thể điều chỉnh bất cứ lúc nào tùy thuộc vào nhu cầu sử dụng.
* Tìm hiểu thêm và 2 loại Policy tại đây:
  * [VNG Managed Policy](https://docs.vngcloud.vn/display/ONVINA/VNG+Cloud+Manage+Policies)
  * [Customer Managed Policy](https://docs.vngcloud.vn/display/ONVINA/Customer+Managed+Policies)
