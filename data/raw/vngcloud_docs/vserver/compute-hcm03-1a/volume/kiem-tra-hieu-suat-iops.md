# Kiểm tra hiệu suất IOPS

## Tổng quan

Để kiểm tra hiệu suất IOPS (Input/Output Operations Per Second) trên một Volume, bạn có thể sử dụng công cụ `fio.`

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Cảnh báo**

* Việc thực hiện kiểm tra hiệu suất IOPS có thể gây ảnh hưởng tới Volume của bạn. Chúng tôi khuyên bạn nên sao lưu dữ liệu bằng cách tạo snapshot của Volume hoặc tạo Volume mới không chứa dữ liệu để thử nghiệm. Để biết thêm thông tin, hãy xem phần [Snapshot](../snapshot/).
{% endhint %}

## **Các bước thực hiện** <a href="#kiemtrahieusuatiops-kiemtrahieusuatdongthoirandomread-and-randomwrite" id="kiemtrahieusuatiops-kiemtrahieusuatdongthoirandomread-and-randomwrite"></a>

{% hint style="info" %}
Bên dưới là hướng dẫn chi tiết và kết quả mẫu cho 3 bài test kiểm tra hiệu suất IOPS Read và Write đồng thời, chỉ Read, chỉ Write vào Volume. Cụ thể, một số cấu hình chúng tôi sử dụng như sau:&#x20;

* **Region:** HCM-03
* **OS Images:** Ubuntu
* **Ubuntu Version:** 1\_Ubuntu-22.04x64
* **Instance**: s-general-4x8
* **Volume Type:** NVME
* **IOPS:** 5000 và 10000
* **Volume Size:** 100 GB
{% endhint %}



### **Kiểm tra hiệu suất đồng thời random read & random write** <a href="#kiemtrahieusuatiops-kiemtrahieusuatdongthoirandomread-and-randomwrite" id="kiemtrahieusuatiops-kiemtrahieusuatdongthoirandomread-and-randomwrite"></a>

1. Tạo một server với ổ đĩa Volume loại **NVME** với IOPS **5000** tại trang chủ vServer:

<figure><img src="../../../.gitbook/assets/image (6).png" alt="" width="563"><figcaption></figcaption></figure>

2. **Kết nối vào Server** của bạn. Để biết thêm thông tin hãy xem hướng dẫn [Kết nối vào máy chủ ảo](../server/ket-noi-vao-may-chu-ao/).
3. Chạy lệnh sau để cài đặt **FIO**:

*   **Ubuntu/Debian**:

    ```bash
    sudo apt update
    sudo apt install fio -y
    ```
*   **CentOS/RHEL**:

    ```bash
    sudo yum install fio -y
    ```

4. Tạo 1 file 4GB, sau đó chạy câu lệnh bên dưới để thực hiện việc **read/write đồng thời** với blocksize 4KB theo tỉ lệ 75% – 25% (tức 3 read/1 write) và thực hiện đồng thời 64 tác vụ một lúc (Tỉ lệ 3:1 rất phổ biến và xấp xỉ với các dạng database hiện nay):

* Với chỉ 1 job chạy, bạn có thể dùng lệnh:

```bash
sudo fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=TGS --filename=TGS --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75 --numjobs=1
```

* Với 8 jobs chạy đồng thời, bạn có thể sử dụng:&#x20;

```bash
sudo fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=TGS --filename=TGS --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75 --numjobs=8
```

Ngoài ra, bạn có thể thay đổi một vài thông số theo điều kiện mô tả bên dưới:

