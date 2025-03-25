# Hướng dẫn gắn 1 policy vào Auto-scaling group

Có 2 cách gắn 1 policy vào Auto-scaling group

**Cách 1: Gắn 1 policy vào group đã tạo**

**Bước 1**: Tại giao diện Scaling Group Management -> Chọn group bạn muốn gắn Policy , bạn sẽ thấy thông tin chi tiết của group hiện ra ở dưới

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650348/image2019-5-24_0-0-38.png?version=1&#x26;modificationDate=1681444009000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Bước 2:** Chọn Policy -> Bạn sẽ thấy danh sách các policy đã gắn. Tại đây bạn có thể gắn (Assign) hoặc bỏ (Detach) policy

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650348/image2019-5-24_0-0-51.png?version=1&#x26;modificationDate=1681444010000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Bước 3**: Chọn Assign Policy -> Chọn type policy và Policy bạn muốn gắn

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650348/image2019-5-24_0-1-9.png?version=1&#x26;modificationDate=1681444010000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Lưu ý**: nếu bạn đã tạo policy mà không thấy trong danh sách Policy, thì có thể xem lại và thay đổi lựa chọn phần Type policy. Danh sách policy chỉ hiển thị những policy phù hợp với type policy đã chọn

Sau khi hoàn tất, chọn Assign để hoàn tất. Bạn sẽ thấy policy vừa gắn hiện ra ở giao diện quản lý policy

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650348/image2019-5-24_0-1-22.png?version=1&#x26;modificationDate=1681444010000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

**Cách 2**: Nếu như bạn đã có POLICY trước khi tạo group, có thể gắn Policy ngay trong lúc tạo 1 Auto-Scaling group như sau

Ở bước khai báo configure khi tạo scaling group, nhấn Advance

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650348/image2019-5-24_0-1-34.png?version=1&#x26;modificationDate=1681444010000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Chọn Type policy -> chọn policy.

**Lưu ý**: nếu bạn đã tạo policy mà không thấy trong danh sách Policy, thì có thể xem lại và thay đổi lựa chọn phần Type policy. Danh sách policy chỉ hiển thị những policy phù hợp với type policy đã chọn

Sau khi hoàn tất, nhấn next bạn sẽ thấy group vừa tạo sẽ có gắn policy vừa chọn

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650348/image2019-5-24_0-1-47.png?version=1&#x26;modificationDate=1681444010000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
