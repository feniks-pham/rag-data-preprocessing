# Sử dụng công cụ S3cmd

## Một số use case thông thường <a href="#sudungcongcus3cmd-motsousecasethongthuong" id="sudungcongcus3cmd-motsousecasethongthuong"></a>

**Lấy danh sách tất cả bucket**

> $ s3cmd ls

**Tạo một bucket mới**

> $ s3cmd mb s3://BUCKET

**Lấy danh sách tất cả object trong một bucket**

> $ s3cmd la

**Tải lên tệp tin vào một bucket** &#x20;

> s3cmd put FILE \[FILE...] s3://BUCKET\[/PREFIX]

**Xóa một object trong một bucket**

> s3cmd del s3://BUCKET/OBJECT

**Sao chép một object**

> s3cmd cp s3://BUCKET1/OBJECT1 s3://BUCKET2\[/OBJECT2]

**Di chuyển một object**

> s3cmd mv s3://BUCKET1/OBJECT1 s3://BUCKET2\[/OBJECT2]

## Một số use case nâng cao <a href="#sudungcongcus3cmd-motsousecasenangcao" id="sudungcongcus3cmd-motsousecasenangcao"></a>

**Truy xuất presign URL cho một bucket trong một khoảng thời gian cố định**

> s3cmd signurl s3://BUCKET/OBJECT \<expiry\_epoch|+expiry\_offset>

**Liệt kê các multipart upload chưa hoàn thành**&#x20;

> s3cmd multipart s3://BUCKET \[Id]

**Xóa các incomplete segment (segment rác) cho các incomplete upload id được liệt kê ở câu lệnh trên**

> s3cmd abortmp s3://BUCKET/OBJECT Id

#### Chú ý khi sử dụng S3cmd <a href="#sudungcongcus3cmd-chuykhisudungs3cmd" id="sudungcongcus3cmd-chuykhisudungs3cmd"></a>

{% hint style="info" %}
**Chú ý:**

1. Không nên sử dụng phiên bản S3cmd quá cũ/ quá mới trên các hệ điều hành có phiên bản quá cũ/ quá mới vì có thể gặp lỗi.
2. S3cmd có hỗ trợ dọn incomplete segments khi tải object lớn (Multipart upload). Khi bạn sử dụng S3cmd để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, S3cmd của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Chúng tôi khuyến cáo bạn thực hiện xóa bỏ những segment rác này để tối ưu hóa chi phí và dung lượng lưu trữ bằng cách:
3. Liệt kê các multipart upload chưa hoàn thành dùng câu lệnh sau:

> s3cmd multipart s3://BUCKET

* Xóa các incomplete segment (segment rác) cho các incomplete upload id được liệt kê ở câu lệnh trên:\


> s3cmd abortmp s3://BUCKET/OBJECT Id
>
> Ví dụ: s3cmd abortmp s3://s3cmd-bucket/2gb-video.mp4 MWRmNjBhNWUtZGMwNy00YjNiLThhOTgtMWFmYmIxYzI0OTE

Các segment rác của tệp tin chưa được tải lên thành công sẽ được dọn sạch. Chi tiết tham khảo tại [đây.](https://s3tools.org/usage)&#x20;
{% endhint %}