* `--randrepeat=1:` Sử dụng cùng một seed ngẫu nhiên cho các bài kiểm tra.
* `--ioengine=libaio:` Chỉ định I/O Engine, libaio (Linux asynchronous I/O) là một phương thức I/O không đồng bộ, phù hợp cho các bài kiểm tra hiệu suất I/O trên Linux.
* `--direct=1: Bỏ`qua bộ đệm của hệ điều hành (OS cache) khi thực hiện I/O.
* `--gtod_reduce=1:`Giảm độ chính xác của timestamp (giảm số lần gọi `gettimeofday`), giúp giảm tác động đến hiệu suất và cải thiện tính chính xác của bài kiểm tra.
* `--name=TGS:` Tên bài kiểm tra
* `--filename=TGS:` Tên file kiểm tra
* `--iodepth=64:` Độ sâu hàng đợi (queue depth) là 64, tức là tối đa 64 yêu cầu I/O có thể chờ xử lý cùng lúc.
* `--rwmixread=75:` Tỷ lệ giữa đọc và ghi là 75:25.
* `--readwrite=randrw`: Thực hiện đọc/ghi ngẫu nhiên.
* `--size=4G`: Tổng kích thước dữ liệu cần kiểm tra.
* `--bs=blocksize=4k`: Kích thước block (4KB là phổ biến để kiểm tra IOPS).
* `--numjobs=8`: Số lượng job chạy đồng thời.

5. Dưới đây là kết quả ghi nhận được (với cấu hình 4 core 8 GB)

* Khi bạn thiết lập **numjob = 1**:

```bash
TGS: (g=0): rw=randrw, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.28
Starting 1 process
Jobs: 1 (f=1): [m(1)][100.0%][r=14.5MiB/s,w=5196KiB/s][r=3709,w=1299 IOPS][eta 00m:00s]
TGS: (groupid=0, jobs=1): err= 0: pid=66983: Fri Dec 27 08:45:29 2024
  read: IOPS=3748, BW=14.6MiB/s (15.4MB/s)(3070MiB/209636msec)
   bw (  KiB/s): min=14480, max=17728, per=100.00%, avg=15006.60, stdev=226.44, samples=418
   iops        : min= 3620, max= 4432, avg=3751.65, stdev=56.61, samples=418
  write: IOPS=1252, BW=5012KiB/s (5132kB/s)(1026MiB/209636msec); 0 zone resets
   bw (  KiB/s): min= 4536, max= 6256, per=100.00%, avg=5015.60, stdev=190.53, samples=418
   iops        : min= 1134, max= 1564, avg=1253.90, stdev=47.63, samples=418
  cpu          : usr=1.06%, sys=6.39%, ctx=939035, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=785920,262656,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=14.6MiB/s (15.4MB/s), 14.6MiB/s-14.6MiB/s (15.4MB/s-15.4MB/s), io=3070MiB (3219MB), run=209636-209636msec
  WRITE: bw=5012KiB/s (5132kB/s), 5012KiB/s-5012KiB/s (5132kB/s-5132kB/s), io=1026MiB (1076MB), run=209636-209636msec

Disk stats (read/write):
  sda: ios=785024/262487, merge=0/48, ticks=12943132/437608, in_queue=13380944, util=100.00%
```

* Khi bạn thiết lập **numjob = 8:**

