# Làm việc với Application Load Balancer (ALB)

## Tổng quan <a href="#workingwithapplicationloadbalancer-alb-tongquan" id="workingwithapplicationloadbalancer-alb-tongquan"></a>

### ALB là gì? <a href="#workingwithapplicationloadbalancer-alb-alblagi" id="workingwithapplicationloadbalancer-alb-alblagi"></a>

* Application Load Balancer (ALB) là một công cụ trong hạ tầng mạng và máy chủ được sử dụng để phân phối lưu lượng mạng đến nhiều máy chủ hoặc máy ảo để cải thiện hiệu suất và khả năng sẵn sàng của các ứng dụng. ALB hoạt động ở tầng ứng dụng, cho phép phân phối lưu lượng dựa trên nhiều yếu tố như loại yêu cầu, trạng thái của máy chủ và thuật toán phân phối tải. ALB cung cấp khả năng route nâng cao, cho phép điều hướng lưu lượng dựa trên các Host hay Path Header. Nó cũng hỗ trợ tính năng duy trì phiên, giúp duy trì liên tục phiên của người dùng đối với cùng một máy chủ. Điều này rất hữu ích cho các ứng dụng yêu cầu sự nhất quán trong quá trình tương tác của người dùng. Để biết thêm thông tin chi tiết về ALB, vui lòng tham khảo tại \[How it works (ALB)]

### Mô hình triển khai <a href="#workingwithapplicationloadbalancer-alb-mohinhtrienkhai" id="workingwithapplicationloadbalancer-alb-mohinhtrienkhai"></a>

<figure><img src="../../../.gitbook/assets/image%20(6)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt=""><figcaption></figcaption></figure>

**Ngoài các thành phần cơ bản của một cụm K8S và một ALB mà bạn đã biết, trong mô hình này chúng tôi sử dụng:**

* **Ingress**: là tài nguyên trong Kubernetes được cấu hình để cho các Services có thể truy cập được từ bên ngoài k8s cluster thông qua URL, ngoài ra cũng có thể cân bằng tải traffic, hỗ trợ kết nối SSL/TLS và cung cấp virtual hosting dựa theo tên. Một Ingress không expose tùy tiện các protocol ngoài HTTP và HTTPS. **Ingress** đóng vai trò như một điểm vào duy nhất cho các request HTTP và HTTPS từ bên ngoài cluster đến các service bên trong. Việc route traffic được kiểm soát bởi các quy tắc (rule) được định nghĩa trong tài nguyên Ingress (Ingress Yaml File). Một Ingress được quản lý bởi **VNGCloud Ingress Controller:** là một ứng dụng chạy trong cluster và quản lý các tài nguyên Ingress dựa trên Ingress Yaml File do khách hàng định nghĩa
