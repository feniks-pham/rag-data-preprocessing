# Tự động quản lý Certificate trong VKS với Nginx Ingress Controller, Cert-Manager, và Let's Encrypt

## Điều kiện cần <a href="#dieu-kien-can" id="dieu-kien-can"></a>

* Bạn đã thực hiện khởi tạo Cluster trên hệ thống VKS theo các hướng dẫn tại [đây ](https://docs.vngcloud.vn/vng-cloud-document/vn/vks/bat-dau-voi-vks/expose-mot-service-thong-qua-vlb-layer4)và trên cụm của bạn đã được cài đặt **VNGCloud LoadBalancer Controller.**
* Tiếp theo, hãy đảm bảo bận có một **domain** đã được đăng ký và sử dụng.
* Cuối cùng, bạn cần một địa chỉ **email** để thực hiện kiểm tra việc quản lý Certificate.
* Tiếp theo, bạn cần thực hiện cài đặt nginx-ingress-controller theo lệnh:

```bash
helm install nginx-ingress-controller oci://ghcr.io/nginxinc/charts/nginx-ingress --namespace kube-system
```

***

## **Cài đặt Cert-Manager**

**Cert-Manager** chịu trách nhiệm tự động cấp phát và gia hạn chứng chỉ từ **Let's Encrypt.**

* Sử dụng **Helm** để cài đặt Cert-Manager qua lệnh:

```bash
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.16.2 \
  --set crds.enabled=true

```

***

## **Các bước thực hiện**

### **Deploy sample app**

Bạn hãy thực hiện deploy một sample app, ví dụ:

```bash
kubectl create deployment echo-server --image=mccutchen/go-httpbin
kubectl expose deployment echo-server --name=clusterip --port=80 --target-port=8080 --type=ClusterIP
```

### **Cấu hình Issuer**

Issuer là thành phần giúp Cert-Manager giao tiếp với Let's Encrypt để cấp phát chứng chỉ.

<details>

<summary>Thử nghiệm trên môi trường STAGING</summary>

1.  Tạo file `letsencrypt-issuer.yaml`:

    ```yaml
    apiVersion: cert-manager.io/v1
    kind: Issuer
    metadata:
      name: letsencrypt-staging
    spec:
      acme:
        server: https://acme-staging-v02.api.letsencrypt.org/directory
        email:  ______________________ # Change to your email
        privateKeySecretRef:
          name: letsencrypt-staging
        solvers:
          - http01:
              ingress:
                ingressClassName: nginx
    ```
2.  Thực hiện tạo Issuer trên cụm VKS qua lệnh:

    ```bash
    kubectl apply -f letsencrypt-issuer.yaml
    ```
3.  Kiểm tra Issuer qua lệnh:

    ```bash
    kubectl describe issuer letsencrypt-staging
    ```

4)  Kết quả trả về như sau:

    ```bash
    Status:
      Acme:
        Uri:  https://acme-staging-v02.api.letsencrypt.org/acme/acct/...
      Conditions:
        Last Transition Time:  ...
        Message:               The ACME account was registered with the ACME server
        Reason:                ACMEAccountRegistered
        Status:                True
        Type:                  Ready
    ```
5)  Tiếp tục thực hiện deploy ingress, thay đổi domain của bạn trong file yaml bên dưới:&#x20;

    ```bash
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: go-httpbin
      annotations:
        cert-manager.io/issuer: "letsencrypt-staging"
        acme.cert-manager.io/http01-edit-in-place: "true"
    spec:
      ingressClassName: nginx
      tls:
      - hosts:
        - ______________________ # Change to your domain
        secretName: quickstart-example-tls
      rules:
      - host: ______________________ # Change to your domain
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: clusterip
                port:
                  number: 80
    ```
6)  Kiểm tra certificate qua lệnh:

    ```bash
    kubectl get certificate

    NAME                     READY   SECRET                   AGE
    quickstart-example-tls   True    quickstart-example-tls   16m     # Ready should be True
    ```