```bash
TGS: (g=0): rw=randrw, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
...
fio-3.28
Starting 8 processes
Jobs: 1 (f=1): [_(1),m(1),_(6)][100.0%][r=14.5MiB/s,w=4960KiB/s][r=3719,w=1240 IOPS][eta 00m:00s]
TGS: (groupid=0, jobs=1): err= 0: pid=1454: Fri Dec 27 08:37:31 2024
  read: IOPS=474, BW=1899KiB/s (1944kB/s)(3070MiB/1655679msec)
   bw (  KiB/s): min=  680, max= 3712, per=12.65%, avg=1899.92, stdev=364.08, samples=3309
   iops        : min=  170, max=  928, avg=474.92, stdev=91.05, samples=3309
  write: IOPS=158, BW=635KiB/s (650kB/s)(1026MiB/1655679msec); 0 zone resets
   bw (  KiB/s): min=  152, max= 1336, per=12.66%, avg=634.95, stdev=141.81, samples=3309
   iops        : min=   38, max=  334, avg=158.71, stdev=35.45, samples=3309
  cpu          : usr=0.13%, sys=0.43%, ctx=276151, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=785920,262656,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=1455: Fri Dec 27 08:37:31 2024
  read: IOPS=468, BW=1874KiB/s (1919kB/s)(3067MiB/1676092msec)
   bw (  KiB/s): min=  608, max=14436, per=12.47%, avg=1872.46, stdev=474.65, samples=3350
   iops        : min=  152, max= 3609, avg=468.05, stdev=118.67, samples=3350
  write: IOPS=157, BW=629KiB/s (644kB/s)(1029MiB/1676092msec); 0 zone resets
   bw (  KiB/s): min=  176, max= 5154, per=12.54%, avg=628.25, stdev=172.93, samples=3350
   iops        : min=   44, max= 1288, avg=157.03, stdev=43.22, samples=3350
  cpu          : usr=0.16%, sys=0.42%, ctx=290477, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=785179,263397,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=1456: Fri Dec 27 08:37:31 2024
  read: IOPS=471, BW=1885KiB/s (1931kB/s)(3070MiB/1667591msec)
   bw (  KiB/s): min=  608, max= 3664, per=12.56%, avg=1886.29, stdev=358.69, samples=3333
   iops        : min=  152, max=  916, avg=471.51, stdev=89.69, samples=3333
  write: IOPS=157, BW=630KiB/s (645kB/s)(1026MiB/1667591msec); 0 zone resets
   bw (  KiB/s): min=  200, max= 1304, per=12.58%, avg=630.13, stdev=139.36, samples=3333
   iops        : min=   50, max=  326, avg=157.50, stdev=34.83, samples=3333
  cpu          : usr=0.16%, sys=0.42%, ctx=279562, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=786007,262569,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=1457: Fri Dec 27 08:37:31 2024
  read: IOPS=471, BW=1884KiB/s (1930kB/s)(3071MiB/1668845msec)
   bw (  KiB/s): min=  704, max= 4472, per=12.56%, avg=1885.38, stdev=367.18, samples=3336
   iops        : min=  176, max= 1118, avg=471.28, stdev=91.82, samples=3336
  write: IOPS=157, BW=629KiB/s (644kB/s)(1025MiB/1668845msec); 0 zone resets
   bw (  KiB/s): min=  208, max= 1384, per=12.56%, avg=629.35, stdev=138.18, samples=3336
   iops        : min=   52, max=  346, avg=157.31, stdev=34.54, samples=3336
  cpu          : usr=0.14%, sys=0.43%, ctx=279931, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=786156,262420,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=1458: Fri Dec 27 08:37:31 2024
  read: IOPS=469, BW=1877KiB/s (1923kB/s)(3072MiB/1675283msec)
   bw (  KiB/s): min=  568, max= 7304, per=12.51%, avg=1878.59, stdev=429.34, samples=3349
   iops        : min=  142, max= 1826, avg=469.58, stdev=107.35, samples=3349
  write: IOPS=156, BW=626KiB/s (641kB/s)(1024MiB/1675283msec); 0 zone resets
   bw (  KiB/s): min=  144, max= 2320, per=12.50%, avg=626.56, stdev=158.62, samples=3349
   iops        : min=   36, max=  580, avg=156.61, stdev=39.64, samples=3349
  cpu          : usr=0.15%, sys=0.42%, ctx=288230, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=786322,262254,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=1459: Fri Dec 27 08:37:31 2024
  read: IOPS=477, BW=1909KiB/s (1954kB/s)(3073MiB/1648859msec)
   bw (  KiB/s): min=  600, max= 3720, per=12.72%, avg=1909.87, stdev=363.42, samples=3296
   iops        : min=  150, max=  930, avg=477.41, stdev=90.88, samples=3296
  write: IOPS=158, BW=635KiB/s (650kB/s)(1023MiB/1648859msec); 0 zone resets
   bw (  KiB/s): min=  104, max= 1312, per=12.68%, avg=635.52, stdev=138.71, samples=3296
   iops        : min=   26, max=  328, avg=158.85, stdev=34.67, samples=3296
  cpu          : usr=0.14%, sys=0.42%, ctx=276105, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=786765,261811,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=1460: Fri Dec 27 08:37:31 2024
  read: IOPS=471, BW=1887KiB/s (1932kB/s)(3072MiB/1667012msec)
   bw (  KiB/s): min=  688, max= 3864, per=12.57%, avg=1887.81, stdev=350.52, samples=3332
   iops        : min=  172, max=  966, avg=471.89, stdev=87.66, samples=3332
  write: IOPS=157, BW=629KiB/s (644kB/s)(1024MiB/1667012msec); 0 zone resets
   bw (  KiB/s): min=  184, max= 1384, per=12.56%, avg=629.62, stdev=136.59, samples=3332
   iops        : min=   46, max=  346, avg=157.38, stdev=34.14, samples=3332
  cpu          : usr=0.13%, sys=0.44%, ctx=276590, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=786314,262262,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=1461: Fri Dec 27 08:37:31 2024
  read: IOPS=469, BW=1880KiB/s (1925kB/s)(3074MiB/1674605msec)
   bw (  KiB/s): min=  600, max= 5608, per=12.52%, avg=1880.19, stdev=423.17, samples=3347
   iops        : min=  150, max= 1402, avg=469.99, stdev=105.81, samples=3347
  write: IOPS=156, BW=625KiB/s (640kB/s)(1022MiB/1674605msec); 0 zone resets
   bw (  KiB/s): min=  168, max= 2088, per=12.48%, avg=625.04, stdev=159.39, samples=3347
   iops        : min=   42, max=  522, avg=156.23, stdev=39.84, samples=3347
  cpu          : usr=0.14%, sys=0.44%, ctx=287417, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=786981,261595,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=14.7MiB/s (15.4MB/s), 1874KiB/s-1909KiB/s (1919kB/s-1954kB/s), io=24.0GiB (25.8GB), run=1648859-1676092msec
  WRITE: bw=5009KiB/s (5129kB/s), 625KiB/s-635KiB/s (640kB/s-650kB/s), io=8199MiB (8597MB), run=1648859-1676092msec

Disk stats (read/write):
  sda: ios=6279077/2104043, merge=11772/10995, ticks=397920368/24398012, in_queue=422384834, util=100.00%
```

