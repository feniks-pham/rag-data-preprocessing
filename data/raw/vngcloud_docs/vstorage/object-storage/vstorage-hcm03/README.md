# Object storage (HCM03, HAN01)

**Lưu trữ đối tượng** (hay còn gọi là **Object Storage**, **Cloud Storage**) là một hình thức lưu trữ dữ liệu dưới dạng các đơn vị riêng biệt gọi là **đối tượng (object)**. Mỗi đối tượng bao gồm dữ liệu thực tế (như hình ảnh, video, tệp) cùng với metadata cung cấp thông tin về đối tượng đó.

#### Lợi ích của Object Storage:

* **Hiệu quả về chi phí**:
  * Thường cung cấp chi phí thấp hơn so với các giải pháp lưu trữ truyền thống, đặc biệt đối với nhu cầu lưu trữ dữ liệu lớn.
* **Khả năng mở rộng**:
  * Dễ dàng mở rộng mà không cần cấu hình lại phức tạp hoặc ngừng hoạt động.
* **Metadata linh hoạt**:
  * Khả năng metadata phong phú tăng cường quản lý và truy xuất dữ liệu.
* **Độ bền cao**:
  * Độ bền và khả năng sẵn sàng cao nhờ vào các tính năng sao lưu và dự phòng dữ liệu.

***

## **Farm**

Farm là một thuật ngữ dùng riêng cho vStorage, farm được chúng tôi định nghĩa là một hệ thống bao gồm cơ sở hạ tầng, dịch vụ, v.v. được triển khai tại một vị trí cụ thể thuộc 2 region Hà Nội và Hồ Chí Minh với mục đích cung cấp dịch vụ lưu trữ vStorage. Đối với 2 farm HCM03, HAN01, các thông số cụ thể cho mỗi farm được chúng tôi cung cấp như sau:&#x20;

<table data-full-width="true"><thead><tr><th width="107.80000000000001">Farm</th><th width="200">Farm ID </th><th width="213">Authentication endpoint</th><th width="197">vStorage endpoint</th><th>Mục đích sử dụng</th></tr></thead><tbody><tr><td>HAN01</td><td>5d10c8ba-7187-4acc-b8c5-2d67d71c9233</td><td>https://han.auth.vstorage.vngcloud.vn/v3</td><td>https://han01.vstorage.vngcloud.vn</td><td>Farm phục vụ đa mục đích và được dùng chung cho dữ liệu khởi tạo project tại Region Hà Nội.</td></tr><tr><td>HCM03</td><td>8b1e9c9b-7123-54a5-ua8f-2d67d71c9212</td><td>https://hcm03.auth.vstorage.vngcloud.vn/v3</td><td>https://hcm03.vstorage.vngcloud.vn</td><td>Farm phục vụ đa mục đích và được dùng chung cho dữ liệu khởi tạo project tại Region Hồ Chí Minh.</td></tr><tr><td>HCM03</td><td>8b1e9c9b-7123-54a5-ua8f-2d67d71c9212</td><td>https://hcm03.auth.vstorage.vngcloud.vn/v3</td><td>https://hcm03-encrypt.vstorage.vngcloud.vn</td><td>Khi sử dụng encryption endpoint này, dữ liệu của bạn sẽ được tự động mã hóa khi tải tệp tin lên vStorage theo đúng chuẩn mã hóa AES-256.</td></tr></tbody></table>

Để biết thông tin cụ thể, vui lòng tham khảo tại [đây](vstorage-la-gi/farm-la-gi.md).

***

## Hạn mức tài nguyên

Các bảng sau đây liệt kê các giá trị tối đa cho tài nguyên lưu trữ trên vStorage của bạn.

### Bandwidth

<table data-full-width="true"><thead><tr><th width="113">Farm</th><th width="210">Download BW Domestic</th><th width="238">Download BW International</th><th width="198">Upload BW Domestic</th><th>Upload BW International</th></tr></thead><tbody><tr><td>HAN01</td><td>10Gbps shared</td><td>TBA</td><td>10Gbps shared</td><td>TBA</td></tr><tr><td>HCM03</td><td>10Gbps shared</td><td>TBA</td><td>10Gbps shared</td><td>TBA</td></tr></tbody></table>

### Request per limit

* Per IP

<table data-full-width="true"><thead><tr><th width="167">Storage Class</th><th width="232">Request all types</th><th width="283">Put request</th><th>Get request</th></tr></thead><tbody><tr><td>Gold</td><td>2500 request/s/IP</td><td>1000 request/s/IP</td><td>1500 request/s/IP</td></tr><tr><td>Silver</td><td>2500 request/s/IP</td><td>1000 request/s/IP</td><td>1500 request/s/IP</td></tr><tr><td>Archive</td><td>2500 request/s/IP</td><td>1000 request/s/IP</td><td>1500 request/s/IP</td></tr></tbody></table>

* Per path

<table data-full-width="true"><thead><tr><th width="171">Storage Class</th><th width="229">Request all types</th><th width="285">Put request</th><th>Get request</th></tr></thead><tbody><tr><td>Gold</td><td>2500 request/s/path</td><td>1000 request/s/path</td><td>1500 request/s/path</td></tr><tr><td>Silver</td><td>2500 request/s/path</td><td>1000 request/s/path</td><td>1500 request/s/path</td></tr><tr><td>Archive</td><td>2500 request/s/path</td><td>1000 request/s/path</td><td>1500 request/s/path</td></tr></tbody></table>

### Các hạn mức khác

<table data-full-width="true"><thead><tr><th>Item</th><th>Limit</th></tr></thead><tbody><tr><td>Số lượng object tối đa được lưu trữ trên một container</td><td>600 triệu objects</td></tr><tr><td>Số lượng container/ bucket tối đa có thể tạo trên một project</td><td>Không giới hạn</td></tr></tbody></table>
