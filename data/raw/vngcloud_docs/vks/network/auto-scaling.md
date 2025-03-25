# Auto Scaling

## Tổng quan

Tính năng Auto Scaling cho phép vLB tự động điều chỉnh số lượng Slave dựa trên lưu lượng truy cập, giúp tối ưu hóa hiệu suất và chi phí. Auto Scaling giúp bạn:

* **Tối ưu hóa hiệu suất:** Đảm bảo vLB luôn có đủ tài nguyên để xử lý lưu lượng truy cập, tránh tình trạng quá tải.
* **Tiết kiệm chi phí:** Tự động giảm số lượng LB khi lưu lượng thấp, hoặc tăng số lượng LB khi lưu lượng tăng, giúp bạn tiết kiệm và tối ưu chi phí một cách tốt nhất.
* **Đơn giản hóa quản lý:** Không cần phải theo dõi và điều chỉnh quy mô vLB thủ công.

## **Bật/ Tắt Auto Scaling**

* Auto Scaling **chỉ có thể được bật khi khởi tạo vLB** và **không thể tắt** sau đó. Nếu bạn khởi tạo LoadBalancer thông qua vLB Portal, hãy chọn option: **Enable auto scaling**.

<figure><img src="../../.gitbook/assets/image.png" alt="" width="196"><figcaption></figcaption></figure>

* Nếu LoadBalancer của bạn được khởi tạo tự động thông qua hệ thống VKS, vui lòng thêm annotation `vks.vngcloud.vn/enable-autoscale: true` ngay khi tạo service LoadBalancer hay Ingress với Class vngcloud. Việc cập nhật annotation này sau khi LoadBalancer này đã được tạo sẽ không có tác dụng. Ví dụ:

```yaml
// For NLB
apiVersion: apps/v1
kind: Deployment
metadata:
  name: external-http-nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
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
---
kind: Service
apiVersion: v1
metadata:
  name: external-http-nginx-service
  annotations:
    vks.vngcloud.vn/enable-autoscale: true
spec:
  selector:
    app: nginx
  type: LoadBalancer
  ports:
  - name: http
    port: 80
    targetPort: 80
```

```yaml
// For ALB
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    vks.vngcloud.vn/enable-autoscale: true
spec:
  ingressClassName: "vngcloud"
  defaultBackend:
    service:
      name: apache-service
      port:
        number: 80
  tls:
    - hosts:
        - host.example.com
  rules:
    - host: host.example.com
      http:
        paths:
          - path: /4
            pathType: Exact
            backend:
              service:
                name: nginx-service
                port:
                  number: 80
```

## **Chính sách Auto Scaling**

* Chính sách dựa trên tỷ lệ phần trăm kết nối đang hoạt động (active connection) so với giới hạn kết nối tối đa (max connection).
  * **Scaling out (Mở rộng):**
    * Khi đạt ngưỡng 80% active connection/max connection trong 3 phút liên tục, hệ thống sẽ tự động thêm 1 LB thành viên.
  * **Scaling in (Thu hẹp):**
    * Khi ngưỡng giảm xuống dưới 20% active connection/max connection trong 3 phút liên tục, hệ thống sẽ tự động xóa 1 LB thành viên.

{% hint style="info" %}
**Chú ý:**

* **Tính năng Resize bị vô hiệu hóa:** Đối với các vLB đã bật Auto Scaling, bạn không thể thay đổi gói dịch vụ (resize) thủ công.
* **Trạng thái Scaling:** Trong quá trình mở rộng hoặc thu hẹp quy mô LB, trạng thái của LB sẽ chuyển từ "Active" sang "Scaling in/Scaling out". Sau khi hoàn tất, trạng thái sẽ trở lại "Active".
* **Thời gian Scaling:** Thời gian để scale lên hoặc xuống 1 LB role Slave là khoảng 5-10 phút, kể từ thời điểm connection vượt ngưỡng cho phép, tùy thuộc vào số lượng listener của LB đó.
* **Phân giải CNAME**: Đối với các LB bật tính năng auto scale, hệ thống sẽ tự động tạo tên miền cho cụm LB theo template `lb_name-{userid}.{region}.vlb.vngcloud.vn`. Sau đó, người dùng cần chủ động cập nhật bản ghi CNAME để trỏ tên miền riêng đến tên miền của LB. Khi có sự thay đổi về số lượng LB slave (scale up/down), hệ thống sẽ tự động cập nhật bản ghi DNS tương ứng với tên miền LB.
{% endhint %}

## **Xem lịch sử Scaling**

* Truy cập trang chi tiết của LB .
* Chọn tab "Scale History" để xem lịch sử các lần mở rộng/thu hẹp quy mô và số lượng LB thành viên hiện tại. Giải thích ý nghĩa các trường thông tin như sau
  * **Event type:** Hành động Scale in hoặc Scale out
  * **Adjustment number:** Số lượng LB thành viên sẽ thay đổi. Ví dụ Adjustment number là 1, Event type là Scale out, thì hành động Scale out này sẽ scale thêm 1 LB thành viên vào cụm LB
  * **Total number:** Số lượng LB sau khi scale
  * **Scale at:** Thời gian hoàn tất quá trình scale.
