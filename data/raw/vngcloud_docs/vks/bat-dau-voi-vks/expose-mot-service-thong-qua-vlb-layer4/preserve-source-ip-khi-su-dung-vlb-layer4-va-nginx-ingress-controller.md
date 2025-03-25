# Preserve Source IP khi sử dụng vLB Layer4 và Nginx Ingress Controller

**Preserve Source IP** khi sử dụng vLB Layer 4 và Nginx Ingress Controller trong Kubernetes là quá trình duy trì địa chỉ IP gốc của client khi traffic được chuyển tiếp qua load balancer và vào cụm Kubernetes. Điều này rất quan trọng trong một số trường hợp khi bạn cần các thông tin chi tiết về kết nối của client, chẳng hạn như địa chỉ IP gốc và port gốc của client, để có thể thực hiện các quyết định xử lý traffic hoặc logging chính xác. Bên dưới là hướng dẫn cụ thể của chúng tôi để giúp bạn có thể thực hiện usecase này.

***

### Điều kiện cần

* Bạn đã thực hiện khởi tạo Cluster trên hệ thống VKS theo các hướng dẫn tại [đây ](./)và trên cụm của bạn đã được cài đặt **VNGCloud LoadBalancer Controller.**
* Tiếp theo, bạn cần thực hiện cài đặt nginx-ingress-controller theo lệnh:

```
helm install nginx-ingress-controller oci://ghcr.io/nginxinc/charts/nginx-ingress --namespace kube-system
```

***

### **Cấu hình ConfigMap cho Nginx Ingress Controller**

* Thêm vào ConfigMap của Nginx Ingress Controller các thiết lập để kích hoạt proxy protocol thông qua lệnh:

```
kubectl edit cm -n kube-system nginx-ingress-controller
```

* Nếu bạn không sử dụng `cert-manager`, bạn cần thêm đoạn code sau vào tệp tin ConfigMap:

```
data:
  proxy-protocol: "True"
  real-ip-header: proxy_protocol
  real-ip-recursive: "True"
  set-real-ip-from: 0.0.0.0/0
```

* Nếu bạn có sử dụng `cert-manager`, bạn cần thêm đoạn code sau vào tệp tin ConfigMap:

```
data:
  proxy-protocol: "True"
  real-ip-header: proxy_protocol
  real-ip-recursive: "True"
  set-real-ip-from: 0.0.0.0/0
  use-proxy-protocol: "True"
```

***

### Cấu hình vLB Layer 4

* Tiếp theo, bạn cần cấu hình vLB Layer4 cho phép sử dụng proxy protocol cho service Load Balancer Nginx. Giá trị truyền vào là danh sách các service name trong Load Balancer sử dụng Proxy Protocol.

```
kubectl annotate service -n kube-system nginx-ingress-controller-controller \
   vks.vngcloud.vn/enable-proxy-protocol="http,https"
```

* Cuối cùng, bạn hãy thực hiện kiểm tra NLB trên vLB Portal cho tới khi các Load Balancer này được ACTIVE với đầy đủ listener, pool.

***

### Cách sử dụng

* Giả sử, bạn có một service prometheus-node-exporter với port 9100 trong namespace default, bạn có thể apply yaml sau để có thể truy cập thông qua NLB

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test-ingress
  namespace: default
spec:
  ingressClassName: nginx
  rules:
  - host: kkk.example.com
    http:
      paths:
      - backend:
          service:
            name: prometheus-node-exporter
            port:
              number: 9100
        path: /metrics
        pathType: Exact
```

* Sau đó tôi sử dụng IP 103.245.252.75 để curl vào host kkk.example.com như sau:

<figure><img src="../../../.gitbook/assets/image (383).png" alt=""><figcaption></figcaption></figure>

* Kết quả log ghi nhận được đã có thông tin Client IP này như hình:

<figure><img src="../../../.gitbook/assets/image (384).png" alt=""><figcaption></figcaption></figure>
