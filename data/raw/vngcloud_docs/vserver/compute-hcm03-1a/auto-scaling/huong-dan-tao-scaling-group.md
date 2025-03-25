# Hướng dẫn tạo Scaling group

Tại giao diện Scaling Group Management chọn group configure &#x20;

Tại scaling group configuration, nhập các thông tin cần thiết &#x20;

* Group name (Bắt buộc): Đặt tên giúp bạn gợi nhớ và quản lý khi có nhiều group. Tên group cho phép đặt các ký tự (a-z, A-Z, 0-9, '\_'), bắt đầu với chữ và giới hạn từ 6-20 ký tự &#x20;
* Profile (Bắt buộc): Mỗi scaling group bắt buộc phải được gắn với 1 profile. Click drop down list để xem danh sách các profile đã tạo và chọn 1 profile mong muốn. Nếu như không có option nào thì bạn cần quay lại giao diện profile management và tạo 1 profile trước. &#x20;
* Desire Capacity: Nhập số lượng instance bạn mong muốn, scaling group sẽ scale số instance lên tương ứng. Số desire không được nhỏ hơn Min Capacity hoặc lớn hơn Max. &#x20;
* Min capacity: Số lượng instance nhỏ nhất mà bạn mong muốn group này có&#x20;
* Max capacity: Số lượng instance tối đa. Khi sử dụng receiver để scale tự động thì chỉ số Min / Max sẽ đảm bảo instance không vượt ra khỏi con số bạn mong muốn. &#x20;
* Timeout: Đơn vị là giây (s), nếu thời gian tạo group vượt quá Timeout, group này sẽ bị lỗi, bình thường bạn không cần điều chỉnh thông số này. &#x20;

Nếu bạn đã có policy tạo sẵn và muốn gắn vào , có thể nhấn Advance và chọn trong danh sách policy. Bạn có thể bỏ qua phần này và bổ sung sau. &#x20;

Lưu ý: nếu bạn đã tạo policy mà không thấy trong danh sách Policy, thì có thể xem lại và thay đổi lựa chọn phần Type policy. Danh sách policy chỉ hiển thị những policy phù hợp với type policy đã chọn&#x20;

Nhấn next để đến giao diện Summary, tại đây hãy kiểm tra lại các thông tin bạn đã nhập lại một lần nữa. Lưu ý bạn không thể thay đổi profile & group name sau khi tạo group thành công &#x20;

Chọn configure group để tạo, sau khi tạo thành công bạn sẽ thấy group xuất hiện ở giao diện quản lý Auto-scaling group với Status là CREATING. &#x20;

Sau một khoảng thời gian, bạn sẽ thấy group có Status là ACTIVE (nhấn Refresh trong Action hoặc F5)&#x20;

Nếu muốn xem thông tin chi tiết của Group,  nhấp vào ô vuông tickbox ngay tại màn hình Scaling Group Management để xem&#x20;
