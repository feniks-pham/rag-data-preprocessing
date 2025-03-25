# Làm việc với project

## Tổng quan

Một Project là một thuật ngữ trên vStorage thể hiện một gói lưu trữ với dung tích cụ thể mà bạn thực hiện mua sắm trên VNG Cloud. **Với Region HCM04, tại  một thời điểm&#x20;**<mark style="color:red;">**bạn chỉ có thể sở hữu một Project**</mark>**&#x20;và sử dụng chúng để tổ chức lưu trữ dữ liệu của bạn.**

***



## **Phạm vi giới hạn project**

**Quy tắc đặt tên project**

Các quy tắc sau áp dụng cho việc đặt tên project trong vStorage:

* Tên project phải dài từ 1 (tối thiểu) đến 40 (tối đa) ký tự.
* Tên project chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Tên project không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...).
* Tên project phải là duy nhất trên một tài khoản VNG Cloud trong hoặc ngoài một region cho đến khi project đó bị xóa. Chúng tôi khuyến khích tên dự án hoặc sản phẩm của doanh nghiệp bạn được sử dụng như tên của project lưu trữ trong vStorage.

**Ví dụ minh họa**

* Các tên project ví dụ sau đây hợp lệ và tuân theo các nguyên tắc đặt tên được đề xuất:
  * project du an 1
  * du-an-nam-2022
  * ...
