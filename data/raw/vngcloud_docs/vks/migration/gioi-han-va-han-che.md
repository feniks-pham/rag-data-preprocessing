# Giới hạn và hạn chế

Khi sử dụng Velero để migrate Cluster to Cluster, bạn có thể thêm các tùy chọn sau.&#x20;

## Đánh dấu các Volume bạn muốn backup và các resource không cần thiết

Để đánh dấu các Volume bạn muốn backup và các resource không cần thiết, đầu tiên bạn cần tài xuống đoạn helper bash script được chung tôi cung cấp sẵn và thực hiện grand execute permission. Chi tiết file mấu bạn có thể xem tại: [velero\_helper.sh](https://raw.githubusercontent.com/vngcloud/velero/main/velero\_helper.sh)

### 1. Chuyển hostPath Volume thành Persistent Volume để có thể thực hiện backup

Do Velero không hỗ trợ sao lưu hostPath Volume, bạn cần phải chuyển hostPath Volume thành Persistent Volume theo hướng dẫn sau đây:

* Để list các hostPath Volume đang sử dụng:

  ```bash
  ./helper.sh check_hostPath
  ```

### 2. Mark Persistent Volume to include in backup

Tất cả data Persistent Volumes được lưu trữ trên vStorage. Cần thêm annotation cho tất cả pod dùng PV với volume name: `backup.velero.io/backup-volumes=volume1,volume2`

* Hoặc có thể tự động tìm các volume bằng cách:

  ```bash
  ./helper.sh mark_volume
  ```

### 3. Mark resource in exclude in backup

Do VKS hoạt động theo cơ chế Fully Managed Control Plane, nên bạn không cần backup các resource như: `calico`, `kube-dns`, `kube-scheduler`, `kube-apiserver`,... Ngoài ra, các resource của vContainer như là: `magnum-auto-healer`, `cluster-autoscaler`, `csi-cinder`,... cũng sẽ được bỏ qua.

* Đánh dầu resource không cần backup thông qua lệnh:

  ```bash
  ./helper.sh mark_exclude
  ```

### 4. Check label and taint of node

Khi thực hiện migrate, có thể tài nguyên trong Cluster nguồn đang sử dụng label và taint. Bạn cần đảm bảo các label và taint quan trọng này tồn tại trong Cluster đích.

* Kiểm tra lable và taint thông qua lệnh:

  ```bash
  ./helper.sh check_node_label
  ./helper.sh check_node_taint
  ```

### 5. Mapping Storage Class

* Nếu Storage Class của bạn khác nhau giữa Cluster nguồn và Cluster đích, bạn cần chuyển Storage Class giữa 2 cụm. Ví dụ:
  * Tại Cluster nguồn, bạn đang có 2 Storage Class sau:

    ```bash
    @ kubectl get sc
    NAME                            PROVISIONER       RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
    sc-iops-200-retain (default)    csi.vngcloud.vn   Retain          Immediate           true                   81s
    sc-ssd-10000-delete (default)   csi.vngcloud.vn   Delete          Immediate           true                   14d
    ```

* Bạn có thể tạo file mapping chưa nội dung như ví dụ bên dưới để thực hiện chuyển đổi 2 storage class từ Cluster nguồn thành 2 storage class tại Cluster đích. File này phải được apply tại Cluster đích trước khi bạn chạy lệnh backup:

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
    sc-iops-200-retain: ssd-200
    sc-ssd-10000-delete: ssd-10000
  ```
