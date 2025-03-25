# Tối ưu hiệu suất tải lên các file có kích thước nhỏ

#### Vấn đề <a href="#toiuuhieusuattailencacfilecokichthuocnho-vande" id="toiuuhieusuattailencacfilecokichthuocnho-vande"></a>

Người dùng có nhu cầu tải lên các file có kích thước nhỏ (N bytes, N Kbytes, hoặc N Mbytes) với số lượng lớn (từ hàng ngàn tới hàng triệu file) dẫn tới tốc độ tải lên file khá chậm.

***

#### Giải pháp tối ưu hiệu suất <a href="#toiuuhieusuattailencacfilecokichthuocnho-giaiphaptoiuuhieusuat" id="toiuuhieusuattailencacfilecokichthuocnho-giaiphaptoiuuhieusuat"></a>

* Sử dụng trình nén file: Có nhiều trình nén file miễn phí mã nguồn mở có sẵn, chẳng hạn như gzip, bzip2 và 7-Zip. Các trình nén này có thể giảm đáng kể kích thước của các file nhỏ, từ đó giúp cải thiện tốc độ tải lên. Tuy nhiên, nếu thư mục chứa quá nhiều file thì quá trình nén file có thể mất một chút thời gian hay file nén có thể có kích thước lớn hơn các file riêng lẻ nếu thuật toán nén hoạt động không hiệu quả. Quan trọng nhất, người nhận file này cần giải nén nó trước khi họ có thể truy cập vào từng file, vì vậy việc sử dụng trình nén file sẽ hợp lý nhất khi bạn muốn sao lưu (backup) dữ liệu.
* Sử dụng công cụ tải lên nhiều luồng: Thay thế công cụ phía người dùng đang được sử dụng để tải lên file, có một số công cụ tải lên nhiều luồng có sẵn chẳng hạn như Rclone, Cyberduck, FileZilla. Các công cụ này có thể tải lên nhiều file cùng lúc, từ đó giúp cải thiện đáng kể tốc độ tải lên. Công cụ được chúng tôi khuyến khích sử dụng tại đây là Rclone với các tham số cấu hình tối ưu hiệu suất được chỉ định bên dưới:

> rclone --config=rclone.conf copy /local/path remote:path --transfers=8 --buffer-size=64M --size-only --fast-list
>
> \--transfers=8: Sử dụng 8 luồng (threads).\
> \--buffer-size=64M: Thiết lập kích thước buffer là 64MB\
> \--size-only: Chỉ đồng bộ kích thước của các file, nó sẽ chỉ so sánh kích thước chứ không phải giá trị băm.\
> \--fast-list: Bật chế độ ghi nhớ danh sách (memory cache) -> nó chỉ liệt kê 1 lần từ directory gốc -> cải thiện hiệu suất khi upload các folder có nhiều file

* Tối ưu hóa cài đặt mạng của bạn: Nếu bạn đang tải lên file qua mạng Wi-Fi, hãy đảm bảo rằng router của bạn được định cấu hình để có hiệu suất tối ưu. Bạn cũng có thể thử thay đổi kênh mà router của bạn đang sử dụng để tránh nhiễu từ các thiết bị khác.
* Nâng cấp kết nối internet của bạn. Nếu bạn có kết nối internet chậm, việc nâng cấp lên gói nhanh hơn có thể cải thiện đáng kể tốc độ tải lên của các file nhỏ.

Ngoài ra, còn một số mẹo bên dưới cũng có thể bổ sung để cải thiện tốc độ tải lên của các file nhỏ:

* Tải lên file vào giờ không cao điểm: Nếu bạn đang tải lên file vào giờ cao điểm, khi nhiều người khác cũng đang sử dụng internet, bạn có thể sẽ gặp phải tốc độ chậm hơn.
* Tránh tải lên file lên các máy chủ cách xa bạn: Khoảng cách giữa máy tính của bạn và máy chủ sẽ ảnh hưởng đến tốc độ tải lên. Nếu có thể, hãy tải lên file lên các máy chủ gần bạn.
* Kiểm tra tốc độ tải lên của bạn: Có một số trang web cho phép bạn kiểm tra tốc độ tải lên của mình. Điều này có thể giúp bạn xác định bất kỳ nút thắt cổ chai nào trong mạng của bạn và thực hiện các điều chỉnh cần thiết.

Bằng cách làm theo các mẹo này, bạn có thể cải thiện đáng kể tốc độ tải lên của các file nhỏ. Điều này có thể giúp bạn tiết kiệm thời gian và công sức khi tải lên lượng lớn dữ liệu.
