# Release notes

## Mar 5, 2025 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng mới cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:

**Tính năng mới:**

* **Hỗ trợ Container-Optimized OS with containerd cho region HCM**– Trước đây, VKS chỉ hỗ trợ **Ubuntu with containerd**. Giờ đây, khách hàng có thể sử dụng **Container-Optimized OS with containerd** làm node group image cho node group khi triển khai Kubernetes phiên bản **v1.29.1, v1.30.5** tại region HCM.

***

## Feb 27, 2025 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng mới cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:

**Tính năng mới:**

* **Fleet management**: cho phép gom nhóm các Kubernetes cluster trên nhiều **zone/region**, giúp quản lý traffic linh hoạt giữa các cluster. Tính năng này hỗ trợ:
  * **North-South Traffic Management với Global Load Balancer (GLB)**: Quản lý traffic vào/ra giữa các cluster. Hỗ trợ **Calico Overlay, Cilium Overlay, và Cilium VPC Native**.
  * **East-West Traffic Management với Multi Cluster Service (MCS)**: Quản lý traffic nội bộ giữa các cluster, chỉ hỗ trợ **Cilium VPC Native**.

Chi tiết vui lòng tham khảo tài liệu hướng dẫn sử dụng tại [đây](../network/fleet-management.md).

***

## Jan 20, 2025 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng mới cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:

**Tính năng mới:**

* **Hỗ trợ Container-Optimized OS with containerd cho zone BKK** – Trước đây, VKS chỉ hỗ trợ **Ubuntu with containerd**. Giờ đây, khách hàng có thể sử dụng **Container-Optimized OS with containerd** làm node group image cho node group khi triển khai Kubernetes phiên bản **v1.29.1, v1.30.5** tại zone BKK.

***

## Jan 2, 2025 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng mới cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:

**Tính năng mới:**

* **Hỗ trợ Kubernetes v1.30:** Phiên bản này thuộc **Release Channel: Rapid**, dành cho mục đích thử nghiệm. VKS không cam kết SLA cho phiên bản này.
* **Hỗ trợ Container-Optimized OS with containerd cho region HAN** – Trước đây, VKS chỉ hỗ trợ **Ubuntu with containerd**. Giờ đây, khách hàng có thể sử dụng **Container-Optimized OS with containerd** làm node group image cho node group khi triển khai Kubernetes phiên bản **v1.29.1, v1.30.5** tại region HAN.
* **Upgrade Insight** – Cung cấp thông tin chi tiết về quá trình nâng cấp phiên bản Kubernetes, giúp người dùng đánh giá rủi ro, tác động và kế hoạch nâng cấp một cách hiệu quả.

***

## Dec 5, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng mới cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:

**Tính năng mới:**

* **Force-Upgrade, Auto-Upgrade**: Tự động nâng cấp phiên bản Kubernetes cho cluster/ node group theo lịch trình hoặc khi phiên bản hiện tại sắp hết hạn.. Chi tiết tham khảo thêm tại [đây](../upgrade-kubernetes-version/automatically-upgrade.md).

***

## Oct 23, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều cải tiến cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:

**Cải tiến:**

* **Hỗ trợ POC/ Stop POC cho Cluster**: Người dùng giờ đây có thể thực hiện POC/ Stop POC cho các tài nguyên trên VKS như Server, Volume, Load Balancer, Endpoint. Tính năng này mang đến sự linh hoạt cao cho người dùng khi muốn trải nghiệm với VKS. Chi tiết tham khảo thêm tại [đây](../clusters/stop-poc.md).
* **Nâng cấp Plugin VNGCloud BlockStorage CSI Driver:** Các lỗi đã được phát hiện trong các phiên bản trước đã được khắc phục, giúp hệ thống hoạt động mượt mà và tin cậy hơn.
* **Tự do lựa chọn/ chỉnh sửa cấu hình có/ không sử dụng plugin VNGCloud LoadBalancer Controller, Plugin VNGCloud Ingress Controller trên cụm VKS hiện có:** Khả năng tùy chỉnh cấu hình plugin cho phép người dùng tối ưu hóa cụm VKS theo nhu cầu cụ thể của mình. Điều này giúp tăng tính linh hoạt và đáp ứng các yêu cầu đặc biệt của từng ứng dụng.
* **Ngoài ra,** trong bản cập nhật này, chúng tôi cũng đã khắc phục một số lỗi nhỏ để mang đến trải nghiệm người dùng tốt hơn.

