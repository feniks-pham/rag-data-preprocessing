# Cấu hình cho một Application Load Balancer

Tại trang \[Ingress for an Application Load Balancer], chúng tôi đã hướng dẫn bạn cách thực hiện cài đặt VNGCloud LoadBalancer Controller và tạo ingress thông qua Ingress Yaml file. Sau đây là chi tiết các ý nghĩa các thông tin bạn có thể thiết lập cho một Ingress

### Annotation <a href="#configureforanapplicationloadbalancer-annotation" id="configureforanapplicationloadbalancer-annotation"></a>

Sử dụng các annotation dưới đây khi thực thiện tạo ingress để tuỳ chỉnh Load Balancer phù hợp với nhu cầu của bạn:

<table data-full-width="true"><thead><tr><th width="167">Annotation</th><th width="230">Bắt buộc/ Không bắt buộc</th><th>Ý nghĩa</th></tr></thead><tbody><tr><td>vks.vngcloud.vn/load-balancer-id</td><td>Không bắt buộc</td><td><ul><li><strong>Nếu bạn chưa có sẵn một Application Load Balancer</strong> đã khởi tạo trước đó trên hệ thống vLB. Lúc này, khi tạo một Ingress, bạn hãy để trống thông tin này. Sau khi bạn đã thực hiện triển khai Ingress theo hướng dẫn tại <a href="https://docs.vngcloud.vn/display/VKSVI/Ingress+for+an+Application+Load+Balancer">Ingress for an Application Load Balancer</a>. Chúng tôi sẽ tự động tạo 1 ALB trên cluster của bạn. ALB này sẽ hiển thị trên vLB Portal, chi tiết truy cập tại <a href="https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb">đây</a></li><li><p><strong>Nếu bạn đã có sẵn một Application Load Balancer</strong> đã khởi tạo trước đó trên hệ thống vLB và bạn muốn tái sử dụng ALB cho cluster của bạn. Lúc này, khi tạo một Ingress, bạn hãy nhập thông tin Load Balancer ID vào annotation này. Sau khi bạn đã thực hiện tạo Ingress theo hướng dẫn tại <a href="https://docs.vngcloud.vn/display/VKSVI/Ingress+for+an+Application+Load+Balancer">Ingress for an Application Load Balancer</a>. Nếu:</p><ul><li><p>ALB của bạn đang có sẵn 2 listener trong đó:</p><ul><li>1 listener có cấu hình protocol HTTP và port 80</li><li>1 listener có cấu hình protocol HTTPS và port 443 thì chúng tôi sẽ sử dụng 2 listener này.</li></ul></li><li>ALB của bạn chưa có một trong hai hoặc cả 2 listener có cấu hình trên, chúng tôi sẽ tự động khởi tạo chúng.</li></ul></li></ul><p>Chú ý:</p><p>Nếu ALB của bạn có:</p><ul><li>1 listener có cấu hình protocol HTTP và port 443</li><li>Hoặc 1 listener có cấu hình protocol HTTPS và portal 80</li></ul><p>thì khi tạo Ingress sẽ xảy ra lỗi. Lúc này, bạn cần chỉnh sửa lại thông tin listener hợp lệ trên hệ thống vLB và thực hiện tạo lại ingress.</p></td></tr><tr><td>vks.vngcloud.vn/load-balancer-name</td><td>Không bắt buộc</td><td><ul><li>Annotation <code>vks.vngcloud.vn/load-balancer-name</code> sẽ được sử dụng nếu bạn <strong>không</strong> sử dụng annotation <code>load-balancer-id</code>.</li><li>Annotation <code>vks.vngcloud.vn/load-balancer-name</code> <strong>chỉ có ý nghĩa</strong> khi bạn tạo mới một Ingress resource. Sau khi Ingress resource được tạo thành công, annotation này <strong>sẽ tự động bị xóa</strong>. Việc sử dụng annotation này sau khi Ingress resource được tạo sẽ <strong>không có tác dụng</strong>.</li><li><strong>Khi bạn sử dụng annotation này, nếu bạn chưa có sẵn một Application Load Balancer</strong> đã khởi tạo trước đó trên hệ thống vLB. Chúng tôi sẽ tự động tạo 1 ALB trên cluster của bạn. ALB này sẽ hiển thị trên vLB Portal, chi tiết truy cập tại <a href="https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb">đây</a></li><li><strong>Nếu bạn đã có sẵn một Application Load Balancer</strong> đã khởi tạo trước đó trên hệ thống vLB và bạn muốn tái sử dụng ALB cho cluster của bạn. Lúc này, bạn hãy nhập thông tin Load Balancer Name vào annotation này.</li></ul></td></tr><tr><td>vks.vngcloud.vn/package-id</td><td>Không bắt buộc</td><td><ul><li>Nếu bạn không nhập thông tin này thì mặc định chúng tôi sẽ sử dụng cấu hình <strong>ALB Small.</strong></li><li>Nếu bạn đã có sẵn host vLB đang ACTIVE và bạn muốn tích hợp host này vô cụm K8S của bạn, vui lòng bỏ qua trường thông tin này.</li></ul></td></tr><tr><td>vks.vngcloud.vn/tags</td><td>Không bắt buộc</td><td><ul><li>Tag được gắn thêm cho ALB của bạn.</li></ul></td></tr><tr><td>vks.vngcloud.vn/scheme</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>internet-facing</strong>, bạn có thể đổi thành <strong>internal</strong> tùy theo nhu cầu sử dụng.</li></ul></td></tr><tr><td>vks.vngcloud.vn/security-groups</td><td>Không bắt buộc</td><td><ul><li>Mặc định sẽ tạo một <strong>security group default</strong> theo Cluster của bạn.</li></ul></td></tr><tr><td>vks.vngcloud.vn/inbound-cidrs</td><td>Không bắt buộc</td><td><ul><li>Mặc định All CIRD: <strong>0.0.0.0/0</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/healthy-threshold-count</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>3</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/unhealthy-threshold-count</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>3</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-interval-seconds</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>30</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-timeout-seconds</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>5</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-protocol</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>TCP</strong>. Người dùng có thể chọn một trong các giá trị TCP/ HTTP</li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-http-method</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>GET</strong>. Người dùng có thể chọn một trong các giá trị GET / POST / PUT</li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-path</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>/</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-http-version</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>1.0</strong>. Người dùng có thể chọn một trong các giá trị 1.0, 1.1</li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-http-domain-name</td><td>Không bắt buộc</td><td><ul><li>Mặc định trống</li></ul></td></tr><tr><td>vks.vngcloud.vn/healthcheck-port</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>traffic port</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/success-codes</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>200</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/idle-timeout-client</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>50</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/idle-timeout-member</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>50</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/idle-timeout-connection</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>5</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/pool-algorithm</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>ROUND_ROBIN</strong>. Người dùng có thể chọn một trong các giá trị ROUND_ROBIN / LEAST_CONNECTIONS / SOURCE_IP</li></ul></td></tr><tr><td>vks.vngcloud.vn/enable-sticky-session</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>false</strong>.</li></ul></td></tr><tr><td>vks.vngcloud.vn/enable-tls-encryption</td><td>Không bắt buộc</td><td><ul><li>Mặc định <strong>false</strong></li></ul></td></tr><tr><td>vks.vngcloud.vn/target-node-labels</td><td>Không bắt buộc</td><td><ul><li>Mặc định trống</li></ul></td></tr><tr><td>vks.vngcloud.vn/certificate-ids</td><td>Không bắt buộc</td><td><ul><li>Mặc định trống</li></ul></td></tr><tr><td>vks.vngcloud.vn/is-poc</td><td>Không bắt buộc</td><td><ul><li>Mặc định false.</li><li>Nếu người dùng chỉ định field này là true, hệ thống sẽ tạo Load Balancer và thực hiện thanh toán bởi số dư ví POC.</li></ul></td></tr><tr><td>vks.vngcloud.vn/enable-autoscale</td><td>Không bắt buộc</td><td><ul><li>Mặc định false.</li><li>Nếu người dùng chỉ định field này là true, hệ thống sẽ tạo Load Balancer với mode autoscale được bật.</li></ul></td></tr><tr><td>vks.vngcloud.vn/ignore</td><td>Không bắt buộc</td><td><ul><li>Mặc định false.</li><li>Nếu người dùng chỉ định field này là false, operator của chúng tối sẽ không quản lý Service và Ingress. Mọi thay đổi đối với resource sẽ bị bỏ qua và LoadBalancer sẽ không được cập nhật.</li></ul></td></tr><tr><td>vks.vngcloud.vn/implementation-specific-params</td><td>Không bắt buộc</td><td><ul><li>Mặc định trống</li><li>Theo mặc định, <strong>ALB policy</strong> chỉ có 1 rule dành cho host và path, với các thao tác giới hạn như <strong>EQUAL_TO</strong> <strong>(Exact)</strong> và <strong>START_WITH (Prefix)</strong>. Nếu người dùng muốn tạo thêm policy hoặc sử dụng các thao tác khác như <strong>ENDS_WITH</strong> hoặc <strong>REGEX</strong>, cần thay đổi <strong>pathType</strong> thành <strong>ImplementationSpecificParams</strong> và sử dụng <strong>annotation</strong> với giá trị JSON để cấu hình. Ví dụ:</li></ul><pre class="language-json"><code class="lang-json">[{
  "path": "/haha",
  "rules": [
    {
      "type": "PATH",
      "compare": "EQUAL_TO",
      "value": "/foo#"
    },
    {
      "type": "PATH",
      "compare": "REGEX",
      "value": "/foo#anchor"
    }
  ],
  "action": {
    "action": "REJECT",
    "redirectUrl": "http://golang.cafe/a",
    "redirectHttpCode": 301
  }
}]
</code></pre></td></tr><tr><td>vks.vngcloud.vn/header</td><td>Không bắt buộc</td><td><ul><li>Mặc định: {"http":["X-Forwarded-For", "X-Forwarded-Proto", "X-Forwarded-Port"],"https":["X-Forwarded-For", "X-Forwarded-Proto", "X-Forwarded-Port"]}</li></ul></td></tr><tr><td>vks.vngcloud.vn/client-certificate-id</td><td>Không bắt buộc</td><td><ul><li>Mặc định trống</li><li><strong>Client CA</strong> là một tính năng bảo mật của <strong>Load Balancer</strong> giúp xác thực client bằng cách sử dụng <strong>client certificate</strong> để cho phép các client được ủy quyền truy cập vào ứng dụng hoặc dịch vụ. Truyền một <strong>certificate id</strong> trong <strong>portal</strong> vào <strong>annotation</strong> này sẽ kích hoạt <strong>Client CA</strong> cho <strong>https listener</strong>.</li></ul></td></tr></tbody></table>