{% hint style="info" %}
**Kết luận:**

* Khi tăng số lượng job (`numjob=8`), **IOPS tổng** (IOPS tổng hợp từ tất cả các job) đảm bảo đã đạt mức **IOPS = 5000**.
* Với `numjob=1`, **Read IOPS: 3748** và **Write IOPS: 1252.** Kết quả này đảm bảo đã đạt mức **IOPS = 5000**.
{% endhint %}

### **Kiểm tra hiệu suất random read** <a href="#kiemtrahieusuatiops-kiemtrahieusuatrandomread" id="kiemtrahieusuatiops-kiemtrahieusuatrandomread"></a>

1. Thực hiện các bước 1,2,3 tương tự trường hợp Kiểm tra hiệu suất đồng thời random read và random write.
2. Tạo 1 file 4GB, sau đó chạy câu lệnh bên dưới để chỉ thực hiện việc **read** với blocksize 4KB theo tỉ lệ 100% (tức toàn bộ chỉ read) và thực hiện đồng thời 64 tác vụ một lúc:

* Với chỉ 1 job chạy, bạn có thể dùng lệnh:

```bash
sudo fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=TGS --filename=TGS --bs=4k --iodepth=64 --size=4G --readwrite=randread --numjobs=1
```

* Với 8 jobs chạy đồng thời, bạn có thể sử dụng:&#x20;

```bash
sudo fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=TGS --filename=TGS --bs=4k --iodepth=64 --size=4G --readwrite=randread --numjobs=8
```

3. Dưới đây là kết quả ghi nhận được:

* Khi bạn thiết lập **numjob = 1**:

