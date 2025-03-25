# Khởi tạo một Public Cluster với Public Node Group

### Điều kiện cần <a href="#khoitaomotpublicclustervoipublicnodegroup-dieukiencan" id="khoitaomotpublicclustervoipublicnodegroup-dieukiencan"></a>

Để có thể khởi tạo một **Cluster** và **Deploy** một **Workload**, bạn cần:

* Có ít nhất 1 **VPC** và 1 **Subnet** đang ở trạng thái **ACTIVE**. Nếu bạn chưa có VPC, Subnet nào, vui lòng khởi tạo VPC, Subnet theo hướng dẫn tại [đây.](../../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)&#x20;
* Có ít nhất 1 **SSH** key đang ở trạng thái **ACTIVE**. Nếu bạn chưa có SSH key nào, vui lòng khởi tạo SSH key theo hướng dẫn tại [đây.](../../../vserver/compute-hcm03-1a/security/ssh-key-bo-khoa.md)
* Đã cài đặt và cấu hình **kubectl** trên thiết bị của bạn. vui lòng tham khảo tại [đây](https://kubernetes.io/vi/docs/tasks/tools/install-kubectl/) nếu bạn chưa rõ cách cài đặt và sử dụng kuberctl. Ngoài ra, bạn không nên sử dụng phiên bản kubectl quá cũ, chúng tôi khuyến cáo bạn nên sử dụng phiên bản kubectl sai lệch không quá một phiên bản với version của cluster.

***

### Khởi tạo Cluster <a href="#khoitaomotpublicclustervoipublicnodegroup-khoitaocluster" id="khoitaomotpublicclustervoipublicnodegroup-khoitaocluster"></a>

**Cluster trong Kubernetes** là một tập hợp gồm một hoặc nhiều máy ảo (VM) được kết nối lại với nhau để chạy các ứng dụng được đóng gói dạng container. Cluster cung cấp một môi trường thống nhất để triển khai, quản lý và vận hành các container trên quy mô lớn.

Để khởi tạo một Cluster, hãy làm theo các bước bên dưới:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console.vngcloud.vn/overview)

**Bước 2:** Tại màn hình **Overview**, chọn **Activate.**

**Bước 3:** Chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn. Sau khi Activate thành công, bạn hãy chọn **Create a Cluster**

**Bước 4:** Tại màn hình khởi tạo Cluster, chúng tôi đã thiết lập thông tin cho Cluster và một **Default Node Group** cho bạn, bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Cluster và Node Group của bạn tại Cluster Configuration, Default Node Group Configuration, Plugin. **Mặc định chúng tôi sẽ khởi tạo cho bạn một Public Cluster với Public Node Group.**

**Bước 5:** Chọn **Create Kubernetes cluster.** Hãy chờ vài phút để chúng tôi khởi tạo Cluster của bạn, trạng thái của Cluster lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Cluster** là **Active**, bạn có thể xem thông tin Cluster, thông tin Node Group bằng cách chọn vào Cluster Name tại cột **Name**.

***

### Kết nối và kiểm tra thông tin Cluster vừa tạo <a href="#khoitaomotpublicclustervoipublicnodegroup-ketnoivakiemtrathongtinclustervuatao" id="khoitaomotpublicclustervoipublicnodegroup-ketnoivakiemtrathongtinclustervuatao"></a>