***

## Oct 03, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng và cải tiến cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:

**Triển khai Region mới:**

* Bên cạnh Region HCM03, VKS hiện đã hỗ trợ thêm Region HAN01. Việc bổ sung này giúp khách hàng có thêm lựa chọn trong việc triển khai ứng dụng, đặc biệt hữu ích cho các doanh nghiệp có yêu cầu về vị trí đặt dữ liệu.

**Tính năng mới:**

* **Network Type: Cilium Overlay, Cilium VPC Native Routing:** Ngoài Calico Overlay, bản phát hành lần này chúng tôi đã bổ sung hai loại mạng mới: Cilium Overlay và Cilium VPC Native Routing. Cilium Overlay cho phép bạn xây dựng mạng overlay linh hoạt, trong khi Cilium VPC Native Routing tích hợp chặt chẽ với VPC của VNG Cloud, giúp tối ưu hiệu suất và bảo mật cho ứng dụng của bạn. Chi tiết tham khảo thêm tại [đây](../network/cni/).

**Cải tiến:**

* **Multiple Subnet cho Cluster trên VKS:** VKS giờ đây hỗ trợ sử dụng nhiều subnet cho một cluster. Điều này cho phép bạn cấu hình từng node group trong cluster nằm ở các subnet khác nhau trong cùng một VPC, tối ưu hóa việc phân bổ tài nguyên và quản lý mạng.
* **Chỉnh sửa Labels/Taints trên cụm VKS hiện có:** Với khả năng chỉnh sửa trực tiếp Labels/Taints trên cụm VKS đã triển khai, bạn có thể điều khiển việc lên lịch Pod, áp dụng các chính sách khác nhau cho các Node Group, và tùy chỉnh quy tắc lựa chọn node cho các ứng dụng. Điều này giúp quản lý và phân loại tài nguyên hiệu quả hơn.
* **Enable/Disable lựa chọn sử dụng Private Service Endpoint:** Trước đây, khi tạo private cluster trên VKS, việc tạo private service endpoint là bắt buộc. Giờ đây, bạn có thể dễ dàng bật/tắt tính năng này, cho phép các dịch vụ trong cụm VKS giao tiếp qua địa chỉ IP nội bộ, tăng cường bảo mật và giảm thiểu rủi ro tấn công từ bên ngoài.
* **Enable/Disable lựa chọn mã hóa Volume:** Tính năng mã hóa Volume cho phép bạn bảo vệ dữ liệu nhạy cảm được lưu trữ trong các Persistent Volume của cụm VKS. Việc này đảm bảo an toàn dữ liệu và tuân thủ các quy định về bảo vệ thông tin. Giờ đây, bạn có thể bật/tắt tính năng mã hóa cho từng Volume theo nhu cầu.

***

## Aug 28, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều tính năng mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Tính năng mới:**

* **Private Cluster:** Trước đây, các public cluster trên VKS đang sử dụng địa chỉ Public IP để giao tiếp giữa nodes và control plane. Để nâng cao bảo mật cho cluster của bạn, chúng tôi đã cho ra mắt mô hình private cluster. Tính năng Private Cluster giúp cho cụm K8S của bạn được bảo mật nhất có thể, mọi kết nối hoàn toàn là private từ kết nối giữa nodes tới control plane, kết nối từ client tới control plane, hay kết nối từ nodes tới các sản phẩm dịch vụ khác trong VNG Cloud như: vStorage, vCR, vMonitor, VNGCloud APIs,...Private Cluster là lựa chọn lý tưởng cho **các dịch vụ yêu cầu kiểm soát truy cập chặt chẽ, đảm bảo tuân thủ các quy định về bảo mật và quyền riêng tư dữ liệu**. Chi tiết 2 mô hình hoạt động của Cluster, bạn có thể tham khảo thêm tại [đây ](../mo-hinh-hoat-dong.md)và tham khảo các bước khởi tạo một private Cluster tại [đây](../bat-dau-voi-vks/khoi-tao-mot-private-cluster.md).

