# Xoá Kubernetes Cluster

Khi sử dụng xong Kubernetes Cluster, bạn nên xóa các tài nguyên được liên kết với cụm đó để không phải chịu bất kỳ chi phí không cần thiết nào. Tuy nhiên khi xoá Kubernetes Cluster các tài nguyên sau sẽ bị xóa:

* Tất cả các node có trong Cluster
* Bất kỳ Pod nào đang chạy trên các node instance đó
* Dữ liệu được lưu trữ trong ổ đĩa máy chủ

Hệ thống có thể không xóa các tài nguyên sau:

* Bộ cân bằng tải bên ngoài được đính kèm với Kubernetes Cluster
* Bộ cân bằng tải bên trong được đính kèm với Kubernetes Cluster
* Persistent volume

***

### **Xoá Kubernetes Cluster trên giao diện vServer** <a href="#xoakubernetescluster-xoakubernetesclustertrengiaodienvserver" id="xoakubernetescluster-xoakubernetesclustertrengiaodienvserver"></a>

**Quyền tối thiểu**

Để xóa Kubernetes Cluster, bạn phải có quyền chạy hành động sau:\
IAM: DeleteCluster

1. Mở bảng điều khiển vContainer tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Chỉ định Kubernetes cluster cần xoá và chọn **Action**
3. Chọn **Xoá** và xác nhận thao tác

\
