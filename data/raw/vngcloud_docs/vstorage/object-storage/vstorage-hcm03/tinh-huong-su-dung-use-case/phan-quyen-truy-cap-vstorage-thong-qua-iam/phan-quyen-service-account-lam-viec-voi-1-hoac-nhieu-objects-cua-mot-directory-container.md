# Phân quyền Service Account làm việc với 1 hoặc nhiều objects của một directory/container

#### Kịch bản <a href="#phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuobjectscuamotdirectoryhoaccontainer-kichban" id="phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuobjectscuamotdirectoryhoaccontainer-kichban"></a>

* Giả sử bạn là người dùng **Root User Account** và bạn đã khởi tạo và tải lên tệp tin vào 2 project: **Project01** và **Project02**.
* Hiện tại, bạn muốn tạo 2 một người dùng mới, trong đó
  * Người dùng Leo có thể **sử dụng 3rd party software** (ở đây chúng tôi ví dụ bạn muốn sử dụng **S3 Browser**) và có quyền đọc tất cả dữ liệu **Directory01/object 01.txt, object03.png** trên **Container01** thuộc **Project01**.
  * Người dùng Anne có thể **sử dụng 3rd party software** (ở đây chúng tôi ví dụ bạn muốn sử dụng **S3 Browser**) và có quyền đọc và ghi **Directory01, object04.txt** trên **Container01** thuộc **Project01** và **Directory02/object06.jpg, object07.png, object08.txt** trên **Container02** thuộc **Project02**.

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

#### Để giải quyết bài toán phân quyền này, hãy làm theo các bước bên dưới: <a href="#phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuobjectscuamotdirectoryhoaccontainer-degiaiquyetb" id="phanquyennguoidungserviceaccountlamviecvoi1hoacnhieuobjectscuamotdirectoryhoaccontainer-degiaiquyetb"></a>

**Bước 1: Khởi tạo S3 key**

Thực hiện khởi tạo S3 key theo hướng dẫn tại [Khởi tạo S3 key](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-s3-key.md). Giả sử 2 S3 key được khởi tạo là:

| S3 key name      | **S3key\_User\_Leo**                         | **S3key\_User\_Anne**                        |
| ---------------- | -------------------------------------------- | -------------------------------------------- |
| Region           | <ul><li><strong>HAN01</strong></li></ul>     | <ul><li><strong>HCM01</strong></li></ul>     |
| vStorage project | <ul><li><strong>Project01</strong></li></ul> | <ul><li><strong>Project02</strong></li></ul> |

* Thiết lập trạng thái Restriction by IAM = **ON** cho S3 key mà bạn vừa khởi tạo.

**Bước 2: Khởi tạo tài khoản Service Account**

Thực hiện khởi tạo 2 tài khoản Service Account theo hướng dẫn tại [Khởi tạo tài khoản Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-tai-khoan-service-account.md). Giả sử 2 tài khoản Service Account được khởi tạo là:

* **SA\_User\_Leo**
* **SA\_User\_Anne**

**Bước 3: Khởi tạo policy cho 2 Service Account( SA\_User\_Leo và SA\_User\_Anne)**

Thực hiện khởi tạo policy cho 2 Service Account theo hướng dẫn tại [Khởi tạo policy cho Service Account](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-policy-cho-service-account.md). Cụ thể:

<table><thead><tr><th>Thành phần</th><th width="226">Policy cho SA_User_Leo</th><th width="241">Policy cho SA_User_Anne</th><th></th></tr></thead><tbody><tr><td>Product</td><td>vstorage</td><td>vstorage</td><td></td></tr><tr><td>Action</td><td><ul><li><strong>List</strong></li><li><strong>Read</strong></li></ul><p>(Bao gồm tất cả các actions trong mỗi nhóm)</p></td><td><ul><li><strong>All vstorage actions</strong>. (List, Read, Write)</li></ul><p>(Bao gồm tất cả các actions trong mỗi nhóm)).</p></td><td></td></tr><tr><td>Resource</td><td>Region</td><td><ul><li><strong>HAN01</strong></li></ul></td><td><ul><li><strong>HAN01</strong></li><li><strong>HCM01</strong></li></ul></td></tr><tr><td>Project_ID</td><td><ul><li><strong>Project_ID</strong> của Project01</li></ul></td><td><ul><li><strong>Project_ID</strong> của Project01</li><li><strong>Project_ID</strong> của Project02</li></ul></td><td></td></tr><tr><td>Container name</td><td><ul><li><strong>Container01</strong></li></ul></td><td><ul><li><strong>Container01</strong></li><li><strong>Container02</strong></li></ul></td><td></td></tr><tr><td>Object name</td><td><ul><li><strong>Directory01/object 01.txt</strong></li><li><strong>object03.png</strong></li></ul></td><td><ul><li><strong>Directory01/*</strong></li><li><strong>object04.txt</strong></li><li><strong>Directory02/object06.jpg</strong></li><li><strong>object07.png</strong></li><li><strong>object08.txt</strong></li></ul></td><td></td></tr></tbody></table>

**Bước 3: Liên kết (Gán quyền) tài khoản Service Account với policy tương ứng.**

Thực hiện liên kết (gán quyền) 2 tài khoản Service Account với policy đã tạo ở bước 2 theo hướng dẫn tại [Liên kết tài khoản Service Account với policy tương ứng](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/lien-ket-tai-khoan-service-account-voi-policy-tuong-ung.md)

**Bước 4: Tích hợp vStorage với S3 Browser**

Thực hiện tích hợp vStorage với S3 Browser theo hướng dẫn tại [Tích hợp công cụ S3 Browser với vStorage](../../3rd-party-softwares/s3-browser/tich-hop-cong-cu-s3-browser-voi-vstorage.md). Cụ thể:&#x20;

<table><thead><tr><th>Thành phần</th><th width="306">Nội dung</th><th></th></tr></thead><tbody><tr><td>Display name</td><td>Tên hiển thị của account.</td><td></td></tr><tr><td>Account type</td><td><strong>S3 Compatible Storage</strong></td><td></td></tr><tr><td>REST Endpoint</td><td>SA_User_Leo</td><td><a href="http://han01.vstorage.vngcloud.vn/">han01.vstorage.vngcloud.vn</a></td></tr><tr><td>SA_User_Anne</td><td><a href="http://hcm01.vstorage.vngcloud.vn/">hcm01.vstorage.vngcloud.vn</a></td><td></td></tr><tr><td>Access Key ID</td><td><strong>Access Key</strong> được tạo ở bước 1.</td><td></td></tr><tr><td>Secret Access Key</td><td><strong>Secret Key</strong> được tạo ở bước 1.</td><td></td></tr><tr><td>Protocol</td><td><strong>Use Secure transfer (SSL/TLS)</strong></td><td></td></tr><tr><td>Signature version</td><td><strong>Signature V4</strong></td><td></td></tr><tr><td>Addressing model</td><td><p>Path Style (Request URL: <a href="https://hcm01.vstorage.vngcloud.vn/">https://hcm01.vstorage.vngcloud.vn</a>/v1/AUTH_{project_id}/{bucket}/{file})</p><p>Virtual hosted style (Request URL: https://{bucket}.<a href="http://hcm01.vstorage.vngcloud.vn/%7Bfile">hcm01.vstorage.vngcloud.vn/{file</a>})</p></td><td></td></tr><tr><td>Override storage region</td><td>SA_User_Leo</td><td><strong>HAN01</strong></td></tr><tr><td>SA_User_Anne</td><td><strong>HCM01</strong></td><td></td></tr></tbody></table>
