# Quản lý vContainer với Terraform

#### Để quản lý vContainer với Terraform, bạn cần làm các bước sau đây: <a href="#quanlyvcontainervoiterraform-dequanlyvcontainervoiterraform-bancanlamcacbuocsauday" id="quanlyvcontainervoiterraform-dequanlyvcontainervoiterraform-bancanlamcacbuocsauday"></a>

### **Cài đặt Terraform CLI** <a href="#quanlyvcontainervoiterraform-caidatterraformcli" id="quanlyvcontainervoiterraform-caidatterraformcli"></a>

Để có thể quản lý vContainer với Terraform bạn cần cài đặt Terraform CLI theo hướng dẫn [tại đây ](cai-dat-terraform.md)

***

### **Cấp quyền IAM cho việc sử dụng**  <a href="#quanlyvcontainervoiterraform-capquyeniamchoviecsudung" id="quanlyvcontainervoiterraform-capquyeniamchoviecsudung"></a>

Để có thể thực hiện quản lý vContainer với Terraform bạn cần tạo **Service account** từ Root account trên trang chủ **IAM** (xem hướng dẫn cách tạo Service account và sử dụng IAM [tại đây](../quan-ly-dinh-danh-va-truy-cap-iam-cho-vserver/)), trong trường hợp này lấy ví dụ cho việc bạn muốn tạo Kubernetes Cluster (K8S) với Terraform cần có các quyền (Policy) sau:

* CreateCluster
* GetCluster (specify by **all resources**)
* ListClusterSecGroupDefault (specify by **all resources**)
* GetClusterConfig (specify by **all resources**)

hoặc bạn có thể cấp quyền **vServerFullAccess** (nên có quyền **vServerReadOnlyAccess** để get thông tin resource sau khi tạo xong). Tham khảo thêm về cách phân quyền cho từng **Resource, Action** tương ứng tại [{Trang phân quyền IAM}](../quan-ly-dinh-danh-va-truy-cap-iam-cho-vserver/cac-hanh-dong-tai-nguyen-va-dieu-kien-can-cho-phan-quyen-truy-cap-vserver.md).

> **Ghi chú:** Mỗi hành động quản lý tài nguyên khác nhau sẽ yêu cầu các quyền khác nhau, vì thế điều cần thiết là phải thiết lập một bộ phân quyền hợp lý phù hợp với nhu cầu kinh doanh của bạn.

***

### **Tạo thư mục chứa terraform file** **và tải example file từ VNG Cloud repo** <a href="#quanlyvcontainervoiterraform-taothumucchuaterraformfilevataiexamplefiletuvngcloudrepo" id="quanlyvcontainervoiterraform-taothumucchuaterraformfilevataiexamplefiletuvngcloudrepo"></a>