Sau khi Cluster được khởi tạo thành công, bạn có thể thực hiện kết nối và kiểm tra thông tin Cluster vừa tạo theo các bước:&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/k8s-cluster](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Danh sách Cluster được hiển thị, chọn biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/73761995/image2024-4-4_14-37-11.png?version=1&#x26;modificationDate=1712216232000&#x26;api=v2" alt="" data-size="line"> và chọn **Download Config File** để thực hiện tải xuống file kubeconfig. File này sẽ giúp bạn có toàn quyền truy cập vào Cluster của bạn.

**Bước 3**: Đổi tên file này thành config và lưu nó vào thư mục **\~/.kube/config**

**Bước 4:** Thực hiện kiểm tra Cluster thông qua lệnh:&#x20;

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

### Deploy một Workload <a href="#khoitaomotpublicclustervoipublicnodegroup-deploymotworkload" id="khoitaomotpublicclustervoipublicnodegroup-deploymotworkload"></a>

Sau đây là hướng dẫn để bạn deploy service nginx trên Kubernetes.

**Bước 1**: **Tạo Deployment và Service cho Nginx app**

* Tạo file **nginx-service.yaml** với nội dung sau:

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
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

* Deploy Deployment này bằng lệch:&#x20;

```
kubectl apply -f nginx-service.yaml
```

***

**Bước 2: Kiểm tra thông tin Deployment, Service trước khi expose ra Internet.**

* Chạy câu lệnh sau đây để kiểm tra **Deployment**

```
kubectl get svc,deploy,pod -owide
```

* Nếu kết quả trả về như bên dưới tức là bạn đã deploy service nginx thành công.

```
NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE    SELECTOR
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP   2d4h   <none>
service/nginx-service   ClusterIP   10.96.178.229   <none>        80/TCP    74s    app=nginx

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS   IMAGES         SELECTOR
deployment.apps/nginx-app   1/1     1            1           74s   nginx        nginx:1.19.1   app=nginx

NAME                             READY   STATUS    RESTARTS   AGE   IP              NODE                                            NOMINATED NODE   READINESS GATES
pod/nginx-app-7f45b65946-5pcvz   1/1     Running   0          74s   172.16.24.201   ng-3f06013a-f6a5-47ba-a51f-bc5e9c2b10a7-ecea1   <none>           <none>
```

### **Expose Nginx Service ra Internet**

* Chạy câu lệnh sau đây để expose nginx-service ra internet:

```
kubectl expose deployment nginx-app --type=NodePort --port=30080 --target-port=80
```

* Nếu kết quả trả về như bên dưới tức là bạn đã expose Service ra Internet thành công.

```
NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)           AGE     SELECTOR
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP           2d4h    <none>
service/nginx-app       NodePort    10.96.215.192   <none>        30080:31289/TCP   4s      app=nginx
service/nginx-service   ClusterIP   10.96.178.229   <none>        80/TCP            2m43s   app=nginx

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE     CONTAINERS   IMAGES         SELECTOR
deployment.apps/nginx-app   1/1     1            1           2m43s   nginx        nginx:1.19.1   app=nginx

NAME                             READY   STATUS    RESTARTS   AGE     IP              NODE                                            NOMINATED NODE   READINESS GATES
pod/nginx-app-7f45b65946-5pcvz   1/1     Running   0          2m43s   172.16.24.201   ng-3f06013a-f6a5-47ba-a51f-bc5e9c2b10a7-ecea1   <none>           <none
```

***

**Để truy cập vào app nginx vừa export, bạn có thể sử dụng URL với định dạng:**

```
http://<node_ip>:31289/
```

Trong đó node\_ip có thể là địa chỉ node\_port của bất kỳ node nào trong cluster. Bạn có thể lấy thông tin External IP của Node tại giao diện vServer. Cụ thể truy cập tại [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server).

Ví dụ, bên dưới tôi đã truy cập thành công vào app nginx với địa chỉ : [http://61.28.231.65:31007/](http://61.28.231.65:31007/)

<figure><img src="../../../.gitbook/assets/image (702).png" alt=""><figcaption></figcaption></figure>

Nếu bạn muốn expose service này thông qua vLB Layer4, vLB Layer7, vui lòng tham khảo tại:&#x20;

* [Expose một service thông qua vLB Layer4](../expose-mot-service-thong-qua-vlb-layer4/)
* [Expose một service thông qua vLB Layer7](../expose-mot-service-thong-qua-vlb-layer7.md)