***

## Aug 26, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Kubernetes Version**: VKS đã bổ sung các image mới nhằm tối ưu hóa size, feature, network,...so với các image cũ. Việc xây dựng các image này cũng nhằm phục vụ cho cả hai loại cluster là Public và Private mà VKS sắp ra mắt. Cụ thể, trong bản phát hành này, chúng tôi đã bổ sung thêm các image sau:
  * Ubuntu-22.kube\_v1.27.12-vks.1724605200
  * Ubuntu-22.kube\_v1.28.8-vks.1724605200
  * Ubuntu-22.kube\_v1.29.1-vks.1724605200

{% hint style="info" %}
**Chú ý:**

* Để khởi tạo một **Private Cluster**, bạn cần chọn sử dụng một trong 3 image mới này. Đối với Public Cluster, bạn có thể chọn sử dụng bất kỳ image cũ hoặc mới tùy theo nhu cầu của bạn.
{% endhint %}

***

## Aug 13, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Event History**: VKS đã bổ sung thêm các sự kiện của **Auto Scaling** và **Auto Healing.** Giờ đây, với Event History, bạn có thể theo dõi từng thay đổi xảy ra trong Cluster, từ việc tự động điều chỉnh quy mô (Auto Scaling) cho đến việc tự động phục hồi (Auto Healing). Các event này giúp tăng cường khả năng giám sát và quản lý cụm Kubernetes của bạn.

***

## Aug 01, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều tính năng và cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Tính năng mới:**

* **Giám sát tài nguyên VKS:** Người dùng có thể theo dõi trực tiếp tình trạng hoạt động của Cluster, Node, tình trạng sử dụng CPU, RAM, Memory,... của Node thông qua các dashboard trực quan. Để hiển thị dữ liệu lên dashboard, người dùng cần cài đặt `vmonitor-metric-agent` vào cụm mong muốn thực hiện giám sát. Chi tiết tham khảo thêm tại [đây](../giam-sat/metrics.md).

***

## July 25, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Nâng cấp quản lý VKS thông qua Terraform:** Người dùng có thể **đồng thời** điều chỉnh số lượng node (Number of nodes) và thay đổi số lượng node cho autoscale (Minimum/ Maximum node Autoscale) ngay trong quá trình chỉnh sửa cấu hình. Với khả năng điều chỉnh nhiều thông số cùng lúc, việc quản lý cụm Kubernetes trở nên linh hoạt và thuận tiện hơn. Chi tiết tham khảo thêm ví dụ tại [đây](https://registry.terraform.io/providers/vngcloud/vngcloud/latest/docs/resources/vks_cluster).

***

## July 23, 2024 <a href="#april_19_2024-3" id="april_19_2024-3"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Nâng cấp Plugin VNGCloud LoadBalancer Controller, Plugin VNGCloud Ingress Controller:** Các lỗi đã được phát hiện trong các phiên bản trước đã được khắc phục, giúp hệ thống hoạt động mượt mà và tin cậy hơn.

***

## July 18, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Nâng cấp Plugin VNGCloud BlockStorage CSI Driver:** Các lỗi đã được phát hiện trong các phiên bản trước đã được khắc phục, giúp hệ thống hoạt động mượt mà và tin cậy hơn.

***

