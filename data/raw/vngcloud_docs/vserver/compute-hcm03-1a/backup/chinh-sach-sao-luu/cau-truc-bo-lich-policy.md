# Cấu trúc bộ lịch Policy

### **Cấu trúc lập lịch phối hợp 3 loại Daily/ Weekly/ Monthly** <a href="#cautrucbolichpolicy-cautruclaplichphoihop3loaidaily-weekly-monthly" id="cautrucbolichpolicy-cautruclaplichphoihop3loaidaily-weekly-monthly"></a>

Khi đối tượng backup là máy ảo và ổ đĩa thì việc triển khai bộ lịch cân nhắc đến Policy phối cả 3 Daily+Weekly+Monthly để đảm bảo được use-case quản lý vòng đời sao lưu của đối tượng máy ảo từ ngắn hạn đến dài hạn.

Điều này được hiện thực hoá dựa trên việc một máy ảo sẽ có một bộ lịch map 1:1 với bộ lịch thực tế hiện thực hóa, trong đó mỗi một ngày dưới quy ước phối Policy sẽ đánh dấu thuộc tính cơ sở của backup ngày hôm đó cần phải thực hiện

Ví dụ: bảng bên dưới là mô tả của một bộ lịch với use-case quy tắc sau:

**Daily backup:** các ngày trong tuần (daily là ngày nào cũng phải backup cơ bản không có lựa chọn nào đặc biệt bổ sung thêm với phương án là backup diff)

**Weekly backup:** thực thi vào ngày chủ nhật hàng tuần do nghiệp vụ khách hàng slowdown vào cuối tuần với phương án là backup full

**Monthly backup:** thực thi vào ngày thứ bảy của tuần cuối cùng của một tháng bất kỳ với phương án là backup full

<figure><img src="https://docs.vngcloud.vn/download/attachments/49649826/image2023-3-15_17-59-20.png?version=1&#x26;modificationDate=1678877960000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Mục tiêu của việc thực thi hoá:**

Đảm bảo đơn giản hoá quy tắc backup theo đối tượng máy ảo trong cùng một giao diện tương tác về quy luật sao lưu

Tiết giản rủi ro liên qua trùng lắp các tác vụ sao lưu của cùng một Volume cùng với giảm thiểu trùng lắp dữ liệu sao lưu cùng một ngày
