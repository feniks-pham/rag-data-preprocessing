# Quản lý vòng đời tài nguyên

Sử dụng tài liệu này để hiểu hơn về tài nguyên mà bạn đang sử dụng.&#x20;

Tại đây, chúng tôi cung cấp thông tin về **vòng đời tài nguyên** và **các hành động của người dùng** / **hệ thống** có thể ảnh hưởng đến **trạng thái tài nguyên** mà người dùng đang sử dụng.

Thông qua **mô hình vòng tài nguyên** dưới đây, bạn sẽ có cái nhìn tổng quan về sự **chuyển đổi trạng thái tài nguyên**, cũng như sự **liên kết giữa tài nguyên với hóa đơn .**

### **Mô hình vòng đời tài nguyên**  <a href="#quanlyvongdoitainguyen-mohinhvongdoitainguyen" id="quanlyvongdoitainguyen-mohinhvongdoitainguyen"></a>

* **Người dùng trả trước action trên tài nguyên**

***

\


\


<figure><img src="https://docs.vngcloud.vn/download/attachments/49649293/Daily_Job_HC%20(3)-Page-2.drawio.png?version=1&#x26;modificationDate=1677814179000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **New → Active:**&#x20;
  * Khi người dùng khởi tạo tài nguyên thành công, tài nguyên sẽ có trạng thái là Active và **phát sinh hóa đơn tương ứng**
* **Active → ← Stop:**
  * Người dùng thực hiện action Start, Reboot / Stop tài nguyên để chuyển đổi qua lại 2 trạng thái này
* **Active → ← Suspense:**
  * Active → Suspense: Tài nguyên hết thời hạn sử dụng và bị chuyển vào trash chờ xóa hẳn
  * Suspense → Active: Người dùng thực hiện khôi phục tài nguyên đang ở trash để tiếp tục sử dụng
* **Active → Deleted:**
  * Người dùng thực hiện xóa tài nguyên
* **Suspense → Deleted:**
  * Tài nguyên đã hết hạn, sau 1 khoảng thời gian ở trash sẽ bị xóa hẳn và không thể khôi phục lại

### **Mô hình vòng đời tài nguyên**  <a href="#quanlyvongdoitainguyen-mohinhvongdoitainguyen.1" id="quanlyvongdoitainguyen-mohinhvongdoitainguyen.1"></a>

* **Người dùng trả sau action trên tài nguyên**

***

<figure><img src="https://docs.vngcloud.vn/download/attachments/49649293/Daily_Job_HC%20(3)-Page-4.drawio%20(1).png?version=1&#x26;modificationDate=1677818819000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **New → Active:**&#x20;
  * Khi người dùng khởi tạo tài nguyên thành công, tài nguyên sẽ có trạng thái là Active
* **Active → ← Stop:**
  * Người dùng thực hiện action Start, Reboot / Stop để chuyển đổi qua lại 2 trạng thái này
* **Active → Deleted:**
  * Người dùng thực hiện xóa tài nguyên
* **Suspense → Deleted:**
  * Tài nguyên đã hết hạn, sau 1 khoảng thời gian ở trash sẽ bị xóa hẳn và không thể khôi phục lại
* **Phát sinh hóa đơn:**
  * Đối với người dùng trả sau, hóa đơn sẽ được phát sinh tại thời điểm cuối tháng, ghi nhận thông tin sử dụng của tài nguyên đó
  * Trong trường hợp người dùng xoá tài nguyên, thông tin sử dụng cũng sẽ được ghi nhận lại và phát sinh hóa đơn dựa trên thông tin đó

### &#x20;<a href="#quanlyvongdoitainguyen-detimhieuchitietvehanhdongnguoidungtrentainguyen-thamkhaothemtaiday" id="quanlyvongdoitainguyen-detimhieuchitietvehanhdongnguoidungtrentainguyen-thamkhaothemtaiday"></a>
