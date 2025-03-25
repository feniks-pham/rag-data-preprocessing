# Nhật ký và giám sát dịch vụ K8S

Trong môi trường Kubernetes, việc quản lý và giám sát là rất quan trọng để đảm bảo hiệu suất và tin cậy của các ứng dụng và các thành phần của hệ thống. Hai khái niệm chính trong việc giám sát Kubernetes cluster là "log" và "metric".

1. **Log (Nhật ký)**:
   * Logs là thông tin chi tiết về hoạt động của các container, các pod và các thành phần khác trong môi trường Kubernetes.
   * Logs có thể bao gồm các thông tin về lỗi, thông tin gỡ lỗi, hoạt động của ứng dụng và hệ thống, giao tiếp giữa các thành phần, v.v.
   * Giám sát log giúp trong việc phát hiện và gỡ lỗi sự cố, theo dõi hoạt động của ứng dụng và hệ thống, cũng như phân tích và cải thiện hiệu suất.
2. **Metric (Đo lường)**:
   * Metrics là các con số định lượng về hiệu suất và trạng thái của hệ thống và các thành phần của nó.
   * Các metric thường bao gồm thông tin như CPU sử dụng, lượng bộ nhớ sử dụng, số lượng request đối với một dịch vụ cụ thể, thời gian phản hồi, v.v.
   * Giám sát metric giúp bạn theo dõi sự thay đổi trong tình trạng hệ thống theo thời gian, đánh giá hiệu suất, dự đoán vấn đề tiềm năng và tự động thích nghi với tải công việc thay đổi.

***

### **Vì sao nên sử dụng Log và Metric** <a href="#nhatkyvagiamsatdichvuk8s-visaonensudunglogvametric" id="nhatkyvagiamsatdichvuk8s-visaonensudunglogvametric"></a>

Sử dụng log và metric trong Kubernetes cluster có thể giúp bạn thực hiện nhiều hoạt động quan trọng để duy trì, giám sát và cải thiện hiệu suất của ứng dụng và hệ thống trong môi trường Kubernetes. Dưới đây là một số cách bạn có thể sử dụng log và metric:

**Sử dụng Log:**

* **Gỡ lỗi và phân tích sự cố**: Logs có thể giúp bạn xác định lỗi và sự cố xảy ra trong ứng dụng và hệ thống. Bằng cách theo dõi logs, bạn có thể phát hiện các vấn đề như lỗi runtime, khả năng xảy ra tấn công, hoặc sự cố liên quan đến cấu hình.
* **Theo dõi hoạt động ứng dụng**: Logs cho phép bạn hiểu cách mà các ứng dụng hoạt động trong thực tế. Bạn có thể theo dõi sự tương tác giữa các thành phần khác nhau và xác định hiệu suất và hoạt động của ứng dụng.
* **Xác minh tuân thủ**: Đối với các ứng dụng và hệ thống cần tuân thủ các quy định và chính sách nhất định (ví dụ: an toàn, bảo mật), logs có thể giúp bạn kiểm tra xem các hành vi và sự kiện có tuân thủ các quy tắc này hay không.

**Sử dụng Metric:**

* **Đo lường hiệu suất**: Metrics giúp bạn đo lường và theo dõi hiệu suất của các ứng dụng và hệ thống. Bằng cách theo dõi các metric như CPU sử dụng, tải trung bình, thời gian phản hồi, bạn có thể xác định liệu hệ thống có hoạt động hiệu quả hay không.
* **Dự đoán vấn đề**: Bằng cách theo dõi các trend và biểu đồ metric, bạn có thể dự đoán các vấn đề có thể xảy ra trong tương lai, ví dụ như tăng tải trong một khoảng thời gian cụ thể.
* **Tối ưu hóa tài nguyên**: Metrics giúp bạn hiểu cách tài nguyên như CPU, bộ nhớ và lưu trữ được sử dụng. Dựa trên các thông số này, bạn có thể tối ưu hóa việc phân phối tài nguyên, điều chỉnh kích thước pod hoặc điều hướng traffic để đảm bảo hiệu suất tốt nhất.
* **Thống kê và báo cáo**: Metrics cung cấp dữ liệu cụ thể để thực hiện thống kê và báo cáo về hiệu suất và sự hoạt động của hệ thống, giúp quản trị viên và nhóm phát triển có cái nhìn toàn diện về tình trạng của ứng dụng.

Tóm lại, sử dụng log và metric trong Kubernetes cluster giúp bạn duy trì, giám sát và tối ưu hóa hiệu suất của ứng dụng và hệ thống, từ việc phát hiện lỗi đến cải thiện trải nghiệm người dùng cuối.
