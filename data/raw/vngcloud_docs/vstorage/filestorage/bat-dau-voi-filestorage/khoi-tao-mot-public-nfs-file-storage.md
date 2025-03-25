# Khởi tạo một Public NFS File Storage

Để khởi tạo một Private NFS (Network File System) trên hệ thống File Storage, bạn có thể làm theo các bước sau:

## Khởi tạo File Storage

**Bước 1:** Truy cập vào [https://efs.console.vngcloud.vn/overview](https://efs.console.vngcloud.vn/overview)

**Bước 2:** Chọn mục **File Storage** sau đó chọn **Create a File storage.**

<figure><img src="../../../.gitbook/assets/image (818).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Tại màn hình khởi tạo File Storage, bạn cần nhập/ chọn:&#x20;

* **File Storage name:** tên gợi nhớ của file storage. Tên file cần dài từ 5 tới 50 ký tự và có thể bao gồm các ký tự a-z, A-Z, 0-9, '-', '\_'
* **Description**: nhập mô tả cho file storage.
* **File storage type:** chọn loại ổ đĩa mà bạn mong muốn sử dụng. Hiện tại chúng tôi chỉ cung cấp loại ổ đĩa **Standard HDD.**
* **Protocol:** chọn NFS và version NFS mà bạn mong muốn
* **Tag:** bạn có thể thêm các tag để đánh dầu file storage theo nhu cầu.

<figure><img src="../../../.gitbook/assets/image (908).png" alt=""><figcaption></figcaption></figure>

* **File Storage Max quota:** trong bước khởi tạo file storage, bạn cần đặt một giới hạn quota tối đa cho file storage đó. Quota này có ý nghĩa chính là giới hạn dung lượng lưu trữ mà file storage có thể sử dụng, giúp quản lý tài nguyên hiệu quả. <mark style="color:red;">**Mức quota tối thiểu bạn cần chọn là 1 TB và mức quota tối đa chúng tôi cung cấp là 50 TB.**</mark> Nếu bạn có nhu cấu sử dụng nhiều hơn 50 TB cho một file storage, vui lòng liên hệ với chúng tôi.
* **Network type**: lựa chọn network type mà bạn mong muốn. Ở ví dụ này, bạn có thể chọn Public.
* **Permission: c**ấu hình quyền truy cập dựa trên IP
  * **No one:** Không có IP nào được phép truy cập.
  * **All:** Cho phép tất cả IP có quyền truy cập RO (Read-Only) hoặc RW (Read-Write).
  * **Restricted:** Chỉ cho phép một số IP cụ thể truy cập với quyền RO hoặc RW.

<figure><img src="../../../.gitbook/assets/image (909).png" alt=""><figcaption></figcaption></figure>

**Bước 5:** Chọn **Create File Storage.**

***

## Lấy thông tin mount guide

Sau khi hệ thống khởi tạo xong File Storage của bạn, để lấy mount guide, vui lòng chọn **Action** sau đó chọn **Mount Guide**

<figure><img src="../../../.gitbook/assets/image (3) (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (4) (4).png" alt=""><figcaption></figcaption></figure>

***

## Mount File Storage tới server

Các bước thực hiện mount FileStorage tới một server qua giao thức **NFS:**

**Bước 1:** Cập nhật danh sách gói và cài đặt NFS client:&#x20;

* **Đối với Debian/Ubuntu:**

```bash
sudo apt-get -y update && sudo apt-get install nfs-common
```

* **Đối với Red Hat Enterprise Linux/CentOS:**

```bash
sudo yum update && sudo yum install nfs-utils
```

**Bước 2:** Tạo thư mục mount:

* Ví dụ lệnh bên dưới tôi đã tạo thư mục /mnt/demo

```bash
sudo mkdir -p /mnt/demo
```

**Bước 3:** Mount FileStorage volume:&#x20;

* Ví dụ lệnh bên dưới tôi mount FileStorage có name = demo\_test với thư mục mount = /mnt/demo

<pre class="language-bash"><code class="lang-bash"><strong>sudo mount -t nfs -o vers=4.1,hard,timeo=600,retrans=3,rsize=1048576,wsize=1048576,resvport,async hcm04.efs.vngcloud.vn:/demo_test /mnt/demos/
</strong></code></pre>

**Bước 4**: Kiểm tra mount:

```bash
df -h
```

Các bước này sẽ giúp bạn mount một file share của FileStorage lên server của mình.
