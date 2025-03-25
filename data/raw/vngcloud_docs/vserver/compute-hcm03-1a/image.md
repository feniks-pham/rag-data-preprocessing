# Image

System Image là bản sao của các hệ điều hành phổ biến hiện nay trên thị trường và đang được VNG Cloud hỗ trợ và duy trì tương thích ở mức tốt nhất với hệ thống ảo hoá đang phát triển. System image cần phải được chỉ định trong quá trình khởi chạy một Server. Bạn có thể khởi chạy nhiều Server từ một System Image duy nhất khi bạn yêu cầu nhiều Server có cùng cấu hình. Sử dụng các System Image khác nhau để khởi chạy các Server khi bạn yêu cầu các Server có cấu hình khác nhau.

<figure><img src="../../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

Các image tại VNG Cloud được phân loại thành Image chung, Image riêng và Image từ Marketplace.

* VNG Cloud cung cấp các Image chung với các đảm bảo về tính bảo mật và ổn định. Các image chung này chủ yếu là các dòng có hệ điều hành Windows Server và Linux phổ biến
* Image riêng được tạo ra từ snapshot của máy chủ ảo khác hoặc được đưa lên từ khách hàng
* Image từ marketplace là các image có cài sẵn các loại phần mềm hoặc dịch vụ đã được kiểm chứng bởi VNG Cloud mang lại sự tiện lợi và nhanh chóng khi tạo máy chủ ảo mới

***

### **Làm việc với Image** <a href="#image-lamviecvoiimage" id="image-lamviecvoiimage"></a>

#### Tạo Image từ Server <a href="#image-taoimagetuserver" id="image-taoimagetuserver"></a>

Để tạo VPC, bạn cần thực hiện các bước sau:

1. Truy cập vào trang chủ vSer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview)
2. Tại thanh menu điều hướng, chọn Tab **"Server"**
3. Chọn Server cần tạo Image tại trang danh sách các Server hiện hữu, sau đó nhấn vào nút **"Action"** và chọn **"Create Image"**
4. Đợi 1 vài phút bạn và bạn có thể xem thông tin Image đã tạo ở tab **"Block Store"** mục Image\


#### Khởi tạo Server từ Image <a href="#image-khoitaoservertuimage" id="image-khoitaoservertuimage"></a>

1. Để khởi tạo vServer từ My image, bạn có thể xem hướng dẫn về [Khởi tạo vServe](trai-nghiem-san-pham-vserver/)r, khi đến bước **Chọn Boot Image**, ở mục "**Basic Configuration**", chọn Image để khởi tạo Server, bạn cần thực hiện theo _**Option 3**_: Khởi tạo vServer với **MY IMAGES** đã được tạo ra trước đó, nhằm phục vụ cho việc Clone Server đang chạy trên Cloud thành các Server mới hoặc Backup / Restore Server
2. Tại tab **MY IMAGES**, chọn images tương ứng cần để tạo vServer
3. Thực hiện tiếp các bước còn lại của hướng dẫn về Khởi tạo vServer để tạo ra Server hoàn chỉnh từ My image

\


Trang liên quan: Image Overview, Custom Image, Marketplace Image
