# Tìm kiếm object/ directory

Sau khi tạo container và tải lên tệp tin vào container đó, bạn có thể tìm kiếm object/ directory thông qua:



{% tabs %}
{% tab title="Sử dụng vStorage Portal" %}


1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **project** và **container** mà bạn muốn thực hiện tìm kiếm object/ directory.
3. Tại ô **Search directories and objects**, bạn có thể thực hiện tìm kiếm object/ directory theo các cách sau:
   1. Nếu bạn muốn tìm kiếm object theo tiền tố:
      1. Chọn Search by **Name match by prefix**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm.&#x20;
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).
   2. Nếu bạn muốn tìm kiếm theo một chuỗi ký tự bất kỳ được chứa trong tên object:
      1. Chọn Search by **Name match phrase**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm.&#x20;
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).
   3. Nếu bạn muốn tìm kiếm theo toàn bộ tên object:&#x20;
      1. Chọn Search by **Name match all**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm.&#x20;
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).
   4. Nếu bạn muốn tìm kiếm theo thông tin tags của object:\

      1. Chọn Search by **Tags**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm.&#x20;
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).

Ví dụ: nếu bạn muốn tìm kiếm các object có điểm chung là tiền tố trong tên object là **file** thì bạn cần thực hiện:

* Chọn Search by **Name match by prefix**
* Nhập tiền tố **file**
* Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2)

Bạn có thể tìm hiểu thêm cách chúng tôi tìm kiếm kết quả Search theo mỗi phương thức tại bảng bên dưới:

