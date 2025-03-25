# Sử dụng Swift Rest API

Để sử dụng Swift Rest API, bạn cần có ít nhất 1 Swift user. Để tạo swift user, tham khảo thêm tại [Khởi tạo Swift user](../../quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-swift-user.md). Bạn có thể sử dụng Swif user này để tạo (hoặc xóa) nhiều container, container như một đơn vị lưu trữ (giống như một thư mục), trong mỗi container khách hàng có thể upload, get, delete nhiều object tương ứng (object ở đây được hiểu như một file, hoặc một folder con trong container).

**Quy trình cơ bản**: Xác thực -> Tạo container -> Upload Object

Bên dưới là danh sách các Swift rest API mà chúng tôi cung cấp và hướng dẫn thao tác với POSTMAN hoặc CURL

#### 1. Get token <a href="#sudungswiftrestapi-1.gettoken" id="sudungswiftrestapi-1.gettoken"></a>

Thông tin cần cung cấp: username, password, projectId, authentication url

<table data-header-hidden><thead><tr><th width="205"></th><th></th></tr></thead><tbody><tr><td>Url</td><td>/auth/tokens</td></tr><tr><td>Method</td><td>POST</td></tr><tr><td>Header</td><td>Content-Type: application/json</td></tr><tr><td>Body</td><td>{ "auth": { "identity": { "methods": [ "password" ], "password": { "user": { "domain": { "name": "default" }, "name": "{username}", "password": "{password}" } } }, "scope": { "project": { "domain": { "name": "default" }, "id": "{projectId}" } } } }</td></tr></tbody></table>

&#x20;Kết quả trả về cần lưu ý những thông tin sau:

**Response trả về**

> "url: [https://vos-ss-lab-hcm-sw.vinadata.vn/v1/AUTH\_d6f0078021f4417989d6ba8ae4320dea](https://vos-ss-lab-hcm-sw.vinadata.vn/v1/AUTH_d6f0078021f4417989d6ba8ae4320dea)" với public interface trong catalog có type "object-store", đây là link dùng cho những request sau này. Trong đó, " _AUTH\_d6f0078021f4417989d6ba8ae4320dea_" tương ứng với một account trong object storage.

**Header trả về**&#x20;

> "x-subject-token: gAAAAABdAhsbpeT0CLQiUvTgX3TcVua8c7RLFIY074FlLvDWpGp06EV8SRCbuLGzSL5Q2AnfYogSWydNeZc5dWpRbTKxiwGXuP-wAoPPmIGvBctSkkwnhMF8UQXLBmwlIT43Mudc9ZuHgRLqlW1BT3OmhN9ugKTQHyzgCuzBmHqVgtXp6dRJYr0", đây là thông tin token dùng để xác thực cho những request sau.

**Chú ý:**

* Token luôn có expired, nếu hết expired vui lòng get token mới

**Get token dùng CURL thông qua RESTful API**

> curl -i -X POST -H 'Content-Type: application/json; charset=utf-8' \<authentication\_url>/v3/auth/tokens -d \<auth\_body>
>
> curl -i -X POST "[https://sw-auth-1.vinadata.vn/v3/auth/tokens](https://sw-auth-1.vinadata.vn/v3/auth/tokens)" \\
>
> -H 'Content-Type: application/json; charset=utf-8' \\
>
> -d $'{
>
> "auth": {
>
> "scope": {
>
> "project": {
>
> "id": "6e89e27c18824e70b84a02487a93c69f",
>
> "domain": {
>
> "name": "default"
>
> }
>
> }
>
> },
>
> "identity": {
>
> "methods": \[
>
> "password"
>
> ],
>
> "password": {
>
> "user": {
>
> "name": "${username}",
>
> "password": "${password},
>
> "domain": {
>
> "name": "default"
>
> }
>
> }
>
> }
>
> }
>
> }
>
> }'

#### 2. Tạo mới một container <a href="#sudungswiftrestapi-2.taomoimotcontainer" id="sudungswiftrestapi-2.taomoimotcontainer"></a>

| Url    | /v1/{account}/{container\_name} |
| ------ | ------------------------------- |
| Method | PUT                             |
| Header | X-Auth-Token                    |
| Body   | (Không bắt buộc)                |

* Trong đó :

