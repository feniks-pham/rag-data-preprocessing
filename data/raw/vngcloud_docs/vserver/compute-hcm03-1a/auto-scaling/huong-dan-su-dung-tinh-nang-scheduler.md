# Hướng dẫn sử dụng tính năng scheduler

Scheduler là tính năng giúp bạn tạo lịch chạy một auto-scaling group tự động theo thời gian mong muốn. Scheduler giúp bạn tiết kiệm được workload cho những tác vụ lặp đi lặp lại vào cùng 1 thời điểm. Ví dụ ở thời gian cao điểm 8h-10h mỗi ngày bạn cần nhiều instance để phục vụ, bạn có thể dùng scheduler để tăng số VM vào lúc 8h và dùng scheduler để giảm số VM sau 10h mỗi ngày.

Để tạo 1 scheduler, bước 1 tại giao diện Auto-scaling group management, chọn 1 group bạn muốn dùng scheduler.

&#x20;Bạn sẽ thấy thông tin chi tiết của group bên dưới, chọn scheduler

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650356/image2019-5-24_0-2-19.png?version=1&#x26;modificationDate=1681444078000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Chọn create scheduler và nhập các thông tin yêu cầu

\-          **Name**: Có thể nhập các ký tự (a-z, A-Z, 0-9, '\_'), và phải bắt đầu với chữ

\-          **Group**:  hệ thống tự động chọn Group mà bạn đang xem

\-          **Desire capacity**: Nhập số lượng instance bạn mong muốn, scaling group sẽ scale số instance tương ứng

\-          **Min capcity:** Số lượng instance tối thiểu

\-          **Max capcity:** Số lượng instance tối đa.

\-          **Scheduler**: Cách thức (tuần suất) scheduler sẽ chạy, bao gồm các option sau

* **One**: Scheduler chỉ chạy 1 lần duy nhất
* **Cron**: Bạn có thể tự định nghĩa thời gian scheduler lặp lại theo cấu trúc Cron job. Tham khảo thêm tại đây [http://www.cronmaker.com/](http://www.cronmaker.com/)
* **Everyday**: Lặp lại mỗi ngày. Ví dụ như setting bên dưới, scheduler sẽ lặp lại vào lúc 10:07 mỗi ngày

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650356/image2019-5-24_0-2-34.png?version=1&#x26;modificationDate=1681444079000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Everyweek**: Lặp lại mỗi tuần. Ví dụ như bên dưới, scheduler sẽ lặp lại vào lúc 20:15 mỗi thứ 2 hàng tuần

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650356/image2019-5-24_0-2-48.png?version=1&#x26;modificationDate=1681444079000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Everymonth**: Lặp lại mỗi tháng. Ví dụ như bên dưới, scheduler sẽ lặp lại vào lúc 15:10 tại ngày 2 của mỗi tháng (2/1, 2/2, 2/3 v...v…)

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650356/image2019-5-24_0-3-0.png?version=1&#x26;modificationDate=1681444079000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\-  **Run start:** Ngày scheduler bắt đầu chạy

**- Run end:** Sau thời điểm end-time, scheduler sẽ kết thúc việc lặp lại

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650356/image2019-5-24_0-3-13.png?version=1&#x26;modificationDate=1681444079000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Sau khi thiết lập xong, chọn create để tạo scheduler. Tạo thành công bạn sẽ thấy Scheduler được list ra như hình dưới

<figure><img src="https://docs.vngcloud.vn/download/attachments/49650356/image2019-5-24_0-3-34.png?version=1&#x26;modificationDate=1681444079000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\
