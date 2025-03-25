# Tình huống sử dụng (use case)

## Tổng quan

Các trường hợp Sao lưu dữ liệu sử dụng với Veeam thường được sử dụng với các trường hợp nhua sau:

* Sao lưu dữ liệu;
* Khôi phục dữ liệu đã mất;
* Bảo vệ chống Ransomware;
* Quản lý nhiều Repository sao lưu.

***

## Sao lưu dữ liệu&#x20;

Giả sử Doanh nghiệp ABC một số tệp tin và thư mục quan trọng về tài chính trên máy chủ của hệ thống công ty. Do đó, họ cần sao lưu bảo vệ những tài liệu nhạy cảm này đến một nơi lưu trữ an toàn khác như trên vStorage (hoặc trên hệ thống Ceph hay AWS) ngoài máy chủ đang có.

Sử dụng Veeam để sao lưu dữ liệu:

* Thiết lập kho lưu trữ (repository) trên Veeam;
* Thiết lập job định kỳ sao lưu các dữ liệu đó;
* Có thể kiểm tra phiên bản lần cập nhật gần nhất trên Veeam.

## Khôi phục dữ liệu đã mất

Giả sử Doanh nghiệp ABC đã sử dụng Veeam để sao lưu định kỳ các dữ liệu quan trọng. Nhưng đến một hôm hệ thống máy chủ bị sự cố nghiêm trọng và mất một số dữ liệu đã lưu trên máy chủ.

Sử dụng Veeam để khôi phục dữ liệu đã mất:

* Chọn job đã thực hiện backup các dữ liệu đến các nơi lưu trữ;
* Trong danh sách các thời điểm backup của Job thì chọn thời điểm phù hợp cần phục hồi dữ liệu (thường là thời điểm cuối cùng mà job đã chạy);

## Bảo vệ chống Ransomware

Giả sử Doanh nghiệp ABC có những tài liệu lưu trữ quan trọng cần lưu trữ, cũng như doanh nghiệp ý thức được sự nguy cơ gây phá hoại dữ liệu của Ransomware. Doanh nghiệp thật sự muốn dữ liệu được sao lưu và có biện pháp đảm bảo dữ liệu được an toàn khỏi những tác nhân nguy hiểm như Ransomware.&#x20;

Sử dụng Veeam phối hợp với Storage có hỗ trợ tính năng Object Lock:

* Storage cần tạo Bucket/Container có hỗ trợ Object Lock;
* Khi tạo Repository, chọn tùy chọn "Make recent backups immutable for (30) days" để kích hoạt Immutable để chống Ransomware;
* Tính năng Immutable bảo vệ các bạn sao lưu khỏi bị xóa hoặc thay đổi trong khoảng thời gian nhất định.

## Quản lý nhiều Repository sao lưu &#x20;

Giả sử Doanh nghiệp ABC đã sử dụng Veeam để sao lưu dữ liệu, nhưng hiện doanh nghiệp này có nhiều repository sao lưu phân tán trên nhiều nơi lưu trữ khác nhau, và đng gặp khó khăn trong việc quản lý và tối ưu hóa không gian lưu trữ.

Sử dụng Veeam với tính năng Scale-out Backup  Repository (SOBR):

* Thiết lập các Repository riêng lẻ ở các nơi như bình thường;
* Tạo một Scale-out Repositories, thêm các Repository riêng lẻ vào SOBR;
* Doanh nghiệp tạo job với SOBR và chỉ quản lý trên 1 Repository duy nhất là SOBR;
* Nếu một repository gặp sự cố, dữ liệu có thể được truy cập từ các repository khác trong SOBR.&#x20;