## July 17, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Private Node Group**: MTU cho các Node thuộc Private Node Group đã được cập nhật lên 1450. Điều này giúp cải thiện hiệu suất mạng cho các ứng dụng chạy trong Private Node Group.
* **Number of nodes và AutoScale**: Giờ đây bạn có thể chỉnh sửa cả hai thuộc tính này trong cùng một API. Điều này giúp đơn giản hóa việc quản lý Cluster của bạn.

***

## July 02, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều tính năng và cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Tính năng mới:**

* **Hỗ trợ Stop POC cho Cluster**: Người dùng giờ đây có thể thực hiện Stop POC cho toàn bộ các tài nguyên đang được POC trên một Cluster một cách dễ dàng, thay vì phải thực hiện Stop POC riêng lẻ cho từng resource. Điều này giúp tiết kiệm thời gian và công sức khi chuyển Cluster từ tài nguyên thử nghiệm sang tài nguyên thật. Chi tiết tham khảo thêm tại [đây](../clusters/stop-poc.md).

**Cải tiến:**

* **Trạng thái Node Group**: Bổ sung trạng thái "**Degraded**" để người dùng có thể theo dõi tình trạng hoạt động của Node Group một cách chính xác hơn. Trạng thái này sẽ hiển thị khi số node hoạt động ít hơn số replica thực tế.
* **Timeout cho Cluster và Node Group**: Đã thêm thời gian chờ (timeout) cho việc tạo Cluster và Node Group, cải tiến này đảm bảo VKS vận hành mượt mà và hiệu quả, đồng thời cung cấp thông tin rõ ràng và kịp thời cho người dùng. Timeout cho việc tạo Cluster là <mark style="color:red;">**1 giờ**</mark> và cho Node Group là <mark style="color:red;">**3 giờ**</mark>. Nếu sau khoảng thời gian này mà Cluster hoặc Node Group của bạn chưa được tạo thành công, chúng tôi sẽ cập nhật trạng thái chúng về ERROR. Lúc này, bạn có thể thực hiện xóa và tạo Cluster, Node Group khác thay thế.
* **KubeConfig Access:** Việc truy cập vào tệp tin KubeConfig giờ chỉ được phép khi Cluster đã Active. Cải tiến này giúp người dùng tránh các lỗi cấu hình khi sử dụng Terraform để tự động hóa việc triển khai Kubernetes.

***

## June 27, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Nâng cấp Plugin VNGCloud LoadBalancer Controller, Plugin VNGCloud Ingress Controller:** Các lỗi đã được phát hiện trong các phiên bản trước đã được khắc phục, giúp hệ thống hoạt động mượt mà và tin cậy hơn.

***

## June 19, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Cải tiến:**

* **Nâng cấp tính năng thiết lập kích cỡ PVC (Persistent Volume Claim Size):** Người dùng giờ đây có thể chỉ định kích cỡ tối thiểu cho ổ đĩa CSI là <mark style="color:red;">**1GB**</mark> thay vì kích cỡ tối thiểu là 20GB như trước đây. Chi tiết bạn có thể tham khảo thêm tại [Volume ](broken-reference/)và [Integrate with Container Storage Interface](broken-reference/).
* **Thay đổi Storage Class mặc định sử dụng cho Cluster:** thay đổi mặc định từ ổ đĩa loại SSD - IOPS 200 thành mặc định ổ đĩa loại SSD - IOPS 3000.
* **Nâng cấp Plugin VNGCloud LoadBalancer Controller, Plugin VNGCloud Ingress Controller:** cải tiến plugin giúp tránh trùng lặp việc đặt tên Load Balancer.

{% hint style="info" %}
**Chú ý:**

Do Storage Class mặc định cũ đã được chúng tôi xóa khỏi hệ thống, nếu bạn muốn tiếp tục sử dụng và thực hiện resize storage class này, bạn có thể:

* Tạo Storage Class có tên sc-iops-200-retain với Volume Type mà bạn mong muốn.
* Resize Storage Class thông qua lệnh:

```
kubectl patch pvc sc-iops-200-retain -p '{"spec":{"resources":{"requests":{"storage":"50Gi"\}}\}}'
```