<table data-header-hidden data-full-width="true"><thead><tr><th width="73"></th><th width="131"></th><th width="190"></th><th width="144"></th><th></th></tr></thead><tbody><tr><td><strong>STT</strong></td><td><strong>Phương thức (Search by)</strong></td><td><strong>Cú pháp mẫu</strong></td><td><strong>Kết quả tìm kiếm</strong></td><td><strong>Giải thích ý nghĩa</strong></td></tr><tr><td>1</td><td>Name match all</td><td><p>Name match all <strong>abc.txt</strong> (object nằm trong container)</p><p>Name match all <strong>directoryA/abc.txt</strong> (object nằm trong directoryA)</p></td><td><strong>abc.txt</strong> có phân biệt hoa thường.</td><td>Tìm kiếm bằng cách so sánh chuỗi ký tự nhập vào với toàn bộ tên object.</td></tr><tr><td>2</td><td>Name match by prefix</td><td><p>Name match by prefix <strong>abc</strong> (object nằm trong container)</p><p>Name match by prefix <strong>directoryA/abc</strong> (object nằm trong directoryA)</p></td><td><strong>abc1, abc2</strong>,…có phân biệt hoa thường.</td><td>Tìm kiếm bằng cách so sánh chuỗi ký tự nhập vào với tiền tố của tên object.</td></tr><tr><td>3</td><td>Name match phase</td><td><p>Name match phase <strong>abc</strong> (object nằm trong container)</p><p>Name match phase <strong>directoryA/abc</strong> (object nằm trong directoryA)</p></td><td><strong>abc1.exe, xabce.ill, 1abc.gif,</strong>…có phân biệt hoa thường.</td><td>Tìm kiếm bằng cách so sánh chuỗi ký tự nhập có được chứa trong tên object.</td></tr><tr><td>4</td><td>Name match by wildcard</td><td><p>Name match by wildcard <strong>ab*c</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>?abc?</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>abc*.?xt</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>ab\*c.txt</strong> (object nằm trong container)</p><p>Name match by wildcard <strong>directoryA/ab*c</strong> (object nằm trong directoryA)</p><p>Name match by wildcard <strong>directoryA/?abc?</strong> (object nằm trong directoryA)</p><p>Name match by wildcard <strong>directoryA/abc*.?xt</strong> (object nằm trong directoryA)</p><p>Name match by wildcard <strong>directoryA/ab\*c.txt</strong> (object nằm trong directoryA)</p></td><td><p><strong>abc, abdc, ab)c, abUUc, ab&#x26;-Bc</strong>…có phân biệt hoa thường.</p><p><strong>1abcx, -abc*, 1abcD,…</strong> có phân biệt hoa thường.</p><p><strong>abc.txt, abc123.^xt,</strong>… có phân biệt hoa thường.</p><p><strong>ab*c.txt</strong> có phân biệt hoa thường.</p></td><td><p><strong>*</strong>: 0 tới n ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt.</p><p><strong>?</strong>: 1 ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt.</p><p><strong>\</strong>*, <strong>\</strong>?: ký tự *, ? lúc này được coi là một ký tự trong bình thường, không phải là toán tử đại diện sử dụng để search.</p></td></tr><tr><td>5</td><td><p>Name match by regex</p><p><br></p></td><td><p>Name match by regex <strong>ab.</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ab.</strong> (object nằm trong directoryA)</p></td><td><strong>ab1,ab2,ab3, abx, ab*,</strong>… có phân biệt hoa thường.</td><td><strong>.</strong>: 1 ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt.</td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex <strong>abc?</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/abc?</strong> (object nằm trong directoryA)</p></td><td><strong>ab, abc</strong> có phân biệt hoa thường.</td><td><strong>?</strong>: không lặp lại ký tự liền kề gần nhất hoặc lặp lại ký tự gần nhất 1 lần.</td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex <strong>ab+</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ab+</strong> (object nằm trong directoryA)</p></td><td><strong>ab, abb, abbb</strong>,… có phân biệt hoa thường.</td><td><strong>+</strong>: lặp lại ký tự liền kề gần nhất 1 hoặc nhiều lần.</td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex <strong>ab*</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ab*</strong> (object nằm trong directoryA)</p></td><td><strong>a, ab, abb, abbb</strong>,… có phân biệt hoa thường.</td><td><strong>*</strong>: không lặp lại ký tự liền kề gần nhất hoặc lặp lại ký tự gần nhất 1 hoặc nhiều lần.</td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex <strong>a{2}</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/a{2}</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>a{2,4}</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/a{2,4}</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>a{2,}</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/a{2,}</strong> (object nằm trong directoryA)</p></td><td><p><strong>aa</strong> có phân biệt hoa thường.</p><p><strong>aa, aaa, aaaa</strong> có phân biệt hoa thường.</p><p><strong>aa, aaa, aaaa, aaaaa,</strong>… có phân biệt hoa thường.</p></td><td><p>{}: số ký tự tối thiếu và tối đa mà ký tự liền kề gần nhất lặp lại.</p><p><br></p><p><strong>Hạn chế sử dụng số lớn trong ngoặc</strong></p></td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex <strong>abc|xyz</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/abc|xyz</strong> (object nằm trong directoryA)</p></td><td><strong>abc, xyz</strong> có phân biệt hoa thường.</td><td>| hoặc.</td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex</p><p>Name match by regex <strong>abc(xyz)</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/abc(xyz)</strong> (object nằm trong directoryA)</p></td><td><strong>abc, abcxyz</strong> có phân biệt hoa thường.</td><td>() hoặc tồn tại.</td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex <strong>[abc]</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ [abc]</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>[a-d]</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ [a-d]</strong> (object nằm trong directoryA)</p><p>Name match by regex <strong>[^abc\-]</strong> (object nằm trong container)</p><p>Name match by regex <strong>directoryA/ [^abc\-]</strong> (object nằm trong directoryA)</p></td><td><p><strong>a, b, c</strong> có phân biệt hoa thường.</p><p><strong>a, b, c, d</strong> có phân biệt hoa thường.</p><p><strong>khác a, b, c, hoặc -</strong> có phân biệt hoa thường.</p></td><td><p>[ ] một trong các ký tự trong ngoặc.</p><p>^: ngoại trừ</p><p>\: hoặc</p></td></tr><tr><td>5</td><td>Name match by regex</td><td><p>Name match by regex <strong>a{2,6}+d?*</strong></p><p>Name match by regex <strong>directoryA/ a{2,6}+d?*</strong></p><p>Name match by regex <strong>directoryA{2,6}+d?*/ a{2,6}+d?*/ a{2,6}+d?*</strong></p></td><td><strong>aaaaaaa, aaaaaaaaaaaaddddd,</strong>… có phân biệt hoa thường.</td><td>Sử dụng lồng các toán tử lại trong một cú pháp tìm kiếm regex.</td></tr><tr><td>6</td><td>Tags</td><td>Tags <strong>abc</strong></td><td>Object, directory có tags chính xác là abc</td><td>Tìm kiếm bằng tags được thiết lập trên object.</td></tr></tbody></table>
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để tìm kiếm object/ directory qua vStorage API, hãy xem [API Developers](../../api-developers/).
{% endtab %}

{% tab title="Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](../../3rd-party-softwares/) và sử dụng các công cụ này.&#x20;

Để tìm kiếm object/ directory qua 3rd party software, hãy xem [3rd party softwares](../../3rd-party-softwares/).
{% endtab %}
{% endtabs %}
