# Sử dụng tính năng container lifecycle

**Lifecycle** là một tính năng do VNG Cloud phát triển cho phép bạn thiết lập các hành động mà vStorage áp dụng cho một container. Chúng tôi định nghĩa 2 loại rule sau đây để hỗ trợ bạn quản lý vòng đời của container:

<figure><img src="../../../../../.gitbook/assets/image (389).png" alt="" width="563"><figcaption></figcaption></figure>

Trong đó:&#x20;

* **Transition rule:** Rule hỗ trợ di chuyển object giữa các storage class. Bạn có thể thực hiện thiết lập một hoặc nhiều lifecycle rule di chuyển object nếu trong vòng N ngày mà object không được truy cập.
  * Từ storage class **Gold** qua storage class **Silver**.
  * Từ storage class **Gold** qua storage class **Archive**.&#x20;
* **Expiration rule**: Rule hỗ trợ xóa các object theo điều kiện ràng buộc.  Bạn có thể thực hiện thiết lập một hoặc nhiều lifecycle rule xóa object sau một khoảng thời gian nhất định kể từ ngày object tồn tại trên hệ thống vStorage. Bạn có thể thiết lập lifecycle để:
  * Xóa object thuộc Storage Class **Gold**.
  * Xóa object thuộc Storage Class **Silver**.

{% hint style="info" %}
**Lưu ý:**

* Việc xử lý object trong một lần chạy lifecycle rule phụ thuộc vào **số lượng object** trong container được thiết lập lifecycle rule của bạn và **workload** của hệ thống chúng tôi. Nếu container có **nhiều object** hoặc hệ thống có tải cao, việc xử lý sẽ **chậm và kéo dài qua các ngày kế tiếp**. Nếu container có **ít object** hoặc hệ thống có tải thấp, việc xử lý sẽ **nhanh và có thể hoàn thành trong một ngày**. Để đảm bảo việc xử lý object diễn ra hiệu quả và nhanh chóng, bạn nên chia nhỏ các lần chạy lifecycle rule và sử dụng Bộ lọc (Filter) để giảm thiểu số lượng object cần xử lý.
* Về khả năng xử lý, hệ thống có thể chuyển tối đa <mark style="color:red;">**500,000**</mark> object mỗi ngày. Tuy nhiên, tốc độ xử lý còn phụ thuộc vào số lượng object trong container và tải của hệ thống tại thời điểm đó
* Bạn chỉ có thể tạo lifecycle rule thuộc 1 trong 2 loại (transition, expiration) trên 1 container ở 1 project bất kỳ. Ví dụ nếu bạn đã thiết lập một lifecycle rule loại transition cho container01 thì bạn không thể thiết lập một lifecycle rule khác loại expiration cho container01 nữa và ngược lại.&#x20;
* Nếu bạn thiết lập lifecycle rule loại transition cho 1 container thì bạn chỉ có thể tạo tối đa 1 transition rule.&#x20;
* Nếu bạn thiết lập lifecycle rule loại expiration cho 1 container thì bạn có thể tạo tối đa 10 expiration rule.
{% endhint %}

Để tạo một lifecycle cho container, bạn có thể thực hiện qua vStorage Portal theo hướng dẫn bên dưới:&#x20;

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **project** và chọn **container** bạn muốn thiết lập lifecycle.
3. Chọn biểu tượng <img src="../../../../../.gitbook/assets/image (390).png" alt="" data-size="line">hoặc chọn biểu tượng <img src="../../../../../.gitbook/assets/image (391).png" alt="" data-size="line">tại **container** bạn muốn thực hiện sử dụng tính năng container lifecycle và chọn <img src="../../../../../.gitbook/assets/image (392).png" alt="" data-size="line">.
4. Màn hình **Lifecycle** được hiển thị. Chọn **Tạo một quy tắc lifecycle**.
5. Nhập **Tên quy tắc Lifecycle**. Tên quy tắc Lifecycle mà chúng tôi cho phép bạn nhập bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài **Tên quy tắc Lifecycle** của bạn phải nằm trong khoảng từ 5 đến 50.
6. Chọn **Loại quy tắc** và nhập **Mô tả quy tắc** nếu c&#xF3;**.** Chúng tôi cung cấp cho bạn 2 loại quy tắc bao gồ&#x6D;**:**&#x20;
   1. Transition: Rule hỗ trợ di chuyển object giữa các storage class.&#x20;
   2. Expiration: Rule hỗ trợ xóa các object theo điều kiện ràng buộc.&#x20;
