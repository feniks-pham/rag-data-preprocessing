# Tổng quan object

Bạn có thể bắt đầu với vStorage bằng cách làm việc với project, container và object. Một container là nơi chứa cho các object. Object là đối tượng lưu trữ dữ liệu gốc và thông tin metadata của tệp tin được tải lên trên hệ thống vStorage.

Để lưu trữ một object trong vStorage, bạn tạo một container rồi tải một tệp tin lên container đó. Tệp tin mới được tải lên này được lưu trữ bên trong container như một object. Khi object đó ở trong container, bạn có thể tải cùng một tệp tin lên container để ghi đè object (cập nhật object), tải xuống, sao chép, di chuyển hoặc thay đổi thiết thiết lập tag, metadata cho object đó. Khi bạn không còn cần một object hoặc một nhóm object, bạn có thể xóa để dọn sạch tài nguyên của mình trên vStorage.

Một object trong một container bao gồm các thông tin sau đây:

* **Thông tin chung**: tên, kích thước, content type, đường dẫn tới object.
* **Tag**: là một nhãn (label) gắn liền với một object với mục đích nhận dạng, phân loại hoặc cung cấp thêm thông tin khác liên quan đến object.
* **Metadata**: là thông tin về dữ liệu, bao gồm các thông tin như tên, địa chỉ, kích thước, ngày tạo ra và các thuộc tính khác. Nó có thể được sử dụng để giúp người dùng hiểu rõ hơn và truy cập dữ liệu mong muốn.
* **Checksum**: là một chuỗi các số và chữ cái có được thông qua quá trình tính toán từ dữ liệu gốc và metadata của một tệp tin nhằm mục đích phát hiện các lỗi có thể xảy ra trong quá trình truyền hoặc lưu trữ. Checksum thường được sử dụng để xác minh tính toàn vẹn của dữ liệu nhưng không được dựa vào để xác minh tính xác thực của dữ liệu.
* **Phiên bản**: là một từ được sử dụng để chỉ một phiên bản của một phần mềm, tài liệu. Version được chúng tôi sử dụng thông qua tính năng Versioning.
