# Tăng dung lượng tự động (Auto-scale Quota)

### Tổng Quan

Tính năng Tự động tăng dung lượng lưu trữ (Auto-scale Quota) trên vStorage cho phép bạn thiết lập tự động mở rộng dung lượng lưu trữ dựa trên mức sử dụng và nhu cầu của bạn. Hướng dẫn này sẽ cung cấp chi tiết cách thức cấu hình và quản lý tính năng này thông qua vStorage Portal.

***

### Các bước thực hiện

**Bước 1:** Đăng nhập vào vStorage Portal tại [đây](https://vstorage.console.vngcloud.vn/overview).

**Bước 2**: Tại project cần thiết lập Auto-scale Quota, chọn biểu tượng <img src="../../../../../.gitbook/assets/image (398).png" alt="" data-size="line"> sau đó chọn mục **Auto-scale** và tiếp tục chọn **Configure Auto-scale** hoặc chọn biểu tượng <img src="../../../../../.gitbook/assets/image (400).png" alt="" data-size="line"> sau đó chọn **Set Auto-scale**.

**Bước 3**: Tại màn hình cấu hình **Auto-scale**, thực hiện thiết lập các thông số cần thiết cho **Auto Scale**. Cụ thể:&#x20;

* **Thiết lập Quota Unit:** bạn có thể chọn 1 trong hai loại đơn vị bao gồm **GB** hoặc **Percent**.
* **Thiết lập Quota Threshold hoặc Quota Remain:** Nếu bạn chọn **Quota Unit** là **Percent**, tại đây bạn sẽ nhập phần trăm ngưỡng sử dụng mà khi đạt tới thì hệ thống sẽ kích hoạt việc tăng quota. Nếu bạn chọn **Quota Unit** là **GB**, tại đây bạn sẽ nhập lượng quota còn lại mà khi đạt tới hệ thống cũng sẽ kích hoạt việc tăng quota.&#x20;
* **Thiết lập Mức Tăng Quota**: nhập mức tăng mong muốn theo **GB** hoặc **Percent**.

**Bước 4**: Chọn nhận thông báo qua **email** khi tăng quota thành công nếu muốn.

**Bước 5:** Bật tính năng **Auto-scale** tại biểu tượng <img src="../../../../../.gitbook/assets/image (402).png" alt="" data-size="line">. Khi biểu tượng này trở thành <img src="../../../../../.gitbook/assets/image (403).png" alt="" data-size="line">tức là bạn đã bật **Auto-scale** thành công.&#x20;

**Ví Dụ:**&#x20;

1. Giả sử, bạn cần thiết lập tự động tăng dung lượng quota lên **50%** nếu usage/ quota của bạn chạm ngưỡng **80%**. Cụ thể:
   * **Quota ban đầu**: 100 GB
   * **Lượng Usage Sử dụng**: 83 GB
   * **Bạn cấu hình Quota Threshold**: 80%
   * **Bạn cấu hình Quota Up**: 50%
   * **Hệ thống tự động tăng Quota mới**: 100 GB + (100 GB \* 50%) = 150 GB
2. Một ví dụ khác, bạn cần thiết lập tự động tăng dung lượng quota lên **50 GB** nếu lượng quota còn lại của bạn **<= 30 GB**. Cụ thể:&#x20;
   * **Quota ban đầu**: 100 GB
   * **Lượng Usage Sử dụng**: 83 GB
   * **Bạn cấu hình Quota Remain:** 30 GB
   * **Bạn cấu hình Quota Up**: 50 GB
   * **Hệ thống tự động tăng Quota mới**: 100 GB + 50 GB = 150 GB

{% hint style="info" %}
**Chú ý:**

* **Hệ thống vStorage** sẽ thực hiện kiểm tra project có/ không đủ điều kiện được auto-scale theo chu kỳ mỗi **5 phút** để tự động tăng dung lượng dựa trên ngưỡng đã thiết lập.
* Giá cước áp dụng theo bảng giá **vStorage tiêu chuẩn**, tính năng chỉ thực hiện tăng dung lượng mà không làm thay đổi Storage Class.
* Người dùng cần đảm bảo có **đủ số dư credit** cho tài khoản (trả trước) trước khi thực hiện Auto-scale.
* Nếu việc tăng dung lượng **thất bại**, người dùng sẽ nhận được thông báo qua email. Sau hai lần thực hiện auto-scale thất bại liên tiếp, hệ thống của chúng tôi sẽ ngừng gửi thông báo qua email cho bạn. Bạn cần chủ động truy cập vào vStorage để thực hiện resize project thủ công theo hướng dẫn tại [đây](tang-giam-han-muc-project.md).
{% endhint %}