\+ Value của header "X-Auth-Token" chính là value của "x-subject-token" được lấy từ mục 3.1 (Get Token).

\+ "container\_name" là tên của container, bạn có thể đặt tùy ý. Tuy nhiên để tương thích với tất cả các client tools cũng như tránh các lỗi liên quan đến việc xử lý ký tự đặc biệt hoặc unicode thì tên container chỉ nên chứa các ký tự (a-z, A-Z) hoặc số (0-9). Tên container không nên chứa các ký tự đặc biệt như @, #, $, %, ^, &, \*, ., /, \\, {, }, \[, ], |, ), ( …

**Lưu ý:**

**Chú ý:**

* Một số client tools sẽ lỗi nếu tên container chứa các ký tự đặc biệt trên.
* Để làm việc với các containers (buckets) dùng giao thức S3, thì tên các containers này phải chứa các ký tự thường và số, không chứa ký tự in hoa, không chứa ký tự đặc biệt, không chứa khoảng trắng.
* Nếu request trả về mã code 201 thì bạn đã tạo thành công một container (trong ví dụ trên container được tạo thành công với tên "container\_name").
* Trong mỗi container bạn có thể upload nhiều object để lưu trữ (Object ở đây ví dụ như hình ảnh, file bất kì hoặc thư mục).&#x20;

**Tạo container dùng CURL thông qua RESTful API**

> curl -i -X PUT -H "X-Auth-Token: \<token>" \<storage url>/mycontainer
>
> curl -v -i -X PUT -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/new\_container](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/new_container)

#### 3. Tải lên object (object size < 5GB) <a href="#sudungswiftrestapi-3.tailenobject-objectsize-less-than-5gb" id="sudungswiftrestapi-3.tailenobject-objectsize-less-than-5gb"></a>

| Url          | /v1/{account}/{container}/{name\_object}                                                                      |                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| Method       | PUT                                                                                                           |                                     |
| Header       | X-Auth-Token                                                                                                  | Token được lấy từ "x-subject-token" |
| Content-Type | Chọn content-type phù hợp với object upload (Ví dụ: Content-Type: image/jpeg với file hình có định dạng jpg). |                                     |
| Body         | Binary file: choose file                                                                                      |                                     |

Ví dụ cụ thể:

| Url    | [https://vos-ss-lab-hcm-sw.vinadata.vn/v1/AUTH\_d6f0078021f4417989d6ba8ae4320dea/nameContainer/fileName.png](https://vos-ss-lab-hcm-sw.vinadata.vn/v1/AUTH_d6f0078021f4417989d6ba8ae4320dea/nameContainer/fileName.png)                    | fileName.png là tên của object, object này sẽ được lưu trong container "nameContainer" |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Method | PUT                                                                                                                                                                                                                                        | <p><br></p>                                                                            |
| Header | <p>X-Auth-Token: gAAAAABdAhsbpeT0CLQiUvTgX3TcVua8c7RLFIY074FlLvDWpGp06EV8SRCbuLGzSL5Q2AnfYogSWydNeZc5dWpRbTKxiwGXuP-wAoPPmIGvBctSkkwnhMF8UQXLBmwlIT43Mudc9ZuHgRLqlW1BT3OmhN9ugKTQHyzgCuzBmHqVgtXp6dRJYr0</p><p>Content-Type: image/png</p> | Với hình ảnh có định dạng file png tương ứng Content-Type: image/png                   |
| Body   | Binary file: choose file                                                                                                                                                                                                                   | Ví dụ trong postman: chọn body binary, rồi chọn file tương ứng với máy tính local.     |

**Tải lên object dùng CURL thông qua RESTful API**

> curl -i -T myobject -X PUT -H "X-Auth-Token: \<token>" \<storage url>/mycontainer/myobject
>
> curl -v -i --data-binary 50GB -X PUT -H "Content-Type:application/octet-stream" -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt)

#### 4. Tải lên object lớn (object size > 5GB) <a href="#sudungswiftrestapi-4.tailenobjectlon-objectsize-greater-than-5gb" id="sudungswiftrestapi-4.tailenobjectlon-objectsize-greater-than-5gb"></a>

