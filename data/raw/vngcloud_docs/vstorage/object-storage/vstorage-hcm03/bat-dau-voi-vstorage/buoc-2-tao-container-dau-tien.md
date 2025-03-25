# Bước 2: Tạo container đầu tiên

Trước khi có thể lưu trữ dữ liệu trong vStorage, bạn phải tạo 1 container. Container là đối tượng chứa dữ liệu (Object). Trong vStorage, có thể hiểu đối tượng này tương đương một thư mục trong hệ điều hành. Bạn có thể quản lý tệp và thư mục bằng các công cụ và API được cung cấp.

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list). Chọn **project** muốn thực hiện tạo **container.**
2. Chọn **Tạo một container.**
3. Nhập **Tên container** theo quy định của chúng tôi.
4. Chọn **Tạo mới.**

Khi tạo thành công một container, thì có các container segments được khởi tạo cùng với container gốc. Các large object khi được upload sẽ được phân ra thành nhiều segments để tải lên. Các segments này được lưu vào một trong các container segment trên tùy theo công cụ được sử dụng để upload large object. Trong khi đó, container gốc chứa một file manifest liên kết với nội dung của các segments. Tên của object segments được giữ nguyên hoặc mã hóa base64 tùy vào cách hành xử của công cụ phía người dùng dùng để tải lên. vStorage đang hỗ trợ 2 loại container segment với suffix: \_segments, +segments. Mỗi công cụ phía người dùng sẽ tương tác với mỗi loại container segment này tùy theo đặc tính riêng của từng công cụ.

_**Video hướng dẫn:**_



<figure><img src="../../../../.gitbook/assets/Khoi_tao_container (1).gif" alt=""><figcaption></figcaption></figure>
