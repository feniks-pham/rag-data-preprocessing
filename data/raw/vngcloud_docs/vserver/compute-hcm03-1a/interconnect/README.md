# Interconnect

### Tổng quan

Dịch vụ VNG Cloud Interconnect là lựa chọn tối ưu để kết nối tới tài nguyên VNG Cloud của bạn một cách trực tiếp và hiệu quả nhất. Khi sử dụng Interconnect, dữ liệu của bạn di chuyển thông qua hệ thống mạng nội bộ của VNG Cloud mà không cần phải sử dụng Internet công cộng. Điều này giúp giảm nguy cơ tắc nghẽn mạng hoặc độ trễ bất ngờ. Khi bạn cần tạo kết nối mới, bạn có thể triển khai một kết nối chuyên dụng từ VNG Cloud. Bên cạnh đó, chúng tôi cho phép bạn truyền dữ liệu giữa các vị trí VNG Cloud Direct Connect để xây dựng một mạng riêng biệt, kết nối linh hoạt giữa các văn phòng và trung tâm dữ liệu trong mạng lưới của bạn.

***

### **Cách thức hoạt động** <a href="#interconnect-cachthuchoatdong" id="interconnect-cachthuchoatdong"></a>

1. **Thiết lập Kết nối Vật lý**:
   * Thiết lập kết nối vật lý cần thiết từ vị trí của tổ chức đến trung tâm dữ liệu của VNG Cloud, kết nối vật lý này thường sử dụng cáp quang hoặc các công nghệ truyền dẫn khác để kết nối trực tiếp từ mạng nội bộ của tổ chức đến trạm Direct Connect của chúng tôi.
2. **Lớp Vật lý**:
   * Tại trạm Direct Connect, có lớp vật lý cung cấp các cơ sở hạ tầng mạng để xử lý và định tuyến dữ liệu từ kết nối vật lý của bạn.
   * Các thiết bị mạng chuyên dụng và hệ thống cáp quang đảm bảo hiệu suất cao và độ tin cậy của kết nối.
3. **Kết nối Logic (VLAN ảo)**:
   * Sau khi dữ liệu đã đi qua lớp vật lý, tổ chức cần thiết lập kết nối logic bằng cách sử dụng các VLAN ảo (Virtual LANs).
   * Các VLAN này được sử dụng để xác định cách kết nối đến các tài nguyên và dịch vụ cụ thể trong cloud.
4. **Truyền dữ liệu qua Kết nối Logic**:
   * Khi kết nối logic đã được thiết lập, dữ liệu có thể truyền qua kết nối này.
   * Dữ liệu đi từ mạng nội bộ của tổ chức, đi qua kết nối vật lý, sau đó đi qua lớp vật lý và cuối cùng đi qua kết nối logic để đến các tài nguyên và dịch vụ VNG Cloud.
5. **Sử dụng Direct Connect cho Truy cập Cloud**:
   * Tổ chức sử dụng Direct Connect để truy cập các tài nguyên và dịch vụ VNG Cloud của nhà cung cấp dịch vụ.
   * Việc này đảm bảo tính bảo mật và hiệu suất cao hơn so với việc sử dụng Internet công cộng.

***

### **Trường hợp sử dụng** <a href="#interconnect-truonghopsudung" id="interconnect-truonghopsudung"></a>

{% tabs %}
{% tab title="Kết nối Văn phòng và Chi nhánh" %}
Tổ chức có nhiều văn phòng hoặc chi nhánh và muốn xây dựng kết nối mạng riêng giữa các địa điểm này sử dụng Interconnect, giúp cải thiện truy cập và giao tiếp giữa các địa điểm khác nhau.
{% endtab %}

{% tab title="Ứng dụng Đòi hỏi Băng thông Lớn" %}
Các ứng dụng yêu cầu băng thông lớn, chẳng hạn như ứng dụng video trực tuyến hoặc dự án khoa học tính toán, thường sử dụng Interconnect để có được băng thông cao và đáng tin cậy hơn so với Internet công cộn&#x67;**.**
{% endtab %}

{% tab title="Thiết lập hệ thống mạng kết hợp" %}
Kết nối mạng VNG Cloud của bạn với các mạng cơ sở để phát triển ứng dụng mở rộng mà không gây tác động đến hiệu suất.
{% endtab %}
{% endtabs %}

