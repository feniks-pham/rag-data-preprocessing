# Cách quản lý Image

Truy cập vào Repository để quản lý các images tại đây với các tính năng như:

#### Xem danh sách Images <a href="#imagemanagement-xemdanhsachimages" id="imagemanagement-xemdanhsachimages"></a>

Tại màn hình danh sách Image, người dùng có thể xem danh sách Image với các thông tin như:

* **Image name:** Tên image
* **Artifact:** tổng số lượng Artifact tương ứng với Image.&#x20;
  * Giải thích thêm về Artifact: Khi tải lên cùng image đã có tại Repository, nếu Image có sự thay đổi lớn (ví dụ như thay đổi layer) thì sẽ tự động phát sinh một Artifact mới tương ứng với Image vừa Push lên với cùng Image name trước đó
* **Pull Count:** Tổng số lần Pull tính trên Image
* **Last Modified At:** Lần thực hiện Pull/Push gần nhất, tính trên Image

#### Xem chi tiết Image <a href="#imagemanagement-xemchitietimage" id="imagemanagement-xemchitietimage"></a>

Tại màn hình chi tiết Image, người dùng có thể xem danh sách Artifacts của Image với các thông tin như:

* **Artifacts:** ArtifactId tương ứng
* **Tag:** Danh sách tag tương ứng với 1 Artifact
* **Size:** Dung lượng image tương ứng với từng Artifact
* **Push Time**: Thời gian push gần nhất (ghi nhận khi có sự thay đổi về image tag/artifact)
* **Pull Time:** Thời gian pull gần nhất (tính trên Artifact)

#### Push (Tải lên) Image <a href="#imagemanagement-push-tailen-image" id="imagemanagement-push-tailen-image"></a>

**Cách Push image để lưu trữ tại Repository**

1. Mở docker/podman và đăng nhập với Repository User có quyền Push trên Repository lưu trữ image;
   * User name: Repository Name
   * Password: Repository User Secret Key
2. Truy cập vào vCR Console, nhấn vào Repository cần tải lên image, tại tab **"Image"**, nhấn vào **"Push Command"** để xem nhanh các lệnh cần thao tác.
3. Sao chép lệnh **"Tag an image for this project"** để đánh tag cho image cần push lên.&#x20;
4. Sao chép lệnh **"Push an image to this project"** để push image lên Repository.
5. Kiểm tra xem image đã được push lên thành công hay chưa tại tab "Image" tại trang chi tiết Reposiotry.

#### Pull (Tải về) Image <a href="#imagemanagement-pull-taive-image" id="imagemanagement-pull-taive-image"></a>

**Cách Pull image từ Repository**

1. Mở docker/podman và đăng nhập với Repository User có quyền Pull trên Repository lưu trữ image;
   * User name: Repository Name
   * Password: Repository User Secret Key
2. Truy cập vào vCR Console, nhấn vào Repository lưu trữ image cần tải, tại tab **"Image"**, truy cập vào Image chi tiết cần tải về.
3. Tại màn hình chi tiết Image, tại cột **Action**, nhấn vào biểu tượng "ba chấm" tại Image Artifact cần tải.
4. Một popup **"Copy pull command"** cho phép người dùng sao chép nhanh các lệnh pull tương ứng:
   * Pull theo Artifact: Mặc định tải về Image Artifact với tag gần nhất
   * Pull theo từng Artifact tag: Pull Image Artifact với từng tag cụ thể
