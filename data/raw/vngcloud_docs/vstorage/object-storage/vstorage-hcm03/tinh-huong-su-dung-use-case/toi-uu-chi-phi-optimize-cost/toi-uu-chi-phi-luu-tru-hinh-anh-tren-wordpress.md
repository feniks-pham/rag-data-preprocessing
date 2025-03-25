# Tối ưu chi phí lưu trữ hình ảnh trên Wordpress

Nhằm tiết kiệm không gian lưu trữ trên Wordpress Server, bạn có thể tích hợp thêm vStorage để lưu trữ hình ảnh, video.&#x20;

Để kết nối, bạn cần cài đặt một Worpress Plugin hỗ trợ giao thức S3. Chúng tôi gợi lý cho bạn có thể sử dụng Plugin: MediaCloud. Để biết thêm thông tin, hãy xem tại [https://wordpress.org/plugins/ilab-media-tools/](https://wordpress.org/plugins/ilab-media-tools/).

<details>

<summary>Cài đặt Plugin MediaCloud</summary>

1. Tại giao diện quản trị Wordpress, bạn chọn **Plugins** rồi tiếp tục chọn **Add New**.&#x20;
2. Tại ô search, bạn nhập **MediaCloud**, nhấn **Tìm kiếm** và chọn **Install Now** và chờ cho quá trình cài đặt hoàn tất.&#x20;
3. Sau khi cài đặt xong, bạn chọn tiếp **Activate.**

</details>

<details>

<summary>Cài đặt thêm Region của vStorage</summary>

1. Trước khi cấu hình, bên góc trái, bạn quay lại Plugins, chọn **Plugin Editor**.&#x20;
2. Tại góc phải, bạn chọn đến Media Cloud và nhấn **Select**.&#x20;
3. Sau đó, bạn duyệt tới file **config/storage/s3.config.php** và thêm thông tin **Region** của container đã tạo trên vStorage tại mục **options** trong **mcloud-storage-s3-region**. VD: Nếu là Region HAN01, bạn thêm với cú pháp tương tự:  'HAN01’ => ‘HAN01’.
4. Sau khi thêm, bạn kéo xuống duới chọn **Update File**.&#x20;

</details>

<details>

<summary>Cấu hình vStorage làm nơi lưu trữ media cho Wordpress</summary>

1. Tại góc trái, bạn chuyển tới **MediaCloud** rồi chọn **Settings**.&#x20;

Giả sử bạn có vStorage với thông tin sau (tham khảo cách lấy thông tin tại bài viết trước): &#x20;

Region: HCM01  &#x20;

S3 storage URL: [https://](https://s3-hcm-1.vinadata.vn/)[hcm01.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/)/&#x20;

Container: container01 (Public Container)&#x20;

Access Key: f6eb9432193a3cfb9da7834aac5c41c5&#x20;

Secret Key: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&#x20;

&#x20;Bạn cấu hình như sau:&#x20;

\+ Storage Provider: Other S3 Compatible Service.&#x20;

\+ Access key: f6eb9432193a3cfb9da7834aac5c41c5&#x20;

\+ Secret: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&#x20;

\+ Bucket: container01&#x20;

\+ Region: HCM01&#x20;

\+ Custom endpoint: [hcm01.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/)

\+ Path Style Endpoint: tick chọn có.&#x20;

\+ Upload Privacy ACL: public-read&#x20;

\+ Cache Control: public,max-age=2592000&#x20;

2\. Tick chọn **có** tại: Queue Deletes, Delete From Storage, Delete Uploaded Files, Upload Images, Upload Videos Files, Upload Audio Files, Upload Documents.&#x20;

3\. Tại phần cấu hình CDN URL: nếu bạn có sử dụng một dịch vụ CDN như **vCDN** của VNG Cloud, bạn có thể cấu hình thêm **Endpoint** của vCDN tại đây. Nếu không, bạn có thể để đuờng dẫn đến container trên vStorage.&#x20;

4\. Để lấy link public của container trên vStorage, bạn có thể **upload** thử một file sample bất kì lên container, click chọn vào và xem đuờng link trước tên file sample.&#x20;

VD: đuờng link của container container01 như trong hình là:  \
[https://](https://sw-hcm-1.vinadata.vn/v1/AUTH\_cb6845eecfb345b39f5cd2f0ffc4d3db/container01/)[hcm01.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/)/v1/AUTH\_cb6845eecfb345b39f5cd2f0ffc4d3db/container01/ &#x20;

5\. Bạn điền **URL** này vào **CDN Base URL** và **Document CDN Base URL**.&#x20;

6\. Sau cùng, bạn kéo xuống cuối và chọn **Save Changes**.&#x20;

</details>
