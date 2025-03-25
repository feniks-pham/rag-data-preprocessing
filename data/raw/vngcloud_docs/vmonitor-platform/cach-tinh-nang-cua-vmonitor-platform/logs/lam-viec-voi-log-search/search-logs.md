# Search logs

### Cách sử dụng <a href="#searchlogs-cachsudung" id="searchlogs-cachsudung"></a>

Tại **vùng số 2 - nơi để bạn nhập thông tin tìm kiếm log**: chúng tôi hỗ trợ bạn 2 phương thức tìm kiếm là **Suggestion mode và Editor mode.**

* **Suggestion mode** (mặc định): chúng tôi sẽ hiển thị gợi ý tất cả các fields của logs đổ về để bạn chọn (nên chọn các field có hậu tố là keyword để chúng tôi có thể gợi ý luôn được giá trị đang có sẵn của field cho bạn). Việc tìm kiếm sẽ có kết quả chính xác nhất khi bạn nhập đúng cú pháp **Fields \<Toán tử> Value**.

Ví dụ: để filter các bản ghi logs có phương thức HTTP là GET trong vòng 15 phút gần nhất thì bạn chọn query là http\_method.keyword = 'GET' và thiết lập time range là 15m..&#x20;

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59807124/image2023-8-2_17-39-24.png?version=1&#x26;modificationDate=1690972765000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* **Editor mode**: mặc định khi bạn search logs, chúng tôi sẽ bật **Suggestion mode**. Để sử dụng Editor mode, bạn hãy chọn vào biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/59807124/image2023-8-7_11-14-17.png?version=1&#x26;modificationDate=1691381658000&#x26;api=v2" alt="" data-size="line">, khi màn hình hiển thị <img src="https://docs-admin.vngcloud.vn/download/thumbnails/59807124/image2023-8-7_11-14-46.png?version=1&#x26;modificationDate=1691381687000&#x26;api=v2" alt="" data-size="line"> tức là bạn đã có thể bắt đầu nhập filter thông qua Editor mode. Cú pháp nhập query giống với Suggestion mode là **Fields \<Toán tử> Value.** Ví dụ: bạn nhập http\_method.keyword = "GET" thì hệ thống sẽ tìm kiếm tất cả các bản ghi logs mà field http\_method.keyword = "GET".

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59807124/image2023-8-9_13-26-7.png?version=1&#x26;modificationDate=1691562368000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

Sau khi chọn theo **Suggestion mode** hoặc nhập theo **Editor mode**, bạn có thể :

* Nhấn **Enter** hoặc chọn biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/59807124/image2023-8-7_13-28-51.png?version=1&#x26;modificationDate=1691389732000&#x26;api=v2" alt="" data-size="line"> để thực hiện tìm kiếm logs.
* Chọn biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/59807124/image2023-8-7_13-29-31.png?version=1&#x26;modificationDate=1691389771000&#x26;api=v2" alt="" data-size="line"> nếu bạn muốn xóa tất cả điều kiện filter đã nhập/ chọn.

***

### Tình huống sử dụng <a href="#searchlogs-tinhhuongsudung" id="searchlogs-tinhhuongsudung"></a>

* #### Cú pháp đơn giản (single query) <a href="#searchlogs-cuphapdongian-singlequery" id="searchlogs-cuphapdongian-singlequery"></a>
  * Để tìm kiếm logs, bạn cần chọn/ nhập theo cú pháp  **Fields \<Toán tử> Value. Trong đó:**&#x20;
    * **Field**: danh sách các fields trong log project mà bạn đang chọn.
    * **Operator**: chúng tôi cung cấp cho bạn các phép toán được mô tả ở bảng bên dưới:&#x20;
    * **Value**: giá trị của field được gợi ý hoặc do bạn tự nhập.

