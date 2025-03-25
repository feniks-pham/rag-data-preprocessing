# Cách tính phí

## Tổng quan

Hệ thống **vCDN** hỗ trợ cả hai loại người dùng:

1. **Người dùng trả trước**: Khách hàng mua trước dung lượng **Traffic** và sử dụng theo lượng đã mua.
2. **Người dùng trả sau**: Khách hàng sử dụng dịch vụ trước và thanh toán dựa trên mức tiêu thụ vào cuối kỳ.

***

## Traffic Package <a href="#huongdanmuahang-goitangtocwebsite" id="huongdanmuahang-goitangtocwebsite"></a>

### **Người dùng trả trước**

Khi mua **Traffic**, bạn có thể lựa chọn:

* **Group Type**: Chọn thời gian gói sử dụng (**3 tháng,** **6 tháng hoặc 12 tháng**).
* **Traffic Type**: Loại lưu lượng:
  * **Domestic**: Lưu lượng nội địa.
  * **International**: Lưu lượng quốc tế.
* **Package Traffic**: Dung lượng **Traffic** mong muốn.

{% hint style="info" %}
**Lưu ý:**

* Nếu bạn chọn **Traffic type = Domestic**, tối đa **20% traffic** có thể được sử dụng cho **international**.
  * Ví dụ: Gói Domestic 50000GB → 10000GB được phép dùng cho International.
* **Khi bạn sử dụng hết Traffic**:
  * **Domestic**: Có thể mua **Extra Domestic**, thời gian sử dụng phụ thuộc vào thời hạn của gói chính.
  * **International**: Có thể mua **Extra International** với thời hạn tương tự.
* Nếu bạn chọn **Traffic type =** **International**, traffic này có thể dùng cho cả **Domestic và International.**
* Mỗi tài khoản chỉ được áp dụng **1 gói chính duy nhất tại một thời điểm nhưng có thể mua nhiều gói extra.**
* Hệ thống có hỗ trợ **cộng dồn traffic** nếu bạn thay đổi gói.
{% endhint %}

### **Người dùng trả sau**

* Hệ thống sẽ thống kê **traffic tiêu thụ hàng tháng** và tính toán chi phí thanh toán vào cuối tháng.

## **Accelerator Package** <a href="#huongdanmuahang-goitangtocwebsite" id="huongdanmuahang-goitangtocwebsite"></a>

Khách hàng có thể mua các gói theo tính năng như:

* **Basic**, **Standard**, **Pro**, và **Enterprise**.
* Những gói này chỉ áp dụng cho dịch vụ **Web Accelerator**.

**DANH SÁCH CÁC TÍNH NĂNG CỦA WEB ACCELERATOR**