```bash
TGS: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.28
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=19.5MiB/s][r=5003 IOPS][eta 00m:00s]
TGS: (groupid=0, jobs=1): err= 0: pid=66992: Fri Dec 27 08:55:43 2024
  read: IOPS=5002, BW=19.5MiB/s (20.5MB/s)(4096MiB/209618msec)
   bw (  KiB/s): min=19864, max=23992, per=100.00%, avg=20025.43, stdev=195.36, samples=418
   iops        : min= 4966, max= 5998, avg=5006.36, stdev=48.84, samples=418
  cpu          : usr=1.01%, sys=6.15%, ctx=915643, majf=0, minf=71
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=19.5MiB/s (20.5MB/s), 19.5MiB/s-19.5MiB/s (20.5MB/s-20.5MB/s), io=4096MiB (4295MB), run=209618-209618msec

Disk stats (read/write):
  sda: ios=1047448/18, merge=0/5, ticks=13385109/25, in_queue=13385134, util=100.00%
```

* Khi bạn thiết lập **numjob = 8:**

```bash
TGS: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
...
fio-3.28
Starting 8 processes
Jobs: 1 (f=1): [_(6),r(1),_(1)][100%][r=19.5MiB/s][r=5004 IOPS][eta 00m:00s]
TGS: (groupid=0, jobs=1): err= 0: pid=67019: Fri Dec 27 09:34:16 2024
  read: IOPS=626, BW=2508KiB/s (2568kB/s)(4096MiB/1672501msec)
   bw (  KiB/s): min=  633, max=10028, per=12.51%, avg=2508.96, stdev=569.55, samples=3344
   iops        : min=  158, max= 2507, avg=627.18, stdev=142.40, samples=3344
  cpu          : usr=0.13%, sys=0.41%, ctx=297140, majf=0, minf=70
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67020: Fri Dec 27 09:34:16 2024
  read: IOPS=629, BW=2517KiB/s (2578kB/s)(4096MiB/1666112msec)
   bw (  KiB/s): min=  768, max= 4936, per=12.56%, avg=2518.86, stdev=475.31, samples=3331
   iops        : min=  192, max= 1234, avg=629.66, stdev=118.83, samples=3331
  cpu          : usr=0.13%, sys=0.40%, ctx=286577, majf=0, minf=73
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67021: Fri Dec 27 09:34:16 2024
  read: IOPS=628, BW=2512KiB/s (2572kB/s)(4096MiB/1669595msec)
   bw (  KiB/s): min=  704, max= 4904, per=12.54%, avg=2513.51, stdev=484.30, samples=3338
   iops        : min=  176, max= 1226, avg=628.32, stdev=121.08, samples=3338
  cpu          : usr=0.14%, sys=0.40%, ctx=286580, majf=0, minf=71
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67022: Fri Dec 27 09:34:16 2024
  read: IOPS=628, BW=2513KiB/s (2573kB/s)(4096MiB/1668976msec)
   bw (  KiB/s): min=  632, max= 5048, per=12.54%, avg=2514.58, stdev=507.70, samples=3337
   iops        : min=  158, max= 1262, avg=628.59, stdev=126.93, samples=3337
  cpu          : usr=0.13%, sys=0.40%, ctx=294892, majf=0, minf=71
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67023: Fri Dec 27 09:34:16 2024
  read: IOPS=627, BW=2511KiB/s (2571kB/s)(4096MiB/1670313msec)
   bw (  KiB/s): min=  808, max= 5979, per=12.53%, avg=2511.70, stdev=508.10, samples=3339
   iops        : min=  202, max= 1494, avg=627.87, stdev=127.02, samples=3339
  cpu          : usr=0.12%, sys=0.41%, ctx=291621, majf=0, minf=71
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67024: Fri Dec 27 09:34:16 2024
  read: IOPS=627, BW=2510KiB/s (2570kB/s)(4096MiB/1670929msec)
   bw (  KiB/s): min=  832, max= 7880, per=12.53%, avg=2511.61, stdev=528.38, samples=3341
   iops        : min=  208, max= 1970, avg=627.84, stdev=132.09, samples=3341
  cpu          : usr=0.13%, sys=0.40%, ctx=291707, majf=0, minf=70
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67025: Fri Dec 27 09:34:16 2024
  read: IOPS=626, BW=2505KiB/s (2565kB/s)(4096MiB/1674276msec)
   bw (  KiB/s): min=  721, max=20024, per=12.48%, avg=2502.90, stdev=763.78, samples=3347
   iops        : min=  180, max= 5006, avg=625.67, stdev=190.95, samples=3347
  cpu          : usr=0.14%, sys=0.41%, ctx=303280, majf=0, minf=72
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67026: Fri Dec 27 09:34:16 2024
  read: IOPS=628, BW=2513KiB/s (2573kB/s)(4096MiB/1669191msec)
   bw (  KiB/s): min=  848, max= 4928, per=12.54%, avg=2514.00, stdev=513.98, samples=3337
   iops        : min=  212, max= 1232, avg=628.44, stdev=128.50, samples=3337
  cpu          : usr=0.14%, sys=0.39%, ctx=292611, majf=0, minf=72
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=1048576,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=19.6MiB/s (20.5MB/s), 2505KiB/s-2517KiB/s (2565kB/s-2578kB/s), io=32.0GiB (34.4GB), run=1666112-1674276msec

Disk stats (read/write):
  sda: ios=8371218/25, merge=16847/6, ticks=422350060/186, in_queue=422350252, util=100.00%
```

