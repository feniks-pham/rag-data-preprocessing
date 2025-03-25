# Cho phép integrate vLB vào dịch vụ Containers của VNG CLOUD

**Nhu cầu:**  Khách hàng có nhu cầu triển khai 2 website: [**httpd.app.com**](http://httpd.app.com/) và [**nginx.app.com**](http://nginx.app.com/) theo kiến trúc microservice trên hạ tầng VNG Cloud.

**Giải pháp:**  Sử dụng dịch vụ vLB(Load Balancer) kết hợp với dịch vụ vContainer trên VNG Cloud.

### **Kiến trúc giải pháp:** <a href="#chophepintegratevlbvaodichvucontainerscuavngcloud-kientrucgiaiphap" id="chophepintegratevlbvaodichvucontainerscuavngcloud-kientrucgiaiphap"></a>

<figure><img src="../../../../../.gitbook/assets/image (473).png" alt=""><figcaption></figcaption></figure>

***

### **Triển khai:** <a href="#chophepintegratevlbvaodichvucontainerscuavngcloud-trienkhai" id="chophepintegratevlbvaodichvucontainerscuavngcloud-trienkhai"></a>

#### **1. Khởi tạo vLB và vContainer** <a href="#chophepintegratevlbvaodichvucontainerscuavngcloud-1.khoitaovlbvavcontainer" id="chophepintegratevlbvaodichvucontainerscuavngcloud-1.khoitaovlbvavcontainer"></a>

1.1 Tạo Network LoadBalancer(Layer 4)

<figure><img src="../../../../../.gitbook/assets/image (474).png" alt=""><figcaption></figcaption></figure>

_Note: Như ở trên, chúng ta sẽ tạo 1 Listener trên Port 80. Nếu muốn sử dụng TLS cho website, có thể tạo thêm Listener trên Port 443 và cấu hình TLS ở LoadBalancer Controller. Bài này sẽ chỉ triển khai với Listener Port 80._

<figure><img src="../../../../../.gitbook/assets/image (476).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (477).png" alt=""><figcaption></figcaption></figure>

1.2 Nhấn **Create Load Balancer** để tạo vLB

1.3 Sau đó truy cập vào bảng điều khiển **tạo K8S** tại đường link: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster):&#x20;

<figure><img src="../../../../../.gitbook/assets/image (478).png" alt=""><figcaption></figcaption></figure>

_Note: Khi tạo vContainer, chúng ta có thể chọn Enable LoadBalancer Controller để tạo cluster với LoadBalancer Controller đã được triển khai sẵn. Để sử dụng LoadBalancer Controller với những tính năng phù hợp theo nhu cầu của ứng dụng, trong bài viết này sẽ không chọn Enable LoadBalancer Controller mà sẽ tự triển khai Nginx LoadBalancer Controller, vì thế bạn cần tắt Ingress Control khi khởi tạo K8S._

1.4 Kiểm tra việc khởi tạo cluster và tải config file để access cluster:

<figure><img src="../../../../../.gitbook/assets/image (480).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (481).png" alt=""><figcaption></figcaption></figure>

#### 2. Triển khai Nginx LoadBalancer Controller <a href="#chophepintegratevlbvaodichvucontainerscuavngcloud-2.trienkhainginxingresscontroller" id="chophepintegratevlbvaodichvucontainerscuavngcloud-2.trienkhainginxingresscontroller"></a>

2.1 Truy cập [https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters](https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters)

<figure><img src="../../../../../.gitbook/assets/image (483).png" alt=""><figcaption></figcaption></figure>

2.2 Copy và chạy command trên để triển khai Nginx LoadBalancer Controller:

<figure><img src="../../../../../.gitbook/assets/image (485).png" alt=""><figcaption></figcaption></figure>

2.3 Kiểm tra:\
→ Như vậy chúng ta đã triển khai thành công Nginx LoadBalancer Controller.

<figure><img src="../../../../../.gitbook/assets/image (486).png" alt=""><figcaption></figcaption></figure>

2.4 Service ingress-nginx-controller được khởi tạo với _Type: NodePort_ và lắng nghe trên Port: 30398, 31873 của các Minion Node.

#### 3. Attach vLB với vContainer <a href="#chophepintegratevlbvaodichvucontainerscuavngcloud-3.attachvlbvoivcontainer" id="chophepintegratevlbvaodichvucontainerscuavngcloud-3.attachvlbvoivcontainer"></a>

_Note: Mặc định vLB không thể kết nối tới vContainer Cluster dù nằm trong cùng VPC/Subnet. Do đó cần tạo mới một Security Group và attach cho Minion Node._

3.1 Tạo Security Group: Do chỉ có 1 Listener Port 80 trên vLB do đó chỉ cần 1 Inbound rule. Trong trường hợp có Listener Port 443, vui lòng tạo thêm Inbound rule.

<figure><img src="../../../../../.gitbook/assets/image (487).png" alt=""><figcaption></figcaption></figure>

3.2 Update Security Group cho Minion Node:\


<figure><img src="../../../../../.gitbook/assets/image (488).png" alt=""><figcaption></figcaption></figure>

3.3 Điền 30398. Khi đó Listener sẽ forward traffic tới Backend Pool với port 30398.\
vLB sẽ định kỳ health check các Pool Member thông qua Monitor Port, traffic sẽ không được gửi tới những member không health check thành công.:

<figure><img src="../../../../../.gitbook/assets/image (489).png" alt=""><figcaption></figcaption></figure>

3.4 Nhấn **Lưu** để hoàn tất attach vLB với vContainer

#### 4. Triển khai ứng dụng <a href="#chophepintegratevlbvaodichvucontainerscuavngcloud-4.trienkhaiungdung" id="chophepintegratevlbvaodichvucontainerscuavngcloud-4.trienkhaiungdung"></a>

4.1 Chuẩn bị YAML file: service.yaml, deployment.yaml và app-ingress.yaml

<figure><img src="../../../../../.gitbook/assets/image (491).png" alt=""><figcaption></figcaption></figure>

4.2 Triển khai:

<figure><img src="../../../../../.gitbook/assets/image (492).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (494).png" alt=""><figcaption></figcaption></figure>

4.3 Kiểm tra\
Review the vLB status:

<figure><img src="../../../../../.gitbook/assets/image (495).png" alt=""><figcaption></figcaption></figure>

4.4 Edit file host trên laptop cá nhân để kiểm tra: _**C:\Windows\System32\drivers\etc\hosts:**_

<figure><img src="../../../../../.gitbook/assets/image (496).png" alt=""><figcaption></figcaption></figure>

4.5 Mở trình duyệt web và kiểm tra:

<figure><img src="../../../../../.gitbook/assets/image (497).png" alt=""><figcaption></figcaption></figure>
