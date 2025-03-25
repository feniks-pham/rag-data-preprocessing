# Làm việc với vStorage-Log

Để có thể xem được log của vStorage Project bạn truy cập vào vMonitor, sau đó vào **Infrastructure list/vStorage Log**, tại đây hệ thống vMonitor đã tự động đồng bộ tất cả vStorage Project ở 2 Region: HCM và HN về. Tại màn hình này, mỗi vStorage Project bạn sẽ thấy các cột thông tin cơ bản như:

* **vStorage project**: tên của vStorage Project
* **vStorage region**: region của vStorage Project
* **Log Project**: log project sẽ chứ logs của vStorage Project khi bạn enable "Detailed Monitoring"
* **Log Project Usage**: thông tin về mức độ sử dụng của Log Project mà đã được gắn vào vStorage Project này
* **Monitoring Status**: trạng thái monitoring của vStorage Project, nếu chưa enable "Detailed Monitoring" thì trạng thái sẽ là INACTIVE, nếu đã enable thì trạng thái là ACTIVE và bạn có thể vào Log Project được gắn để xem vStorage Logs
* **Detailed Monitoring**: bật tắt theo dõi Logs của vStorage Project.

Để có thể xem Logs của vStorage Project bạn cần nhấn **enable** tại cột **Detailed Monitoring**, hệ thống sẽ hiển thị Popup và bạn cần **chọn Log Project** để chứa logs của vStorage Project này, sau đó nhấn "**enable**". Nếu bạn chưa có bất kì Log Project nào, bạn có thể nhấn "Create a log project" ở popup hoặc qua tab Quota & Usage để tạo Log Project trước.

<figure><img src="../../../../.gitbook/assets/image (333).png" alt=""><figcaption></figcaption></figure>

Sau khi enable bạn sẽ thấy status của vStorage Project này chuyển thành **ACTIVE**, và bạn có thể truy cập vào Log Project vừa chọn để xem logs

Nếu có nhu cầu thay đổi Log Project chứa Logs, bạn có thể chọn nút 3 chấm và chọn "**Edit Log Project**" để thay đổi.

Nếu không còn nhu cầu để xem logs của vStorage Project thì bạn có thể **disable** ở cột **Detailed Monitoring**.

***

## **Một số chú ý:**

* vStorage Project sau khi được tạo từ vStorage Portal, sẽ mất khoảng vào phút (tối đa 10 phút) để có thể đồng bộ về vMonitor
