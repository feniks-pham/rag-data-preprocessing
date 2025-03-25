# Giới hạn và hạn chế NLB

## Giới hạn <a href="#restrictionsandlimitationsnlb-gioihan" id="restrictionsandlimitationsnlb-gioihan"></a>

Một vài lưu ý về giới hạn của việc intergrate a NLB vào một cluster:&#x20;

* Một NLB có thể được sử dụng chung cho nhiều cluster nhưng phải đảm bảo các cluster này có chung **VPC**.
* Một NLB có thể bao gồm nhiều listener, nhiều pool, nhiều policy. Các giới hạn về số lượng listener, số lượng pool, số lượng policy vui lòng tham khảo tại [Hạn mức tài nguyên](https://docs.vngcloud.vn/pages/viewpage.action?pageId=59802094).

***

## Hạn chế <a href="#restrictionsandlimitationsnlb-hanche" id="restrictionsandlimitationsnlb-hanche"></a>

* Việc thay đổi tên hoặc kích thước (Rename, Resize) tài nguyên Load Balancer trên vServer Portal có thể gây ra sự không tương thích với tài nguyên trên Kubernetes Cluster. Điều này có thể dẫn đến việc các tài nguyên không hoạt động trên Cluster, hoặc tài nguyên bị đồng bộ lại hoặc thông tin tài nguyên giữa vServer Portal và Cluster không khớp. Để ngăn chặn vấn đề này, hãy sử dụng `kubectl`để quản lý tài nguyên của Cluster.
