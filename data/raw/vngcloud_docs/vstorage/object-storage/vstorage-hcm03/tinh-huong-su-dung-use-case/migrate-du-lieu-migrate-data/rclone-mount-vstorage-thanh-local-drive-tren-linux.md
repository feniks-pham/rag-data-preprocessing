# \[Rclone] Mount vStorage thành Local Drive trên Linux

Để thực hiện Mount vStorage thành Local Drive trên Linux sử dụng Rclone, hãy làm theo hướng dẫn sau:

**1:** Tải & cài đặt **rclone** theo hướng dẫn sau:&#x20;

Với CentOS 7:

| <p><code>curl https://</code><a href="http://rclone.org/install.sh"><code>rclone.org/install.sh</code></a> <code>| sudo bash</code><br><code>sudo yum install fuse -y</code></p> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Với các OS khác: bạn tham khảo link download tại: [https://downloads.rclone.org/v1.55.1/](https://downloads.rclone.org/v1.55.1/)

**Lưu ý:** Nếu rclone của bạn đang sử dụng **version cũ < 1.50** (Để kiểm tra version, bạn dùng lệnh **rclone version**), bạn nên upgrade xuống **rclone version mới** theo cách sau:

* Nếu bạn cài theo script: curl [https://rclone.org/install.sh](https://rclone.org/install.sh) | sudo bash.

| <p><code>sudo rm /usr/bin/rclone</code><br> <br><code>sudo rm /usr/local/share/man/man1/rclone.1</code></p> |
| ----------------------------------------------------------------------------------------------------------- |

* Nếu bạn cài theo repo của OS, bạn có thể:

| `yum remove rclone` |
| ------------------- |

Sau đó, bạn tải và cài đặt **version mới** như hướng dẫn ở trên.

**2:** Tạo file chứng thực rclone.conf theo mẫu sau:

| <p><code>[vstorage]</code></p><p><code>type = swift</code></p><p><code>env_auth = false</code></p><p><code>auth_version = 3</code></p><p><code>user = ******</code></p><p><code>key = ******</code></p><p><code>auth =</code> <a href="https://hcm.auth.vstorage.vngcloud.vn/v3tenant_id"><code>https://hcm.auth.vstorage.vngcloud.vn/v3</code></a></p><p><a href="https://hcm.auth.vstorage.vngcloud.vn/v3tenant_id"><code>tenant_id</code></a> <code>= 410ded5c02674846b534ff7b4a894c2e</code></p><p><code>endpoint_type = public</code></p><p><code>tenant_domain = default</code></p><p><code>domain = default</code></p><p><code>location_constraint = HCM01</code></p><p><code>region = HCM01</code></p><p><br></p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Các thông tin bên trên bạn có thể thực hiện lấy theo hướng dẫn tại [Tích hợp công cụ Rclone với vStorage](../../3rd-party-softwares/rclone/tich-hop-cong-cu-rclone-voi-vstorage.md). Trong đó:&#x20;

* User/ Key: thông tin Swift user bạn khởi tạo từ IAM.
* Auth: xem tại [Farm là gì?](../../vstorage-la-gi/farm-la-gi.md)
* Tenant\_id: thông tin project id, bạn có thể lấy tại vStorage Portal.

Trước khi mount, bạn kiểm tra kết nối tới vStorage bằng lệnh lsd của rclone với cú pháp:

| `rclone --config=rclone.conf lsd vstorage:` |
| ------------------------------------------- |

Nếu bạn đã sử dụng vStorage trước đó, bạn sẽ thấy các container chứa các file mình đã upload lên.

**3**: Để thực hiện mount, bạn dùng câu lệnh với cú pháp sau:

| `rclone mount --config=rclone.conf vstorage:<container_name> <mount_point> --vfs-cache-mode full --allow-non-empty --allow-other --drive-chunk-size 128M  --max-read-ahead 200M --dir-cache-time 30m --daemon` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Trong đó:

* **container\_name**: tên container bạn sẽ backup file vào trên vStorage. (nếu chưa có, rclone sẽ tự động sinh ra). Lưu ý, bạn nên đặt một tên khác các container hiện có.
* **mount\_point**: vùng sẽ mount trên local của bạn.

VD: bạn muốn mount container tên **backup** tại đuờng dẫn **/backup** trên máy local:

| `rclone mount --config=/root/.config/rclone/rclone.conf vstorage:backup /backup --vfs-cache-mode full --allow-non-empty --allow-other --drive-chunk-size 128M  --max-read-ahead 200M --dir-cache-time 30m --daemon` |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Quá trình mount sẽ mất một lúc để hoàn thành. (Khoảng 3 phút).

Để test quá trình mount đã hoàn thành hay chưa, bạn có thể tạo file vào vùng mount trên:

VD: touch /backup/abc

Đợi một lúc để quá trình sync dữ liệu diễn ra (tùy dung dung lượng file của bạn mà quá trình này sẽ nhanh hay chậm).

Để check quá trình sync đã thành công, bạn dùng lệnh **ls** của rclone để kiểm tra:

| `rclone --config=rclone.conf ls vstorage:<container_name>` |
| ---------------------------------------------------------- |

Ví dụ:&#x20;

| `rclone --config=rclone.conf ls vstorage:backup` |
| ------------------------------------------------ |

Để unmount, bạn dùng lệnh sau:

| `fusermount -uz <mount_point>` |
| ------------------------------ |
