# Route Table

Trong môi trường đám mây, Route table là một thành phần quan trọng trong dịch vụ quản lý mạng, cho phép điều hướng lưu lượng mạng giữa các tài nguyên trong một mạng ảo hoặc mạng riêng ảo trong đám mây.

**Route table** là một bảng dữ liệu trong mạng máy tính được sử dụng để quyết định cách điều hướng lưu lượng mạng giữa các mạng, máy tính hoặc thiết bị trong hệ thống mạng. Nó chứa các bản ghi định tuyến (route entries) mô tả các con đường mạng và các giao diện mạng liên kết với nhau. Mỗi bản ghi định tuyến trong route table bao gồm thông tin về địa chỉ mạng đích, giao diện ra, và những thông số khác để quyết định con đường mạng mà gói tin sẽ được đi qua.

**Route** là một mục đích cụ thể trong route table, xác định cách mà gói tin mạng sẽ được điều hướng từ nguồn đến đích. Nó bao gồm các thông tin như địa chỉ mạng đích, địa chỉ mạng tiếp theo (next-hop), và các thuộc tính khác như metric (đo lường độ ưu tiên) và giao diện ra (outgoing interface). Mỗi bản ghi định tuyến trong route table đại diện cho một route duy nhất, quyết định cách mà gói tin sẽ được chuyển tiếp từ nguồn đến đích thông qua các giao diện mạng.

Tổng quan, route table là một cấu trúc dữ liệu chứa các bản ghi định tuyến, trong khi route là một bản ghi cụ thể trong route table mô tả cách điều hướng lưu lượng mạng từ nguồn đến đích. Sự kết hợp của route table và các route entries trong nó giúp điều phối và quản lý việc điều hướng gói tin mạng trong hệ thống mạng.

***

### **Làm việc với Route table** <a href="#routetable-lamviecvoiroutetable" id="routetable-lamviecvoiroutetable"></a>

#### **Tạo Route table** <a href="#routetable-taoroutetable" id="routetable-taoroutetable"></a>

Sử dụng hướng dẫn bên dưới để tạo mới một Route table

1. Mở trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview).
2. Tại thanh menu điều hướng, chọn **Tab Network/ Route table.**
3. Nhấn **Tạo Route table.**
4. Đối với **Tên** hãy nhập tên mô tả cho Route table. Tên Route table có thể bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào nằm trong khoảng từ 5 đến 50. Nó không được bao gồm khoảng trắng ở đầu hoặc ở cuối.
5. Chọn **VPC** cho Route table của bạn, nếu chưa có VPC cần tạo mới một VPC theo hướng dẫn tại [Trang VPC](virtual-private-cloud-vpc/).
6. Nhấn **Create** để tạo mới Route table.

#### **Thêm, xoá, sửa Route**  <a href="#routetable-them-xoa-suaroute" id="routetable-them-xoa-suaroute"></a>

Bạn có thể thêm, xóa và sửa đổi các Route trong Route table của mình. Bạn chỉ có thể sửa đổi các Route mà bạn đã thêm:

Để cập nhật các Route cho Route table bằng bảng điều khiển:

1. Mở trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview).
2. Tại thành menu điều hướng, chọn **Tab Network/ Route table.**
3. Chọn một Route table, nhấn **Chỉnh sửa Routes.**
4.  Sau đó tại phần thêm mới **Route** hãy nhập vào các thông tin bên dướ&#x69;**:**\


    | Destination      | `Target`      |
    | ---------------- | ------------- |
    | ex: 10.21.0.0/24 | ex: 10.21.0.0 |

    Đối với Destination, hãy nhập **Destination CIDR.**

    Đối với Target, hãy nhập **Target CIDR.**
5. Để sửa đổi một Route, đối với Destination, hãy thay thế khối CIDR đích hoặc một địa chỉ IP. Đối với Target, hãy nhập một Target CIDR.
6. Để xóa một Route, hãy chọn **Xóa**.
7. Chọn **Lưu** thay đổi.

#### **Xoá Route table** <a href="#routetable-xoaroutetable" id="routetable-xoaroutetable"></a>

Bạn có thể xoá Route table nếu không còn nhu cầu sử dụng nó, để xoá Route table bằng bảng định tuyến:

1. Mở trang chủ vServer tại: [https://hcm-3.console.vngcloud.vn/vserver/overview](https://hcm-3.console.vngcloud.vn/vserver/overview).
2. Tại thành menu điều hướng, chọn **Tab Network/ Route table.**
3. Chọn Route table cần xoá, sau đó chọn hành động **Xoá.**
4. Nhấ**n Xác nhận.**
