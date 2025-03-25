# Storage gateway

#### Tổng quan <a href="#storagegateway-tongquan" id="storagegateway-tongquan"></a>

Storage Gateway là dịch vụ cung cấp cổng kết nối giữa hạ tầng vật lý của khách hàng và dịch vụ lưu trữ trên cloud. Storage Gateway hỗ trợ các giao thức lưu trữ tiêu chuẩn như: NFS, SMB, CIFS. Với Storage Gateway của VNG Cloud, khách hàng thay vì phải tự cấu hình với các câu lệnh phức tạp thì có thể làm chỉ thông qua giao diện web portal.

Mô hình triển khai storage gateway&#x20;

<figure><img src="../../../../.gitbook/assets/image (554).png" alt=""><figcaption></figcaption></figure>

* Storage gateway được build trên 1 vServer hoặc trên 1 máy chủ on-premise
* Storage gateway đảm nhận nhiệm vụ làm trung gian giữa người dùng cuối và vStorage cho các tác vụ upload / download. Data nằm trên cache (block disk) giúp enduser truy cập nhanh chóng.&#x20;
* Các dữ liệu sẽ được đồng bộ tự động lên vStorage nhằm cho việc lưu trữ lâu dài tối ưu chi phí.&#x20;
* Dữ liệu từ gateway sẽ được mã hóa trước khi đưa lên vStorage.&#x20;

***

#### Chủ đề <a href="#storagegateway-chude" id="storagegateway-chude"></a>

Từ mô hình triển khai Storage Gateway này, chúng tôi cung cấp các tính năng mà bạn có thể sử dụng bao gồm:

* Khởi tạo và sử dụng Storage Gateway
