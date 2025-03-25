# POC và Stop POC

Trước khi tìm hiểu cách Stop POC cho tài nguyên của bạn trên VKS, bạn nên hiểu rõ các khái niệm cũng các hành động mà bạn có thể thao tác đối với tài nguyên POC. Chi tiết tham khảo thêm [tại đây](https://docs.vngcloud.vn/vng-cloud-document/v/vn/quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud/trai-nghiem-billing-and-kenh-thanh-toan/ve-billing-and-payment/quan-ly-vong-doi-tai-nguyen/tai-nguyen-poc).&#x20;

## **Khởi tạo tài nguyên VKS thông qua ví POC**

Để khởi tạo  Cluster thông qua ví POC, hãy thực hiện các bước như sau;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console.vngcloud.vn/overview)

**Bước 2:** Tại màn hình **Overview**, chọn **Activate.**

**Bước 3:** Chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn. Sau khi Activate thành công, bạn hãy chọn **Create a Cluster**

**Bước 4:** Tại màn hình khởi tạo Cluster, chúng tôi đã thiết lập thông tin cho Cluster và một **Default Node Group** cho bạn, bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Cluster và Node Group của bạn tại Cluster Configuration, Default Node Group Configuration, Plugin. **Mặc định chúng tôi sẽ khởi tạo cho bạn một Public Cluster với Public Node Group.**

**Bước 5:** Chọn POC như hình bên dưới

<figure><img src="../../.gitbook/assets/image%20(792).png" alt=""><figcaption></figcaption></figure>

**Bước 6:** Chọn **Create Kubernetes cluster.** Hãy chờ vài phút để chúng tôi khởi tạo Cluster của bạn, trạng thái của Cluster lúc này là **Creating**.

**Bước 7:** Khi trạng thái **Cluster** là **Active**, bạn có thể xem thông tin Cluster, thông tin Node Group bằng cách chọn vào Cluster Name tại cột **Name**.

{% hint style="info" %}
**Chú ý:**&#x20;

* Khi bạn khởi tạo Cluster và chọn sử dụng ví POC, chúng tôi đã tự động tạo Control Plane, Node, Volume và Private Service Endpoint (nếu bạn chọn sử dụng) thông qua ví POC. Đối với các tài nguyên khác như&#x20;
  * **PVC:** khi thực hiện khởi tạo qua yaml, bạn vui lòng thêm tham số `isPOC: "true"` vào file yaml này. Tham khảo ví dụ bên dưới.
  * **LoadBalancer:** khi thực hiện khởi tạo qua yaml, bạn vui lòng thêm annotation `vks.vngcloud.vn/is-poc: "true"` vào file yaml này. Tham khảo ví dụ bên dưới.
* Do các resource **Load Balancer** và **PVC** được quản lý thông qua YAML, sau khi Stop POC, nếu trong file YAML của bạn vẫn có tham số `isPOC : true hoặc is-poc : true`, trong trường hợp bạn xóa Load Balancer từ Portal vLB và xóa tham số`load-balancer-id` trong yaml, lúc này hệ thống sẽ tự động tạo lại các resource này thông qua ví POC. Để tạo Load Balancer và PVC khác bằng tiền thật, vui lòng thay đổi tham số isPOC thành false. (`isPOC : false hoặc is-poc : false`). Chúng tôi khuyến cáo bạn nên thực hiện điều chỉnh tham số này trước khi thực hiện Stop POC cho Cluster của bạn.
{% endhint %}

Bên dưới là yaml mẫu để tạo **Load Balancer** thông qua số dư ví POC:&#x20;

```bash
apiVersion: apps/v1
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
    vks.vngcloud.vn/is-poc: "true"
spec:
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
    vks.vngcloud.vn/is-poc: "true"
spec:
  ingressClassName: vngcloud
  defaultBackend:
    service:
      name: nginx-service
      port:
        name: http-server
```

Và đây là yaml mẫu để tạo **PVC** thông qua số dư ví POC:&#x20;

