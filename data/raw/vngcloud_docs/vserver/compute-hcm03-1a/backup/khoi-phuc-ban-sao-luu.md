# Khôi phục bản sao lưu

Sau khi một tài nguyên đã được sao lưu ít nhất một lần, tài nguyên đó được coi là đã được bảo vệ và có sẵn để khôi phục bằng vBackup.

Nếu bạn đang khôi phục máy ảo của VNG Cloud, bạn có thể thực hiện Khôi phục hoàn toàn để khôi phục toàn bộ hệ thống của máy ảo lên một máy ảo mới. Hoặc, bạn có thể khôi phục các ổ đĩa cụ thể thuộc một máy ảo. Làm theo các bước dưới đây để hoàn thực hiện việc khôi phục một máy ảo hoặc ổ đĩa của bạn:

### **Quy trình khôi phục máy chủ ảo** <a href="#khoiphucbansaoluu-quytrinhkhoiphucmaychuao" id="khoiphucbansaoluu-quytrinhkhoiphucmaychuao"></a>

1. Mở bảng điều khiển vBackup tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup)
2. Tại trang điều hướng, chọn máy chủ ảo được sao lưu và nhấn vào **Restore**
3. Trang tạo mới máy chủ ảo sẽ hiển thị với cấu hình của bản sao lưu, bạn cần chọn các thông số còn lại để hoàn tất việc khôi phục bản sao lưu lên một máy ảo
4. Chọn **tạo mới máy ảo**&#x20;
5. Một máy chủ ảo sẽ tạo ra ở trạng thái **Shutdown** với cấu hình của bản sao lưu mà bạn đã chọn trước đó

### **Quy trình khôi phục ổ đĩa** <a href="#khoiphucbansaoluu-quytrinhkhoiphucodia" id="khoiphucbansaoluu-quytrinhkhoiphucodia"></a>

1. Mở bảng điều khiển vBackup tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup)
2. Tại trang điều hướng, xem chi tiết máy chủ ảo được sao lưu
3. Tại danh sách ổ đĩa đính kèm với máy ảo, chọn ổ đĩa bạn được sao lưu và nhấn vào **Restore**
4. Trang tạo mới ổ đĩa sẽ hiển thị với cấu hình của bản sao lưu, bạn cần chọn các thông số còn lại để hoàn tất việc khôi phục bản sao lưu lên một ổ đĩa
5. Chọn **tạo mới ổ đĩa**
6. Một ổ đĩa mới được tạo ra với cấu hình của bản sao lưu mà bạn đã chọn trước đó



{% hint style="info" %}
Ghi chú

Bất kể bạn thực hiện khôi phục một máy ảo hay ổ đĩa, mỗi lần khôi phục sẽ đều sẽ tạo mới. Nếu bạn thử khôi phục nhiều lần cho cùng một tài nguyên, có thể tồn tại nhiều mục trùng nhau cho tài nguyên đó.
{% endhint %}
