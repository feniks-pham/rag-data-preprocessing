# Promote Read Relica thành Standalone

Khi bạn mong muốn chuyển 1 read replica thành standalone, bạn có thể sử dụng tính năng **Promote to Standalone** trên Portal, chọn DB Instance có **role: slave**, chọn **Action**



Chọn **Promote to Standalone**

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555997/image2021-6-14_16-29-18.png?version=1&#x26;modificationDate=1623662958000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Trước khi xác nhận promote, chúng tôi khuyến cáo rằng bạn nên dừng việc ghi dữ liệu vào master và đợi đến khi read replica đã đồng bộ toàn bộ dữ liệu, mặc khác sẽ có tỉ lệ read replica không có đủ dữ liệu đã được ghi tại master, chú ý rằng quá trình promotion này có thể mất 1 khoảng thời gian để hoàn thành và sau quá trình này, read replicas sẽ trở thành standalone, và quá trình replication giữa master và slave sẽ dừng lại:

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555997/image2021-6-14_16-33-23.png?version=1&#x26;modificationDate=1623663204000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Sau khi promote thành công, read replica đã chuyển thành **role:standalone** và có thể ghi được, đồng thời DB Instance có role master trước đó cũng chuyển thành role:standalone vì không còn ai replicate từ nó nữa

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555997/image2021-6-14_16-34-35.png?version=1&#x26;modificationDate=1623663276000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.vngcloud.vn/download/attachments/31555997/image2021-6-14_16-35-29.png?version=1&#x26;modificationDate=1623663330000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
