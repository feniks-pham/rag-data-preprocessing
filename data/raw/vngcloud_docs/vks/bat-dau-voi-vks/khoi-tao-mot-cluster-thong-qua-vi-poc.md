# Khởi tạo một Cluster thông qua ví POC

Tài nguyên POC sinh ra nhằm mục đích hỗ trợ người dùng có thể trải nghiệm dịch vụ tại VNG Cloud một cách tốt nhất.

Điều kiện sử dụng tài nguyên POC:

* **Đối tượng**: Người dùng trả trước được cấp ví POC
* **Nguồn tiền:** [**Ví POC**](https://docs.vngcloud.vn/vng-cloud-document/vn/quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/trai-nghiem-billing-and-kenh-thanh-toan/ve-billing-and-payment/thanh-toan/thanh-toan-tai-nguyen-poc)
* **Tài nguyên:** Tất cả các tài nguyên được áp dụng POC
* **Thời gian sử dụng:** Tùy thuộc vào thời hạn ví POC được cấp.

***

### Điều kiện cần <a href="#khoitaomotpublicclustervoipublicnodegroup-dieukiencan" id="khoitaomotpublicclustervoipublicnodegroup-dieukiencan"></a>

Để có thể khởi tạo một **Cluster** và **Deploy** một **Workload**, bạn cần:

* Có ít nhất 1 **VPC** và 1 **Subnet** đang ở trạng thái **ACTIVE**. Nếu bạn chưa có VPC, Subnet nào, vui lòng khởi tạo VPC, Subnet theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)&#x20;
* Có ít nhất 1 **SSH** key đang ở trạng thái **ACTIVE**. Nếu bạn chưa có SSH key nào, vui lòng khởi tạo SSH key theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/security/ssh-key-bo-khoa.md)
* Đã cài đặt và cấu hình **kubectl** trên thiết bị của bạn. vui lòng tham khảo tại [đây](https://kubernetes.io/vi/docs/tasks/tools/install-kubectl/) nếu bạn chưa rõ cách cài đặt và sử dụng kuberctl. Ngoài ra, bạn không nên sử dụng phiên bản kubectl quá cũ, chúng tôi khuyến cáo bạn nên sử dụng phiên bản kubectl sai lệch không quá một phiên bản với version của cluster.

***

### Khởi tạo Cluster <a href="#khoitaomotpublicclustervoipublicnodegroup-khoitaocluster" id="khoitaomotpublicclustervoipublicnodegroup-khoitaocluster"></a>

**Cluster trong Kubernetes** là một tập hợp gồm một hoặc nhiều máy ảo (VM) được kết nối lại với nhau để chạy các ứng dụng được đóng gói dạng container. Cluster cung cấp một môi trường thống nhất để triển khai, quản lý và vận hành các container trên quy mô lớn.

Để khởi tạo một Cluster, hãy làm theo các bước bên dưới:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console.vngcloud.vn/overview)

**Bước 2:** Tại màn hình **Overview**, chọn **Activate.**

**Bước 3:** Chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn. Sau khi Activate thành công, bạn hãy chọn **Create a Cluster**

**Bước 4:** Tại màn hình khởi tạo Cluster, chúng tôi đã thiết lập thông tin cho Cluster và một **Default Node Group** cho bạn, bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Cluster và Node Group của bạn tại Cluster Configuration, Default Node Group Configuration, Plugin. **Mặc định chúng tôi sẽ khởi tạo cho bạn một Public Cluster với Public Node Group.**

**Bước 5:** Chọn **POC** và chọn tiếp **Create Kubernetes cluster.** Hãy chờ vài phút để chúng tôi khởi tạo Cluster của bạn, trạng thái của Cluster lúc này là **Creating**.

<figure><img src="../../.gitbook/assets/image (819).png" alt=""><figcaption></figcaption></figure>

**Bước 6:** Khi trạng thái **Cluster** là **Active**, bạn có thể xem thông tin Cluster, thông tin Node Group bằng cách chọn vào Cluster Name tại cột **Name**.

{% hint style="info" %}
**Chú ý:**

* Khi bạn khởi tạo Cluster và chọn sử dụng ví POC, chúng tôi đã tự động tạo Control Plane, Node, Volume và Private Service Endpoint (nếu bạn chọn sử dụng) thông qua ví POC. Đối với các tài nguyên khác như
  * **PVC:** khi thực hiện khởi tạo qua yaml, bạn vui lòng thêm tham số `isPOC: "true"` vào file yaml này. Tham khảo ví dụ bên dưới.
  * **LoadBalancer:** khi thực hiện khởi tạo qua yaml, bạn vui lòng thêm `annotation vks.vngcloud.vn/is-poc: "true"` vào file yaml này. Tham khảo ví dụ bên dưới.
