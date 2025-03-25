# Hạn chế

Khi phân quyền sử dụng **IAM** trên **vStorage**, có một số hạn chế sau:

1. **Không hỗ trợ Object Lock Mode Governance:** chế độ này tạm thời không được hỗ trợ trên hệ thống vStorage, do đó bạn có thể sử dụng thay thế các chế độ **Compliance** hoặc **Legal Hold** để đảm bảo tính năng bảo vệ dữ liệu.
2. **Hạn chế phân quyền cho IAM User:**\
   Một số tính năng không thể tùy chỉnh quyền hạn cho IAM User và sẽ mặc định có **full quyền như Root User**, bao gồm:
   * **Bucket Versioning:** IAM User có thể tự do enable/ disable versioning mà không cần phân quyền.
   * **Bucket CORS:** IAM User có thể thiết lập hoặc chỉnh sửa, xóa cấu hình CORS mà không bị hạn chế.
   * **Object Lock:** IAM User có thể bật/tắt chế độ locked object hoặc thay đổi **retention day** mà không bị kiểm soát.

Những hạn chế này có thể gây ảnh hưởng đến khả năng kiểm soát chặt chẽ quyền hạn khi làm việc với các tính năng trên. Chúng tôi khuyến nghị bạn cân nhắc khi cấp quyền IAM User trong các trường hợp sử dụng liên quan đến dữ liệu quan trọng.
