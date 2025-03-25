# Tích hợp công cụ AWS CLI với vStorage

Để tích hợp công cụ AWS CLI với vStorage, bạn có thể thực hiện theo hướng dẫn bên dưới:&#x20;

1. Tải và cài đặt AWS CLI theo hướng dẫn tại [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Sử dụng S3 key tạo từ vIAM và tiếp tục thực hiện thiết lập theo hướng dẫn tại [https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-short-term.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-short-term.html)

Trong đó:&#x20;

* **Endpoint**: Đường dẫn đến vstorage, [hcm01.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/) (region HCM01 - Hồ Chí Minh) hoặc [han01.vstorage.vngcloud.vn](http://han01.vstorage.vngcloud.vn/) (Region HAN01 - Hà Nội).
* **Access Key & Secret Key:** Là cặp key được cấp thông qua vIAM.
* **Region**: Là vị trí địa lý mà vStorage lưu trữ dữ liệu, tham khảo tại [Region là gì?](../../vstorage-la-gi/region-la-gi.md) và [Farm là gì?](../../vstorage-la-gi/farm-la-gi.md).
