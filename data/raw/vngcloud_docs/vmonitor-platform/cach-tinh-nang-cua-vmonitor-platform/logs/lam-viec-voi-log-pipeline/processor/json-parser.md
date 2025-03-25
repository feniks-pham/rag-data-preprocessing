# JSON Parser

### Tổng quan

Grok parser là một bộ lọc (filter) giúp phân tích và cấu trúc hóa dữ liệu có định dạng JSON. Json parser sử dụng thư viện Json để chuyển đổi một field chứa JSON thành một cấu trúc dữ liệu thực trong logs.

***

### Cấu hình JSON parser

Để tạo cấu hình Grok parser, hãy làm theo hướng dẫn bên dưới:&#x20;

1. Tại mục **Processor information**, nhập các thông tin chung cho một processor theo hướng dẫn tại [Processor](./). Trong nội dung này thì bạn sẽ chọn **Processor type** là **JSON Parser**.
2. Tại mục **Parsing rule**, nhập các thông tin sau đây:

* Nhập **Source field**: field chứa logs sẽ cần parse.
* Nhập **Target field**: field sẽ được ghi đè bên destination log project, thông thường bạn sẽ không cần nhập thông tin này.
* Chọn **Skip on invalid JSON** nếu bạn muốn bỏ qua parser source field không đúng định dạng logs là JSON.

Ví dụ:&#x20;

| Source log project | Destination log project | Message (field logs mà chúng tôi thực hiện parser)                                                                                                                                                  | Kết quả parser                                                                                                                                                                                                             |
| ------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| webserver          | webserver-parse         | <pre><code>{\"timestamp\":\"2023-07-23T12:34:56Z\",\"level\":\"error\",
\"message\":\"Therewasanerrorprocessingtherequest\",
\"request_id\":\"1234567890\",\"user_id\":\"vngcloud1\"}
</code></pre> | <p>{<br>     "timestamp": "2023-07-23T12:34:56Z",<br>     "level": "error",<br>      "message": "There was an error processing the request",<br>      "request_id": "1234567890",<br>      "user_id": "vngcloud1"<br>}</p> |

<figure><img src="../../../../../.gitbook/assets/image (323).png" alt=""><figcaption></figcaption></figure>

***

### Lưu trữ và tái sử dụng Parsing rule

* Bạn có thể lưu trữ một parsing rule bằng cách tích chọn vào **Save this rule**, sau đó nhập tên gợi nhớ cho parsing rule mà bạn muốn lưu trữ. Tên gợi nhớ có chiều dài tối thiểu là 5 ký tự, chiều dài tối đa là 255 ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Sau khi parsing rule đã được lưu trữ, trong các lần tạo processor kế tiếp bạn có thể tái sử dụng rule này bằng cách chọn **Rule presets** tại mục Pasing rule. .
