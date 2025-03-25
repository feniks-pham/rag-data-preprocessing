# Security for IAM

#### Tổng quan <a href="#securityforiam-tongquan" id="securityforiam-tongquan"></a>

User, Group, Service Account, Policy là các tài nguyên định nghĩa trên IAM Portal. Mỗi khách hàng sẽ có thể khởi tạo và duy trì tại một thời điểm nhiều tài nguyên dùng trong kế hoạch phân chia tài nguyên trong doanh nghiệp, cũng như phân cấp của doanh nghiệp.

Bảo mật trên hệ thống Quản lý Nhận dạng và Truy cập (Identity and Access Management - IAM) là một vấn đề quan trọng đối với các doanh nghiệp và tổ chức. IAM là một giải pháp giúp quản lý và bảo vệ danh tính, quyền truy cập và tài nguyên của người dùng trên các hệ thống, ứng dụng và dịch vụ. IAM cung cấp các chức năng như xác thực, ủy quyền, phân quyền, kiểm soát truy cập, đồng bộ hóa danh tính, quản lý danh tính,...

Các tiêu chuẩn bảo mật được áp dụng trên IAM bao gồm:&#x20;

* Nguyên tắc nhất quán: đảm bảo rằng các chính sách và quy trình IAM được áp dụng nhất quán trên toàn bộ hệ thống.
* Nguyên tắc cần thiết: chỉ cấp cho người dùng những quyền truy cập cần thiết cho công việc của họ, không nhiều hơn, không ít hơn.
* Nguyên tắc tối thiểu: giới hạn số lượng người dùng có quyền truy cập cao nhất hoặc đặc biệt trên hệ thống.
* Nguyên tắc phân tách nhiệm vụ: ngăn chặn việc một người dùng có thể thực hiện các hoạt động có thể gây ra xung đột lợi ích hoặc rủi ro bảo mật.
* Nguyên tắc kiểm tra và xem xét: theo dõi và kiểm tra các hoạt động truy cập của người dùng, đánh giá hiệu quả của các biện pháp IAM và cập nhật khi cần thiết.

Bằng cách tuân thủ các nguyên tắc và tiêu chuẩn bảo mật trên, các doanh nghiệp và tổ chức có thể nâng cao an toàn thông tin trên hệ thống IAM, bảo vệ danh tính và tài nguyên của người dùng, giảm thiểu rủi ro xâm nhập và vi phạm bảo mật, tăng cường uy tín và niềm tin của khách hàng và đối tác.

Để bảo vệ thông tin của khách hàng và dữ liệu mà khách hàng sử dụng trên dịch vụ IAM, hiện tại VNG Cloud đang áp dụng các biện pháp kiểm soát bảo mật như:

* **Bảo mật quyền hạn truy cập:** VNG Cloud sử dụng chính IAM để quản lý quyền truy cập của người dùng vào các tài nguyên IAM. IAM cho phép các doanh nghiệp tạo và quản lý các chính sách truy cập cho từng tài nguyên IAM. Điều này giúp đảm bảo rằng chỉ những người có quyền truy cập cần thiết mới có thể truy cập vào các tài nguyên
* **Bảo mật dữ liệu trên đường truyền:** VNG Cloud sử dụng HTTPS để mã hóa dữ liệu trên đường truyền. HTTPS là một giao thức bảo mật dựa trên HTTP, sử dụng mã hóa TLS/SSL để bảo vệ dữ liệu trong quá trình truyền.
* **Bảo mật các thông tin nhạy cảm trên IAM:** VNG Cloud sẽ chịu trách nhiệm mã hóa các thông tin nhạy cảm tại máy chủ lưu trữ của mình. Dữ liệu sẽ được mã hóa bằng một key do VNG Cloud cung cấp.

VNG Cloud luôn nỗ lực để nâng cao các biện pháp bảo mật của mình để đảm bảo an toàn cho khách hàng.

\
