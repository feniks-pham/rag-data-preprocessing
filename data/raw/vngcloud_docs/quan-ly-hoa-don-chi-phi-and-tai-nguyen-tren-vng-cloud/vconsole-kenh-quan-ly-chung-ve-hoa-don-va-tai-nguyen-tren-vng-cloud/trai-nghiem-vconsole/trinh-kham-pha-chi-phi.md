# Trình khám phá chi phí

**Trình khám phá chi phí / Cost explorer** tại vConsole cung cấp thống kê, dự đoán chi phí sử dụng trong tháng của các sản phẩm VNG Cloud Service.

**Trước mắt, Cost explorer chỉ hỗ trợ dự đoán chi phí dịch vụ của các sản phẩm / dịch vụ sau:**

| Sản phẩm                                   | Dịch vụ                                                                       | Hỗ trợ thống kê / dự đoán phí tại Cost Explorer |
| ------------------------------------------ | ----------------------------------------------------------------------------- | ----------------------------------------------- |
| <p><br></p><p><strong>vServer</strong></p> | Server, Image, Volume, Elastic IP, vContainer (k8s), vLB (Load balancer), vDB | Có                                              |
| Bandwidth, Interconnect                    | Chưa hỗ trợ (sẽ tích hợp trong thời gian tới)                                 |                                                 |
| **vStorage**                               | Quota                                                                         | Có                                              |
| **vMonitor**                               | Metric, Log, Notification (SMS & Email), Synthetic                            | Chưa hỗ trợ (sẽ tích hợp trong thời gian tới)   |
| **vCDN**                                   | <p><br></p>                                                                   | Chưa hỗ trợ (sẽ tích hợp trong thời gian tới)   |

Tại **Trình khám phá chi phí / Cost explorer**, vConsole cung cấp các tính năng phù hợp với nhu cầu người dùng như:

* Dự đoán chi phí sử dụng so với tháng trước
* Thống kê chi phí sử dụng dịch vụ trong tháng theo 2 hình thức
  * Biểu đồ: Biểu đồ cột, Biểu đồ tròn, Biểu đồ xếp chồng
  * Bảng biểu: Bảng dữ liệu

