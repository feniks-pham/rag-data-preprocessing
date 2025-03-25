# Quản lý truy cập

## Tổng quan

VNG Cloud quan tâm đến việc bảo vệ cơ sở hạ tầng của các dịch vụ VNG Cloud, đặc biệt hơn là các dịch vụ lưu trữ dữ liệu. Trong đó kiểm soát phân quyền truy cập là một trong những ưu tiên hàng đầu, kể cả việc sử dụng phần mềm Veeam để sao lưu dữ liệu.&#x20;

Phân quyền truy cập là yếu tố thiết yếu của bảo mật nhằm xác định đối tượng và điều kiện để truy cập vào phần mềm và thực hiện các thao tác sao lưu hay phục hồi.&#x20;

Bên cạnh việc phân quyền truy cập theo user có thể sử dụng phần mềm, Veeam còn đảm bảo việc bảo mật thực hiện các hành động sao lưu và phục hồi dữ liệu với cơ chế là Four-Eyes Authorization (Xác thực bốn mắt). Bài viết này sẽ mô tả các quyền truy cập của user và xác thực bốn mắt ngay bên dưới.

## Quyền truy cập

Chính sách kiểm soát truy nhập dựa trên quy định của Veeam với các vai trò (roles) khác nhau được thiết kế để quản lý quyền truy cập và quyền hạn của người dùng đối với các tính năng khác nhau của hệ thống. Dưới đây là định nghĩa và sự so sánh các vai trò:

<table><thead><tr><th width="79">STT</th><th width="258">Vai trò (Roles)</th><th>Mô tả</th></tr></thead><tbody><tr><td>1</td><td><strong>Veeam Backup Administrator</strong></td><td>Cho phép thực hiện <strong>tất cả các hoạt động</strong> quản trị trong Veeam Backup &#x26; Replication. Lưu ý rằng vai trò này có quyền truy cập đầy đủ vào tất cả các tệp trên các máy chủ và host được thêm vào cơ sở hạ tầng sao lưu.</td></tr><tr><td>2</td><td><strong>Veeam Restore Operator</strong></td><td><p>Cho phép <strong>thực hiện các thao tác khôi phục</strong> bằng cách sử dụng các bản sao lưu và bản sao hiện có. Tuy nhiên, vai trò này không thể di chuyển một máy ảo VM đã khôi phục vào môi trường sản xuất trong quá trình Instant Recovery.</p><p>Hãy xem xét các điều sau:</p><ul><li>Vai trò này có thể khôi phục dữ liệu từ bất kỳ bản sao lưu nào. Điều này cho phép họ khôi phục các đĩa và tệp có nội dung độc hại được tạo ra một cách đặc biệt. Điều này mở ra cơ hội cho các cuộc tấn công từ bên trong, bao gồm nhưng không giới hạn ở việc leo thang quyền hạn dẫn đến chiếm đoạt toàn bộ hệ thống. Vì khả năng này, vai trò này nên được xem là một vai trò nhạy cảm tương tự như Veeam Backup Administrators.</li><li>Trong quá trình khôi phục, vai trò này có thể ghi đè lên các phiên bản hiện có: máy ảo trong quá trình khôi phục máy ảo, đĩa trong quá trình khôi phục đĩa và tệp trong quá trình khôi phục tệp ở cấp độ tệp.</li></ul></td></tr><tr><td>3</td><td><strong>Veeam Backup Operator</strong></td><td>Có thể thực hiện <strong>bắt đầu và dừng các job</strong> hiện có, xuất bản sao lưu, sao chép bản sao lưu và tạo các bản sao lưu VeeamZip.</td></tr><tr><td>4</td><td><strong>Veeam Backup Viewer</strong></td><td>Chỉ có có quyền <strong>truy cập chỉ-đọc</strong>  (read only) vào Veeam Backup &#x26; Replication. Có thể xem danh sách các job hiện có và xem chi tiết các phiên làm việc của job.</td></tr><tr><td>5</td><td><strong>Veeam Tape Operator</strong></td><td>Có thể <strong>quản lý băng từ</strong> và thực hiện các thao tác sau: quét lại thư viện/máy chủ, đẩy băng từ ra, xuất băng từ, nhập băng từ, đánh dấu băng từ là miễn phí, chuyển băng từ vào pool phương tiện, xóa băng từ, lập danh mục băng từ, kiểm kê băng từ, đặt mật khẩu băng từ, sao chép băng từ, xác minh băng từ, bắt đầu và dừng các job sao lưu băng từ.</td></tr></tbody></table>

{% hint style="info" %}
Bạn có thể **gán nhiều vai trò cho cùng một người dùng**. Ví dụ, nếu người dùng cần có khả năng bắt đầu các job và thực hiện các thao tác khôi phục, bạn có thể gán các vai trò Veeam Backup Operator và Veeam Restore Operator cho người dùng này.
{% endhint %}

Đề phân quyền truy cập và hướng dẫn thêm user, bạn vui lòng tham khảo trên tài liệu chính thức của Veeam sau đây: [https://helpcenter.veeam.com/docs/backup/vsphere/configuring\_users.html?ver=120](https://helpcenter.veeam.com/docs/backup/vsphere/configuring\_users.html?ver=120)

## Four Eyes Authorization

Bạn có thể kích hoạt chức năng này để giảm rủi ro từ các hành động vô tình ảnh hướng đến các dữ liệu lưu trữ nhạy cảm. Chức năng này sử dụng một cơ chế kiểm soát bổ sung yêu cầu sự phê duyệt thêm từ người dùng khác có vai trò Veeam Backup Administrator cho các thao tác cụ thể trong Veeam.

{% hint style="info" %}
Trước khi kích hoạt chức năng này, phải đảm bảo có ít nhất 2 người dùng  với vai trò là Veeam Backup Administrator được chỉ định.
{% endhint %}

Để kích hoạt và cách xét duyệt các thao tác của vai trò Veeam Backup Administrator, bạn vui lòng tham khảo trên tài liệu chính thức của Veeam sau đây : [https://helpcenter.veeam.com/docs/backup/vsphere/four\_eyes\_authorization.html?ver=120](https://helpcenter.veeam.com/docs/backup/vsphere/four\_eyes\_authorization.html?ver=120)
