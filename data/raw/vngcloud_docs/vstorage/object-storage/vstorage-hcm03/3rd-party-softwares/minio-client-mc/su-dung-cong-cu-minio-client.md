# Sử dụng công cụ MinIO Client

#### Một số use case thông thường <a href="#sudungcongcuminioclient-motsousecasethongthuong" id="sudungcongcuminioclient-motsousecasethongthuong"></a>

**Lấy danh sách tất cả container**

> $ ./mc ls s3

**Tải lên tệp tin vào một container**

> $ ./mc cp myobject.txt s3/bucket-1

**Tạo một container mới**

> $ ./mc mb bucket\_name

**Lấy danh sách tất cả object trong một container**

> $ ./mc ls cos/testbucket1

**Xóa một object trong một container**

> $ ./mc rm cos/my\_test\_bucket/cp\_from\_minio.txt

**Sao chép một object**

> $ ./mc cp cos/testbucket1/mynewfile1.txt cos/my\_test\_bucket/cp\_from\_minio.txt

***

#### Một số use case nâng cao <a href="#sudungcongcuminioclient-motsousecasenangcao" id="sudungcongcuminioclient-motsousecasenangcao"></a>

**Tạo URL để tải xuống object**

> $ ./mc share download servername/pathtofile

**Tạo URL để tải lên object**

> $ ./mc share upload servername/pathtofile

{% hint style="info" %}
**Chú ý:**

1. Không nên sử dụng phiên bản MinIO Client quá cũ trên các hệ điều hành có phiên bản quá cũ hoặc mới nhất vì có thể gặp lỗi.
2. MinIO Client (mc) không có hỗ trợ dọn các incomplete segment khi tải object lớn (Multipart upload). Khi bạn sử dụng MinIO Client để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, MinIO Client của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Hiện tại, MinIO Client chưa hỗ trợ tính năng dọn các segment rác này. Do đó, chúng tôi khuyến nghị bạn nên xem xét kỹ trước khi sử dụng công cụ này.
{% endhint %}
