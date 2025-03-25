# Sử dụng công cụ AWS CLI

#### Một số use case thông thường <a href="#sudungcongcuawscli-motsousecasethongthuong" id="sudungcongcuawscli-motsousecasethongthuong"></a>

**Tạo một container mới**

> `aws --endpoint-url=`[`https://s3.storage.selcloud.ru`](https://s3.storage.selcloud.ru/) `s3 mb s3://BucketName`

**Tải lên tệp tin vào một container**

> a`ws --endpoint-url=`[`https://s3.storage.selcloud.ru`](https://s3.storage.selcloud.ru/) `s3 cp PathToTheFile s3://BucketName/`

**Tải xuống một object**&#x20;

> `aws --endpoint-url=`[`https://s3.storage.selcloud.ru`](https://s3.storage.selcloud.ru/) `s3 cp s3://BucketName/PathToTheFile File`

**Lấy danh sách tất cả object trong một container**

> `aws --endpoint-url=`[`https://s3.storage.selcloud.ru`](https://s3.storage.selcloud.ru/) `s3 ls --recursive s3://BucketName`

**Xóa một object trong một container**

> `aws --endpoint-url=`[`https://s3.storage.selcloud.ru`](https://s3.storage.selcloud.ru/) `s3 rm s3://BucketName/PathToTheFile/File`

{% hint style="info" %}
**Chú ý:**&#x20;



1. Không nên sử dụng phiên bản AWS CLI quá cũ trên các hệ điều hành có phiên bản quá cũ hoặc mới nhất vì có thể gặp lỗi.
2. AWS CLI có hỗ trợ dọn incomplete segments khi tải object lớn (multipart upload). Khi bạn sử dụng AWS CLI để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, AWS CLI của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Chúng tôi khuyến nghị bạn thực hiện xóa bỏ những segment rác này để tối ưu hóa chi phí và dung lượng lưu trữ bằng cách liệt kê các multipart upload chưa hoàn thành (in-progress multipart upload) dùng câu lệnh bên sau:

> aws s3api list-multipart-uploads --bucket my-bucket

* Xóa các incomplete segment (segment rác) của các multipart upload chưa hoàn thành dùng câu lệnh sau:

> aws s3api abort-multipart-upload --bucket my-bucket --key multipart/01 --upload-id dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx

Chi tiết tham khảo tại: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/abort-multipart-upload.html#examples](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/abort-multipart-upload.html#examples) và [https://docs.aws.amazon.com/cli/latest/reference/s3api/list-multipart-uploads.html#examples](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-multipart-uploads.html#examples)
{% endhint %}
