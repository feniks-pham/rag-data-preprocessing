# Tăng giảm quy mô minion node cho Node Group

Việc tăng giảm số lượng minion (node) trong một node group có thể có nhiều lý do khác nhau, tùy thuộc vào ngữ cảnh và mục tiêu của hệ thống hoặc ứng dụng bạn đang sử dụng. Dưới đây là một số lý do chính để thực hiện việc tăng giảm số lượng minion của node group:

1. **Điều chỉnh Tải Công việc:** Khi tải công việc trên hệ thống tăng cao, việc tăng số lượng minion có thể giúp phân tán tải và đảm bảo rằng hệ thống hoạt động một cách hiệu quả hơn mà không gặp vấn đề về tải quá cao.
2. **Mở Rộng Khả năng Xử lý:** Việc tăng số lượng minion trong node group có thể tạo ra sự mở rộng khả năng xử lý của hệ thống, cho phép xử lý cùng lúc nhiều công việc và yêu cầu từ người dùng.
3. **Hiệu Suất Cao hơn:** Tăng số lượng minion có thể cải thiện hiệu suất của hệ thống, đặc biệt là khi nó đang gặp khó khăn trong việc đáp ứng nhu cầu tài nguyên của ứng dụng.
4. **Dự Phòng và Độ Tin Cậy:** Bằng cách có nhiều minion hơn trong node group, bạn có thể tạo ra các bản sao dự phòng của các tài nguyên, giúp tăng khả năng chịu lỗi và độ tin cậy của hệ thống.
5. **Tối Ưu Hóa Chi phí:** Khi tải công việc thấp, việc giảm số lượng minion có thể giúp tiết kiệm chi phí bằng cách giảm sự sử dụng tài nguyên không cần thiết.
6. **Quản Lý Tài Nguyên Linh Hoạt:** Tăng giảm số lượng minion có thể giúp bạn điều chỉnh tài nguyên theo nhu cầu thay đổi của ứng dụng hoặc hệ thống mà không cần đầu tư thêm vào cơ sở hạ tầng cứng.
7. **Tuân Thủ Quy định Định mức:** Trong một số trường hợp, bạn có thể cần điều chỉnh số lượng minion để tuân thủ các quy định về định mức tài nguyên hoặc quy định an ninh.

Bạn có thể tăng giảm số lượng Minion node của Node Group Default và Node group tạo bởi người dùng, tuy nhiên không được vượt quá định mức 10 Minion node trên một Node Group

***

#### Tăng giảm quy mô Minion Node trên bảng điều khiển vServer <a href="#tanggiamquymominionnodechonodegroup-tanggiamquymominionnodetrenbangdieukhienvserver" id="tanggiamquymominionnodechonodegroup-tanggiamquymominionnodetrenbangdieukhienvserver"></a>

1. Truy cập vào bảng điều khiển vServer của chúng tôi tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Chọn vào xem chi tiết Cluster bằng cách nhấn vào tên của Cluster, sau đó chọn **Scale Minions**
3. Màn hình sẽ hiển thị pop-up **Thay đổi quy mô minion**
4. Tại đây bạn có thể chọn Node Group muốn thay đổi số lượng Minion tại mục Node Group sau đó nhập số lượng Minion muốn thay đổi vào mục **Số lượng mới**
5. Chọn **Thay đổi** để lưu lại thao tác

\
