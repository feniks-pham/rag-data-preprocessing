# Làm việc với vBackup project

vBackup project là một loại project được tạo từ chức năng backup nhằm lưu trữ dữ liệu từ hệ thống vBackup khi bạn thực hiện tạo các bản sao lưu (backup) cho Server của bạn từ hệ thống vServer về hệ thống vStorage theo hướng dẫn tại [đây](../../../../vserver/compute-hcm03-1a/backup/).

Đối với vBackup project, sẽ có 2 trường hợp xảy ra:&#x20;

* Nếu bạn chưa có backup project nào trên hệ thống vStorage thì khi bạn thực hiện backup Server, một backup project mới sẽ được tạo với 50 GB dung lượng miễn phí trên lớp lưu trữ Gold class và thời hạn sử dụng backup project này là 1 tháng kể từ thời điểm thiết lập thành công backup server theo hướng dẫn bên trên.&#x20;
* Nếu bạn đã có backup project được tạo sau đó xóa trước đây thì khi bạn thực hiện backup Server lần kế tiếp, một backup project mới sẽ được tạo với 0 GB dung lượng miễn phí trên lớp lưu trữ Gold class (tên backup project không đổi).&#x20;

Đối với 2 loại vBackup project này, bạn có thể:

<details>

<summary>Tăng hạn mức backup project</summary>

Sau khi một backup project được khởi tạo lần đầu tiên, lúc này backup project của bạn có dung lượng lưu trữ 50GB với thời hạn lưu trữ là 1 tháng. Từ lần khởi tạo thứ hai, backup project có dung lượng lưu trữ 0GB. Nếu dung lượng lưu trữ này là không đủ so với nhu cầu của bạn, bạn có thể tiếp tục thực hiện tăng hạn mức của backup project này bằng cách:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng \<update khi lên guide>tại **project** bạn muốn thực hiện thay đổi quota. Chọn **Thay đổi quota.**
3. Màn hình **Thay đổi quota** được hiển th&#x1ECB;**.** Chọn **quota** lưu trữ mong muốn tăng thêm, **quota** lưu trữ bạn có thể tăng thêm hoặc giảm đi đến mức tối đa hoặc tối thiểu bằng **quota** lưu trữ mà gói lưu trữ cung cấp. Bạn không thể điều chỉnh **quota** lưu trữ nhỏ hơn hoặc vượt quá giá trị này.
4. Chọn **Thay đổi quota project.**
5. Thực hiện các bước **thanh toán giỏ hàng** nếu bạn là người dùng trả trước hoặc chọn **Thay đổi quota project** nếu bạn là người dùng trả sau.

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, backup project của bạn đã được tăng giảm hạn mức.

Chúng tôi chỉ miễn phí cho bạn dung lượng lưu trữ 50GB ở lớp lưu trữ Gold class trong chu kỳ lưu trữ 1 tháng. Nếu bạn thực hiện tăng dung lượng quá 50 GB thì chi phí sẽ được tính bao gồm dung lượng lưu trữ ngoài 50GB này. Quy trình và phương thức tính giá tương tự như khi tăng giảm hạn mức project thông thường. Chi tiết tham khảo thêm tại [Cách tính phí](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648482).

</details>

<details>

<summary>Gia hạn backup project</summary>

Sau khi một backup project được khởi tạo lần đầu tiên, lúc này backup project của bạn có dung lượng lưu trữ 50GB với thời hạn lưu trữ là 1 tháng. Từ lần khởi tạo thứ hai, backup project có dung lượng lưu trữ 0GB với thời hạn lưu trữ là 1 tháng. Sau 1 tháng sử dụng thì backup project của bạn sẽ hết hạn và sẽ bị xóa khỏi hệ thống của chúng tôi. Nếu bạn có nhu cầu lưu trữ dữ liệu backup Server này quá 1 tháng thì bạn có thể thực hiện gia hạn backup project theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng \<update khi lên guide> tại **project** bạn muốn thực hiện gia hạn. Chọn **Gia hạn**.
3. Chọn **chu kỳ** mà bạn mong muốn gia hạn.
4. Chọn **Gia hạn project**.
5. Thực hiện các bước **thanh toán giỏ hàng** nếu bạn là người dùng trả trước hoặc chọn **Gia hạn project** nếu bạn là người dùng trả sau.

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, backup roject của bạn đã được gia hạn.