7. Nhập **Bộ lọc**. Bộ lọc này được áp dụng cho một lifecycle rule cụ thể. **Mỗi lifecycle rule chỉ được đặt 1 bộ lọc duy nhất, nếu bạn muốn áp dụng quy tắc lifecycle mà bạn đang tạo lên tất cả các object thuộc container này, hãy nhập giá trị '\*' vào trường thông tin này.** Hoặc bạn có thể lọc các object mong muốn áp dụng lifecycle rule thông qua các phương thức sau:
   1. Nếu bạn muốn tìm kiếm object theo Prefix:
      1. Chọn **Prefix**.
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm.&#x20;
   2. Nếu bạn muốn tìm kiếm object theo Wildcard:
      1. Chọn **Wildcard**.
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm.&#x20;
   3. Nếu bạn muốn tìm kiếm object theo Regex:
      1. Chọn **Regex**.
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm.&#x20;

Ví dụ: nếu bạn muốn tìm kiếm các object có điểm chung là tiền tố trong tên object là **file** thì bạn cần thực hiện nhập bộ lọc:&#x20;

* Chọn **Prefix**
* Nhập tiền tố **file**

Bạn có thể tìm hiểu thêm cách chúng tôi tìm kiếm kết quả Search theo mỗi phương thức tại bảng bên dưới:

<table data-full-width="true"><thead><tr><th width="140">Phương thức (Search by)</th><th width="335">Cú pháp mẫu</th><th width="249">Kết quả tìm kiếm</th><th>Giải thích ý nghĩa</th></tr></thead><tbody><tr><td>Name match by prefix</td><td><p>Name match by prefix <strong>abc</strong> (object nằm trong container)</p><p>Name match by prefix <strong>directoryA/abc</strong> (object nằm trong directoryA)</p></td><td><strong>abc1, abc2</strong>,…có phân biệt hoa thường.</td><td>Tìm kiếm bằng cách so sánh chuỗi ký tự nhập vào với tiền tố của tên object.</td></tr><tr><td>Name match by wildcard</td><td><p>Name match by wildcard <strong>ab*c</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>?abc?</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>abc*.?xt</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>ab\*c.txt</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>directoryA/ab*c</strong> (object nằm trong directoryA)</p><p>Name match by wildcard <strong>directoryA/?abc?</strong> (object nằm trong directoryA)</p><p>Name match by wildcard <strong>directoryA/abc*.?xt</strong> (object nằm trong directoryA)</p><p>Name match by wildcard <strong>directoryA/ab\*c.txt</strong> (object nằm trong directoryA)</p></td><td><p><strong>abc, abdc, ab)c, abUUc, ab&#x26;-Bc</strong>…có phân biệt hoa thường.</p><p><strong>1abcx, -abc*, 1abcD,…</strong> có phân biệt hoa thường.</p><p><strong>abc.txt, abc123.^xt,</strong>… có phân biệt hoa thường.</p><p><strong>ab*c.txt</strong> có phân biệt hoa thường.</p></td><td><p><strong>*</strong>: 0 tới n ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt.</p><p><strong>?</strong>: 1 ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt.</p><p><strong>\</strong>*, <strong>\</strong>?: ký tự *, ? lúc này được coi là một ký tự trong bình thường, không phải là toán tử đại diện sử dụng để search.</p></td></tr><tr><td>Name match by regex</td><td><p>Name match by regex <strong>ab.</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ab.</strong> (object nằm trong directoryA)</p></td><td><strong>ab1,ab2,ab3, abx, ab*,</strong>… có phân biệt hoa thường.</td><td><strong>.</strong>: 1 ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt.</td></tr><tr><td></td><td><p>Name match by regex <strong>abc?</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/abc?</strong> (object nằm trong directoryA)</p></td><td><strong>ab, abc</strong> có phân biệt hoa thường.</td><td><strong>?</strong>: không lặp lại ký tự liền kề gần nhất hoặc lặp lại ký tự gần nhất 1 lần.</td></tr><tr><td></td><td><p>Name match by regex <strong>ab+</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ab+</strong> (object nằm trong directoryA)</p></td><td><strong>ab, abb, abbb</strong>,… có phân biệt hoa thường.</td><td><strong>+</strong>: lặp lại ký tự liền kề gần nhất 1 hoặc nhiều lần.</td></tr><tr><td></td><td><p>Name match by regex <strong>ab*</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ab*</strong> (object nằm trong directoryA)</p></td><td><strong>a, ab, abb, abbb</strong>,… có phân biệt hoa thường.</td><td><strong>*</strong>: không lặp lại ký tự liền kề gần nhất hoặc lặp lại ký tự gần nhất 1 hoặc nhiều lần.</td></tr><tr><td></td><td><p>Name match by regex <strong>a{2}</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/a{2}</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>a{2,4}</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/a{2,4}</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>a{2,}</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/a{2,}</strong> (object nằm trong directoryA)</p></td><td><p><strong>aa</strong> có phân biệt hoa thường.</p><p><strong>aa, aaa, aaaa</strong> có phân biệt hoa thường.</p><p><strong>aa, aaa, aaaa, aaaaa,</strong>… có phân biệt hoa thường.</p></td><td><p>{}: số ký tự tối thiếu và tối đa mà ký tự liền kề gần nhất lặp lại.</p><p><br></p><p><strong>Hạn chế sử dụng số lớn trong ngoặc</strong></p></td></tr><tr><td></td><td><p>Name match by regex <strong>abc|xyz</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/abc|xyz</strong> (object nằm trong directoryA)</p></td><td><strong>abc, xyz</strong> có phân biệt hoa thường.</td><td>| hoặc.</td></tr><tr><td></td><td><p>Name match by regex</p><p>Name match by regex <strong>abc(xyz)</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/abc(xyz)</strong> (object nằm trong directoryA)</p></td><td><strong>abc, abcxyz</strong> có phân biệt hoa thường.</td><td>() hoặc tồn tại.</td></tr><tr><td></td><td><p>Name match by regex <strong>[abc]</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ [abc]</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>[a-d]</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ [a-d]</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>[^abc\-]</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ [^abc\-]</strong> (object nằm trong directoryA)</p></td><td><p><strong>a, b, c</strong> có phân biệt hoa thường.</p><p><strong>a, b, c, d</strong> có phân biệt hoa thường.</p><p><strong>khác a, b, c, hoặc -</strong> có phân biệt hoa thường.</p></td><td><p>[ ] một trong các ký tự trong ngoặc.</p><p>^: ngoại trừ</p><p>\: hoặc</p></td></tr><tr><td></td><td><p>Name match by regex <strong>a{2,6}+d?*</strong></p><p>Name match by regex <strong>directoryA/ a{2,6}+d?*</strong></p><p>Name match by regex <strong>directoryA{2,6}+d?*/ a{2,6}+d?*/ a{2,6}+d?*</strong></p></td><td><strong>aaaaaaa, aaaaaaaaaaaaddddd,</strong>… có phân biệt hoa thường.</td><td>Sử dụng lồng các toán tử lại trong một cú pháp tìm kiếm regex.</td></tr></tbody></table>

