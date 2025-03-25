# Start Replication

Để bắt đầu quá trình replication, bạn cần thêm máy chủ chính cần replicate vào SDR. Xem hướng dẫn thêm máy chủ chính vào SDR [tại đây](them-may-chu-attach-a-server.md).

Sau khi thêm máy chủ thành công, làm theo hướng dẫn dưới đây để bắt đầu quá trình replicate dữ liệu.

## Start Replication

1. Chọn máy chủ chính vừa thêm trước đó từ danh sách tại đây:
2. Nhấn nút **"Start Replication"** để bắt đầu cấu hình thông số máy chủ dự phòng, một cửa sổ giao diện sẽ hiển thị cho phép bạn cấu hình các thông tin sau:
   1. **Thông tin cơ bản (Basic Information)**
      * **Tên máy chủ dự phòng (Shadow Server Name):** Đặt một tên dễ nhận biết cho máy chủ dự phòng.
      * **Vùng (Region):** Nếu bạn muốn thay đổi vùng đặt máy chủ dự phòng, bạn có thể chọn lại tại đây.
      * **Khoảng thời gian (Interval):** Chọn tần suất sao chép dữ liệu. Bạn có thể chọn từ 1 giờ đến 12 giờ, tùy thuộc vào mức độ quan trọng và tần suất thay đổi dữ liệu của máy chủ chính.
   2. **Cài đặt mạng (Network Settings)**
      * Cấu hình **VPC**, **Subnet** và chỉ định địa chỉ **IP private và Floating IP** (tùy chọn) cho máy chủ dự phòng.
      * Chọn cấu hình **Security Group** cho máy chủ dự phòng: Security group này phải thuộc danh sách group của máy chủ server ở Vùng (Region) đã chọn ở mục Basic Information.
   3. **Cấu hình ổ đĩa (Volume Setting)**
      * **Mặc định:** Hệ thống sẽ tự động tải lên số lượng ổ đĩa (volume) giống hệt về cấu hình loại ổ đĩa (SSD/NVMe), IOPS (Input/Output Operations Per Second) và dung lượng so với máy chủ chính. Điều này giúp đảm bảo rằng máy chủ dự phòng có khả năng xử lý dữ liệu tương đương với máy chủ chính.
      * **Tùy chỉnh:** Bạn được phép thay đổi loại ổ đĩa (type) và IOPS cho phù hợp với nhu cầu của mình. Ví dụ, nếu bạn cần hiệu suất cao hơn cho máy chủ dự phòng, bạn có thể chọn loại ổ đĩa NVMe hoặc tăng IOPS.
        * **Shadow Server volume type:** Chọn loại ổ đĩa cho máy chủ dự phòng (SSD hoặc NVMe).
        * **Shadow Server IOPS:** Chọn mức IOPS cho máy chủ dự phòng. IOPS càng cao, hiệu suất đọc/ghi của ổ đĩa càng nhanh.
        * **Lưu ý:** Nếu vùng (Region) đặt máy chủ dự phòng không hỗ trợ cấu hình loại ổ đĩa và IOPS giống với vùng đặt máy chủ chính, hệ thống sẽ tự động điều chỉnh và tải lên thông tin mặc định của vùng đó. Điều này đảm bảo rằng bạn vẫn có thể tạo máy chủ dự phòng, mặc dù có thể có sự khác biệt về hiệu suất so với máy chủ chính.
   4. **Cấu hình Instance Type:** Bạn cần chọn một flavor (loại máy chủ) phù hợp với nhu cầu sử dụng của máy chủ dự phòng. Điều này bao gồm việc xem xét các yếu tố như số lượng CPU, dung lượng RAM, và khả năng lưu trữ. Bạn hoàn toàn có thể **thay đổi flavor** của máy chủ dự phòng sau khi đã khởi tạo thành công. Điều này cho phép bạn linh hoạt điều chỉnh cấu hình máy chủ để đáp ứng tốt hơn nhu cầu sử dụng thực tế, hoặc tối ưu hóa chi phí.
   5. **Cấu hình khác (Other Setting)**:&#x20;
      * Bạn có thể tùy chọn cấu hình một placement group cho máy chủ dự phòng. Placement group là một tính năng cho phép bạn nhóm các máy chủ lại với nhau để đảm bảo chúng được đặt trên cùng một hạ tầng vật lý, giúp giảm thiểu độ trễ mạng và tăng hiệu suất truyền dữ liệu giữa các máy chủ.
      * **Lưu ý:** Nhóm này phải thuộc cùng vùng (region) với vùng đặt máy chủ dự phòng. Điều này đảm bảo rằng các máy chủ trong placement group được đặt gần nhau về mặt vật lý, giúp tối ưu hóa hiệu suất truyền dữ liệu.
3. Nhấn nút **"Start Replication"** để bắt đầu quá trình sao chép dữ liệu.

**Lưu ý khi tạo máy chủ dự phòng**