{% hint style="info" %}
**Kết luận:**

* Khi tăng số lượng job (`numjob=8`), **Read IOPS tổng** (IOPS tổng hợp từ tất cả các job) đảm bảo đã đạt mức **IOPS = 5000**.
* Với `numjob=1`, **Read IOPS: 5002.** Kết quả này đảm bảo đã đạt mức **IOPS = 5000**.
{% endhint %}

### **Kiểm tra hiệu suất random write** <a href="#kiemtrahieusuatiops-kiemtrahieusuatrandomwrite" id="kiemtrahieusuatiops-kiemtrahieusuatrandomwrite"></a>

1. Thực hiện các bước 1,2,3 tương tự trường hợp Kiểm tra hiệu suất đồng thời random read và random write. <mark style="background-color:blue;">(Để tăng độ đa dạng, trong ví dụ này, tôi sẽ tăng IOPS của Volume này lên</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**10000**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">thay vì</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**5000,**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">các cấu hình còn lại tôi giữ nguyên).</mark>&#x20;
2. Tạo 1 file 4GB, sau đó chạy câu lệnh bên dưới để chỉ thực hiện việc **write** với blocksize 4KB theo tỉ lệ 100% (tức toàn bộ chỉ write) và thực hiện đồng thời 64 tác vụ một lúc:

* Với chỉ 1 job chạy, bạn có thể dùng lệnh:

```bash
sudo fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=TGS --filename=TGS --bs=4k --iodepth=64 --size=4G --readwrite=randwrite --numjobs=1
```

* Với 8 jobs chạy đồng thời, bạn có thể sử dụng:&#x20;

```bash
sudo fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=TGS --filename=TGS --bs=4k --iodepth=64 --size=4G --readwrite=randwrite --numjobs=8
```

3. Dưới đây là kết quả ghi nhận được:

* Khi bạn thiết lập **numjob = 1**:

```bash
TGS: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.28
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=39.1MiB/s][w=10.0k IOPS][eta 00m:00s]
TGS: (groupid=0, jobs=1): err= 0: pid=67053: Fri Dec 27 09:47:50 2024
  write: IOPS=10.0k, BW=39.1MiB/s (41.0MB/s)(4096MiB/104775msec); 0 zone resets
   bw (  KiB/s): min=39824, max=47872, per=100.00%, avg=40067.29, stdev=545.02, samples=209
   iops        : min= 9956, max=11968, avg=10016.82, stdev=136.26, samples=209
  cpu          : usr=1.59%, sys=8.58%, ctx=891397, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
  WRITE: bw=39.1MiB/s (41.0MB/s), 39.1MiB/s-39.1MiB/s (41.0MB/s-41.0MB/s), io=4096MiB (4295MB), run=104775-104775msec

Disk stats (read/write):
  sda: ios=0/1047478, merge=0/24, ticks=0/6680115, in_queue=6680435, util=99.99%
```

