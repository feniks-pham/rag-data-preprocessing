# Tích hợp công cụ MinIO Client với vStorage

Để tích hợp công cụ MinIO Client với vStorage, bạn có thể thực hiện theo hướng dẫn bên dưới:&#x20;

1. Tải và cài đặt MinIO Client theo hướng dẫn tại [https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs-redirect](https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs-redirect).
2. Chạy lệnh

> mc config host add \<ALIAS> \<COS-ENDPOINT> \<ACCESS-KEY> \<SECRET-KEY>

Trong đó:&#x20;

* **Cos endpoint**: Đường dẫn đến vstorage, [hcm01.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/) (region HCM01 - Hồ Chí Minh) hoặc [han01.vstorage.vngcloud.vn](http://han01.vstorage.vngcloud.vn/) (Region HAN01 - Hà Nội).
* **Access Key & Secret Key:** Là cặp key được cấp thông qua vIAM.
