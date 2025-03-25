# Làm việc với vCDN-Log

### Tổng quan <a href="#lamviecvoivcdn-log-tongquan" id="lamviecvoivcdn-log-tongquan"></a>

**vCDN Log Monitoring** là hệ thống tích hợp giữa **vCDN** và **vMonitor Platform** giúp người dùng giám sát tài nguyên trên vCDN thông qua việc đồng bộ, thu thập và lọc thông tin tại từng **CDN domain** của người dùng. Để bật/ tắt (enable/ disable) tính năng đẩy logs từ **vCDN** về hệ thống vMonitor Platform, trước tiên bạn hãy truy cập tại [đây.](https://hcm-3.console.vngcloud.vn/vmonitor) Sau đó chọn thư mục **Infrastructure list/vCDN - Log.** Tại đây, bạn có thể xem danh sách tất cả các **vCDN domain** mà bạn có trên tài khoản của bạn.

* Tại màn hình này, bạn sẽ thấy các cột thông tin cơ bản như:
  * **vCDN domains**: tên domain của CDN.
  * **Domain type**: loại domain. Hiện tại, chúng tôi đang hỗ trợ bạn đẩy và giám sát logs của 4 loại hình dịch vụ trên vCDN bao gồm: **Web Accelerator, Object Download, Video on Demand, Live Streaming.**
  * **Log Project**: log project trên vMonitor Platform và là nơi sẽ chứa logs vCDN domain đổ về khi bạn bật tính năng **Detail Monitoring**.
  * **Log Project Usage**: thông tin về mức độ sử dụng của Log Project mà bạn đã thiết lập làm nơi nhận vCDN logs này.
  * **Monitoring Status**: trạng thái monitoring của vCDN domain. Nếu bạn chưa bật tính năng Detailed Monitoring thì trạng thái sẽ là **INACTIVE**, nếu bạn đã bật tính năng này và chọn một Log project làm nơi nhận vCDN logs thì trạng thái sẽ là **ACTIVE**, còn nếu vCDN domain đã bị xóa khỏi hệ thống vCDN thì trạng thái sẽ là **DELETED**. Sau 24h, nếu không có logs đổ về thì các vCDN domain có trạng thái monitoring là **DELETED** sẽ bị ẩn khỏi giao diện monitoring của bạn.
  * **Detailed Monitoring**: bật/ tắt (enable/ disable) tính năng theo dõi Logs của từng vCDN domain.

<figure><img src="../../../../.gitbook/assets/image (334).png" alt=""><figcaption></figcaption></figure>

***

### Bật (enable) tính năng Detailed Monitoring <a href="#lamviecvoivcdn-log-bat-enable-tinhnangdetailedmonitoring" id="lamviecvoivcdn-log-bat-enable-tinhnangdetailedmonitoring"></a>

Để bật (enable) tính năng theo dõi logs của từng vCDN domain, bạn cần nhấn vào biểu tượng **Enable** tại cột **Detailed Monitoring:**&#x20;

* Lúc này hệ thống sẽ hiển thị popup và bạn cần **chọn Log Project** để chứa logs của vCDN domain này, sau đó nhấn nút **Enable**.  Nếu bạn chưa có bất kì Log Project nào, bạn có thể nhấn nút **Create a log project** ở popup hoặc trở lại menu **Quota & Usage** để tạo **Log Project** trước.

<figure><img src="../../../../.gitbook/assets/image (335).png" alt="" width="375"><figcaption></figcaption></figure>

* Sau khi bật enable monitoring bạn sẽ thấy status của vCDN domain này chuyển thành **INACTIVE** thành **ACTIVE**, lúc này bạn có thể truy cập vào Log Project vừa chọn để xem logs. Chi tiết tham khảo thêm tại [Làm việc với Log search](../lam-viec-voi-log-search/).

<figure><img src="../../../../.gitbook/assets/image (336).png" alt=""><figcaption></figcaption></figure>

***

### Chỉnh sửa Log project nhận vCDN logs <a href="#lamviecvoivcdn-log-chinhsualogprojectnhanvcdnlogs" id="lamviecvoivcdn-log-chinhsualogprojectnhanvcdnlogs"></a>

Nếu bạn có nhu cầu thay đổi Log Project chứa Logs, bạn có thể chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/69468834/image2024-1-9\_13-27-31.png?version=1\&modificationDate=1704781652000\&api=v2) và chọn nút **Edit Log Project**. Tại popup **Change Log project**, bạn hãy chọn Log Project mới mà bạn muốn thay đổi và bấm **Save**.

<figure><img src="../../../../.gitbook/assets/image (337).png" alt="" width="375"><figcaption></figcaption></figure>

***

### Tắt tính năng Detail Monitoring <a href="#lamviecvoivcdn-log-tattinhnangdetailmonitoring" id="lamviecvoivcdn-log-tattinhnangdetailmonitoring"></a>

Nếu bạn không còn nhu cầu để xem logs của 1 vCDN domain bất kỳ, bạn cần nhấn vào biểu tượng **Disable** tại cột **Detailed Monitoring**:

* Lúc này hệ thống sẽ hiển thị popup và bạn cần chọn **Disable** để tắt tính năng đẩy logs từ **vCDN domain** đang chọn về hệ thống vMonitor Platform.

<figure><img src="../../../../.gitbook/assets/image (338).png" alt="" width="375"><figcaption></figcaption></figure>

***

### Một số chú ý: <a href="#lamviecvoivcdn-log-motsochuy" id="lamviecvoivcdn-log-motsochuy"></a>

* vCDN domain sau khi được tạo sẽ mất tối đa **5 phút** để có thể đồng bộ về vMonitor Platform.
* Kể từ thời điểm bật Detail monitoring cho một vCDN domain, sẽ mất một khoảng thời gian (có thể từ **5 phút - 10 phút**) để logs có thể xuất hiện tại hệ thống vMonitor Platform. (Thông số này tùy thuộc vào độ trễ đẩy logs của hệ thống vCDN).
* Kể từ thời điểm xóa một vCDN domain trên hệ thống vMonitor Platform, trong vòng **24h** thì chúng tôi sẽ xóa hoàn toàn vCDN domain của bạn khỏi hệ thống vMonitor Platform.
