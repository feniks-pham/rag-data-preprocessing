---
description: >-
  Volume (gắn rời) của vServer có thể dễ dàng được mở rộng, mà không làm gián
  đoạn vServer.  Lưu ý: Volume không thể giảm kích thước chỉ có thể tăng kích
  thước.
---

# Mở rộng Volume với hệ điều hành Linux

### **Mở rộng Volume với hệ điều hành Linux** <a href="#morongvolumevoihedieuhanhlinux-morongvolumevoihedieuhanhlinux" id="morongvolumevoihedieuhanhlinux-morongvolumevoihedieuhanhlinux"></a>

Sử dụng hướng dẫn sau để thay đổi kích thước Volume trên bảng điều khiển:

**Bước 1: Tăng dung lượng ổ cứng trên bảng điều khiển vServer**

1. Mở trình điều khiển vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/block-store/volumes](https://hcm-3.console.vngcloud.vn/vserver/block-store/volumes)
2. Trên tab VPC/  Volumes, chọn một Volume và nhấn chọn **Hành động**
3. Sau đó chọn **Mở rộng**
4. Chọn kích thước và IOPS mới cho Volume, lưu ý kích thước của Volume phải lớn hơn hoặc bằng 20 GB và kích thước lớn nhất là 10000 GB, bạn có thể kiểm tra chi phí tăng thêm ở cột bên phải
5. Nhấn **Mở rộng** để hoàn tất

Sau khi quá trình tăng dung lượng trên bảng điều khiển hoàn tất, cần tăng dung lượng của ổ bên trong server.

**Bước 2: Tăng dung lượng ổ cứng bên trong Server**

**a. Kiểm tra ổ đĩa đã được tăng dung lượng hay chưa:**

1. [Kết nối vào Server](../server/ket-noi-vao-may-chu-ao/#ketnoivaomaychuao-ketnoivaomaychulinuxbangcongcusshclient)
2. Gõ lệnh **`lsblk`**\
   Trong đầu ra ví dụ sau, ổ đĩa gốc (disk0) có hai phân vùng (disk01 và disk02), trong khi ổ đĩa bổ sung (disk00) không có phân vùng.

```
sudo lsblk
NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
disk00        259:0    0  30G  0 disk /data
disk0         259:1    0  16G  0 disk
└─disk0p1     259:2    0   8G  0 part /
└─disk0p2     259:3    0   1M  0 part
```

Nếu ổ đĩa có một phân vùng, hãy tiếp tục quy trình từ bước sau (2b). Nếu ổ đĩa không có phân vùng, hãy bỏ qua các bước 2b, 2c và 2d, rồi tiếp tục quy trình từ bước 3.

3. Kiểm tra xem phân vùng có cần được mở rộng hay không. Trong đầu ra lệnh `lsblk` từ bước trước, hãy so sánh kích thước phân vùng và kích thước ổ đĩa gốc. Nếu kích thước phân vùng nhỏ hơn kích thước ổ đĩa, hãy tiếp tục bước tiếp theo. Nếu kích thước phân vùng bằng kích thước ổ đĩa, thì không thể mở rộng phân vùng.

**b. Tăng dung lượng ổ đĩa bằng câu lệnh:**

1.  Mở rộng phân vùng. Sử dụng lệnh **`growpart`** và chỉ định phân vùng để mở rộng. Gõ lệnh: growpart <ổ> \<partition của ổ>\


    Ví dụ: để mở rộng phân vùng có tên disk0p1, hãy sử dụng lệnh sau.

    Quan trọng

    Lưu ý khoảng cách giữa tên thiết bị (disk0) và số phân vùng (1).

```
sudo growpart /dev/disk0 1
```

2. Xác minh rằng phân vùng đã được mở rộng. Sử dụng lệnh **`lsblk`**. Kích thước phân vùng bây giờ phải bằng kích thước ổ đĩa.

```
sudo lsblk
NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
disk00        259:0    0  30G  0 disk /data
disk0         259:1    0  16G  0 disk
└─disk0p1     259:2    0  16G  0 part /
└─disk0p2     259:3    0   1M  0 part
```

**c. Mở rộng tập tin hệ thống**

1. Nhận tên, kích thước, loại và điểm gắn kết cho hệ thống tệp mà bạn cần mở rộng. Sử dụng lệnh **`df -hT`**.\
   Đầu ra ví dụ sau đây cho thấy hệ thống tệp /dev/disk0p1 có kích thước 8 GB, loại của nó là xfs và điểm gắn kết của nó là /.

```
df -hT
Filesystem      Type  Size  Used Avail Use% Mounted on
/dev/disk0p1    xfs   8.0G  1.6G  6.5G  20% /
/dev/disk00     xfs   8.0G   33M  8.0G   1% /data
```

2. Các lệnh để mở rộng hệ thống tệp khác nhau tùy thuộc vào loại hệ thống tệp. Chọn lệnh đúng sau đây dựa trên loại hệ thống tệp mà bạn đã lưu ý ở bước trước.\
   \[**Tệp hệ thống XFS**] Sử dụng lệnh **`xfs_growfs`** và chỉ định điểm gắn kết của hệ thống tệp mà bạn đã lưu ý ở bước trước.

```
sudo xfs_growfs -d /
```

Gợi ý

* xfs\_growfs: /data không phải là hệ thống tệp XFS được gắn kết: Cho biết rằng bạn đã chỉ định điểm gắn kết không chính xác hoặc hệ thống tệp không phải là XFS. Để xác minh điểm gắn kết và loại hệ thống tệp, hãy sử dụng lệnh df -hT.
* Kích thước dữ liệu không thay đổi, bỏ qua: Cho biết rằng hệ thống tệp đã mở rộng toàn bộ ổ đĩa. Nếu ổ đĩa không có phân vùng, hãy xác nhận rằng sửa đổi ổ đĩa đã thành công. Nếu ổ đĩa có các phân vùng, hãy đảm bảo rằng phân vùng đó đã được mở rộng như mô tả trong bước b.

\[**Tệp hệ thống Ext4**] Sử dụng lệnh **resize2fs** và chỉ định tên của hệ thống tệp mà bạn đã lưu ý ở bước trước.

```
sudo resize2fs /dev/disk0p1
```

3. Xác minh rằng tập tin hệ thống đã được mở rộng. Sử dụng lệnh **`df -hT`** và xác nhận rằng kích thước hệ thống tệp bằng với kích thước ổ đĩa.

\
