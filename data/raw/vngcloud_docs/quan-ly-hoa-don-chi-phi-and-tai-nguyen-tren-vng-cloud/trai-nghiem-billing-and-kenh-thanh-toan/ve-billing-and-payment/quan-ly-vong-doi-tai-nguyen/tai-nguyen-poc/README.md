# Tài nguyên POC

Tài nguyên POC sinh ra nhằm mục đích hỗ trợ người dùng có thể trải nghiệm dịch vụ tại VNG Cloud một cách tốt nhất.&#x20;

Điều kiện sử dụng tài nguyên POC:

* **Đối tượng**: Người dùng trả trước được cấp ví POC
* **Nguồn tiền:** [**Ví POC**](../../thanh-toan/thanh-toan-tai-nguyen-poc.md)
* **Tài nguyên:** Tất cả các tài nguyên được áp dụng POC
* **Thời gian sử dụng:** Tùy thuộc vào thời hạn ví POC được cấp.

## Khởi tạo tài nguyên POC <a href="#tainguyenpoc-khoitaotainguyenpoc" id="tainguyenpoc-khoitaotainguyenpoc"></a>

***

* **Bước 1: Cấu hình tài nguyên**&#x20;
  * 1.1 Truy cập vào trang sản phẩm **vServer, vStorage, vMonitor**
  * 1.2 Chọn tài nguyên và cấu hình cần sử dụng tại trang sản phẩm
  * 1.3 Nhấn chọn sử dụng tài nguyên POC
  * 1.3 Xác nhận sử dụng tài nguyên để chuyển đến bước thanh toán: Tại đây, hệ thống sẽ điều hướng người dùng đến trang thanh toán tài nguyên
* **Bước 2: Thanh toán tài nguyên bằng ví POC**
  * Xem hướng dẫn chi tiết [**tại đây**](../../thanh-toan/thanh-toan-tai-nguyen-poc.md)
* **Bước 3: Hệ thống thực hiện**
  * Cung cấp tài nguyên&#x20;
  * Email thông báo thông tin tài nguyên vừa khởi tạo

**Một số lưu ý khi khởi tạo tài nguyên POC**

* Thời gian sử dụng tài nguyên POC mặc định trùng với thời gian kết thúc ví POC
* Chỉ được dùng ví POC để thanh toán tài nguyên POC
* Đối với tài nguyên POC, hệ thống sẽ không phát sinh hóa đơn tài nguyên tương ứng
* Cách tính giá sử dụng tài nguyên POC tương tự như tài nguyên thường. Tham khảo chi tiết [tại đây](../khoi-tao-tai-nguyen.md)

## Thay đổi cấu hình tài nguyên POC <a href="#tainguyenpoc-thaydoicauhinhtainguyenpoc" id="tainguyenpoc-thaydoicauhinhtainguyenpoc"></a>

***

Quy trình và phương thức tính giá tương tự như khi thay đổi cấu hình khi sử dụng tài nguyên thường. Tham khảo chi tiết [tại đây](../thay-doi-cau-hinh-tai-nguyen.md)

#### Gia hạn tài nguyên POC <a href="#tainguyenpoc-giahantainguyenpoc" id="tainguyenpoc-giahantainguyenpoc"></a>

***

Trong trường hợp thời hạn sử dụng ví POC của người dùng được gia hạn thêm sau khi đã khởi tạo tài nguyên POC, người dùng có thể tiến hành gia hạn tài nguyên POC tương ứng với thời gian kết thúc mới của ví POC.

Quy trình và phương thức tính giá tương tự như khi gia hạn tài nguyên thường. Tham khảo chi tiết [tại đây](../gia-han-tai-nguyen.md)

## Dừng POC đối với tài nguyên POC <a href="#tainguyenpoc-dungpocdoivoitainguyenpoc" id="tainguyenpoc-dungpocdoivoitainguyenpoc"></a>

***

**Trong trường hợp người dùng dừng POC trước thời hạn kết thúc tài nguyên POC, hệ thống sẽ:**

* Tiến hành hoàn phí sử dụng tài nguyên POC còn lại (nếu có) vào ví POC

**Để tiếp tục sử dụng tài nguyên vừa dừng POC như một tài nguyên bình thường (với mục đích giữ nguyên cấu hình), người dùng có thể:**

* Gia hạn tài nguyên (trong trường hợp tài nguyên chưa bị chuyển vào mục thùng rác)
* Khôi phục tài nguyên (trường hợp đã bị chuyển vào mục thùng rác trong vòng 7 ngày)

Đối với cả 2 tác vụ trên, tài nguyên sẽ được tính là tài nguyên thường và người dùng phải tiến hành thanh toán phí sử dụng tài nguyên thông qua các hình thức khác ngoài ví POC

## Hết thời gian sử dụng ví POC <a href="#tainguyenpoc-hetthoigiansudungvipoc" id="tainguyenpoc-hetthoigiansudungvipoc"></a>

***

Tại thời điểm hết hạn sử dụng ví POC, hệ thống sẽ:

* Dừng POC đối với tất cả tài nguyên POC đang sử dụng
  * Đối với các tài nguyên áp dụng **tạm giữ credit**, khi dừng POC sẽ dừng cung cấp dịch vụ và xóa luôn tài nguyên POC đó. Do đó, quý khách hàng cần chủ động dừng POC trước thời hạn kết thúc để đảm bảo tiếp tục sử dụng tài nguyên. [Danh sách dịch vụ áp dụng tạm giữ credit tại đây](../../thanh-toan/tam-giu-credit.md).
  * Đối với các tài nguyên áp dụng hình thức trả trước từ ví POC, hệ thống sẽ tạm giữ tài nguyên trong vòng 7 ngày trước khi xóa vĩnh viễn, quý khách có thể vào khôi phục lại nếu có nhu cầu sử dụng tiếp
* Tắt ví POC: Người dùng sẽ không được phép sử dùng tài nguyên dưới hình thức POC cho đến khi ví POC được bật trở lại
