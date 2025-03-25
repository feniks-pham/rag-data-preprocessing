# Tạo bản sao lưu cho máy chủ ảo theo bộ lịch Policy

Trên bảng điều khiển của vBackup, trang tài nguyên được bảo vệ sẽ liệt kê tất cả các tài nguyên được sao lưu ít nhất một lần. Nếu bạn đang sử dụng vBackup cho lần đầu tiên thì lưu ý rằng sẽ không có bất kỳ tài nguyên nào (chẳng hạn như máy ảo hay ổ đĩa được bảo vệ) được liệt kê trên trang này. Tại VNG Cloud chúng tôi hỗ trợ bảo vệ dữ liệu tập trung cho các máy ảo (Server) trên môi trường điện toán đám mây. Bạn có thể sao lưu máy ảo và dữ liệu sẽ được chuyển sang vStorage.

Tuy nhiên điều cần làm lúc này là tạo phiên công việc Backup cho tài nguyên của bạn theo hướng dẫn bên dưới:

***



{% hint style="info" %}
Quan trọng

Khi bạn sử dụng dịch vụ vBackup. Trong lần đầu tiên, chúng tôi sẽ tự động tạo một nơi lưu trữ mặc định tại vStorage với dung lượng miễn phí 50 GB và thời hạn sử dụng 1 tháng, tuy nhiên để có thể lưu trữ với dung lượng lớn hơn, bạn cần phải mua thêm dung lượng lưu trữ. Việc sử dụng và thanh toán của backup sẽ được lưu trữ tại lớp Gold class của vStorage, xem thêm các chính sách và điều khoản lưu trữ dung lượng backup tại đây [https://docs.vngcloud.vn/pages/viewpage.action?pageId=59802113](https://docs.vngcloud.vn/pages/viewpage.action?pageId=59802113)
{% endhint %}



### **Tạo bản sao lưu theo bộ lịch Policy tại giao diện vBackup** <a href="#taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicytaigiaodienvbackup" id="taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicytaigiaodienvbackup"></a>

1. Mở bảng điều khiển vBackup tại [https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-server](https://hcm-3.console.vngcloud.vn/vserver/block-store/backup/backup-server)
2. Chọn **Tạo Backup Server**
3. Chọn loại tài nguyên bạn muốn sao lưu, ở đây là danh sách Server và Volume đính kèm với nó
4. Chọn **Policy** bạn muốn áp dụng cho bản sao lưu. Lưu ý bạn cần tạo một Policy để có thể thêm vào cho bản Backup Server của mình. Xem hướng dẫn tạo Policy tại [Tạo, chỉnh sửa, xóa chính sách sao lưu](chinh-sach-sao-luu/tao-chinh-sua-xoa-chinh-sach-sao-luu.md)
5. Nơi lưu trữ mặc định sẽ nằm tại **vStorage,** nên lưu ý rằng khi thực hiện thao tác chọn tài nguyên để tạo bản sao lưu, hệ thống sẽ tính toán và đưa ra kết quả dự đoán về dung lượng tạo bản sao lưu, để việc tạo không bị gián đoạn và gặp sự cố cần đảm bảo rằng dung lượng nơi lưu trữ của bạn tại vStorage là đủ dùng
6. Nhập thông tin **ghi chú** cho các bản sao lưu của bạn để tạo sự gợi nhớ&#x20;
7. Chọn **Tạo Backup Server**
8. Sau đó bạn có thể xem thông tin công việc sao lưu vừa tạo tại màn hình danh sách, chọn Backup Server để xem các thông tin về máy ảo được bảo vệ và ổ đĩa đính kèm, chính sách, nơi lưu trữ và kích thước bản sao lưu cũng như thời gian sao lưu gần nhất

### **Tạo bản sao lưu theo bộ lịch Policy khi khởi tạo Server** <a href="#taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicykhikhoitaoserver" id="taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicykhikhoitaoserver"></a>

1. Ngoài cách tạo bản sao lưu tại giao diện vBackup, bạn cũng có thể tùy chọn tạo bản sao lưu khi tạo mới Server. Thực hiện mở bảng điều khiển Server tại [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Chọn **Tạo mới một Server**
3. Trang tạo mới Server sẽ hiển th&#x1ECB;**,** tại đây bạn có thể tích chọn vào ô tạo Backup Server tại mục **Cài đặt Khác**
4. Sau đó khi Server được tạ&#x6F;**,** một bản Backup Server sẽ được tạo kèm cùng với bộ lịch Policy mặc định và hiển thị tại trang danh sách Backup Server

### **Tạo bản sao lưu theo bộ lịch Policy tại trang danh sách Server** <a href="#taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicytaitrangdanhsachserver" id="taobansaoluuchomaychuaotheobolichpolicy-taobansaoluutheobolichpolicytaitrangdanhsachserver"></a>

1. Bạn có thể tạo nhanh bản sao lưu cho một hoặc nhiều Server tại trang quản lý danh sách các Server. Thực hiện mở bảng điều khiển Server tại [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Tích chọn một hoặc nhiều Server cần tạo bản sao lưu, sau đó nhấn vào vào thanh công cụ và chọn **Tạo Backup**
3. Một hoặc nhiều bản Backup Server sẽ được tạo với bộ lịch Policy mặc định tùy theo số lượng Server bạn đã chọn để tạo bản sao lưu

Sau khi tạo Backup Server, bạn có thể đợi tới thời gian trong bộ lịch Policy để hệ thống thực hiện tạo tệp Backup, hoặc có thể lựa chọn [Backup Now](tao-ban-sao-luu-ngay-lap-tuc-backup-now.md) để tạo bạn Backup ngay tại thời điểm bạn thao tác chọn.

\


\
