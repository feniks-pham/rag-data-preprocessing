# Quản lý Node Group

Dịch vụ Kubernetes Cluster của VNG Cloud cung cấp tính năng Node Group. Khi bạn tiến hành tạo mới Kubernetes Cluster, hệ thống sẽ tự động sinh ra Node Group Default để quản lý các Node trong Cluster. Mỗi Node Group quản lý các Node là một phần của Auto Scaling. Vì thế hiệu lực của Auto Scaling tác động lên các tài khoản không loại trừ các Node trong Node Group.

Việc sử dụng Node group giúp dễ dàng quản lý các nhóm node trong cụm Kubernetes, giúp bạn tối ưu hóa tài nguyên và quản lý linh hoạt hơn các phần khác nhau của ứng dụng của bạn.

Bạn có thể tạo một hoặc nhiều Node Group để quản lý các Node trong Cluster bằng trình điều khiển hoặc cơ sở hạ tầng dưới dạng công cụ mã như API, Terraform được cung cấp bởi VNG Cloud . Mỗi node group có thể có cấu hình tùy chỉnh về loại máy chủ, số lượng node khác nhau. Các Node Group được quản lý bởi VNG Cloud vì thế, bạn có thể tạo, tự động cập nhật hoặc xoá các Node cho Cluster của mình chỉ bằng một thao tác. Các Node được khởi chạy như một phần của Node Group và được quản lý tự động được gắn thẻ để được phát hiện bởi trình tự động chia tỷ lệ Autoscale của Kubernetes Cluster. Bạn có thể quản lý riêng biệt các nhóm và gắn tên riêng biệt để xác định chức năng của chúng và cập nhật bất cứ lúc nào.

Bạn không phải trả thêm phí khi sử dụng các Node Group được quản lý bởi VNG Cloud, bạn chỉ phải trả phí cho các tài nguyên Kubernetes Cluster khởi tạo. Chúng bao gồm các cấu hình Master Node, Minion Node, ổ đĩa, số giờ hoạt động của Kubernetes Cluster và bất kỳ cơ sở hạ tầng VNG Cloud nào khác. Có yêu cầu phí tối thiểu đối với tài khoản trả trước và tính toán lại vào cuối tháng.

Để bắt đầu với Kubernetes Cluster mới và Node Group được quản lý, hãy xem [Bắt đầu với Kubernetes – Bảng điều khiển quản lý vServer.](../bat-dau-voi-kubernetes-cluster/)

Để thêm một Node Group được quản lý vào một Cluster hiện có, hãy xem [Tạo Node Group](tao-node-group.md).

VNG Cloud tuân theo mô hình chia sẻ trách nhiệm đối với các bản vá bảo mật trên các Node Group được quản lý. Khi các Node được quản lý chạy và được tối ưu hóa của VNG Cloud, chúng tôi chịu trách nhiệm xây dựng các phiên bản Image đã vá lỗi khi có lỗi hoặc sự cố được báo cáo. Chúng tôi có thể xuất bản một sửa chữa. Tuy nhiên, bạn chịu trách nhiệm triển khai các phiên bản Image đã vá lỗi này cho các Node Group được quản lý của mình. Khi các nút được quản lý chạy My Image tùy chỉnh, bạn chịu trách nhiệm xây dựng các phiên bản Image đã vá lỗi khi có lỗi hoặc sự cố được báo cáo, sau đó triển khai My Image.&#x20;

***

### **Quản lý Node Group trên bảng điều khiển vServer** <a href="#quanlynodegroup-quanlynodegrouptrenbangdieukhienvserver" id="quanlynodegroup-quanlynodegrouptrenbangdieukhienvserver"></a>

**Quyền tối thiểu**

Để xem thông tin Node Group, bạn phải có quyền IAM chạy các hành động sau:

* List Clusters
* List Cluster Node Groups

Bạn có thể xem thông tin Node Group Default và Node Group được tạo bởi người dùng bằng cách làm theo hướng dẫn sau:

1. Truy cập vào bảng điều khiển Kubernetes Cluster tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Chỉ định một Cluster và vào tên để xem trang chi tiết
3. Tại đây bạn có thể xem các Node Group tại Tab Node Group của mục Detail Information
