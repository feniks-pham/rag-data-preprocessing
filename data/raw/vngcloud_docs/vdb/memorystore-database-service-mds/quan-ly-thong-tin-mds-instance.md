# Quản lý thông tin MDS Instance (Database)

Giao diện quản lý Database cho phép bạn có cái nhìn tổng quát về tất cả các Database (DB Instance) hiện có cũng như thông tin chi tiết cho từng DB Instance. Hãy cùng điểm qua các tính năng có thể thao tác trên MDS Instance

* [A - Create Read Replica](quan-ly-thong-tin-mds-instance.md#quanlythongtinmdsinstance-a-giaodienquanlydatabase)
* [B - Promote To Standalone](quan-ly-thong-tin-mds-instance.md#quanlythongtinmdsinstance-a-giaodienquanlydatabase-1)
* [C - Resize Instance Type](quan-ly-thong-tin-mds-instance.md#quanlythongtinmdsinstance-a-giaodienquanlydatabase-2)
* [D - Edit Configuration Group](quan-ly-thong-tin-mds-instance.md#quanlythongtinmdsinstance-a-giaodienquanlydatabase-3)
* [E - Edit DB Setting](quan-ly-thong-tin-mds-instance.md#quanlythongtinmdsinstance-a-giaodienquanlydatabase-4)
* [F - Start, Shutdown, Reboot](quan-ly-thong-tin-mds-instance.md#quanlythongtinmdsinstance-a-giaodienquanlydatabase-5)
* [G - Delete MDS](quan-ly-thong-tin-mds-instance.md#quanlythongtinmdsinstance-a-giaodienquanlydatabase-6)

### A - Create Read Replica <a href="#quanlythongtinmdsinstance-a-giaodienquanlydatabase" id="quanlythongtinmdsinstance-a-giaodienquanlydatabase"></a>

Nhằm mở rộng khả năng read scale cho vDB, bạn có thể tạo read replicas cho các DB Instance, hệ thống sẽ tự động thiết lập mô hình master, slave và đồng bộ dữ liệu với cơ chế async, chi tiết các bước làm như sau:

* Đầu tiên bạn chọn DB Instance cần tạo read replicas từ đó, lưu ý chỉ những DB Instance có **role:standalone** hoặc **role:master** mới khởi tạo đc read replicas, chọn **Action** và chọn **Create Read Replica.**

<figure><img src="../../.gitbook/assets/image%20(526).png" alt=""><figcaption></figcaption></figure>

* Tiếp theo, tại trang khởi tạo, bạn chỉ cần đặt **DB Instance Name** cho read replicas và giữ nguyên các thông tin khác như: flavor, storage type, storage size, backup schedule, tuy nhiên chúng tôi khuyến cáo bạn giữ nguyên các thông tin này giống Master hoặc chọn các thông số cao hơn khi cần thiết.&#x20;
* Cuối cùng, Nhấn **Create Database** để khởi tạo. Sau khi khởi tạo bạn chờ một khoảng thời gian cho đến khi read replicas đã **Active.**

Vây là bạn đã tạo thành công Read Replica cho vDB hay còn gọi là mô hình master-slave, bạn có thể kiểm tra dữ liệu của master đã được đồng bộ qua slave hay chưa.

### B - Promote To Standalone <a href="#quanlythongtinmdsinstance-a-giaodienquanlydatabase" id="quanlythongtinmdsinstance-a-giaodienquanlydatabase"></a>

Khi bạn mong muốn chuyển 1 read replica thành standalone, bạn có thể sử dụng tính năng **Promote to Standalone** trên Portal, làm theo các bước hướng dẫn bên dưới:

* Đầu tiên, chọn DB Instance có **role: slave**, chọn **Action - Promote to Standalone.**

<figure><img src="../../.gitbook/assets/image%20(527).png" alt=""><figcaption></figcaption></figure>

* Tiếp theo, nhấn xác nhận **Promote** để hoàn tất quá trình.&#x20;

**Lưu ý:** Trước khi xác nhận promote, chúng tôi khuyến cáo rằng bạn nên dừng việc ghi dữ liệu vào master và đợi đến khi read replica đã đồng bộ toàn bộ dữ liệu, mặc khác sẽ có tỉ lệ read replica không có đủ dữ liệu đã được ghi tại master, chú ý rằng quá trình promotion này có thể mất 1 khoảng thời gian để hoàn thành và sau quá trình này, read replicas sẽ trở thành standalone, và quá trình replication giữa master và slave sẽ dừng lại.

Sau khi promote thành công, read replica đã chuyển thành **role:standalone** và có thể ghi được, đồng thời DB Instance có role master trước đó cũng chuyển thành role:standalone vì không còn ai replicate từ nó nữa

### C - Resize Instance Type <a href="#quanlythongtinmdsinstance-a-giaodienquanlydatabase" id="quanlythongtinmdsinstance-a-giaodienquanlydatabase"></a>

Để thay đổi cấu hình flavor MDS cho phù hợp hơn với nhu cầu sử dụng thực tế, bạn làm theo các hướng dẫn dưới đây:

* Đầu tiên, chọn MDS Instance cần thay đổi, nhấp vào nút **Action**, chọn **“Thay Đổi Cấu Hình”** / **"Resize Instance Type".**

<figure><img src="../../.gitbook/assets/image%20(558).png" alt=""><figcaption></figcaption></figure>

* Tiếp theo, một trình chỉnh sửa sẽ hiển thị cho phép bạn chọn cấu hình flavor mới, xem xét giá cấu hình mới và hiện tại ở phía bên phải trước khi xác nhận.
* Cuối cùng, nhấn **"Resize" / "Thay đổi"** để xác nhận quá trình. Bạn chờ một lát để hệ thống thực hiện các bước cần thiết, khi MDS Instance thay đổi cấu hình thành công sẽ có trạng thái **Active**.

### D - Edit Configuration Group <a href="#quanlythongtinmdsinstance-a-giaodienquanlydatabase" id="quanlythongtinmdsinstance-a-giaodienquanlydatabase"></a>

Để thay đổi liên kết MDS Instance với Configuration Group đã có, bạn có hai phương án:

* Liên kết ngay khi MDS Instance được khởi tạo.
* Thực hiện thay đổi cấu hình MDS Instance.

Đối với phương án 1, mời bạn xem lại hướng dẫn [Khởi tạo MDS Instance](https://docs.vngcloud.vn/pages/viewpage.action?pageId=13010707).

Đối với phương án 2, bạn có thể thực hiện như sau:

* Đầu tiên, bạn đến màn hình quản lý Database tại đường dẫn:  [https://vdb.console.vngcloud.vn/memorystore/database](https://vdb.console.vngcloud.vn/memorystore/database)
* Chọn đến MDS Instance và nhấn **Edit Configuration Group**.

<figure><img src="../../.gitbook/assets/image%20(3)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt=""><figcaption></figcaption></figure>

* Tại màn hình thay đổi chọn đến Configuration Group muốn áp dụng.
* Khi mọi lựa chọn đã chính xác, bạn nhấn nút **Save** ở góc phải trên cùng. Bạn chờ một lát để các biến cấu hình được áp dụng xuống MDS Instance và nếu quá trình thay đổi thành công, MDS Instance sẽ có trạng thái **Active**.

**Lưu ý:** Trong một số truờng hợp, biến cấu hình đòi hỏi cần **Restart** lại dịch vụ Database trên MDS Instance, status của MDS Instance lúc này sẽ là **Restart\_required**. Với VNG Cloud, bạn có thể chủ động thời điểm thực hiện thao tác này. Sau khi đã sao lưu các tác vụ trên MDS Instance, bạn click vào **Action**, chọn **Restart** để hoàn tất quá trình.

### E - Edit DB Setting <a href="#quanlythongtinmdsinstance-a-giaodienquanlydatabase" id="quanlythongtinmdsinstance-a-giaodienquanlydatabase"></a>

Sửa đổi Cài đặt DB cho phép bạn thay đổi **Mật khẩu Maste**r, **Khả năng Truy cập Công khai** và **Cài đặt Sao lưu**. Để làm điều này, chọn database cần sửa đổi, nhấp vào nút **“Edit DB Setting”** ở góc trên bên phải (tham khảo hình bên dưới).

<figure><img src="../../.gitbook/assets/image%20(560).png" alt=""><figcaption></figcaption></figure>

Một trình chỉnh sửa sẽ hiển thị để thay đổi Cài đặt DB của bạn, bao gồm:

* Bật/Tắt master password khi truy cập vào MDS Instance.
* Bật/Tắt khả năng truy cập công khai (Public accessibility)
* Bật/Tắt cài đặt tự động sao lưu.

Lưu ý: Đối với MDS Instance **role:slave**, việc bật/tắt master password phụ thuộc vào MDS Instance **role:master**, nếu MDS Instance role:master bật master password, thì toàn bộ db role:slave của db role:master sẽ bật password, và ngược lại, khi db role:master tắt password, toàn bộ db role:slave của db role:master sẽ tắt password.

### F - Start, Shutdown, Reboot <a href="#quanlythongtinmdsinstance-a-giaodienquanlydatabase" id="quanlythongtinmdsinstance-a-giaodienquanlydatabase"></a>

Các hành động Start, Shutdown và Reboot giúp bạn tối ưu hóa việc sử dụng tài nguyên MDS Instance. Thực hiện các hành động này khi cần thiết, để thực hiện, bạn chọn MDS Instance cần thay đổi, chọn Action và nhấp vào nút “Start” / “Reboot” / “Shutdown” tùy vào mục đích sử dụng.

<figure><img src="../../.gitbook/assets/image%20(559).png" alt=""><figcaption></figcaption></figure>

### G - Delete MDS <a href="#quanlythongtinmdsinstance-a-giaodienquanlydatabase" id="quanlythongtinmdsinstance-a-giaodienquanlydatabase"></a>

Chức năng **"Xóa"** cho phép người dùng xóa vĩnh viễn một MDS Instance khỏi hệ thống, đảm bảo loại bỏ hoàn toàn database, dữ liệu, cấu hình và bất kỳ phụ thuộc nào liên quan. VNG Cloud khuyến nghị bạn nên cho phép hệ thống của chúng tôi tạo bản sao lưu cuối cùng của cơ sở dữ liệu trước khi xóa nó để bảo vệ và phục hồi dữ liệu bằng cách chọn vào ô **“Tạo bản sao lưu cuối cùng”** trước khi xác nhận xóa.

Lưu ý: Sau khi hoàn tất quá trình xóa, nếu MDS Instance được chỉ định xóa là **role:master,** thì khi xóa thành công, toàn bộ db **role:slave** của master được xóa sẽ promote lên standalone.

<figure><img src="https://docs.vngcloud.vn/download/attachments/13010741/image2020-2-21_10-36-7.png?version=1&#x26;modificationDate=1582256168000&#x26;api=v2" alt=""><figcaption></figcaption></figure>
