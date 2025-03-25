# Thanh toán tài nguyên POC

Trước khi tìm hiểu phương thức thanh toán tài nguyên POC, bạn nên hiểu rõ các khái niệm cũng các hành động mà người dùng có thể thao tác đối với tài nguyên POC. Tìm hiểu thêm về tài nguyên POC [**tại đây**](../quan-ly-vong-doi-tai-nguyen/tai-nguyen-poc/)**.**

Thanh toán tài nguyên POC là một hình thức thanh toán tại VNG Cloud Service, áp dụng đối với:

* **Đối tượng**:
  * Người dùng trả trước
* **Tài nguyên / Dich vụ**:

Các tài nguyên được áp dụng POC theo thỏa thuận. Ví POC hiện đã hỗ trợ các tài nguyên dịch vụ:

* vServer : Server, Volume, Elastic IP, LB, K8S, VKS, Snapshot, vCR, vDB, Marketplace, BW&#x20;
* vStorage: Project, Backup
* vMonitor: Metric, Log
* Terraform: Support khởi tạo POC cho VM từ Terraform
* **Nguồn tiền**:
  * Ví POC
* **Tác vụ**:
  * Người dùng thực hiện cấu hình tài nguyên được phép POC và xác nhận thanh toán
  * Hệ thống tiến hành thanh toán:
    * Thanh toán thành công: Tiến hành cung cấp tài nguyên theo cấu hình, phát sinh lịch sử sử dụng credit ví POC
    * Thanh toán thất bại: Hủy tác vụ
  * Cung cấp tài nguyên POC theo cấu hình, trường hợp có lỗi trong quá trình cung cấp tài nguyên sẽ tiến hành hoàn tiền vào ví POC
* **Kết quả thi hành tác vụ:**
  * Gửi email thông báo thông tin tài nguyên

#### Ví POC là gì? <a href="#thanhtoantainguyenpoc-vipoclagi" id="thanhtoantainguyenpoc-vipoclagi"></a>

***

POC là một loại ví do VNG Cloud cung cấp nhằm mục đích đem đến cho người dùng trải nghiệm dịch vụ một cách toàn diện nhất. Người dùng sử dụng ví POC như là 1 phương thức thanh toán đối với các tài nguyên được phép POC.

* **Số dư ví POC:** Phụ thuộc vào thỏa thuận giữa người dùng và phía VNG Cloud
* **Thời hạn sử dụng ví:** Phụ thuộc vào thỏa thuận giữa người dùng và phía VNG Cloud

#### Sở hữu ví POC bằng cách nào? <a href="#thanhtoantainguyenpoc-sohuuvipocbangcachnao" id="thanhtoantainguyenpoc-sohuuvipocbangcachnao"></a>

***

Hiện tại, ví POC được cấp thông qua các chương trình khuyến mãi, chiến dịch quảng cáo của VNG Cloud hoặc thông qua bộ phận Sale/Sale Operation sau khi đã hoàn thành các thỏa thuận.

\
