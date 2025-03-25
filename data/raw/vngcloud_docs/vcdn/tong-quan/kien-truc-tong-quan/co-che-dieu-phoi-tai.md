# Cơ Chế Điều Phối Tải

**vCDN Request Router** là hệ thống điều phối tải thông qua dịch vụ DNS của vCDN. Cứ định kỳ 30s, vCDN Request Router sẽ kiểm tra tình trạng sức khỏe của tất cả các server Edge trong mạng lưới CDN bao gồm ở tất cả các ISP khác nhau. Việc này sẽ giúp cho vCDN Request Router nằm bắt được trạng thái của các server Edge gần như tức thời nhằm loại bỏ các server bị lỗi ra khỏi mạng lưới phục vụ sớm nhất và điều phối traffic của server đang bị lỗi sang các server khác. Khi user cần truy cập tài nguyên trên hệ thống CDN thì user sẽ request đến các Public DNS như Google, Cloudflare, OpenDNS hay các DNS Server local của ISP mà user đang hòa mạng. Các server Public DNS sẽ chuyển tiếp yêu cầu đến server vCDN Request Router. Với các thông tin có được tài thời điểm nhận request như:

* IP Client.
* Trạng thái hoạt động của các server hiện tại.
* Tải của các đường kết nối giữa các POP.
* Tải của từng POP.

Minh họa:

<figure><img src="../../../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

Hệ thống vCDN Request Router sẽ quyết định gửi lại IP Server tốt nhất khả thi cho user tại thời điểm đó. Cụ thể Rules điều phối sẽ được thực hiện như sau (ưu tiên từ trên xuống dưới):

* User ở mạng nào và vùng nào sẽ về server có tải ít nhất ở vùng đó thuộc ISP đó.
* Trong trường hợp POP thuộc ISP tại khu vực của người dùng bị sự cố hoặc quá tải, sẽ chuyển đến POP của ISP khác đang có khả năng phục vụ tại khu vực đó.&#x20;

Với người dùng các ISP nhỏ như CMC, SPT, SCTV, Netnam sẽ được điều phối ưu tiên lưu lượng về POP của VNG Cloud tại Công Viên Phần Mềm Quang Trung vì tại đây VNG Cloud đã thực hiện peering trực tiếp tới mỗi ISP như trên. Việc này đảm bảo phục vụ tốt cho tất cả người dùng cuối.

**Đối với traffic Domectic (trong nước) thông thường, VNG hiện không cam kết tốc độ với traffic đến từ quốc tế. Quý khách hàng tham khảo thêm dịch vụ vCDN quốc tế mà VNGCloud cung cấp để có chất lượng tốt nhất với traffic quốc tế hoặc liên hệ support@vng.com.vn để được hướng dẫn thêm.**