Chi tiết tham khảo thêm tại [Integrate with Container Storage Interface](broken-reference/).
{% endhint %}

***

## June 12, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều tính năng và cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Tính năng mới:**

* **Hỗ trợ người dùng làm việc với VKS thông qua Terraform:** Người dùng có thể dễ dàng khởi tạo Cluster và Node Group trong VKS bằng Terraform. Chi tiết tham khảo thêm tại [đây](broken-reference/).

**Cải tiến:**

* **Nâng cấp Plugin VNGCloud LoadBalancer Controller:** Bổ sung Annotation để cấu hình Load Balancer hỗ trợ Proxy Protocol. Chi tiết tham khảo thêm tại [đây](../../../English/vks/bat-dau-voi-vks/preserve-source-ip-khi-su-dung-vlb-layer4-va-nginx-ingress-controller.md).

***

## May 30, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

Chúng tôi vô cùng trân trọng thông báo, bản release chính thức (**General Availability**) của dịch vụ VNGCloud Kubernetes Service đã có sẵn. Với bản release chính thức này, ngoài các tính năng mà chúng tôi đã cung cấp trên các bản release trước đó, phiên bản này sẽ mang đến nhiều tính năng và cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Tính năng mới:**

* **Re-activate :** VKS cho phép bạn thực hiện yêu cầu hệ thống tự động khởi tạo lại IAM Service Account mặc định khi bạn xóa nhầm hoặc thay đổi thông tin IAM Service Account mặc định đã khởi tạo trước đó. IAM Service Account mặc định là IAM Service Account được hệ thống VKS tự động khởi tạo khi bạn bắt đầu làm việc với VKS, chúng tôi sẽ sử dụng IAM Service Account này để khởi tạo các resource cho Cluster của bạn.
* **Event History**: VKS sẽ thực hiện hiển thị lịch sử các sự kiện xảy ra khi người dùng làm việc với Cluster hoặc từng Node Group. Đây sẽ là một cách giúp bạn có thể giám sát các hoạt động xảy ra với Cluster của bạn, từ đó hạn chế các hoạt động bất thường xảy ra.
* **Volume**: VKS đã tích hợp hiển thị danh sách Volume tại Resource Tab, giúp bạn dễ dàng quản lý các Volume đang được attach vào Cluster của bạn.
* **Load Balancer**: VKS đã tích hợp hiển thị danh sách Load Balancer tại Resource Tab, giúp bạn dễ dàng quản lý các Load Balancer đang được sử dụng cho Cluster của bạn.

**Cải tiến:**

* **Hiệu năng**: VKS đã thực hiện tối ưu hiệu năng khi khởi tạo Cluster. Cụ thể, tại bản Alpha, thời gian từ khi bắt đầu khởi tạo Cluster (với Default Node Group) tới khi Cluster chuyển trạng thái **ACTIVE** vào khoảng 04:00s tới 04:30s. Hiện tại thời gian này đã được chúng tôi tối ưu về <mark style="color:red;">**02:30s tới 03:00s**</mark> tùy thuộc vào từng Cluster và từng thời điểm mà bạn khởi tạo.
* **Garbage collection of unused containers and images**: VKS sẽ tự động xóa các image không được sử dụng khi disk chạm mức giới hạn sử dụng (tỷ lệ usage/ quota >= 85%).
* **Ngoài ra**, bản GA này được chúng tôi cải thiến một vài vấn đề khác như:
  * Thay đổi cách đặt tên **Node Name** giúp bạn dễ dàng sử dụng và quản lý Cluster của bạn. Cụ thể, tên Node Name sẽ có thêm thông tin **Cluster Name**, **Node Group Name**.
  * Xóa **User Builder** trên User's Worker Node.
  * Thay đổi cơ chế **SSH** từ Port 22 qua Port 234.

Nếu bạn gặp bất kỳ vấn đề với bản phát hành chính thức này, vui lòng liên hệ với bộ phận hỗ trợ của VKS để được trợ giúp.

