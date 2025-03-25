# Bật Auto Scaling cho Cluster

Auto Scaling cho Cluster là một tính năng trong hệ thống quản lý cụm (cluster management) như Kubernetes, Docker Swarm, hoặc các dịch vụ điện toán đám mây, cho phép tự động điều chỉnh số lượng các node hoặc các tài nguyên trong cụm dựa trên tải công việc và yêu cầu của ứng dụng.

Tính năng Auto Scaling giúp đáp ứng một số vấn đề quan trọng trong việc quản lý cụm:

1. **Tối ưu hóa hiệu suất:** Auto Scaling cho phép cụm tự động mở rộng tài nguyên khi có nhu cầu. Khi tải công việc cao hơn, cụm sẽ tự động tạo thêm các node hoặc tài nguyên để đảm bảo các ứng dụng hoạt động với hiệu suất tốt nhất.
2. **Tiết kiệm chi phí:** Auto Scaling cho phép cụm tự động giảm quy mô tài nguyên khi không cần thiết. Nếu tải công việc giảm đi, cụm sẽ tự động thu hồi các tài nguyên không sử dụng để tiết kiệm chi phí.
3. **Đảm bảo tính sẵn sàng:** Auto Scaling giúp đảm bảo rằng cụm có sẵn để đáp ứng nhu cầu sử dụng và tránh tình trạng quá tải hoặc thiếu tài nguyên.
4. **Tự động phục hồi:** Auto Scaling giúp tự động phục hồi từ các sự cố hoặc lỗi bằng cách tạo ra các node mới để thay thế các node bị hỏng.
5. **Tích hợp với khái niệm về Infrastructure as Code (IaC):** Auto Scaling thường được tích hợp với các công cụ IaC như Terraform hoặc CloudFormation để định nghĩa và quản lý cơ sở hạ tầng của cụm dưới dạng mã, giúp tự động hóa việc triển khai và mở rộng tài nguyên.

Khi triển khai các ứng dụng trong môi trường cloud hoặc hệ thống phân tán, sử dụng tính năng Auto Scaling cho Cluster giúp tối ưu hóa sử dụng tài nguyên, cải thiện tính sẵn sàng và hiệu suất của ứng dụng, và giúp quản lý cụm trở nên dễ dàng và hiệu quả hơn.

\


***

### **Bật Auto Scaling trên giao diện Portal** <a href="#batautoscalingchocluster-batautoscalingtrengiaodienportal" id="batautoscalingchocluster-batautoscalingtrengiaodienportal"></a>

Để bật Auto Scaling cho Kubernetes Cluster của bạn vui lòng chọn Bật Auto Scaling ở mục Tùy chọn nâng cao tại màn hình tạo mới Kubernetes Cluster, bạn có thể xem quy trình khởi tạo Kubernetes Cluster tại [Bước 2: Khởi tạo dịch vụ K8S](../bat-dau-voi-kubernetes-cluster/buoc-2-khoi-tao-dich-vu-k8s.md)