| Url    | /v1/{account}/{container}/{name\_object}/{segment\_object\_name} |
| ------ | ---------------------------------------------------------------- |
| Method | POST                                                             |
| Header | X-Auth-Token                                                     |
| Body   | (Optional)                                                       |

* Trong đó:

\+ "container" là tên container.

\+ "name\_object" tên của object muốn lấy nằm trong container.

**Tải lên object lớn dùng CURL thông qua RESTful API**

Với các object có kích thước lớn (kích thước > 5GB) thì vStorage không hỗ trợ upload theo flow bình thường. Để có thể tải lên được những object này, cần phải thực hiện các bước sau:

* **Bước 1: Tạo segments container**

vStorage dùng container segments để lưu trữ danh sách tất cả các segment objects của mỗi large object. Do đó, trước khi upload một large cần phải tạo container nếu nó chưa tồn tại, nếu nó đã tồn tại trước đó, không cần phải tạo lại thêm lần nữa.

Tên container này có pattern \<container\_segments>

Ví dụ: container bạn muốn lưu trữ large object có tên là: _**\<mycontainer>**_ thì segments container của nó sẽ có tên là _**\<mycontainer\_segments>**_.

Để tạo container, vui lòng tham chiếu đến mục \<Create container>

* **Bước 2: Chia một large object thành những phần nhỏ hơn (segment a large object into segment objects)**

Việc chia một large object thành những phần riêng biệt có thể dùng command line, client tool hoặc library.

Ví dụ: Upload object _**myobject**_ (10 GB), segment object _**myobject**_ này các segment objects:

* Ví dụ:
  * 00000001 (2GB)
  * 00000002 (2GB)
  * 00000003 (2GB)
  * 00000004 (2GB)
  * 00000005 (2GB)
* **Bước 3: Upload các phần này lên vStorage dùng RESTful API (uploads the segment objects using RESTful API)**

Việc upload các segment objects như upload các small objects dùng Postman, CURL hay bất kỳ client tool, library nào hỗ trợ upload file thông qua HTTP. Sau khi upload từng segment object lên vStorage, response trả về sẽ gồm giá trị Etag, giá trị này được dùng tạo nội dung Json cho manifest.

Ví dụ: Upload các segment objects của Object _**myobject**_ dùng CURL:

> curl -X PUT -H 'X-Auth-Token: \<token>'
>
> http://\<storage\_url>/container/myobject/00000001 --data-binary '00000001'
>
> \=> ETAG:  etagoftheobjectsegment1
>
> curl -X PUT -H 'X-Auth-Token: \<token>'         http://\<storage\_url>/container/myobject/00000002 --data-binary '00000002'
>
> \=> ETAG:  etagoftheobjectsegment2
>
> curl -X PUT -H 'X-Auth-Token: \<token>'         http://\<storage\_url>/container/myobject/00000003 --data-binary '00000003'
>
> \=> ETAG:  etagoftheobjectsegment3
>
> curl -X PUT -H 'X-Auth-Token: \<token>'         http://\<storage\_url>/container/myobject/00000004 --data-binary '00000004'
>
> \=> ETAG:  etagoftheobjectsegment4
>
> curl -X PUT -H 'X-Auth-Token: \<token>'         http://\<storage\_url>/container/myobject/00000005 --data-binary '00000005'
>
> \=> ETAG:  etagoftheobjectsegment5

* **Bước 4: Tạo nội dung Json cho manifest (build manifest content)**

Nội dung của manifest là một chuỗi Json với các keys sau:

| **Key**     | **Description**                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path        | Đường dẫn lưu trữ của segment (the path to the segment object (not including account) /container/object\_name)                                                 |
| etag        | Giá trị checksum của segment object, được trả về sau khi upload thành công 1 segment object lên vStorage (the ETag given back when the segment object was PUT) |
| size\_bytes | Kích thước của mỗi segment object với đơn vị bytes (the size of the complete segment object in bytes)                                                          |

Ví dụ: Tạo nội dung Json cho manifest cho object _**myobject**_:

> \[{"path": "/container/myobject/00000001", "etag": "etagoftheobjectsegment1", "size\_bytes": 2000000000}, {"path": /container/myobject/00000001", "etag": "etagoftheobjectsegment2", "size\_bytes": 2000000000},{"path": /container/myobject/00000003", "etag": "etagoftheobjectsegment3", "size\_bytes": 2000000000},{"path": /container/myobject/00000004", "etag": "etagoftheobjectsegment4", "size\_bytes": 2000000000},{"path": /container/myobject/00000005", "etag": "etagoftheobjectsegment5", "size\_bytes": 2000000000}]

