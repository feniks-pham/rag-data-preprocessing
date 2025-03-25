# Cập nhật Minion security group

Cập nhật lại security group cho cluster là cần thiết để đảm bảo rằng các tài nguyên và dịch vụ trong cluster của bạn đang hoạt động trong môi trường an toàn và bảo mật. Có một số lý do chính để thực hiện việc này:

1. **Thay đổi yêu cầu bảo mật:** Khi yêu cầu bảo mật thay đổi, bạn cần điều chỉnh các security group để đảm bảo rằng chỉ các thiết bị và máy tính được ủy quyền mới có thể truy cập vào các tài nguyên trong cluster.
2. **Chặn truy cập không mong muốn:** Có thể có những thay đổi trong môi trường mạng hoặc các rủi ro bảo mật mới xuất hiện. Bằng cách cập nhật lại security group, bạn có thể chặn truy cập từ các nguồn không mong muốn hoặc đối tượng độc hại.
3. **Tuân thủ chuẩn mạng và quy định an ninh:** Trong một số trường hợp, bạn có thể cần phải điều chỉnh security group để tuân thủ các quy định an ninh hoặc chuẩn mạng mới.
4. **Tối ưu hóa mô hình bảo mật:** Khi hệ thống hoặc ứng dụng của bạn phát triển, bạn có thể muốn tối ưu hóa mô hình bảo mật bằng cách điều chỉnh security group để phản ánh cách mà các thành phần giao tiếp với nhau.
5. **Điều chỉnh theo nhu cầu kinh doanh:** Sự thay đổi trong nhu cầu kinh doanh có thể yêu cầu thay đổi cách mà tài nguyên trong cluster được truy cập và quản lý.

Vì thế, cập nhật lại security group cho cluster là một phần quan trọng của việc duy trì và cải thiện bảo mật của hệ thống và dịch vụ trong môi trường điện toán đám mây.

***

### **Cập nhật Minion security group trên bảng điều khiển vServer** <a href="#capnhatminionsecuritygroup-capnhatminionsecuritygrouptrenbangdieukhienvserver" id="capnhatminionsecuritygroup-capnhatminionsecuritygrouptrenbangdieukhienvserver"></a>

Để cập nhật Minion security group, bạn cần làm theo hướng dẫn sau:

1. Truy cập vào bảng điều khiển vServer của chúng tôi tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Chọn vào xem chi tiết Cluster bằng cách nhấn vào tên của Cluster, sau đó chọn **Cập nhật Minion Security Groups**
3. Màn hình sẽ hiển thị cho phép bạn chọn Security Groups mới cho Cluster của mình, lưu ý rằng bạn chỉ có thể cập nhật lại Master Security Group mà bạn đã tạo cho cluster của mình, Master security group do hệ thống tạo ra không thể được chỉnh sửa\


{% hint style="info" %}
**Lưu ý**

Các quy định trong Security Group do bạn tự tạo có thể sẽ không đảm bảo cấu hình đúng và phù hợp với Kubernetes Cluster, vì thế hãy cân nhắc sử dụng tính năng này.
{% endhint %}



\
