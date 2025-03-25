# Host Origin

## Tổng quan

**Host Origin** là một loại nguồn dữ liệu (origin) được sử dụng trong vCDN để truy xuất nội dung từ một server hoặc địa chỉ cụ thể do người dùng chỉ định. Khác với các origin như S3 Origin, Host Origin thường được sử dụng khi nội dung của bạn được lưu trữ trên các máy chủ web (web server) hoặc ứng dụng nội bộ.

## Chi tiết

Để kết nối trực tiếp đến origin thông qua tên miền được chỉ định, hãy nhập/ chọn các thông số sau:&#x20;

<figure><img src="../../../.gitbook/assets/image (12) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Origin Host Header:** Header được gửi tới Origin Server trong yêu cầu HTTP.
* **Use SSL:** Kích hoạt SSL để mã hóa kết nối với Host Origin.
