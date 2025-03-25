# Node

Trong Kubernetes, khái niệm "node" thường được sử dụng để chỉ các máy tính vật lý hoặc ảo trong một cluster mà Kubernetes quản lý. Cụ thể, "node" là một máy chủ làm nhiệm vụ chạy các container và cung cấp tài nguyên tính toán và môi trường thực thi cho các ứng dụng chạy trên Kubernetes.

Mỗi node trong Kubernetes có một tập hợp các tác vụ quan trọng:

* [**Container runtime**](https://kubernetes.io/docs/setup/production-environment/container-runtimes/): Điều này thường là Docker, Containerd, hoặc các runtime container khác, chịu trách nhiệm thực thi các container trên node.
* [**Kubelet**](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/): Là một thành phần chạy trên mỗi node và giám sát trạng thái của node, quản lý các container, và tương tác với API Server của Kubernetes.
* [**Kube-proxy**:](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/) Là một dịch vụ trên node để cung cấp kết nối mạng và định tuyến giữa các pod trên cùng một cluster.
* Các ứng dụng và container: Node chạy các ứng dụng được triển khai trong các pod. Mỗi pod là một nhóm các container liên quan đến nhau chia sẻ mạng và tài nguyên.

Khi triển khai ứng dụng trên Kubernetes, các pod được lên lịch chạy trên các node trong cluster. Kubelet trên mỗi node đảm bảo rằng pod được chạy đúng cách và duy trì trạng thái ổn định của node.

\