* **Trạng thái mặc định:** Máy chủ dự phòng được tạo ra mặc định ở trạng thái **tắt (shutdown)**. Điều này nhằm mục đích phục vụ cho quá trình sao chép dữ liệu và giúp bạn tiết kiệm chi phí. Trong trạng thái tắt, bạn sẽ **không bị tính phí** sử dụng máy chủ dự phòng.
* **Tính phí khi khởi động:** Tuy nhiên, nếu bạn **khởi động (start)** máy chủ dự phòng, bạn sẽ bắt đầu bị tính phí sử dụng máy chủ theo cấu hình đã chọn.
* **Ảnh hưởng đến sao chép:** Lưu ý rằng khi bạn khởi động máy chủ dự phòng, quá trình sao chép dữ liệu trên máy chủ đó sẽ bị **lỗi**. Điều này là do máy chủ dự phòng cần ở trạng thái tắt để hệ thống có thể thực hiện sao chép một cách an toàn và hiệu quả.

## Full Replication

Sau khi nhấn "**Start Replication**" hệ thống sẽ tiến hành các quy trình như sau:

1. **Khởi tạo máy chủ dự phòng:** Hệ thống sẽ tiến hành khởi tạo máy chủ dự phòng dựa trên cấu hình bạn đã chọn để bắt đầu quá trình replication
2. **Bắt đầu Full Replication:** Hệ thống sẽ bắt đầu quá trình sao chép toàn bộ dữ liệu (Full Replication) từ máy chủ chính sang máy chủ dự phòng.
3. **Chi phí:** Trong quá trình này, bạn sẽ bắt đầu phải trả chi phí cho:
   * **Máy chủ dự phòng:** Bao gồm chi phí cho máy chủ (server) và các ổ đĩa (volume) gắn liền với nó.
   * **Lưu trữ snapshot:** Chi phí lưu trữ các bản sao snapshot (ảnh chụp nhanh) của dữ liệu để phục vụ quá trình sao chép.
   * Tham khảo thêm cách tính phí [tại đây](../cach-tinh-phi.md)
4. **Trạng thái sao chép (Pairing Status):**
   * **Replicating:** Nếu quá trình sao chép dữ liệu thành công, trạng thái ghép cặp (pairing status) sẽ chuyển sang "Replicating". Lúc này, bạn có thể vào xem điểm khôi phục (recovery point) vừa được tạo ra.
   * **Error:** Nếu trạng thái là "Error", có nghĩa là quá trình "Start Replication" chưa được bắt đầu hoặc đã gặp lỗi. Bạn có thể:
     * **Xem chi tiết lỗi:** Truy cập vào thông tin chi tiết của máy chủ để xem lỗi cụ thể là gì. Từ đó, bạn có thể thử tự mình giải quyết vấn đề dựa trên thông tin lỗi.
     * **Liên hệ hỗ trợ:** Nếu không thể tự giải quyết, hãy liên hệ với đội ngũ hỗ trợ của chúng tôi để được giúp đỡ theo các kênh sau:
       * Email [**support@vngcloud.vn**](mailto:support@vngcloud.vn) or hotline **19001549 – Ext 3.**
       * Open ticket: [https://vngcloud.vn/en/web/guest/contact](https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fu12870758.ct.sendgrid.net%2Fls%2Fclick%3Fupn%3D6Th82stgZiRII4JWBZ2k-2F8jp0RwIXS6fxA7KQMXjUq8DSCsrmL59yXstoJFgaU1dGY-2FSWg-2FK9UdGxb9Lh9dNFA-3D-3DpvNZ\_Ym-2Fxt4z9Amb7foJoUGq7k-2FFaxzUNhQVDcUTybZdrS2NXAbbCaEQkSCrQOhYjTHUSbv6080NfkWdCEMWKJJF2zpfOBUaPuOIa3OzTC0yp1D9JlA3uof8O-2BtBLR8V2gs8RQIrzb7xDzuI-2FW-2BVnmHahaTWks-2FX1rqpdHNVHwVyZ6vhj-2BZLRAIyEc2XrBxbfG0QrF7-2FsBJLgoViI1e7tTyjc8Q-3D-3D\&data=05%7C01%7Ctult4%40vng.com.vn%7C7e33555fd46c4091057908db827ef130%7C7c112a6e10e24e09afc42e37bc60d821%7C0%7C0%7C638247253964298461%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C\&sdata=VmVhSabKwqQW2lPslozGS3cQzp0jF4ShJuofnhGp%2Fzs%3D\&reserved=0)

**Lưu ý quan trọng:**

* **Chi phí:** Hãy đảm bảo bạn đã hiểu rõ về các chi phí liên quan đến việc sử dụng máy chủ dự phòng và lưu trữ snapshot trước khi bắt đầu quá trình sao chép.
* **Giám sát trạng thái:** Thường xuyên kiểm tra trạng thái sao chép để đảm bảo quá trình diễn ra suôn sẻ. Nếu gặp lỗi, hãy xử lý kịp thời để tránh ảnh hưởng đến khả năng phục hồi của hệ thống.
