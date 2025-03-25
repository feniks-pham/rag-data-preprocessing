# Refill

Sau một thời gian bạn sử dụng tính năng Archive mà chúng tôi cung cấp, dữ liệu log đã được định kỳ đẩy về storage tương ứng mà bạn chọn. Nếu bạn có nhu cầu tìm kiếm và phân tích dữ liệu log được lưu trữ tại storage này, bạn có thể đưa chúng trở lại bằng tính năng Refill mà chúng tôi cung cấp. <mark style="color:red;">**Để thuận tiện nhất, chúng tôi khuyến khích bạn nên tạo một Log project mới (ngắn hạn hay dài hạn tùy thuộc vào nhu cầu của bạn) để xử lý dữ liệu log được refill này thay vì sử dụng lại một Log project đã tạo trước đó. Chúng tôi sẽ cho phép bạn cấu hình refill logs data đến các logs project empty và chưa được cấu hình cho bất cứ hoạt động refill nào trước đó.**</mark>

Để sử dụng tính năng Refill, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Log**.
3. Chọn **Log project.**
4. Chọn **Log project name** mà bạn muốn thực hiện **Refill** vào, dữ liệu sau khi refill sẽ được lưu trữ trong Log Project này.
5. Tại màn hình hiển thị thông tin **Log** **project**, tại tab **Refill**, chọn **Refill**.
6. Nhập **Refill name** theo quy định của chúng tôi. **Tên Refill** phải dài từ 1 (tối thiểu) tới 63 (tối đa) ký tự. **Tên Archive** có thể bao gồm chữ cái in hoa, in thường (a-z, A-Z), chữ số (0-9) hoặc dấu gạch ngang. **Tên Archive** phải bắt đầu bởi một chữ cái và kết thúc bởi một chữ cái hoặc một chữ số.

<figure><img src="../../../../.gitbook/assets/image (310).png" alt=""><figcaption></figcaption></figure>

7\. Chọn **Source**. Source tại đây là nguồn dữ liệu đã được archive trước đó mà bạn đã tạo.

Tuỳ vào việc dữ liệu bạn đã archive ở đâu, bạn có thể chọn 1 trong 3 nơi dữ liệu log được archive bao gồm: nguồn **archive** đã tạo trước đó,  **vStorage container** hoặc **S3 compatible**.&#x20;

<figure><img src="../../../../.gitbook/assets/image (311).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Choose an archive</summary>

Chọn một cấu hình **archive** đã tạo trước đó trong danh sách các cấu hình **archive** đang tồn tại trên hệ thống vMonitor Platform trong tài khoản Root User account hiện tại của bạn, hệ thống sẽ tự động điền đầy đủ các thông tin để có thể lấy được dữ liệu Logs

</details>

<details>

<summary>Select a vStorage container</summary>

Chọn **My container** nếu bạn muốn chọn vStorage container thuộc sở hữu của tài khoản bạn đang cần archive. Hoặc chọn **Custom container** nếu bạn muốn chọn vStorage container không thuộc sở hữu của tài khoản bạn đang cần archive.

* My container

1. Chọn một **Region**. Nếu bạn muốn xem lại thông tin **Region** và các **vStorage project** cũng như **vStorage container** bạn đang có trên hệ thống vStorage, hãy chọn tại ![](https://docs-admin.vngcloud.vn/download/thumbnails/49650640/image2023-4-27\_13-54-3.png?version=1\&modificationDate=1683512577000\&api=v2)
2. Chọn một **vStorage project** trong danh sách các project mà bạn đang có tại **Region** đã chọn trước đó trên hệ thống vStorage. Nếu danh sách vStorage project hiển thị cho bạn hiển thị đúng danh sách project tại thời điểm hiện tại, hãy chọn ![](https://docs-admin.vngcloud.vn/download/thumbnails/49650640/image2023-4-27\_13-55-2.png?version=1\&modificationDate=1683512577000\&api=v2).
3. Chọn một **vStorage container** trong danh sách các container mà bạn đang có tại **project** đã chọn trước đó trên hệ thống vStorage. Nếu danh sách vStorage container hiển thị cho bạn hiển thị đúng danh sách container tại thời điểm hiện tại, hãy chọn ![](https://docs-admin.vngcloud.vn/download/thumbnails/49650640/image2023-4-27\_13-55-2.png?version=1\&modificationDate=1683512577000\&api=v2).
4. Nhập **Access key** và **Secret key** để xác thực thông tin kết nối tới hệ thống vStorage. Bạn có thể tìm thấy **Access key** và **Secret key** theo hướng dẫn tại [Service Account](https://docs.vngcloud.vn/display/ONVINA/Service+Account) và [Sử dụng Service Account](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648950).
5. Chọn **Select**.

![](<../../../../.gitbook/assets/image (312).png>)

* Custom container

1. Chọn một **Region**. Nếu bạn muốn xem lại thông tin **Region** và các **vStorage project** cũng như vStorage container bạn đang có trên hệ thống vStorage, hãy chọn tại ![](https://docs-admin.vngcloud.vn/download/thumbnails/49650640/image2023-4-27\_13-54-3.png?version=1\&modificationDate=1683512577000\&api=v2)
2. Nhập tên một **vStorage container** mà bạn muốn thực hiện archive qua.
3. Nhập **Access key** và **Secret key** để xác thực thông tin kết nối tới hệ thống vStorage. Bạn có thể tìm thấy **Access key** và **Secret key** theo hướng dẫn tại [Service Account](https://docs.vngcloud.vn/display/ONVINA/Service+Account) và [Sử dụng Service Account](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648950).
4. Chọn **Select**.

![](<../../../../.gitbook/assets/image (313).png>)

</details>

<details>

<summary>Select an S3 compatible</summary>



</details>

8\. Chọn **Next** để tiếp tục chọn cấu hình cho refill.

9\. Nhập **Filter** cho log nếu có. Bạn có thể nhập điều kiện lọc cho log bằng phương thức **Suggestion mode** hoặc **Editor mode**. Để biết thêm thông tin hãy xem tại [Log search](https://docs-admin.vngcloud.vn/display/VPV/Log+search).

10\. Chọn **Time range** bằng cách chọn ![](https://docs-admin.vngcloud.vn/download/thumbnails/49650640/image2023-5-8\_9-30-18.png?version=1\&modificationDate=1683513020000\&api=v2)sau đó chọn hoặc nhập khung thời gian mong muốn refill.

11\. Nếu bạn muốn thay đổi thông tin **Refill information**, bạn có thể chọn **Previous** sau đó bạn có thể thực hiện thay đổi thông tin theo nhu cầu của bạn. Nếu bạn đã cấu hình xong thông tin cho refill, chọn **Refill** để bắt đầu.

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/49650640/Screen%20Shot%202022-07-11%20at%2010.57.52.png?version=1&#x26;modificationDate=1682490125000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

12\. **Process refill** sẽ bắt đầu thực hiện cho đến khi báo status “Finished”. Bạn có thể check data đã được refill ở trang log search như các project log khác.

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/49650640/Screen%20Shot%202022-07-11%20at%2011.22.07.png?version=1&#x26;modificationDate=1682490125000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
