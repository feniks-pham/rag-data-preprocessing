# Khởi tạo một Private Cluster

Trước đây, các public cluster trên VKS đang sử dụng địa chỉ Public IP để giao tiếp giữa nodes và control plane. Để nâng cao bảo mật cho cluster của bạn, chúng tôi đã cho ra mắt mô hình private cluster. Tính năng Private Cluster giúp cho cụm K8S của bạn được bảo mật nhất có thể, mọi kết nối hoàn toàn là private từ kết nối giữa nodes tới control plane, kết nối từ client tới control plane, hay kết nối từ nodes tới các sản phẩm dịch vụ khác trong VNG Cloud như: vStorage, vCR, vMonitor, VNGCloud APIs,...Private Cluster là lựa chọn lý tưởng cho **các dịch vụ yêu cầu kiểm soát truy cập chặt chẽ, đảm bảo tuân thủ các quy định về bảo mật và quyền riêng tư dữ liệu**.&#x20;

### Model <a href="#khoitaomotpublicclustervoiprivatenodegroup-dieukiencan" id="khoitaomotpublicclustervoiprivatenodegroup-dieukiencan"></a>

<figure><img src="../../.gitbook/assets/image (691).png" alt=""><figcaption></figcaption></figure>

**Thành phần**

* **Control plane**: Được quản lý bởi VNG Cloud, chịu trách nhiệm điều phối và quản lý toàn bộ cluster.
* **Nodes**: Các Node trong Cluster khi được tạo ra sẽ chỉ có internal IP và không thể đi ra public internet. Nếu muốn node truy cập được internet, bạn cần sử dụng NAT Gateway. Chi tiết tham khảo thêm tại [đây](khoi-tao-mot-public-cluster/khoi-tao-mot-public-cluster-voi-private-node-group/pfsense-as-a-nat-gateway.md).
* **Private Load Balancer**: Được quản lý bởi VNG Cloud, chịu trách nhiệm giúp các Private Node giao tiếp với Control Plane.
* **Private Service Endpoint**: Khi bạn tạo một private cluster, hệ thống tự động tạo 4 endpoints giúp kết nối với các dịch vụ khác trên VNG Cloud bao gồm:
  * **Endpoint** để kết nối tới dịch vụ **IAM** (Endpoint Name: vks-iam-endpoint-...)
  * **Endpoint** để kết nối tới dịch vụ **vCR** (Endpoint Name: vks-vcr-endpoint-...)
  * **Endpoint** để kết nối tới dịch vụ **vServer** (Endpoint Name: vks-vserver-endpoint-...)
  * **Endpoint** để kết nối tới dịch vụ **vStorage** (Endpoint Name: vks-vstorage-endpoint-...)