<table data-full-width="true"><thead><tr><th width="186">Tính năng</th><th width="467">Mô tả</th><th width="108">Cơ bản</th><th width="120">Tiêu chuẩn</th><th width="215">Cao cấp</th><th>Doanh Nghiệp</th></tr></thead><tbody><tr><td>Enable HTTP2</td><td>Bật/tắt hỗ trợ HTTP/2</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>CDN</td><td>Số lượng CDN có thể được tạo</td><td>1</td><td>3</td><td>5</td><td>20</td></tr><tr><td>Multi CNAME </td><td>Hỗ trợ khách hàng điền nhiều domain để sử dụng dịch vụ trên mỗi CDN    </td><td> </td><td>3</td><td>5</td><td>10</td></tr><tr><td>SSL Cert</td><td>Hỗ trợ khách hàng upload SSL để sử dụng dịch vụ    </td><td>50</td><td>50</td><td>50</td><td>50</td></tr><tr><td>Tối ưu hình ảnh</td><td><p>Tự động tối ưu hình ảnh trên website khách hàng:</p><p>  - Nếu hình ảnh chất lượng cao, tự giảm về 1080p hoặc bằng kích thước chiều dọc của màn hình thiết bị (&#x3C;1080);</p><p>  - Chất lượng ảnh: Tự động nén ảnh còn 60% cho PC, Tablet là 50% và mobile còn 30%;</p><p>**Với các trình duyệt hỗ trợ định dạng ảnh WebP => Tự động convert ảnh sang WebP để giảm dung lượng và tăng tốc độ load trang.</p></td><td> </td><td> </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Tự động thu nhỏ    </td><td>Tự động tối ưu các đoạn Javascript, CSS, HTMl trên website của khách hàng.    </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Cân bằng tải    </td><td>Hỗ trợ LB các Servers Origin trong pool để phân bố request hợp lý, các loại LB Algorithms hỗ trợ: Weight RoundRobin, Least Connected, IP Hashing.    </td><td> </td><td>3 (ips)</td><td>5 (ips)</td><td>50 (ips)</td></tr><tr><td>Hỗ trợ HSTS    </td><td>Hổ trợ HSTS    </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Hỗ trợ HTTPS    </td><td>Tự động rewrite trang chủ từ http -> https    </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Automatic HTTPS Rewrites    </td><td>Hỗ trợ rewrite các url http sang https tự động trong page content    </td><td> </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>TLS 1.3: Hỗ trợ TLS Version 1.3    </td><td>Hỗ trợ chọn version TLS thấp nhất có thể hỗ trợ    </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Brotli Compression    </td><td>Tùy chọn nén trang giúp giảm dung lượng đối với các thiết bị hỗ trợ    </td><td> </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Cache</td><td>Tùy chọn cache kết quả phản hồi từ origin    </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Development Mode</td><td>Bật chế độ không cache trên toàn dịch vụ    </td><td> </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Cache Browser</td><td>Thời gian Cache trên Browser    </td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr><tr><td>Cache Edge TTL </td><td>Thời gian Cache trên Edge    </td><td>>3 ngày</td><td>>1 ngày</td><td>>12 giò</td><td>>30 phút</td></tr><tr><td>Purge Cache</td><td>Công cụ hỗ trợ xóa nội dung đã cache trên hệ thống CDN    </td><td>5 lần/ngày</td><td>20 lần/ngày</td><td>50 lần/ngày</td><td>1000 lần/ngày</td></tr><tr><td>Page Rules</td><td>Tùy chọn page rule để điều chỉnh cache, chất lượng, kích thước, định dạng ảnh    </td><td>1 rule</td><td>3 rule</td><td>5 rule</td><td>100 rule</td></tr><tr><td>Thống kê</td><td>Báo cáo thống kê</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td><td>Có hỗ trợ</td></tr></tbody></table>

## &#x20;**Các bước thực hiện**

Hướng dẫn mua và sử dụng Traffic trên vCDN Portal

**Bước 1**: Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/).

**Bước 2**: Chọn **Package** hoặc **Buy More Traffic**. Màn hình **vCDN Billing** sẽ hiển thị.

<figure><img src="../.gitbook/assets/image (859).png" alt=""><figcaption></figcaption></figure>

**Bước 3**: Chọn **Accelerator Package** và **Period** (thời hạn sử dụng) mà bạn mong muốn. Nhấn **Confirm** để tiếp tục.

<figure><img src="../.gitbook/assets/image (860).png" alt=""><figcaption></figcaption></figure>

**Bước 4**: Tiếp tục thực hiện theo điều kiện:

* **Đối với khách hàng trả trước**: chọn thời gian sử dụng và gói **Traffic Package** mong muốn
* **Đối với khách hàng trả sau**: không cần chọn gói Traffic, có thể sử dụng ngay và thanh toán vào cuối tháng.
* Sau khi chọn gói (nếu có), nhấn **Confirm**.

<figure><img src="../.gitbook/assets/image (861).png" alt=""><figcaption></figcaption></figure>

**Bước 5**: Tại mục **Payment Details**, kiểm tra lại các gói dịch vụ đã chọn. Nếu thông tin chính xác, chọn **Payment Confirm** để hoàn tất.

<figure><img src="../.gitbook/assets/image (862).png" alt=""><figcaption></figcaption></figure>

**Bước 6**: Tại màn hình **Payment Confirm**, chọn **Continue**. Thực hiện các bước thanh toán theo hướng dẫn.

<figure><img src="../.gitbook/assets/image (863).png" alt=""><figcaption></figcaption></figure>

**Bước 7:** Sau khi hoàn tất, bạn có thể kiểm tra thông tin thanh toán và tiêu thụ tại mục **Pay/Consume History**.
