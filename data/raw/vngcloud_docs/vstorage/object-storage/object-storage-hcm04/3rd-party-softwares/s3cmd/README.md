# S3cmd

## Tổng quan <a href="#s3cmd-tongquan" id="s3cmd-tongquan"></a>

S3cmd là một công cụ command line miễn phí và client để tải lên, lấy và quản lý dữ liệu trong Amazon S3 và các nhà cung cấp dịch vụ lưu trữ đám mây khác sử dụng giao thức S3 như Google Cloud Storage hay DreamHost DreamObjects. s3cmd phù hợp cho người sử dụng quen thuộc với các phần mềm command line. Công cụ cho phép batch script và backup tự động lên S3, kích hoạt tự động từ cron, ...

S3cmd được viết bằng ngôn ngữ lập trình Python. Đây là một dự án mã nguồn mở với giấy phép GNU Public License v2 (GPLv2) và miễn phí cho mục đích sử dụng thương mại và cá nhân. Bạn chỉ cần trả phí Amazon khi sử dụng dịch vụ lưu trữ của họ.

Để giúp bạn có thể cài đặt và cấu hình nhanh chóng công cụ người dùng này, chúng tôi cung cấp một tính năng tích hợp thông qua vStorage Portal. Bạn chỉ cần cung cấp thông tin Region, Project, thông tin chứng thực (vStorage credentials) chính xác và sau đó tải xuống tệp tin cấu hình (configuration file) cho S3cmd về là có thể sử dụng để tệp tin cấu hình này để truy cập đến tài nguyên của bạn trên dịch vụ lưu trữ vStorage. Chi tiết tham khảo tại Tích hợp công cụ S3cmd với vStorage.  Sau khi đã truy cập được các tài nguyên (project, bucket, object, v.v.) của bạn trên dịch vụ vStorage, để làm việc với các tài nguyên này sử dụng công cụ S3cmd, bạn có thể tham khảo thêm các tình huống (use case) sử dụng hay tính năng của S3cmd để làm việc với tài nguyên vStorage. Chi tiết tham khảo tại Sử dụng công cụ S3cmd.
