---
description: >-
  Để thực hiện Mount vStorage thành Local Drive trên Window sử dụng Rclone, hãy
  làm theo hướng dẫn sau:
---

# \[Rclone] Mount vStorage lên Window server

## 1. Tải và cài đặt **rclone** theo hướng dẫn sau:

* Bạn thực hiện tải Rclone qua link:  [https://rclone.org/downloads/](https://rclone.org/downloads/).

## 2. Tạo file chứng thực rclone.conf theo mẫu sau:

Sau khi tải xuống và cài đặt Rclone, thực hiện tạo file rclone.conf tại thư mục `C:\Users\username\.config\rclone` với nội dung

```bash
[vstorage]
type = s3
provider = Other
access_key_id = <<Lấy thông tin từ vStorage Portal>>
secret_access_key = <<Lấy thông tin từ vStorage Portal>>
endpoint = https://hcm04.vstorage.vngcloud.vn
```

## 3. Thực hiện mount

* Tiếp theo, bạn có thể sử dụng Rclone với CMD hoặc PowerShell
  *   Để list danh sách object trong một bucket, hãy sử dụng lệnh:&#x20;

      ```
      C:\Users\stackops\Downloads\rclone.exe ls vstorage:[bucket_name]
      ```
  *   Để upload một object lên bucket, hãy dùng lệnh:

      ```
      C:\Users\stackops\Downloads\rclone.exe copy [local_path] vstorage:[bucket_name]
      ```
  *   Để mount một bucket trên vStorage thành local\_path, hãy chạy lệnh:

      ```
      C:\Users\stackops\Downloads\rclone.exe mount vstorage:[bucket_name] [local_path] --vfs-cache-mode off --allow-non-empty --allow-other --drive-chunk-size 128M  --max-read-ahead 200M --dir-cache-time 30m
      ```

**Lưu ý:**

* Nếu gặp lỗi thiếu gói winfsp như hình dưới, bạn có thể tải thêm gói tại link này [https://github.com/billziss-gh/winfsp/releases/tag/v1.4.19049](https://github.com/billziss-gh/winfsp/releases/tag/v1.4.19049)

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Bạn không cần phải tạo sẵn đường dẫn local\_path trên máy local khi tiến hành mount.
* Rclone không hỗ trợ mode chạy ngầm (background mode) nên bạn không được đóng cmd trong quá trình sử dụng.
