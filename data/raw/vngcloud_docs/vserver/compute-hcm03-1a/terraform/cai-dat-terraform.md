# Cài đặt Terraform

## **Cài đặt Terraform**  <a href="#caidatterraform-caidatterraform" id="caidatterraform-caidatterraform"></a>

Để sử dụng Terraform, bạn sẽ cần cài đặt nó (Bạn có thể cài đặt Terraform theo hướng dẫn tại [trang chủ Terrafrom](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) hoặc có thể cài đặt theo bài viết bên dưới của chúng tôi).

HashiCorp phân phối Terraform dưới dạng **binary package**. Bạn cũng có thể cài đặt Terraform bằng các trình quản lý gói phổ biến.



**Bước 1**: Cài đặt Terraform



**Bước 1.1:** Truy xuất `TERRAFORM` `binary` bằng cách tải xuống Pre-complied binary hoặc Compile from source theo hướng dẫn bên dưới :

#### **Pre-complied binary** <a href="#caidatterraform-pre-compliedbinary" id="caidatterraform-pre-compliedbinary"></a>

Để cài đặt `TERRAFORM`, hãy [tìm gói thích hợp](https://developer.hashicorp.com/terraform/downloads) cho hệ thống của bạn và tải xuống dưới dạng tệp nén zip.

Sau khi tải xuống Terraform, hãy giải nén gói. Terraform chạy dưới dạng một địa hình nhị phân có tên duy nhất là `TERRAFORM` . Bất kỳ tệp nào khác trong gói có thể được xóa một cách an toàn và Terraform sẽ vẫn hoạt động.

Cuối cùng, đảm bảo rằng `TERRAFORM` `binary` có sẵn trên PATH của bạn. Quá trình này sẽ khác nhau tùy thuộc vào hệ điều hành của bạn.

#### **Pre-complied binary** <a href="#caidatterraform-pre-compliedbinary.1" id="caidatterraform-pre-compliedbinary.1"></a>

Để biên dịch tệp nhị phân Terraform từ nguồn, hãy sao chép kho lưu trữ [HashiCorp Terraform](https://github.com/hashicorp/terraform).

| `git clone https://github.com/hashicorp/terraform.git` |
| ------------------------------------------------------ |

Điều hướng đến thư mục mới.

| `cd terraform` |
| -------------- |

Sau đó, biên dịch binary. Lệnh này sẽ biên dịch tệp binary và lưu trữ nó trong _$GOPATH/bin/terraform_.

| `go install` |
| ------------ |

Cuối cùng, đảm bảo rằng `TERRAFORM binary` có sẵn trên PATH của bạn. Quá trình này sẽ khác nhau tùy thuộc vào hệ điều hành của bạn.



**Bước 1.2: Cài đặt trên Mac or Linux:**

In danh sách các vị trí được phân tách bằng dấu hai chấm trong PATH của bạn.

| `echo $PATH` |
| ------------ |

Di chuyển Terraform binary đến một trong các vị trí được liệt kê. Lệnh này giả định rằng tệp nhị phân hiện có trong thư mục tải xuống của bạn và PATH của bạn bao gồm /usr/local/bin, nhưng bạn có thể tùy chỉnh nó nếu vị trí của bạn khác.

| `sudo mv ~/Downloads/terraform /usr/local/bin/` |
| ----------------------------------------------- |

Để biết thêm chi tiết về việc thêm các binaries vào binary path của bạn, hãy xem bài viết về [Stack Overflow ](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)này.



**Bước 1.3: Cài đặt trên Window**

Bài viết về [Stack Overflow](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows) này chứa hướng dẫn đặt PATH trên Windows thông qua giao diện người dùng.



## **Xác minh cài đặt**

Xác minh rằng quá trình cài đặt đã hoạt động bằng cách mở một phiên cuối mới và liệt kê các tiểu ban có sẵn của Terraform.

```
terraform -help
Usage: terraform [-version] [-help] <command> [args]
 
The available commands for execution are listed below.
The most common, useful commands are shown first, followed by
less common or more advanced commands. If you're just getting
started with Terraform, stick with the common commands. For the
other commands, please read the help and docs before usage.
#...
```

Thêm bất kỳ lệnh con nào vào TERRAFORM -HELP để tìm hiểu thêm về chức năng của lệnh này và các tùy chọn khả dụng.

```
terraform -help plan
```

## **Khắc phục sự cố** <a href="#caidatterraform-khacphucsuco" id="caidatterraform-khacphucsuco"></a>

Nếu bạn gặp lỗi không thể tìm thấy địa hình, biến môi trường PATH của bạn không được thiết lập đúng cách. Vui lòng quay lại và đảm bảo rằng biến PATH của bạn chứa thư mục cài đặt Terraform.

### **Bật Tab hoàn thành** <a href="#caidatterraform-battabhoanthanh" id="caidatterraform-battabhoanthanh"></a>

Nếu bạn sử dụng Bash hoặc Zsh, bạn có thể bật hoàn thành tab cho các lệnh Terraform. Để bật tính năng tự động hoàn thành, trước tiên hãy đảm bảo rằng tệp cấu hình tồn tại cho trình bao bạn đã chọn.

**Bash**

```
touch ~/.bashrc
```

**Zsh**

```
touch ~/.zshrc
```

Sau đó cài đặt gói tự động hoàn thành.

```
terraform -install-autocomplete
```

Sau khi hỗ trợ tự động hoàn thành được cài đặt, bạn sẽ cần khởi động lại Shell của mình.

***

## **Hướng dẫn bắt đầu nhanh** <a href="#caidatterraform-huongdanbatdaunhanh" id="caidatterraform-huongdanbatdaunhanh"></a>

Bây giờ bạn đã cài đặt Terraform, bạn có thể cung cấp máy chủ NGINX trong vòng chưa đầy một phút bằng cách sử dụng [Docker ](https://www.docker.com/products/docker-desktop/)trên Mac, Windows hoặc Linux. Bạn cũng có thể làm theo phần còn lại của hướng dẫn này trong trình duyệt web của mình.

**Bước 1**: Nhấp vào (các) tab bên dưới có liên quan đến hệ điều hành của bạn.

**Docker Desktop for Mac**

Tải [Docket Desktop cho Mac](https://docs.docker.com/desktop/install/mac-install/)

Sau khi bạn cài đặt Terraform và Docker trên máy cục bộ của mình, hãy khởi động Docker Desktop.

```
open -a Docker
```

**Docker Desktop for Window**

Để chạy Docker trên máy Windows 10 của bạn, bạn phải sử dụng Hệ thống con Windows cho Linux (WSL2). [Tải xuống và cài đặt WSL2 ](https://learn.microsoft.com/en-us/windows/wsl/install)trước khi tiếp tục.

Tải xuống [Docker Desktop cho Windows](https://docs.docker.com/desktop/install/windows-install/).

Sau khi bạn cài đặt Terraform và Docker trên máy cục bộ của mình, hãy khởi động Docker Desktop bằng cách tìm kiếm Docker từ Menu Bắt đầu của bạn và chọn Docker Desktop trong kết quả tìm kiếm. Khi biểu tượng cá voi trên thanh trạng thái vẫn ổn định, Docker Desktop đang hoạt động và có thể truy cập được từ bất kỳ cửa sổ đầu cuối nào.

Để biết thêm thông tin về các yêu cầu của Docker Desktop dành cho Windows, hãy truy cập [tài liệu Docker](https://docs.docker.com/desktop/install/windows-install/#start-docker-desktop)

**Docker Engine for Linux**

Để làm theo hướng dẫn này trên Linux, trước tiên hãy cài đặt [Docker Engine](https://docs.docker.com/engine/install/) cho bản phân phối của bạn.

**Bước 2**: Tạo một thư mục có tên _learn-terraform-docker-container_.

```
mkdir learn-terraform-docker-container
```

Thư mục làm việc này chứa các tệp cấu hình mà bạn viết để mô tả cơ sở hạ tầng mà bạn muốn Terraform tạo và quản lý. Khi bạn khởi tạo và áp dụng cấu hình tại đây, Terraform sử dụng thư mục này để lưu trữ các plugin, mô-đun cần thiết (cấu hình được viết sẵn) và thông tin về cơ sở hạ tầng thực mà nó đã tạo.

**Bước 3:** Điều hướng vào thư mục làm việc.

```
cd learn-terraform-docker-container
```

Trong thư mục làm việc, tạo một tệp có tên **`main.tf`** và dán cấu hình Terraform (Server, Container, LB) vào sau đó.

\
