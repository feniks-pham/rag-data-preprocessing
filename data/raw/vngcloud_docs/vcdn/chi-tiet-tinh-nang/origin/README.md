# Origin

## Tổng quan

**Origin** trong CDN chính là máy chủ gốc chứa toàn bộ dữ liệu gốc của website. Đây là nơi lưu trữ bản gốc của các file như hình ảnh, video, HTML, CSS, JavaScript,... Mọi thay đổi trên website đều bắt nguồn từ Origin trước khi được phân phối đến các máy chủ (Edge server) của CDN.

## **Chi tiết**

Hiện tại, vCDN đang hỗ trợ 3 loại Origin: **HTTP Origin, S3 Origin và Host Origin**. Cụ thể, vui lòng tham khảo bảng bên dưới.

<table data-full-width="true"><thead><tr><th width="149">Loại Origin</th><th>Mô tả</th><th>Ví dụ</th><th>Loại dịch vụ hỗ trợ</th></tr></thead><tbody><tr><td><strong>HTTP Origin</strong></td><td>Lấy nội dung từ một máy chủ web hoặc ứng dụng thông qua giao thức HTTP/HTTPS.</td><td>Một website lưu trữ tại <code>https://example.com</code>.</td><td><ul><li>Web Accelerator</li><li>Object Download</li><li>Video On Demand</li></ul></td></tr><tr><td><strong>S3 Origin</strong></td><td>Lấy nội dung trực tiếp từ các dịch vụ lưu trữ đối tượng S3 - compatible.</td><td>Một bucket S3 có URL như <code>https://bucket-name.s3.amazonaws.com</code>.</td><td><ul><li>Object Download</li><li>Video On Demand</li></ul></td></tr><tr><td><strong>Host Origin</strong></td><td>Dữ liệu được cung cấp từ một server hoặc IP cụ thể do người dùng chỉ định.</td><td>Server tại địa chỉ IP <code>192.168.1.1</code> hoặc domain <code>cdn-origin.example.com</code>.</td><td><ul><li>Object Download</li><li>Video On Demand</li></ul></td></tr></tbody></table>