* **Bước 5: Upload nội dung Json của manifest lên vStorage (upload the manifest content in Json form)**

Việc upload nội dung manifest như upload bất kỳ một textjson content nào khác lên vStorage dùng Postman, CURL hay bất kỳ client tool, library.

> curl -i -X PUT -H "X-Auth-Token: ${\<token>}" ${\<storage url>}/mybigfilescontainer/file?multipart-manifest=put -d '\[{"path": "/container/myobject/00000001", "etag": "etagoftheobjectsegment1", "size\_bytes": 2000000000}, {"path": /container/myobject/00000001", "etag": "etagoftheobjectsegment2", "size\_bytes": 2000000000},{"path": /container/myobject/00000003", "etag": "etagoftheobjectsegment3", "size\_bytes": 2000000000},{"path": /container/myobject/00000004", "etag": "etagoftheobjectsegment4", "size\_bytes": 2000000000},{"path": /container/myobject/00000005", "etag": "etagoftheobjectsegment5", "size\_bytes": 2000000000}]'

**Ví dụ thực tế về upload một large object:**

Upload một large object có kích thước là 10 GB với đường dẫn sau _**\</home/hientt5/large\_file/largefile>**_ đến container _**\<mybigfilecontainer>**_

* **Bước 1: Tạo segments container**

> curl -i -X PUT -H "x-auth-token: ${\<token>}" ${\<storage url>}/mybigfilescontainer\_segments

* **Bước 2: Chia \</home/hientt5/large\_file/largefile> thành nhiều segment objects dùng command line split**

> split -b 40000 /home/hientt5/large\_file/largefile
>
> Lệnh split sẽ segment file _**\</home/hientt5/large\_file/largefile>**_ thành những segment objects sau:
>
> -rw-r--r-- 1 ron ron 100000000 apr 24 18:21 file
>
> -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xaa
>
> -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xab
>
> -rw-r--r-- 1 ron ron  20000000 apr 24 18:39 xac

* **Bước 3: Upload những segment objects trên lên vStorage**

> curl -i -X PUT -H "x-auth-token: ${\<token>}" ${\<storage url>}/mybigfilescontainer\_segments/xaa --data-binary @xaa
>
> \=> ETAG:  48e9a108a3ec623652e7988af2f88867
>
> curl -i -X PUT -H "x-auth-token: ${\<token>}" ${\<storage url>}/mybigfilescontainer\_segments/xab --data-binary @xab
>
> \=> ETAG:  48e9a108a3ec623652e7988af2f88867
>
> curl -i -X PUT -H "x-auth-token: ${\<token>}" ${\<storage url>}/mybigfilescontainer\_segments/xac --data-binary @xac
>
> \=> ETAG:  10e4462c9d0b08e7f0b304c4fbfeafa3

* **Bước 4: Tạo nội dung Json cho manifest**

