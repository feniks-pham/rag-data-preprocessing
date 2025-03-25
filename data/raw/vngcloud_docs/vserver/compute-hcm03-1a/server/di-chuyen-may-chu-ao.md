# Di chuyển máy chủ ảo

## Di chuyển máy chủ là gì? <a href="#dichuyenmaychuao-dichuyenmaychulagi" id="dichuyenmaychuao-dichuyenmaychulagi"></a>

VNG Cloud cung cấp tự động hóa quá trình di chuyển dữ liệu các máy ảo VM cùng ổ đĩa ảo Volume. Hệ thống sẽ dần dần sao chép máy ảo máy chủ của bạn dưới dạng Image, sau đó sẽ di chuyển địa điểm lưu trữ từ **QTSC** sang **HCM-03-1A**, quá trình này thường bao gồm một hoặc nhiều máy chủ, tùy thuộc vào cấu hình của máy chủ lưu trữ. Thực hiện theo dõi trên giao diện, bạn có thể dễ dàng kiểm tra và cập nhật tình trạng các máy chủ của mình trước khi quyết định triển khai di chuyển chúng.

### **Quy trình di chuyển máy chủ** <a href="#dichuyenmaychuao-quytrinhdichuyenmaychu" id="dichuyenmaychuao-quytrinhdichuyenmaychu"></a>

Bằng cách sử dụng trình quản lý trực quan vServer Portal để quản lý quá trình di chuyển máy chủ, bạn có thể:

1. **Đơn giản hóa quá trình di chuyển bằng việc sao chép dữ liệu gốc.** Bạn có thể bắt đầu di chuyển một nhóm máy chủ bằng cách truy vập vào vServer Portal của chúng tôi tại [{Trang danh sách Server}](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server). Với lần đầu tiên, giao diện sẽ hiển thị danh sách các máy chủ với trạng thái **Ready to migrate,** bạn cần chọn một nhóm máy chủ muốn di chuyển sau đó nhấp vào **Migrate to HCM-03-1A,** tiến trình thực hiện sẽ bắt đầ&#x75;**.** Sau khi quá trình di chuyển bắt đầu, VNG Cloud quản lý tất cả các yếu tố phức tạp của quá trình di chuyển, bao gồm tự động sao chép dữ liệu gốc các máy chủ và tạo Image mới theo định kỳ. Việc bạn cần làm lúc này là theo dõi tiến trình di chuyển và chờ đợi cho đến khi hoàn tất giai đoạn này.
2. **Khởi chạy máy chủ trên HCM-03-1A trong bảng điều khiển:** Sau khi hoàn tất giai đoạn sao chép dữ liệu gốc, trạng thái của máy chủ sẽ chuyển đổi thành **Ready to switch**, với sự hỗ trợ của sao chép tăng dần, VNG Cloud cho phép bạn nhanh chóng khởi chạy máy chủ ảo mà không cần phải chờ đợi giúp giảm thiểu thời gian chết, hạn chế tác động kinh doanh liên quan đến thời gian ngừng hoạt động của ứng dụng trong quá trình chuyển đổi cuối cùng. Lúc này điều bạn cần làm là chọn máy chủ và nhấp vào **Shutdown,** sau đó khi máy chủ đã được tắt, chọn **Switch to HCM-03-1A** để thực hiện khởi động máy chủ trên địa điểm mới.
3. **Kiểm tra tình trạng máy chủ và xác nhận quá trình di chuyển:** Khi bạn đã thực sự di chuyển dữ liệu từ máy chủ này sang máy chủ khác, đã đến lúc thử nghiệm. Việc kiểm tra đầy đủ chức năng và truyền dữ liệu hoàn chỉnh có thể tốn thời gian và rườm rà, nhưng đó là khoảng thời gian hợp lý để tránh phát hiện ra sự cố vào một ngày sau đó. Chọn máy chủ và kiểm tra tình trạng của nó sau khi di chuyển dữ liệu, nếu mọi thứ vẫn hoạt động bình thường và hiệu quả, nhấp vào **Confirm final migration** để hoàn tất tiến trình di chuyển dữ liệu của bạn, lúc này hệ thống sẽ xóa toàn bộ dữ liệu máy chủ ảo ở QTSC, nếu không hãy chọn **Back to QTSC** để hủy bỏ tiến trình di chuyển dữ liệu, mọi thứ sẽ trở về trạng thái ban đầu.

Việc di chuyển dữ liệu có thể gặp một số hạn chế như sau:

* Bạn có thể phải tốn một ít thời gian chờ đợi để tiến trình di chuyển thực hiện hoàn tất.
* Dữ liệu sau khi di chuyển có thể bị thất thoát, mất đồng bộ, nhưng trường hợp này là hiếm khi xảy ra.

### **Quá trình di chuyển máy chủ mất bao lâu?** <a href="#dichuyenmaychuao-quatrinhdichuyenmaychumatbaolau" id="dichuyenmaychuao-quatrinhdichuyenmaychumatbaolau"></a>

Quá trình di chuyển máy chủ điển hình có thể mất từ 2 phút đến 3 giờ, tốc độ trung bình ở mức 200 Mb/s. Điều này là do thời gian dành cho việc di chuyển máy chủ sẽ phụ thuộc rất nhiều vào lượng dữ liệu được truyền, độ lớn của dữ liệu. Máy chủ chỉ có một lượng băng thông nhất định để đáp ứng các tác vụ như thế này. Khi bạn tăng số lượng tệp và ứng dụng được di chuyển, quá trình này sẽ chiếm nhiều băng thông của máy chủ hơn – cuối cùng mất nhiều thời gian hơn để hoàn thành.

### **Chi phí** <a href="#dichuyenmaychuao-chiphi" id="dichuyenmaychuao-chiphi"></a>

Không có phí để sử dụng Dịch vụ di chuyển máy chủ, chúng tôi luôn mong muốn đem đến sự trải nghiệm tuyệt vời nhất cho khách hàng của VNG Cloud.

### **Vì sao nên xem xét di chuyển máy chủ?** <a href="#dichuyenmaychuao-visaonenxemxetdichuyenmaychu" id="dichuyenmaychuao-visaonenxemxetdichuyenmaychu"></a>

Một số tình huống có thể xảy ra có thể khiến việc di chuyển máy chủ trở nên cần thiết:

* Tận dụng lợi thế của công nghệ mới đạt chuẩn Tier 3 và các dịch vụ tốt hơn hoặc đảm bảo rằng hệ điều hành (OS) và phần cứng dựa vào công nghệ mới luôn được cập nhật.
* Di chuyển lên địa điểm mới để tăng tính linh hoạt hoặc khả năng mở rộng.
* Để tiết kiệm và hợp nhất dịch vụ lưu trữ.
* Thay thế cơ sở hạ tầng cũ kỹ vào cuối vòng đời của nó, nâng cao chất lượng phần cứng để đáp ứng chiến lược thay đổi nâng cấp trung tâm dữ liệu trong tương lai của VNG Cloud
* Mở rộng và phân phối hosting giúp giảm tải tại một điểm duy nhất và đạt tính sẵn sàng cao.

\
