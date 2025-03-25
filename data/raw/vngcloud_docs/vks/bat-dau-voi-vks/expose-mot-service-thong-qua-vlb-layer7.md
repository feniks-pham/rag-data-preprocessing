# Expose một service thông qua vLB Layer7

### Điều kiện cần <a href="#exposemotservicethongquavlblayer7-dieukiencan" id="exposemotservicethongquavlblayer7-dieukiencan"></a>

Để có thể khởi tạo một **Cluster** và **Deploy** một **Workload**, bạn cần:

* Có ít nhất 1 **VPC** và 1 **Subnet** đang ở trạng thái **ACTIVE**. Nếu bạn chưa có VPC, Subnet nào, vui lòng khởi tạo VPC, Subnet theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)
* Có ít nhất 1 **SSH** key đang ở trạng thái **ACTIVE**. Nếu bạn chưa có SSH key nào, vui lòng khởi tạo SSH key theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)
* Đã cài đặt và cấu hình **kubectl** trên thiết bị của bạn. vui lòng tham khảo tại [đây](https://kubernetes.io/vi/docs/tasks/tools/install-kubectl/) nếu bạn chưa rõ cách cài đặt và sử dụng kuberctl. Ngoài ra, bạn không nên sử dụng phiên bản kubectl quá cũ, chúng tôi khuyến cáo bạn nên sử dụng phiên bản kubectl sai lệch không quá một phiên bản với version của cluster.

***

### Khởi tạo Cluster <a href="#exposemotservicethongquavlblayer7-khoitaocluster" id="exposemotservicethongquavlblayer7-khoitaocluster"></a>

**Cluster trong Kubernetes** là một tập hợp gồm một hoặc nhiều máy ảo (VM) được kết nối lại với nhau để chạy các ứng dụng được đóng gói dạng container. Cluster cung cấp một môi trường thống nhất để triển khai, quản lý và vận hành các container trên quy mô lớn.

Để khởi tạo một Cluster, hãy làm theo các bước bên dưới:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn **Activate.**

**Bước 3:** Chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn. Sau khi Activate thành công, bạn hãy chọn **Create a Cluster**

**Bước 4:** Tại màn hình khởi tạo Cluster, chúng tôi đã thiết lập thông tin cho Cluster và một **Default Node Group** cho bạn, bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Cluster và Node Group của bạn tại Cluster Configuration, Default Node Group Configuration, Plugin. **Khi bạn chọn bật option**![](https://docs-admin.vngcloud.vn/download/thumbnails/73762059/image2024-4-16_14-18-22.png?version=1\&modificationDate=1713252320000\&api=v2) **, mặc định chúng tôi sẽ cài sẵn plugin này vào Cluster của bạn.**

**Bước 5:** Chọn **Create Kubernetes cluster.** Hãy chờ vài phút để chúng tôi khởi tạo Cluster của bạn, trạng thái của Cluster lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Cluster** là **Active**, bạn có thể xem thông tin Cluster, thông tin Node Group bằng cách chọn vào Cluster Name tại cột **Name**.

***

### Kết nối và kiểm tra thông tin Cluster vừa tạo <a href="#exposemotservicethongquavlblayer7-ketnoivakiemtrathongtinclustervuatao" id="exposemotservicethongquavlblayer7-ketnoivakiemtrathongtinclustervuatao"></a>

Sau khi Cluster được khởi tạo thành công, bạn có thể thực hiện kết nối và kiểm tra thông tin Cluster vừa tạo theo các bước:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/k8s-cluster](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Danh sách Cluster được hiển thị, chọn biểu tượng ![](https://docs-admin.vngcloud.vn/download/thumbnails/73762059/image2024-4-4_14-37-11.png?version=1\&modificationDate=1712222544000\&api=v2) và chọn **Download Config File** để thực hiện tải xuống file kubeconfig. File này sẽ giúp bạn có toàn quyền truy cập vào Cluster của bạn.

**Bước 3**: Đổi tên file này thành config và lưu nó vào thư mục **\~/.kube/config**

**Bước 4:** Thực hiện kiểm tra Cluster thông qua lệnh:

* Chạy câu lệnh sau đây để kiểm tra **node**

```
kubectl get nodes
```

* Nếu kết quả trả về như bên dưới tức là bạn Cluster của bạn được khởi tạo thành công với 3 node như bên dưới.

```
NAME                                            STATUS     ROLES    AGE   VERSION
ng-0e10592c-e70e-404d-a4e8-5e3b80f805e4-834b7   Ready      <none>   50m   v1.28.8
ng-0e10592c-e70e-404d-a4e8-5e3b80f805e4-cf652   Ready      <none>   23m   v1.28.8
ng-0f4ed631-1252-49f7-8dfc-386fa0b2d29b-a8ef0   Ready      <none>   28m   v1.28.8
```

***

### Khởi tạo Service Account và cài đặt VNGCloud LoadBalancer Controller <a href="#exposemotservicethongquavlblayer7-khoitaoserviceaccountvacaidatvngcloudingresscontroller" id="exposemotservicethongquavlblayer7-khoitaoserviceaccountvacaidatvngcloudingresscontroller"></a>

{% hint style="info" %}
Chú ý:

Khi bạn thực hiện khởi tạo Cluster theo hướng dẫn bên trên, nếu bạn chưa bật option **Enable vLB Native Integration Driver**, mặc định chúng tôi sẽ không cài sẵn plugin này vào Cluster của bạn. Bạn cần tự thực hiện Khởi tạo Service Account và cài đặt **VNGCloud LoadBalancer Controller** theo hướng dẫn bên dưới. Nếu bạn đã bật option **Enable vLB Native Integration Driver**, thì chúng tôi đã cài sẵn plugin này vào Cluster của bạn, hãy bỏ qua bước Khởi tạo Service Account, cài đặt **VNGCloud LoadBalancer Controller** và tiếp tục thực hiện theo hướng dẫn kể từ Deploy một Workload.
{% endhint %}

<details>

<summary>Khởi tạo Service Account và cài đặt VNGCloud LoadBalancer Controller</summary>

**Khởi tạo Service Account**

* Khởi tạo hoặc sử dụng một **service account** đã tạo trên IAM và gắn policy: **vLBFullAccess**, **vServerFullAccess**. Để tạo service account bạn truy cập tại [đây](https://hcm-3.console.vngcloud.vn/iam/service-accounts) và thực hiện theo các bước sau:
  * Chọn "**Create a Service Account**", điền tên cho Service Account và nhấn **Next Step** để gắn quyền cho Service Account
  * Tìm và chọn **Policy:** **vLBFullAccess và Policy:** **vServerFullAccess**, sau đó nhấn "**Create a Service Account**" để tạo Service Account, Policy: vLBFullAccess vàPolicy: vServerFullAccess do VNG Cloud tạo ra, bạn không thể xóa các policy này.
  * Sau khi tạo thành công bạn cần phải lưu lại **Client\_ID** và **Secret\_Key** của Service Account để thực hiện bước tiếp theo.

**Cài đặt VNGCloud LoadBalancer Controller**

* Cài đặt Helm phiên bản từ 3.0 trở lên. Tham khảo tại [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/) để biết cách cài đặt.
* Thay thế thông tin ClientID, Client Secret và ClusterID của cụm K8S của bạn và tiếp tục chạy:

```bash
helm install vngcloud-load-balancer-controller oci://vcr.vngcloud.vn/81-vks-public/vks-helm-charts/vngcloud-load-balancer-controller \
  --namespace kube-system \
  --set mysecret.global.clientID= __________________ \
  --set mysecret.global.clientSecret= __________________
```

* Sau khi việc cài đặt hoàn tất, thực hiện kiểm tra trạng thái của pods:

```bash
kubectl get pods -n kube-system | grep vngcloud-ingress-controller
```

Ví dụ như ảnh bên dưới là bạn đã cài đặt thành công pods:

```bash
NAME                                      READY   STATUS    RESTARTS   AGE
vngcloud-ingress-controller-0             1/1     Running   0          12s
```

</details>

***

### Deploy một Workload <a href="#exposemotservicethongquavlblayer7-deploymotworkload" id="exposemotservicethongquavlblayer7-deploymotworkload"></a>

Sau đây là hướng dẫn để bạn deploy service nginx trên Kubernetes.

**Bước 1**: **Tạo Deployment cho Nginx app.**

* Tạo file **nginx-service-lb7.yaml** với nội dung sau:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-app
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.19.1
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx 
  type: NodePort 
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

* Deploy Deployment này bằng lệch:

```
kubectl apply -f nginx-service-lb7.yaml
```

***

**Bước 2: Kiểm tra thông tin Deployment, Service vừa deploy**

* Chạy câu lệnh sau đây để kiểm tra **Deployment**

```
kubectl get svc,deploy,pod -owide
```

* Nếu kết quả trả về như bên dưới tức là bạn đã deploy Deployment thành công.

```
NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE     SELECTOR
service/kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP        5h4m    <none>
service/nginx-service   NodePort    10.96.25.133   <none>        80:32572/TCP   2m50s   app=nginx

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE     CONTAINERS   IMAGES         SELECTOR
deployment.apps/nginx-app   1/1     1            1           2m50s   nginx        nginx:1.19.1   app=nginx

NAME                             READY   STATUS    RESTARTS   AGE     IP            NODE                                            NOMINATED NODE   READINESS GATES
pod/nginx-app-7f45b65946-6wlgw   1/1     Running   0          2m49s   172.16.54.3   ng-e0fc7245-0c6e-4336-abcc-31a70eeed71d-972a9   <none>           <none>
```

***

### **Tạo Ingress Resource**

* Tạo file **nginx-ingress.yaml** với nội dung sau:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  ingressClassName: "vngcloud"
  defaultBackend:
    service:
      name: nginx-service
      port:
        number: 80
  rules:
    - http:
        paths:
          - path: /path1
            pathType: Exact
            backend:
              service:
                name: nginx-service
                port:
                  number: 80               
```

* Chạy câu lệnh sau đây để triển khai Ingress

```
kubectl apply -f nginx-ingress.yaml
```

Lúc này, hệ thống vLB sẽ tự động tạo một LB tương ứng với Ingress resource bên trên, ví dụ:

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Chú ý:

* Hiện tại Ingress chỉ hỗ trợ duy nhất TLS port 443 và là điểm kết thúc cho TLS (TLS termination). TLS Secret phải chứa các trường với tên key là tls.crt và tls.key, đây chính là certificate và private key để sử dụng cho TLS. Nếu bạn muốn sử dụng Certificate cho một host, hãy thực hiện tải lên Certificate theo hướng dẫn tại \[Upload a certificate] và sử dụng chúng như một annotation. Ví dụ:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    # kubernetes.io/ingress.class: "vngcloud" # this annotation is deprecated will cause warning, can use option `ingressClassName` below instead.
    vks.vngcloud.vn/load-balancer-id: "lb-6cdea8fd-4589-410e-933f-c3bc46fa9d25"
    vks.vngcloud.vn/certificate-ids: "secret-a6d20ec6-f3e5-499a-981b-b1484e340cec"
spec:
  ingressClassName: "vngcloud"
  defaultBackend:
    service:
      name: apache-service
      port:
        number: 80
  tls:
    - hosts:
        - host.example.com
  rules:
    - host: host.example.com
      http:
        paths:
          - path: /path1
            pathType: Exact
            backend:
              service:
                name: nginx-service
                port:
                  number: 80
```
{% endhint %}

***

**Để truy cập vào app nginx, bạn có thể sử dụng Endpoint của Load Balancer mà hệ thống đã tạo.**

```
http://Endpoint/
```

Bạn có thể lấy thông tin Public Endpoint của Load Balancer tại giao diện vLB. Cụ thể truy cập tại

Ví dụ, bên dưới tôi đã truy cập thành công vào app nginx với địa chỉ : [http://180.93.181.129/](http://180.93.181.129/)

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Bạn có thể xem thêm về ALB tại [Working with Application Load Balancer (ALB](../network/lam-viec-voi-application-load-balancer-alb/)).

{% hint style="info" %}
**Chú ý:**

* Việc thay đổi tên hoặc kích thước (Rename, Resize) tài nguyên Load Balancer trên vServer Portal có thể gây ra sự không tương thích với tài nguyên trên Kubernetes Cluster. Điều này có thể dẫn đến việc các tài nguyên không hoạt động trên Cluster, hoặc tài nguyên bị đồng bộ lại hoặc thông tin tài nguyên giữa vServer Portal và Cluster không khớp. Để ngăn chặn vấn đề này, hãy sử dụng `kubectl`để quản lý tài nguyên của Cluster.
{% endhint %}
