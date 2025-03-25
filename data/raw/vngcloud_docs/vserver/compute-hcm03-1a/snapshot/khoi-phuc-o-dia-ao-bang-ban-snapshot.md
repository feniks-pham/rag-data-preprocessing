# Khôi phục ổ đĩa ảo bằng bản Snapshot

Bạn có thể khôi phục ổ đĩa ảo hoặc máy chủ ảo bằng các bản Snapshot đã tạo, nội dung bên dưới mô tả cách khôi phục ổ đĩa ảo bằng các bản Snapshot.

Sử dụng bản Snapshot cho phép bạn khôi phục dữ liệu và hệ thống nhanh chóng sau khi xảy ra sự cố. Điều này giúp giảm thời gian chịu ảnh hưởng của hệ thống. Đồng thời Khôi phục Snapshot là cách an toàn để sao lưu dữ liệu quan trọng của bạn. Nó đảm bảo rằng bạn có thể khôi phục dữ liệu và ổ đĩa trong trường hợp cần thiết, như lỗi phần cứng, lỗi phần mềm hoặc xóa dữ liệu một cách không cẩn thận. So với việc tái cấu hình và khôi phục hệ thống từ đầu, việc sử dụng Snapshot tiết kiệm thời gian và công sức đáng kể.

***

### **Rủi ro:** <a href="#khoiphucodiaaobangbansnapshot-ruiro" id="khoiphucodiaaobangbansnapshot-ruiro"></a>

* **Dữ liệu lỗi:** Nếu bạn sử dụng một Snapshot đã lỗi hoặc chứa dữ liệu bị hỏng, việc khôi phục có thể đưa ra dữ liệu không đúng hoặc dữ liệu bị hỏng. Điều này đặc biệt quan trọng nếu bạn không kiểm tra Snapshot trước khi sử dụng nó.
* **Thời gian tạo Snapshot:** Nếu bạn tạo Snapshot không đều đặn hoặc không đủ thường xuyên, bạn có thể mất dữ liệu quan trọng nếu sự cố xảy ra giữa các lần tạo Snapshot. Thời gian cách biệt giữa các Snapshot cũng ảnh hưởng đến khả năng khôi phục dữ liệu.
* **Chi phí lưu trữ:** Việc duy trì nhiều Snapshot có thể tạo ra chi phí lưu trữ đáng kể. Bạn cần xem xét cân nhắc giữa lợi ích của việc lưu trữ nhiều Snapshot và chi phí tương ứng.
* **Sự cẩn thận trong quản lý Snapshot:** Quản lý các bản Snapshot đòi hỏi sự cẩn thận để đảm bảo rằng bạn không xóa nhầm các bản sao lưu quan trọng hoặc duy trì quá nhiều bản sao lưu không cần thiết.

Việc sử dụng bản Snapshot để khôi phục ổ đĩa ảo có nhiều lợi ích quan trọng, nhưng cũng đi kèm với những rủi ro cần phải cân nhắc và quản lý một cách cẩn thận. Điều quan trọng là phải thực hiện các biện pháp bảo mật và kiểm tra tính toàn vẹn của Snapshot trước khi thực hiện việc khôi phục dữ liệu.

***

Ghi chú

Bạn chỉ có thể khôi phục ổ đĩa ảo với bản Snapshot của Data Volume.

### **Khôi phục ổ đĩa ảo bằng Snapshot trên bảng điều khiển** <a href="#khoiphucodiaaobangbansnapshot-khoiphucodiaaobangsnapshottrenbangdieukhien" id="khoiphucodiaaobangbansnapshot-khoiphucodiaaobangsnapshottrenbangdieukhien"></a>

1. Mở bảng điều khiển vServer tại [https://hcm-3.console.vngcloud.vn/vserver/](https://hcm-3.console.vngcloud.vn/vserver/).
2. Trong ngăn điều hướng, chọn **Snapshot**.
3. Chọn Snapshot của bản Data Volume tại trang danh sách rồi chọn **Hành động**, nhấn Rollback Volum&#x65;**.**