<table data-header-hidden><thead><tr><th width="141"></th><th width="276"></th><th></th></tr></thead><tbody><tr><td><p><strong>Phép toán</strong></p><p><strong>(Operator)</strong></p></td><td><strong>Mô tả</strong></td><td><strong>Ví dụ minh họa</strong></td></tr><tr><td>=</td><td>equal some value </td><td>host = "ABC" - Hệ thống sẽ tìm các bản ghi logs có field host= "ABC".</td></tr><tr><td>!=</td><td>not equal some value</td><td>host != "ABC" - Hệ thống sẽ tìm các bản ghi logs có field type khác "ABC".</td></tr><tr><td>:*</td><td>exists is any form</td><td>type.keyword :* - Hệ thống sẽ tìm các bản ghi logs có tồn tại field host. (Có tồn tại tức là có xuất hiện field host trong dòng log, bất kể value của field host là gì).</td></tr><tr><td>!:*</td><td>not exists</td><td>type.keyword !:* - Hệ thống sẽ tìm các bản ghi logs không tồn tại field host. (Không tồn tại tức là không xuất hiện field host trong dòng log).</td></tr><tr><td>&#x3C;</td><td>less than some value</td><td>@timestamp &#x3C; "1690772380191" - Hệ thống sẽ tìm các bản ghi logs có field timestamp nhỏ hơn giá trị 1690772380191.</td></tr><tr><td>></td><td>greater than some value</td><td>@timestamp > "1690772380191" - Hệ thống sẽ tìm các bản ghi logs có field timestamp lớn hơn giá trị 1690772380191.</td></tr><tr><td>&#x3C;=</td><td>less than or equal to some value</td><td>@timestamp &#x3C;= "1690772380191" - Hệ thống sẽ tìm các bản ghi logs có field timestamp nhỏ hơn hoặc bằng giá trị 1690772380191.</td></tr><tr><td>>=</td><td>greater than equal to some value</td><td>@timestamp >= "1690772380191" - Hệ thống sẽ tìm các bản ghi logs có field timestamp lớn hơn hoặc bằng giá trị 1690772380191.</td></tr></tbody></table>

* #### Cú pháp phức tạp (complex query với boolean operator) <a href="#searchlogs-cuphapphuctap-complexqueryvoibooleanoperator" id="searchlogs-cuphapphuctap-complexqueryvoibooleanoperator"></a>
  * Bạn có thể kết hợp nhiều Single query vào thành một Complex query theo cú pháp **Field \<Toán tử> Value \<AND/OR> Field \<Toán tử> Value... Trong đó:**&#x20;
    * **Field**: danh sách các fields trong log project mà bạn đang chọn.
    * **Operator**: chúng tôi cung cấp cho bạn các phép toán được mô tả ở bảng bên trên.
    * **Value**: giá trị của field được gợi ý hoặc do bạn tự nhập.
    * **Boolean operator**: chúng tôi cung cấp cho bạn các phép toán nối được mô tả ở bảng bên dưới:&#x20;

<table data-header-hidden><thead><tr><th width="163"></th><th width="202"></th><th></th></tr></thead><tbody><tr><td><p><strong>Phép toán nối</strong></p><p><strong>(Operator)</strong></p></td><td><strong>Mô tả</strong></td><td><strong>Ví dụ minh họa</strong></td></tr><tr><td>AND</td><td>equal some value </td><td>http_method.keyword = "POST" AND response_code.keyword = "404" - Hệ thống sẽ tìm các bản ghi logs có field http_method.keyword = "POST" và field response_code.keyword = "404."</td></tr><tr><td>OR</td><td>not equal some value</td><td>http_method.keyword = "POST" OR response_code.keyword = "404" - Hệ thống sẽ tìm các bản ghi logs có field http_method.keyword = "POST" hoặc field response_code.keyword = "404."</td></tr></tbody></table>

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59807124/image2023-8-7_13-24-21.png?version=1&#x26;modificationDate=1691389462000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59807124/image2023-8-7_13-26-42.png?version=1&#x26;modificationDate=1691389602000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

* #### Truy vấn với cho một phần nội dung <a href="#searchlogs-truyvanvoichomotphannoidung" id="searchlogs-truyvanvoichomotphannoidung"></a>
  * Bạn có thể tìm kiếm một phần nội dung bằng cách nhập trực tiếp GET vào vùng tìm kiếm. Ví dụ: bạn nhập text GET thì hệ thống sẽ tìm kiếm tất cả các bản ghi logs mà bất kỳ một field dữ kiệu nào xuất hiện chuỗi ký tự này.

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59807124/image2023-8-7_11-22-30.png?version=1&#x26;modificationDate=1691382151000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

\
