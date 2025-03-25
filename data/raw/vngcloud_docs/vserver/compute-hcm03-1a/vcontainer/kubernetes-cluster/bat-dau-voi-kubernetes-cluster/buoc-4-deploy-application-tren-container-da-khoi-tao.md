# Bước 4: Deploy Application trên Container đã khởi tạo

### **Khởi tạo file Deployment - trường hợp này sử dụng file YAML** <a href="#buoc4-deployapplicationtrencontainerdakhoitao-khoitaofiledeployment-truonghopnaysudungfileyaml" id="buoc4-deployapplicationtrencontainerdakhoitao-khoitaofiledeployment-truonghopnaysudungfileyaml"></a>

1.  Bước đầu, chúng ta sẽ khởi tạo một file YAML để triển khai ứng dụng. File này có tên là "myapp-deploy.yaml" và có nội dung như sau:

    yaml

    | `apiVersion: apps/v1kind: Deploymentmetadata:  # tên của deployment  name: deployappspec:  # số POD tạo ra  replicas: 3` `# thiết lập các POD do deploy quản lý, là POD có nhãn  "app=deployapp"  selector:    matchLabels:      app: deployapp` `# Định nghĩa mẫu POD, khi cần Deploy sử dụng mẫu này để tạo Pod  template:    metadata:      name: podapp      labels:        app: deployapp    spec:      containers:      - name: node        image: ichte/swarmtest:node        resources:          limits:            memory: "128Mi"            cpu: "100m"        ports:          - containerPort: 8085` |
    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
2.  Sau đó, chúng ta sẽ triển khai file YAML này bằng lệnh sau:

    | `kubectl apply -f 1.myapp-deploy.yaml` |
    | -------------------------------------- |
3.  Khi Deployment tạo ra, tên của nó là `deployapp`, để kiểm tra việc triển khai, chúng ta có thể sử dụng lệnh sau:\


    | `kubectl get deploy -o wide` |
    | ---------------------------- |
4.  Deploy này quản sinh ra một ReplicasSet và quản lý nó, gõ lệnh sau để hiện thị các ReplicaSet\


    | `kubectl get rs -o wide` |
    | ------------------------ |
5.  Đến lượt ReplicaSet do Deploy quản lý lại thực hiện quản lý (tạo, xóa) các Pod. Để xem danh sách các Pod, chúng ta có thể sử dụng lệnh:

    | `kubeclt get po -o wide` |
    | ------------------------ |

    \# Hoặc lọc cả label kubectl get po -l "app=deployapp" -o wide

    \
    Ví Dụ: Case deploy APP echo1:\


    <figure><img src="../../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

### **Kiểm tra việc deploy** <a href="#buoc4-deployapplicationtrencontainerdakhoitao-kiemtraviecdeploy" id="buoc4-deployapplicationtrencontainerdakhoitao-kiemtraviecdeploy"></a>

1.  Bạn có thể kiểm tra việc triển khai bằng câu lệnh sau:

    | `kubeclt get po -o wide` |
    | ------------------------ |
2. Kết quả sẽ trả ra

<figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

### **Expose Services Vừa deploy ra ngoài Public**  <a href="#buoc4-deployapplicationtrencontainerdakhoitao-exposeservicesvuadeployrangoaipublic" id="buoc4-deployapplicationtrencontainerdakhoitao-exposeservicesvuadeployrangoaipublic"></a>

1.  Expose dịch vụ để có thể truy cập từ bên ngoài bằng câu lệnh:

    | `kubectl expose deployment deployapp --type=LoadBalancer --port=30309` `--target-port=8085` |
    | ------------------------------------------------------------------------------------------- |

    <figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  Thực hiện Áp dụng cấu hình lên container:\


    <figure><img src="../../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3.  Kiểm tra việc access từ ngoài Internet vào Dịch vụ Echo1 với port 30309:\
    \


    <figure><img src="../../../../../.gitbook/assets/image (472).png" alt=""><figcaption></figcaption></figure>
4. Như vậy đã hoành thành việc khởi tạo Application và Expose ra ngoài internet