Khi bạn chọn:&#x20;

<details>

<summary>Transition</summary>

Transition rule sẽ di chuyển các object thỏa điều kiện nhất định từ storage class Gold qua storage class Silver hoặc từ từ storage class Gold qua storage class Archive. Hiện tại tính năng transition chỉ hỗ trợ cho:

* **Chuyển object đối với tài khoản khách hàng trả sau.**
* **Chuyển object từ Gold container sang Silver container.**
* **Chuyển object từ Gold container sang Archive container.**

8\. Chọn vị trí và thời điểm mà các object được di chuyển

* **Transition to:** chọn vStorage Silver hoặc vStorage Archive.
* Sau đó nhập **số ngày kể từ lần cuối object được truy cập** (Request Get / Tải xuống).

Sau khi bạn thực hiện tạo mới Lifecycle rule loại transition thành công,&#x20;

* Nếu bạn chọn **Transition to: vStorage Silver**, hệ thống vStorage sẽ tự động tạo một container với hậu tố tier. Container này sẽ được sử dụng làm nơi lưu trữ các object được transit.  Ví dụ khi bạn tạo lifecycle rule loại **Transition to: vStorage Silver** cho Container01  thì hệ thống sẽ tự động tạo Container01\_tier (storage class Silver). Trong vòng **5h** kể từ khi lifecycle rule được tạo, hệ thống vStorage sẽ thực hiện chạy rule, các object thỏa mãn điều kiện sẽ được di chuyển từ Container01 sang Container01\_tier với URL object không thay đổi.
* Nếu bạn chọn **Transition to: vStorage Archive**, hệ thống vStorage sẽ tự động tạo một container với hậu tố archive\_tier. Container này sẽ được sử dụng làm nơi lưu trữ các object được transit.  Ví dụ khi bạn tạo lifecycle rule loại **Transition to: vStorage Archive** cho Container01  thì hệ thống sẽ tự động tạo Container01\_archive\_tier (storage class archive). Trong vòng **5h** kể từ khi lifecycle rule được tạo, hệ thống vStorage sẽ thực hiện chạy rule, các object thỏa mãn điều kiện sẽ được di chuyển từ Container01 sang Container01\_archive\_tier với URL object không thay đổi.

