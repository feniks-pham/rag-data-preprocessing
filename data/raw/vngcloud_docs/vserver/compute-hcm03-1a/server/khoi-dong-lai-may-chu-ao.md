# Khởi động lại máy chủ ảo

Khởi động lại máy chủ ảo tương đương với việc khởi động lại hệ điều hành. Trong hầu hết các trường hợp, chỉ mất vài phút để khởi động lại máy chủ ảo của bạn.

Khi bạn khởi động lại Server, nó sẽ giữ nguyên như sau:

* Tên DNS công khai (IPv4)
* Địa chỉ IPv4 riêng
* Địa chỉ IPv4 công khai
* Địa chỉ IPv6 (nếu có)

Và bất kỳ dữ liệu nào trên khối lượng lưu trữ của nó.

Khởi động lại Server không bắt đầu thời hạn thanh toán phiên bản mới (với mức phí tối thiểu là một phút), không giống như việc dừng và bắt đầu Server của bạn.

Chúng tôi có thể lên lịch khởi động lại phiên bản của bạn để bảo trì cần thiết, chẳng hạn như để áp dụng các bản cập nhật yêu cầu khởi động lại. Bạn không cần thực hiện hành động nào; chúng tôi khuyên bạn nên đợi quá trình khởi động lại diễn ra trong cửa sổ đã lên lịch.&#x20;

Chúng tôi khuyên bạn nên sử dụng bảng điều khiển vServer Portal công cụ dòng lệnh hoặc API để khởi động lại phiên bản của bạn. Nếu bạn sử dụng bảng điều khiển vServer, công cụ dòng lệnh hoặc API để khởi động lại Server của mình, chúng tôi sẽ thực hiện khởi động lại cứng nếu phiên bản không tắt hoàn toàn trong vòng vài phút.

\


***

**Để khởi động lại một Server bằng bảng điều khiển:**

1. Mở bảng điều khiển vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/)
2. Trong ngăn điều hướng, chọn Tab Server.
3. Chỉ định Server và chọn **Hành động,** trong danh sách mở ra chọn **Khởi động lại.**
4. Chọn **Khởi động lại** khi được nhắc xác nhận.\
   Sau đó Server vẫn ở trạng thái _**Rebooting**_.
