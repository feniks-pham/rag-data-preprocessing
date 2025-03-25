# Tải lên tệp tin

Object là đối tượng lưu trữ dữ liệu gốc và thông tin metadata của tệp tin được tải lên trên hệ thống vStorage. Bạn có thể sử dụng vStorage Portal, vStorage API hoặc 3rd party softwares để thực hiện tải tệp tin lên container, chi tiết được chúng tôi mô tả bên dưới.



<details>

<summary>Sử dụng vStorage Portal</summary>

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **container** bạn muốn thực hiện tải lên tệp tin. Nếu bạn muốn tải lên tệp tin vào một directory, hãy chọn vào directory đó.

3\. Chọn **Tải lên.**

Màn hình tải lên object được hiển thị.

4\. Lúc này, bạn có thể tải lên tệp tin bằng hai cách:&#x20;

* Kéo các tệp tin từ thiết bị của bạn vào khu vực chứa tệp tin để tải lên.
* Chọn **Chọn tệp tin để tải lên** sau đó chọn tệp tin cần tải lên từ thiết bị của bạn.

5\. Chọn **Open**.

6\. Chọn **Tải lên**.

Lúc này, các tệp tin của bạn đang được hệ thống tải lên, trạng thái của các tệp tin lúc này là Đang tải lên. Khi trạng thái này chuyển thành **Thành công** nghĩa là tệp tin của bạn đã được tải lên thành công.

Trong thời gian object đang được tải lên, bạn không thể thực hiện các hành động khác tới container. Khi việc tải lên object hoàn thành, bạn có thể tiếp tục sử dụng các tính năng khác bình thường.&#x20;

Tất cả dữ liệu do bạn tải lên đều thuộc sở hữu của bạn, VNG Cloud sẽ không thể can thiệp hay khôi phục dữ liệu khi bị xóa hay ghi đè bởi lỗi người dùng. Để tránh các các sự cố về ghi đè hay xóa nhầm chúng tôi khuyến khích bạn nên sao lưu phiên bản container (tính năng versioning) để bảo vệ dữ liệu. Để xem chi tiết tính năng versioning, hãy xem [Sử dụng tính năng container versioning](../lam-viec-voi-container/su-dung-tinh-nang-container-versioning.md).

<img src="../../../../../.gitbook/assets/Tai_len_tep_tin (1).gif" alt="" data-size="original">

</details>

&#x20;

