# Chuyển đổi hình thức sử dụng từ POC sang dịch vụ trả phí

Tại VNG Cloud Service, chúng tôi hỗ trợ người dùng thay đổi mục đích sử dụng tài nguyên một cách linh hoạt, từ giai đoạn POC chuyển sang dịch vụ trả phí trên cùng một tài nguyên. Việc chuyển đổi mục đích sử dụng trên mang lại lợi ích đáng kể như _**tiết kiệm thời gian khởi tạo tài nguyên mới (cấu hình, thanh toán,...), tối ưu hóa chi phí sử dụng, tái sử dụng dữ liệu cũ cho mục địch mới,...**_

Để thực hiện quá trình chuyển đổi, vui lòng thực hiện theo các hướng dẫn bên dưới:

* **Bước 1:** Truy cập vào trang web quản lý tài nguyên
* **Bước 2:** Tại phần quản lý thông tin tài nguyên, chọn hành động "Dừng POC"
* **Bước 3:** Xác nhận dừng POC khi có cửa sổ xác nhận bật lên, lúc này người dùng sẽ được chuyển hướng đến trang thanh toán tài nguyên
* **Bước 4:** Tại trang thanh toán, người dùng thực hiện tương tự việc mua mới, theo nhu cầu sử dụng như
  * Chọn thời gian sử dụng tài nguyên
  * Bật tính năng tự động gia hạn
  * Chọn thanh toán bằng VNG Cloud credit hoặc trực tiếp từ cổng thanh toán
* **Bước 5:** Sau khi thanh toán thành công, người dùng sẽ được chuyển hướng về trang web quản lý tài nguyên để kiểm tra thông tin và tiếp tục sử dụng tài nguyên

Lúc này, hệ thống đã ghi nhận tài nguyên hoàn tất quá trình chuyển đổi sang dịch vụ trả phí, người dùng có thể kiểm tra thông tin hóa đơn dịch vụ (ngoại trừ dịch vụ K8s (vContainer)) tại trang web vConsole - Lịch sử hóa đơn: [https://dashboard.console.vngcloud.vn/billing-report](https://dashboard.console.vngcloud.vn/billing-report)

### **Chuyển đổi tài nguyên K8s (vContainer)** <a href="#chuyendoihinhthucsudungtupocsangdichvutraphi-chuyendoitainguyenk8s-vcontainer" id="chuyendoihinhthucsudungtupocsangdichvutraphi-chuyendoitainguyenk8s-vcontainer"></a>

***

Nhằm giúp người dùng có cái nhìn chi tiết hơn về quá trình trên, dưới đây là các bước hướng dẫn chuyển đổi một loại tài nguyên, cụ thể là Cluster (trong nhóm dịch vụ K8s/vContainer) sang dịch vụ trả phí:

* **Bước 1:** Truy cập vào trang web quản lý tài nguyên tại vServer portal [https://hcm-3.console.vngcloud.vn/vserver/billing](https://hcm-3.console.vngcloud.vn/vserver/billing)
* **Bước 2:** Chọn cluster POC cần chuyển đổi (sử dụng thanh công cụ tìm kiếm, tìm theo tên/định danh tài nguyên để lọc ra cluster cần tìm). Tham khảo hình bên dưới:

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804267/image2023-11-29_16-42-44.png?version=1&#x26;modificationDate=1701250964000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Bước 3:** Chọn hành động "**Dừng POC**" đối với cluster vừa tìm được tại Bước 2
* **Bước 4:** Xác nhận chuyển đổi một lần nữa tại cửa sổ bật lên, lúc này người dùng sẽ được chuyển hướng sang trang thanh toán
  * Kiểm tra thông tin giá tiền tại trang thanh toán **(Check out).** Nhấn **"Continue" / "Tiêp tục"** để tiếp tục quá trình.
  * Xác nhận thanh toán bằng phương thức **"Hold"**: hiểu thêm về phương thức "Hold" [tại đây](../../thanh-toan/tam-giu-credit.md)
  * Hệ thông tiến hành tạm giữ credit đối với tài nguyên trên, cho 3 ngày sử dụng dịch vụ

<figure><img src="https://docs.vngcloud.vn/download/attachments/59804267/image2023-11-29_16-50-41.png?version=1&#x26;modificationDate=1701251441000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Bước 5:** Sau khi thanh toán thành công, người dùng sẽ được chuyển hướng về trang web vServer để kiểm tra thông tin và tiếp tục sử dụng tài nguyên

**(\*) Lưu ý:**

* Riêng đối với tài nguyên thuộc nhóm dịch vụ K8s/vContainer, hệ thống sẽ không xuất hóa đơn tại thời điểm thực hiện chuyển đổi, mà hóa đơn sẽ được ghi nhận vào kì đối soát hàng tháng của dịch vụ này dựa trên chi phí sử dụng thực tế
* Việc chuyển đổi tài nguyên cluster sang dịch vụ trả phí, đồng nghĩa với việc chuyển đổi toàn bộ persistent volume (được khởi tạo trong quá trình POC cluster) sang dịch vụ trả phí tại cùng thời điểm.
