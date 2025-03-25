# Khởi tạo Certificate

Sau khi mua Log Project, hệ thống sẽ tự động sinh ra certificate cho từng Log Project, certificate này dùng để xác thực Log Agent với hệ thống vMonitor Platform. Để tạo mới hay tải xuống một certificate, hãy làm theo các bước bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor).&#x20;
2. Chọn **Integration -> c**họn **Certificate.**
3. Nếu bạn chưa khởi tạo Log project nào, chọn **New cert** để tạo Certificate mới. Nếu bạn đã khởi tạo Log project thành công từ  [Khởi tạo Log project](../lam-viec-voi-log-project-quota.md), tại Log project này, chọn **New cert.**
4. Chúng tôi bắt đầu khởi tạo certificate cho Log project của bạn, khi trạng thái certificate là **ACTIVE** nghĩa là certificate này đã sẵn sàng cho bạn sử dụng.&#x20;
5. Chọn **Tải xuống** để tải thông tin certificate về thiết bị của bạn hoặc chọn **Delete** để xóa Certificate vừa tạo.&#x20;

Sau khi tải về và giải nén, bạn sẽ thấy các tệp tin certificate và các câu lệnh hướng dẫn cài đặt theo từng môi trường và từng loại agent giúp bạn dễ dàng thiết lập bước đầu:

| <pre><code>/Linux
│   ├── Filebeat               // Bộ cài cho agent filebeat , môi trường Linux
│   |   ├── VNG.trust.pem      // các file pem để  xác thực người dùng
│   |   ├── user.cer.pem       
│   |   ├── user.key.pem
│   |   ├── filebeat.sh        // script cài khởi đầu
│   |   ├── info.md            // thông tin endpoint gửi dữ liệu
│   |   ├── readme.md          // hướng dẫn sơ bộ
│   ├── Logstash               // Bộ cài cho agent logstash , môi trường Linux
/Windows                       // Bộ cài cho môi trường Windows
│   ├── ...                    // tương tự cũng có các file .pem như trên
/Docker                        // Bộ cài cho môi trường Docker
/Kubernetes                    // Bộ cài cho môi trường Kubernetes
</code></pre> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

\
