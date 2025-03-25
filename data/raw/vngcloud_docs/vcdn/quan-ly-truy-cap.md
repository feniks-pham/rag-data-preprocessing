# Quản lý truy cập

## Tổng quan

Hệ thống phân quyền thứ cấp cho phép khách hàng quản lý quyền truy cập và thao tác trên dịch vụ CDN một cách linh hoạt và chi tiết. Thông qua giao diện Portal của VNG Cloud, khách hàng có thể ủy quyền quản trị cho bất kỳ tài khoản nào đã tồn tại trên hệ thống với quyền hạn được tùy chỉnh.

## Chi tiết

1. **Loại tài khoản được ủy quyền**
   * Khách hàng có thể ủy quyền cho tài khoản Root User Account như là một IAM User Account của mình để thao tác với dịch vụ CDN của quý khách.
2. **Loại quyền cấp phát:**
   * **Full:** Toàn quyền, cho phép thực hiện tất cả các thao tác trên hệ thống CDN (cấu hình, quản lý, xóa, thêm mới, v.v.).
   * **Read Only:** Chỉ được phép xem thông tin và trạng thái của dịch vụ CDN, không thể thực hiện thay đổi.
   * **Deny:** Quyền mặc định, ngăn chặn mọi truy cập hoặc thao tác với hệ thống.
3. **Đối tượng được phân quyền:**
   * Phân quyền có thể được áp dụng lên từng loại đối tượng trên hệ thống CDN, bao gồm:
     * **Analytic Resources:**
       * Dashboard
       * Report
     * **Product Management:**
       * Web Accelerator
       * Live Entrypoint
       * Object Download
       * Live Streaming
       * Video On Demand
       * Certificate
       * Purge Cache
     * **System Management:**
       * Profile
       * API Key
       * Activity Logs

***

## **Quy trình thực hiện phân quyền**

**Bước 1:** Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)

**Bước 2:** Chọn mục **IAM**, sau đó chọn **Add new.**

**Bước 3:** Nhập địa chỉ email của tài khoản đã tồn tại trên hệ thống VNG Cloud.

**Bước 4:** Tại đối tượng cần phân quyền, chọn loại quyền hạn phù hợp với nhu cầu. Trong đó:&#x20;

* **Full:** Toàn quyền, cho phép thực hiện tất cả các thao tác trên hệ thống CDN (cấu hình, quản lý, xóa, thêm mới, v.v.).
* **Read Only:** Chỉ được phép xem thông tin và trạng thái của dịch vụ CDN, không thể thực hiện thay đổi.
* **Deny:** Quyền mặc định, ngăn chặn mọi truy cập hoặc thao tác với hệ thống.

**Bước 5:** Chọn **Save** để áp dụng các thay đổi.

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1).png" alt="" width="371"><figcaption></figcaption></figure>