Bạn có thể xem thông tin 4 private service endpoint thông qua portal vServer theo đường dẫn tại [đây](https://hcm-3.console.vngcloud.vn/vserver/vnetwork/endpoint/list).

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Warning:**

*   <mark style="color:red;background-color:red;">**Không xóa Private Service Endpoint**</mark>: Để đảm bảo hoạt động ổn định của cluster, bạn không nên xóa 4 service endpoint đã được tạo sẵn. Nếu vô tình xóa hoặc chỉnh sửa 4 endpoint này, trong vòng tối đa 5 phút, hệ thống sẽ tự động tạo lại nhưng có thể gây gián đoạn đến các dịch vụ đang chạy. Lúc này, do service endpoint tạo lại có thể đã thay đổi Endpoint IP so với ban đầu nên để cluster hoạt động được, bạn cần thực hiện thêm Endpoint IP một cách thủ công cho những server đang chạy trước đó thông qua câu lệnh:

    ```
    vks-bootstraper add-host -i <IP> -d <DOMAIN>
    ```

    Ví dụ, nếu bạn xóa private service endpoint của vCR thì bạn cần add host qua lệnh:

    ```
    vks-boostraper add-host -i 10.10.10.10 -d vcr.vngcloud.vn
    ```
* <mark style="color:red;background-color:red;">**Tái sử dụng Private Service Endpoint:**</mark> Các service endpoint có thể được nhiều private cluster cùng sử dụng. Khi các private cluster chung VPC thì chúng tôi sẽ tái sử dụng chúng cho các cluster này.
* <mark style="color:red;background-color:red;">**Xóa Private Service Endpoint tự động:**</mark> Khi bạn xóa cluster, nếu không còn cluster nào tái sử dụng các service endpoint này, hệ thống sẽ tự động xóa chúng.
* <mark style="color:red;background-color:red;">**Chi phí sử dụng Private Service Endpoint:**</mark> Việc sử dụng private cluster sẽ phát sinh thêm chi phí cho 4 private service endpoint, nhưng nó mang lại nhiều lợi ích về bảo mật cho dự án của bạn. Bạn hãy cân nhắc kỹ lưỡng các yếu tố để đưa ra quyết định sử dụng public hay private cho cluster của mình.
{% endhint %}

***

### Điều kiện cần <a href="#khoitaomotpublicclustervoiprivatenodegroup-dieukiencan" id="khoitaomotpublicclustervoiprivatenodegroup-dieukiencan"></a>

Để có thể khởi tạo một **Cluster** và **Deploy** một **Workload**, bạn cần:

* Có ít nhất 1 **VPC** và 1 **Subnet** đang ở trạng thái **ACTIVE**. Nếu bạn chưa có VPC, Subnet nào, vui lòng khởi tạo VPC, Subnet theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc/)
* Có ít nhất 1 **SSH** key đang ở trạng thái **ACTIVE**. Nếu bạn chưa có SSH key nào, vui lòng khởi tạo SSH key theo hướng dẫn tại [đây.](../../vserver/compute-hcm03-1a/security/ssh-key-bo-khoa.md)
* Đã cài đặt và cấu hình **kubectl** trên thiết bị của bạn. vui lòng tham khảo tại [đây](https://kubernetes.io/vi/docs/tasks/tools/install-kubectl/) nếu bạn chưa rõ cách cài đặt và sử dụng kuberctl. Ngoài ra, bạn không nên sử dụng phiên bản kubectl quá cũ, chúng tôi khuyến cáo bạn nên sử dụng phiên bản kubectl sai lệch không quá một phiên bản với version của cluster.

***

### Khởi tạo Cluster <a href="#khoitaomotpublicclustervoiprivatenodegroup-khoitaocluster" id="khoitaomotpublicclustervoiprivatenodegroup-khoitaocluster"></a>

**Cluster trong Kubernetes** là một tập hợp gồm một hoặc nhiều máy ảo (VM) được kết nối lại với nhau để chạy các ứng dụng được đóng gói dạng container. Cluster cung cấp một môi trường thống nhất để triển khai, quản lý và vận hành các container trên quy mô lớn.

Để khởi tạo một Cluster, hãy làm theo các bước bên dưới:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn **Activate.**

**Bước 3:** Chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn. Sau khi Activate thành công, bạn hãy chọn **Create a Cluster**

**Bước 4:** Tại màn hình khởi tạo Cluster, chúng tôi đã thiết lập thông tin cho Cluster và một **Default Node Group** cho bạn, bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Cluster và Node Group của bạn tại Cluster Configuration, Default Node Group Configuration, Plugin.

<figure><img src="../../.gitbook/assets/image (693).png" alt=""><figcaption></figcaption></figure>

**Bước 5:** Chọn **Create Kubernetes cluster.** Hãy chờ vài phút để chúng tôi khởi tạo Cluster của bạn, trạng thái của Cluster lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Cluster** là **Active**, bạn có thể xem thông tin Cluster, thông tin Node Group bằng cách chọn vào Cluster Name tại cột **Name**.

{% hint style="info" %}
**Warning:**

* **Một Cluster** có thể có **nhiều Node Group**, mỗi Node Group có thể hoạt động ở mode Public/ Private tùy theo nhu cầu của bạn.
* Do **Cluster** của bạn được khởi tạo ở chế độ **Private**, để có thể truy cập vào **kube-api** của Control Plane thì bạn cần **đứng trong VPC** mà bạn chọn sử dụng cho Cluster của bạn.
{% endhint %}

***

### Kết nối và kiểm tra thông tin Cluster vừa tạo <a href="#khoitaomotpublicclustervoiprivatenodegroup-ketnoivakiemtrathongtinclustervuatao" id="khoitaomotpublicclustervoiprivatenodegroup-ketnoivakiemtrathongtinclustervuatao"></a>

Sau khi Cluster được khởi tạo thành công, bạn có thể thực hiện kết nối và kiểm tra thông tin Cluster vừa tạo theo các bước:

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/k8s-cluster](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Danh sách Cluster được hiển thị, chọn biểu tượng **Download** và chọn **Download config file** để thực hiện tải xuống file kubeconfig. File này sẽ giúp bạn có toàn quyền truy cập vào Cluster của bạn.

**Bước 3**: Đổi tên file này thành config và lưu nó vào thư mục **\~/.kube/config**

**Bước 4:** Do Cluster của bạn được khởi tạo ở chế độ Private, để có thể truy cập vào kube-api, bạn cần đứng trong VPC mà bạn đã chọn sử dụng cho Cluster của bạn. Ví dụ, khi bạn không đứng ở VPC và thực hiện get nodes, kết quả sẽ hiển thị như sau:

```
kubectl get nodes
E0821 14:27:03.793829   23348 memcache.go:265] couldn't get current server API group list: Get "https://10.7.8.9:6443/api?timeout=32s": dial tcp 10.7.8.9:6443: connectex: No connection could be made because the target machine actively refused it.
E0821 14:27:05.866230   23348 memcache.go:265] couldn't get current server API group list: Get "https://10.7.8.9:6443/api?timeout=32s": dial tcp 10.7.8.9:6443: connectex: No connection could be made because the target machine actively refused it.
E0821 14:27:07.922272   23348 memcache.go:265] couldn't get current server API group list: Get "https://10.7.8.9:6443/api?timeout=32s": dial tcp 10.7.8.9:6443: connectex: No connection could be made because the target machine actively refused it.
E0821 14:27:09.989832   23348 memcache.go:265] couldn't get current server API group list: Get "https://10.7.8.9:6443/api?timeout=32s": dial tcp 10.7.8.9:6443: connectex: No connection could be made because the target machine actively refused it.
E0821 14:27:12.055864   23348 memcache.go:265] couldn't get current server API group list: Get "https://10.7.8.9:6443/api?timeout=32s": dial tcp 10.7.8.9:6443: connectex: No connection could be made because the target machine actively refused it.
Unable to connect to the server: dial tcp 10.7.8.9:6443: connectex: No connection could be made because the target machine actively refused it.
```

Trong ví dụ bên dưới tôi sẽ đứng tại một server có VPC cùng với VPC được sử dụng cho Cluster. Bạn có thể thực hiện SSH vào server theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/v/vn/vserver/compute-hcm03-1a/server/ket-noi-vao-may-chu-ao/ket-noi-vao-may-chu-linux-bang-cong-cu-ssh-client). Sau khi SSH vào server, hãy cài đặt kubectl theo hướng dẫn tại [đây](huong-dan-cai-dat-va-cau-hinh-cong-cu-kubectl-trong-kubernetes.md).

