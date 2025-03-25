# Lable và Taint

### Lable <a href="#label" id="label"></a>

Label là một tính năng quan trọng trong Kubernetes, được sử dụng để tổ chức và quản lý các đối tượng một cách hiệu quả. Bạn có thể gán các cặp key-value cho các đối tượng Kubernetes như Pod, Node, Service, Deployment, v.v. Cụ thể:

* **Mỗi Lable là một cặp key-value:** Key (khoá) là một chuỗi ký tự dùng để xác định tên của lable. Value (giá trị) là một chuỗi ký tự tùy chọn, cung cấp thông tin chi tiết về lable.
* **Key và value phải tuân theo các quy tắc đặt tên:** Key và value không được chứa dấu khoảng trắng, ký tự đặc biệt ngoài (-, \_,.).
* Lable có thể được sử dụng cho nhiều mục đích khác nhau, bao gồm:
  * Phân loại các đối tượng dựa trên các tiêu chí như environment, version, status, v.v.
  * Theo dõi và quản lý các đối tượng trong cụm Kubernetes.

**Ví dụ:**

* `app: nginx` - Lable này cho biết đối tượng có liên quan đến ứng dụng Nginx.
* `environment: production` - Lable này cho biết đối tượng thuộc về môi trường production.
* `version: 1.7.2` - Lable này cho biết đối tượng có liên quan đến phiên bản 1.7.2.

### **Tạo Lable**

Để tạo Lable cho một Node Group, bạn hãy thực hiện theo hướng dẫn sau:&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại Cluster đã khởi tạo trước đó, hãy chọn **Create a Node group.**

**Bước 3:** Tại màn hình khởi tạo Node Group, chúng tôi đã thiết lập thông tin cho Node Group của bạn. Bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Node Group của bạn. Tại mục **Node Group Metadata Setting,** bạn cần:

