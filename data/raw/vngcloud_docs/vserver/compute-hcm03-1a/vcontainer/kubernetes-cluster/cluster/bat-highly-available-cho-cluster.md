# Bật Highly Available cho Cluster

Highly Available Clusters (HAC) là một kiến trúc cluster được thiết kế để đảm bảo tính sẵn sàng và độ tin cậy cao, đặc biệt là trong môi trường điện toán đám mây và hệ thống phân tán. Mục tiêu chính của Highly Available Clusters là đảm bảo rằng dịch vụ hoặc ứng dụng được triển khai trên cụm có sẵn để sử dụng liên tục mà không bị gián đoạn, ngay cả khi xảy ra sự cố với một số thành phần trong cụm.

Các đặc điểm và lợi ích của Highly Available Clusters bao gồm:

1. **Tính sẵn sàng cao:** Highly Available Clusters cung cấp khả năng duy trì hoạt động của ứng dụng và dịch vụ ngay cả khi một hoặc nhiều thành phần trong cụm gặp sự cố. Nếu một node hoặc một máy chủ bị hỏng, các dịch vụ vẫn tiếp tục hoạt động trên các thành phần còn lại trong cụm.
2. **Tăng tính tin cậy:** HAC giảm nguy cơ mất dữ liệu và gián đoạn dịch vụ bằng cách triển khai các bản sao dự phòng của ứng dụng hoặc dịch vụ trên các node khác nhau trong cụm. Điều này đảm bảo rằng nếu một node gặp sự cố, các bản sao dự phòng vẫn có thể phục vụ yêu cầu của người dùng.
3. **Tối ưu hóa hiệu suất:** HAC cho phép phân phối công việc và tải tỷ lệ cân đối trên nhiều node trong cụm. Khi nhu cầu tăng cao, cụm có thể tự động mở rộng để đáp ứng tải công việc cao hơn và đảm bảo hiệu suất tốt nhất.
4. **Tự động phục hồi:** Các Highly Available Clusters thường có tích hợp chức năng tự động phục hồi, cho phép cụm tự động phát hiện và xử lý các lỗi, chuyển đổi dự phòng và tái khởi động các thành phần khi cần thiết.
5. **Quản lý và khắc phục lỗi nhanh chóng:** Kiến trúc HAC giúp dễ dàng phát hiện và khắc phục các sự cố, giúp giảm thiểu thời gian gián đoạn và sự không ổn định của dịch vụ.

Các công nghệ và phương pháp phổ biến để tạo Highly Available Clusters bao gồm sử dụng Load Balancer, Redundancy (dự phòng), Replication (nhân bản), Quorum (đa số quyết định) và kỹ thuật tự động mở rộng tài nguyên khi có nhu cầu. Điều này đảm bảo rằng một dịch vụ hoặc ứng dụng được duy trì với tính sẵn sàng và độ tin cậy cao, giúp tăng cường trải nghiệm của người dùng và hạn chế tác động tiêu cực khi xảy ra sự cố.

***

### **Bật Highly Available trên bảng điều khiển** <a href="#bathighlyavailablechocluster-bathighlyavailabletrenbangdieukhien" id="bathighlyavailablechocluster-bathighlyavailabletrenbangdieukhien"></a>

Để bật Highly Available cho Kubernetes Cluster của bạn vui lòng chọn **Bật HA** ở mục **Tùy chọn nâng cao** tại màn hình tạo mới Kubernetes Cluster, bạn có thể xem quy trình khởi tạo Kubernetes Cluster tại [Bước 2: Khởi tạo dịch vụ K8S](../bat-dau-voi-kubernetes-cluster/buoc-2-khoi-tao-dich-vu-k8s.md)
