# Volume Types

Volume Type thể hiện thông tin hiệu năng của volume. VNG Cloud sử dụng Volume Type để cung cấp tính năng QoS cho Volume. QoS giúp kiểm soát băng thông và IOPS cho từng Volume, bạn cần chọn mức QoS phù hợp với ứng dụng để ứng dụng hoạt động tốt nhất.

### **Volume QoS** <a href="#volumetypes-volumeqos" id="volumetypes-volumeqos"></a>

IOPS là chỉ số thể hiện số read/write có thể thực hiện trên volume trong mỗi giây. IOPS cao sẽ cần thiết cho các ứng dụng nhạy cảm về giao tiếp đọc ghi data ví dụ như các ứng dụng database.

Bảng sau mô tả thông tin IOPS chi tiết cho từng loại Volume Type:

| Volume Type | IOPS max    | Disk Type | Description                     |
| ----------- | ----------- | --------- | ------------------------------- |
| 200         | 200         | SSD SATA  | <p><br></p>                     |
| 400         | 400         | SSD SATA  | <p><br></p>                     |
| 800         | 800         | SSD SATA  | <p><br></p>                     |
| 1000        | 1000        | SSD SATA  | <p><br></p>                     |
| 1200        | 1200        | SSD SATA  | <p><br></p>                     |
| 1600        | 1600        | SSD SATA  | <p><br></p>                     |
| 3000        | 3000 shared | SSD SATA  | Shared IOPS with other customer |
| 3200        | 3200        | SSD SATA  | <p><br></p>                     |
| 6400        | 6400        | SSD SATA  | <p><br></p>                     |
| 10000       | 10000       | SSD SATA  | <p><br></p>                     |
| custom      | custom      | SSD SATA  | <p><br></p>                     |
| 5000        | 5000        | SSD NVMe  | <p><br></p>                     |
| 10000       | 10000       | SSD NVMe  | <p><br></p>                     |
| 20000       | 20000       | SSD NVMe  | <p><br></p>                     |
| 40000       | 40000       | SSD NVMe  | <p><br></p>                     |
| 60000       | 60000       | SSD NVMe  | <p><br></p>                     |

Bạn có thể thay đổi Volume Type bất cứ lúc nào.