* Ví dụ, tôi đang sử dụng một server linux để thực hiện get nodes, tôi có thể cài đặt kubectl qua lệnh:

```
sudo snap install kubectl --classic
```

* Sau đó, tôi kiểm tra kubectl qua lệnh:

```
kubectl version
```

* Tạo thư mục .`kube` qua lệnh:

```
mkdir -p .kube
```

* Sau đó, bạn hãy nhập file kubeconfig qua lệnh:

```
vim .kube/config
```

* Sau đó, bạn nhập **:wq** để lưu file kubeconfig và thoát vim.
* Chạy câu lệnh sau đây để kiểm tra **cluster**

```
kubectl get svc
```

* Bạn sẽ thấy kết quả trả về tương tự sau:

```
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   10m
```

* Chạy câu lệnh sau đây để kiểm tra **node**

```
kubectl get nodes
```

* Nếu kết quả trả về như bên dưới tức là bạn Cluster của bạn được khởi tạo thành công với 1 node như bên dưới.

```
NAME                                    STATUS   ROLES    AGE     VERSION
vks-demo-cluster-nodegroup-demo-7c9aa   Ready    <none>   8m11s   v1.28.8
```

***

### Sử dụng Docker để Pull/Push image <a href="#khoitaomotpublicclustervoiprivatenodegroup-deploymotworkload" id="khoitaomotpublicclustervoiprivatenodegroup-deploymotworkload"></a>

Do Private Cluster chỉ có thể kết nối private tới hệ thống vContainer Registry (vCR) và không thể kết nối ra các Container Registry khác ngoài internet, nên bạn cần pull/ push image về vCR để sử dụng theo hướng dẫn sau đây:

#### **Bước 1: Cài đặt Docker**