Truy cập đến trang **Trình khám phá chi phí / Cost explorer** [**tại đây**](https://dashboard.console.vngcloud.vn/cost-explorer)**.**

### **1. Current month cost / Phí sử dụng trong tháng** <a href="#trinhkhamphachiphi-costexplorer-1.currentmonthcost-phisudungtrongthang" id="trinhkhamphachiphi-costexplorer-1.currentmonthcost-phisudungtrongthang"></a>

***

**Current month cost / Phí sử dụng trong tháng hiển thị các số liệu về:**

* Chi phí sử dụng dịch vụ VNG Cloud (chỉ tính các sản phẩm được vConsole hỗ trợ), tính từ đầu tháng đến thời điểm hiện tại
* So sánh chênh lệch phí (tăng / giảm bao nhiêu %) từ đầu tháng đến thời điểm hiện tại so với phí sử dụng thực tế của tháng trước
* Công thức tính tỉ lệ (%) chênh lệch giá: Tỉ lệ % = (Chi phí hiện tại \*100 / Tổng chi phí tháng trước) - 100
  * Nếu tỉ lệ % >= 0 : Tăng so với tháng trước
  * Ngược lại: Giảm so với tháng trước

### **2. Forecast month cost /  Dự đoán phí sử dụng** <a href="#trinhkhamphachiphi-costexplorer-2.forecastmonthcost-dudoanphisudung" id="trinhkhamphachiphi-costexplorer-2.forecastmonthcost-dudoanphisudung"></a>

***

**Forecast month cost / Dự đoán phí sử dụng hiển thị các số liệu về:**

* Dự đoán chi phí sử dụng dịch vụ VNG Cloud (chỉ tính các sản phẩm được vConsole hỗ trợ), **từ đầu tháng đến cuối tháng hiện tại (tính tại thời điểm truy cập)**. vConsole dựa trên xu hướng sử dụng dịch vụ của người dùng từ đầu tháng đến thời điểm hiện tại, từ đó dự đoán chi phí sử dụng đến hết tháng.
* So sánh chênh lệch phí dự đoán (tăng / giảm bao nhiêu %) so với phí sử dụng thực tế của tháng trước
* Công thức tính tỉ lệ (%) chênh lệch giá: Tỉ lệ % = (Tổng chi phí dự đoán tháng này \*100 / Tổng chi phí tháng trước) - 100
  * Nếu tỉ lệ % >= 0 : Tăng so với tháng trước
  * Ngược lại: Giảm so với tháng trước

**Ví dụ số liệu cụ thể:**

* Tháng hiện tại: 03/2023
* Chi phí sử dụng thực tế của tháng trước (02/2023): 8,000,000 VND
* Ngày truy cập: 15/03/2023&#x20;

| Current month cost                                         | Forecast month cost         |                                              |                             |
| ---------------------------------------------------------- | --------------------------- | -------------------------------------------- | --------------------------- |
| **Chi phí sử dụng thực tế từ đầu tháng đến ngày truy cập** | **So sánh với tháng trước** | **Dự đoán chi phí sử dụng đến hết tháng 03** | **So sánh với tháng trước** |
| 5,000,000 VND                                              | Giảm 37,5%                  | 10,000,000 VND                               | Tăng 25%                    |

### **3. Biểu đồ và bảng biểu thống kê chi phí** <a href="#trinhkhamphachiphi-costexplorer-3.bieudovabangbieuthongkechiphi" id="trinhkhamphachiphi-costexplorer-3.bieudovabangbieuthongkechiphi"></a>

***

**Biểu đồ và bảng biểu thống kê chi phí sử dụng dịch vụ VNG Cloud (tính trên các sản phẩm được vConsole hỗ trợ)**

* Các sản phẩm hiện đang được hỗ trợ dự đoán giá bởi vConsole:&#x20;
  * **vServer:** Server, Image, Volume, Elastic IP, vContainer (K8s), vLB (Load balancer), vDB
  * **vStorage:** Quota
  * vMonitor và các sản phẩm / dịch vụ khác sẽ được tích hợp sau.
* Số liệu chỉ hỗ trợ thời gian tối đa 1 tháng (tính từ đầu tháng đến thời điểm truy cập)
* Các loại biểu đồ đang được hỗ trợ: Biểu đồ cột, biểu đồ xếp chồng
* Các kiểu xem đang được hỗ trợ
  * Daily: xem chi phí theo ngày trong tháng, tính từ đầu tháng tới thời điểm truy cập
  * Monthly: xem tổng chi phí các sản phẩm, tính từ đầu tháng tới thời điểm truy cập

### **Một số lưu ý (\*)** <a href="#trinhkhamphachiphi-costexplorer-motsoluuy" id="trinhkhamphachiphi-costexplorer-motsoluuy"></a>

***

* Số liệu tại Cost Explorer chỉ là con số dự đoán, không chính xác 100%, lý do:
  * Dữ liệu đang cập nhật tại vConsole không phải là dữ liệu thời gian thực, có độ trễ (mỗi 1h cập nhật 1 lần)
  * Dữ liệu chỉ tính trên các sản phẩm / dịch vụ được hỗ trợ ghi nhận bởi Cost Explorer (xem bảng đầu trang để biết thêm chi tiết)
* Cost Explorer chỉ hiển thị dữ liệu trong tháng (từ đầu tháng đến thời điểm trong cập), chưa hỗ trợ xem nhiều tháng trong quá khứ
* Đơn giá dùng để tính giá tại Cost Explorer là ban giá hiện hành, do đó số liệu tại Cost Explorer sẽ **phản ánh gần đúng nhất đối với hành vị sử dụng của người dùng trả sau**, **với người dùng trả trước, sẽ có 1 chút sai lệch** trong các trường hợp sau:
  * **Người dùng trả trước** thanh toán phí dịch vụ trong tháng với đơn giá áp dụng là mức giá A, nhưng tại thời điểm truy cập vào Cost Explorer, bảng giá hiện hành tại VNG Cloud Service có sự thay đổi lên / xuống mức giá B, do đó dữ liệu mà người dùng thấy sẽ không phản ánh chính xác chi phí sử dụng thực tế đã chi trả.
