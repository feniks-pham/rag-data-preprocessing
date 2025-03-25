# Sử dụng tính năng Bucket Policy

## Tổng quan

Tính năng **Bucket Policy** trên vStorage là một công cụ mạnh mẽ giúp quản lý quyền truy cập vào bucket của bạn thông qua các quy tắc dạng JSON. Tính năng này cho phép bạn kiểm soát chi tiết các action mà IAM User (coming soon), tài khoản vStorage khác, hoặc các nguồn bên ngoài có thể thực hiện trên bucket và các object trong đó. Dưới đây là hướng dẫn cơ bản để cấu hình Bucket Policy:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng <img src="../../../../../../.gitbook/assets/image (7) (1) (1).png" alt="" data-size="line">tại **project** chứa **bucket** bạn muốn phân quyền.
3. Nếu bạn muốn phân quyền bucket cho một **Root User Account** hoặc **IAM User Account** hay **Service Account** khác, bạn cần biết thông tin **vStorage User ID** của người dùng mà bạn muốn phân quyền:&#x20;
   1. Đối với **Root User Account**: bạn có thể lấy thông tin **vStorage User ID** ngay tại trang thông tin **project** theo hình dưới.

<figure><img src="../../../../../../.gitbook/assets/image (867).png" alt=""><figcaption></figcaption></figure>

b. Đối với **IAM User Account** và **Service Account**: bạn có thể lấy thông tin **vStorage User ID** tại mục  **Identity and Access Management**

<figure><img src="../../../../../../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Tiếp tục chọn **Bucket** bạn muốn thực hiện phân quyền.
5. Chọn biểu tượng **Action** và chọn **Configure policy.**

<figure><img src="../../../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Tại đây, bạn có thể chọn cấu hình cho từng **Statement** ở bên trái hoặc trực tiếp chỉnh sửa file JSON ở cột bên phải. Cụ thể cấu trúc một Bucket Policy bao gồm:

* **Version**: Xác định phiên bản của Bucket Policy (nên dùng `"2012-10-17"`).
* **Statement**: Mỗi chính sách sẽ có một hoặc nhiều **Statement** (mục đích cụ thể của policy).
  * **Effect**: `Allow` hoặc `Deny` quyền truy cập.
  * **Principal**: Đối tượng được cấp quyền truy cập (IAM User (coming soon),  tài khoản vStorage cụ thể).
  * **Action**: Các hành động cho phép trên bucket, ví dụ: `s3:GetObject` (xem object), `s3:PutObject` (tải lên object), `s3:DeleteObject` (xóa object),…
  * **Resource**: Các bucket và object cụ thể bị ảnh hưởng bởi policy (dùng ARN để định danh tài nguyên).
  * **Condition**: (Tùy chọn) Điều kiện cụ thể giới hạn quyền truy cập.

<figure><img src="../../../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Chọn **Save** để lưu lại cấu hình Bucket Policy.

***

## Ví dụ minh họa

### **Ví dụ 1: Cấp quyền public-read (chỉ đọc) cho toàn bộ bucket**&#x20;

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}

```

_Cấp quyền cho tất cả mọi người (`*`) quyền đọc (`s3:GetObject`) tất cả các object trong bucket._

***

### **Ví dụ 2: Chỉ cấp quyền cho một vStorage User cụ thể tải lên và xóa object**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam:::user/vStorage user ID" },
      "Action": ["s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

_Chỉ cho phép người dùng có vStorage user ID trong file được quyền tải lên (`s3:PutObject`) và xóa (`s3:DeleteObject`) object._

***

### **Ví dụ 3: Chặn tất cả vStorage User (trừ Root User Account) action vào bucket và object**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    }
  ]
}
```

_Không cho phép ai ngoài Root User làm việc với bucket và object._

### **Ví dụ 4: Chỉ cấp quyền cho người dùng sử dụng địa chỉ IP 10.0.0.1 mới có thể action lấy thông tin object**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ],
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": "10.0.0.1"
        }
      }
    }
  ]
}
```

_Chỉ cho phép người dùng có địa chỉ IP 10.0.0.1 mới có thể lấy thông tin object_

### **Ví dụ 5: Thêm nhiều statement trong một file JSON**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    },
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam:::user/vStorage user ID" },
      "Action": ["s3:PutObject", "s3:DeleteObject"],
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    },
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutBucketEncryption",
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    }
  ]
}

```

_Cho phép tất cả người dùng GetObject + chỉ cho phép 1 vStorage user trong file được PutObject và DeleteObject + Không cho phép tất cả user thực hiện PutBucketEncryption_

{% hint style="info" %}
**Chú ý:**

* **Kiểm tra quyền public**: Một số Bucket Policy có thể dẫn đến các quyền truy cập public. Bạn nên kiểm tra kỹ để đảm bảo bảo mật cho dữ liệu.
* **Bucket Policy và ACL**: Đảm bảo rằng các quyền trong Bucket Policy không xung đột với **Access Control List (ACL)** của bucket hoặc object.
{% endhint %}
