# Date Parser

### Tổng quan

Date Parser là một bộ lọc giúp phân tích và chuyển đổi các chuỗi ký tự biểu diễn ngày tháng sang một định dạng khác, thường là một đối tượng ngày tháng (date object) có thể sử dụng được trong các ngôn ngữ lập trình.

***

### Cấu hình Date Parser

Để cáu hình Date Parser, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Tại mục **Processor information**, nhập các thông tin chung cho một processor theo hướng dẫn tại [Processor](./). Trong nội dung này thì bạn sẽ chọn **Processor type** là **Date Parser**.
2. Tại mục **Parsing rule**, nhập các thông tin sau đây:

* Nhập **Source field**: field chứa logs sẽ cần parse.
* Nhập **Locate:** ngôn ngữ được sử dụng cho định dạng date mà bạn mong muốn. Locale ảnh hưởng đến cách hiển thị và sắp xếp thứ, ngày, tháng và các ký tự phân cách, ví dụ năm-tháng-ngày, ngày-tháng-năm hoặc tháng-ngay-nam.
* Nhập **Timezone:** múi giờ của một vùng địa lý. Timezone ảnh hưởng đến giá trị của ngày tháng, bởi vì cùng một thời điểm có thể có giá trị ngày tháng khác nhau tùy thuộc vào múi giờ. Nếu bạn không lựa chọn **Locale** và **Timezone** thì chúng tôi sẽ mặc định lấy Locale và Timezone của hệ thống.
* Nhập **Target field**: field sẽ được ghi đè bên destination log project, thông thường bạn sẽ không cần nhập thông tin này&#x20;
* Nhập **Pattern:** chứa date pattern để matching với source field và parse ra theo cấu trúc.&#x20;

Ví dụ:&#x20;

<table data-full-width="true"><thead><tr><th>Items</th><th>Value</th><th>Ý nghĩa</th><th>Source logs</th><th>Destination logs</th></tr></thead><tbody><tr><td><strong>Source field</strong></td><td>date</td><td>Field nguồn cần parser là <strong>date</strong>.</td><td>{ "date":"Apr 17 09:32:01 }</td><td>{"date":"2023-08-01T07:45:11.130Z",}</td></tr><tr><td><strong>Locate</strong></td><td>Vietnamese</td><td>Ngôn ngữ sử dụng là <strong>Vietnamese</strong>.</td><td>nt</td><td>nt</td></tr><tr><td><strong>Timezone</strong></td><td>N/A</td><td>Múi giờ lấy theo hệ thống.</td><td>nt</td><td>nt</td></tr><tr><td><strong>Target field</strong></td><td>date_parser</td><td>Field được parser sẽ ghi đè vô Destination log ở field <strong>date_parser</strong>.</td><td>nt</td><td>nt</td></tr><tr><td><strong>Pattern</strong></td><td>yyyy-MM-dd'T'HH:mm:ss.SSSZ</td><td>Định dạng ngày tháng của field <strong>date</strong>.</td><td>nt</td><td>nt</td></tr></tbody></table>

<figure><img src="../../../../../.gitbook/assets/image (326).png" alt=""><figcaption></figcaption></figure>

***

### Lưu trữ và tái sử dụng Parsing rule

* Bạn có thể lưu trữ một parsing rule bằng cách tích chọn vào **Save this rule**, sau đó nhập tên gợi nhớ cho parsing rule mà bạn muốn lưu trữ. Tên gợi nhớ có chiều dài tối thiểu là 5 ký tự, chiều dài tối đa là 255 ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Sau khi parsing rule đã được lưu trữ, trong các lần tạo processor kế tiếp bạn có thể tái sử dụng rule này bằng cách chọn **Rule presets** tại mục Pasing rule.&#x20;
