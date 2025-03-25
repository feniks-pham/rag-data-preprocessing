# vStorage Swift REST API

#### Tổng quan <a href="#vstorageswiftrestapi-tongquan" id="vstorageswiftrestapi-tongquan"></a>

Trước tiên, vStorage là một dịch vụ lưu trữ dựa trên kiến trúc Object Storage. Vì vậy để am hiểu chi tiết về Object Storage API, vui lòng tham khảo: [https://developer.openstack.org/api-ref/object-store/?expanded=show-account-details-and-list-containers-detail,create-container-detail](https://developer.openstack.org/api-ref/object-store/?expanded=show-account-details-and-list-containers-detail,create-container-detail).

Từ đó, vStorage cung cấp Swift API cho phép các công ty, tổ chức hoặc người dùng khác để tích hợp với các ứng dụng, công cụ phía người dùng của mình với vStorage để lưu trữ dữ liệu như ảnh, video, tài liệu,...vStorage Swift API bao gồm các API để làm việc với project, làm việc với container, làm việc với object/ directory, ...

Tích hợp các ứng dụng, công cụ phía người dùng của bạn với vStorage bằng cách sử dụng vStorage Swift API sẽ giúp bạn lưu trữ và quản lý dữ liệu của mình trên vStorage. Đây là những gì bạn có thể làm:

* Lấy thông tin token xác thực.
* Làm việc với container: khởi tạo container.
* Làm việc với object: ví dụ tải lên/ tải xuống /đổi tên/sao chép/xóa đối tượng bằng tempURL.

Để giúp bạn có thể dễ dàng tích hợp cũng như trải nghiệm nhanh các vStorage Swift REST API, chúng tôi cung cấp một tính năng tích hợp thông qua vStorage Portal. Bạn chỉ cần cung cấp thông tin Region, Project, thông tin chứng thực (vStorage credentials) chính xác và sau đó bạn có thể xem thông tin cũng như trải nghiệm các vStorage Swift REST API ngày trên vStorage Portal. Sau khi đã truy cập được các tài nguyên (project, container, object, v.v.) của bạn trên dịch vụ vStorage, để làm việc với các tài nguyên này sử dụng vStorage Swift REST API, bạn có thể tham khảo tại [đây](https://vstorage.console.vngcloud.vn/assets/resources/vos-docx/vStorage-RESTFUL-API.pdf).

***

#### Chủ đề <a href="#vstorageswiftrestapi-chude" id="vstorageswiftrestapi-chude"></a>

* Tích hợp Swift Rest API
* Sử dụng Swift Rest API
