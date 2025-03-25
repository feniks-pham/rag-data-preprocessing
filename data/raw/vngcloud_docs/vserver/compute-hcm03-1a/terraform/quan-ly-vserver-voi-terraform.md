# Quản lý vServer với Terraform

### **Cài đặt Terraform CLI** <a href="#quanlyvservervoiterraform-caidatterraformcli" id="quanlyvservervoiterraform-caidatterraformcli"></a>

Để có thể quản lý vServer với Terraform bạn cần cài đặt Terraform CLI theo hướng dẫn [tại đây ](cai-dat-terraform.md)

***

### **Cấp quyền IAM cho việc sử dụng**  <a href="#quanlyvservervoiterraform-capquyeniamchoviecsudung" id="quanlyvservervoiterraform-capquyeniamchoviecsudung"></a>

Để có thể thực hiện quản lý vContainer với Terraform bạn cần tạo **Service account** từ Root account trên trang chủ **IAM** (xem hướng dẫn cách tạo Service account và sử dụng IAM [tại đây](../quan-ly-dinh-danh-va-truy-cap-iam-cho-vserver/)), trong trường hợp này lấy ví dụ cho việc bạn muốn tạo Server với Terraform cần có các quyền (Policy) sau:

* CreateServer
* GetServer

hoặc bạn có thể cấp quyền **vServerFullAccess** (nên có quyền **vServerReadOnlyAccess** để get thông tin resource sau khi tạo xong). Tham khảo thêm về cách phân quyền cho từng **Resource, Action** tương ứng tại [{Trang phân quyền IAM}](../quan-ly-dinh-danh-va-truy-cap-iam-cho-vserver/cac-hanh-dong-tai-nguyen-va-dieu-kien-can-cho-phan-quyen-truy-cap-vserver.md).

> **Ghi chú:** Mỗi hành động quản lý tài nguyên khác nhau sẽ yêu cầu các quyền khác nhau, vì thế điều cần thiết là phải thiết lập một bộ phân quyền hợp lý phù hợp với nhu cầu kinh doanh của bạn.

***

### **Tạo thư mục chứa terraform file** **và tải example file từ VNG Cloud repo** <a href="#quanlyvservervoiterraform-taothumucchuaterraformfilevataiexamplefiletuvngcloudrepo" id="quanlyvservervoiterraform-taothumucchuaterraformfilevataiexamplefiletuvngcloudrepo"></a>

