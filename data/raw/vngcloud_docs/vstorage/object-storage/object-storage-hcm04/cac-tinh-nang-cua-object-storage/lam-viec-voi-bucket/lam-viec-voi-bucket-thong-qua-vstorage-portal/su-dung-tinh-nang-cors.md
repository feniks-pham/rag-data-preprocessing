# Sử dụng tính năng CORS

## **Tổng quan**

**CORS (Cross-Origin Resource Sharing)** trên vStorage cho phép các ứng dụng từ một domain khác (origin) có thể truy cập tài nguyên trên bucket của bạn. Tính năng này hữu ích khi bạn muốn truy cập các object trong bucket từ một ứng dụng web chạy trên một domain khác, chẳng hạn như một ứng dụng frontend muốn tải ảnh từ bucket S3.

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** chứa **bucket** bạn muốn thiết lập CORS.

3\. Chọn biểu tượng **Action** và chọn **Set CORS.**

<figure><img src="../../../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4\. Tại đây, bạn hãy nhập file CORS configuration. CORS Configuration trong vStorage là một file JSON với một danh sách các quy tắc (rules) mà bạn muốn áp dụng. Mỗi quy tắc sẽ bao gồm:&#x20;

* **AllowedMethods**: Các phương thức HTTP được phép, như `GET`, `PUT`, `POST`, `DELETE`, `HEAD`.
* **AllowedOrigins**: Các domain được phép truy cập bucket.
* **AllowedHeaders**: Các loại header mà ứng dụng có thể gửi trong request.
* **ExposeHeaders**: Các header mà ứng dụng có thể thấy trong response từ S3.
* **MaxAgeSeconds**: Thời gian tính bằng giây mà trình duyệt nên lưu trữ kết quả của request trước khi gửi request khác.

<figure><img src="../../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5\. Chọn **Update** để lưu lại cấu hình đã thiết lập cho CORS.

***

## Ví dụ minh họa

### **Ví dụ 1:** CORS cho phép một domain cụ thể truy cập với phương thức GET

* Cho phép một domain cụ thể truy cập object trong bucket của bạn qua phương thức `GET`.

```json
[
  {
    "AllowedOrigins": ["https://example.com"],
    "AllowedMethods": ["GET"],
    "AllowedHeaders": ["*"],
    "MaxAgeSeconds": 3000
  }
]
```

### **Ví dụ 2:** CORS cho nhiều domain và nhiều phương thức HTTP

* Cho phép nhiều domain truy cập với nhiều phương thức khác nhau, bao gồm `GET`, `POST`, và `DELETE`.

```json
[
  {
    "AllowedOrigins": ["https://example.com", "https://anotherdomain.com"],
    "AllowedMethods": ["GET", "POST", "DELETE"],
    "AllowedHeaders": ["Authorization", "Content-Type"],
    "ExposeHeaders": ["x-amz-request-id", "x-amz-id-2"],
    "MaxAgeSeconds": 3600
  }
]
```

{% hint style="info" %}
**Chú ý:**

* **Bảo mật**: Chỉ cho phép các origin tin cậy để tránh các rủi ro bảo mật.
* **CORS không thay thế được quyền S3**: CORS chỉ quy định những request nào từ các domain khác sẽ được phép, nhưng các quyền truy cập thực tế vào bucket vẫn được kiểm soát qua **Bucket Policy**, **ACL**, hoặc **IAM Policy**.
{% endhint %}
