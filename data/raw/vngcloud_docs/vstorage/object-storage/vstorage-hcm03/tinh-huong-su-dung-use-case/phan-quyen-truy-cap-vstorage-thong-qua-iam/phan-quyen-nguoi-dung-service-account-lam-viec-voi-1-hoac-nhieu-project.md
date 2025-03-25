# Phân quyền người dùng Service Account làm việc với 1 hoặc nhiều project

#### Kịch bản <a href="#phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuproject-kichban" id="phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuproject-kichban"></a>

* Giả sử bạn là người dùng **Root User Account** và bạn đã khởi tạo và tải lên tệp tin vào 2 project: **Project01** và **Project02**.
* Hiện tại, bạn muốn tạo 2 một người dùng mới, trong đó
  * Người dùng Leo có thể **sử dụng 3rd party software** (ở đây chúng tôi ví dụ bạn muốn sử dụng **S3 Browser**) và có quyền đọc tất cả dữ liệu bao gồm các container, directory, object trên **Project01**.
  * Người dùng Anne có thể **sử dụng 3rd party software** (ở đây chúng tôi ví dụ bạn muốn sử dụng **S3 Browser**) và có quyền đọc và ghi trên tất cả các container, directory, object trên **Project01** và **Project02**.

Minh họa cấu trúc lưu trữ dữ liệu của bạn trên vStorage:

```
Project01 - HAN01            
Container01                                          
    └── Directory01                                            
           ├── object01.txt                                
           ├── object02.jpg
    └── object03.png
    └── object04.txt
Container03
    └── object10.png
Container04
-------------------------------
Project02 - HCM01          
Container02
    └── Directory02                                            
           ├── object05.txt                                
           ├── object06.jpg
    └── object07.png
    └── object08.txt
Container05
```

#### Để giải quyết bài toán phân quyền này, hãy làm theo các bước bên dưới: <a href="#phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuproject-degiaiquyetbaitoanphanquyennay-haylamthe" id="phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuproject-degiaiquyetbaitoanphanquyennay-haylamthe"></a>

**Bước 1: Khởi tạo S3 key**

Thực hiện khởi tạo S3 key theo hướng dẫn tại [Khởi tạo S3 key](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-s3-key.md). Giả sử 2 S3 key được khởi tạo là:

| S3 key name      | **S3key\_User\_Leo**                         | **S3key\_User\_Anne**                        |
| ---------------- | -------------------------------------------- | -------------------------------------------- |
| Region           | <ul><li><strong>HAN01</strong></li></ul>     | <ul><li><strong>HCM01</strong></li></ul>     |
| vStorage project | <ul><li><strong>Project01</strong></li></ul> | <ul><li><strong>Project02</strong></li></ul> |

* Nếu S3 key bạn vừa tạo có trạng thái Restriction by IAM = **ON** thì bạn cần tiếp tục thực hiện các bước số 2, 3, 4 mà chúng tôi mô tả bên dưới.&#x20;
* Nếu S3 key bạn vừa tạo có trạng thái Restriction by IAM = **OFF** thì bạn có thể trực tiếp sử dụng S3 key này để tích hợp với ứng dụng S3 Browser theo mô tả tại bước số 5 bên dưới.

**Bước 2: Khởi tạo tài khoản Service Account**

Thực hiện khởi tạo 2 tài khoản Service Account theo hướng dẫn tại [Khởi tạo tài khoản Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md). Giả sử 2 tài khoản Service Account được khởi tạo là:

* **SA\_User\_Leo**
* **SA\_User\_Anne**

**Bước 3: Khởi tạo policy cho 2 Service Account( SA\_User\_Leo và SA\_User\_Anne)**

Thực hiện khởi tạo policy cho 2 Service Account theo hướng dẫn tại [Khởi tạo policy cho Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-policy-cho-service-account.md). Cụ thể:

| Thành phần     | Policy cho SA\_User\_Leo                                                                                                | Policy cho SA\_User\_Anne                                                                                                                       |                                                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Product        | vstorage                                                                                                                | vstorage                                                                                                                                        |                                                                         |
| Action         | <ul><li><strong>List</strong></li><li><strong>Read</strong></li></ul><p>(Bao gồm tất cả các actions trong mỗi nhóm)</p> | <ul><li><strong>All vstorage actions</strong>. (List, Read, Write)</li></ul><p>(Bao gồm tất cả các actions trong mỗi nhóm)).</p>                |                                                                         |
| Resource       | Region                                                                                                                  | <ul><li><strong>HAN01</strong></li></ul>                                                                                                        | <ul><li><strong>HAN01</strong></li><li><strong>HCM01</strong></li></ul> |
| Project\_ID    | <ul><li><strong>Project_ID</strong> của <strong>Project01</strong></li></ul>                                            | <ul><li><strong>Project_ID</strong> của <strong>Project01</strong></li><li><strong>Project_ID</strong> của <strong>Project02</strong></li></ul> |                                                                         |
| Container name | <ul><li>Any</li></ul>                                                                                                   | <ul><li>Any</li></ul>                                                                                                                           |                                                                         |
| Object name    | <ul><li>Any</li></ul>                                                                                                   | <ul><li>Any</li></ul>                                                                                                                           |                                                                         |

**Bước 3: Liên kết (Gán quyền) tài khoản Service Account với policy tương ứng.**

Thực hiện liên kết (gán quyền) 2 tài khoản Service Account với policy đã tạo ở bước 2 theo hướng dẫn tại [Liên kết tài khoản Service Account với policy tương ứng](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/lien-ket-tai-khoan-service-account-voi-policy-tuong-ung.md)

**Bước 4: Tích hợp vStorage với S3 Browser**

Thực hiện tích hợp vStorage với S3 Browser theo hướng dẫn tại [Tích hợp công cụ S3 Browser với vStorage](../../3rd-party-softwares/s3-browser/tich-hop-cong-cu-s3-browser-voi-vstorage.md). Cụ thể:&#x20;

| Thành phần              | Nội dung                                                                                                                                                                                                                                                                                                        |                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Display name            | Tên hiển thị của account.                                                                                                                                                                                                                                                                                       |                                                                  |
| Account type            | **S3 Compatible Storage**                                                                                                                                                                                                                                                                                       |                                                                  |
| REST Endpoint           | SA\_User\_Leo                                                                                                                                                                                                                                                                                                   | [han01.vstorage.vngcloud.vn](http://han01.vstorage.vngcloud.vn/) |
| SA\_User\_Anne          | [hcm01.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/)                                                                                                                                                                                                                                                |                                                                  |
| Access Key ID           | **Access Key** được tạo ở bước 1.                                                                                                                                                                                                                                                                               |                                                                  |
| Secret Access Key       | **Secret Key** được tạo ở bước 1.                                                                                                                                                                                                                                                                               |                                                                  |
| Protocol                | **Use Secure transfer (SSL/TLS)**                                                                                                                                                                                                                                                                               |                                                                  |
| Signature version       | **Signature V4**                                                                                                                                                                                                                                                                                                |                                                                  |
| Addressing model        | <p>Path Style (Request URL: <a href="https://hcm01.vstorage.vngcloud.vn/">https://hcm01.vstorage.vngcloud.vn</a>/v1/AUTH_{project_id}/{bucket}/{file})</p><p>Virtual hosted style (Request URL: https://{bucket}.<a href="http://hcm01.vstorage.vngcloud.vn/%7Bfile">hcm01.vstorage.vngcloud.vn/{file</a>})</p> |                                                                  |
| Override storage region | SA\_User\_Leo                                                                                                                                                                                                                                                                                                   | **HAN01**                                                        |
| SA\_User\_Anne          | **HCM01**                                                                                                                                                                                                                                                                                                       |                                                                  |
