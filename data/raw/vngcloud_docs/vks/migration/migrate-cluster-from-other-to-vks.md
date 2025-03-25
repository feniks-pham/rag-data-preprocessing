# Migrate Cluster from another platform to VKS

Để migrate một Cluster từ hệ thống Cloud Provider hoặc On-premise tới hệ thống VKS, hãy thực hiện theo các bước theo tài liệu này.

## Điều kiện cần

* <mark style="color:red;">**Thực hiện tải xuống helper bash script và grand execute permission cho file này**</mark> ([velero\_helper.sh](https://raw.githubusercontent.com/vngcloud/velero/main/velero\_helper.sh))
*   (Optional) Triển khai một vài service để kiểm tra tính đúng đắn của việc migrate. Giả sử, tại Cluster nguồn, tôi đã triển khai một service nginx như sau:

    * File triển khai:

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: nginx
      namespace: mynamespace
      labels:
        app: nginx
    spec:
      ports:
      - port: 80
        name: web
      selector:
        app: nginx
      type: NodePort
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: web
      namespace: mynamespace
    spec:
      selector:
        matchLabels:
          app: nginx
      serviceName: "nginx"
      replicas: 1
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx
            ports:
            - containerPort: 80
              name: web
            volumeMounts:
            - name: disk-ssd
              mountPath: /usr/share/nginx/html
      volumeClaimTemplates:
      - metadata:
          name: disk-ssd
          namespace: mynamespace
        spec:
          accessModes: [ "ReadWriteOnce" ]
          storageClassName: standard-rwo
          resources:
            requests:
              storage: 40Gi
    ```

    ```bash
    kubectl exec -n mynamespace -it web-0 bash
    cd /usr/share/nginx/html
    echo -e "<html>\n<head>\n  <title>MyVNGCloud</title>\n</head>\n<body>\n  <h1>Hello, MyVNGCloud</h1>\n</body>\n</html>" > index.html
    ```
* Lúc này, khi bạn truy cập vào Public IP của Node, bạn sẽ thấy "Hello, MyVNGCloud".

***

## Chuẩn bị cluster đích (Prepare target resource)

Trên hệ thống VKS, bạn cần thực hiện khởi tạo một Cluster theo hướng dẫn tại [đây](../clusters/). Đảm bảo rằng cấu hình của cluster đích giống với cấu hình của cluster nguồn.

{% hint style="info" %}
**Chú ý:**

Để việc migrate thành công, trên Cluster đích, bạn cần đảm bảo các yêu cầu sau:

* Lượng resource cần thiết như số lượng node, cấu hình instance của node,...
* Node labels và node taints giống cluster cũ.
* Storage Class tương ứng hoặc thay thế.
{% endhint %}

***

## \[Optional] Migrate resources private outside cluster

Migrating resources private outside cluster (di chuyển tài nguyên riêng tư bên ngoài cụm) là quá trình di chuyển tài nguyên riêng tư nằm ngoài Cluster nguồn sang một nơi mà Cluster đích có thể sử dụng. Ví dụ, bạn có thể có những tài nguyên riêng tư như image, database,... Lúc này, trước khi bắt đầu migrate, bạn cần tự thực hiện việc migrate các tài nguyên này. Ví dụ, nếu bạn cần:

* Migrate Container Images: bạn có thể migrate image tới VNGCloud Container Registry thông qua hướng dẫn tại [đây](../../vcontainer-registry/).
* Migrate Databases: bạn có thể sử dụng **Relational Database Service (RDS)** và **Object Storage Service (OBS)** tùy theo nhu cầu sử dụng của bạn. Sau khi việc migration hoàn tất, hãy nhớ config lại database cho applications của bạn trên VKS Cluster.
* Migrate Storage: bạn có thể sử dụng **NFS Server** của vServer.

{% hint style="info" %}
**Chú ý:**

* Sau khi bạn thực hiện migrate các resource ngoài Cluster, bạn cần đảm bảo Cluster đích kết nối được tới các resource đã migrate này.
{% endhint %}

***

## Cài đặt Velero trên cả 2 cluster nguồn và cluster đích (Install Velero tool)

Sau khi bạn đã thực hiện migrate các tài nguyên private ngoài cluster, bạn có thể sử dụng công cụ migration để sao lưu (backup) và khôi phục (restore) application trên cluster nguồn và cluster đích.

* Tạo một **vStorage Project, Container** làm nơi nhận dữ liệu backup của cụm theo hướng dẫn tại [đây](../../vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-project/khoi-tao-project.md).
* Khởi tạo S3 key tương ứng với vStorage Project này theo hướng dẫn tại [đây](../../vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-s3-key.md).

Ví dụ, tôi đã khởi tạo một vStorage Project, Container có thông tin sau: Region: HCM03, Container: mycontainer, Endpoint: [https://hcm03.vstorage.vngcloud.vn](https://hcm03.vstorage.vngcloud.vn).

### Trên cả 2 Cluster (source and target)

*   Tạo file **credentials-velero** với nội dung sau:

    ```yaml
    [default]
    aws_access_key_id=________________________
    aws_secret_access_key=________________________
    ```
*   Cài đặt Velero CLI:

    ```bash
    curl -OL https://github.com/vmware-tanzu/velero/releases/download/v1.13.2/velero-v1.13.2-linux-amd64.tar.gz
    tar -xvf velero-v1.13.2-linux-amd64.tar.gz
    cp velero-v1.13.2-linux-amd64/velero /usr/local/bin
    ```
*   Cài đặt Velero trên 2 cụm của bạn theo lệnh:

    ```bash
    velero install \
        --provider aws \
        --plugins velero/velero-plugin-for-aws:v1.9.0 \
        --use-node-agent \
        --use-volume-snapshots=false \
        --secret-file ./credentials-velero \
        --bucket ______________________________ \
        --backup-location-config region=hcm03,s3ForcePathStyle="true",s3Url=https://hcm03.vstorage.vngcloud.vn
    ```

***

## Đối với Cluster trên Amazon Elastic Kubernetes Service (EKS)

### Tại Cluster nguồn

*   Annotate các Persistent Volume cần backup. Mặc định velero sẽ không backup volume. Bạn có thể chạy lệnh dưới để annotate backup tất cả volume.

    ```yaml
    ./velero_helper.sh mark_volume -c
    ```
*   Ngoài ra, bạn có thể đánh dấu không backup các resource của system bằng lệnh sau:

    ```yaml
    ./velero_helper.sh mark_exclude -c
    ```
*   Thực hiện backup theo cú pháp:

    ```bash
    velero backup create eks-cluster --include-namespaces "" \
      --include-cluster-resources=true \
      --wait
    ```

    ```bash
    velero backup create eks-namespace --exclude-namespaces velero \
        --wait
    ```

{% hint style="info" %}
**Chú ý:**

* Bạn phải tạo 2 phiên bản backup cho Cluster Resource và Namespace Resource.
{% endhint %}

***

### Tại Cluster đích

*   Tạo file mapping Storage Class giữa Cluster nguồn và đích:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: change-storage-class-config
      namespace: velero
      labels:
        velero.io/plugin-config: ""
        velero.io/change-storage-class: RestoreItemAction
    data:
      _______old_storage_class_______: _______new_storage_class_______  # <= Adjust here
      _______old_storage_class_______: _______new_storage_class_______  # <= Adjust here
    ```
*   Thực hiện restore theo lệnh:

    ```bash
    velero restore create --item-operation-timeout 1m --from-backup eks-cluster \
        --exclude-resources="MutatingWebhookConfiguration,ValidatingWebhookConfiguration"
    ```

    ```bash
    velero restore create --item-operation-timeout 1m --from-backup eks-namespace
    ```

    ```bash
    velero restore create --item-operation-timeout 1m --from-backup eks-cluster
    ```

***

## Đối với Cluster trên Google Kubernetes Engine (GKE)

### Tại Cluster nguồn

*   Annotate các Persistent Volume và lable resource cần loại trừ khỏi bản backup

    ```yaml
    ./velero_helper.sh mark_volume -c
    ```
*   Ngoài ra, bạn có thể đánh dấu không backup các resource của system bằng lệnh sau:

    ```yaml
    ./velero_helper.sh mark_exclude -c
    ```
*   Thực hiện backup theo cú pháp:

    ```bash
    velero backup create gke-cluster --include-namespaces "" \
      --include-cluster-resources=true \
      --wait
    ```

    ```bash
    velero backup create gke-namespace --exclude-namespaces velero \
        --wait
    ```

{% hint style="info" %}
**Chú ý:**

* Bạn phải tạo 2 phiên bản backup cho Cluster Resource và Namespace Resource.
{% endhint %}

***

### Tại Cluster đích

*   Tạo file mapping Storage Class giữa Cluster nguồn và đích:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: change-storage-class-config
      namespace: velero
      labels:
        velero.io/plugin-config: ""
        velero.io/change-storage-class: RestoreItemAction
    data:
      _______old_storage_class_______: _______new_storage_class_______  # <= Adjust here
      _______old_storage_class_______: _______new_storage_class_______  # <= Adjust here
    ```
*   Thực hiện restore theo lệnh:

    ```bash
    velero restore create --item-operation-timeout 1m --from-backup gke-cluster \
        --exclude-resources="MutatingWebhookConfiguration,ValidatingWebhookConfiguration"
    ```

    ```bash
    velero restore create --item-operation-timeout 1m --from-backup gke-namespace
    ```

    ```bash
    velero restore create --item-operation-timeout 1m --from-backup gke-cluster
    ```

{% hint style="info" %}
**Chú ý:**

* Google Kubernetes Engine (GKE) không cho phép triển khai daemonset trên tất cả các node. Tuy nhiên, Velero chỉ cần triển khai daemonset trên node có mount PV. Giải pháp cho vấn đề này là bạn có thể điều chỉnh taint và toleration của daemonset để chỉ triển khai nó trên node có mount PV.
* Bạn có thể thay đổi yêu cầu tài nguyên mặc định `cpu:500m` và `mem:512M` trong bước cài đặt hoặc điều chỉnh khi triển khai yaml.
{% endhint %}