* Khi bạn thiết lập **numjob = 8:**

```bash
TGS: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
...
fio-3.28
Starting 8 processes
Jobs: 1 (f=0): [_(6),f(1),_(1)][100.0%][w=44.1MiB/s][w=11.3k IOPS][eta 00m:00s]
TGS: (groupid=0, jobs=1): err= 0: pid=67058: Fri Dec 27 10:02:37 2024
  write: IOPS=1254, BW=5018KiB/s (5139kB/s)(4096MiB/835782msec); 0 zone resets
   bw (  KiB/s): min= 2669, max=12456, per=12.52%, avg=5019.11, stdev=781.23, samples=1670
   iops        : min=  667, max= 3114, avg=1254.74, stdev=195.31, samples=1670
  cpu          : usr=0.27%, sys=0.79%, ctx=269253, majf=0, minf=6
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67059: Fri Dec 27 10:02:37 2024
  write: IOPS=1261, BW=5045KiB/s (5166kB/s)(4096MiB/831365msec); 0 zone resets
   bw (  KiB/s): min= 2944, max= 7504, per=12.59%, avg=5047.65, stdev=647.34, samples=1661
   iops        : min=  736, max= 1876, avg=1261.88, stdev=161.84, samples=1661
  cpu          : usr=0.27%, sys=0.79%, ctx=262815, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67060: Fri Dec 27 10:02:37 2024
  write: IOPS=1259, BW=5038KiB/s (5159kB/s)(4096MiB/832552msec); 0 zone resets
   bw (  KiB/s): min= 2816, max= 8808, per=12.57%, avg=5041.52, stdev=675.10, samples=1664
   iops        : min=  704, max= 2202, avg=1260.35, stdev=168.77, samples=1664
  cpu          : usr=0.27%, sys=0.79%, ctx=263818, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67061: Fri Dec 27 10:02:37 2024
  write: IOPS=1264, BW=5057KiB/s (5178kB/s)(4096MiB/829428msec); 0 zone resets
   bw (  KiB/s): min= 2808, max= 7400, per=12.62%, avg=5059.43, stdev=659.53, samples=1657
   iops        : min=  702, max= 1850, avg=1264.82, stdev=164.88, samples=1657
  cpu          : usr=0.27%, sys=0.78%, ctx=263498, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67062: Fri Dec 27 10:02:37 2024
  write: IOPS=1253, BW=5014KiB/s (5134kB/s)(4096MiB/836601msec); 0 zone resets
   bw (  KiB/s): min= 2672, max=16752, per=12.51%, avg=5015.98, stdev=856.28, samples=1672
   iops        : min=  668, max= 4188, avg=1253.96, stdev=214.06, samples=1672
  cpu          : usr=0.29%, sys=0.78%, ctx=273352, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67063: Fri Dec 27 10:02:37 2024
  write: IOPS=1258, BW=5035KiB/s (5156kB/s)(4096MiB/832948msec); 0 zone resets
   bw (  KiB/s): min= 3136, max= 7400, per=12.56%, avg=5037.31, stdev=664.81, samples=1664
   iops        : min=  784, max= 1850, avg=1259.29, stdev=166.20, samples=1664
  cpu          : usr=0.26%, sys=0.80%, ctx=264159, majf=0, minf=6
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67064: Fri Dec 27 10:02:37 2024
  write: IOPS=1252, BW=5012KiB/s (5132kB/s)(4096MiB/836927msec); 0 zone resets
   bw (  KiB/s): min= 2800, max=16440, per=12.47%, avg=5000.63, stdev=849.81, samples=1672
   iops        : min=  700, max= 4110, avg=1250.12, stdev=212.45, samples=1672
  cpu          : usr=0.25%, sys=0.79%, ctx=276394, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64
TGS: (groupid=0, jobs=1): err= 0: pid=67065: Fri Dec 27 10:02:37 2024
  write: IOPS=1253, BW=5014KiB/s (5134kB/s)(4096MiB/836501msec); 0 zone resets
   bw (  KiB/s): min= 2680, max=13896, per=12.50%, avg=5011.05, stdev=786.42, samples=1671
   iops        : min=  670, max= 3474, avg=1252.73, stdev=196.60, samples=1671
  cpu          : usr=0.29%, sys=0.78%, ctx=272760, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=0,1048576,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
  WRITE: bw=39.2MiB/s (41.1MB/s), 5012KiB/s-5057KiB/s (5132kB/s-5178kB/s), io=32.0GiB (34.4GB), run=829428-836927msec

Disk stats (read/write):
  sda: ios=0/8367804, merge=0/18890, ticks=0/211109530, in_queue=211112656, util=100.00%
```