* Nhập key cho lable của bạn. Key phải bắt đầu và kết thúc bằng chữ hoặc số và bao gồm các ký tự a-z, A-Z, 0-9, -, \_, . tối đa 253 ký tự. Ngoài ra bạn có thể nhập key là một DNS subdomain ví dụ:  [example.com/my-app](http://example.com/my-app)
* Nhập value cho key tương ứng này.

**Bước 5:** Chọn **Create Node Group.** Hãy chờ vài phút để chúng tôi khởi tạo Node Group của bạn, trạng thái của Node Group lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Node Group** là **Active**, bạn có thể xem thông tin Node Group bằng cách chọn vào **Node Group Name** tại màn hình chính.

Hoặc bạn có thể tạo Lable thông qua kubectl theo câu lệnh:

```
kubectl label nodes my-node1 disktype=ssd
```

Bạn có thể kiểm tra lại lable vừa tạo qua lệnh:

```
kubectl get nodes --show-labels
```

Ví dụ kết quả cho lệnh này sẽ như sau:

```shell
NAME      STATUS    ROLES    AGE     VERSION        LABELS
worker0   Ready     <none>   1d      v1.13.0        ...,disktype=ssd,kubernetes.io/hostname=worker0
worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
```

### **Sử dụng Lable với nodeSelector**

nodeSelector là một tham số được sử dụng trong PodSpec để chỉ định rằng Pod chỉ nên được lên lịch trên các Node có lable cụ thể. Điều này hữu ích khi bạn muốn chạy Pod trên các Node có tài nguyên hoặc thuộc tính cụ thể.

* Tạo tệp tin **my-pod.yaml** chứa nội dung như sau:&#x20;

```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  nodeSelector:
    disktype: ssd
    region: hcm03
```

Trong ví dụ này, Pod `my-pod` chỉ được lên lịch trên các Node có lable `disktype: ssd` và `region: hcm03`.

* Triển khai Pod trên Cluster của bạn:

```
kubectl -f apply my-pod.yaml
```

***

### Taint

Taint là một tính năng quan trọng trong Kubernetes, đóng vai trò như một cơ chế để đánh dấu các Node và kiểm soát việc lên lịch Pod trên những Node đó. Khác với Label thông thường, Taint được sử dụng để chỉ định các thuộc tính đặc biệt của Node và thực thi các hành động cụ thể khi Pod không đáp ứng các điều kiện được xác định bởi Taint. Cụ thể:&#x20;

&#x20;Cụ thể:

* **Mỗi Taint bao gồm:**
  * Key (khoá) là một chuỗi ký tự dùng để xác định tên của taint.&#x20;
  * Value (giá trị) là một chuỗi ký tự tùy chọn, cung cấp thông tin chi tiết về taint.
  * Effect:&#x20;
    * **NoSchedule:** Ngăn Pod không có Toleration tương ứng được lên lịch trên Node.
    * **NoExecute:** Cho phép Pod được lên lịch trên Node nhưng Pod sẽ không được thực thi.
    * **PreferNoSchedule:** Kubernetes sẽ cố gắng ưu tiên không lên lịch Pod lên Node có Taint này.
* **Key và value phải tuân theo các quy tắc đặt tên:** Key và value không được chứa dấu khoảng trắng, ký tự đặc biệt ngoài (-, \_,.).
* **Toleration:** Để Pod có thể được lên lịch và chạy trên Node có Taint, Pod cần có Toleration tương ứng. Toleration được khai báo trong PodSpec bằng cách sử dụng `tolerations` field. Ví dụ:&#x20;

```
tolerations: - key: node.role.kubernetes.io/master effect: NoSchedule
```

* **Mối quan hệ giữa Taint và Toleration:** Khi Kubernetes lên lịch Pod, Kubernetes sẽ so khớp các Taint của Node với các Toleration của Pod. Pod chỉ được lên lịch trên Node nếu có Toleration cho tất cả các Taint của Node đó.

**Ví dụ:**

* node.role.kubernetes.io/master:NoSchedule - ngăn các Pod thông thường được chạy trên Node này.

### **Tạo Taint**

Để tạo Taint cho một Node Group, bạn hãy thực hiện theo hướng dẫn sau:&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại Cluster đã khởi tạo trước đó, hãy chọn **Create a Node group.**

**Bước 3:** Tại màn hình khởi tạo Node Group, chúng tôi đã thiết lập thông tin cho Node Group của bạn. Bạn có thể giữ các giá trị mặc định này hoặc điều chỉnh các thông số mong muốn cho Node Group của bạn. Tại mục **Node Group Metadata Setting,** bạn cần:

* Nhập key cho taint của bạn. Key phải bắt đầu và kết thúc bằng chữ hoặc số và bao gồm các ký tự a-z, A-Z, 0-9, -, \_, . tối đa 253 ký tự. Ngoài ra bạn có thể nhập key là một DNS subdomain ví dụ:  [example.com/my-app](http://example.com/my-app)
* Nhập value cho key tương ứng này.
* Chọn 1 trong 3 loại effect: **NoSchedule, NoExecute, PreferNoSchedule.**

**Bước 5:** Chọn **Create Node Group.** Hãy chờ vài phút để chúng tôi khởi tạo Node Group của bạn, trạng thái của Node Group lúc này là **Creating**.

**Bước 6:** Khi trạng thái **Node Group** là **Active**, bạn có thể xem thông tin Node Group bằng cách chọn vào **Node Group Name** tại màn hình chính.

Hoặc bạn có thể tạo Taint thông qua kubectl theo câu lệnh:

```
kubectl taint node my-node node.role.kubernetes.io/master:NoSchedule.
```

**Ví dụ sử dụng Taint:**

Giả sử bạn có một Node `master` được sử dụng cho mục đích quản lý và bạn muốn ngăn các Pod thông thường được chạy trên Node này. Bạn có thể sử dụng Taint như sau:

```
kubectl taint node my-master node.role.kubernetes.io/master:NoSchedule
```

Để Pod có thể chạy trên Node `master`, Pod cần có Toleration tương ứng:

```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  tolerations:
  - key: node.role.kubernetes.io/master
    effect: NoSchedule
```