7)  Kiểm tra thông tin chi tiết certificate:

    ```bash
    kubectl describe certificate quickstart-example-tls

    Name:         quickstart-example-tls
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>
    API Version:  cert-manager.io/v1
    Kind:         Certificate
    Metadata:
      Cluster Name:
      Creation Timestamp:  2018-11-17T17:58:37Z
      Generation:          0
      Owner References:
        API Version:           networking.k8s.io/v1
        Block Owner Deletion:  true
        Controller:            true
        Kind:                  Ingress
        Name:                  kuard
        UID:                   a3e9f935-ea87-11e8-82f8-42010a8a00b5
      Resource Version:        9295
      Self Link:               /apis/cert-manager.io/v1/namespaces/default/certificates/quickstart-example-tls
      UID:                     68d43400-ea92-11e8-82f8-42010a8a00b5
    Spec:
      Dns Names:
        www.example.com
      Issuer Ref:
        Kind:       Issuer
        Name:       letsencrypt-staging
      Secret Name:  quickstart-example-tls
    Status:
      Acme:
        Order:
          URL:  https://acme-staging-v02.api.letsencrypt.org/acme/order/...
      Conditions:
        Last Transition Time:  2018-11-17T18:05:57Z
        Message:               Certificate issued successfully
        Reason:                CertIssued
        Status:                True
        Type:                  Ready
    Events:
      Type     Reason          Age                From          Message
      ----     ------          ----               ----          -------
      Normal   CreateOrder     9m                 cert-manager  Created new ACME order, attempting validation...
      Normal   DomainVerified  8m                 cert-manager  Domain "www.example.com" verified with "http-01" validation
      Normal   IssueCert       8m                 cert-manager  Issuing certificate...
      Normal   CertObtained    7m                 cert-manager  Obtained certificate from ACME server
      Normal   CertIssued      7m                 cert-manager  Certificate issued Successfully

    ```
8)  Kiểm tra kết nối đến domain qua lệnh:

    ```bash
    curl -kivL -H 'Host: ______DOMAIN______' 'http://_____IP_____'
    ```

    &#x20;
9)  Bạn cũng có thể thực hiện xóa các resource thử nghiệm qua lệnh:

    ```bash
    kubectl delete ingress go-httpbin
    kubectl delete issuer letsencrypt-staging
    kubectl delete secret quickstart-example-tls
    kubectl delete secret letsencrypt-staging
    ```

</details>

<details>

<summary>Thực hiện trên môi trường PRODUCTION</summary>

1.  Tạo file `letsencrypt-issuer.yaml`:

    ```yaml
    apiVersion: cert-manager.io/v1
    kind: Issuer
    metadata:
      name: letsencrypt-prod
    spec:
      acme:
        server: https://acme-v02.api.letsencrypt.org/directory
        email: ______________________ # Change to your email
        privateKeySecretRef:
          name: letsencrypt-prod
        solvers:
          - http01:
              ingress:
                ingressClassName: nginx
    ```
2.  Thực hiện tạo Issuer trên cụm VKS qua lệnh:

    ```bash
    kubectl apply -f letsencrypt-issuer.yaml
    ```
3.  Kiểm tra Issuer qua lệnh:

    ```bash
    kubectl describe issuer letsencrypt-prod
    ```

4)  Tiếp tục thực hiện deploy ingress, thay đổi domain của bạn trong file yaml bên dưới:&#x20;

    ```bash
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: go-httpbin
      annotations:
        cert-manager.io/issuer: "letsencrypt-prod"  # Change to letsencrypt-prod
        acme.cert-manager.io/http01-edit-in-place: "true"
    spec:
      ingressClassName: nginx
      tls:
      - hosts:
        - ______________________ # Change to your domain
        secretName: quickstart-example-tls
      rules:
      - host: ______________________ # Change to your domain
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: clusterip
                port:
                  number: 80
    ```

</details>
