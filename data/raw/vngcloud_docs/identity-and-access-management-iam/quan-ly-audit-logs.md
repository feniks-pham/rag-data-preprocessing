# Quản lý Audit Logs

Cloud Audit Logs là tính năng ghi lại tất cả các hoạt động quản trị và truy cập trên tài nguyên VNG Cloud của bạn. Audit Logs sẽ giúp bạn trả lời những câu hỏi: "**Ai đã làm gì, nơi nào và khi nào?**"  trên các tài nguyên VNG Cloud cùng với mức độ minh bạch như trên môi trường On-premise của bạn. Việc bật tính năng Audit Logs sẽ giúp bạn theo dõi, rà soát và đảm bảo bảo mật cho các tài nguyên trên VNG Cloud.

#### **1. Các loại Audit Logs** <a href="#auditlogs-1.cacloaiauditlogs" id="auditlogs-1.cacloaiauditlogs"></a>

Cloud Audit Logs cung cấp các loại Audit Logs như bên dưới đây, tuỳ vào các products hay services mà sẽ hỗ trợ loại audit logs nào:

* **Admin Activity Audit Logs**: chứa tất cả các logs cho những hành động mà thay đổi tài nguyên (Create, Update, Delete) trên VNG Cloud. Ví dụ như là: những logs khi người dùng tạo vServer hay xoá security group. Gọi tắt là **ADMIN\_WRITE**
* **Data Access Audit Logs** (coming soon): chứa tất cả các logs cho những hành động mà đọc thông tin cấu hình của tài nguyên, cũng như những hành động mà tạo, xoá, sửa và đọc dữ liệu của tài nguyên. Dữ liệu của tài nguyên là những dữ liệu của người dùng đưa lên trên VNG Cloud, ví dụ như là các object của vStorage. Cụ thể chia 3 loại như bên dưới:&#x20;
  * **ADMIN\_READ**: hành động đọc thông tin cấu hình của tài nguyên. Ví dụ như là: liệt kê danh sách vServer hay xem chi tiết một vServer
  * **DATA\_WRITE**: hành động tạo, xoá, sửa dữ liệu của tài nguyên. Ví dụ như là: tải object lên vStorage hay là xoá object trên vStorage
  * **DATA\_READ**: hành động đọc dữ liệu của tài nguyên. Ví dụ như là: liệt kê danh sách objects của vStorage
* **System Event Audit Logs**: chứa tất cả các logs cho những hành động mà thay đổi tài nguyên trên VNG Cloud; tuy nhiên nó là những hành động mà được tạo ra bởi VNG Cloud systems, mà không phải được thực hiện trực tiếp từ người dùng. Ví dụ những dòng logs khi VNG Cloud systems tự động mở rộng (autoscale) node group của vContainer, hay những hành động tự động tạo bản daily backup cho vDB. Gọi tắt là **SYSTEM\_EVENT**
* **Policy Denied Audit Logs** (coming soon): chứa tất cả các logs khi mà VNG Cloud products/services từ chối truy cập của IAM user account hay service accounts bởi vì vi phạm các Policy. Gọi tắt là **POLICY\_DENIED**

#### **2. Danh sách các Products/Services hỗ trợ các loại Audit Logs** <a href="#auditlogs-2.danhsachcacproducts-serviceshotrocacloaiauditlogs" id="auditlogs-2.danhsachcacproducts-serviceshotrocacloaiauditlogs"></a>

<table data-header-hidden><thead><tr><th width="154"></th><th width="127"></th><th width="137"></th><th width="134"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Products/Service Name</td><td>Admin Activity Audit Logs</td><td>Data Access Audit Logs<br><br></td><td>System Event Audit Logs</td><td>Policy Denied Audit Logs</td><td></td><td></td></tr><tr><td>ADMIN_WRITE</td><td>ADMIN_READ</td><td>DATA_WRITE</td><td>DATA_READ</td><td>SYSTEM_EVENT</td><td>POLICY_DENIED</td><td></td></tr><tr><td>vServer</td><td>YES</td><td><strong>COMING SOON</strong></td><td>N/A</td><td>N/A</td><td>N/A</td><td>COMING SOON</td></tr><tr><td>vLB</td><td>YES</td><td>COMING SOON</td><td>N/A</td><td>N/A</td><td>N/A</td><td>COMING SOON</td></tr><tr><td>vDB</td><td>COMING SOON</td><td>COMING SOON</td><td>N/A</td><td>N/A</td><td>COMING SOON</td><td>COMING SOON</td></tr><tr><td>vContainer</td><td>YES</td><td>COMING SOON</td><td>N/A</td><td>N/A</td><td>YES</td><td>COMING SOON</td></tr><tr><td>vMonitor</td><td>YES</td><td>COMING SOON</td><td>N/A</td><td>N/A</td><td>N/A</td><td>COMING SOON</td></tr><tr><td>vStorage</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>N/A</td><td>COMING SOON</td></tr></tbody></table>

