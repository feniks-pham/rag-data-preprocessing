# Tình huống sử dụng (use case)

vStorage có thể được sử dụng cho nhiều nhu cầu lưu trữ khác nhau, bên dưới là một vài ứng dụng phổ biến:

* **Ứng dụng làm media hosting**&#x20;
  * Lưu trữ static files cho web: Các dữ liệu static như hình, html, document v..v... có thể được lưu trên vStorage để giảm tải dung lượng cho Server disk giúp tiết kiệm chi phí và tăng trải nghiệm người dùng.&#x20;
  * Lưu trữ video, image phục vụ CDN (Content delivery network): vStorage Gold / Silver class được thiết kế để đáp ứng lượng request từ CDN hoặc người dùng cuối. Thêm vào đó với băng thông mỗi chiều upload/download lên đến 10Gbps, original storage của bạn sẽ không bao giờ bị tắc nghẽn cho dù lượng người dùng có tăng cao đột biến.&#x20;
* **Lưu trữ backup**: Silver và Archive là 2 lớp lưu trữ phù hợp cho nhu cầu sao lưu backup dữ liệu nhờ băng thông lớn giúp bạn dễ dàng upload các dữ liệu backup một cách nhanh chóng. Khả năng autoscale của vStorage giúp giảm thiểu rủi ro thiếu dung lượng cho dữ liệu backup và giải quyết các khó khăn khi dữ liệu tăng trưởng nhanh.
* **Mount storage thành network drive:** Một trong những ứng dụng phổ biến của vStorage là mount thành một network disk trên server, client, nhờ tính năng này đa phần các ứng dụng đang chạy có thể dễ dàng chuyển tải dữ liệu sang mà không cần bỏ thời gian tìm hiểu tính tương thích của ứng dụng, hay điều chỉnh để sử dụng.&#x20;
* **Software delievery**: vStorage có thể được ứng dụng làm nơi hosting cho app, content, game client để người dùng tải về. Với hạ tầng lớn của vstorage bạn không cần lo nghĩ về việc tắc nghẽn khi lượt tải tăng đột biến.&#x20;
* **Ứng dụng làm lưu trữ cho fileserver**: Với nhu cầu lưu trữ tập trung chia sẻ phân quyền trên cloud, cách đơn giản nhất bạn có thể xây dựng một server gateway cùng với vStorage. Server gateway đảm nhiệm phần trung gian luân chuyển dữ liệu, đáp ứng được các yêu cầu truy suất nhanh nhờ vào cache tại server, trong khi đó lượng dữ liệu chủ yếu sẽ được đưa vào vStorage nhằm tối ưu chi phí lưu trữ.&#x20;
