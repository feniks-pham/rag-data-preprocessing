# Giới hạn và hạn chế ALB

## Giới hạn <a href="#restrictionsandlimitationsalb-gioihan" id="restrictionsandlimitationsalb-gioihan"></a>

Một vài lưu ý về giới hạn của việc ingress an ALB vào một cluster:

* Một cluster có thể có nhiều Ingress, mỗi Ingress có chứa thông tin tài nguyên cho một ALB duy nhất.
* Một ALB có thể được sử dụng chung cho nhiều Ingress. Từ đó một ALB có thể được sử dụng chung cho nhiều cluster nhưng phải đảm bảo các cluster này có chung **VPC**.
* Một ALB có thể bao gồm nhiều listener, nhiều pool, nhiều policy. Các giới hạn về số lượng listener, số lượng pool, số lượng policy vui lòng tham khảo tại \[Hạn mức tài nguyên]

***

## Hạn chế <a href="#restrictionsandlimitationsalb-hanche" id="restrictionsandlimitationsalb-hanche"></a>

* Ingress controller manager cần phải cấu hình các annotation để chỉ định các thuộc tính của ALB, như protocol, port,... Các annotation này có thể khác nhau tùy theo nhà cung cấp dịch vụ đám mây, hiện tại với **VNGCloud LoadBalancer Controller** đang cung cấp danh sách annotation tham khảo tại [cau-hinh-cho-mot-application-load-balancer.md](cau-hinh-cho-mot-application-load-balancer.md "mention"). Chúng tôi sẽ nâng cấp thêm phần này trong các phiên bản release kế tiếp.
* Hiện tại, vLB chưa hỗ trợ tính năng strip path ở Load Balancer Layer 7, chúng tôi sẽ sớm tích hợp tính năng này trong tương lai.
* Việc thay đổi tên hoặc kích thước (Rename, Resize) tài nguyên Load Balancer trên vServer Portal có thể gây ra sự không tương thích với tài nguyên trên Kubernetes Cluster. Điều này có thể dẫn đến việc các tài nguyên không hoạt động trên Cluster, hoặc tài nguyên bị đồng bộ lại hoặc thông tin tài nguyên giữa vServer Portal và Cluster không khớp. Để ngăn chặn vấn đề này, hãy sử dụng `kubectl`để quản lý tài nguyên của Cluster.