* **Ý nghĩa các trạng thái**

YES : đã hỗ trợ đầy đủ loại audit logs này

PARTIAL YES :  đã hỗ trợ nhưng chưa đầy đủ&#x20;

COMING SOON : có loại audit logs này và sẽ hỗ trợ sắp tới

N/A : không hỗ trợ loại audit logs này

#### **3. Kích hoạt Audit Logs** <a href="#auditlogs-3.kichhoatauditlogs" id="auditlogs-3.kichhoatauditlogs"></a>

Mặc định VNG Cloud sẽ không bật sẵn tính năng Audit Logs, khách hàng cần thực hiện các bước dưới đây để kích hoạt:

1. Truy cập vào trang Audit Logs của IAM Portal: [https://hcm-3.console.vngcloud.vn/iam/audit-logs](https://hcm-3.console.vngcloud.vn/iam/audit-logs)
2. Chọn **Set default configuration,** popup thiết lập sẽ hiển thị cho phép bạn chọn bật ADMIN\_WRITE hay SYSTEM\_EVENT
3. Chọn kích hoạt bật loại audit logs ADMIN\_WRITE hay SYSTEM\_EVENT mà bạn mong muốn
4. Nhấn nút **Save** để kích hoạt

Ví dụ bạn chọn cả 2 loại Audit Logs đang được hỗ trợ, bạn sẽ thấy màn hình như bên dưới, đối với 2 loại ADMIN\_WRITE và SYSTEM\_EVENT khi được kích hoạt sẽ áp dụng cho tất cả product/services đang được hỗ trợ theo như bảng trên

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806595/image2023-6-19_17-31-59.png?version=1&#x26;modificationDate=1690877516000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Khi đã kích hoạt Audit Logs, hệ thống sẽ bắt đầu lưu các Audit Logs kể từ thời điểm kích hoạt (không có quá khứ), và tự động tạo **Log Project: required** bên phía **vMonitor Logs** để lưu trữ, **Log Project: required** sẽ hoàn toàn miễn phí và lưu trữ các Audit Logs trong vòng **90 ngày**. Đồng thời khi đã kích hoạt 2 loại Audit Logs: ADMIN\_WRITE VÀ SYSTEM\_EVENT, thì bạn sẽ không thể tắt tính năng này đi, hệ thống sẽ luôn luôn lưu trữ tất cả hành động thuộc 2 loại Audit Logs này.

#### **4. Xem các Audit Logs đã kích hoạt** <a href="#auditlogs-4.xemcacauditlogsdakichhoat" id="auditlogs-4.xemcacauditlogsdakichhoat"></a>

Để xem các Audit Logs đã kích hoạt, bạn cần làm theo các hướng dẫn sau:

1. Truy cập mục Log Search của vMonitor Logs: [https://hcm-3.console.vngcloud.vn/vmonitor/log/search](https://hcm-3.console.vngcloud.vn/vmonitor/log/search)
2. Chọn **Log Project: required** để xem các Audit Logs đã được lưu trữ. Ví dụ như hình dưới đây là hành động 1 root user account tạo Security Group thuộc vServer tại thời điểm 19/06/2023 17:51:57 đã được ghi nhận lại.

<figure><img src="https://docs.vngcloud.vn/download/attachments/59806595/image2023-6-19_18-8-35.png?version=1&#x26;modificationDate=1690877516000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\


#### **3. Cấu trúc và định dạng các Audit Logs** <a href="#auditlogs-3.cautrucvadinhdangcacauditlogs" id="auditlogs-3.cautrucvadinhdangcacauditlogs"></a>

Mỗi dòng Audit Logs sẽ có thể có các field như bên dưới

* **timestamp**: thời gian logs được sinh ra
* **logId**: UUID để phân biệt từng dòng log
* **source**: nơi sinh ra dòng log, và đặc tả rõ đó là loại logs gì, ví dụ nếu dòng logs được sinh ra từ audit logs và loại là ADMIN\_WRITE thì nội dung sẽ là source: cloud\_audit/admin\_write
* **serviceName**: thông tin sản phẩm/dịch vụ được theo dõi, ví dụ dòng Audit Logs này là của vServer thì nội dung sẽ là serviceName: vserver
* **resource**: thông tin chi tiết và cụ thể tài nguyên nào được theo dõi, sẽ gồm 2 fields con là: type và labels&#x20;
  * **type**: thông tin resource nào của product, ví dụ nếu là dòng logs liên quan server sẽ là type: vserver\_server
  * **labels**: tên và ID của resource hay các thông tin khác của resource
  * Ví dụ ở dưới là resource server của vServer có serverID: ins-b019f5d0-1234-41ba-1234-851f9ef39003

| <p><code>"resource":{</code><br><code>"labels":{</code><br><code>"serverVRN":"vserver::12345:server/ins-b019f5d0-1234-41ba-1234-851f9ef39003",</code><br><code>"serverId":"ins-b019f5d0-1234-41ba-1234-851f9ef39003"</code><br><code>},</code><br><code>"type":"vserver:server"</code><br><code>},</code></p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* **JsonPayload**: chứa thông tin cụ thể hành động là gì, ai đã tạo ra hành động này (root user account, IAM user account hay service account), request metadata và các request/response body nếu có. Ví dụ ở bên dưới bạn có thể thấy userType: root-user là root user account với ID: 12345 đang thực hiện hành động DeleteServer với server có ID: ins-b019f5d0-1234-41ba-1234-851f9ef39003

| <p><code>"jsonPayload":{</code><br><code>"authenticationInfo":{</code><br><code>"rootUserAccountId":12345,</code><br><code>"userType":"root-user"</code><br><code>},</code><br><code>"serviceName":"vserver"</code><br><code>"action":"vserver:DeleteServer",</code><br><code>"resource":"vserver::12345:server/ins-b019f5d0-1234-41ba-1234-851f9ef39003",</code><br><code>"request":{},</code><br><code>"requestMetadata":{},</code><br><code>"response":{}</code><br><code>},</code></p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

* &#x20;Với ví dụ bên dưới, bạn có thể thấy userType: iam-user là IAM user account có ID: e6d39955-e4c3-1234-1234-84d82ea554bf thuộc root user account có ID: 12345 đang thực hiện hành động SearchLogs với Log Project có ID: bbb5f6ef-1234-49a1-1234-b41332376fef. Tương tự với serviceAccount bạn cũng sẽ thấy userType: user-sa.

| <p><code>"jsonPayload":{</code><br><code>"authenticationInfo":{</code><br><code>"userType":"iam-user",</code><br><code>"rootUserAccountId":12345,</code><br><code>"userAccount":"e6d39955-e4c3-1234-1234-84d82ea554bf"</code><br><code>},</code><br><code>"serviceName":"vmonitor",</code><br><code>"action":"vmonitor:SearchLogs",</code><br><code>"resource":"vmonitor::12345:log-project/bbb5f6ef-1234-49a1-1234-b41332376fef",</code><br><code>"request":{},</code><br><code>"requestMetadata":{},</code><br><code>"response":{}</code><br><code>},</code></p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

* Ngoài ra bạn cũng có thể thấy thêm các thông tin về requestMetadata, request và response của hành động này (tuỳ vào loại action sẽ có hay không)

| <p><code>"jsonPayload":{</code><br><code>"authenticationInfo":{</code><br><code>"userType":"iam-user",</code><br><code>"rootUserAccountId":12345,</code><br><code>"userAccount":"e6d39955-e4c3-1234-1234-84d82ea554bf"</code><br><code>},</code><br><code>"serviceName":"vmonitor",</code><br><code>"action":"vmonitor:SearchLogs",</code><br><code>"resource":"vmonitor::12345:log-project/bbb5f6ef-1234-49a1-1234-b41332376fef",</code><br><code>"request":{</code><br><code>"method":"POST",</code><br><code>"path":"/v1/projects/bbb5f6ef-1234-49a1-1234-b41332376fef/search-logs",</code><br><code>"httpVersion":"HTTP/1.1"</code><br><code>},</code><br><code>"requestMetadata":{</code><br><code>"callerIp":"103.1.208.50",</code><br><code>"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"</code><br><code>},</code><br><code>"response":{</code><br><code>"duration":272,</code><br><code>"status":200</code><br><code>}</code><br><code>},</code></p> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