</details>

<details>

<summary>Expiration</summary>

Expiration rule sẽ xóa các object thuộc container theo các điều kiện ràng buộc nhất định. Hiện tại tính năng expiration hỗ trợ cho:

* **Xóa object đối với cả tài khoản khách hàng trả trước và tài khoản khách hàng trả sau.**
* **Xóa object thuộc Gold container, Silver container và Archive container. (Đối với Archive container, số ngày tối thiểu có thể thực hiện xóa object là 180 ngày).**

8\. Chọn hành động xảy ra với object tại container mà bạn chọn, bao gồm:

* **Expire phiên bản hiện tại của các object (Expire current version of objects):** sử dụng khi bạn muốn thiết lập xóa object thuộc container gốc đang thiết lập lifecycle rule sau một khoảng thời gian kể từ ngày object tồn tại trên hệ thống vStorage. Rule này áp dụng cho việc xóa object ở các container không phải versioning. Khi bạn chọn thiết lập này, bạn cần nhập số ngày kể từ khi khởi tạo object.

- **Xóa vĩnh viễn các phiên bản trước đó (Permanently delete previous versions):** sử dụng khi bạn muốn thiết lập xóa object thuộc container version tương ứng của container gốc đang thiết lập lifecycle rule sau một khoảng thời gian kể từ lúc object version được sinh ra. Rule này áp dụng cho việc xóa object ở container versioning. Khi bạn chọn thiết lập này, bạn cần nhập số ngày kể từ khi object trở thành phiên bản cũ (tức object tồn tại trong container version).

* **Expire các object được đánh dấu là xóa (Expire marked-deleted objects):** sử dụng khi bạn muốn thiết lập xóa các tệp tin delete marked sinh ra trong các container version. (Tệp tin delete marked là các tệp tin sinh ra khi bạn thực hiện xóa object thuộc container gốc mà container gốc này đã được bật versioning). Rule này áp dụng cho việc xóa object ở container versioning.

Sau khi bạn thực hiện tạo mới Lifecycle rule loại expiration thành công, trong vòng 2h kể từ khi lifecycle rule được tạo, hệ thống vStorage sẽ thực hiện chạy rule, các object thỏa mãn điều kiện sẽ được xóa.

_**Tham khảo 2 ví dụ bên dưới để hiểu cơ chế hoạt động của expiration rule:**_&#x20;

_**Ví dụ 1:** bạn đã tạo container01 (container01 chưa được bạn bật tính năng container versioning). Lúc này bạn có nhu cầu thiết lập 1 rule theo quy tắc: nếu 60 ngày mà các object không được truy cập thì hệ thống thực hiện xóa. Lúc này bạn sẽ thiết lập quy tắc expiration như sau:_&#x20;

![](<../../../../../.gitbook/assets/image (396).png>)

_Trong vòng 2h kể từ khi lifecycle rule này được tạo, hệ thống vStorage sẽ thực hiện chạy rule, kiểm tra các object trong container01 và xóa các object thỏa mãn điều kiện 60 ngày không được truy cập._&#x20;

_**Ví dụ 2:** bạn đã tạo container01 (container01 đã được bạn bật tính năng container versioning). Lúc này bạn có nhu cầu thiết lập 1 rule theo quy tắc: nếu 60 ngày mà các object không được truy cập thì hệ thống thực hiện xóa. Lúc này bạn sẽ thiết lập quy tắc expiration như sau:_&#x20;

![](<../../../../../.gitbook/assets/image (397).png>)

_Trong vòng 2h kể từ khi lifecycle rule này được tạo, hệ thống vStorage sẽ thực hiện chạy rule, kiểm tra các object trong container01, container01\_version và thực hiện:_

* _Xóa các object thuộc container01 thỏa mãn điều kiện 60 ngày không được truy cập._&#x20;
* _Xóa các object thuộc container01\_version thỏa mãn điều kiện 60 ngày trở thành phiên bản cũ (tức object tồn tại trong container01\_version đủ 60 ngày)._
* _Xóa các tệp tin delete marker sinh ra ở container01\_version._&#x20;

</details>