> Tạo nội dung Json của manifest như sau:
>
> \[{"path":"/mybigfilescontainer\_segments/xaa",
>
> &#x20; "etag":"48e9a108a3ec623652e7988af2f88867",
>
> &#x20; "size\_bytes":4000000000},
>
> &#x20;{"path":"/mybigfilescontainer\_segments/xab",
>
> &#x20; "etag":"48e9a108a3ec623652e7988af2f88867",
>
> &#x20; "size\_bytes":4000000000},
>
> &#x20;{"path":"/mybigfilescontainer\_segments/xac",
>
> &#x20; "etag":"10e4462c9d0b08e7f0b304c4fbfeafa3",
>
> &#x20; "size\_bytes":2000000000}]

* **Bước 5: Upload nội dung Json của manifest lên vStorage**

> curl -i -X PUT -H "X-Auth-Token: ${\<token>}" ${\<storage url>}/mybigfilescontainer/file?multipart-manifest=put -d '\[{"path":"/mybigfilescontainer\_segments/xaa",
>
> &#x20; "etag":"48e9a108a3ec623652e7988af2f88867",
>
> &#x20; "size\_bytes":4000000000},
>
> &#x20;{"path":"/mybigfilescontainer\_segments/xab",
>
> &#x20; "etag":"48e9a108a3ec623652e7988af2f88867",
>
> &#x20; "size\_bytes":4000000000},
>
> &#x20;{"path":"/mybigfilescontainer\_segments/xac",
>
> &#x20; "etag":"10e4462c9d0b08e7f0b304c4fbfeafa3",
>
> &#x20; "size\_bytes":2000000000}]'

* **Upload large object dùng Swift client tool**

Việc upload một large object dùng Swift client tool rất đơn giản, về cơ bản, client tool này sẽ hỗ trợ tất cả các bước trên, người dùng chỉ cần truyền vào thông tin token để chứng thực, đường dẫn large object và kích thước của từng segment object.

> Ví dụ: swift --os-auth-url [https://api.example.com/v3](https://api.example.com/v3) --auth-version 3\\
>
> &#x20;   \--os-project-name project1 --os-project-domain-name domain1 \\
>
> &#x20;   \--os-username user --os-user-domain-name domain1 \\
>
> &#x20;   \--os-password password upload test\_container -S 1073741824 large\_file

#### 5. Lấy object <a href="#sudungswiftrestapi-5.layobject" id="sudungswiftrestapi-5.layobject"></a>

| Url    | /v1/{account}/{container}/{name\_object} |
| ------ | ---------------------------------------- |
| Method | Get                                      |
| Header | X-Auth-Token                             |
| Body   | (Optional)                               |

* Trong đó:

\+ "container" là tên container.

\+ "name\_object" tên của object muốn lấy nằm trong container.

**Lấy object dùng CURL thông qua RESTful API**

> curl -i -X GET -H "X-Auth-Token: \<token>" \<storage url>/mycontainer/myobject
>
> curl -v -i -X GET -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt)

#### 6. Lấy object lớn <a href="#sudungswiftrestapi-6.layobjectlon" id="sudungswiftrestapi-6.layobjectlon"></a>

| Url    | /v1/{account}/{container}/{name\_object} |
| ------ | ---------------------------------------- |
| Method | Get                                      |
| Header | X-Auth-Token                             |
| Body   | (Optional)                               |

* Trong đó:

\+ "container" là tên container.

\+ "name\_object" tên của object muốn lấy nằm trong container.

**Lấy object lớn dùng CURL thông qua RESTful API**

> curl -i -X GET -H "X-Auth-Token: \<token>" \<storage url>/mycontainer/myobject?multipart-manifest=get
>
> curl -v -i -X GET -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt?multipart-manifest=get](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt?multipart-manifest=get)

#### 7. Xóa object lớn <a href="#sudungswiftrestapi-7.xoaobjectlon" id="sudungswiftrestapi-7.xoaobjectlon"></a>

| Url    | /v1/{account}/{container}/{name\_object}?multipart-manifest=delete |
| ------ | ------------------------------------------------------------------ |
| Method | Delete                                                             |
| Header | X-Auth-Token                                                       |
| Body   | (Optional)                                                         |

* Trong đó:

\+ "container" là tên container.

\+ "name\_object" tên của object muốn lấy nằm trong container.

**Xóa object lớn dùng CURL thông qua RESTful API**

> curl -i -X DELETE -H "X-Auth-Token: \<token>" \<storage url>/mycontainer/myobject?multipart-manifest=delete
>
> curl -v -i -X GET -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt?multipart-manifest=delete](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt?multipart-manifest=delete)

#### 8. Xóa object <a href="#sudungswiftrestapi-8.xoaobject" id="sudungswiftrestapi-8.xoaobject"></a>

| Url    | /v1/{account}/{container}/{name\_object} |
| ------ | ---------------------------------------- |
| Method | Delete                                   |
| Header | X-Auth-Token                             |
| Body   | (Optional)                               |

* Trong đó:

\+ "container" là tên container.

\+ "name\_object" tên của object muốn xóa nằm trong container.

**Xóa object dùng CURL thông qua RESTful API**

> curl -i -X DELETE -H "X-Auth-Token: \<token>" \<storage url>/mycontainer/myobject
>
> curl -v -i -X DELETE -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt)