***

## May 03, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

Bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều tính năng và cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:

**Tính năng mới:**

* **Hỗ trợ tính năng Whitelist:** VKS cho phép tạo Private Node Group với chỉ Private IP đồng thời cho phép IP nào kết nối tới Cluster thông qua tính năng Whitelist IP. Chi tiết tham khảo thêm tại [Whitelist](broken-reference/).

**Cải tiến:**

* **Tối ưu hóa hệ thống:** Giúp hệ thống hoạt động trơn tru và hiệu quả hơn.
* **Sửa lỗi:** Khắc phục một số lỗi nhỏ để mang đến trải nghiệm người dùng tốt hơn.

Nếu bạn gặp bất kỳ vấn đề nào sau khi cập nhật, vui lòng liên hệ với bộ phận hỗ trợ của VKS để được trợ giúp.

***

## April 17, 2024 <a href="#april_19_2024" id="april_19_2024"></a>

**Chúng tôi vô cùng giới thiệu bản cập nhật mới cho dịch vụ VKS, mang đến cho bạn trải nghiệm quản lý Kubernetes mạnh mẽ và hiệu quả hơn bao giờ hết!**

**Điểm nổi bật:**

* **Quản lý Control Plane hoàn toàn tự động (Fully Managed control plane):** VKS sẽ giải phóng bạn khỏi gánh nặng quản lý Control Plane của Kubernetes, giúp bạn tập trung vào việc phát triển ứng dụng.
* **Hỗ trợ các phiên bản Kubernetes mới nhất:** VKS luôn cập nhật những phiên bản Kubernetes mới nhất (minor version từ 1.27, 1.28, 1.29) để đảm bảo bạn luôn tận dụng được những tính năng tiên tiến nhất.
* **Kubernetes Networking:** VKS tích hợp Calico CNI, mang lại tính hiệu quả và bảo mật cao.
* **Upgrade seamlessly:** VKS hỗ trợ nâng cấp giữa các phiên bản Kubernetes một cách dễ dàng và nhanh chóng, giúp bạn luôn cập nhật những cải tiến mới nhất.
* **Scaling & Healing Automatically:** VKS tự động mở rộng Node group khi cần thiết và tự động sửa lỗi khi node gặp vấn đề, giúp bạn tiết kiệm thời gian và công sức quản lý.
* **Giảm chi phí và nâng cao độ tin cậy:** VKS triển khai Control Plane của Kubernetes ở chế độ sẵn sàng cao và hoàn toàn miễn phí, giúp bạn tiết kiệm chi phí và nâng cao độ tin cậy cho hệ thống.
* **Tích hợp Blockstore Native (Container Storage Interface - CSI):** VKS cho phép bạn quản lý Blockstore thông qua YAML của Kubernetes, cung cấp lưu trữ bền vững cho container và hỗ trợ các tính năng quan trọng như thay đổi kích thước, thay đổi IOPS và snapshot volume.
* **Tích hợp Load Balancer (Network Load Balancer, Application Load Balancer) thông qua các driver được tích hợp sẵn như VNGCloud Controller Mananger, VNGCloud Ingress Controller:** VKS cung cấp khả năng quản lý NLB/ALB thông qua YAML của Kubernetes, giúp bạn dễ dàng expose Service trong Kubernetes ra bên ngoài.
* **Nâng cao bảo mật:** VKS cho phép bạn tạo Private Node Group với chỉ Private IP và kiểm soát quyền truy cập vào cluster thông qua tính năng Whitelist IP, đảm bảo an toàn cho hệ thống của bạn.

**Với những tính năng đột phá này, VKS hứa hẹn sẽ mang đến cho bạn trải nghiệm quản lý Kubernetes hoàn toàn mới, giúp bạn tối ưu hóa hiệu quả và tiết kiệm chi phí!**

**Hãy liên hệ với chúng tôi để được tư vấn và hỗ trợ thêm!**
