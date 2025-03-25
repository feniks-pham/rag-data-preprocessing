---
description: >-
  Volume (gắn rời) của vServer có thể dễ dàng được mở rộng, mà không làm gián
  đoạn vServer.  Lưu ý: Volume không thể giảm kích thước chỉ có thể tăng kích
  thước.
---

# Mở rộng Volume với hệ điều hành Windows

### **Mở rộng Volume với hệ điều hành Window** <a href="#morongvolumevoihedieuhanhwindow-morongvolumevoihedieuhanhwindow" id="morongvolumevoihedieuhanhwindow-morongvolumevoihedieuhanhwindow"></a>

Sử dụng hướng dẫn sau để thay đổi kích thước Volume trên bảng điều khiển:

**Bước 1: Tăng dung lượng ổ đĩa trên bảng điều khiển vServer**

1. Mở trình điều khiển vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/block-store/volumes](https://hcm-3.console.vngcloud.vn/vserver/block-store/volumes)
2. Trên tab VPC/  Volumes, chọn một Volume và nhấn chọn **Hành động**
3. Sau đó chọn **Mở rộng**
4. Chọn kích thước và IOPS mới cho Volume, lưu ý kích thước của Volume phải lớn hơn hoặc bằng 20 GB và kích thước lớn nhất là 10000 GB, bạn có thể kiểm tra chi phí tăng thêm ở cột bên phải
5. Nhấn **Mở rộng** để hoàn tất

Sau khi quá trình tăng dung lượng trên bảng điều khiển hoàn tất, hãy sử dụng tiện ích Windows Disk Management hoặc PowerShell để mở rộng kích thước ổ đĩa sang kích thước mới của ổ đĩa. Bạn có thể bắt đầu thay đổi kích thước hệ thống tệp ngay sau khi Mở rộng trên bảng điều khiển vServer.

**Bước 2: Mở rộng tệp hệ thống Windows bằng tiện ích Disk Management utility**

Sử dụng quy trình sau để mở rộng hệ thống tệp Windows bằng Disk Management.

1. Để mở rộng hệ thống tệp bằng **Disk Management**\
   Trước khi mở rộng một hệ thống tệp có chứa dữ liệu có giá trị, cách tốt nhất là tạo ảnh chụp nhanh (Snapshot) của ổ đĩa chứa nó trong trường hợp bạn cần khôi phục các thay đổi của mình.&#x20;
2. Đăng nhập vào phiên bản Windows của bạn bằng Remote Desktop.
3.  Trong hộp thoại **Run**, nhập **diskmgmt.msc** và nhấn Enter. Tiện ích **Disk Management** sẽ mở ra.\


    <figure><img src="../../../.gitbook/assets/image (429).png" alt=""><figcaption></figcaption></figure>
4. Trên menu **Disk Management**, chọn **Action**, **Rescan Disks**.
5.  Mở menu ngữ cảnh (nhấp chuột phải) cho ổ đĩa được mở rộng và chọn **Extend Volume**.

    Ghi chú

    Extend Volume có thể bị tắt (chuyển sang màu xám) nếu:

    * Không gian chưa phân bổ không liền kề với ổ đĩa. Không gian chưa phân bổ phải liền kề với phía bên phải của ổ đĩa mà bạn muốn mở rộng.
    * Ổ đĩa sử dụng kiểu phân vùng Bản ghi khởi động chính (MBR) và nó đã có kích thước 2TB. Ổ đĩa sử dụng MBR không thể vượt quá kích thước 2TB.\


    <figure><img src="../../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>
6.  Trong trình hướng dẫn **Extend Volume**, chọn **Next**. Đối với **Select the amount of space in MB**, hãy nhập số megabyte để mở rộng âm lượng. Nói chung, bạn chỉ định không gian tối đa có sẵn. Văn bản được đánh dấu bên dưới **Đã chọn** là dung lượng được thêm vào, không phải là kích thước cuối cùng mà ổ đĩa sẽ có. Hoàn thành trình hướng dẫn.\


    <figure><img src="../../../.gitbook/assets/image (431).png" alt=""><figcaption></figcaption></figure>

**Bước 2: Mở rộng tệp hệ thống Windows PowerShell**

Sử dụng quy trình sau để mở rộng hệ thống tệp Windows bằng PowerShell.

**Để mở rộng hệ thống tệp bằng PowerShell**

1. Trước khi mở rộng một hệ thống tệp có chứa dữ liệu có giá trị, cách tốt nhất là tạo ảnh chụp nhanh của ổ đĩa chứa nó trong trường hợp bạn cần khôi phục các thay đổi của mình.
2. Đăng nhập vào phiên bản Windows của bạn bằng Remote Desktop.
3. Chạy PowerShell với tư cách quản trị viên.
4. Chạy lệnh `Get-Partition`. PowerShell trả về số phân vùng tương ứng cho từng phân vùng, ký tự ổ đĩa, độ lệch, kích thước và loại. Lưu ý ký tự ổ đĩa của phân vùng để mở rộng.
5.  Chạy lệnh sau để quét lại đĩa.

    | `"rescan"` `\| diskpart` |
    | ------------------------ |
6.  Chạy lệnh sau, sử dụng ký tự ổ đĩa mà bạn đã lưu ý ở bước 4 thay cho \<ký tự ổ đĩa>. PowerShell trả về kích thước tối thiểu và tối đa của phân vùng được phép, tính bằng byte.

    | `Get-PartitionSupportedSize -DriveLetter <drive-letter>` |
    | -------------------------------------------------------- |
7.  Để mở rộng phân vùng đến một lượng xác định, hãy chạy lệnh sau, nhập kích thước mới của ổ đĩa thay cho \<size>. Bạn có thể nhập kích thước tính bằng KB, MB và GB; ví dụ: 50GB.

    | `Resize-Partition -DriveLetter <drive-letter>` `-Size <size>` |
    | ------------------------------------------------------------- |

    Để mở rộng phân vùng đến kích thước khả dụng tối đa, hãy chạy lệnh sau.

    | `Resize-Partition -DriveLetter <drive-letter>` `-Size $(Get-PartitionSupportedSize -DriveLetter <drive-letter>).SizeMax` |
    | ------------------------------------------------------------------------------------------------------------------------ |

    \
    Các lệnh PowerShell sau hiển thị dòng lệnh và phản hồi hoàn chỉnh để mở rộng hệ thống tệp đến một kích thước cụ thể.\
    \


    <figure><img src="../../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>

Các lệnh PowerShell sau hiển thị dòng lệnh và phản hồi hoàn chỉnh để mở rộng hệ thống tệp đến kích thước khả dụng tối đa.

<figure><img src="../../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>
