# Tạo bản sao lưu ngay lập tức (Backup Now)

Tính năng Backup Now cho phép bạn thực hiện một phiên sao lưu dữ liệu ngay lập tức bằng cách nhấn vào một nút "Backup Now" cho bản Backup Server hoặc Server bạn chọn. Thường thì, người dùng có thể cần thực hiện việc sao lưu định kỳ, nhưng đôi khi cũng cần thực hiện một phiên sao lưu ngay tức thì để bảo vệ dữ liệu quan trọng tại thời điểm đó.

Lợi ích của Sao lưu Dữ liệu Ngay Lập Tức:

1. **Tính Linh Hoạt và Khẩn Cấp:** Sao lưu dữ liệu ngay lập tức cho phép bạn thực hiện việc sao lưu bất kỳ khi nào bạn cảm thấy cần thiết, thay vì phải chờ đến thời điểm sao lưu định kỳ. Điều này rất hữu ích trong tình huống khẩn cấp hoặc khi bạn muốn bảo vệ dữ liệu ngay lập tức trước một sự cố có thể xảy ra.
2. **Bảo Vệ Dữ Liệu Quan Trọng Trong Thời Gian Ngắn:** Nếu bạn chỉ cần sao lưu một phần nhỏ hoặc một dự án cụ thể, việc sao lưu ngay lập tức sẽ giúp bạn bảo vệ những dữ liệu quan trọng mà bạn vừa làm việc trên chúng.
3. **Phục Hồi Nhanh Chóng:** Khi bạn cần phục hồi dữ liệu, bạn sẽ có bản sao lưu gần nhất\


***

### **Tạo bản sao lưu ngay lập tức cho bản Backup Server trên bảng điều khiển vBackup** <a href="#taobansaoluungaylaptuc-backupnow-taobansaoluungaylaptucchobanbackupservertrenbangdieukhienvbackup" id="taobansaoluungaylaptuc-backupnow-taobansaoluungaylaptucchobanbackupservertrenbangdieukhienvbackup"></a>

1. Sau khi tạo bản Backup Server theo bộ lịch Policy. Xem hướng dẫn tạo Backup Server tại [Tạo bản sao lưu cho máy chủ ảo theo bộ lịch Policy](tao-ban-sao-luu-cho-may-chu-ao-theo-bo-lich-policy.md)
2. Chọn bản Backup Server vừa tạo, sau đó chọn **Backup Now**
3. Chọn **Backup Now,** và sau đó một bản Backup sẽ được tạo ngay tại thời điểm thực hiện hành động đồng thời sẽ hiển thị tại trang danh sách Backup Server



{% hint style="info" %}
**Lưu ý**

Khi bạn tạo bản Backup Now cho Backup Server, bản Backup này sẽ nằm tại Tab Restore Point, và không bị ảnh hưởng theo luật xóa (Retention) của bộ lịch Policy, trừ khi bạn thao tác xóa chúng.
{% endhint %}

***

### **Tạo bản sao lưu ngay lập tức cho Server trên bảng điều khiển vBackup** <a href="#taobansaoluungaylaptuc-backupnow-taobansaoluungaylaptucchoservertrenbangdieukhienvbackup" id="taobansaoluungaylaptuc-backupnow-taobansaoluungaylaptucchoservertrenbangdieukhienvbackup"></a>

1. Bạn có thể thực hiện tạo Backup Now tại trang danh sách Server. Truy cập vào bảng điều khiển vServer tại đường link: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Chọn một hoặc nhiều Server bạn muốn tạo bản Backup ngay lập tức
3. Sau đó chọn **Hành động, chọn** Backup Now
4. Sau đó một bản Backup sẽ được tạo ngay tại thời điểm thực hiện hành động đồng thời sẽ hiển thị tại trang danh sách Backup Server

{% hint style="info" %}
**Lưu ý**

Khi bạn tạo bản Backup Now cho Server, bản Backup này sẽ nằm tại Tab Restore Point, và không bị ảnh hưởng theo luật xóa (Retention) của bộ lịch Policy, trừ khi bạn thao tác xóa chúng.
{% endhint %}
