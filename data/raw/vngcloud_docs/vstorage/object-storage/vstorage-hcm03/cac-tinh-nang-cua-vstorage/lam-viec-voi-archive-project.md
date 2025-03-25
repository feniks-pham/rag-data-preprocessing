# Làm việc với Archive project

Archive project của dịch vụ lưu trữ vStorage là project sử dụng lớp lưu trữ Archive (Archive class) để lưu trữ dữ liệu. Archive class là lớp lưu trữ thứ 3 của vStorage bên cạnh Gold class và Silver class. Archive class được chúng tôi thiết kế nhằm mục đích sử dụng làm nơi nơi lưu trữ an toàn, bền bỉ với chi phí cực kỳ thấp, phù hợp với nhu cầu lưu trữ và sao lưu dữ liệu dài hạn của bạn.

Với Archive class, tỉ lệ SLA vẫn luôn đảm bảo đạt mức 99.99% cùng với các tính năng bảo mật dữ liệu theo các tiêu chuẩn an toàn dữ liệu của doanh nghiệp. Bên cạnh đó chi phí lưu trữ của Archive class thấp nhất trong 3 class có thể giúp bạn tiết kiệm rất nhiều chi phí so với các giải pháp lưu trữ sao lưu khác. Không chỉ vậy Archive class còn hướng đến việc tối ưu sự tiện dụng cho bạn thông qua việc dữ liệu sẽ luôn sẵn sàng để tải về ngay lập tức mà không mất bất kỳ thời gian chờ đợi nào. Thêm vào đó việc quản lý dữ liệu dễ dàng trên giao diện vStorage Portal cùng với các tính năng tìm kiếm thuận tiện. Tương tự các class khác của vStorage, Archive class cũng tương thích với các 3rd party software giúp bạn có thể tích hợp và sử dụng trên những phần mềm quen thuộc của mình.

#### Một số use case phổ biến của Archive project <a href="#lamviecvoiarchiveproject-motsousecasephobiencuaarchiveproject" id="lamviecvoiarchiveproject-motsousecasephobiencuaarchiveproject"></a>

* Dữ liệu được lưu trữ với mục đích để backup.
* Dữ liệu không cần truy cập, thao tác thường xuyên (cold data).
* Dữ liệu không yêu cầu cao về tốc độ đọc/ ghi.
* Dữ liệu có thể được nén trước khi lưu xuống vStorage archive và khi cần người dùng sẽ download dữ liệu được nén về và extract ra để làm việc.
* Dữ liệu phải được lưu trữ ít nhất N tháng, không yêu cầu xóa thường xuyên.

#### Quy định chung của Archive class <a href="#lamviecvoiarchiveproject-quydinhchungcuaarchiveclass" id="lamviecvoiarchiveproject-quydinhchungcuaarchiveclass"></a>

Để đáp ứng được các tiêu chí về chi phí cực thấp và chất lượng dịch vụ được phản ánh qua SLA cam kết 99,99%, Archive class có những quy định về việc lưu trữ như sau:

* Bạn chỉ có thể thực hiện mua gói lưu trữ ở **Archive class** thông qua **vStorage Portal.**&#x20;
* Bạn chỉ có thể tạo được các container có lớp lưu trữ **Archive class** thông qua **vStorage Portal**. Bạn không nên sử dụng các công cụ phía người dùng (3rd party software) để tạo mới container vì khi đó, các container sẽ được tạo ra với lớp lưu trữ mặc định **Gold class.**
* Trong **24 tiếng** đầu tiên kể từ thời điểm bạn tải lên một tệp tin vào **Archive class**, nếu tệp tin đã tải lên của bạn chưa chính xác thì bạn có thể thực hiện xóa chúng. Sau 24 tiếng này, dữ liệu sẽ không được xóa cho đến khi đủ thời gian quy định ít nhất là 6 tháng theo quy định bên dưới.
* Dữ liệu khi upload lên archive class này sẽ không được xóa cho đến khi đạt đủ thời gian tồn tại ít nhất là **6 tháng**. Chúng tôi vẫn sẽ cho phép bạn thực hiện các hành động khác trên dữ liệu này bao gồm: sao chép, di chuyển, thay đổi tên, chia sẻ, thiết lập tag, thiết lập metadata, tải lên tệp tin thay thế).
* Archive class cung cấp và hỗ trợ đầy đủ các công cụ để sử dụng bao gồm: **vStorage Portal, vStorage API, 3rd party software**. Tuy nhiên việc xóa dữ liệu chỉ có thể thực hiện thông qua **vStorage Portal**.
* Với nhu cầu khôi phục dữ liệu: tệp tin sẽ sẵn sàng để download trong vòng **1-12 tiếng**. Chi phí cho các thao tác được quy định rõ ràng khi bạn thực hiện mua tài nguyên, chi tiết xem tại [Cách tính phí](../cach-tinh-phi/).

#### Tips khi sử dụng <a href="#lamviecvoiarchiveproject-tipskhisudung" id="lamviecvoiarchiveproject-tipskhisudung"></a>

* Hãy chắc chắn dữ liệu bạn đưa lên **Archive class** là những dữ liệu cần lưu trữ nhưng ít có nhu cầu sử dụng. Vì tuy rằng chi phí lưu trữ của **Archive class** là thấp nhất nhưng chi phí phát sinh từ việc thao tác với dữ liệu như xóa, restore, v.v. sẽ cao hơn các lớp lưu trữ **Gold class** và **Silver class** từ 1-2 lần.
* **Archive class** cũng không phù hợp cho việc lưu trữ dữ liệu thay đổi liên tục vì quy định hạn chế xóa dữ liệu trong vòng 6 tháng của chúng tôi. Nếu bạn có nhu cầu lưu trữ dữ liệu backup nhưng có thời gian thay đổi dữ liệu hàng tuần, tháng thì **Silver class** sẽ là lựa chọn phù hợp. &#x20;

\