#### 9. Sao chép object <a href="#sudungswiftrestapi-9.saochepobject" id="sudungswiftrestapi-9.saochepobject"></a>

| Url         | /v1/{account}/{container}/{name\_object} |
| ----------- | ---------------------------------------- |
| Method      | COPY                                     |
| Header      | X-Auth-Token                             |
| Destination | {dest\_container}/{name\_object}         |
| Body        | (Optional)                               |

* Trong đó:

\+ "container" là tên container.

\+ "name\_object" tên của object muốn copy nằm trong container.

\+ “dest\_container” tên của destination container

**Lấy object dùng CURL thông qua RESTful API**

> curl -i -X COPY -H "X-Auth-Token: \<token>" -H "Destination: anothercontainer/myobject" \<storage url>/mycontainer/myobject
>
> curl -v -i -X COPY -H "Destination: lifecycle/test.txt"  -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt)

#### 10. Xóa container <a href="#sudungswiftrestapi-10.xoacontainer" id="sudungswiftrestapi-10.xoacontainer"></a>

| Url    | /v1/{account}/{container} |
| ------ | ------------------------- |
| Method | Delete                    |
| Header | X-Auth-Token              |
| Body   | (Optional)                |

* Trong đó:

\+ "container" là tên container cần được xóa.

**Xóa container dùng CURL thông qua RESTful API**

> curl -s -S -X DELETE -H "X-Auth-Token: \<token>" \<storage url>/mycontainer
>
> curl -v -i -X DELETE -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle)

#### 11. Đổi tên object <a href="#sudungswiftrestapi-11.doitenobject" id="sudungswiftrestapi-11.doitenobject"></a>

| Url    | /v1/{account}/{container}/{name\_object} |
| ------ | ---------------------------------------- |
| Method | COPY and DELETE                          |
| Header | X-Auth-Token                             |
| Body   | (Optional)                               |

* Trong đó:

\+ "container" là tên container chứa đối tượng cần rename.

\+ “name\_object” là tên của đối tượng cần được rename.

* Để rename một object, cần thực hiện hai bước sau:

\+ Copy object đó với tên mới

\+ Xóa object cũ

**Rename object dùng CURL thông qua RESTful API**

> curl -i -X COPY -H "X-Auth-Token: \<token>" -H "Destination: anothercontainer/new\_myobject" \<storage url>/mycontainer/myobject
>
> curl -i -X DELETE -H "X-Auth-Token: \<token>" \<storage url>/mycontainer/myobject
>
> curl -v -i -X COPY -H "Destination: lifecycle/new\_test.txt"  -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt)
>
> curl -v -i -X DELETE -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle/test.txt](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle/test.txt)

#### 12. Liệt kê các container của một tài khoản <a href="#sudungswiftrestapi-12.lietkecaccontainercuamottaikhoan" id="sudungswiftrestapi-12.lietkecaccontainercuamottaikhoan"></a>

| Url    | /v1/{account} |
| ------ | ------------- |
| Method | GET           |
| Header | X-Auth-Token  |
| Body   | (Optional)    |

* Trong đó:

\+ "account" là tên hoặc ID của account cần liệt kê danh sách containers.

**List containers dùng CURL thông qua RESTful API**

> curl -s -S -X GET -H "X-Auth-Token: \<token>" \<storage url>
>
> curl -v -i -X GET -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399)

#### 13. Liệt kê nội dung của một container <a href="#sudungswiftrestapi-13.lietkenoidungcuamotcontainer" id="sudungswiftrestapi-13.lietkenoidungcuamotcontainer"></a>

| Url    | /v1/{account}/{container} |
| ------ | ------------------------- |
| Method | GET                       |
| Header | X-Auth-Token              |
| Body   | (Optional)                |

* Trong đó:

\+ "account" là tên hoặc ID của account cần liệt kê danh sách containers.

\+ "container" là tên của container cần liệt kê nội dung.

**List contents dùng CURL thông qua RESTful API**

> curl -s -S -X GET -H "X-Auth-Token: \<token>" \<storage url>/mycontainer
>
> curl -v -i -X GET -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle)

#### 14. Lấy tempURL của một object <a href="#sudungswiftrestapi-14.laytempurlcuamotobject" id="sudungswiftrestapi-14.laytempurlcuamotobject"></a>

