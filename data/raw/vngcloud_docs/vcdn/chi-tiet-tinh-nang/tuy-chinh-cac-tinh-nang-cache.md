# Caching

## Tổng quan

**Caching** là một chức năng cốt lõi của hệ thống vCDN, giúp tăng tốc độ truy cập nội dung bằng cách lưu trữ tạm thời các bản sao dữ liệu (như file tĩnh, hình ảnh, video, hoặc dữ liệu API) trên các máy chủ biên (edge servers) gần người dùng cuối. Điều này không chỉ giảm thời gian tải trang mà còn giảm tải cho máy chủ gốc (origin server).

## Chi tiết

Hiện tại, vCDN đang hỗ trợ tùy chỉnh các tính năng cach&#x65;**:** cho phép khách hàng tùy chỉnh các chỉ số cache trên hệ thống và trên browser. Cụ thể:&#x20;

<figure><img src="../../.gitbook/assets/image (16) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Trong đó:    &#x20;

* **Caching Level**: Xác định mức độ cache của CDN. Với VOD, vCDN đang cung cấp 3 mức độ cache bao gồm: URL without query string only, Skip Query String of URL, URL With Query String.
  * URL Without Query String Only: Không cache nếu có URL Param trong request.
  * Skip Query String of URL: Loại bỏ URL Param khi tạo Cache.
  * URL With Query String: Cache toàn bộ URL bao gồm cả URL Param.
* **Server Cache Expiration (TTL):** Khoảng thời gian mà hệ thống vCDN sẽ lưu trữ tài nguyên của bạn trong bộ nhớ cache. Trong khoảng thời gian này, hệ thống vCDN sẽ không truy cập server gốc mà phản hồi yêu cầu từ bộ nhớ cache của vCDN. Bạn có thể chọn thời gian này từ 30 phút cho tới 1 năm tùy theo nhu cầu cho hệ thống của bạn.
* **Browser Cache Expiration:** Thời gian vCDN yêu cầu trình duyệt của người dùng lưu trữ tệp trong bộ nhớ cache cục bộ.
* **Development mode:** Chế độ nhà phát triển. Tính năng này cho phép tạm thời tắt caching tại Edge Server để hỗ trợ giai đoạn thử nghiệm hoặc kiểm tra nội dung trong khi phát triển. Mọi yêu cầu sẽ được trả về trực tiếp từ Origin, giúp cập nhật nội dung ngay lập tức mà không cần xóa cache.
