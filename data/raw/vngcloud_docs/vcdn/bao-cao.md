# Báo cáo

## T**ổng quan**

Ngoài Dashboard, Hệ thống vCDN đang cung cấp tính năng **Report**, cho phép khách hàng theo dõi và phân tích lịch sử sử dụng CDN của mình. Các báo cáo được cập nhật dữ liệu với tần suất **tới ngày N-1** (ngày hiện tại là N).

## Chi tiết

Các thông tin thống kê trong report bao gồm:

* **Thông tin chính:**
  * **CDN**: Bao gồm các loại tài nguyên như Web Accelerator, Object Download, Video on Demand (VoD), Live Stream, và Live Entrypoint mà khách hàng sở hữu.
  * **Group Type**: Phân loại gói dịch vụ khách hàng đang sử dụng (Basic, Standard, Pro, Enterprise).
  * **Traffic Type**: Phân biệt lưu lượng truyền tải, gồm:
    * **Domestic**: Lưu lượng nội địa.
    * **International**: Lưu lượng quốc tế.
* **Dữ liệu chi tiết:**
  * **Traffic từng ngày**: Lưu lượng truy cập được tính từ **07:00 ngày N-2 đến 07:00 ngày N-1**.
  * **Tổng lưu lượng CDN (Total CDN's Traffic)**: Tổng lưu lượng qua toàn bộ các tài nguyên CDN của khách hàng trong khoảng thời gian lọc.
* **Tùy chọn nhiều ngày:**
  * Khách hàng có thể sử dụng bộ lọc để xem báo cáo của một hoặc nhiều ngày trong quá khứ tùy ý.

## **Các bước thực hiện**

**Bước 1:** Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)

**Bước 2:** Chọn mục **Report** để xem báo cáo. Dữ liệu bao gồm các thông tin thống kê như đã nêu ở phần chi tiết.

<figure><img src="../.gitbook/assets/image (857).png" alt="" width="166"><figcaption></figcaption></figure>

**Bước 3:** Bạn có thể thực hiện **Filter theo điều kiện:**

* **Service**: Loại dịch vụ.
* **CDN**: Chọn tài nguyên cụ thể.
* **Traffic Type**: Domestic hoặc International.
* **Group**: Gói dịch vụ.
* **Khung thời gian:** Chọn khoảng thời gian báo cáo.

<figure><img src="../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

**Bước 4:** Nhấp vào biểu tượng **Excel** để xuất báo cáo ra file Excel để lưu trữ hoặc phân tích thêm.

<figure><img src="../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>
