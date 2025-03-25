# Release Leaked Segment Detecting & Deleting Tool

#### 1. Thông tin release <a href="#releaseleakedsegmentdetecting-and-deletingtool-1.thongtinrelease" id="releaseleakedsegmentdetecting-and-deletingtool-1.thongtinrelease"></a>

| **Tên sản phẩm**      | vStorage                                   |
| --------------------- | ------------------------------------------ |
| **Tên release**       | Leaked segment detecting and deleting tool |
| **Ngày release**      | Nov 2022                                   |
| **Phiên bản release** | vos-leak-segment-v1.0.0                    |

#### 2. Tính năng release <a href="#releaseleakedsegmentdetecting-and-deletingtool-2.tinhnangrelease" id="releaseleakedsegmentdetecting-and-deletingtool-2.tinhnangrelease"></a>

<table data-header-hidden data-full-width="true"><thead><tr><th width="84"></th><th width="207"></th><th width="271"></th><th></th><th></th></tr></thead><tbody><tr><td>STT</td><td><strong>Tính năng</strong></td><td><strong>Phạm vi &#x26; giới hạn</strong></td><td><strong>Loại</strong></td><td><strong>Giá trị mang lại</strong></td></tr><tr><td>1</td><td><ul><li>Xử lý segment rác trong module upload/ reupload file qua S3API, S3 Client Tool.</li></ul></td><td><ul><li>Đối với module upload/ reupload qua Web Portal phải tự xử lý việc sinh ra các segment rác nên không xử lý trong tool này.</li><li>Các tính năng container versioning, copy multipart bằng phương thức GET, xóa object thông qua xóa manifest file mà không xóa segment có thể sinh ra segment rác nhưng tool này không xử lý segment rác sinh ra (nếu có) cho các tính năng này.</li></ul></td><td>New</td><td><br></td></tr></tbody></table>

**Ghi chú:**

* New: tính năng mới
* Enhancement: nâng cấp tính năng đang có sẵn
* Fixed Bugs: sửa lỗi tính năng
