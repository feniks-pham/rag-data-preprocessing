# Sử dụng Terraform để khởi tạo Cluster và Node Group

### Tổng quan

Terraform là một công cụ mã nguồn mở được sử dụng để tự động hóa việc cung cấp và quản lý cơ sở hạ tầng như máy ảo, mạng, lưu trữ và Kubernetes.

Với Terraform, bạn có thể mô tả cơ sở hạ tầng mong muốn bằng mã, sau đó Terraform sẽ thực hiện các thao tác cần thiết để tạo hoặc cập nhật cơ sở hạ tầng cho phù hợp với mô tả của bạn.

***

### **Khởi tạo Cluster và Node Group**

Để khởi tạo một Cluster Kubernetes bằng Terraform, bạn cần thực hiện các bước sau:

1. **Truy cập IAM Portal** tại [đây](https://iam.console.vngcloud.vn/), thực hiện tạo Service Account với quyền hạn **VKS Full Access**. Cụ thể, tại trang IAM, bạn có thể:
   * Chọn "**Create a Service Account**", điền tên cho Service Account và nhấn **Next Step** để gắn quyền cho Service Account.
   * Tìm và chọn **Policy:** **VKSFullAccess** sau đó nhấn "**Create a Service Account**" để tạo Service Account, **Policy: VKSFullAccess** do VNG Cloud tạo ra, bạn không thể xóa các policy này.
   * Sau khi tạo thành công bạn cần phải lưu lại **Client\_ID** và **Secret\_Key** của Service Account để thực hiện bước tiếp theo.
2. **Truy cập VKS Portal** tại [đây](https://vks.console.vngcloud.vn/overview)**, thực hiện Activate** dịch vụ VKS ở tab **Overview.** Hãy chờ đợi tới khi chúng tôi khởi tạo thành công tài khoản VKS của bạn.
3. **Cài đặt Terraform:**
   * Tải xuống và cài đặt Terraform cho hệ điều hành của bạn từ [https://developer.hashicorp.com/terraform/install](https://developer.hashicorp.com/terraform/install).
4. **Khởi tạo cấu hình Terraform:**
   * Tạo tệp `variable.tf` và khai báo thông tin Service Account trong file này.
   * Tạo tệp `main.tf` và định nghĩa các tài nguyên Kubernetes Cluster mà bạn muốn tạo.

Ví dụ:

* Tệp `variable.tf:`bạn cần thay thế Client ID và Client Secret đã khởi tạo ở bước 1 ở file này.

```
variable "client_id" {
  type = string
  default = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
variable "client_secret" {
  type = string
  default = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

* Tệp `main.tf:` trong ví dụ này tôi thực hiện khởi tạo một Cluster và một Node Group có thông tin sau:
  * Tên Cluster: my-cluster
  * K8S Version: v1.28.8
  * Mode: Public Cluster và Public Node Group
  * Tên Node Group: my-nodegroup
  * Bật AutoScaling: scale từ 0 tới 5 nodes

{% hint style="info" %}
**Chú ý:**

* Trong file main.tf, để khởi tạo một cluster với một node group, bạn bắt buộc cần truyền vào các thông số sau: &#x20;

```hcl
  vpc_id    = "net-xxxxxxxx-xxxx-xxxxx-xxxx-xxxxxxxxxxxx"
  subnet_id = "sub-xxxxxxxx-xxxx-xxxxx-xxxx-xxxxxxxxxxxx"
  ssh_key_id= "ssh-xxxxxxxx-xxxx-xxxxx-xxxx-xxxxxxxxxxxx"
```
{% endhint %}

* File `main.tf` mẫu giúp bạn tạo Cluster và Node Group theo cấu hình bên trên:

```
terraform {
  required_providers {
    vngcloud = {
      source  = "vngcloud/vngcloud"
      version = "1.2.2"
    }
  }
}

provider "vngcloud" {
  token_url        = "https://iamapis.vngcloud.vn/accounts-api/v2/auth/token"
  client_id        = var.client_id
  client_secret    = var.client_secret
  vserver_base_url = "https://hcm-3.api.vngcloud.vn/vserver/vserver-gateway"
  vlb_base_url     = "https://hcm-3.api.vngcloud.vn/vserver/vlb-gateway"
}

resource "vngcloud_vks_cluster" "primary" {
  name      = "my-cluster"
  description = "VNGCLOUD uses terraform"
  version = "v1.28.8"
  cidr      = "172.16.0.0/16"
  enable_private_cluster = false
  network_type = "CALICO"
  vpc_id    = "net-xxxxxxxx-xxxx-xxxxx-xxxx-xxxxxxxxxxxx"
  subnet_id = "sub-xxxxxxxx-xxxx-xxxxx-xxxx-xxxxxxxxxxxx"
  enabled_load_balancer_plugin = true
  enabled_block_store_csi_plugin = true
}

resource "vngcloud_vks_cluster_node_group" "primary" {
  cluster_id= vngcloud_vks_cluster.primary.id
  name= "my-nodegroup"
  num_nodes
  auto_scale_config {
    min_size = 0
    max_size = 5
  }
  upgrade_config {
    strategy = "SURGE"
    max_surge = 1
 max_unavailable = 0
  }
  image_id = "img-983d55cf-9b5b-44cf-aa72-23f3b25d43ce"
  flavor_id = "flav-9e88cfb4-ec31-4ad4-8ba5-243459f6dc4b"
  disk_size = 20
  disk_type = "vtype-61c3fc5b-f4e9-45b4-8957-8aa7b6029018"
  enable_private_nodes = false
  ssh_key_id= "ssh-xxxxxxxx-xxxx-xxxxx-xxxx-xxxxxxxxxxxx"
  labels = {
    "mylabel" = "vngcloud"
  }
  taint {
    key    = "mykey"
    value  = "myvalue"
    effect = "PreferNoSchedule"
  }
}
```

5. **Khởi tạo Terraform:**

* Chạy lệnh `terraform init.`Lệnh này sẽ tải xuống các plugin cần thiết và khởi tạo trạng thái Terraform.

6. **Áp dụng cấu hình Terraform:**

* Chạy lệnh `terraform apply.` Lệnh này sẽ tạo Cluster Kubernetes theo mô tả trong tệp `main.tf`.

Tham khảo thêm về cách sử dụng Terraform để làm việc với VKS tại [đây](https://registry.terraform.io/providers/vngcloud/vngcloud/latest/docs/resources/vks\_cluster).