| Url    | /v1/{account}/{container}/{name\_object} |
| ------ | ---------------------------------------- |
| Method | GET                                      |
| Header | X-Auth-Token                             |
| Body   | (Optional)                               |

* Trong đó:

\+ "account" là tên hoặc ID của account cần liệt kê danh sách containers.

\+ "container" là tên của container cần liệt kê nội dung.

\+ “name\_object” là tên đối tượng cần tạo tempurl.

* Để tạo một tempurl của một object, cần thực hiện các bước sau:

\+ Lấy về secret key của container chứa object đó.

\+ Tạo tempurl dựa trên secret key đó.

**Get secret key từ giá trị của field&#x20;**_**X-Account-Meta-Temp-URL-Key**_**&#x20;của meta-data của container dùng CURL thông qua RESTful API**

> curl -s -S -X GET -H "X-Auth-Token: \<token>" \<storage url>/mycontainer
>
> curl -v -i -X GET -H "X-Auth-Token: gAAAAABdQQ8uIM6CWmA85hKi6MtOvuGP1qok8OJzp0-h74QAn9ptncjT16sg0pxxilUSCPgFeb9NKpNfmkD9kDLYRAPkymOB9wlNWNTkiz20m2uZpCeTIDUpPMO110rSXBMaE8Gszq9BLiKFyuHVmTEKeyoQ3qEFxitXilEwIg201IRtbJFiCa0" \\
>
> [https://\<vStorage endpoint>/v1/AUTH\_a5bf65ca71594d85a60dc73cf9fc8399/test\_lifecycle](https://sw-hcm-1.vinadata.vn/v1/AUTH_a5bf65ca71594d85a60dc73cf9fc8399/test_lifecycle)

**Tạo tempurl dùng script sau**

> \#!/bin/bash
>
> seconds=\<number of seconds until url expires>
>
> method=GET
>
> expires=$(( $(date '+%s') + $seconds ))
>
> path='\<container>/\<object>'
>
> fullpath=\`echo $OS\_STORAGE\_URL | sed 's/http.\*\\/v1/\\/v1/'\`"/"$path
>
> key=${secret\_key}
>
> sig=\`printf '%s\n%s\n%s' $method $expires $fullpath  | openssl sha1 -hmac $key | awk '{print $2}'\`
>
> \# print the URL
>
> echo "${OS\_STORAGE\_URL}/${path}?temp\_url\_sig=${sig}\&temp\_url\_expires=$
>
> {expires}"

#### 15. Tạo thư mục mới ở một container cụ thể <a href="#sudungswiftrestapi-15.taothumucmoiomotcontainercuthe" id="sudungswiftrestapi-15.taothumucmoiomotcontainercuthe"></a>

| Url    | /v1/{account}/{container}/{new\_folder} |
| ------ | --------------------------------------- |
| Method | PUT                                     |
| Header | X-Auth-Token                            |
| Body   | (Optional)                              |

* Trong đó:

\+ "account" là tên hoặc ID của account cần liệt kê danh sách containers.

\+ "container" là tên của container cần liệt kê nội dung.

\+ “new\_folder” là tên của thư mục mới cần tạo.

**Tạo thư mục mới dùng CURL thông qua RESTful API**

> curl -s -S -X PUT -H "X-Auth-Token: \<token>" -H “Content-Length: 0” -H “Content-Type: application/directory” \<storage url>/mycontainer/newfolder
>
> curl -X PUT -i [https://\<vStorage endpoint>/v1/AUTH\_f0a1d142185e4f8dae22ae67764d099b/syncdata1/newfolder/](https://sw-hcm-1.vinadata.vn/v1/AUTH_f0a1d142185e4f8dae22ae67764d099b/syncdata1/newfolder/) -H "Content-Length:0" -H "Content-Type:application/directory" -H "X-Auth-Token: gAAAAABfKhbKq-9EVUhbSjPMJEMiPh7yJ0fXCZ33\_\_J1dIQJaN58UPWKg96mAx9VGp3X7H-LyJhT0S5bN4dqKOCPERRQ8zw2Mo0zVRxlOG861vEWGKR1vkMbykAWTETa8cMnrXK6W2LYXkCpefJw75Q62UDIt1dmjT7WidpnICowW26FKp7B9WM"
