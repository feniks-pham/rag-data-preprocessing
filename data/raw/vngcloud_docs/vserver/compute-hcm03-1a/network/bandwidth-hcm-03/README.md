# Băng thông (Bandwidth)

### Tổng quan

**Bandwidth** (băng thông) là lượng dữ liệu được truyền đến và đi từ máy chủ ảo của bạn trong một khoảng thời gian nhất định, thường là một tháng. Băng thông thường được đo bằng các đơn vị như kilobit trên giây (kbps), megabit trên giây (Mbps), gigabit trên giây (Gbps), v.v. Bên cạnh đó, băng thông cũng đóng vai trò quan trọng trong việc tăng tốc độ truy cập dữ liệu, cải thiện hiệu suất của các ứng dụng,...

Với VNG Cloud, chúng tôi hiện tại cung cấp 4 gói băng thông cho khách hàng có thể dễ dàng lựa chọn bao gồm:&#x20;

* **VNG Dedicated**: Gói băng thông miễn phí mặc định với tốc độ tiêu chuẩn dành cho tất cả khách hàng. Ở gói này, chúng tôi sẽ cung cấp cho bạn băng thông trong nước lên tới 300Mbps và băng thông quốc tế lên tới 5Mbps. **Gói này phù hợp cho những khách hàng có nhu cầu ổn định và không thay đổi nhiều theo thời gian. Đây là lựa chọn tốt cho các doanh nghiệp muốn tránh những chi phí không lường trước được và cần một mức giá cố định.**
* **Pay As You Go:** Gói băng thông mà bạn cần chi trả tiền cho lượng băng thông sử dụng vượt quá gói băng thông miễn phí (VNG Dedicated). **Điều này có thể hợp lý hơn cho các doanh nghiệp có nhu cầu sử dụng biến động, cần sự linh hoạt và khả năng mở rộng nhanh chóng mà không muốn bị giới hạn bởi mức băng thông cố định.** Gói Pay As You Go này sẽ bao gồm 3 gói cụ thể:
  * **PAYG-ALL**: Gói này cho phép bạn sử dụng băng thông không giới hạn cho cả lưu lượng trong nước và quốc tế. Bạn sẽ trả tiền cho tổng lượng băng thông sử dụng vượt quá mức miễn phí, bất kể lưu lượng đó là trong nước hay quốc tế. **Gói này sẽ phù hợp với các doanh nghiệp hoặc cá nhân có nhu cầu sử dụng băng thông lớn và đa dạng, bao gồm cả trong nước và quốc tế.**
  * **PAYG-DOMESTIC**: Gói này sẽ áp dụng cho băng thông sử dụng trong nước. Bạn sẽ trả tiền cho lượng băng thông sử dụng vượt quá mức miễn phí dành riêng cho lưu lượng **nội địa**. Tại gói này, lưu lượng **quốc tế sẽ theo cấu hình gói mặc định. Gói này sẽ phù hợp với các doanh nghiệp hoặc cá nhân chủ yếu hoạt động trong nước và có nhu cầu sử dụng băng thông nội địa lớn.**
  * **PAYG-INTERNATIONAL**: Gói này sẽ áp dụng cho băng thông sử dụng quốc tế. Bạn sẽ trả tiền cho lượng băng thông sử dụng vượt quá mức miễn phí dành riêng cho lưu lượng quốc tế. Tại gói này, lưu lượng **trong nước sẽ theo cấu hình gói mặc định. Gói này sẽ phù hợp với các doanh nghiệp hoặc cá nhân có nhu cầu sử dụng băng thông quốc tế cao, nhưng băng thông nội địa ít.**
* **Share**: Gói băng thông với tốc độ cao được chia sẻ cho nhiều khách hàng cùng sử dụng. Tốc độ của gói này có thể khác nhau tại các thời điểm trong ngày. **Gói này phù hợp cho các doanh nghiệp nhỏ hoặc các dự án không yêu cầu băng thông lớn và ổn định liên tục**. Nếu bạn chỉ cần băng thông để duy trì các hoạt động cơ bản và không có yêu cầu cao về hiệu suất mạng, đây là lựa chọn hợp lý nhất cho bạn.

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Dedicated**: Gói băng thông với tốc độ tùy chọn của riêng bạn. Với gói này, chúng tôi cam kết và đảm bảo chất lượng dịch vụ cho khách hàng với dung lượng theo yêu cầu. **Gói này phù hợp cho các doanh nghiệp hoặc dự án cần băng thông lớn và ổn định, ví dụ như các trang web có lượng truy cập cao, các ứng dụng đòi hỏi kết nối mạng nhanh và liên tục, hoặc các dịch vụ trực tuyến cần đảm bảo chất lượng trải nghiệm người dùng.**

<figure><img src="../../../../.gitbook/assets/image (22) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Các gói băng thông loại **VNG Dedicated, Pay As You Go, và Share** được chúng tôi tự động tạo và thêm sẵn vào gói dịch vụ cho bạn. Các gói này được đánh dấu bởi nhãn **System** trên giao diện.
* Gói băng thông **VNG Dedicated** được lựa chọn làm gói mặc định cho tất cả IP (IP trên tất cả các resource của bạn trên hệ thống **vServer**). Gói này được đánh dấu bởi nhãn **Default** trên giao diện.
* Kể từ thời điểm bạn tạo một resource mới, khoảng sau 1 phút thì các địa chỉ IP này sẽ tự động được gán vào gói băng thông **VNG Dedicated.** Bạn có thể Thêm IP này vào các gói băng thông khác tùy theo nhu cầu hoặc bạn có thể tùy chỉnh và tạo các gói băng thông theo mong muốn trong gói **Dedicated**.
{% endhint %}

