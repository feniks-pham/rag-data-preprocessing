# Global load balancer

Global Load Balancer (GLB) là một công cụ phân phối lưu lượng mạng trên quy mô đa vùng địa lý. Khác với Load Balancer truyền thống chỉ hoạt động trong một vùng (region) hoặc một mạng cục bộ, GLB có khả năng phân phối lưu lượng đến các máy chủ nằm rải rác trên nhiều vùng địa lý khác nhau.

## Tại sao nên sử dụng GLB?

* **Tầm nhìn toàn cầu:** Cho phép bạn phân phối lưu lượng đến các máy chủ nằm rải rác trên nhiều vùng địa lý khác nhau.
* **Tăng hiệu suất:** Giảm thời gian phản hồi cho người dùng bằng cách định tuyến yêu cầu đến máy chủ gần nhất.
* **Độ tin cậy cao:** Phân tán rủi ro, đảm bảo dịch vụ không bị gián đoạn khi một vùng gặp sự cố.
* **Mở rộng quy mô:** Dễ dàng thêm hoặc xóa các máy chủ vào pool mà không ảnh hưởng đến hoạt động của hệ thống.
* **Linh hoạt:** Dễ dàng cấu hình và quản lý các Global Pool, cho phép bạn linh hoạt điều chỉnh cấu hình cân bằng tải theo nhu cầu.
* **Tối ưu hóa chi phí:** Sử dụng hiệu quả các tài nguyên máy chủ bằng cách phân bổ tải đều.

## So sánh với Load Balancer truyền thống

| Tính năng         | LB truyền thống                | GLB                                                                         |
| ----------------- | ------------------------------ | --------------------------------------------------------------------------- |
| Phạm vi hoạt động | Trong một mạng VPC             | Trên nhiều vùng (region)                                                    |
| Mục tiêu          | Cân bằng tải trong một khu vực | Cân bằng tải trên quy mô đa vùng địa lý, tối ưu hóa hiệu suất và độ tin cậy |
| Khả năng mở rộng  | Hạn chế                        | Linh hoạt, dễ dàng mở rộng quy mô                                           |
| Độ phức tạp       | Thấp                           | Cao hơn nhưng đi kèm với nhiều tính năng nâng cao                           |

## Các tính năng chính

* [Tạo và quản lý Network GLB](network-glb/)
* [Quản lý truy cập GLB](quan-ly-truy-cap.md)
* [Giám sát hoạt động GLB](giam-sat-hoat-dong.md)
