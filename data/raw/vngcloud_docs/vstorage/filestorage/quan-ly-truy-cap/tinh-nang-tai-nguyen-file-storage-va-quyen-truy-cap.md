# Tính năng, tài nguyên File Storage và quyền truy cập

**Tài nguyên File Storage được hỗ trợ phân quyền truy cập:**

* File Storage

***

**Tính năng File Storage và quyền cần để thực hiện tính năng:**

Chúng tôi cung cấp cho bạn 3 nhóm quyền chính (List, Read, Write) với ý nghĩa được mô tả ở bảng bên dưới:

<table data-full-width="true"><thead><tr><th width="304">Action</th><th width="401">Mục đích sử dụng</th><th>Resource</th></tr></thead><tbody><tr><td>ListFileStorage</td><td>Lấy danh sách các file storage</td><td>N/A</td></tr><tr><td>ListTag</td><td>Lấy danh sách tag trên từng file storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>GetFileStorage</td><td>Lấy thông tin chi tiết một file storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>GetMountGuide</td><td>Lấy thông tin mount target</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>CreateFileStorage</td><td>Tạo mới một file storage</td><td>N/A</td></tr><tr><td>CreateFileStorageTag</td><td>Tạo mới một tag cho file storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>ResizeFileStorage</td><td>Thay đổi kích thước max quota của một File Storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>EditFileStorage</td><td>Chỉnh sửa một file storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>EditFileStorageTag</td><td>Chỉnh sửa tag của một file storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>DeleteFileStorage</td><td>Xóa một file storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr><tr><td>DeleteFileStorageTag</td><td>Xóa tag của một file storage</td><td><ul><li>All resource hoặc theo từng resource file-storage-id cụ thể</li></ul></td></tr></tbody></table>