Sau khi cấp quyền IAM cho account cần sử dụng Terraform, bạn cần tạo một thư mục chứa file Terraform để cài đặt các thông số trên đó, bạn có thể tải file Example từ VNG Cloud repo của chúng tôi tại [đây](https://github.com/vngcloud/terraform-provider-vngcloud/tree/main/examples)



***

### **Cài đặt thông số trong Terraform file** <a href="#quanlyvservervoiterraform-caidatthongsotrongterraformfile" id="quanlyvservervoiterraform-caidatthongsotrongterraformfile"></a>

Sau khi tải thư mục Example về máy, người dùng mở file [_**variable.tf**_](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/variable.tf) _(theo đường dẫn **/examples/variable.tf**),_ sau đó thay đổi các thông tin cần thiết như sau:

* **Client\_id:** Lấy tại trang chủ IAM/ Service accoun&#x74;**/ Tab Security credentials**
* **Client\_secret:** Lấy khi khởi tạo Service account tại trang chủ **IAM** hoặc có thể reset lại tại trang IAM/ Service accoun&#x74;**/ Tab Security credentials**

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

| `variable "client_id"` `{  type` `= string  default = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}variable "client_secret"` `{  type` `= string  default = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}` |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Bước 4:** Kiểm tra lại thông tin file [**main.tf**](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/main.tf) _**(**&#x74;heo đường dẫn **examples/main.tf)**_**,** trường hợp này bạn cần xóa đi các dóng bên dưới:

* _module "k8s" { source = "./modules/vng-cloud-k8s" }_
* _module "vlb" { source = "./modules/vng-cloud-vlb" }_

_chỉ để lại:_

* _module "vserver" {_\
  &#xNAN;_&#x73;ource = "./modules/vng-cloud-vserver"_\
  &#xNAN;_}_

| `terraform {  required_providers {    vngcloud = {      source`  `= "vngcloud/vngcloud"      version = "1.1.0"    }  }  #  backend "s3" {  #    skip_credentials_validation = true  #    skip_metadata_api_check = true  #    skip_region_validation = true  #    bucket = "bucket-name"  #    endpoint = "`[`https://hcm01.vstorage.vngcloud.vn/`](https://hcm01.vstorage.vngcloud.vn/)`"  #    key = "terraform.tfstate"  #    region = "HCM01"  #    access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  #    secret_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  #  }}` `provider "vngcloud"` `{  token_url        = "`[`https://iamapis.vngcloud.vn/accounts-api/v2/auth/token`](https://iamapis.vngcloud.vn/accounts-api/v2/auth/token)`"  client_id        = var.client_id  client_secret    = var.client_secret  vserver_base_url = "`[`https://hcm-3.api.vngcloud.vn/vserver/vserver-gateway`](https://hcm-3.api.vngcloud.vn/vserver/vserver-gateway)`"  vlb_base_url = "`[`https://hcm-3.api.vngcloud.vn/vserver/vlb-gateway`](https://hcm-3.api.vngcloud.vn/vserver/vlb-gateway)`"}` `module "vserver"` `{  source` `= "./modules/vng-cloud-vserver"}` |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

\
**Bước 5:** Sau đó truy cập vào thư mục **vng-cloud-vserver/ examples/ modules/ vng-cloud-vserver/**, và mở file [**variable/tf**](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/modules/vng-cloud-vserver/variable.tf)**:**

* **project\_id**: thông tin project của bạn, bạn có thể lấy ở [{Tab Limit}](https://hcm-3.console.vngcloud.vn/vserver/limit) trên vServer Portal, Ví dụ: **pro-462803f3-6858-466f-bf05-df2b33faa360:**

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **image\_id**: hệ điều hành để khởi tạo vServer ví dụ như: **img-b5bf635e-0456-4765-b493-31d5fcfc05aa** (1\_Ubuntu-22.04x64) ... bạn có thể xem danh sách Id khi tạo vServer trên Portal/ [{Tab System Image}](https://hcm-3.console.vngcloud.vn/vserver/v-server/system-image)

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **flavor\_id**: cấu hình vServer mà bạn sẽ khởi tạo ví dụ: flav-e2028a81-cc75-47e4-8af1-9eef2f857f84 (s-general-2x4) ,... bạn có thể xem danh sách khi tạo vServer trên Portal/ [{Tab Flavors}](https://hcm-3.console.vngcloud.vn/vserver/v-server/flavor).

<figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

| `variable "project_id"` `{  type`    `= string  default = "pro-462803f3-6858-466f-bf05-df2b33faa360"}variable "s_general_4x8"` `{  type`    `= string  default = "flav-05f97524-0410-46a4-87a8-af92aa759231"}variable "ubuntu_20_04"` `{  type`    `= string  default = "img-a34d639b-e070-46ff-8b91-addf4fac45b4"}` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* **volume\_type\_name**: chỉ định IOPS cho root disk và data disk, ví dụ: **SSD-3000, SSD-200, SSD-400,** bạn có thể xem danh sách Volume Type trên vServer Portal/ [{Tab Volume Type}](https://hcm-3.console.vngcloud.vn/vserver/v-server/system-image)

<figure><img src="../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **root\_disk\_size**: chỉ định dung lượng ổ root disk, ví dụ: **20**
* **data\_disk\_size**: chỉ định dung lượng ổ root disk, ví dụ: **50**

| `variable "ssd_3000"` `{  type`    `= string  default = "3000"}variable "root_disk_size"` `{  type`    `= number  default = 20}variable "data_disk_size"` `{  type`    `= number  default = 50}` |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

* **network\_id**: chỉ định network id mà vServer sẽ được tạo trên đó, bạn có thể lấy từ tab [VPC](https://hcm-3.console.vngcloud.vn/vserver/network/vpc), nếu chưa khởi tạo bất cứ network nào bạn có thể xem hướng dẫn [{Trang tạo network}](../network/virtual-private-cloud-vpc/):

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650384/image2023-6-9_9-55-7.png?version=1&#x26;modificationDate=1686279309000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **subnet\_id**: chỉ định subnet id mà vServer sẽ được tạo trên đó, bạn có thể lấy từ [{Tab VPC}](https://hcm-3.console.vngcloud.vn/vserver/network/vpc), nếu chưa khởi tạo bất cứ subnet nào bạn có thể xem hướng dẫn tại [{Trang tạo subnet}](../network/virtual-private-cloud-vpc/)

<figure><img src="../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

| `variable "network_id"` `{  type`    `= string  default = "net-22581aed-a65d-4b1e-86d3-102d68e148e0"}variable "subnet_id"` `{  type`    `= string  default = "sub-5f101cba-7ce0-4084-8576-06b8dbfb298a"` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

\


* **ssh\_key\_id**: chỉ định ssh key sẽ được inject vào vServer, bạn có thể lấy ở [{Tab SSH Keys}](https://hcm-3.console.vngcloud.vn/vserver/v-server/ssh-key), nếu chưa khởi tạo bất kì ssh key nào bạn có thể xem tại [{](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647901)[T](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647901)[rang tạo SSH key](../security/ssh-key-bo-khoa.md)[}](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49647901):&#x20;

<figure><img src="../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **security\_group\_id\_list**: chỉ định danh sách security group id cần gắn vào vServer, bạn có thể lấy ở [{Tab Security Groups}](https://hcm-3.console.vngcloud.vn/vserver/network/sec-group), nếu cần tạo thêm security group bạn có thể xem tại [{Trang tạo Security Group}](../security/security-groups.md)

<figure><img src="../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

| `variable "ssh_key_id"` `{  type`    `= string  default = "ssh-b4fbf87a-d9bc-4f04-9ea1-39e086f443de"}variable "security_group_id_list"` `{  type`    `= list(string)  default = [    "secg-28e91c47-11b1-4cc1-8e24-dd174882708d"  ]}` |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

\


**Bước 6:** Kiểm tra lại thông tin file [main.tf](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/modules/vng-cloud-vserver/main.tf) _(theo đường dẫn **terraform-provider-vngcloud/examples/modules/vng-cloud-vserver/**)_, trong file chúng tôi để sẵn một số câu lệnh: **Create Server**, **Create Volume, Attach volume to Server,** trường hợp này để Tạo mới Server bạn chỉ cần để lại resource **Create Server** theo hướng dẫn bên dưới:

| `data "vngcloud_vserver_volume_type_zone"` `"volume_type_zone"` `{  name       = "SSD"  project_id = var.project_id}data "vngcloud_vserver_volume_type"` `"volume_type"` `{  name                = var.ssd_3000  project_id          = var.project_id  volume_type_zone_id = data.vngcloud_vserver_volume_type_zone.volume_type_zone.id}` `resource "vngcloud_vserver_server"` `"server"` `{  count             = var.server_count  project_id        = var.project_id  name              = "vngcloud-tinbhn22-${count.index}"  encryption_volume = false  attach_floating   = true  flavor_id         = var.s_general_4x8  image_id          = var.ubuntu_20_04  network_id        = var.network_id  root_disk_size    = var.root_disk_size  root_disk_type_id = data.vngcloud_vserver_volume_type.volume_type.id  security_group    = var.security_group_id_list  subnet_id         = var.subnet_id  action            = "start"  #  user_name         = "stackops"  #  user_password     = "Vng@Cloud3030"  #  expire_password   = false  #  ssh_key           = var.ssh_key_id  #user_data_base64_encode = var.user_data_base64_encode  #user_data               = "${data.template_cloudinit_config.user_data.rendered}"  lifecycle {    create_before_destroy = true  }}` |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

\


**Bước 7:** Khởi chạy terraform command

* Sau khi hoàn tất các thông tin trên, để terraform khởi tạo và tải VNG Cloud provider về đồng thời thiết lập các thông tin cần thiết chạy lệnh bên dưới, lưu ý khi chạy cần đứng tại thư mục terraform-provider-vngcloud/ [examples](https://github.com/vngcloud/terraform-provider-vngcloud/tree/main/examples)/: \


| `terraform init` |
| ---------------- |

Hệ thống sẽ trả ra kết quả:

| `vnglab:vngcloud cbr09$ terraform init` `Initializing the backend...` `Initializing provider plugins...- Finding vngcloud/vngcloud` `versions matching "0.0.5"...- Installing vngcloud/vngcloud` `v0.0.5...- Installed vngcloud/vngcloud` `v0.0.5 (self-signed, key ID A6A27B3126EF15EB)` `Partner and community providers are signed by their developers.If you'd like to know more` `about provider signing, you can read` `about it here:https://www.terraform.io/docs/cli/plugins/signing.html` `Terraform has created a lock file` `.terraform.lock.hcl to record the providerselections it made above. Include this file` `in` `your version control repositoryso that Terraform can guarantee to make` `the same selections by default whenyou run "terraform init"` `in` `the future.` `Terraform has been successfully initialized!` `You may now begin working with Terraform. Try running "terraform plan"` `to seeany changes that are required for` `your infrastructure. All Terraform commandsshould now work.` `If you ever set` `or change modules or backend configuration for` `Terraform,rerun this command` `to reinitialize your working directory. If you forget, othercommands will detect it and remind you to do` `so if` `necessary.` |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Sau đó, bạn để xem những thay đổi sẽ được áp dụng trên những resource mà terraform đang quản lý bạn có thể chạy:

| `terraform plan` |
| ---------------- |

Cuối cùng bạn chọn chạy dòng lệnh&#x20;

| `terraform apply` |
| ----------------- |

và chọn **YES** để thực hiện việc khởi tạo vServer thông qua Terraform

**Bước 8**: Bạn có thể lên [Portal ](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)để xem Server đang được khởi tạo từ Terraform:

<figure><img src="../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
