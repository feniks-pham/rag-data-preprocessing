# Migrate Cluster from VKS to VKS

Để migrate một Cluster từ hệ thống VKS tới hệ thống VKS, hãy thực hiện theo các bước theo tài liệu này.

## Điều kiện cần

* <mark style="color:red;">**Thực hiện tải xuống helper bash script và grand execute permission cho file này**</mark> ([velero\_helper.sh](https://raw.githubusercontent.com/vngcloud/velero/main/velero\_helper.sh))
* (Optional) Triển khai một vài service để kiểm tra tính đúng đắn của việc migrate. Giả sử, tại Cluster nguồn, tôi đã triển khai một service nginx như sau:

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
          storageClassName: ssd-3000
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

* Tạo file **credentials-velero** với nội dung sau:

    ```yaml
    [default]
    aws_access_key_id=________________________
    aws_secret_access_key=________________________
    ```

* Cài đặt Velero CLI:

    ```bash
    curl -OL https://github.com/vmware-tanzu/velero/releases/download/v1.13.2/velero-v1.13.2-linux-amd64.tar.gz
    tar -xvf velero-v1.13.2-linux-amd64.tar.gz
    cp velero-v1.13.2-linux-amd64/velero /usr/local/bin
    ```

* Cài đặt Velero trên 2 cụm của bạn theo lệnh:

    ```bash
    velero install --provider aws \
      --plugins velero/velero-plugin-for-aws:v1.9.0,velero/velero-plugin-for-csi:v0.7.0 \
      --secret-file ./credentials-velero \
      --bucket ________________________ \
      --backup-location-config region=hcm03,s3ForcePathStyle="true",s3Url=https://hcm03.vstorage.vngcloud.vn \
      --use-node-agent \
      --features=EnableCSI
    ```

    ```bash
    velero client config set features=EnableCSI
    ```

{% hint style="info" %}
**Chú ý:**

* Khi bạn thực hiện migrate cluster từ VKS tới VKS, chúng tôi khuyến cáo bạn sử dụng **Snapshot** để migrate Volume của bạn từ cluster nguồn qua cluster đích.
{% endhint %}

* Cài đặt plugin **VNGCloud Snapshot Controller** trên 2 cluster theo lệnh:

    ```bash
    helm repo add vks-helm-charts https://vngcloud.github.io/vks-helm-charts
    helm repo update
    helm install vngcloud-snapshot-controller vks-helm-charts/vngcloud-snapshot-controller \
      --replace --namespace kube-system
    ```

***

## Tại Cluster nguồn

* Annotate các Persistent Volume cần backup. Mặc định velero sẽ không backup volume. Bạn có thể chạy lệnh dưới để annotate backup tất cả volume.

    ```bash
    ./velero_helper.sh mark_volume -c
    ```

* Ngoài ra, bạn có thể đánh dấu không backup các resource của system bằng lệnh sau:

    ```bash
    ./velero_helper.sh mark_exclude -c
    ```

* Thực hiện apply file bên dưới để tạo default VolumeSnapshotClass:

    ```yaml
    apiVersion: snapshot.storage.k8s.io/v1
    kind: VolumeSnapshotClass
    metadata:
      name: vngcloud-vsclass
      labels:
        velero.io/csi-volumesnapshot-class: "true"
    driver: bs.csi.vngcloud.vn
    deletionPolicy: Delete

    # user can choose the VolumeSnapshotClass by setting annotation velero.io/csi-volumesnapshot-class_disk.csi.cloud.com: "test-snapclass" on backup resource.
    # user can choose the VolumeSnapshotClass by setting annotation velero.io/csi-volumesnapshot-class: "test-snapclass" on PersistentVolumeClaim resource.
    ```

* Thực hiện backup theo cú pháp:

    ```bash
    velero backup create vks-full-backup \
      --exclude-namespaces velero \
      --include-cluster-resources=true \
      --wait
    ```

    ```bash
    velero backup describe vks-full-backup --details
    ```

***

## Tại Cluster đích

* Thực hiện restore theo lệnh:

    ```bash
    velero restore create --from-backup vks-full-backup \
        --exclude-resources="MutatingWebhookConfiguration,ValidatingWebhookConfiguration"
    ```

    ```bash
    velero restore create --from-backup vks-full-backup
    ```