* Thực hiện cài đặt docker theo hướng dẫn tại [đây](https://docs.docker.com/engine/install/).

#### **Bước 2: Khởi tạo Public Repository và Repository User trên vContainer Registry Portal:**

* Đăng nhập portal vCR tại đường dẫn: [https://vcr.console.vngcloud.vn/list](https://vcr.console.vngcloud.vn/list)
* Thực hiện khởi tạo Repositoryvà Repository theo hướng dẫn tại [đây](../../vcontainer-registry/repository/). Ví dụ trong hình dưới, tôi đã khởi tạo demo\_repo với demo\_user có thể pull/ push image:

<figure><img src="../../.gitbook/assets/image (697).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (698).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Warning:**

* Nếu bạn mong muốn khởi tạo Private Reposity, để pull image từ Private Reposity, bạn cần tạo secret key theo hướng dẫn tại [đây](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).
{% endhint %}

**Bước 3:** Thực hiện pull image nginx về theo lệnh:

```
docker pull nginx:latest
```

**Bươc 4:** Thực hiện login vào vCR qua lệnh:

```
docker login vcr.vngcloud.vn -u <repository_user>
```

* Ví dụ, câu lệnh dưới tôi sử dụng để login vào repo demo:

```
docker login vcr.vngcloud.vn -u 53461-user_demo
```

**Bước 5:** Gán tag cho image nginx

```
docker tag SOURCE_IMAGE[:TAG] vcr.vngcloud.vn/REPO_NAME/IMAGE[:TAG]
```

* Ví dụ, câu lệnh dưới tôi sử dụng để gán tag cho image nginx:

```
docker tag nginx:latest vcr.vngcloud.vn/53461-repo_demo/nginx-demo:latest
```

**Bước 6:** Thực hiện push image lên repo qua lệnh:

```
docker push vcr.vngcloud.vn/REPO_NAME/IMAGE[:TAG]
```

* Ví dụ, câu lệnh dưới tôi sử dụng để push image lên demo\_repo:

```
docker push vcr.vngcloud.vn/53461-repo_demo/nginx-demo:latest
```

***

### Deploy một Workload <a href="#khoitaomotpublicclustervoiprivatenodegroup-deploymotworkload" id="khoitaomotpublicclustervoiprivatenodegroup-deploymotworkload"></a>

Sau đây là hướng dẫn để bạn deploy service nginx và expose service này qua Network Load Balancer

#### **Bước 1: Thực hiện tạo file nginx-service-lb4.yaml qua lệnh:**

```
vi nginx.yaml
```

Sau đó, bạn hãy nhập nội dung cho file này như sau: bạn cần thay image bằng đường dẫn image lưu trên vCR mà bạn đã push ở bước bên trên:

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
        image: vcr.vngcloud.vn/53461-repo_demo/nginx-demo:latest
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

* Nhập **:wq** để lưu tệp tin này.
* Deploy Deployment này bằng lệch:

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
NAME                    TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE     SELECTOR
service/kubernetes      ClusterIP      10.96.0.1      <none>           443/TCP        91m     <none>
service/nginx-service   LoadBalancer   10.96.81.236   116.118.88.236   80:32333/TCP   3m32s   app=nginx

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE     CONTAINERS   IMAGES                                              SELECTOR
deployment.apps/nginx-app   1/1     1            1           3m32s   nginx        vcr.vngcloud.vn/53461-repo_demo/nginx-demo:latest   app=nginx

NAME                             READY   STATUS    RESTARTS   AGE     IP             NODE                                    NOMINATED NODE   READINESS GATES
pod/nginx-app-56bbc8fdd8-4pz68   1/1     Running   0          3m32s   172.16.4.207   vks-demo-cluster-nodegroup-demo-7c9aa   <none>           <none>
```

***

Lúc này, hệ thống vLB sẽ khởi tạo môt Network Load Balancer, bạn có thể xem thông tin LB này thông qua portal vLB tại [đây](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb).

<figure><img src="../../.gitbook/assets/image (699).png" alt=""><figcaption></figcaption></figure>

**Bước 3: Để truy cập vào app nginx vừa export, bạn có thể sử dụng Endpoint của Load Balancer URL với định dạng:**

```
http://Endpoint/
```

Bạn có thể lấy thông tin Public Endpoint của Load Balancer tại giao diện vLB. Cụ thể truy cập tại [https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb/](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb/detail/lb-927c0b5f-5bcf-4ee1-b645-41d6a0caeecb)

Ví dụ, bên dưới tôi đã truy cập thành công vào app nginx với địa chỉ : [http://116.118.88.236/](http://116.118.88.236/)

<figure><img src="../../.gitbook/assets/image (700).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Một vài chú ý khác:**

* Bên trên là ví dụ hướng dẫn bạn thực hiện expose một service thông qua vLB Layer 4, bạn có thể thực hiện expose service thông qua vLB Layer 7 theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/v/vn/vks/bat-dau-voi-vks/expose-mot-service-thong-qua-vlb-layer7).
* Để đảm bảo private cluster hoạt động hiệu quả, chúng tôi đã tự động thêm Subnet mà bạn chọn sử dụng cho Cluster vào danh sách Whitelist của cụm. Bạn có thể sử dụng tính năng Whitelist để giới hạn các Subnet trong VPC có quyền truy cập vào kube-api. Chi tiết cách sử dụng tính năng Whitelist vui lòng tham khảo tại [đây](https://docs.vngcloud.vn/vng-cloud-document/v/vn/vks/clusters/whitelist).
{% endhint %}
