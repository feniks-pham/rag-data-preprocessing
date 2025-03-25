# Tải tệp Config Kubernetes Cluster

Khi bạn tải xuống tệp cấu hình (config) của Kubernetes cluster, thực chất là bạn đang tải xuống một tệp chứa thông tin cần thiết để kubectl (công cụ dòng lệnh chính của Kubernetes) có thể kết nối và tương tác với cluster đó.

***

### **Tải tệp Config của Kubernetes Cluster trên giao diện Portal** <a href="#taitepconfigkubernetescluster-taitepconfigcuakubernetesclustertrengiaodienportal" id="taitepconfigkubernetescluster-taitepconfigcuakubernetesclustertrengiaodienportal"></a>

**Quyền tối thiểu**

Để tải tệp config Kubernetes Cluster, bạn phải có quyền chạy hành động sau:\
IAM: GetClusterConfig

1. Mở bảng điều khiển vContainer tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Chỉ định Kubernetes cluster cần xoá và chọn **Hành động - Lấy file config**
3. File config sẽ được lưu về máy, sau đó bạn có thể dùng Kubectl để quản lý trên máy tính cá nhân của mình