***

### IngressClassName <a href="#configureforanapplicationloadbalancer-ingressclassname" id="configureforanapplicationloadbalancer-ingressclassname"></a>

Các Ingress được cài đặt bởi các VNGCloud LoadBalancer Controller sẽ có thông tin IngressClassName = "vngcloud". Bạn không được thay đổi thông tin này.

***

### DefaultBackend

* Một Ingress không có rule nào sẽ gửi tất cả traffic đến 1 service default backend mặc định duy nhất hoặc nếu không có _host_ và _path_ nào khớp với HTTP request trong Ingress Yaml file thì traffic sẽ được route đến service default backend. Ví dụ như bên dưới, chúng tôi đang cấu hình mặc định nếu request không thỏa mãn rule nào trong Ingress yaml file thì sẽ đi vào service name: example-svc-1 với port number 8080

```
defaultBackend:
    service:
      name: example-svc-1
      port:
        number: 8080
```

***

### TLS <a href="#configureforanapplicationloadbalancer-tls" id="configureforanapplicationloadbalancer-tls"></a>

Bạn có thể bảo mật Ingress bằng cách chỉ định 1 Secret có chứa TLS key và certificate. Hiện tại Ingress chỉ hỗ trợ duy nhất TLS port 443 và là điểm kết thúc cho TLS (TLS termination). TLS Secret phải chứa các trường với tên key là tls.crt và tls.key, đây chính là certificate và private key để sử dụng cho TLS. Cụ thể, bạn cần chỉ định:

