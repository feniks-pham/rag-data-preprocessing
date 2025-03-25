# Placement Group

Affinity group là một chính sách khởi tạo vị khí tài nguyên cho một nhóm các máy chủ ảo, nhằm đảm bảo các nhu cầu về hiệu năng cao cũng như tính sẵn sàng.

### **Chính sách của Placement Group** <a href="#servergroup-chinhsachcuaservergroup" id="servergroup-chinhsachcuaservergroup"></a>

Hiện tại, VNG Cloud cung cấp 2 loại chính sách dành cho Placement Group để quản lý tốt hơn về phân bổ máy chủ ảo và host vật lý: Soft anti-affinity và soft affinity

* Soft Anti-affinity: Cấp phát các máy chủ ảo trong Placement group trên các host vậy lý khác nhau một cách tối đa. Nếu không còn host vật lý đủ để đảm bảo chính sách thì máy chủ ảo sẽ được cấp phát ngẫu nhiên trên các host
* Soft Affinity: Cấp phát các máy chủ ảo trong Placement group trên cùng một host vật lý một cách tối đa. Nếu không có host vật lý nào còn đủ resource để tuân thủ chính sách thì máy chủ ảo sẽ được cấp phát ngẫu nhiên trên các host

### **Các ngữ cảnh** <a href="#servergroup-cacngucanh" id="servergroup-cacngucanh"></a>

Một số trường hợp thực tế sử dụng chính sách soft anti-affinity và soft affinity:

* Soft Anti-affinity group: Bạn muốn cài đặt các máy chủ ảo có các vai trò khác nhau trên nhiều host vật lý khác nhau nhằm đảm bảo hiệu năng tối đa, không bị tranh chấp tài nguyên nếu chạy chung host vật lý
  * Ví dụ như khi bạn triển khai hệ thống Hadoop, bạn sẽ gặp khó khăn trong việc tính toán chính xác số lượng máy chủ ảo để đảm nhiệm tất cả các vai trò khác nhau của hệ thống này như NameNode, DataNode, JobTracker và TaskTracker. Với chính sách anti-affinity, bạn có thể xây dựng Hadoop cluster trên nhiều host vật lý khác nhau
* Soft affinity group: Bạn muốn xây dựng các VM instance chạy trên cùng, để đảm bảo độ trễ ít nhất và bandwidth tốt nhất
  * Ví dụ khi bạn tạo 2 VM instances chạy web server nginx và redis caching, và yêu cầu hai phiên bản VM này phải định vị trong cùng một máy chủ để có kết nối nhanh hơn giữa chúng

### **Thao tác với Placement Group** <a href="#servergroup-thaotacvoiservergroup" id="servergroup-thaotacvoiservergroup"></a>

Bạn có thể tạo placement group với chính sách affinity và anti-affinity:

1. Đi đến trang VNG Cloud console, navigate to Placement Group page
2. Bạn có thể tạo thêm Placement Group và lựa chọn chính sách affinity hoặc anti-affinity phù hợp. Placement group sau khi tạo xong sẽ không thể thay đổi thuộc tính chính sách này.
3. Bạn có thể tạo máy chủ ảo và lựa chọn Placement Group có sẵn theo nhu cầu.
