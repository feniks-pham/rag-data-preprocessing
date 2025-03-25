# Sử dụng công cụ Cyberduck

#### Một số use case thông thường <a href="#sudungcongcucyberduck-motsousecasethongthuong" id="sudungcongcucyberduck-motsousecasethongthuong"></a>

**Tạo một container mới**

1. Tại màn hình chính của **Cyberduck**, nhấn chuột phải tại vùng trang trắng và chọn **New Folder.** Hoặc bạn có thể nhấn tổ hợp phím **Ctrl + Shift + N.**
2. Nhập tên **container**. Tên container mà bạn nhập phải tuân thủ theo quy định của chúng tôi. Chi tiết tham khảo tại [Phạm vi giới hạn container](../../cac-tinh-nang-cua-vstorage/lam-viec-voi-container/pham-vi-gioi-han-container.md)

<figure><img src="https://contabo.com/blog/wp-content/uploads/2022/12/image-7.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/59805342/image2023-7-14_14-15-57.png?version=1&#x26;modificationDate=1689318958000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Tải lên tệp tin vào một container** &#x20;

1. Tại màn hình chính của **Cyberduck**, chọn **container** mà bạn muốn tải tệp tin lên.
2. Chọn **Upload**.
3. Chọn tệp tin hay thư mục từ máy của bạn sau đó chọn **Choose**.
4. Tiến trình tải tệp tin lên bắt đầu. Khi tải lên hoàn thành, Cyberduck sẽ thông báo tệp tin được tải lên Thành công.

<figure><img src="https://contabo.com/blog/wp-content/uploads/2022/12/image-9.png" alt=""><figcaption></figcaption></figure>

**Xóa một object trong một container**

1. Tại màn hình chính của **Cyberduck**, chọn **container chứa object** mà bạn muốn xóa.
2. Tại object bạn muốn xóa, chọn chuột phải sau đó chọn **Delete**.

<figure><img src="../../../../../.gitbook/assets/image (533).png" alt=""><figcaption></figcaption></figure>

3. Trên màn hình xác nhận xóa, tiếp tục chọn **Delete**.

***

#### Một số use case nâng cao

**Chia sẻ object thông qua Presign URL**

1. Tại màn hình chính của **Cyberduck**, chọn **container chứa object** mà bạn muốn chia sẻ qua Presign URL.
2. Tại object bạn muốn chia sẻ, chọn chuột phải sau đó chọn **Copy URL** nếu bạn muốn sao chép Presign URL hoặc chọn **Open URL** nếu bạn muốnmở trực tiếp Presign URL trên trình duyệt.

<figure><img src="../../../../../.gitbook/assets/image (534).png" alt=""><figcaption></figcaption></figure>

3. Chọn một trong các phương thức cho **Presign URL** mà bạn mong muốn.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (535).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Chú ý:**&#x20;

* Không nên sử dụng phiên bản Cyberduck quá cũ/ quá mới trên các hệ điều hành có phiên bản quá cũ/ quá mới vì có thể gặp lỗi.
* Khi bạn sử dụng Cyberduck để thực hiện Sao chép (Copy)/ Di chuyển (Move)/ Thay đổi tên (Rename) object trên hệ thống vStorage có thể gây ra lỗi. Chúng tôi khuyến cáo bạn không nên sử dụng các tính năng này.
* Cyberduck không có hỗ trợ dọn incomplete segment khi tải object lớn (Multipart upload). Khi bạn sử dụng Cyberduck (s3, swift) để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, Cyberduck của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Hiện tại, Cyberduck chưa hỗ trợ tính năng dọn các segment rác này. Do đó, chúng tôi khuyến nghị bạn nên xem xét kỹ trước khi sử dụng công cụ này.
{% endhint %}
