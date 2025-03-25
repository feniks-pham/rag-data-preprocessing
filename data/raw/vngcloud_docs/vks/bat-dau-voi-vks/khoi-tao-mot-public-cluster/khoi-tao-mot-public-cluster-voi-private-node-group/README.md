# Khởi tạo một Public Cluster với Private Node Group

### Điều kiện cần <a href="#khoitaomotpublicclustervoiprivatenodegroup-dieukiencan" id="khoitaomotpublicclustervoiprivatenodegroup-dieukiencan"></a>

Để có thể khởi tạo một **Cluster** và **Deploy** một **Workload**, bạn cần:

* Có ít nhất 1 **VPC** và 1 **Subnet** đang ở trạng thái **ACTIVE**. Nếu bạn chưa có VPC, Subnet nào, vui lòng khởi tạo VPC, Subnet theo hướng dẫn tại [đây.](../../../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)&#x20;
* Có ít nhất 1 **SSH** key đang ở trạng thái **ACTIVE**. Nếu bạn chưa có SSH key nào, vui lòng khởi tạo SSH key theo hướng dẫn tại [đây.](../../../../vserver/compute-hcm03-1a/security/ssh-key-bo-khoa.md)
* Đã cài đặt và cấu hình **kubectl** trên thiết bị của bạn. vui lòng tham khảo tại [đây](https://kubernetes.io/vi/docs/tasks/tools/install-kubectl/) nếu bạn chưa rõ cách cài đặt và sử dụng kuberctl. Ngoài ra, bạn không nên sử dụng phiên bản kubectl quá cũ, chúng tôi khuyến cáo bạn nên sử dụng phiên bản kubectl sai lệch không quá một phiên bản với version của cluster.

{% hint style="info" %}
<mark style="color:red;">**Chú ý:**</mark>&#x20;

* <mark style="color:red;">**Để đảm bảo các VM trong các NodeGroup trên subnet có thể đi outbound ra internet và kết nối được tới Control Plane thì bạn bắt buộc phải thiết lập NAT Gateway. Cụ thể tham khảo thêm tại mục bên dưới.**</mark>
{% endhint %}

***

### Khởi tạo Palo Alto hoặc Pfsense thay thế cho NAT Gateway <a href="#khoitaomotpublicclustervoiprivatenodegroup-khoitaopfsense" id="khoitaomotpublicclustervoiprivatenodegroup-khoitaopfsense"></a>

{% hint style="info" %}
**Chú ý:**

* Để được hỗ trợ tốt nhất khi sử dụng Palo Alto hoặc Pfsense, vui lòng liên hệ với đội ngũ chuyên viên của chúng tôi qua Hotline <mark style="color:green;">**1900 1549**</mark> hoặc email <mark style="color:green;">**support@vngcloud.vn**</mark><mark style="color:green;">.</mark>
{% endhint %}

Hoặc bạn có thể chọn sử dụng Palo Alto hoặc Pfsense để làm việc với Private Node Group theo hướng dẫn tại:

* [Palo Alto as a NAT Gateway](palo-alto-as-a-nat-gateway.md)
* [Pfsense as a NAT Gateway](pfsense-as-a-nat-gateway.md)

***

### Khởi tạo Route Table <a href="#khoitaomotpublicclustervoiprivatenodegroup-khoitaoroutetable" id="khoitaomotpublicclustervoiprivatenodegroup-khoitaoroutetable"></a>

Sau khi Palo Alto, Pfsense được khởi tạo thành công, bạn cần tạo một Route table để kết nối tới các mạng khác nhau. Cụ thể thực hiện theo các bước sau để tạo Route table:

**Bước 1:** Truy cập vào [https://hcm-3.console.vngcloud.vn/vserver/network/route-table](https://hcm-3.console.vngcloud.vn/vserver/network/route-table)

**Bước 2:** Tại thanh menu điều hướng, chọn **Tab Network/ Route table.**

**Bước 3:** Chọn **Create Route table.**&#x20;

**Bước 4: N**hập tên mô tả cho Route table. Tên Route table có thể bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào nằm trong khoảng từ 5 đến 50. Nó không được bao gồm khoảng trắng ở đầu hoặc ở cuối.

**Bước 5:** Chọn **VPC** cho Route table của bạn, nếu chưa có VPC cần tạo mới một VPC theo hướng dẫn tại [Trang VPC](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648039). **VPC sử dụng để thiết lập Route table phải là VPC được chọn sử dụng cho Palo Alto hoặc Pfsense và Cluster của bạn.**

**Bước 6**: Chọn **Create** để tạo mới Route table.

**Bước 7:** Chọn <img src="https://docs-admin.vngcloud.vn/download/thumbnails/73762068/image2024-4-16_15-40-3.png?version=1&#x26;modificationDate=1713256805000&#x26;api=v2" alt="" data-size="line">tại Route table vừa tạo sau đó chọn **Edit Routes.**

**Bước 8:** Tại phần thêm mới **Route** hãy nhập vào các thông tin:&#x20;

* Đối với Destination, hãy nhập **Destination CIDR là 0.0.0.0/0**
* Đối với Target, hãy nhập **Target CIDR là địa chỉ IP Network Interface của Palo Alto hoặc Pfsense tương ứng.**

***

### Khởi tạo Cluster <a href="#khoitaomotpublicclustervoiprivatenodegroup-khoitaocluster" id="khoitaomotpublicclustervoiprivatenodegroup-khoitaocluster"></a>

**Cluster trong Kubernetes** là một tập hợp gồm một hoặc nhiều máy ảo (VM) được kết nối lại với nhau để chạy các ứng dụng được đóng gói dạng container. Cluster cung cấp một môi trường thống nhất để triển khai, quản lý và vận hành các container trên quy mô lớn.

Để khởi tạo một Cluster, hãy làm theo các bước bên dưới:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn **Activate.**

**Bước 3:** Chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn. Sau khi Activate thành công, bạn hãy chọn **Create a Cluster**

**Bước 4:** Tại màn hình khởi tạo Cluster, chúng tôi đã thiết lập thông tin cho Cluster và một **Default Node Group** cho bạn, bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Cluster và Node Group của bạn tại Cluster Configuration, Default Node Group Configuration, Plugin. **Mặc định chúng tôi sẽ khởi tạo cho bạn một Public Cluster với Public Node Group. Bạn cần thay đổi lựa chọn của bạn thành&#x20;**<mark style="color:red;">**Private Node Group**</mark>**.**

**Bước 5:** Chọn **Create Kubernetes cluster.** Hãy chờ vài phút để chúng tôi khởi tạo Cluster của bạn, trạng thái của Cluster lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Cluster** là **Active**, bạn có thể xem thông tin Cluster, thông tin Node Group bằng cách chọn vào Cluster Name tại cột **Name**.

***

### Kết nối và kiểm tra thông tin Cluster vừa tạo <a href="#khoitaomotpublicclustervoiprivatenodegroup-ketnoivakiemtrathongtinclustervuatao" id="khoitaomotpublicclustervoiprivatenodegroup-ketnoivakiemtrathongtinclustervuatao"></a>

Sau khi Cluster được khởi tạo thành công, bạn có thể thực hiện kết nối và kiểm tra thông tin Cluster vừa tạo theo các bước:&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/k8s-cluster](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Danh sách Cluster được hiển thị, chọn biểu tượng ![](https://docs-admin.vngcloud.vn/download/thumbnails/73762068/image2024-4-4_14-37-11.png?version=1\&modificationDate=1712223012000\&api=v2) và chọn **Download config file** để thực hiện tải xuống file kubeconfig. File này sẽ giúp bạn có toàn quyền truy cập vào Cluster của bạn.

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

### Deploy một Workload <a href="#khoitaomotpublicclustervoiprivatenodegroup-deploymotworkload" id="khoitaomotpublicclustervoiprivatenodegroup-deploymotworkload"></a>

Sau đây là hướng dẫn để bạn deploy service nginx trên Kubernetes.

**Bước 1**: **Tạo Deployment cho Nginx app.**

*   Tạo file **nginx-service-lb4.yaml** với nội dung sau:

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
      type: LoadBalancer 
      ports:
        - protocol: TCP
          port: 80
          targetPort: 80
    ```

    * Deploy Deployment này bằng lệch:&#x20;

    ```
    kubectl apply -f nginx-service-lb4.yaml
    ```

    ***

    **Bước 2: Kiểm tra thông tin Deployment, Service trước khi expose ra Internet.**

    * Chạy câu lệnh sau đây để kiểm tra **Deployment**

    ```
    kubectl get svc,deploy,pod -owide
    ```

    * Nếu kết quả trả về như bên dưới tức là bạn đã deploy service nginx thành công.

    ```
    NAME                    TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)           AGE     SELECTOR
    service/kubernetes      ClusterIP      10.96.0.1       <none>        443/TCP           2d4h    <none>
    service/nginx-app       NodePort       10.96.215.192   <none>        30080:31289/TCP   8m12s   app=nginx
    service/nginx-service   LoadBalancer   10.96.179.221   <pending>     80:32624/TCP      2m16s   app=nginx

    NAME                        READY   UP-TO-DATE   AVAILABLE   AGE     CONTAINERS   IMAGES         SELECTOR
    deployment.apps/nginx-app   1/1     1            1           2m16s   nginx        nginx:1.19.1   app=nginx

    NAME                             READY   STATUS    RESTARTS   AGE     IP              NODE                                            NOMINATED NODE   READINESS GATES
    pod/nginx-app-7f45b65946-t7d7k   1/1     Running   0          2m16s   172.16.24.202   ng-3f06013a-f6a5-47ba-a51f-bc5e9c2b10a7-ecea1   <none>           <none
    ```

***

**Bước 3: Để truy cập vào app nginx vừa export, bạn có thể sử dụng URL với định dạng:**

```
http://Endpoint/
```

Bạn có thể lấy thông tin Public Endpoint của Load Balancer tại giao diện vLB. Cụ thể truy cập tại [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb/](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb/detail/lb-927c0b5f-5bcf-4ee1-b645-41d6a0caeecb)

Ví dụ, bên dưới tôi đã truy cập thành công vào app nginx với địa chỉ : [http://180.93.181.20/](http://180.93.181.20/)

<figure><img src="../../../../.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt=""><figcaption></figcaption></figure>
