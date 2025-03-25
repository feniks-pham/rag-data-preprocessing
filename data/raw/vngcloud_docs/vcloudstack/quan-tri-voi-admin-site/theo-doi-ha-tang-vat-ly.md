# Theo dõi hạ tầng vật lý

## Tổng quan

Dịch vụ vCloudstack là dịch vụ triển khai cơ sở hạ tầng và chạy các dịch vụ VNG Cloud tại chỗ nên theo dõi tình trạng hoạt động của toàn bộ cơ sở hạ tầng vật lý được xem là quan trọng. vCloudStack cho phép người dùng trải nghiệm việc kiểm soát tình trạng hoạt động của hệ thống trong giao diện Portal Admin Site. Toàn bộ thông tin sẽ tường minh và rõ ràng, giúp người quản trị dễ dàng nắm bắt tình trạng của tất cả thiết bị vật lý để có thể đề ra phương án nâng cấp hoặc bảo trì hệ thống một cách kịp thời.

Bạn có thể tham khảo các các thông tin kiểm soát hạ tầng được mô tả bên dưới.

***

## Thông tin Compute

Giao diện Compute cho phép người quản trị có thể theo dõi thông số về Ram và CPU đang sử dụng của hạ tầng được ảo hóa.&#x20;

Để truy cập vào màn hình Compute, bạn truy cập vào vCloudStack Admin Site chọn vào mục Compute ở thanh điều khiển để được điều hướng tới màn hình Compute.

Các thông số chi tiết được hiển thị trong màn hình giao diện gồm:

* **Host:** Tên Host;
* **Status:** Trạng thái của Host ;
* **vCPUs:** Số CPU đã ảo hóa;
* **Ratio:** Tỷ lệ ảo hóa;
* **Running VMs:** số VM đang chạy;
* **vCPUs Used :** Số CPU đã dùng đề cấp phát cho VM sử dụng;
* **CPU Usage:** Chỉ số CPU cao nhất trong 30 phút gần nhất;
* **Free RAM (MB):** Dung lượng bộ nhớ Ram đang trống (chưa sử dụng)
* **Memory Usage:** Dung lượng bộ nhớ Ram đã sử dụng
* **Host IP:** Địa chỉ IP của Host
* **Processor Version:**  Phiên bản của CPU
* **Aggegate name:** Tên nhóm thuộc tính của Host

***

## Thông tin Storage

Màn hình hiển thị thông tin Storage, cho phép người quản trị có thể theo dõi tình trạng sử dụng của tất cả Cluster đang lưu trữ dữ liệu.&#x20;

Để truy cập vào màn hình Storage, bạn truy cập vào vCloudStack Admin Site chọn vào mục Storage ở thanh điều khiển để được điều hướng tới màn hình Storage.

Các thông tin hiển thị để theo dõi bao gồm:

* **Cluster:** Tên của Cluster;
* **Pool:** Tên Pool;
* **Images:** Tổng số Image;
* **Total Cloud:** Tổng dung lượng lưu trữ trên Cloud;
* **Used Cloud:** Dung lượng lưu trữ đã sử dụng tính theo đơn vị dung lương;
* **Used Cloud (%):** Dung lượng lưu trữ đã sử dụng tính theo %;
* **Avg volume size:** Dung lượng Volume trung bình;&#x20;
* **Free Cloud**: Dung lượng lưu trữ Cloud còn trống tính theo đơn vị dung lượng;
* **Free Cloud (%):** Dung lượng lưu trữ Cloud còn trống tính theo đơn vị  %;
* **Last report:** Lần cập nhật gần nhất;
* **Site name:** Tên Site;
* **Site code:** Mã định danh của Site này;
* **Location:**  Vị trí của Cluster này
* **Data center:** Tên trung tâm dữ liệu của Cluster này.

***

## Thông tin backup

Màn hình hiển thị thông tin Sao lưu dữ liệu, cho phép người quản trị có thể theo dõi tình trạng sao lưu backup của người dùng đã thực hiện đang lưu trữ trên vStorage.

Để truy cập vào màn hình Backup, bạn truy cập vào vCloudStack Admin Site chọn vào mục Backup ở thanhđiều khiển để được điều hướng tới màn hình Backup.

Các thông tin backup trên vStorage hiển thị để theo dõi bao gồm:

* **Các thông tin chung:**
  * **Users:** Số lượng User đang giữ bản backup;
  * **Total Backup Size:** Tổng size Dung lương các bản backup (volume ở trong server);
  * **Server Backups:** Tổng bản sao lưu Server;
  * **Volume Backups:** Tổng bản sao lưu Volume
* **Thông tin đặc thù:**
  * **Total Project:** Tổng số lượng project sao lưu vStorage;
  * **Total Project Size:** Tổng dung lượng sao lưu trên tất cả project;
  * **Protected Volume:** Số lượng volume đang được backup theo policy;
  * **Protected Server:** Số lượng Server đang được backup theo policy;



## Thông tin Network

Giao diện Network cho phép người quản trị có thể theo dõi các Network đã được tạo và ai đang được sử dụng khi tạo máy chủ ảo.&#x20;

Để truy cập vào màn hình Network, bạn truy cập vào vCloudStack Admin Site chọn vào mục Network ở thanh điều khiển để được điều hướng tới màn hình Network.

Các thông số chi tiết được hiển thị trong màn hình giao diện gồm:

* **Name**: Tên của network để nhận diện khi sử dụng
* **Status**: Trạng thái thông tin mạng có sẵn sàng để user sử dụng
* **ID:** Mã định danh mạng
* **Network type:** Phân bổ địa chỉ IP subnet và IP gateway (e.g: vlan, vxlan…);
* **Segment ID**: mã ID dựa theo loại mạng cấu hình;
* **Physical Network:** Thông tin Mạng vật lý (e.g: br0, vlan1, external\_network);
* **Share type/Owner:** Thông tin share cho tất cả user (All) hoặc chỉ cho Owner sử dụng (Private); Hiển thị email user Owner của network.

Để khởi tạo Network, bạn có thể tham khảo mục [Cấu hình Network](../bat-dau-voi-vcloudstack/cau-hinh-network.md).