* Do các resource **Load Balancer** và **PVC** được quản lý thông qua YAML, sau khi Stop POC, nếu trong file YAML của bạn vẫn có tham số `isPOC : true hoặc is-poc : true`, trong trường hợp bạn xóa Load Balancer từ Portal vLB và xóa tham số`load-balancer-id` trong yaml, lúc này hệ thống sẽ tự động tạo lại các resource này thông qua ví POC. Để tạo Load Balancer và PVC khác bằng tiền thật, vui lòng thay đổi tham số isPOC thành false. (`isPOC : false hoặc is-poc : false`). Chúng tôi khuyến cáo bạn nên thực hiện điều chỉnh tham số này trước khi thực hiện Stop POC cho Cluster của bạn.
{% endhint %}

***

### Kết nối và kiểm tra thông tin Cluster vừa tạo <a href="#khoitaomotpublicclustervoipublicnodegroup-ketnoivakiemtrathongtinclustervuatao" id="khoitaomotpublicclustervoipublicnodegroup-ketnoivakiemtrathongtinclustervuatao"></a>

Sau khi Cluster được khởi tạo thành công, bạn có thể thực hiện kết nối và kiểm tra thông tin Cluster vừa tạo theo các bước:&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/k8s-cluster](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Danh sách Cluster được hiển thị, chọn biểu tượng **Download** và chọn **Download Config File** để thực hiện tải xuống file kubeconfig. File này sẽ giúp bạn có toàn quyền truy cập vào Cluster của bạn.

**Bước 3**: Đổi tên file này thành config và lưu nó vào thư mục **\~/.kube/config**

**Bước 4:** Thực hiện kiểm tra Cluster thông qua lệnh:&#x20;

* Chạy câu lệnh sau đây để kiểm tra **node**

```bash
kubectl get nodes
```

* Nếu kết quả trả về như bên dưới tức là bạn Cluster của bạn được khởi tạo thành công với 3 node như bên dưới.

```bash
NAME                                            STATUS     ROLES    AGE   VERSION
ng-0e10592c-e70e-404d-a4e8-5e3b80f805e4-834b7   Ready      <none>   50m   v1.28.8
ng-0e10592c-e70e-404d-a4e8-5e3b80f805e4-cf652   Ready      <none>   23m   v1.28.8
ng-0f4ed631-1252-49f7-8dfc-386fa0b2d29b-a8ef0   Ready      <none>   28m   v1.28.8
```

***

### Deploy Workload và expose service thông qua vLB Layer 4 hoặc vLB Layer 7 <a href="#exposemotservicethongquavlblayer4-deploymotworkload" id="exposemotservicethongquavlblayer4-deploymotworkload"></a>

Sau đây là hướng dẫn để bạn deploy 2 workload và expose chúng qua Load Balancer Layer 4 và Load Balancer Layer 7 trên Kubernetes.

**Bước 1**: **Tạo Deployment, Service cho Nginx app.**

* Tạo file **nginx-service.yaml** với nội dung sau:

<pre class="language-bash"><code class="lang-bash">apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      unique-label: app1
  template:
    metadata:
      labels:
        unique-label: app1
        same-label: vngcloud
    spec:
      containers:
        - name: nginx-deployment
          image: nginx
          ports:
            - containerPort: 80
              name: http
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-http-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-http-server
  template:
    metadata:
      labels:
        app: python-http-server
        same-label: vngcloud
    spec:
      containers:
      - name: python-http-server
        image: python:3.9-slim
        command: ["python", "-m", "http.server", "8080"]
        ports:
        - containerPort: 8080
          name: http
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  namespace: default
  annotations:
<strong>    vks.vngcloud.vn/is-poc: "true"      # Tham số chỉ định Load Balancer được tạo sẽ bằng ví POC
</strong>spec:
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http-server
  selector:
    same-label: vngcloud
  type: LoadBalancer

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp-02
  namespace: default
  annotations:
    vks.vngcloud.vn/is-poc: "true"      # Tham số chỉ định Load Balancer được tạo sẽ bằng ví POC
spec:
  ingressClassName: vngcloud
  defaultBackend:
    service:
      name: nginx-service
      port:
        name: http-server
</code></pre>

* Deploy Service này bằng lệch:&#x20;

```bash
kubectl apply -f nginx-service.yaml
```

* Tiếp theo, bạn có thể thực hiện kiểm tra Deployment qua lệnh:&#x20;

```bash
kubectl get svc,deploy,pod -owide
```

***

### **Tạo Persistent Volume**

* Tạo file **persistent-volume.yaml** với nội dung sau:

```bash
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-expansion-storage-class                    # [1] The StorageClass name, CAN be changed
provisioner: bs.csi.vngcloud.vn                       # The VNG-CLOUD CSI driver name
parameters:
  type: vtype-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    # The volume type UUID
  isPOC: "true"                                       # Tham số chỉ định Volume được tạo sẽ bằng ví POC
allowVolumeExpansion: true                            # MUST set this value to turn on volume expansion feature
---

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-expansion-pvc                           # [2] The PVC name, CAN be changed
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi                                # [3] The PVC size, CAN be changed, this value MUST be in the valid range of the proper volume type
  storageClassName: my-expansion-storage-class     # [4] The StorageClass name, MUST be the same as [1]
---

apiVersion: v1
kind: Pod
metadata:
  name: nginx                                      # [5] The Pod name, CAN be changed
spec:
  containers:
    - image: nginx
      imagePullPolicy: IfNotPresent
      name: nginx
      ports:
        - containerPort: 80
          protocol: TCP
      volumeMounts:
        - mountPath: /var/lib/www/html
          name: my-volume-name                     # MUST be the same as [6]
  volumes:
    - name: my-volume-name                         # [6] The volume name, CAN be changed
      persistentVolumeClaim:
        claimName: my-expansion-pvc                # MUST be the same as [2]
        readOnly: false
```

* Chạy câu lệnh sau đây để triển khai Ingress

```bash
kubectl apply -f persistent-volume.yaml
```

***

### **Tạo Snapshot**

Đối với loại resource **Snapshot**, bạn không thể chỉ định snapshot sử dụng ví POC từ VKS. Để thực hiện tạo Snapshot qua ví POC, tại **vServer Portal**, vui lòng chọn **Activate Snapshot**, sau đó tại màn hình **Checkout**, vui lòng chọn sử dụng ví **POC**. Lúc này **tất cả các resource snapshot của bạn sẽ được tạo qua ví POC**. Do đó, việc stop POC cần được bạn thực hiện thông qua **vConsole** hoặc **vServer Portal**. Tham khảo thêm hình bên dưới.

<figure><img src="../../.gitbook/assets/image (820).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (821).png" alt=""><figcaption></figcaption></figure>

**Cài đặt VNGCloud Snapshot Controller**

* Cài đặt Helm phiên bản từ 3.0 trở lên. Tham khảo tại [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/) để biết cách cài đặt.
* Thêm repo này vào cluster của bạn qua lệnh:

```bash
helm repo add vks-helm-charts https://vngcloud.github.io/vks-helm-charts
helm repo update
```

* Tiếp tục chạy:

```bash
helm install vngcloud-snapshot-controller vks-helm-charts/vngcloud-snapshot-controller \
  --replace --namespace kube-system
```

* Sau khi việc cài đặt hoàn tất, thực hiện kiểm tra trạng thái của vngcloud-blockstorage-csi-driver pods:

```bash
kubectl get pods -n kube-system
```

Ví dụ như ảnh bên dưới là bạn đã cài đặt thành công vngcloud-controller-manager:

```bash
NAME                                           READY   STATUS              RESTARTS       AGE

snapshot-controller-7fdd984f89-745tg           0/1     ContainerCreating   0              3s
snapshot-controller-7fdd984f89-k94wq           0/1     ContainerCreating   0              3s
```

**Tạo file snapshot.yaml với nội dung sau:**

```bash
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: my-snapshot-storage-class  # [2] The name of the volume snapshot class, CAN be changed
driver: bs.csi.vngcloud.vn
deletionPolicy: Delete
parameters:
  force-create: "false"
---

apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: my-snapshot-pvc  # [4] The name of the snapshot, CAN be changed
spec:
  volumeSnapshotClassName: my-snapshot-storage-class  # MUST match with [2]
  source:
    persistentVolumeClaimName: my-expansion-pvc  # MUST match with [3]
```

* Chạy câu lệnh sau đây để triển khai Ingress

```bash
kubectl apply -f snapshot.yaml
```

***

### **Kiểm tra PVC và Snapshot vừa tạo**

* Sau khi apply tập tin thành công, bạn có thể kiểm tra danh sách service, pvc thông qua:

```bash
kubectl get sc,pvc,pod -owide
```

```bash
NAME                                                       PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
storageclass.storage.k8s.io/my-expansion-storage-class     bs.csi.vngcloud.vn   Delete          Immediate           true                   10m
storageclass.storage.k8s.io/sc-iops-200-retain (default)   bs.csi.vngcloud.vn   Retain          Immediate           false                  2d4h

NAME                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE   VOLUMEMODE
persistentvolumeclaim/my-expansion-pvc   Bound    pvc-14456f4a-ee9e-435d-a94f-5a2e820954e9   20Gi       RWO            my-expansion-storage-class   10m   Filesystem

NAME                             READY   STATUS    RESTARTS   AGE   IP              NODE                                            NOMINATED NODE   READINESS GATES
pod/nginx                        1/1     Running   0          10m   172.16.24.203   ng-3f06013a-f6a5-47ba-a51f-bc5e9c2b10a7-ecea1   <none>           <none>
pod/nginx-app-7f45b65946-t7d7k   1/1     Running   0          94m   172.16.24.202   ng-3f06013a-f6a5-47ba-a51f-bc5e9c2b10a7-ecea1   <none>           <none>
```

***

### Thay đổi thông số IOPS của Persistent Volume vừa tạo

\
Để thay đổi thông số IOPS của Persistent Volume vừa tạo, hãy thực hiện theo các bước sau đây:

**Bước 1:** Chạy lệnh bên dưới để liệt kê các PVC trong Cluster của bạn

```bash
kubectl get persistentvolumes
```

**Bước 2:** Chỉnh sửa tệp tin YAML của PVC theo lệnh

```bash
kubectl edit pvc my-expansion-pvc
```

* Nếu bạn chưa chỉnh sửa IOPS của Persistent Volume lần nào trước đó, khi bạn chạy lệnh trên, bạn hãy thêm 1 annotation bs.csi.vngcloud.vn/volume-type: "volume-type-id" . Ví dụ: bên dưới tôi đang thay đổi IOPS của Persistent Volume từ 200 (Volume type id = vtype-61c3fc5b-f4e9-45b4-8957-8aa7b6029018) lên 1000 (Volume type id = vtype-85b39362-a360-4bbb-9afa-a36a40cea748)

```bash
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    bs.csi.vngcloud.vn/volume-type: "vtype-85b39362-a360-4bbb-9afa-a36a40cea748"
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"PersistentVolumeClaim","metadata":{"annotations":{},"name":"my-expansion-pvc","namespace":"default"},"spec":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"20Gi"}},"storageClassName":"my-expansion-storage-class"}}
    pv.kubernetes.io/bind-completed: "yes"
    pv.kubernetes.io/bound-by-controller: "yes"
    volume.beta.kubernetes.io/storage-provisioner: bs.csi.vngcloud.vn
    volume.kubernetes.io/storage-provisioner: bs.csi.vngcloud.vn
  creationTimestamp: "2024-04-21T14:16:53Z"
  finalizers:
  - kubernetes.io/pvc-protection
  name: my-expansion-pvc
  namespace: default
  resourceVersion: "11041591"
  uid: 14456f4a-ee9e-435d-a94f-5a2e820954e9
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
  storageClassName: my-expansion-storage-class
  volumeMode: Filesystem
  volumeName: pvc-14456f4a-ee9e-435d-a94f-5a2e820954e9
status:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 20Gi
  phase: Bound
```

* Nếu bạn đã chỉnh sửa IOPS của Persistent Volume lần nào trước đó, khi bạn chạy lệnh trên, tệp tin yaml của bạn đã có sẵn annotation bs.csi.vngcloud.vn/volume-type: "volume-type-id" . Lúc này, hãy chỉnh sửa annotation này về Volume type id có IOPS mà bạn mong muốn.

### Thay đổi Disk Volume của Persistent Volume vừa tạo

\
Để thay đổi Disk Volume của Persistent Volume vừa tạo, hãy thực hiện chạy lệnh sau:

Ví dụ: ban đầu PVC được tạo có kích cỡ 20 Gi, hiện tại tôi sẽ tăng nó lên 30Gi

```bash
kubectl patch pvc my-expansion-pvc -p '{"spec":{"resources":{"requests":{"storage":"30Gi"}}}}'
```

{% hint style="info" %}
**Chú ý:**

* Bạn chỉ có thể thực hiện tăng Disk Volume mà không thể thực hiện giảm kích thước Disk Volume này.
{% endhint %}

### Restore Persistent Volume từ Snapshot

Để khôi phục Persistent Volume từ Snapshot, bạn hãy thực hiện theo các bước sau:

* Tạo file **restore-volume.yaml** với nội dung sau:

```bash
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-restore-pvc  # The name of the PVC, CAN be changed
spec:
  storageClassName: my-expansion-storage-class  
  dataSource:
    name: my-snapshot-pvc # MUST match with [4] from the section 5.2
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
```

Sau một thời gian trải nghiệm VKS, nếu bạn muốn chuyển các tài nguyên POC này thành tài nguyên thật, vui lòng thực hiện theo các bước theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vks/clusters/stop-poc).
