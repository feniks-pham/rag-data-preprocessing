# Khởi tạo và làm việc với NVIDIA GPU Node Group

## Tổng quan

* [**NVIDIA GPU Operator**](https://github.com/NVIDIA/gpu-operator) là một operator giúp đơn giản hóa việc triển khai và quản lý các node GPU trong các cụm Kubernetes. Nó cung cấp một tập hợp các tài nguyên tùy chỉnh và bộ điều khiển của Kubernetes cùng làm việc để tự động hóa quản lý tài nguyên GPU trong cụm Kubernetes.
* Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn:&#x20;
  * Khởi tạo một node group với NVIDIA GPU
  * Cài đặt NVIDIA GPU Operator.
  * Triển khai một GPU Workload.
  * Thiết lập GPU Sharing.
  * Giám sát hoạt động GPU resources.
  * Autoscale GPU resources.

***

## Khởi tạo một node group với NVIDIA GPU

* Thực hiện khởi tạo một Cluster với ít nhất một node group sử dụng NVIDIA GPU theo hướng dẫn tại [đây ](khoi-tao-mot-public-cluster/khoi-tao-mot-public-cluster-voi-public-node-group.md)nếu bạn muốn khởi tạo public node group hoặc tại [đây ](khoi-tao-mot-public-cluster/khoi-tao-mot-public-cluster-voi-private-node-group/)nếu bạn muốn khởi tạo private node group.
* Ngoài ra, bạn cần đảm bảo đã cài đặt `kubectl` và `helm` tại thiết bị của bạn.&#x20;
* Bên cạnh đó, bạn cũng có thể cài đặt các công cụ và thư viện khác mà bạn có thể sử dụng để giám sát và quản lý tài nguyên Kubernetes của mình:
  * `kubectl-view-allocations` plugin sử dụng để giám sát tài nguyên Kubernetes của bạn. Để biết thêm thông tin, vui lòng tham khảo thêm tại [kubectl-view-allocations](https://github.com/davidB/kubectl-view-allocations).
*   Bạn có thể thực hiện kiểm tra các cài đặt bên trên thông qua lệnh:&#x20;

    ```bash
    # Check kubectl CLI version
    kubectl version

    # Check Helm version
    helm version

    # Check kubectl-view-allocations version
    kubectl-view-allocations --version
    ```

<figure><img src="../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   Trên Cluster vừa tạo, thực hiện kiểm tra node trong node group của bạn qua lệnh:&#x20;

    ```bash
    kubectl get nodes -owide
    ```

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Cài đặt NVIDIA GPU Operator

* Nội dung bên dưới chúng tôi sẽ trực tiếp hướng dẫn bạn cài đặt NVIDIA GPU Operator, để biết thêm thông tin về plugin này, vui lòng tham khảo thêm tại [NVIDIA GPU Operator Documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html).&#x20;
*   Trên Cluster bạn đã tạo ở bước trên, thực hiện chạy lệnh:&#x20;

    ```bash
    helm install nvidia-gpu-operator --wait --version v24.3.0 \
      -n gpu-operator --create-namespace \
      oci://vcr.vngcloud.vn/81-vks-public/vks-helm-charts/gpu-operator \
      --set dcgmExporter.serviceMonitor.enabled=true
    ```

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   Hệ thống mất khoảng 5 - 10 phút để thực hiện cài đặt operator này, bạn hãy đợi tới khi việc cài đặt hoàn thành. Trong thời gian này, bạn có thể kiểm tra tất cả các pods trong namespace`gpu-operator` đang chạy thông qua lệnh:&#x20;

    ```bash
    kubectl -n gpu-operator get pods -owide
    ```

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   Operator sẽ gán label`nvidia.com/gpu`cho node trong node group của bạn, lable này được NVIDIA GPU Operator sử dụng để identify nodes, bạn cũng có thể sử dụng label này để filter những node đang có NVIDIA GPU. Bạn có thể kiểm tra các node được gán nhãn này qua lệnh:&#x20;

    ```bash
    kubectl get node -o json | jq '.items[].metadata.labels' | grep "nvidia.com"
    ```

Ví dụ, đối với kết quả bên dưới, node trong cụm có label `nvidia.com/gpu`, có nghĩa là node đó có GPU. Các label này cũng cho biết nút này đang sử dụng 1 card GPU RTX 2080Ti, số lượng GPU có sẵn, Bộ nhớ GPU và các thông tin khác.

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   Trên pod `nvidia-device-plugin-daemonset`trong namespace`gpu-operator`, bạn có thể chạy lệnh `nvidia-smi` để kiểm tra thông tin GPU trên node:

    ```bash
    POD_NAME=$(kubectl -n gpu-operator get pods -l app=nvidia-device-plugin-daemonset -o jsonpath='{.items[0].metadata.name}')
    kubectl -n gpu-operator exec -it $POD_NAME -- nvidia-smi
    ```

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Triển khai một GPU workload

### Deploy Cuda VectorAdd Test

* Bạn có thể thực hiện deploy `cuda-vectoradd-test` như một workload mẫu trên cluster của bạn. Cụ thể bạn có thể tham khảo thêm về workload mẫu này tại [cuda-vectoradd-test.yaml](https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/cuda-vectoradd-test.yaml).
*   Thực hiện chạy các lệnh bên dưới để deploy workload và kiểm tra các pods đã được khởi chạy:

    ```bash
    # Apply the manifest
    kubectl apply -f \
    https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/cuda-vectoradd-test.yaml

    # Check the pods
    kubectl get pods

    # Check the logs of the pod
    kubectl logs cuda-vectoradd

    # [Optional] Clean the resources
    kubectl delete deploy cuda-vectoradd
    ```

<figure><img src="../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Deploy TensorFlow Test

* Ngoài Cuda VectorAdd Test, bạn cũng có thể deploy TensorFlow như một workload trên Cluster của bạn. Cụ thể bạn có thể tham khảo về workload mẫu này tại [tensorflow-gpu.yaml](https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/tensorflow-gpu.yaml).&#x20;
* Thực hiện chạy các lệnh bên dưới để deploy workload và kiểm tra các pods đã được khởi chạy:

```bash
# Apply the manifest
kubectl apply -f \
  https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/tensorflow-gpu.yaml

# Check the pods
kubectl get pods

# Check processes are running using nvidia-smi
kubectl -n gpu-operator exec -it <put-your-nvidia-driver-daemonset-pod-name> -- nvidia-smi

# Check the logs of the TensorFlow pod
kubectl logs <put-your-tensorflow-gpu-pod-name> --tail 20

# [Optional] Clean the resources
kubectl delete deploy tensorflow-gpu
```

<figure><img src="../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Thiết lập GPU Sharing

* GPU sharing strategies allow multiple containers to efficiently use your attached GPUs and save running costs. The following tables summarizes the difference between the GPU sharing modes supported by NVIDIA GPUs:
* Chiến lược GPU Sharing cho phép nhiều containers có thể sử dụng chung một node GPU nhằm mục đích tiết kiệm chi phí của bạn. Bảng sau đây tóm tắt sự khác biệt giữa các chiến lược GPU Sharing được NVIDIA hỗ trợ:

<table data-view="cards"><thead><tr><th>Sharing mode</th><th align="center">Supported by VKS</th><th align="center">Workload isolation level</th><th>Pros</th><th>Cons</th><th>Suitable for these workloads</th></tr></thead><tbody><tr><td><strong>Multi-instance GPU (MIG)</strong></td><td align="center">❌</td><td align="center">Best</td><td><ul><li>Processes are executed in parallel</li><li>Full isolation (dedicated memory and compute resources)</li></ul></td><td><ul><li>Supported by fewer GPU models (only Ampere or more recent architectures)</li><li>Coarse-grained control over memory and compute resources</li></ul></td><td><ul><li>Recommended for workloads running in parallel and that need certain resiliency and QoS. For example, when running AI inference workloads, multi-instance GPU multi-instance GPU allows multiple inference queries to run simultaneously for quick responses, without slowing each other down.</li></ul></td></tr><tr><td><strong>GPU Time-slicing</strong></td><td align="center">✅</td><td align="center">None</td><td><ul><li>Processes are executed concurrently</li><li>Supported by older GPU architectures (Pascal or newer)</li></ul></td><td><ul><li>No resource limits</li><li>No memory isolation</li><li>Lower performance due to context-switching overhead</li></ul></td><td><ul><li>Recommended for bursty and interactive workloads that have idle periods. These workloads are not cost-effective with a fully dedicated GPU. By using time-sharing, workloads get quick access to the GPU when they are in active phases.</li><li>GPU time-sharing is optimal for scenarios to avoid idling costly GPUs where full isolation and continuous GPU access might not be necessary, for example, when multiple users test or prototype workloads.</li><li>Workloads that use time-sharing need to tolerate certain performance and latency compromises.</li></ul></td></tr><tr><td><strong>Multi-process server (MPS)</strong></td><td align="center">✅</td><td align="center">Medium</td><td><ul><li>Processes are executed parallel</li><li>Fine-grained control over memory and compute resources allocation</li></ul></td><td><ul><li>No error isolation and memory protection</li></ul></td><td><ul><li>Recommended for batch processing for small jobs because MPS maximizes the throughput and concurrent use of a GPU. MPS allows batch jobs to efficiently process in parallel for small to medium sized workloads.</li><li>NVIDIA MPS is optimal for cooperative processes acting as a single application. For example, MPI jobs with inter-MPI rank parallelism. With these jobs, each small CUDA process (typically MPI ranks) can run concurrently on the GPU to fully saturate the whole GPU.</li><li>Workloads that use CUDA MPS need to tolerate the <a href="https://docs.nvidia.com/deploy/mps/#topic_3_3_3">memory protection and error containment limitations</a>.</li></ul></td></tr></tbody></table>

### GPU time-slicing

* **GPU time-slicing** là kỹ thuật chia sẻ tài nguyên GPU giữa nhiều tiến trình hoặc pod trong Kubernetes bằng cách phân bổ thời gian sử dụng GPU cho từng tiến trình theo chu kỳ.

#### Configure GPU time-slicing

* Để sử dụng GPU time-slicing cho cluster của bạn, bạn cần tạo tệp tin `ConfigMap` theo mẫu bên dưới để định nghĩa cấu hình time-slicing. Trong đó:&#x20;
  * `replicas`: field chỉ định số lượng pods có thể share chung GPU, tối đa bạn có thể thiết lập 48 pods share chung một GPU.
  * name: mặc định nvidia.com/gpu - lable sử dụng để filter node có GPU.
  * minStrategy: mặc định none do GPU hiện tại chưa hỗ trợ MIG.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: gpu-sharing-config
data:
  any: |-
    version: v1
    flags:
      migStrategy: none            # Disable MIG, MUST be none in the case your GPU is not supported MIG
    sharing:
      timeSlicing:
        resources:
        - name: nvidia.com/gpu     # Only apply for the node with the node.status contains 'nvidia.com/gpu'
          replicas: 4              # Allow 4 pods to share the GPU, SHOULD less than 48 pods
```

*   Hoặc bạn có thể chạy câu lệnh bên dưới để apply cấu hình trên cho tất cả các node trong cluster của bạn có lable `nvidia.com/gpu` .&#x20;

    ```bash
    kubectl -n gpu-operator create -f \
      https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/time-slicing-config-all.yaml
    ```
* Sau đó, sử dụng lệnh `kubectl patch` để patch ClusterPolicy và bật GPU time-slicing. Lệnh patch chỉ hoạt động khi `ClusterPolicy` có trạng thái `Ready`.
* ```bash
  # Patch the ClusterPolicy
  kubectl patch clusterpolicies.nvidia.com/cluster-policy \
    -n gpu-operator --type merge \
    -p '{"spec": {"devicePlugin": {"config": {"name": "gpu-sharing-config", "default": "any"}}}}'

  # Disable DCGM exporter, time-slicing not support DCGM exporter
  kubectl patch clusterpolicies.nvidia.com/cluster-policy \
    -n gpu-operator --type merge \
    -p '{"spec": {"dcgmExporter": {"enabled": false}}}'
  ```

<figure><img src="../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Verify GPU time-slicing

* Bây giờ, bạn có thể deploy một application có 5 pods sử dụng GPU bằng cách apply yaml theo mấu [time-slicing-verification.yaml](https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/time-slicing-verification.yaml). Bởi vì cấu hình config map thiết lập bên trên đang có replica = 4 nên pod thứ 5 sẽ có trạng thái `Pending` state.&#x20;
*   Lần lượt deploy và verify GPU time-slicing của bạn qua các lệnh:&#x20;

    ```bash
    # Apply the manifest
    kubectl apply -f \
      https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/time-slicing-verification.yaml

    # Check the pods
    kubectl get pods

    # Check the logs of the TensorFlow pod
    kubectl logs <put-your-time-slicing-verification-pod-name> --tail 10

    # Get the event of pending pod
    kubectl events | grep "FailedScheduling"

    # [Optional] Clean the resources
    kubectl delete deploy time-slicing-verification
    ```

<figure><img src="../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Multi-process server (MPS)

* **NVIDIA Multi-Process Server (MPS)** là một giải pháp thay thế và tương thích nhị phân cho giao diện lập trình ứng dụng CUDA (API). Kiến trúc runtime của MPS được thiết kế để cho phép các ứng dụng CUDA đa quy trình hợp tác, thường là các tác vụ MPI, tận dụng khả năng Hyper-Q trên các GPU NVIDIA mới nhất (Kepler và sau đó). Hyper-Q cho phép các kernel CUDA được xử lý đồng thời trên cùng một GPU, điều này có thể mang lại lợi ích về hiệu suất khi dung lượng tính toán GPU không được sử dụng đầy đủ bởi một quy trình ứng dụng duy nhất. Bạn có thể tham khảo thêm về MPS tại [Multi-Process Service (MPS)](https://docs.nvidia.com/deploy/pdf/CUDA_Multi_Process_Service_Overview.pdf).

#### Configure MPS

* Để sử dụng MPS cho cluster của bạn, bạn cần tạo tệp tin `ConfigMap` theo mẫu bên dưới để định nghĩa cấu hình MPS. Trong đó:&#x20;
  * `replicas`: field chỉ định số lượng pods có thể share chung GPU.
  * name: mặc định nvidia.com/gpu - lable sử dụng để filter node có GPU.
  * minStrategy: mặc định none do GPU hiện tại chưa hỗ trợ MIG.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: gpu-sharing-config
data:
  any-mps: |-
    version: v1
    flags:
      migStrategy: none            # MIG strategy is not used, this field SHOULD depends on your GPU model
    sharing:
      mps:                         # Enable MPS for the GPU
        resources:
        - name: nvidia.com/gpu     # Only apply for the node with the node.status contains 'nvidia.com/gpu'
          replicas: 4              # Allow 4 pods to share the GPU
```

*   Hoặc bạn có thể chạy câu lệnh bên dưới để apply cấu hình trên cho tất cả các node trong cluster của bạn có lable `nvidia.com/gpu` .&#x20;

    ```bash
    # Delete the old configmap
    kubectl -n gpu-operator delete cm gpu-sharing-config
    kubectl -n gpu-operator create -f \
      https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/mps-config-all.yaml
    ```
* Sau đó, sử dụng lệnh `kubectl patch` để patch ClusterPolicy và bật GPU MPS. Lệnh patch chỉ hoạt động khi `ClusterPolicy` có trạng thái `Ready`.

```bash
# Patch the ClusterPolicy
kubectl patch clusterpolicies.nvidia.com/cluster-policy \
  -n gpu-operator --type merge \
  -p '{"spec": {"devicePlugin": {"config": {"name": "gpu-sharing-config", "default": "any-mps"}}}}'

# Disable DCGM exporter, MPS not support DCGM exporter
kubectl patch clusterpolicies.nvidia.com/cluster-policy \
  -n gpu-operator --type merge \
  -p '{"spec": {"dcgmExporter": {"enabled": false}}}'

# Check MPS server is running or not
kubectl -n gpu-operator get pods
```

#### Verify MPS

* Bây giờ, bạn có thể deploy một application có 5 pods sử dụng GPU bằng cách apply yaml theo mẫu [mps-verification.yaml](https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/mps-verification.yaml). Bởi vì cấu hình config map thiết lập bên trên đang có replica = 4 nên pod thứ 5 sẽ có trạng thái `Pending` state.&#x20;
* Lần lượt deploy và verify GPU MPS của bạn qua các lệnh:&#x20;

```bash
# Apply the manifest
kubectl apply -f \
  https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/mps-verification.yaml

# Check the pods
kubectl get pods

# Check the logs of the TensorFlow pod
kubectl logs -l job-name=nbody-sample

# [Optional] Clean the resources
kubectl delete job nbody-sample
```

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**

* Trên một node GPU chỉ có thể sử dụng một trong hai chiến lược chia sẻ GPU là Time Slicing hoặc MPS, không thể sử dụng đồng thời cả hai. Lý do là vì cả hai chiến lược đều sử dụng cùng một tài nguyên GPU vật lý, và việc sử dụng cả hai đồng thời sẽ dẫn đến xung đột và hiệu suất không mong muốn.
* Tuy nhiên, nếu bạn có một node group gồm nhiều node GPU, bạn có thể sử dụng hai chiến lược khác nhau trên hai node riêng biệt. Ví dụ: bạn có thể sử dụng Time Slicing trên một node để chia sẻ GPU và sử dụng MPS trên node còn lại để chia sẻ GPU cho các ứng dụng khác. Chi tiết tham khảo mục bên dưới.
{% endhint %}

### Applying Multiple Node-Specific Configurations

* Nếu bạn có một node group gồm nhiều node GPU, bạn có thể sử dụng hai chiến lược khác nhau trên hai node riêng biệt. Ví dụ: bạn có thể sử dụng Time Slicing trên một node để chia sẻ GPU và sử dụng MPS trên node còn lại để chia sẻ GPU cho các ứng dụng khác. Ví dụ, tôi đã tạo 2 node group trong một Cluster với các thông số như sau:&#x20;
  * NodeGroup 1 có instance GPU RTX 2080Ti.
  * NodeGroup 2 có instance GPU RTX 4090.

Hiện tại, bạn mong muốn:&#x20;

* NodeGroup 1 có instance GPU RTX 2080Ti sẽ chạy 4 pods sharing GPU sử dụng time-slicing.
* NodeGroup 2 có instance GPU RTX 4090 sẽ chạy 8 pods sharing GPU sử dụng MPS.

#### Configure Multiple Node-Specific Configurations

*   Để sử dụng GPU time-slicing, MPS cho cluster của bạn, bạn cần tạo tệp tin `ConfigMap` theo mẫu bên dưới để định nghĩa cấu hình time-slicing, MPS mong muốn.&#x20;

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: gpu-multi-sharing-config
    data:
      rtx-2080ti: |-                                # Same the name with the name that you label the GPU node before
        version: v1
        flags:
          migStrategy: none                         # MIG strategy is not used, this field SHOULD depends on your GPU model
        sharing:
          timeSlicing:
            resources:
            - name: nvidia.com/gpu
              replicas: 4                           # Allow the node using this GPU to be shared by 4 pods
      rtx-4090: |-                                  # Same the name with the name that you label the GPU node before
        version: v1
        flags:
          migStrategy: none                         # MIG strategy is not used, this field SHOULD depends on your GPU model
        sharing:
          mps:
            resources:
            - name: nvidia.com/gpu
              replicas: 8                           # Allow the node using this GPU to be shared by 8 pods
    ```
*   Hoặc bạn có thể chạy câu lệnh bên dưới để apply cấu hình trên cho tất cả các node trong cluster của bạn có lable `nvidia.com/gpu` .

    ```bash
    kubectl -n gpu-operator create -f \
      https://raw.githubusercontent.com/vngcloud/kubernetes-sample-apps/main/nvidia-gpu/manifest/multiple-gpu-sharing.yaml
    ```
* Sau đó, sử dụng lệnh `kubectl patch` để patch ClusterPolicy và bật GPU time-slicing, MPS. Lệnh patch chỉ hoạt động khi `ClusterPolicy` có trạng thái `Ready`.

```bash
# Patch the ClusterPolicy
kubectl patch clusterpolicies.nvidia.com/cluster-policy \
  -n gpu-operator --type merge \
  -p '{"spec": {"devicePlugin": {"config": {"name": "gpu-multi-sharing-config"}}}}'

# Disable DCGM exporter
kubectl patch clusterpolicies.nvidia.com/cluster-policy \
  -n gpu-operator --type merge \
  -p '{"spec": {"dcgmExporter": {"enabled": false}}}'

# Check the ClusterPolicy
kubectl get clusterpolicy
```

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Bây giờ, bạn cần thêm label cho node với tên mà bạn chỉ định tại trong file `ConfigMap`:

```bash
# Get the node names
kubectl get nodes

# Label the node with the name that you specified in the ConfigMap
kubectl label node <node-name> nvidia.com/device-plugin.config=rtx-2080ti
kubectl label node <node-name> nvidia.com/device-plugin.config=rtx-4090
```

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Verify Multiple Node-Specific Configurations

*   Bên dưới đây là câu lệnh chúng tôi hướng dẫn bạn training MNIST model trong TensorFlow sử dụng 2 node GPU RTX 2080Ti và RTX 4090. Node RTX 2080Ti sẽ được share chung cho 4 pods sử dụng Time-slicing và node RTX 4090 sẽ được share chung cho 8 pods sử dụng MPS. Tham khảo thêm về TensorFlow tại [tensorflow-mnist-sample.yaml](https://github.com/vngcloud/kubernetes-sample-apps/raw/main/nvidia-gpu/manifest/tensorflow-mnist-sample.yaml).

    ```bash
    # Apply the manifest
    kubectl apply -f \
      https://github.com/vngcloud/kubernetes-sample-apps/raw/main/nvidia-gpu/manifest/tensorflow-mnist-sample.yaml

    # Check the pods
    kubectl get pods -owide

    # Check the logs of the TensorFlow pod
    kubectl logs <put-your-favourite-tensorflow-mnist-pod-name> --tail 20

    # [Optional] Clean the resources
    kubectl delete deploy tensorflow-mnist
    ```

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Giám sát hoạt động GPU Resources

* Giám sát tài nguyên GPU NVIDIA trong cụm Kubernetes là điều cần thiết để đảm bảo hiệu suất tối ưu, sử dụng tài nguyên hiệu quả và giải quyết vấn đề một cách chủ động. Sau đây là hướng dẫn của chúng tôi về việc thiết lập và sử dụng Prometheus và NVIDIA Data Center GPU Manager (DCGM) để giám sát tài nguyên GPU trong môi trường Kubernetes.
*   Đầu tiên, bạn cần cài đặt **Prometheus Stack** và **Prometheus Adapter** để tích hợp với Kubernetes API server qua lệnh:

    ```bash
    # Install Prometheus Stack using Helm
    helm install --wait prometheus-stack \
      --namespace prometheus --create-namespace \
      oci://vcr.vngcloud.vn/81-vks-public/vks-helm-charts/kube-prometheus-stack \
      --version 60.0.2 \
      --set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false

    # Install and configure Prometheus Adapter using Helm 
    prometheus_service=$(kubectl get svc -n prometheus -lapp=kube-prometheus-stack-prometheus -ojsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}')
    helm install --wait prometheus-adapter \
      --namespace prometheus --create-namespace \
      oci://vcr.vngcloud.vn/81-vks-public/vks-helm-charts/prometheus-adapter \
      --version 4.10.0 \
      --set prometheus.url=http://${prometheus_service}.prometheus.svc.cluster.local
    ```

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   Sau khi cài đặt thành công, chạy lệnh bên dưới để kiểm tra các resource Prometheus đang chạy:

    ```bash
    # Check the resources of Prometheus are running
    kubectl -n prometheus get all 
    ```

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   Tiếp theo, bạn cần chạy lệnh bên dưới để enable DCGM exporter để giám sát GPU resources trên cluster của bạn:

    ```bash
    # Enable the DCGM exporter
    kubectl patch clusterpolicies.nvidia.com/cluster-policy \
      -n gpu-operator --type merge \
      -p '{"spec": {"dcgmExporter": {"enabled": true}}}'

    # Confirm Prometheus can scrape the DCGM exporter metrics, sometime you MUST wait for a few minutes
    # (about 1-3 mins) for the DCGM exporter to be ready
    kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq -r . | grep DCGM
    ```

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Bây giờ, bạn hãy chạy lệnh bên dưới để chuyển Prometheus Adapter tới máy localhost của bạn và sau đó kiểm tra các metrics đã thu thập được thông qua [http://localhost:9090](http://localhost:9090)

```bash
# Forward the Prometheus Adapter to your local machine
kubectl -n prometheus \
  port-forward svc/prometheus-stack-kube-prom-prometheus 9090:9090
```

<figure><img src="../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Bên dưới là danh sách một vài GPU Metrics được sử dụng thường xuyên. Tham khảo danh sách GPU metric đầy đủ tại [Field Identifiers](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html).
  *   **Bảng 1**: Usage

      <table><thead><tr><th width="298">Metric Name</th><th width="105">Metric Type</th><th width="131">Unit</th><th>Description</th></tr></thead><tbody><tr><td><code>DCGM_FI_DEV_GPU_UTIL</code></td><td>Gauge</td><td>Percentage</td><td>GPU usage.</td></tr><tr><td><code>DCGM_FI_DEV_MEM_COPY_UTIL</code></td><td>Gauge</td><td>Percentage</td><td>Memory usage.</td></tr><tr><td><code>DCGM_FI_DEV_ENC_UTIL</code></td><td>Gauge</td><td>Percentage</td><td>Encoder usage.</td></tr><tr><td><code>DCGM_FI_DEV_DEC_UTIL</code></td><td>Gauge</td><td>Percentage</td><td>Decoder usage.</td></tr></tbody></table>
  *   **Bảng 2**: Memory

      <table><thead><tr><th width="245">Metric Name</th><th width="118">Metric Type</th><th width="74">Unit</th><th>Description</th></tr></thead><tbody><tr><td><code>DCGM_FI_DEV_FB_FREE</code></td><td>Gauge</td><td>MB</td><td>Number of remaining frame buffers. The frame buffer is called VRAM.</td></tr><tr><td><code>DCGM_FI_DEV_FB_USED</code></td><td>Gauge</td><td>MB</td><td>Number of used frame buffers. The value is the same as the value of memory-usage in the nvidia-smi command.</td></tr></tbody></table>
  *   **Bảng 3**: Temperature and power

      <table><thead><tr><th width="283">Metric Name</th><th width="116">Metric Type</th><th width="62">Unit</th><th>Description</th></tr></thead><tbody><tr><td><code>DCGM_FI_DEV_GPU_TEMP</code></td><td>Gauge</td><td>°C</td><td>Current GPU temperature of the device.</td></tr><tr><td><code>DCGM_FI_DEV_POWER_USAGE</code></td><td>Gauge</td><td>W</td><td>Power usage of the device.</td></tr></tbody></table>

***

## Autoscaling GPU Resources

* Để enable autoscaling GPU Resource, bạn cần:
  * Bật tính năng **Autoscale** cho GPU Nodegroups theo hướng dẫn tại [đây](../node-groups/auto-scaling.md).
  * Cài đặt [**Keda**](https://keda.sh/) thông qua Helm chart trên Cluster của bạn qua lệnh:

```bash
helm install --wait kedacore \
  --namespace keda --create-namespace \
  oci://vcr.vngcloud.vn/81-vks-public/vks-helm-charts/keda \
  --version 2.14.2

kubectl -n keda get all
```

<figure><img src="../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   **Nếu BẠN KHÔNG cài đặt Keda trong cụm của mình**, tính năng Auto-scale của VKS sẽ can thiệp vào và:

    * Phát hiện các pod đang ở trạng thái chờ (Pending).
    * Tự động mở rộng Nodegroup chứa GPU để xử lý các pod này.

    Điều này xảy ra khi **số replica Deployment lớn hơn số GPU khả dụng mà bạn đã cấu hình trong ConfigMap**.
*   **Nếu BẠN CÓ cài đặt Keda trong cụm của mình**, bạn có thể sử dụng `ScaledObject` để scale GPU Nodegroup dựa trên metrics mà bạn mong muốn. Ví dụ, bạn có thể scale GPU Nodegroup dựa trên GPU usage, memory usage hoặc các metrics khác. Ví dụ:

    ```yaml
    apiVersion: keda.sh/v1alpha1
    kind: ScaledObject
    metadata:
      name: scaled-object
    spec:
      scaleTargetRef:
        name: scaling-app   # The name of the Deployment, MUST in same namespace
      minReplicaCount: 1   # Optional. Default: 0
      maxReplicaCount: 3   # Optional. Default: 100
      triggers: # Will be trigger if either of these triggers is true
        - type: prometheus
          metadata: # prometheus-stack-kube-prom-prometheus
            serverAddress: http://prometheus-stack-kube-prom-prometheus.prometheus.svc.cluster.local:9090
            metricName: engine_active
            query: sum(DCGM_FI_DEV_GPU_UTIL) / count(DCGM_FI_DEV_GPU_UTIL) / 100
            threshold: '0.5'  # Scale the GPU Nodegroup when the GPU usage is greater than 50%
        - type: prometheus
          metadata: # prometheus-stack-kube-prom-prometheus
            serverAddress: http://prometheus-stack-kube-prom-prometheus.prometheus.svc.cluster.local:9090
            metricName: engine_active
            query: sum(DCGM_FI_DEV_MEM_COPY_UTIL) / count(DCGM_FI_DEV_MEM_COPY_UTIL) / 100
            threshold: '0.5'  # Scale the GPU Nodegroup when the GPU memory usage is greater than 50%
    ```
* Cấu hình này điều chỉnh số lượng GPU trong Nodegroup dựa trên GPU usage và memory usage. Trong đó:
  * Field`query` chỉ định truy vấn để lấy số liệu từ Prometheus.&#x20;
  * Field`threshold` chỉ định giá trị ngưỡng để điều chỉnh số lượng GPU trong Nodegroup.&#x20;
  * Field `minReplicaCount` và `maxReplicaCount` chỉ định số lượng tối thiểu và tối đa mà Nodegroup GPU có thể điều chỉnh đến.
* Apply [scaling-app.yaml](https://github.com/vngcloud/kubernetes-sample-apps/raw/main/nvidia-gpu/manifest/scaling-app.yaml) manifest to generate resources for testing the autoscaling feature. This manifest run 1 pod of CUDA VectorAdd Test and the GPU Nodegroup will be scaled to 3 when the GPU usage is greater than 50%.
*   Thực hiện apply tệp tin [scaling-app.yaml](https://github.com/vngcloud/kubernetes-sample-apps/raw/main/nvidia-gpu/manifest/scaling-app.yaml) để generate resources sử dụng verify cho tính năng autoscaling:&#x20;

    ```bash
    kubectl apply -f \
      https://github.com/vngcloud/kubernetes-sample-apps/raw/main/nvidia-gpu/manifest/scaling-app.yaml
    ```
*   Tiếp tục thực hiện apply tệp tin [scale-gpu.yaml](https://github.com/vngcloud/kubernetes-sample-apps/raw/main/nvidia-gpu/manifest/scale-gpu.yaml) để tạo `ScaleObject` cho deplyment của bạn:

    ```bash
    kubectl apply -f \
      https://github.com/vngcloud/kubernetes-sample-apps/raw/main/nvidia-gpu/manifest/scale-gpu.yaml

    kubectl get deploy

    # Check the ScaledObject
    kubectl get scaledobject
    ```

<figure><img src="../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Khi trạng thái `ScaledObject` **Ready** là`True`,  GPU Nodegroup được scale dựa trên GPU usage.