* Host: các host được chỉ định sẽ dùng cert.
* SecretName: tên secret chứa cert.

***

### Path types <a href="#configureforanapplicationloadbalancer-pathtypes" id="configureforanapplicationloadbalancer-pathtypes"></a>

Mỗi path (đường dẫn) trong Ingress có một pathType (loại đường dẫn) tương ứng. Có ba pathType được hỗ trợ:

* Exact: Khớp với đường dẫn URL một cách chính xác tuyệt đối và phân biệt chữ hoa chữ thường.
* Prefix: Khớp dựa trên tiền tố của đường dẫn URL được phân tách bởi dấu /. Việc so khớp (match) là có phân biệt chữ hoa thường và được thực hiện trên từng thành phần của đường dẫn URL. Một thành phần của đường dẫn URL chính là 1 label được phân tách bằng dấu phân cách / trong đường dẫn URL (Nghĩa là đường dẫn URL có thể bao gồm nhiều cấp phân tách nhau bởi dẫu /, mỗi chuỗi đứng giữa 2 dấu / chính là 1 label, mỗi label chính là 1 thành phần của đường dẫn URL). Một request URL được xem như là khớp với 1 trường path (được cấu hình trong đặc tả Ingress) khi toàn bộ giá trị của path (có thể gồm nhiều thành phần phân tách bằng dấu /) khớp với các label đầu tiên (tính từ bên trái của đường dẫn URL). Ví dụ /example1/path1 khớp với /example1/path1/path2, nhưng không khớp với /example1/path1path2