Chúng tôi chỉ miễn phí cho bạn dung lượng lưu trữ 50GB ở lớp lưu trữ Gold class trong chu kỳ lưu trữ 1 tháng. Nếu bạn thực hiện gia hạn thì chi phí sẽ được tính từ ngày kết thúc chu kỳ lưu trữ miễn phí tới ngày hết hạn theo chu kỳ mới mà bạn gia hạn. Quy trình và phương thức tính giá tương tự như khi gia hạn project thông thường. Chi tiết tham khảo thêm tại [Cách tính phí](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648482).

\


</details>

<details>

<summary>Xóa backup project còn thời hạn sử dụng</summary>

Sau khi một backup project được khởi tạo lần đầu tiên, lúc này backup project của bạn có dung lượng lưu trữ 50GB với thời hạn lưu trữ là 1 tháng. Từ lần khởi tạo thứ hai, backup project có dung lượng lưu trữ 0GB. Nếu bạn không có nhu cầu sử dụng backup project này, bạn có thể thực hiện xóa chúng theo hướng dẫn tại [Xóa project](lam-viec-voi-project/xoa-project.md).

Lúc này **backup project** bị xóa sẽ nằm trong **Thùng rác**, bạn có thể:

* **Xóa** **hoàn toàn** backup project khỏi vStorage bằng cách chọn **Xóa**.
* **Khôi phục** lại backup project sử dụng theo hướng dẫn ngay bên dưới.

Đối với khách hàng trả trước, nếu bạn đã phát sinh chi phí cho việc gia hạn hay tăng hạn mức backup project này thì khi bạn thực hiện xóa backup project còn thời hạn sử dụng, chúng tôi sẽ thực hiện bồi hoàn lại cho bạn số tiền thực tế mà bạn chưa sử dụng tương ứng trong chu kỳ lưu trữ còn lại. Chi tiết cách vStorage tính phí bồi hoàn và khôi phục project, hãy xem [Cách tính phí](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648482).&#x20;

Do hành động xóa project tiềm ẩn nhiều rủi ro nên chúng tôi khuyến cáo bạn hãy xem xét cẩn thận cũng như tạo một phiên bản dự phòng của project trước khi thực hiện xóa.&#x20;

</details>

<details>

<summary>Khôi phục backup project còn thời hạn sử dụng</summary>

Bạn có thể khôi phục backup project sau khi xóa theo hướng dẫn bên trên bằng cách:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn menu **Thùng rác.**
3. Chọn biểu tượng \<update khi lên guide>trên **project** muốn thực hiện khôi phục.
4. Chọn **Khôi phục project.**
5. Thực hiện các bước **thanh toán giỏ hàng** nếu bạn là người dùng trả trước hoặc chọn **Khôi phục project** nếu bạn là người dùng trả sau.

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, backup project của bạn đã được khôi phục.

Nếu backup project mà bạn thực hiện khôi phục chưa được Gia hạn hay Tăng giảm hạn mức bất kỳ một lần nào thì bạn có thể khôi phục lại backup project này với thông tin thanh toán là 0 VNĐ. Nếu backup project mà bạn thực hiện khôi phục đã được Gia hạn hay Tăng giảm hạn mức ít nhất một lần thì bạn có thể khôi phục lại backup project này với thông tin thanh toán là giá trị tài nguyên được gia hạn hay tăng hạn mức với số ngày sử dụng còn lại tương ứng. Quy trình và phương thức tính giá tương tự như khi khôi phục project thông thường. Chi tiết tham khảo thêm tại [Cách tính phí](../cach-tinh-phi/).

\


</details>

<details>

<summary>Hết thời hạn sử dụng backup project</summary>

Tại thời điểm hết hạn sử dụng backup project, chúng tôi sẽ:

* Chuyển tài nguyên **backup project** vào **thùng rác** và lưu trữ tại đây trong vòng 7 ngày.
* Trong 7 ngày này, bạn có thể xóa hoàn toàn **backup project** hoặc khôi phục **backup project** theo hướng dẫn ở bên trên.

</details>
