# Sử dụng công cụ Rclone

#### Một số use case thông thường <a href="#sudungcongcurclone-motsousecasethongthuong" id="sudungcongcurclone-motsousecasethongthuong"></a>

**Lấy danh sách tất cả container**

> $ rclone lsd \<remote\_name>:

**Tạo một container mới**

> $ rclone mkdir \<remote\_name>:mybucket

**Lấy danh sách tất cả object trong một container**

> $ rclone ls \<remote\_name>:mybucket

**Tải xuống tệp tin `file.txt` từ một container**

> $ rclone copy \<remote\_name>:mybucket/file.txt fichier.txt

***

#### Một số use case nâng cao <a href="#sudungcongcurclone-motsousecasenangcao" id="sudungcongcurclone-motsousecasenangcao"></a>

**Đồng bộ thư mục `/home/user/documents` với một container**

> $ rclone sync /home/user/documents \<remote\_name>:mybucket

**Sao chép một tệp tin ở thư mục `/home/user/file.txt` into a bucket**

> $ rclone copy /home/user/file.txt \<remote\_name>:mybucket

{% hint style="info" %}
**Chú ý:**&#x20;

1. Không nên sử dụng phiên bản Rclone quá cũ/ quá mới trên các hệ điều hành có phiên bản quá cũ/ quá mới vì có thể gặp lỗi.
2. Không khuyến khích sử dụng rclone sync vì khi sync sẽ copy **source** sang **destination** và xóa phần khác biệt ở **destination** (khiến **destination** trở thành bản sao của **source**), dễ gây ra sự cố xoá nhầm data nếu truyền sai thông tin **source**, **destination**. Khuyến cáo nên dùng rclone copy.
3. &#x20;Có vài vấn đề khi dùng rclone mount để mount các vStorage container (bucket) thành local directory để sử dụng:\
   \+ Không thể copy, rename, move\
   \+ Không thể listing nhanh chóng\
   \+ Không phân quyền như trên các loại filesystem truyền thống: rwx, uid, gid,...
4. Rclone có hỗ trợ dọn incomplete segment khi tải object lớn (multipart upload). Khi bạn sử dụng Rclone để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, Rclone của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Chúng tôi khuyến cáo bạn thực hiện xóa bỏ những segment rác này để tối ưu hóa chi phí và dung lượng lưu trữ bằng cách:
5. Liệt kê các multipart upload chưa hoàn thành dùng câu lệnh sau:

> rclone  backend list-multipart-uploads [vng:/my-bucket](http://vng/my-bucket)

* Xóa các incomplete segment (segment rác) dùng câu lệnh sau để xóa tất cả các segment rác từ 24 giờ trở về trước:

> rclone cleanup [vng:/my-bucket](http://vng/my-bucket)

Hãy cẩn khi sử dụng tùy chọn (option) max-age trong câu lệnh cleanup như bên dưới vì nếu giá trị max-age quá nhỏ (ví dụ 1 giây), bạn có thể sẽ xóa các segment của multipart upload đang thực hiện mà không phải là những segment rác thực sự. Chúng tôi khuyến cáo bạn hãy sử dụng max-age > 3 ngày để đảm bảo an toàn khi xóa dữ liệu.

> rclone backend cleanup [vng:/my-web](http://vng/my-web) -o max-age=3d

Để biết thêm chi tiết, bạn vui lòng tham khảo tại [https://rclone.org/s3/#cleanup](https://rclone.org/s3/#cleanup).
{% endhint %}
