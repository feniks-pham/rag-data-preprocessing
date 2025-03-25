# Bật Auto Healing cho Cluster

Auto Healing Clusters là một kiến trúc cluster được thiết kế để tự động phục hồi khi các thành phần trong cụm gặp sự cố hoặc lỗi. Mục tiêu chính của Auto Healing Clusters là đảm bảo rằng các dịch vụ và ứng dụng triển khai trên cụm luôn hoạt động một cách liên tục và ổn định, ngay cả khi xảy ra sự cố với các node hoặc các thành phần khác trong cụm.

Các đặc điểm và lợi ích của Auto Healing Clusters bao gồm:

1. **Tự động phục hồi:** Các Auto Healing Clusters có khả năng tự động phát hiện các sự cố và lỗi, và tự động thực hiện các hành động để khắc phục vấn đề. Nếu một node hoặc một máy chủ gặp sự cố, cụm sẽ tự động chuyển các dịch vụ và ứng dụng đến các node khác để đảm bảo tiếp tục hoạt động của hệ thống.
2. **Tăng tính sẵn sàng và độ tin cậy:** Auto Healing Clusters giảm nguy cơ mất dữ liệu và gián đoạn dịch vụ bằng cách triển khai các bản sao dự phòng của ứng dụng hoặc dịch vụ trên các node khác nhau trong cụm. Nếu một node gặp sự cố, các bản sao dự phòng vẫn sẽ tiếp tục phục vụ yêu cầu của người dùng.
3. **Tối ưu hóa hiệu suất và khả năng mở rộng:** Auto Healing Clusters có thể tự động mở rộng tài nguyên khi có nhu cầu, ví dụ như khi tải công việc cao hơn hoặc có yêu cầu phục vụ lớn. Điều này giúp đảm bảo rằng hệ thống luôn hoạt động ở mức hiệu suất tốt nhất và đáp ứng nhu cầu sử dụng của người dùng.
4. **Quản lý và khắc phục lỗi nhanh chóng:** Tự động phục hồi giúp giảm thiểu thời gian gián đoạn và tác động tiêu cực đối với dịch vụ và người dùng khi xảy ra sự cố. Nó tự động xử lý các vấn đề và giúp hệ thống nhanh chóng trở lại trạng thái hoạt động ổn định.
5. **Tự động mở rộng và giảm quy mô:** Auto Healing Clusters có khả năng tự động mở rộng hoặc giảm quy mô tài nguyên khi tải công việc thay đổi. Điều này giúp tối ưu hóa việc sử dụng tài nguyên và đảm bảo rằng các ứng dụng không bị kẹt trong trạng thái chờ xử lý.

Vì thế, Auto Healing Clusters là một phương tiện quan trọng để đảm bảo tính sẵn sàng, độ tin cậy và hiệu suất cao cho các ứng dụng và dịch vụ trong môi trường điện toán đám mây và hệ thống phân tán. Nó tự động phục hồi và tối ưu hóa cụm để đảm bảo hoạt động liên tục và ổn định của hệ thống.

***

### **Bật Auto Healing** <a href="#batautohealingchocluster-batautohealing" id="batautohealingchocluster-batautohealing"></a>

Để bật Auto Healing cho Kubernetes Cluster của bạn vui lòng chọn **Bật Auto Healing** ở mục **Tùy chọn nâng cao** tại màn hình tạo mới Kubernetes Cluster, bạn có thể xem quy trình khởi tạo Kubernetes Cluster tại [Bước 2: Khởi tạo dịch vụ K8S](../bat-dau-voi-kubernetes-cluster/buoc-2-khoi-tao-dich-vu-k8s.md)
