# Sử dụng PersistentVolumeClaim

#### **1. Chuẩn bị yaml file để sử dụng PVC**  <a href="#sudungpersistentvolumeclaim-1.chuanbiyamlfiledesudungpvc" id="sudungpersistentvolumeclaim-1.chuanbiyamlfiledesudungpvc"></a>

_web-deployment.yaml_&#x20;

\---&#x20;

| `apiVersion:` `apps/v1 kind:` `Deployment metadata:` `name:` `web-deployment spec:` `replicas:` `1   selector:` `matchLabels:` `app:` `nginx   template:` `metadata:` `labels:` `app:` `nginx     spec:` `volumes:` `- name:` `nginx-volume         persistentVolumeClaim:` `claimName:` `nginx-pv           readOnly:` `false` `containers:` `- image:` `nginx         imagePullPolicy:` `IfNotPresent         name:` `web-app         ports:` `- containerPort:` `80           protocol:` `TCP         volumeMounts:` `- mountPath:` `/usr/share/nginx/html           name:` `nginx-volume`  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### 2. Triển khai ứng dụng  <a href="#sudungpersistentvolumeclaim-2.trienkhaiungdung" id="sudungpersistentvolumeclaim-2.trienkhaiungdung"></a>

\# kubectl  apply  -f  web-deployment.yaml&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804492/image2023-4-26_13-37-26.png?version=1&#x26;modificationDate=1687415894000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804492/image2023-4-26_13-37-15.png?version=1&#x26;modificationDate=1687415894000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

&#x20;**Kiểm tra:**&#x20;

* Access vào container và tạo file&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804492/image2023-4-26_13-38-11.png?version=1&#x26;modificationDate=1687415894000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

&#x20;\# kubectl exec -it  web-deployment-859679cc57-v8kw4 bash&#x20;

* **Xóa deployment** &#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804492/image2023-4-26_13-27-42.png?version=1&#x26;modificationDate=1687415895000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\# kubectl delete -f web-deployment.yaml&#x20;

* **Tạo lại deployment: khi này hệ thống sẽ tạo ra Pod, Container mới**&#x20;

\# kubectl apply  -f web-deployment.yaml&#x20;

&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804492/image2023-4-26_13-28-47.png?version=1&#x26;modificationDate=1687415895000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Access vào container mới để kiểm tra dữ liệu trên PersistentVolume có bị mất không**&#x20;

\# kubectl exec -it  web-deployment-859679cc57-tglfg  bash&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804492/image2023-4-26_13-39-46.png?version=1&#x26;modificationDate=1687415895000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

&#x20;\=> Có thể thấy ở đây, dữ liệu trên Persistent Volume không bị mất.&#x20;

\
