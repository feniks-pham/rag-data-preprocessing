# Khởi tạo File Storage

Để khởi tạo một File Storage trên hệ thống File Storage, bạn có thể làm theo các bước sau:

## Khởi tạo File Storage

**Bước 1:** Truy cập vào [https://efs.console.vngcloud.vn/overview](https://efs.console.vngcloud.vn/overview)

**Bước 2:** Chọn mục **File Storage** sau đó chọn **Create a File storage**.

<figure><img src="../../../.gitbook/assets/image (818).png" alt=""><figcaption></figcaption></figure>

**Bước 3:** Tại màn hình khởi tạo File Storage, bạn cần nhập/ chọn:&#x20;

* **File Storage name:** tên gợi nhớ của file storage. Tên file cần dài từ 5 tới 50 ký tự và có thể bao gồm các ký tự a-z, A-Z, 0-9, '-', '\_'
* **Description**: nhập mô tả cho file storage.
* **File storage type:** chọn loại ổ đĩa mà bạn mong muốn sử dụng. Hiện tại chúng tôi chỉ cung cấp loại ổ đĩa **Standard HDD.**
* **Protocol:** chọn protocol mà bạn mong muốn. Hiện tại chúng tôi đang hỗ trợ:
  * **NFS**: v4.0, 4.1
  * **SMB**: v2.0+&#x20;
* **Tag:** bạn có thể thêm các tag để đánh dầu file storage theo nhu cầu.
* **File Storage Max quota:** trong bước khởi tạo file storage, bạn cần đặt một giới hạn quota tối đa cho file storage đó. Quota này có ý nghĩa chính là giới hạn dung lượng lưu trữ mà file storage có thể sử dụng, giúp quản lý tài nguyên hiệu quả. <mark style="color:red;">**Mức quota tối thiểu bạn cần chọn là 1 TB và mức quota tối đa chúng tôi cung cấp là 50 TB.**</mark> Nếu bạn có nhu cấu sử dụng nhiều hơn 50 TB cho một file storage, vui lòng liên hệ với chúng tôi.
* **Network type**: lựa chọn network type mà bạn mong muốn. Hiện tại, chúng tôi đang hỗ trợ:&#x20;
  * **Public**: mọi truy cập là công khai, bạn có thể sử dụng file storage này cho các VM, K8S on-premise, trên VNG Cloud hay tài nguyên tại các nguồn khác.&#x20;
  * **Private:** các kết nối riêng tư trong hệ sinh thái VNGClou&#x64;**.**
* **Permission: c**ấu hình quyền truy cập dựa trên IP
  * **No one:** Không có IP nào được phép truy cập.
  * **All:** Cho phép tất cả IP có quyền truy cập RO (Read-Only) hoặc RW (Read-Write).
  * **Restricted:** Chỉ cho phép một số IP cụ thể truy cập với quyền RO hoặc RW.

**Bước 5:** Chọn **Create File Storage.**
