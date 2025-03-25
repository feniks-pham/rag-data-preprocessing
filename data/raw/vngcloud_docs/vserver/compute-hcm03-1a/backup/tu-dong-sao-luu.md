# Tự động sao lưu

Tính năng tự động sao lưu là một phần quan trọng của dịch vụ backup, giúp người dùng dễ dàng bảo vệ dữ liệu của họ mà không cần thực hiện các bước thủ công phức tạp. Đối với tính năng này, sau khi bạn đã tạo bản backup trên server, hệ thống sẽ tự động kích hoạt chế độ tự động sao lưu. Sau đó sẽ tiếp tục tạo các bản sao lưu theo bộ lịch đã được đặt ra cho đến khi người dùng quyết định tắt tính năng này.

***

### **Bật Tính Năng Tự Động Sao Lưu** <a href="#tudongsaoluu-battinhnangtudongsaoluu" id="tudongsaoluu-battinhnangtudongsaoluu"></a>

Sau khi bạn đã tạo bản backup trên server, tính năng tự động sao lưu sẽ tự động được kích hoạt. Bạn có thể thực hiện điều này thông qua giao diện người dùng hoặc thông qua các lệnh hệ thống cụ thể.

#### **Thực Hiện Thông Qua Giao Diện Người Dùng:** <a href="#tudongsaoluu-thuchienthongquagiaodiennguoidung" id="tudongsaoluu-thuchienthongquagiaodiennguoidung"></a>

1. Truy cập vào trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview)
2. Tại thanh menu điều hướng, chọn Tab Backup/ Backup server
3. Chọn Backup server mà bạn muốn kích hoạt tính năng tự động sao lưu tại trang danh sách
4. Tìm và thực hiện chọn Bật "**Tự động sao lưu"**

#### **Thực Hiện Thông Qua Lệnh Hệ Thống:** <a href="#tudongsaoluu-thuchienthongqualenhhethong" id="tudongsaoluu-thuchienthongqualenhhethong"></a>

* Sử dụng các lệnh dòng lệnh hoặc API để kích hoạt tính năng tự động sao lưu cho bản backup cụ thể.

***

### **Tắt Tính Năng Tự Động Sao Lưu** <a href="#tudongsaoluu-tattinhnangtudongsaoluu" id="tudongsaoluu-tattinhnangtudongsaoluu"></a>

Người dùng có thể tắt tính năng tự động sao lưu bất cứ lúc nào nếu họ không muốn hệ thống tiếp tục tạo bản sao lưu tự động. Quyết định này có thể được thực hiện qua giao diện người dùng hoặc bằng cách sử dụng các lệnh hệ thống cụ thể.

**Thực Hiện Thông Qua Giao Diện Người Dùng:**

1. Truy cập vào trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview)
2. Tại thanh menu điều hướng, chọn Tab Backup/ Backup server
3. Chọn Backup server mà bạn muốn kích hoạt tính năng tự động sao lưu tại trang danh sách
4. Tìm và thực hiện chọn Tắt "**Tự động sao lưu"**

**Thực Hiện Thông Qua Lệnh Hệ Thống:**

* Sử dụng các lệnh dòng lệnh hoặc API để tắt tính năng tự động sao lưu cho bản backup cụ thể.

{% hint style="info" %}
**Lưu ý quan trọng**

Các bản sao lưu đã được tạo khi tính năng tự động sao lưu đang hoạt động sẽ không bị ảnh hưởng bởi quyết định tắt tính năng. Tuy nhiên, bản sao lưu mới sẽ không được tạo tự động theo bộ lịch nếu tính năng này đã được tắt.
{% endhint %}
