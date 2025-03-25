# Bắt đầu với SDR

Server Disaster Recovery (SDR) là giải pháp quan trọng để đảm bảo tính liên tục cho hoạt động kinh doanh của bạn trong trường hợp xảy ra sự cố không mong muốn. Dưới đây là hướng dẫn chi tiết để bạn bắt đầu sử dụng tính năng Server DR trên VNG Cloud, đi qua các tính năng chính và cách thức hoạt động của chúng.

## **1. Truy cập VNG Cloud Console:**

* Truy cập vào bảng điều khiển Server Disaster Recovery tại đây:&#x20;
* Ban sẽ được điều hướng đến trang đăng nhập tài khoản VNG Cloud. Xem hướng dẫn chi tiết [cách đăng nhập vào VNG Cloud](../../../identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md) với tài khoản IAM User và tài khoản Root User

## **2. Kích hoạt dịch vụ Snapshot**

Để sử dụng dịch vụ Server Disaster Recovery (SDR) hiệu quả, người dùng cần kích hoạt dịch vụ Snapshot tại các Region nơi đặt máy chủ chính và máy chủ dự phòng. Snapshot là một tính năng quan trọng cho phép tạo các bản sao lưu nhanh chóng của dữ liệu trên ổ đĩa, giúp đảm bảo khả năng phục hồi dữ liệu trong trường hợp xảy ra sự cố.

**Tự động kích hoạt:**

Nếu bạn chưa kích hoạt dịch vụ Snapshot, SDR sẽ tự động kích hoạt dịch vụ này cho bạn để đảm bảo bạn có thể sử dụng đầy đủ các tính năng của dịch vụ DR. Điều này giúp đơn giản hóa quá trình cài đặt và cấu hình, đồng thời đảm bảo tính liên tục và an toàn cho dữ liệu của bạn.

**Lưu ý:** Bạn có thể kiểm tra trạng thái kích hoạt của dịch vụ Snapshot trong phần quản lý dịch vụ Snapshot của giao diện vServer

## **3. Thêm Máy chủ (Attach Server):**

* Trong bảng điều khiển Server Recovery Center, nhấp vào nút **"Attach a Server"**.
* Chọn máy chủ chính (Main Server) mà bạn muốn bảo vệ từ danh sách các máy chủ khả dụng.
* Cấu hình thông tin cho máy chủ dự phòng (Shadow Server):
  * **Vùng (Region):** Chọn vùng địa lý nơi bạn muốn đặt máy chủ dự phòng. Tốt nhất nên chọn một vùng khác với vùng của máy chủ chính để tăng tính sẵn sàng trong trường hợp sự cố vùng.
  * **VPC (Virtual Private Cloud):** Chọn VPC mà bạn muốn máy chủ dự phòng thuộc về.
  * **Subnet:** Chọn subnet cụ thể trong VPC đã chọn để đặt máy chủ dự phòng.
* Nhấn nút "Attach" để hoàn tất quá trình thêm máy chủ.

## **4. Bắt đầu Sao chép (Start Replication):**

* Sau khi thêm máy chủ thành công, chọn máy chủ đó trong danh sách.
* Nhấn nút **"Start Replication"** để bắt đầu quá trình sao chép dữ liệu từ máy chủ chính sang máy chủ dự phòng.
* Cấu hình các thông số sao chép:
  * **Tên máy chủ dự phòng (Shadow Server Name):** Đặt một tên dễ nhận biết cho máy chủ dự phòng.
  * **Vùng (Region):** Nếu bạn muốn thay đổi vùng đặt máy chủ dự phòng, bạn có thể chọn lại tại đây.
  * **Khoảng thời gian (Interval):** Chọn tần suất sao chép dữ liệu. Bạn có thể chọn từ 1 giờ đến 12 giờ, tùy thuộc vào mức độ quan trọng và tần suất thay đổi dữ liệu của máy chủ chính.
  * **Cài đặt mạng (Network Settings):** Cấu hình VPC, Subnet và địa chỉ IP (tùy chọn) cho máy chủ dự phòng.
* Nhấn nút **"Start Replication"** để bắt đầu quá trình sao chép dữ liệu.

## **5. Giám sát và Quản lý:**

* Sau khi quá trình sao chép bắt đầu, bạn có thể giám sát trạng thái sao chép và các thông tin liên quan trên bảng điều khiển Server Disaster Recovery.
* Bạn cũng có thể thực hiện các thao tác khác như:
  * **Dừng sao chép (Stop Replication):** Tạm dừng quá trình sao chép dữ liệu.
  * **Khởi động lại sao chép (Restart Replication):** Bắt đầu lại quá trình sao chép từ đầu.
  * **Tiếp tục sao chép (Resume Replication):** Tiếp tục quá trình sao chép sau khi đã dừng.
  * **Kiểm tra chuyển đổi dự phòng (Test Failover):** Mô phỏng quá trình chuyển đổi sang máy chủ dự phòng để kiểm tra tính sẵn sàng của hệ thống.
  * **Chuyển đổi dự phòng (Failover):** Thực hiện chuyển đổi sang máy chủ dự phòng trong trường hợp máy chủ chính gặp sự cố.

## **6. Tận dụng các Tính năng Nâng cao:**

* **DR cross-region:** Nếu bạn muốn tăng cường khả năng chống chịu trước các sự cố quy mô lớn, hãy cân nhắc sử dụng tính năng DR cross-region để sao lưu và phục hồi dữ liệu giữa các vùng khác nhau.
* **Action DR theo kế hoạch:** Lên kế hoạch và tự động hóa các hành động DR để đảm bảo quy trình phục hồi diễn ra một cách nhanh chóng và chính xác khi cần thiết.
* **Thứ tự ưu tiên phục hồi:** Đảm bảo các hệ thống quan trọng nhất được khôi phục trước bằng cách tùy chỉnh thứ tự ưu tiên cho các máy chủ chính.

**Lưu ý:**

* Hãy đảm bảo bạn đã đọc và hiểu rõ các chính sách và điều khoản sử dụng dịch vụ Disaster Recovery của VNG Cloud.
* Trong quá trình sử dụng, nếu có bất kỳ thắc mắc hoặc cần hỗ trợ, bạn có thể liên hệ với đội ngũ hỗ trợ kỹ thuật của VNG Cloud.

Tham khảo thêm các hướng dẫn chi tiết về các tính năng của Server Disaster Recovery tại:

* [Quản lý (SDR)](quan-ly-sdr/)
* [Cách tính phí](cach-tinh-phi.md)
