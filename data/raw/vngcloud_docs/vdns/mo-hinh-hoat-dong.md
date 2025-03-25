# Mô hình hoạt động

Hiểu cách thức hoạt động của DNS với từng loại bản ghi (record type) và chính sách định tuyến (routing policy) là rất quan trọng để tối ưu hiệu suất và độ tin cậy của ứng dụng web. Dưới đây là giải thích chi tiết:

## Cách thức hoạt động của DNS với từng loại bản ghi

Khi một người dùng nhập một tên miền (ví dụ: `www.example.com`) vào trình duyệt, quá trình phân giải DNS sẽ diễn ra như sau:

1. **Yêu cầu đệ quy:** Máy tính của người dùng gửi một yêu cầu phân giải tên miền đến máy chủ DNS đệ quy (recursive DNS server) được cấu hình trên máy tính hoặc router.
2. **Truy vấn lặp:** Máy chủ DNS đệ quy bắt đầu một loạt các truy vấn lặp đến các máy chủ DNS khác nhau để tìm địa chỉ IP liên quan đến tên miền. Quá trình này thường bắt đầu từ máy chủ gốc (root server), sau đó đến máy chủ tên miền cấp cao nhất (TLD server) cho `.com`, rồi đến máy chủ tên miền có thẩm quyền (authoritative name server) cho `example.com`.
3. **Trả lời có thẩm quyền:** Máy chủ tên miền có thẩm quyền chứa các bản ghi DNS cho tên miền `example.com`. Nó sẽ trả về bản ghi phù hợp với yêu cầu.

Dưới đây là cách các loại bản ghi khác nhau ảnh hưởng đến quá trình này:

*   **A Record:** Bản ghi A liên kết một tên miền với một địa chỉ IPv4. Ví dụ:

    ```
    www.example.com.    A     192.0.2.1
    ```

    Khi máy chủ DNS nhận được yêu cầu cho `www.example.com`, nó sẽ trả về địa chỉ IP `192.0.2.1`.
*   **CNAME Record:** Bản ghi CNAME tạo một bí danh (alias) cho một tên miền khác. Ví dụ:

    ```
    blog.example.com.   CNAME www.example.com.
    ```

    Khi máy chủ DNS nhận được yêu cầu cho `blog.example.com`, nó sẽ thấy bản ghi CNAME và tiếp tục truy vấn cho `www.example.com`, sau đó trả về địa chỉ IP được liên kết với `www.example.com`.
*   **MX Record:** Bản ghi MX chỉ định máy chủ thư điện tử (mail server) chịu trách nhiệm nhận email cho một tên miền. Ví dụ:

    ```
    example.com.        MX    10 mail.example.com.
    ```

    Số `10` là giá trị ưu tiên (priority). Số càng nhỏ, ưu tiên càng cao. Khi một máy chủ gửi email muốn gửi email đến `user@example.com`, nó sẽ truy vấn bản ghi MX và kết nối đến máy chủ thư điện tử có ưu tiên cao nhất.
*   **SRV Record:** Bản ghi SRV xác định vị trí của các dịch vụ cụ thể. Ví dụ:

    ```
    _sip._tcp.example.com. SRV 10 0 5060 sipserver.example.com.
    ```

    Bản ghi này chỉ định rằng dịch vụ SIP trên giao thức TCP được cung cấp bởi máy chủ `sipserver.example.com` trên cổng `5060`.
*   **PTR Record:** Bản ghi PTR thực hiện phân giải ngược (reverse DNS lookup), từ địa chỉ IP trở lại tên miền. Ví dụ:

    ```
    1.0.2.192.in-addr.arpa. PTR www.example.com.
    ```

    Khi máy chủ DNS nhận được yêu cầu cho địa chỉ IP `192.0.2.1`, nó sẽ trả về tên miền `www.example.com`.
*   **TXT Record:** Bản ghi TXT chứa văn bản tùy ý. Nó thường được sử dụng cho các mục đích như xác thực email (SPF, DKIM, DMARC) hoặc xác minh quyền sở hữu tên miền.

    ```
    example.com.        TXT   "v=spf1 mx -all"
    ```

## **Cách thức hoạt động của DNS với từng chính sách định tuyến (Routing Policy)**

Chính sách định tuyến quyết định cách máy chủ DNS chọn bản ghi nào để trả về trong số nhiều bản ghi có sẵn cho cùng một tên miền.

* **Simple Routing:** Đây là chính sách đơn giản nhất. Máy chủ DNS trả về các bản ghi theo thứ tự được liệt kê. Thường được sử dụng khi chỉ có một máy chủ hoặc khi không cần các tính năng định tuyến phức tạp.
* **Geolocation Routing:** Chính sách này cho phép định tuyến lưu lượng truy cập dựa trên vị trí địa lý của người dùng. Ví dụ: người dùng ở miền Bắc có thể được định tuyến đến máy chủ ở Hà Nội, trong khi người dùng ở miền Nam được định tuyến đến máy chủ ở Hồ Chí Minh. Điều này giúp giảm độ trễ và cải thiện hiệu suất.
* **Weighted Routing (có Sticky Session):** Chính sách này cho phép phân phối lưu lượng truy cập dựa trên trọng số được gán cho từng tài nguyên (ví dụ: máy chủ). Ví dụ: bạn có thể gán trọng số 70 cho máy chủ A và 30 cho máy chủ B, nghĩa là 70% lưu lượng truy cập sẽ được định tuyến đến máy chủ A và 30% đến máy chủ B. Tính năng _Sticky Session_ (phiên dính) đảm bảo rằng một người dùng cụ thể sẽ luôn được định tuyến đến cùng một máy chủ trong suốt phiên làm việc của họ. Điều này rất hữu ích cho các ứng dụng yêu cầu duy trì trạng thái phiên (ví dụ: giỏ hàng trực tuyến).
