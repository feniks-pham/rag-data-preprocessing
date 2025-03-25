# Tạo PersistentVolume(PV) và PersistentVolumeClaim(PVC)

Để sử dụng được PersistentVolume(PV) và PersistentVolumeClaim(PVC) điều cần làm là tạo mới, sử dụng hướng dẫn bên dưới để bắt đầu với việc tạo mới một PersistentVolume(PV) và PersistentVolumeClaim(PVC):

#### **1. Chuẩn bị yaml file để tạo PV và PVC**  <a href="#taopersistentvolume-pv-vapersistentvolumeclaim-pvc-1.chuanbiyamlfiledetaopvvapvc" id="taopersistentvolume-pv-vapersistentvolumeclaim-pvc-1.chuanbiyamlfiledetaopvvapvc"></a>

_**nginx-pvc.yaml**_**&#x20;---** \


| `piVersion:` `v1` `kind:` `PersistentVolumeClaim` `metadata:`  `name:` `nginx-pvc` `spec:`  `accessModes:`  `- ReadWriteOnce` `resources:`  `requests:`  `storage:` `2Gi`  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### **2. Tạo PV và PVC**  <a href="#taopersistentvolume-pv-vapersistentvolumeclaim-pvc-2.taopvvapvc" id="taopersistentvolume-pv-vapersistentvolumeclaim-pvc-2.taopvvapvc"></a>

\# kubectl apply -f nginx-pvc.yaml &#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804471/image2023-4-26_13-34-33.png?version=1&#x26;modificationDate=1687415316000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804471/image2023-4-26_13-35-23.png?version=1&#x26;modificationDate=1687415316000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Khi này PV sẽ tự động được tạo ra và sẽ thuộc StorageClass: csi-sc-cinderplugin-ssd do VNG Cloud đã defined sẵn với thông tin của volume: SSD-IOPS-3000

#### **3. Kiểm tra trên VNG Cloud portal** <a href="#taopersistentvolume-pv-vapersistentvolumeclaim-pvc-3.kiemtratrenvngcloudportal" id="taopersistentvolume-pv-vapersistentvolumeclaim-pvc-3.kiemtratrenvngcloudportal"></a>

Sau đó truy cập vào bảng điều khiển Persistent Volume để kiểm tra thông tin vừa tạo mới tại đường link: [https://hcm-3.console.vngcloud.vn/vserver/container/persistent-volumes](https://hcm-3.console.vngcloud.vn/vserver/container/persistent-volumes)

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804471/image2023-6-22_13-57-47.png?version=1&#x26;modificationDate=1687417068000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