Ví dụ cụ thể:

| Path type | Path(s)                             | Request path(s)           | Có match hay không? |
| --------- | ----------------------------------- | ------------------------- | ------------------- |
| Exact     | `/example1`                         | `/example1`               | Có                  |
| Exact     | `/example1`                         | `/host1`                  | Không               |
| Exact     | `/example1`                         | `/example1/`              | Không               |
| Exact     | `/example1/`                        | `/example1`               | Không               |
| Prefix    | `/`                                 | (all paths)               | Có                  |
| Prefix    | `/example1`                         | `/example1`, `/example1/` | Có                  |
| Prefix    | `/example1/`                        | `/example1`, `/example1/` | Có                  |
| Prefix    | `/example1/host11`                  | `/example1/host1`         | Không               |
| Prefix    | `/example1/host1`                   | `/example1/host1`         | Có                  |
| Prefix    | `/example1/host1/`                  | `/example1/host1`         | Có                  |
| Prefix    | `/example1/host1`                   | `/example1/host1/`        | Có                  |
| Prefix    | `/example1/host1`                   | `/example1/host1/ccc`     | Có                  |
| Prefix    | `/example1/host1`                   | `/example1/host1xyz`      | Không               |
| Prefix    | `/`, `/example1`                    | `/example1/ccc`           | Có                  |
| Prefix    | `/`, `/example1`, `/example1/host1` | `/example1/host1`         | Có                  |
| Prefix    | `/`, `/example1`, `/example1/host1` | `/ccc`                    | Có                  |
| Prefix    | `/example1`                         | `/ccc`                    | Không               |

* Trong một số trường hợp, nhiều path bên trong Ingress sẽ khớp với đường dẫn của request URL. Trong những trường hợp đó, quyền ưu tiên sẽ được trao cho path khớp dài nhất đầu tiên. Nếu hai path vẫn có độ dài khớp bằng nhau thì quyền ưu tiên sẽ theo thứ tự rule được tạo trên Ingress Yaml file.

***

### Ingress rule <a href="#configureforanapplicationloadbalancer-ingressrule" id="configureforanapplicationloadbalancer-ingressrule"></a>

Mỗi HTTP rule chứa các thông tin sau:

* **1 host tùy chọn**. Nếu không có host (ta có thể hiểu là 1 tên miền) nào được chỉ định nên rule sẽ được áp dụng cho tất cả HTTP traffic đi vào (inbound) địa chỉ IP đã được chỉ định. Nếu có chỉ định host (ví dụ example1.com) thì rule chỉ áp dụng cho host đó thôi.
* **1 danh sách các đường dẫn (path)** (ví dụ `/example1/host1`), mỗi path có 1 service backend gắn liền với nó được định nghĩa bởi Service Name và Port Number. Cả host và path phải khớp với nội dung của incoming request trước khi bộ cân bằng tải điều hướng traffic đến Services mong muốn.
* **1 backend** là tổ hợp của tên Services và Port Number. HTTP và HTTPS request đi đến Ingress và có URL khớp với host và path của rule sẽ được gửi đến danh sách các backend.

Ví dụ: Host có khớp với Host header theo bảng:

| Host                                       | Host header                                                      | Có match hay không? |
| ------------------------------------------ | ---------------------------------------------------------------- | ------------------- |
| `*.`[`example1.com`](http://example1.com/) | [`example2.example1.com`](http://example2.example1.com/)         | Có                  |
| `*.`[`example1.com`](http://example1.com/) | [`baz.example2.example1.com`](http://baz.example2.example1.com/) | Không               |
| `*.`[`example1.com`](http://example1.com/) | [`example1.com`](http://example1.com/)                           | Không               |
