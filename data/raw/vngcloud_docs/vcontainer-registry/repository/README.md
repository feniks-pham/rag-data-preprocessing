# Repository

#### Repository là gì? <a href="#repository-repositorylagi" id="repository-repositorylagi"></a>

Repository là một vị trí trung tâm nơi lưu trữ và quản lý các hình ảnh Docker. Nó hoạt động như một nơi lưu trữ các phiên bản (version) khác nhau của images, mỗi phiên bản được xác định bằng một thẻ (tag) duy nhất. Tùy thuộc vào cài đặt kiểm soát truy cập, Repository này có thể là công khai (public) hoặc riêng tư (private).

#### Tôi có thể làm gì với Repositories? <a href="#repository-toicothelamgivoirepositories" id="repository-toicothelamgivoirepositories"></a>

**TẠO MỘT REPOSITORY**

Để tạo một Repository, hãy nhấp vào nút "Tạo repository". Sau đó, bạn sẽ được yêu cầu điền các thông tin cần thiết như Repository name, Access level và Quota Limit. Tham khảo chi tiết tại Create Repository

**CHỈNH SỬA GIỚI HẠN DUNG LƯỢNG**

Để điều chỉnh giới hạn lưu trữ của Repository, đầu tiên, điều hướng đến màn hình danh sách Repository và tìm đến cột "Action". Nhấp vào biểu tượng "ba chấm" tại mỗi dòng Repository trong cột "Action" và chọn "Edit Quota Limit". Tham khảo thêm tại "Edit Quota Limit"

**QUẢN LÝ IMAGE**

Truy cập vào Repository và nhấp vào tab "Images" để xem danh sách image đang được lưu trữ tại Repository. Sau đó, truy cập vào image cụ thể để xem các thông tin chi tiết (artifacts và tags) và sao chép lệnh push/pull cho các artifacts/tags liên quan. Tham khảo chi tiết tại "Image Management"

**QUẢN LÝ REPOSITORY USER**

Xem danh sách Repository User được đính kèm bằng cách nhấp vào tab "Repository User" tại trang chi tiết Repository. Từ đây, bạn có thể nhanh chóng tạo, đính kèm hoặc gỡ đính kèm một Repository User.

* Với vai trò trong một private Repository, Repository User có thể push và pull các container images, đảm bảo truy cập an toàn đối với các images được quản lý tại Reposiotry.
* Tham khảo chi tiết tại Repository User

**XEM LỊCH SỬ**

Lịch sử truy cập của Repository giúp bạn theo dõi tất cả các hành động liên quan đến nó, bao gồm cả những hành động đối với Repository và Images liên quan. Tham khảo thêm tại Repository History.

#### Bài viết liên quan <a href="#repository-baivietlienquan" id="repository-baivietlienquan"></a>

* [Create Repository](cach-tao-repository.md)
* [Edit Quota Limit](cach-chinh-sua-quota-limit.md)
* [Image Management](cach-quan-ly-image.md)
* [Repository User](../cach-tao-repository-user/)
* [Repository History](xem-lich-su-repository-history.md)

\
