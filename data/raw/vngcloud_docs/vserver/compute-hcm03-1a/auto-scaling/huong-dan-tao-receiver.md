# Hướng dẫn tạo Receiver

Receiver là tính năng cho phép bạn Scale (IN / OUT) 1 Group bằng web hook.

**Bước 1:** Tại giao diện Auto-scaling group chọn 1 group bạn muốn dùng receiver

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650364/image2019-5-24_0-4-53.png?version=1&#x26;modificationDate=1681444125000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Bước 2** Chọn receiver -> Create receiver

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650364/image2019-5-24_0-5-4.png?version=1&#x26;modificationDate=1681444126000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Bước 3:** Nhập tên receiver và Loại Acion. Hiện tại có 2 Action là

\-          CLUSTER\_SCALE\_IN : Giảm instance, mỗi lần giảm 1 nếu không có gắn scaling policy

\-          CLUSTER\_SCALE\_OUT: Tăng instance, mỗi lần tăng 1 nếu không có gắn scaling policy

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650364/image2019-5-24_0-5-18.png?version=1&#x26;modificationDate=1681444126000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Chọn receiver để tạo, sau khi tạo thành công bạn sẽ thấy Receiver như hình dưới.

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650364/image2019-5-24_0-5-32.png?version=1&#x26;modificationDate=1681444126000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Để có thể kích hoạt (trigger) được webhook url này bạn cần những thông tin sau:

&#x20;\+ Web hook url: thông tin đường dẫn để bạn gọi vào, bạn lấy bằng cách nhấn vào “Copy channel”

&#x20;\+ User\_id: thông tin định danh account, bạn lấy bằng cách truy cập vào [https://portal.vngcloud.vn/account.html](https://portal.vngcloud.vn/account.html) tại trường Account id.

&#x20;\+ Access key: thông tin xác thực, bạn liên hệ với chúng tôi để được cung cấp

&#x20;Ví dụ bạn có những thông tin như dưới đây:

&#x20;\+ Web hook url: [https://example.vinadata.vn/v1/example/6e88c3f851dc4f48b11276c79a847d1c/receiver/81935b94-fc5c-4d06-869f-61aaaa4797e6/scale?backend=4](https://sdn-vsr-api.vinadata.vn/v1/senlin/6e88c3f851dc4f48b11276c79a847d1c/receiver/81935b94-fc5c-4d06-869f-61aaaa4797e6/scale?backend=4)

&#x20;\+ user\_id: 47777

&#x20;\+ access\_key: 89fa022b-6c44-43f2-b51c-3b332fbbf462

Bạn có thể sử dụng curl để kích hoạt mở rộng

curl -H 'Content-type: application/json' -H 'user\_id:46677-H 'access\_key: 89fa3452b-6345-43f2-0000-3b332fbbf462' -XPOST '[https://example.vinadata.vn/v1/example/6e88c3f851dc4f48b11276c79a847d1c/receiver/81935b94-fc5c-4d06-869f-61aaaa4797e6/scale?backend=4](https://sdn-vsr-api.vinadata.vn/v1/senlin/6e88c3f851dc4f48b11276c79a847d1c/receiver/81935b94-fc5c-4d06-869f-61aaaa4797e6/scale?backend=4)'

\