Sau khi cấp quyền IAM cho account cần sử dụng Terraform, bạn cần tạo một thư mục chứa file Terraform để cài đặt các thông số trên đó, bạn có thể tải file Example từ VNG Cloud repo của chúng tôi tại [đây](https://github.com/vngcloud/terraform-provider-vngcloud/tree/main/examples)

***

### **Cài đặt thông số trong Terraform file** <a href="#quanlyvcontainervoiterraform-caidatthongsotrongterraformfile" id="quanlyvcontainervoiterraform-caidatthongsotrongterraformfile"></a>

1.  Sau khi tải thư mục Example về máy, mở file [_**variable.tf**_](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/variable.tf) _(theo đường dẫn **/examples/ variable.tf**),_ sau đó thay đổi các thông tin cần thiết như sau:\
    **Client\_id:** Lấy tại trang chủ IAM/ Service accoun&#x74;**/ Tab Security credentials**

    **Client\_secret:** Lấy khi khởi tạo Service account tại trang chủ **IAM** hoặc có thể reset lại tại trang IAM/ Service accoun&#x74;**/ Tab Security credentials**

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```markup
variable "client_id" {  
type = string  
default = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
variable "client_secret" {  
type = string  
default = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
```

<figure><img src="https://docs.vngcloud.vn/download/attachments/59803481/image2023-6-8_16-29-29.png?version=1&#x26;modificationDate=1686293474000&#x26;api=v2" alt=""><figcaption></figcaption></figure>



2. Kiểm tra lại thông tin file [**main.tf**](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/main.tf) _**(**&#x74;heo đường dẫn **examples/main.tf)**_**,** trường hợp này bạn cần xóa đi các dòng bên dưới:

* _module "vserver" {source = "./modules/vng-cloud-vserver"_\
  &#xNAN;_}_
* _module "vlb" { source = "./modules/vng-cloud-vlb" }_

_Chỉ để lại:_

* module "k8s" {\
  source = "./modules/vng-cloud-k8s" }

```
terraform {  
required_providers {    
vngcloud = {      
source  = "vngcloud/vngcloud"      
version = "1.1.0"    
}  
}  
#  backend "s3" {  
#    skip_credentials_validation = true  
#    skip_metadata_api_check = true  
#    skip_region_validation = true  
#    bucket = "bucket-name"  
#    endpoint = "https://hcm01.vstorage.vngcloud.vn/"  
#    key = "terraform.tfstate"  
#    region = "HCM01"  
#    access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
#    secret_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
#  }
} 
provider "vngcloud" {  
token_url        = "https://iamapis.vngcloud.vn/accounts-api/v2/auth/token"  
client_id        = var.client_id  
client_secret    = var.client_secret  
vserver_base_url = "https://hcm-3.api.vngcloud.vn/vserver/vserver-gateway"  
vlb_base_url = "https://hcm-3.api.vngcloud.vn/vserver/vlb-gateway"}
module "k8s" {  
source = "./modules/vng-cloud-k8s" }
}
```

3. Sau đó truy cập vào thư mục **vng-cloud-vserver/ examples/ modules/ vng-cloud-k8s/**, và mở file [**variable.tf**](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/modules/vng-cloud-k8s/variable.tf)**:**

* **project\_id**: thông tin project của bạn, bạn có thể lấy ở [{Tab Limit}](https://hcm-3.console.vngcloud.vn/vserver/limit) trên vServer Portal, Ví dụ: **pro-462803f3-6858-466f-bf05-df2b33faa360:**

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **image\_id**: hệ điều hành để khởi tạo vServer ví dụ như: **img-b5bf635e-0456-4765-b493-31d5fcfc05aa** (1\_Ubuntu-22.04x64) ... hiện tại chúng tôi để mặc định image của K8S là Fedora (**Lưu ý**: Thông số này không thể sửa)

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **flavor\_id**: cấu hình vServer mà bạn sẽ khởi tạo ví dụ: flav-e2028a81-cc75-47e4-8af1-9eef2f857f84 (s-general-2x4) ,... bạn có thể xem danh sách khi tạo vServer trên Portal/ [{Tab Flavors}](https://hcm-3.console.vngcloud.vn/vserver/v-server/flavor).

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```
variable "project_id" {  
type    = string  
default = "pro-462803f3-6858-466f-bf05-df2b33faa360"
}
variable "s_general_4x8" {  
type    = string  
default = "flav-05f97524-0410-46a4-87a8-af92aa759231"}
variable "ubuntu_20_04" {  
type    = string  
default = "img-a34d639b-e070-46ff-8b91-addf4fac45b4"
}
```

* **volume\_type\_name**: chỉ định IOPS cho root disk và data disk, ví dụ: **SSD-3000, SSD-200, SSD-400,** bạn có thể xem danh sách Volume Type trên vServer Portal/ [{Tab Volume Type}](https://hcm-3.console.vngcloud.vn/vserver/v-server/system-image)\


<figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **root\_disk\_size**: chỉ định dung lượng ổ root disk, ví dụ: **20**
* **data\_disk\_size**: chỉ định dung lượng ổ root disk, ví dụ: **50**

```
variable "ssd_3000" {  
type    = string  
default = "3000"
}
variable "root_disk_size" {  
type    = number  
default = 20
}
variable "data_disk_size" {  
type    = number  
default = 50
}
```

* **network\_id**: chỉ định network id mà vServer sẽ được tạo trên đó, bạn có thể lấy từ tab [VPC](https://hcm-3.console.vngcloud.vn/vserver/network/vpc), nếu chưa khởi tạo bất cứ network nào bạn có thể xem hướng dẫn [{Trang tạo VPC}](../network/virtual-private-cloud-vpc/):\


<figure><img src="../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **subnet\_id**: chỉ định subnet id mà vServer sẽ được tạo trên đó, bạn có thể lấy từ [{Tab VPC}](https://hcm-3.console.vngcloud.vn/vserver/network/vpc), nếu chưa khởi tạo bất cứ subnet nào bạn có thể xem hướng dẫn tại [{Trang tạo subnet}](../network/virtual-private-cloud-vpc/):

```
variable "network_id" {  
type    = string  
default = "net-22581aed-a65d-4b1e-86d3-102d68e148e0"
}
variable "subnet_id" {  
type    = string  
default = "sub-5f101cba-7ce0-4084-8576-06b8dbfb298a" }
```

<figure><img src="../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   **ssh\_key\_id**: chỉ định ssh key sẽ được inject vào vServer, bạn có thể lấy ở [{Tab SSH Keys}](https://hcm-3.console.vngcloud.vn/vserver/v-server/ssh-key), nếu chưa khởi tạo bất kì ssh key nào bạn có thể xem tại [{](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647901)[T](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647901)[rang tạo SSH key](../security/ssh-key-bo-khoa.md)[}](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647901): \


    <figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **security\_group\_id\_list**: chỉ định danh sách security group id cần gắn vào vServer, bạn có thể lấy ở [{Tab Security Groups}](https://hcm-3.console.vngcloud.vn/vserver/network/sec-group), nếu cần tạo thêm security group bạn có thể xem tại [{Trang tạo Security Group}](../security/security-groups.md):

```
variable "ssh_key_id" {  
type    = string  
default = "ssh-b4fbf87a-d9bc-4f04-9ea1-39e086f443de"
}
variable "security_group_id_list" {  
type    = list(string)  
default = [    "secg-28e91c47-11b1-4cc1-8e24-dd174882708d"  ]
}
```

<figure><img src="../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Kiểm tra lại thông tin file [**main.tf**](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/modules/vng-cloud-k8s/main.tf) _(theo đường dẫn **terraform-provider-vngcloud/examples/modules/vng-cloud-k8s/main.tf**)_, trong file chúng tôi để sẵn một số câu lệnh: **Create K8S**, **Create Cluster Node Group, Change Cluster for SecGroup, Attach Load Balancer for K8s...,** trường hợp này để Tạo mới K8S bạn chỉ  cần để lại resource **Create K8S** theo hướng dẫn bên dưới:

```
data "vngcloud_vserver_volume_type_zone" "volume_type_zone" {  
name       = "SSD"  
project_id = var.project_id
} 
data "vngcloud_vserver_volume_type" "volume_type" {  
name                = var.volume_type_name  
project_id          = var.project_id  
volume_type_zone_id = data.vngcloud_vserver_volume_type_zone.volume_type_zone.id
} 
data "vngcloud_vserver_k8s_version" "k8sVersion1" {  
name       = "Version 1.18.7"  
project_id = var.project_id
} 
data "vngcloud_vserver_k8s_network_type" "k8sNetworkType" {  
name       = "Calico"  
project_id = var.project_id
} resource "vngcloud_vserver_k8s" "k8s" {  
project_id            = var.project_id  
ipip_mode             = "Always"  
name                  = "vng-cloud-k8s-example"  
k8s_version           = data.vngcloud_vserver_k8s_version.k8sVersion1.id  
master_count          = 1  
node_count            = 1  
network_type          = data.vngcloud_vserver_k8s_network_type.k8sNetworkType.id  
calico_cidr           = "10.46.0.0/16"  
network_id            = var.network_id  
subnet_id             = var.subnet_id  
ssh_key_id            = var.ssh_key_id  
master_flavor_id      = var.s_general_4x8  
node_flavor_id        = var.s_general_4x8  
etcd_volume_size      = 20  
etcd_volume_type_id   = data.vngcloud_vserver_volume_type.volume_type.id  
boot_volume_size      = 20  
boot_volume_type_id   = data.vngcloud_vserver_volume_type.volume_type.id  
docker_volume_size    = 20  
docker_volume_type_id = data.vngcloud_vserver_volume_type.volume_type.id  
description           = "K8S example"  
auto_scaling          = true  
min_node_count        = 1  
max_node_count        = 3  
enable_lb             = false  
auto_healing          = true  
ingress_controller = true
}
```

***

### **Khởi chạy Terraform command** <a href="#quanlyvcontainervoiterraform-khoichayterraformcommand" id="quanlyvcontainervoiterraform-khoichayterraformcommand"></a>

1. Sau khi hoàn tất các thông tin trên, để terraform khởi tạo và tải VNG Cloud provider về đồng thời thiết lập các thông tin cần thiết chạy lệnh bên dưới, lưu ý khi chạy cần đứng tại thư mục terraform-provider-vngcloud/ [**examples**](https://github.com/vngcloud/terraform-provider-vngcloud/tree/main/examples)/:&#x20;

```
terraform init
```

2. Hệ thống sẽ trả ra kết quả:

```
vnglab:vngcloud cbr09$ terraform init 

Initializing the backend... 

Initializing provider plugins...
- Finding vngcloud/vngcloud versions matching "0.0.5"...
- Installing vngcloud/vngcloud v0.0.5...
- Installed vngcloud/vngcloud v0.0.5 (self-signed, key ID A6A27B3126EF15EB) 
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html 

Terraform has created a lock file .terraform.lock.hcl to record the providerselections it made above. Include this file in your version control repositoryso that Terraform can guarantee to make the same selections by default whenyou run "terraform init" in the future. 

Terraform has been successfully initialized! 

You may now begin working with Terraform. Try running "terraform plan" to seeany changes that are required for your infrastructure. All Terraform commandsshould now work. 

If you ever set or change modules or backend configuration for Terraform,rerun this command to reinitialize your working directory. If you forget, othercommands will detect it and remind you to do so if necessary.
```

1.  Sau đó, bạn để xem những thay đổi sẽ được áp dụng trên những resource mà terraform đang quản lý bạn có thể chạy:\


    | `terraform plan` |
    | ---------------- |
2.  Cuối cùng bạn chọn chạy dòng lệnh:\


    | `terraform apply` |
    | ----------------- |
3. và chọn **YES** để thực hiện việc khởi tạo vServer thông qua Terraform

***

### **Kiểm tra Container vừa tạo trên giao diện VNG Cloud Portal** <a href="#quanlyvcontainervoiterraform-kiemtracontainervuataotrengiaodienvngcloudportal" id="quanlyvcontainervoiterraform-kiemtracontainervuataotrengiaodienvngcloudportal"></a>

Sau khi khởi tạo thành công Terraform, bạn có thể lên Portal để xem thông tin Container vừa tạo:

<figure><img src="../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
