# Khôi phục tài nguyên

Hướng dẫn này sẽ giúp bạn thực hiện quá trình khôi phục tài nguyên (server hoặc volume) từ các bản sao lưu đã tạo trước đó. Quá trình khôi phục sẽ giúp bạn đưa hệ thống về trạng thái trước đó tại một thời điểm cụ thể, đảm bảo tính liên tục và an toàn cho dữ liệu của bạn.

#### Khái niệm

* **Backup server point:** Một bản sao lưu đầy đủ của toàn bộ máy chủ tại một thời điểm cụ thể.
* **Backup volume point:** Một bản sao lưu của một volume (ổ đĩa) cụ thể trong máy chủ.
* **Khôi phục server:** Khôi phục toàn bộ máy chủ về trạng thái của một backup server point.
* **Khôi phục volume:** Khôi phục một volume cụ thể về trạng thái của một backup volume point.

#### Các bước thực hiện

1. Truy cập vào trang danh sách backup server tại đây: [https://backupcenter.console.vngcloud.vn/backup-server/list](https://backupcenter.console.vngcloud.vn/backup-server/list)
2. Chọn Backup Server cần khôi phục. Bạn có thể nhấn vào ô tìm kiếm, nhập tên backup server cần tìm. ![](<../../../.gitbook/assets/image (767).png>)
3.  Tại trang chi tiết của Backup Server, nhấn chọn tab Restore Point. Tại đây, bạn sẽ thấy danh sách các bản backup server point đã tạo.&#x20;

    <figure><img src="../../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>
4. Chọn bản sao lưu cần khôi phục và nhấn restore cho 2 trường hợp sau:

*   **Chọn backup server point:** Nếu muốn khôi phục toàn bộ máy chủ, hãy chọn backup server point mong muốn và nhấn restore.&#x20;

    <figure><img src="../../../.gitbook/assets/image (1) (2).png" alt=""><figcaption></figcaption></figure>
*   **Chọn backup volume point:** Nếu chỉ muốn khôi phục một volume cụ thể, hãy chọn backup server point chứa volume đó, sau đó chọn backup volume point cần khôi phục và nhấn restore.&#x20;

    <figure><img src="../../../.gitbook/assets/image (2) (2).png" alt=""><figcaption></figcaption></figure>

5. Sau khi nhấn Restore, hệ thống sẽ điều hướng người dùng đến trang khởi tạo Server hoặc Volume để tiến hành cấu hình các thông số cần thiết. Nhấn khởi tạo để bắt đầu quá trình khôi phục.

#### Lưu ý quan trọng

* Server được tạo mới từ việc restore backup server point sẽ có trạng thái **Shutdown**, người dùng cần chủ động vào Start Server khi có nhu cầu sử dụng
* **Backup đầy đủ:** Đảm bảo rằng bản sao lưu bạn chọn chứa đầy đủ dữ liệu cần khôi phục.
* **Kiểm tra dữ liệu:** Sau khi khôi phục, hãy kiểm tra lại dữ liệu để đảm bảo tính chính xác và đầy đủ.
* **Quyền hạn:** Bạn cần có quyền để thực hiện các thao tác khôi phục.
* **Kế hoạch khôi phục:** Nên có một kế hoạch khôi phục chi tiết để ứng phó nhanh chóng trong trường hợp xảy ra sự cố.