{% hint style="info" %}
**Kết luận:**

* Khi tăng số lượng job (`numjob=8`), **Write IOPS tổng** (IOPS tổng hợp từ tất cả các job) đảm bảo đã đạt mức **IOPS = 10000**.
* Với `numjob=1`, **Read** **IOPS: 10k.** Kết quả này đảm bảo đã đạt mức **IOPS = 10000**.
{% endhint %}

***

## **Giám sát hiệu suất ổ đĩa bằng vMonitor Platform** <a href="#kiemtrahieusuatiops-giamsathieusuatodiabangvmonitor" id="kiemtrahieusuatiops-giamsathieusuatodiabangvmonitor"></a>

Hiện tại, hệ thống vServer và vMonitor Platform đã tích hợp sẵn Dashboard giúp bạn quản lý các thông só của server của bạn (bao gồm cả thông số IOPS). Cụ thể, bạn có thể thực hiện theo các bước:&#x20;

1. Truy cập vào [**vMonitor Platform**](../../../vmonitor-platform/vmonitor-platform-la-gi/vmonitor-platform-metric-la-gi/) theo link: [https://vmonitor.console.vngcloud.vn/](https://vmonitor.console.vngcloud.vn/)
2. Chọn mục **Dashboard**, sau đó chọn **All VNG Cloud**
3. Tiếp tục tìm và chọn vào **Dashboard** chứa tên server của bạn, tên **Dashboard** này sẽ có định dạng: `vServer-tên-server-xxxx`

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

4. Tại màn hình chi tiết **Dashboard**, bạn có thể thấy biểu đồ thể hiện thông số IOPS tại biểu đồ bên dưới:&#x20;

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

***

## **Kết quả thử nghiệm kiểm tra hiệu suất ổ đĩa VNG Cloud** <a href="#kiemtrahieusuatiops-ketquathunghiemkiemtrahieusuatodiavngcloud" id="kiemtrahieusuatiops-ketquathunghiemkiemtrahieusuatodiavngcloud"></a>

<table data-full-width="true"><thead><tr><th width="128">IO DEPTH</th><th>VOLUME TYPE</th><th>IOPS MAX</th><th>I/O READ</th><th>I/O WRITE</th><th>I/O READ+WRITE</th></tr></thead><tbody><tr><td>64</td><td>SSD</td><td>3000</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>SSD</td><td>3200</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>SSD</td><td>6400</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>SSD</td><td>10000</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>SSD</td><td>iops-vng</td><td>Shared IOPS with other customer</td><td>Shared IOPS with other customer</td><td>Shared IOPS with other customer</td></tr><tr><td>64</td><td>NVME</td><td>5000</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>NVME</td><td>10000</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>NVME</td><td>20000</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>NVME</td><td>40000</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr><tr><td>64</td><td>NVME</td><td>60000</td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td><td><mark style="background-color:green;"><strong>PASS</strong></mark></td></tr></tbody></table>
