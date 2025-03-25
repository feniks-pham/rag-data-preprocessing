# Terraform

### **Terraform là gì?** <a href="#terraform-terraformlagi" id="terraform-terraformlagi"></a>

Terraform là một cơ sở hạ tầng nguồn mở dưới dạng công cụ mã cho phép người dùng quản lý cơ sở hạ tầng của họ một cách dễ dàng và hiệu quả trên các nền tảng đám mây khác nhau, chẳng hạn như VNG Cloud, AWS, Google Cloud và Azure. Máy chủ Terraform đề cập đến phiên bản của công cụ Terraform đang chạy trên một máy chủ hoặc máy cụ thể. Đây là nơi mã cơ sở hạ tầng được viết và thực thi, cho phép người dùng tạo, sửa đổi và hủy tài nguyên trên nền tảng đám mây.

Bản thân Terraform không có giao diện người dùng đồ họa, thay vào đó người dùng tương tác với nó bằng giao diện dòng lệnh. Terraform yêu cầu tài khoản và khóa của nhà cung cấp đám mây được định cấu hình cùng với tệp cấu hình Terraform để thực thi cơ sở hạ tầng dưới dạng mã. Ngoài ra, Terraform có thể hoạt động trong môi trường nhóm nơi nhiều người dùng có thể cộng tác trên cùng một cơ sở mã cơ sở hạ tầng, khiến nó trở thành một công cụ mạnh mẽ và linh hoạt để quản lý cơ sở hạ tầng đám mây.

<figure><img src="../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### **Lợi ích mà Terraform mang lại?** <a href="#terraform-loiichmaterraformmanglai" id="terraform-loiichmaterraformmanglai"></a>

* **Nâng cao tính chính xác, tiết kiệm thời gian thực hiện:** Với việc định nghĩa file mô tả hạ tầng một lần và tái sử dụng lại, Terraform giúp chúng ta tự động hóa việc xây dựng cơ sở hạ tầng. Chúng đảm bảo hạ tầng được xây dựng một cách chính xác loại bỏ những sai lầm có thể xảy khi thực hiện thủ công. Hạ tầng được xây dựng bởi Terraform cũng đảm bảo được tính nhất quán giữa các môi trường do được xây dựng từ cùng một file. Điều này sẽ loại bỏ được những sai lệch giữa các môi trường phát triển, kiểm thử, production. Đảm bảo kết quả quá trình kiểm thử chính xác, đồng nhất giữa các môi trường. Thời gian xây dựng hạ tầng sẽ được rút ngắn do các bước thực hiện thủ công nay đã được thay bằng các câu lệnh tự động. Khi cần xây dựng hạ tầng cho một môi trường mới hay là thay đổi hạ tầng cho tất cả các môi trường có sẵn, ta chỉ cần thực hiện chạy file mô tả với Terraform. Mọi thay đổi sẽ diễn ra như bạn mong muốn, không cần phải tạo lại từ đầu hay sửa đổi hạ tầng ở tất cả môi trường sao cho đồng nhất với nhau.
* **Quản lý phiên bản thay đổi:** Ta có thể theo dõi được quá trình phát triển, thay đổi của hạ tầng bằng cách sử dụng các công cụ theo dõi phiên bản đối với file mô tả hạ tầng. Từ đó ta có thể dễ dàng, nhanh chóng sửa đổi hạ tầng về một phiên bản cũ nếu quá trình thay đổi xảy ra vấn đề.
* **Tài liệu hóa thông tin hạ tầng:** Theo quy trình truyền thống với cách thực hiện quản lý cơ sở hạ tầng thủ công, để hỗ trợ quá trình phát triển, vận hành hệ thống thì chúng ta cần xây dựng tài liệu mô tả thông tin và các bước thực hiện, nhưng khi sử dụng Terraform thì chúng ta không cần xây dựng các tài liệu đó vì các thông tin cần thiết đã được thể hiện trong file mã nguồn HCL được dùng để xây dựng hạ tầng.
* **Hỗ trợ cộng tác, tái sử dụng:** Do cơ sở hạ tầng được quản lý bằng cách sử dụng ngôn ngữ lập trình HCL để mô tả nên các lập trình viên có thể dễ dàng cộng tác, làm việc với nhau để cùng xây dựng. Các lập trình viên cũng có thể tạo ra các module chung để tái sử dụng cho các dự án sau này, giúp cho quá trình xây dựng hạ tầng cho một hệ thống mới trở nên nhanh hơn, đơn giản hơn thay vì phải thực hiện lại mọi thứ từ đầu.
* **Làm việc đồng thời với nhiều Cloud Provider:** Chúng ta có thể sử dụng Terraform để làm việc với nhiều nhà cung cấp dịch vụ tính toán khác nhau như: VNG Cloud, Amazon Web Service, Microsoft Azure, Google Cloud Platform, Kubernetes, VMWare...Việc sử dùng Terraform để làm việc với nhiều dịch vụ khác nhau giúp quản lý đồng thời các tài nguyên trên nhiều nền tảng khác trở nên dễ dàng, tiện lợi hơn.

\


***

#### Chủ đề <a href="#terraform-chude" id="terraform-chude"></a>

* [Cài đặt Terraform](cai-dat-terraform.md)
* [Quản lý vServer với Terraform](quan-ly-vserver-voi-terraform.md)
* [Quản lý vContainer với Terraform](quan-ly-vcontainer-voi-terraform.md)
* [Quản lý vLB với Terraform](quan-ly-vlb-voi-terraform.md)
* [Tài liệu tham chiếu](tai-lieu-tham-chieu.md)

\