```bash
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-expansion-storage-class                    # [1] The StorageClass name, CAN be changed
provisioner: bs.csi.vngcloud.vn                       # The VNG-CLOUD CSI driver name
parameters:
  type: vtype-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    # The volume type UUID
  isPOC: "true"
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

***

## **Stop POC**

**Trước khi hết hạn sử dụng ví POC cho Cluster, bạn có hai lựa chọn chính:**

* Xóa Cluster đang POC này và tạo lại Cluster bình thường khác.
* Thực hiện Stop POC để gia hạn Cluster đang POC thành Cluster bình thường.

{% hint style="info" %}
**Chú ý:**

Để thực hiện Stop POC cho một Cluster và các thành phần liên quan của Cluster, bạn cần thực hiện:

* **Bước 1:** Thực hiện **cập nhật tham số** `isPOC : true hoặc is-poc : true` về `isPOC : false hoặc is-poc : false` trong các yaml cho Load Balancer, PVC nếu có.
* **Bước 2:** Thực hiện **Stop POC** cho **Cluster** thông qua nút **Stop POC** trên **VKS Portal** theo hướng dẫn bên dưới.
* **Bước 3:** Thực hiện **Thanh toán cho các tài nguyên thông qua tiền thật.**
{% endhint %}

**Để tiếp tục sử dụng tài nguyên vừa dừng POC như một tài nguyên bình thường (với mục đích giữ nguyên cấu hình), người dùng có thể thực hiện:**&#x20;

**Bước 1:** Truy cập vào [VKS Portal](https://vks.console.vngcloud.vn/k8s-cluster), chọn Cluster mà bạn muốn Stop POC.

**Bước 2:** Chọn nút **Stop POC** phía trên góc phải màn hình.

<figure><img src="../../.gitbook/assets/image%20(517).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Lúc này, màn hình hiển thị danh sách tất cả các Server và Volume (<mark style="color:red;">**bao gồm cả Boot Volume và PVC mà bạn attach vào node trong Cluster của bạn)**</mark> , Load Balancer, Endpoint thuộc Cluster đang có trạng thái POC. Bạn có thể kiểm tra thông tin sau đó chọn **Stop POC**

<figure><img src="../../.gitbook/assets/image%20(795).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image%20(794).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image%20(793).png" alt=""><figcaption></figcaption></figure>

**Bước 4**: Tiến hành thanh toán tài nguyên bằng tiền thật, bạn có thể lựa chọn **Chu kỳ sử dụng mong muốn, bật tắt Tự động gia hạn, nhập Coupon** nếu có và chọn **Continue** để thực hiện Thanh toán tài nguyên

<figure><img src="../../.gitbook/assets/image%20(796).png" alt=""><figcaption></figcaption></figure>

**Bước 5**: Thực hiện thanh toán bằng số dư credit hoặc qua các hình thức thanh toán khác nếu có.

<figure><img src="../../.gitbook/assets/image%20(797).png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Để đảm bảo VKS hoạt động chính xác, việc thực hiện Stop POC cần được tiến hành trên VKS Portal thay vì thực hiện riêng lẻ trên vServer Portal hoặc vConsole.**</mark> Nếu bạn đã thực hiện stop POC riêng lẻ cho từng resource trên vServer Portal trước đó, bạn vẫn **cần thực hiện Stop POC** cho Cluster tại VKS Portal, lúc này, màn hình sẽ hiển thị như sau. Bạn hãy nhẫn **Stop** để tắt lựa chọn POC cho Cluster của bạn.

<figure><img src="../../.gitbook/assets/image%20(4)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="" width="258"><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**&#x20;

* Sau khi stop POC trên VKS, nút "**Stop POC**" sẽ tiếp tục hiển thị **nếu chúng tôi thấy vẫn còn resource chưa được Stop POC** sau khi thực hiện trên VKS Portal. Bạn có thể tiếp tục chọn và thực hiện **Stop POC** cho đến khi tất cả các resource được chuyển về resource thật.
* <mark style="color:red;">Đối với loại resource</mark> <mark style="color:red;"></mark><mark style="color:red;">**Snapshot**</mark><mark style="color:red;">, bạn không thể chỉ định snapshot sử dụng ví POC từ VKS. Để thực hiện tạo Snapshot qua ví POC, tại</mark> <mark style="color:red;"></mark><mark style="color:red;">**vServer Portal**</mark><mark style="color:red;">, vui lòng chọn</mark> <mark style="color:red;"></mark><mark style="color:red;">**Activate Snapshot**</mark><mark style="color:red;">, sau đó tại màn hình</mark> <mark style="color:red;"></mark><mark style="color:red;">**Checkout**</mark><mark style="color:red;">, vui lòng chọn sử dụng ví</mark> <mark style="color:red;"></mark><mark style="color:red;">**POC**</mark><mark style="color:red;">. Lúc này</mark> <mark style="color:red;"></mark><mark style="color:red;">**tất cả các resource snapshot của bạn sẽ được tạo qua ví POC**</mark><mark style="color:red;">. Do đó, việc stop POC cần được bạn thực hiện thông qua</mark> <mark style="color:red;"></mark><mark style="color:red;">**vConsole**</mark> <mark style="color:red;"></mark><mark style="color:red;">hoặc</mark> <mark style="color:red;"></mark><mark style="color:red;">**vServer Portal**</mark><mark style="color:red;">. Tham khảo thêm hình bên dưới.</mark>
{% endhint %}

<figure><img src="../../.gitbook/assets/image%20(807).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image%20(808).png" alt=""><figcaption></figcaption></figure>
