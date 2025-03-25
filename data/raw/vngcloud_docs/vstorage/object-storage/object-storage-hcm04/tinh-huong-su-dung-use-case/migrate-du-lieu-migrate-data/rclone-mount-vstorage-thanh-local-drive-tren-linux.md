# \[Rclone] Mount vStorage thành Local Drive trên Linux

Để thực hiện Mount vStorage thành Local Drive trên Linux sử dụng Rclone, hãy làm theo hướng dẫn sau:

## 1. Tải và cài đặt **rclone** theo hướng dẫn sau:

* Với CentOS 7:

```bash
curl https://rclone.org/install.sh
sudo bash
sudo yum install fuse -y
```

Với các OS khác: bạn tham khảo link download tại: [https://downloads.rclone.org/v1.55.1/](https://downloads.rclone.org/v1.55.1/)

**Lưu ý:** Nếu rclone của bạn đang sử dụng **version cũ < 1.50** (Để kiểm tra version, bạn dùng lệnh **rclone version**), bạn nên tải xuống **rclone version mới** theo cách sau:

* Nếu bạn cài theo script:&#x20;

```bash
curl https://rclone.org/install.sh
sudo bash
sudo rm /usr/bin/rclone
sudo rm /usr/local/share/man/man1/rclone.
```

* Nếu bạn cài theo repo của OS, bạn có thể:

```bash
yum remove rclone
```

Sau đó, bạn tải và cài đặt **version mới** như hướng dẫn ở trên.

## 2. Tạo file chứng thực rclone.conf theo mẫu sau:

* Thực hiện tạo file rclone.conf theo mẫu bên dưới, thông tin access\_key\_id và secret\_access\_key bạn có thể lấy tại vStorage Portal:

```bash
[vstorage]
type = s3
provider = Other
access_key_id = <<Lấy thông tin từ vStorage Portal>>
secret_access_key = <<Lấy thông tin từ vStorage Portal>>
endpoint = https://hcm04.vstorage.vngcloud.vn
```

* Trước khi mount, bạn kiểm tra kết nối tới vStorage bằng lệnh lsd của rclone với cú pháp:

```bash
rclone --config=rclone.conf lsd vstorage:
```

Nếu bạn đã sử dụng vStorage trước đó, bạn sẽ thấy các bucket chứa các file mình đã upload lên.

## 3. Thực hiện mount

Để thực hiện mount, bạn dùng câu lệnh với cú pháp sau:

```bash
rclone mount --config=rclone.conf vstorage:<bucket_name> <mount_point> --vfs-cache-mode full --allow-non-empty --allow-other --drive-chunk-size 128M --max-read-ahead 200M --dir-cache-time 30m --daemon
```

Trong đó:

* **bucket\_name**: tên bucket bạn sẽ backup file vào trên vStorage. (nếu chưa có, rclone sẽ tự động sinh ra). Lưu ý, bạn nên đặt một tên khác các bucket hiện có.
* **mount\_point**: vùng sẽ mount trên local của bạn.

VD: bạn muốn mount bucket tên **backup** tại đuờng dẫn **/backup** trên máy local:

<pre class="language-bash"><code class="lang-bash"><strong>rclone mount --config=/root/.config/rclone/rclone.conf vstorage:backup /backup --vfs-cache-mode full --allow-non-empty --allow-other --drive-chunk-size 128M --max-read-ahead 200M --dir-cache-time 30m --daemon
</strong></code></pre>

Quá trình mount sẽ mất một lúc để hoàn thành. (Khoảng 3 phút).

Để test quá trình mount đã hoàn thành hay chưa, bạn có thể tạo file vào vùng mount trên:

VD: touch /backup/abc

Đợi một lúc để quá trình sync dữ liệu diễn ra (tùy dung dung lượng file của bạn mà quá trình này sẽ nhanh hay chậm).

* Để kiểm tra quá trình sync đã thành công, bạn dùng lệnh **ls** của rclone để kiểm tra:

```bash
 rclone --config=rclone.conf ls vstorage:<bucket_name>
```

Ví dụ:

```bash
rclone --config=rclone.conf ls vstorage:backup
```

* Để unmount, bạn dùng lệnh sau:

```bash
fusermount -uz <mount_point>
```
