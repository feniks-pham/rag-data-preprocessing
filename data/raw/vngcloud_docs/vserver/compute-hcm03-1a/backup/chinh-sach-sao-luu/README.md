# Chính sách sao lưu

vBackup cho phép bạn tạo các kế hoạch sao lưu xác định cách sao lưu các tài nguyên máy ảo và ổ đĩa của bạn. Các quy tắc trong kế hoạch bao gồm nhiều cài đặt khác nhau, chẳng hạn như tần suất sao lưu, khung thời gian diễn ra sao lưu, số bản lưu . Sau đó, bạn có thể áp dụng các chính sách này cho các nhóm tài nguyên bạn muốn bảo vệ.

Các chính sách sao lưu trong dịch vụ vBackup sẽ bao gồm chính sách được tạo mặc định bởi hệ thống và các chính sách được tạo sau đó bởi người dùng. Sau khi tạo chính sách, bạn có thể đính kèm chính sách sao lưu vào bản Backup của mình. Bạn có thể áp dụng các quy tắc kế thừa để kết hợp các chính sách lại với nhau, khung thời gian lồng ghép thích hợp, số bản lưu hợp lý. Điều này dẫn đến một chính sách sao lưu hiệu quả cho từng công việc sao lưu khác nhau. Có một chính sách hiệu quả sẽ hướng dẫn vBackup cách tự động sao lưu tài nguyên của bạn một cách tốt nhất cho tổ chức của mình.

Chính sách sao lưu cung cấp cho bạn quyền kiểm soát chi tiết đối với việc sao lưu tài nguyên của mình ở bất kỳ cấp độ nào mà bạn yêu cầu. Ví dụ: bạn có thể chỉ định trong một chính sách đính kèm với các tài nguyên quan trọng để đảm bảo tất cả phải được sao lưu đồng thời và nhất quán. Chính sách đó có thể bao gồm theo cấu hình sao lưu mặc định. Sau đó, bạn có thể chỉnh sửa lại chính sách sao lưu phù hợp với nhu cầu sử dụng. Ví dụ: Tổ chức nhân sự có thể chỉ định tần suất sao lưu là một lần mỗi tuần, trong khi Đơn vị tổ chức sản xuất chỉ định một lần mỗi ngày, lúc này bạn cần chọn bộ lịch lồng ghép 2 khung giờ sao lưu như trên, tham khảo thêm [Cấu trúc bộ lịch Policy](cau-truc-bo-lich-policy.md).

{% hint style="info" %}
**Quan trọng**

Hãy nhớ rằng mặc dù chiến lược chính sách một phần như được mô tả trước đó có thể hoạt động, nhưng nếu một chính sách hiệu quả cho tài khoản không đầy đủ, nó sẽ dẫn đến lỗi hoặc tài nguyên không được sao lưu thành công. Vì thế, hãy cân nhắc việc yêu cầu tất cả các chính sách sao lưu phải hoàn chỉnh và hợp lệ.
{% endhint %}

***

### **Bắt đầu với chính sách sao lưu** <a href="#chinhsachsaoluu-batdauvoichinhsachsaoluu" id="chinhsachsaoluu-batdauvoichinhsachsaoluu"></a>

**Làm theo các bước sau để bắt đầu sử dụng các chính sách sao lưu:**

1. Tìm hiểu về việc mà bạn phải có để thực hiện các tác vụ chính sách sao lưu.
2. Tìm hiểu về một số phương pháp hay nhất mà chúng tôi đề xuất khi sử dụng các chính sách sao lưu.
3. Kích hoạt các chính sách sao lưu cho bản sao lưu của bạn.
4. Tạo một chính sách sao lưu.
5. Đính kèm chính sách sao lưu vào bản sao lưu.
6. Xem chính sách sao lưu hiệu quả và có sự điều chỉnh phù hợp.
