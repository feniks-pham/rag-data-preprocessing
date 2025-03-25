# Chuyển đổi đơn vị lưu trữ từ storage base 1000 sang 1024

#### 1. Thông tin cập nhật <a href="#chuyendoidonviluutrutustoragebase1000sang1024-1.thongtincapnhat" id="chuyendoidonviluutrutustoragebase1000sang1024-1.thongtincapnhat"></a>

| **Tên sản phẩm**       | vStorage                                                 |
| ---------------------- | -------------------------------------------------------- |
| Tên dịch vụ            | vStorage portal                                          |
| **Tên cập nhật**       | Chuyển đổi đơn vị lưu trữ từ storage base 1000 sang 1024 |
| **Ngày cập nhật**      | July, 01 2023                                            |
| **Phiên bản cập nhật** | Version 1.0.4                                            |

#### 2. Tính năng cập nhật <a href="#chuyendoidonviluutrutustoragebase1000sang1024-2.tinhnangcapnhat" id="chuyendoidonviluutrutustoragebase1000sang1024-2.tinhnangcapnhat"></a>

<table data-header-hidden data-full-width="true"><thead><tr><th width="84"></th><th width="171"></th><th width="223"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>STT</strong></td><td><strong>Tính năng</strong></td><td><strong>Phạm vi &#x26; giới hạn</strong></td><td><strong>Loại</strong></td><td><strong>Giá trị mang lại</strong></td></tr><tr><td>1</td><td><ul><li>Tất cả các tính năng mua mới, resize, renew, recovery sẽ chuyển qua dùng đơn vị storage base = 1024 thay vì 1000 như trước đây.</li></ul></td><td><ul><li>Áp dụng cho người dùng trả trước và trả sau.</li><li>Áp dụng cho đơn vị billing Quota, Usage.</li><li>Không áp dụng cho đơn vị billing Traffic.</li></ul></td><td>Enhancement</td><td><ul><li>Việc chuyển đổi cách tính storage base từ 1000 lên 1024 nhằm đồng nhất cách tính storage base giữa VNG Cloud và hệ thống phía khách hàng. Hiện tại quy chuẩn chung của các hệ thống khác thuộc VNG Cloud đều quy đổi từ Bytes thành KB, MB, GB theo tỉ lệ 1024.</li></ul></td></tr></tbody></table>

**Ghi chú:**

* New: tính năng mới
* Enhancement: nâng cấp tính năng đang có sẵn
* Fixed Bugs: sửa lỗi tính năng