* Các tên project ví dụ sau đây hợp lệ nhưng chúng tôi không khuyến khích bạn sử dụng:
  * [docexamplewebsite.com](http://docexamplewebsite.com/)
  * [www.docexamplewebsite.com](http://www.docexamplewebsite.com/)
  * ...
* Các tên project ví dụ sau không hợp lệ:
  * Du an dat hieu qua 80 % (chứa ký tự %)
  * project\_1/2022 (chứa ký tự /)
  * ...

***

## Khởi tạo project

Thực hiện tạo project theo các bước bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [đây](https://register.vngcloud.vn/signup).
2. Chọn **Region HCM04.**
3. Chọn **Tạo một Project.**
4. Nhập **Project Name** và chọn **Project type** (gói) lưu trữ phù hợp theo nhu cầu. Hiện tại ở region HCM04, chúng tôi sẽ cung cấp cho bạn gói lưu trữ **Instant Archive Type**. Với gói lưu trữ này, bạn sẽ có lượng Traffic miễn phí bằng 2 lần lượng Quota mà bạn chọn sử dụng và lượng Request hoàn toàn miễn phí. Để biết thêm thông tin chi tiết về cách tính giá, vui lòng tham khảo thêm tại [Cách tính phí.](../cach-tinh-phi.md)
5. Chọn **Quota** (dung lượng lưu trữ) mà bạn mong muốn.
6. Chọn **Period** và chọn/bỏ chọn **Auto-renew** theo nhu cầu của bạn.
7. Thực hiện các bước **Thanh toán** giỏ hàng và **Project** của bạn sẽ được khởi tạo.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Xem thông tin project

Bạn có thể xem và sử dụng các thuộc tính cho project bao gồm thông tin chung của project, các cặp S3 key được tạo, cấu hình auto-scale nếu có, lịch sử tác động cũng như thông tin kết nối project với S3,...

Để xem các thuộc tính cho một project, bạn có thể:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn/storage](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **Region: HCM04**
3. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (601).png" alt="" data-size="line">tại **project** bạn muốn xem chi tiết.
4. Trên trang hiển thị thông tin chi tiết **project**, bạn có thể xem và sử dụng các thuộc tính cho project

* **Information**: Cung cấp các thông tin chung của project như Tổng quota, Tổng usage, Project type, Account URL, Project Owner.&#x20;
* **S3 key**: Cung cấp thông tin các cặp S3 key được khởi tạo cho project từ vStorage Portal. Để khởi tạo S3 key, vui lòng tham khảo thêm tại đây.
* **History**: Cung cấp thông tin lịch sử tác động tới project bao gồm loại hành động, trạng thái hành động, thời gian hành động xảy ra và mô tả chi tiết hành động nếu có.
* **Connection Information**: Cung cấp các câu lệnh và tệp tin cấu hình để kết nối project với S3.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## Tăng giảm hạn mức project

Bạn đã khởi tạo project với lượng quota ban đầu phù hợp với nhu cầu lưu trữ. Hiện tại nhu cầu kinh doanh của bạn thay đổi mà dung lượng cũ không đáp ứng được. Để giải quyết vấn đề này, bạn có thể thay đổi quota lưu trữ thông qua tính năng Thay đổi quota mà chúng tôi cung cấp.

Để thay đổi quota cho một project, bạn có thể:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn checkbox tại project bạn muốn tăng giảm hạn mức và chọn biểu tượng <img src="../../../../.gitbook/assets/image (604).png" alt="" data-size="line">hoặc bạn cũng có thể chọn biểu tượng <img src="../../../../.gitbook/assets/image (605).png" alt="" data-size="line"> sau đó chọn Resize.
3. Màn hình **Resize project** được hiển th&#x1ECB;**.** Chọn **quota** lưu trữ mong muốn tăng thêm, **quota** lưu trữ bạn có thể tăng thêm hoặc giảm đi đến mức tối đa hoặc tối thiểu bằng **quota** lưu trữ mà gói lưu trữ cung cấp. Bạn không thể điều chỉnh **quota** lưu trữ nhỏ hơn hoặc vượt quá giá trị này.
4. Chọn **Resize project.**
5. Chọn **Thanh toán** sau khi kiểm tra giỏ hàng và hình thức thanh toán.
6. Chọn **Tiếp tục thanh toán** và thực hiện thanh toán sau khi chọn phương thức thanh toán phù hợp.

Sau khi bạn thực hiện thành công 6 bước trên, giá trị tổng **quota** mới sau khi thay đổi sẽ được cập nhật trên thông tin chung của project mà bạn chọn.

<figure><img src="../../../../.gitbook/assets/image (603).png" alt=""><figcaption></figcaption></figure>

***

## Gia hạn project

Bạn đã khởi tạo project với chu kỳ lưu trữ ngắn hạn. Hiện tại nhu cầu kinh doanh của bạn thay đổi và bạn muốn tăng thêm chu kỳ lưu trữ này. Để giải quyết vấn đề này, bạn có thể thay đổi chu kỳ lưu trữ thông qua tính năng renew mà chúng tôi cung cấp.

Để renew một project, bạn có thể:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn checkbox tại **project** bạn muốn tăng giảm hạn mức và chọn biểu tượng <img src="../../../../.gitbook/assets/image (606).png" alt="" data-size="line"> hoặc bạn cũng có thể chọn biểu tượng <img src="../../../../.gitbook/assets/image (605).png" alt="" data-size="line"> sau đó chọn **Renew**.
3. Chọn Period lưu trữ mong muốn gia hạn. Chúng tôi cung cấp các chu kỳ lưu trữ bao gồm: **1 tháng, 3 tháng, 6 tháng, 12 tháng, 24 tháng, 36 tháng**. Khi bạn thực hiện chọn chu kỳ gia hạn, hệ thống sẽ tự động tính toán thời gian có hiệu lực của chu kỳ lưu trữ mới và tổng số tiền bạn cần chi trả cho việc gia hạn **project**.
4. Chọn **Thanh toán** sau khi kiểm tra giỏ hàng và hình thức thanh toán.
5. Chọn **Tiếp tục thanh toán** và thực hiện thanh toán sau khi chọn phương thức thanh toán phù hợp.

Sau khi bạn thực hiện thành công 5 bước trên, chu kỳ lưu trữ mới sau khi gia hạn project sẽ được cập nhật trên thông tin chung của project mà bạn chọn.

***

## Gia hạn tự động project

Ngoài cách gia hạn một project theo các thủ công thì chúng tôi cũng hỗ trợ bạn thiết lập gia hạn tự động thông qua tính năng Auto-renew.

Tính năng gia hạn tự động là tính năng hệ thống hỗ trợ tự động gia hạn các dịch vụ khi hết hạn được dễ dàng hơn cho những khách hàng trả trước. Khách hàng không cần phải lo lắng khi nào dịch vụ bị hết hạn để truy cập vào vStorage Portal gia hạn, thanh toán,...

Trước khi dịch vụ hết hạn 7 ngày hệ thống sẽ gửi mail thông báo về việc tự động gia hạn dịch vụ. Trong vòng 7 ngày này, mỗi ngày bạn sẽ nhận được 1 email thông báo.

Hệ thống sẽ tự động gia hạn 3 ngày trước khi dịch vụ hết hạn:

* Nếu đủ credit sẽ tiến hành gia hạn tất cả các dịch vụ. Khi gia hạn thành công hay thất bại, chúng tôi sẽ gửi email chứa thông tin gia hạn thành công/ thất bại cho bạn. Lịch sử thanh toán gia hạn dịch vụ cũng sẽ được chúng tôi lưu trữ trên hệ thống vConsole. Để biết thêm thông tin, hãy truy cập [Dashboard vConsole](https://dashboard.console.vngcloud.vn/payment-history).
* Nếu không đủ credit, hệ thống sẽ cố gắng gia hạn những dịch cho đến khi không còn đủ credit. Khi gia hạn thành công hay thất bại, chúng tôi sẽ gửi email chứa thông tin gia hạn thành công/ thất bại cho bạn. Lịch sử thanh toán gia hạn dịch vụ cũng sẽ được chúng tôi lưu trữ trên hệ thống vConsole. Để biết thêm thông tin, hãy truy cập [Dashboard vConsole](https://dashboard.console.vngcloud.vn/payment-history).

<details>

<summary>Thiết lập tính năng gia hạn tự động khi khởi tạo project</summary>

1. Thực hiện các bước khởi tạo project theo hướng dẫn tại [Khởi tạo project](../../vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-project/khoi-tao-project.md).
2. Tại thời điểm thiết lập thông tin về project cần mua, chọn **Gia hạn tự động**.
3. Chọn **chu kỳ gia hạn tự động**. Chúng tôi cung cấp các chu kỳ gia hạn bao gồm: 1 tháng, 3 tháng, 6 tháng, 12 tháng, 24 tháng, 36 tháng. Khi bạn thực hiện chọn chu kỳ gia hạn, hệ thống sẽ tự động tính toán thời gian có hiệu lực của chu kỳ lưu trữ mới và tổng số tiền bạn cần chi trả cho việc gia hạn **project**.

Để biết danh sách các loại hình thức thanh toán của vStorage và cách tính phí gia hạn project, hãy xem [Cách tính phí](../../vstorage-hcm03/cach-tinh-phi/).&#x20;

Sau khi bạn thực hiện thành công các bước trên, chu kỳ lưu trữ mới sau khi gia hạn project sẽ được cập nhật trên thông tin chung của project mà bạn chọn.

</details>

<details>

<summary>Thiết lập tính năng gia hạn tự động trên project đã được khởi tạo trước đó</summary>

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (607).png" alt="" data-size="line"> tại **project** bạn muốn thực hiện thiết lập gia hạn tự động. Chọn Enable Auto-renew.
3. Màn hình **Enable Auto-renew** được hiển th&#x1ECB;**.** Chọn **Period** gia hạn mà bạn mong muốn.&#x20;
4. Chọn **OK.**

Sau khi bạn thực hiện thành công các bước trên, chu kỳ lưu trữ mới sau khi gia hạn project sẽ được cập nhật trên thông tin chung của project mà bạn chọn.

</details>

<details>

<summary>Gỡ bỏ tính năng gia hạn tự động trên một project đã được thiết lập gia hạn tự động trước đó</summary>

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (609).png" alt="" data-size="line"> tại **project** bạn muốn thực hiện tắt thiết lập gia hạn tự động. Chọn **Disable Auto-renew.**
3. Màn hình **Disable Auto-renew** được hiển th&#x1ECB;**.**&#x20;
4. Chọn **OK.**

Sau khi bạn thực hiện thành công các bước trên, tính năng gia hạn tự động cho project đã được tắt.

</details>

***

## Xóa project

Bạn đã khởi tạo một project với gói lưu trữ phù hợp. Hiện tại nhu cầu kinh doanh của bạn thay đổi, bạn không có nhu cầu sử dụng project đã tạo. Chúng tôi khuyến khích bạn nên xóa project để tối ưu chi phí.

Để xóa một project, bạn có thể:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (610).png" alt="" data-size="line">tại project bạn muốn thực hiện xóa. Chọn **Delete**.
3. Nhập chuỗi ký tự **delete me** và chọn **Delete.**

Sau khi bạn bạn thực hiện xóa project thì project bị xóa sẽ biến mất khỏi danh sách project của bạn. Lúc này project bị xóa sẽ nằm trong **Thùng rác**, project bị xóa của bạn sẽ được lưu trữ tại **Thùng rác** trong vòng 7 ngày mà không mất phí. Trong 7 ngày này bạn có thể khôi phục lại project bị xóa. Để khôi phục, hãy xem hướng dẫn tại mục Khôi phục project. Nếu sau 7 ngày mà bạn không thực hiện khôi phục project thì project cùng các dữ liệu bên trong sẽ bị xóa hoàn toàn khỏi hệ thống và không thể khôi phục lại được nữa.

Khi bạn thực hiện xóa project trước thời hạn lưu trữ ban đầu, chúng tôi sẽ thực hiện bồi hoàn cho bạn cũng như khi bạn khôi phục project, chúng tôi cũng sẽ tính phí khôi phục. Chi tiết cách vStorage tính phí bồi hoàn và khôi phục project, hãy xem Cách tính phí.

Do hành động xóa project tiềm ẩn nhiều rủi ro nên chúng tôi khuyến cáo bạn hãy xem xét cẩn thận cũng như tạo một phiên bản dự phòng của project trước khi thực hiện xóa.

***

## Khôi phục project

Bạn vừa thực hiện xóa một project hoặc một project hết hạn lưu trữ. Lúc này project sẽ bị đưa vào thư mục Thùng rác và lưu trữ tại đây trong 7 ngày, sau 7 ngày project sẽ bị xóa vĩnh viễn và không thể khôi phục. Trong 7 ngày này bạn phát hiện mình đã xóa nhầm hoặc bạn muốn tiếp tục sử dụng project đã hết hạn lưu trữ. Để giải quyết vấn đề này, chúng tôi cung cấp cho bạn tính năng khôi phục lại project bị xóa.

Để khôi phục một project bị xóa, bạn có thể:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn menu **Trash.**
3. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (611).png" alt="" data-size="line">trên **project** muốn thực hiện khôi phục.
4. Chọn **Restore**.
5. Chọn **Thanh toán** sau khi kiểm tra giỏ hàng và hình thức thanh toán.
6. Chọn **Tiếp tục thanh toán** và thực hiện thanh toán sau khi chọn phương thức thanh toán phù hợp.

Sau khi bạn thực hiện thành công 6 bước trên, project sẽ được khôi phục với thông tin chu kỳ lưu trữ mới và được cập nhật trên thông tin chung của project mà bạn chọn.

Khi project bị đưa vào Thùng rác bạn sẽ không thể tải lên/ tải xuống hoặc thực hiện các hành động tới object được nữa. Chúng tôi khuyến cáo bạn hãy gia hạn hoặc sao lưu toàn bộ dữ liệu trong project trước ngày hết hạn.

***

## Tăng dung lượng tự động (Auto-scale Quota)

Tính năng Tự động tăng dung lượng lưu trữ (Auto-scale Quota) trên vStorage cho phép bạn thiết lập tự động mở rộng dung lượng lưu trữ dựa trên mức sử dụng và nhu cầu của bạn. Hướng dẫn này sẽ cung cấp chi tiết cách thức cấu hình và quản lý tính năng này thông qua vStorage Portal.

Để thiết lập tăng dung lượng tự động cho một project, bạn có thể:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Tại project cần thiết lập Auto-scale Quota, chọn biểu tượng <img src="https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252Fxle5SMO5J6MplFpJZC74%252Fimage.png%3Falt%3Dmedia%26token%3De9cdb754-9a75-4868-90bf-67e670048eb5&#x26;width=27&#x26;dpr=4&#x26;quality=100&#x26;sign=1f9a3808&#x26;sv=1" alt="" data-size="line"> sau đó chọn mục **Auto-scale** và tiếp tục chọn **Configure Auto-scale** hoặc chọn biểu tượng <img src="https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252Fs6DACNvZx3OSJhJDO654%252Fimage.png%3Falt%3Dmedia%26token%3D3164ca6e-fc29-4fd0-b88a-34a960d4cde0&#x26;width=29&#x26;dpr=4&#x26;quality=100&#x26;sign=aa473973&#x26;sv=1" alt="" data-size="line"> sau đó chọn **Set Auto-scale**.
3. Tại màn hình cấu hình **Auto-scale**, thực hiện thiết lập các thông số cần thiết cho **Auto Scale**. Cụ thể:

* **Thiết lập Quota Unit:** bạn có thể chọn 1 trong hai loại đơn vị bao gồm **GB** hoặc **Percent**.
* **Thiết lập Quota Threshold hoặc Quota Remain:** Nếu bạn chọn **Quota Unit** là **Percent**, tại đây bạn sẽ nhập phần trăm ngưỡng sử dụng mà khi đạt tới thì hệ thống sẽ kích hoạt việc tăng quota. Nếu bạn chọn **Quota Unit** là **GB**, tại đây bạn sẽ nhập lượng quota còn lại mà khi đạt tới hệ thống cũng sẽ kích hoạt việc tăng quota.
* **Thiết lập Mức Tăng Quota**: nhập mức tăng mong muốn theo **GB** hoặc **Percent**.

4. Chọn nhận thông báo qua **email** khi tăng quota thành công nếu muốn.
5. Bật tính năng **Auto-scale** tại biểu tượng <img src="https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252FjlLW0mG9Z7he3tym9yeH%252Fimage.png%3Falt%3Dmedia%26token%3D247a3e39-731f-4fdb-a2f4-08b6bf8bbf2d&#x26;width=64&#x26;dpr=4&#x26;quality=100&#x26;sign=44906aa4&#x26;sv=1" alt="" data-size="line">. Khi biểu tượng này trở thành <img src="https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252FVGMWqFlP5OOPvrycdMrg%252Fimage.png%3Falt%3Dmedia%26token%3D94d216a5-2e33-489e-884d-f837683920c6&#x26;width=59&#x26;dpr=4&#x26;quality=100&#x26;sign=38683327&#x26;sv=1" alt="" data-size="line">tức là bạn đã bật **Auto-scale** thành công.

{% hint style="info" %}
**Chú ý:**

* **Hệ thống vStorage** sẽ thực hiện kiểm tra project có/ không đủ điều kiện được auto-scale theo chu kỳ mỗi **5 phút** để tự động tăng dung lượng dựa trên ngưỡng đã thiết lập.
* Giá cước áp dụng theo bảng giá **vStorage tiêu chuẩn**, tính năng chỉ thực hiện tăng dung lượng mà không làm thay đổi Storage Class.
* Người dùng cần đảm bảo có **đủ số dư credit** cho tài khoản (trả trước) trước khi thực hiện Auto-scale.
* Nếu việc tăng dung lượng **thất bại**, người dùng sẽ nhận được thông báo qua email. Sau hai lần thực hiện auto-scale thất bại liên tiếp, hệ thống của chúng tôi sẽ ngừng gửi thông báo qua email cho bạn. Bạn cần chủ động truy cập vào vStorage để thực hiện resize project thủ công theo hướng dẫn bên trên.
{% endhint %}

***

## Thực hiện POC project

Khi bạn là người dùng trên hệ thống vStorage, mặc định bạn sẽ không thể thực hiện POC project. POC là chương trình giúp khách hàng có thể trải nghiệm dịch vụ thông qua giá trị (bằng credit trong ví POC) được VNG Cloud cung cấp cho khách hàng. Thông thường, ví POC sẽ được cấp thông qua các chương trình khuyến mãi, các chương trình chiến dịch quảng bá của VNG Cloud. Qua đó, khách hàng có thể tự trải nghiệm tạo một số dịch vụ nhất định trong khoảng thời gian quy định. Để thực hiện POC project, bạn hãy liên hệ với nhân viên Sale hoặc nhân viên hỗ trợ trực tiếp cho bạn hoặc mở một ticket support trên hệ thống của chúng tôi. Ví POC được cấp có giá trị nhất định được dùng trong khoảng thời gian quy định tùy theo chính sách của công ty. Hết thời gian hiệu lực, bạn có thể yêu cầu gia hạn thời hạn sử dụng ví POC hoặc trả thêm chi phí để duy trì dịch vụ.

Sau khi chúng tôi xác nhận đã cung cấp ví POC cho tài khoản của bạn, để sử dụng ví POC hãy làm theo hướng dẫn bên dưới:

<details>

<summary>Khởi tạo project sử dụng số dư ví POC</summary>

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **region HCM04.**
3. Chọn **Tạo một project.**
4. Màn hình **Tạo mới project** được hiển thị. Trong **Tên project**, hãy nhập tên tuân thủ theo quy định của chúng tôi cho project của bạn.
5. Chọn **Quota** lưu trữ theo nhu cầu của bạn.Quota là kích thước gói lưu trữ tối đa bạn có thể tạo. Đối với mỗi gói lưu trữ, chúng tôi đã cung cấp 1 kích thước tối thiểu và tối đa để bạn có thể lựa chọn thay đổi dựa trên nhu cầu thực tế.
6. Tắt chọn **Bật gia hạn tự động**. Lúc này chúng tôi hiển thị lựa chọn **PoC**.
7. Chọn **PoC**.
8. Chọn **Tạo một project.**
9. Chọn **Checkout PoC** sau khi kiểm tra thông tin giỏ hàng.

Sau khi bạn hoàn thành 9 bước được mô tả bên trên, project của bạn đã được tạo thông qua phương thức thanh toán là ví POC. **Project** này có tiền tố là **\[POC]. Mặc định project này sẽ có ngày bắt đầu là thời gian tạo project và ngày kết thúc là thời gian hết hạn sử dụng ví POC mà bạn được cung cấp.**

Thời gian sử dụng tài nguyên POC mặc định trùng với thời gian kết thúc ví POC. Chúng tôi chỉ hỗ trợ bạn sử dụng ví POC để thanh toán tài nguyên POC. Đối với tài nguyên POC, cách tính giá sử dụng tài nguyên POC tương tự như tài nguyên thường. Chi tiết tham khảo thêm tại Cách tính phí.

</details>

<details>

<summary>Gia hạn project sử dụng ví POC</summary>

Sau khi bạn khởi tạo một project sử dụng ví POC, lúc này bạn có thể tiếp tục gia hạn sử dụng project cũng bằng cách sử dụng ví Poc. Chi tiết hãy làm theo các bước sau:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (620).png" alt="" data-size="line">tại **project** bạn muốn thực hiện gia hạn. Chọn **Gia hạn.**
3. **Bạn có thể gia hạn project sử dụng ví POC nếu bạn đã gia hạn thời gian sử dụng ví POC. Sau khi bạn gia hạn thời gian sử dụng ví POC thì thời gian bạn có thể gia hạn project là quãng thời gian từ ngày kết thúc hiện tại tới ngày hết hạn mới của ví POC**. Để tăng thời gian sử dụng ví POC, bạn hãy liên hệ với nhân viên Sale hoặc nhân viên hỗ trợ trực tiếp cho bạn hoặc mở một ticket support trên hệ thống của chúng tôi. Chọn **Gia hạn**.
4. Chọn **Checkout PoC**.

Sau khi bạn hoàn thành 4 bước được mô tả bên trên, project của bạn đã được gia hạn thông qua phương thức thanh toán là ví POC.&#x20;

Quy trình và phương thức tính giá tương tự như khi gia hạn project thông thường. Chi tiết tham khảo thêm tại Cách tính phí.

</details>

<details>

<summary>Xóa project sử dụng ví POC</summary>

Sau khi bạn khởi tạo một project sử dụng ví POC, lúc này nếu bạn không có nhu cầu sử dụng project này, bạn có thể thực hiện xóa chúng theo hướng dẫn tại Xóa project.

Lúc này **project** bị xóa sẽ nằm trong **Thùng rác**, bạn có thể:

* **Xóa** **hoàn toàn** project khỏi vStorage bằng cách chọn **Xóa**.
* **Khôi phục** lại project sử dụng ví POC theo hướng dẫn ngay bên dưới.

</details>

<details>

<summary>Khôi phục project sử dụng ví POC</summary>

Bạn có thể khôi phục project sau khi xóa theo hướng dẫn bên trên bằng cách:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn menu **Thùng rác.**
3. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (621).png" alt="" data-size="line"> trên **project** muốn thực hiện khôi phục.
4. **Bạn có thể gia hạn project sử dụng ví POC với khoảng thời gian gia hạn tính từ ngày thực hiện xóa project tới ngày kết thúc thời gian sử dụng ví POC.** Để tăng thời gian sử dụng ví POC, bạn hãy liên hệ với nhân viên Sale hoặc nhân viên hỗ trợ trực tiếp cho bạn hoặc mở một ticket support trên hệ thống của chúng tôi. Chọn **Khôi phục.**
5. Chọn **Checkout PoC**.

Sau khi bạn hoàn thành 5 bước được mô tả bên trên, project của bạn đã được khôi phục thông qua phương thức thanh toán là ví POC.&#x20;

Quy trình và phương thức tính giá tương tự như khi khôi phục project thông thường. Chi tiết tham khảo thêm tại Cách tính phí.

</details>

<details>

<summary>Dừng POC trước thời hạn</summary>

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng <img src="../../../../.gitbook/assets/image (622).png" alt="" data-size="line">tại **project** bạn muốn thực hiện dừng POC. Chọn **Dừng POC**.
3. Chọn **Dừng POC**.&#x20;

Sau khi bạn thực hiện dừng POC thành công thì project của bạn sẽ được chuyển thành loại tài nguyên trả trước và được chuyển vào Thùng rác.

* Nếu bạn thực sự không có nhu cầu sử dụng project này nữa thì bạn có thể thực hiện xóa hoàn toàn project khỏi hệ thống của chúng tôi theo hướng dẫn tại Xóa project.
* **Nếu bạn muốn khôi phục project vừa xóa này để tiếp tục sử dụng, hãy làm theo hướng dẫn Khôi phục project. Khi khôi phục project vừa được dừng POC, bạn cần chọn lại chu kỳ gia hạn mới và thực hiện thanh toán tiền thật của bạn (số dư ví credit, ví Momo, ví Zalopay,...).**
* Bạn cũng không thể bật sử dụng POC sau khi đã thực hiện Dừng POC. Nếu bạn có vướng mắc lúc này, hãy liên hệ với nhân viên Sale hoặc nhân viên hỗ trợ trực tiếp cho bạn hoặc mở một ticket support trên hệ thống của chúng tôi.&#x20;

</details>

<details>

<summary>Hết thời hạn thực hiện POC</summary>

Tại thời điểm hết hạn sử dụng ví POC, chúng tôi sẽ:

* **Dừng POC** đối với tất cả tài nguyên POC đang sử dụng. Quy trình xử lý tương tự như khi bạn chủ động dừng POC trên tài nguyên.
* **Tắt ví POC**: bạn sẽ không được phép sử dụng tài nguyên dưới hình thức POC cho đến khi ví POC được bật trở lại.

</details>

***

## Thực hiện trial project

Hiện tại, với region HCM04 chúng tôi chưa hỗ trợ bạn có thể thực hiện tạo project trial. Tính năng này sẽ được chúng tôi phát triển trong các version tiếp theo.
