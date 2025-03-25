# Chia sẻ tài nguyên CORS container

CORS (Cross Origin Resource Sharing) là một cơ chế cho phép nhiều tài nguyên khác nhau của một website có thể được truy vấn từ domain khác với domain của trang đó dựa trên giao thức HTTP. Các CORS request được thực hiện bằng cách thêm các HTTP headers chỉ dẫn cho trình duyệt web về sử dụng và quản lý nội dung cross-domain, cho phép lấy dữ liệu từ một trang khác thông qua các HTTP request chứa các headers chỉ định CORS. CORS được sinh ra là vì [same-origin policy](https://www.w3.org/Security/wiki/Same\_Origin\_Policy), là một chính sách liên quan đến bảo mật được cài đặt vào toàn bộ các trình duyệt hiện nay. Chính sách này ngăn chặn việc truy cập tài nguyên của các domain khác một cách vô tội vạ. Cross-origin resource sharing (viết tắt là CORS) là một tiêu chuẩn để truy cập tài nguyên web trên các tên miền khác nhau. CORS cho phép các web scripts tương tác cởi mở hơn với nội dung bên ngoài tên miền gốc, dẫn đến sự tích hợp tốt hơn giữa các dịch vụ web.

Để chia sẻ tài nguyên CORS container, bạn có thể thực hiện theo hướng dẫn bên dưới:&#x20;



<details>

<summary> Sử dụng vStorage Portal</summary>

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container** bạn muốn chia sẻ tài nguyên CORS.

3\. Chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648515/image2023-3-6\_10-29-22.png?version=1\&modificationDate=1678073363000\&api=v2)hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/49648515/image2023-2-6\_10-20-54.png?version=1\&modificationDate=1675655214000\&api=v2)tại **container** bạn muốn thực hiện sử dụng tính năng chia sẻ tài nguyên CORS và chọn ![](https://docs.vngcloud.vn/download/thumbnails/49648515/image2023-3-6\_10-30-1.png?version=1\&modificationDate=1678073403000\&api=v2).

4\. Màn hình **Thiết lập CORS** được hiển thị. Chọn Header và Value tương ứng cho Header đó. Chọn **Cập nhật**.

CORS chỉ cho thiết lập theo domain xác định ví dụ [https://abc.com.vn](https://abc.com.vn/). Do đó bạn cần nhập Value là giá trị domain xác định này.

<img src="../../../../../.gitbook/assets/Chia_se_tai_nguyen_CORS.gif" alt="" data-size="original">

</details>



<details>

<summary>Sử dụng vStorage API</summary>

Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để chia sẻ tài nguyên CORS container qua vStorage API, hãy xem [API Developers](../../api-developers/).

</details>

