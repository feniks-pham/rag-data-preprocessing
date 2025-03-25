---
description: Về trang User site
---

# Tổng quan các tính năng

## Tổng quan <a href="#tong-quan" id="tong-quan"></a>

vCloudStack là dịch vụ đám mây hybrid được thiết kế quản lý và cho phép mở rộng cơ sở hạ tầng, dịch vụ, API của VNG Cloud đến cơ sở của khách hàng. Bằng cách cung cấp quyền truy cập cục bộ vào cơ sở hạ tầng do VNG Cloud quản lý. vCloudStack cho phép khách hàng xây dựng và vận hành các ứng dụng tại chỗ sử dụng cùng các giao diện lập trình như trong VNG Cloud, đồng thời sử dụng tài nguyên và lưu trữ cục bộ để làm giảm độ trễ và đáp ứng nhu cầu xử lý dữ liệu cục bộ.

Do đó, vCloudStack mang tính chất và tính năng cơ bản gần như giống với các tính năng dịch vụ mà vServer của VNG Cloud đang cung cấp.

***

## Các tính năng <a href="#cac-tinh-nang" id="cac-tinh-nang"></a>

Từ mô hình đám mây hybrid này, vCloudStack của VNG Cloud cung cấp các tính năng như sau mà bạn có thể sử dụng gồm:

### Server <a href="#server" id="server"></a>

* Khởi tạo máy chủ ảo (VM);
* Tạo máy chủ ảo từ file Backup;
* Tạo máy chủ ảo từ file Snapshot;
* Tạo máy chủ ảo từ file Image;
* Thay đổi kích thước máy chủ (Resize);
* Cập nhật Security Group cho Máy chủ ảo;
* Tắt/mở hoặc khởi động lại máy chủ ảo (Shutdown hoặc Start hoặc Reboot);
* Tạo Image từ máy chủ ảo;
* Tạo file backup từ máy chủ ảo;

### BlockStores <a href="#blockstores" id="blockstores"></a>

* Tạo ổ đĩa Volume (mã hóa hoặc không mã hóa);
* Phục hồi với file Snapshot;
* Mở rộng dung lượng Volume;
* Gán/gỡ hoặc xóa Volume (Attach/Deattach hoặc Delete)

### LoadBalancer <a href="#loadbalancer" id="loadbalancer"></a>

* Khởi tạo LB với loại Mạng hoặc loại Ứng dụng (Network hay Application)
* Tạo bộ listener trên LB đã tạo;
* Tạo Policy và Pool cho LB;
* Điều chỉnh cấu hình LB (Resize);
* Nhân đôi bộ LB mới;

