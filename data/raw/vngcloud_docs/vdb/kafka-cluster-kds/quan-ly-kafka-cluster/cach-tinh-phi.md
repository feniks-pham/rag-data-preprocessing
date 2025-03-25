# Cách tính phí

Cách tính phí đối với vDB Kafka Cluster dựa trên số lượng broker của một cụm Kafka, trong đó mỗi broker bao gồm các thành phần sau:

1. **Compute:** Chi phí tính toán dựa trên cấu hình CPU và RAM của mỗi broker.
2. **Storage:** Chi phí lưu trữ dựa trên dung lượng đĩa mà bạn cấp phát cho mỗi broker.
3. **Encryption Volume (nếu có):** Nếu bạn sử dụng tính năng mã hóa dữ liệu, có thể có thêm chi phí cho dung lượng lưu trữ được mã hóa.

**Công thức tính phí tổng:**

```
Tổng chi phí = (Chi phí mỗi broker) x (Số lượng broker)
```

**Chi phí mỗi broker:**

```
Chi phí mỗi broker = (Chi phí compute) + (Chi phí storage) + (Chi phí encryption volume, nếu có)
```

**Ví dụ:**

Giả sử bạn có một cụm Kafka với 3 broker, mỗi broker có cấu hình sau:

* Compute: 4 CPU, 16GB RAM
* Storage: 100GB
* Encryption Volume: Không sử dụng

Và VNG Cloud có bảng giá như sau:

* Compute (4 CPU, 16GB RAM): 1,500,000 VND/tháng
* Storage: 2,000 VND/GB/tháng

**Tính toán chi phí:**

* Chi phí compute mỗi broker: 1,500,000 VND
* Chi phí storage mỗi broker: 100GB x 2,000 VND/GB/tháng = 200,000 VND
* Chi phí mỗi broker: 1,500,000 VND + 200,000 VND = 1,700,000 VND
* Tổng chi phí: 1,700,000 VND/broker x 3 broker = 5,100,000 VND/tháng

**Kết luận:**

Cách tính phí này giúp bạn dễ dàng ước tính chi phí sử dụng vDB Kafka Cluster dựa trên nhu cầu của bạn. Hãy lựa chọn cấu hình và số lượng broker phù hợp để tối ưu hóa chi phí và hiệu suất cho hệ thống của bạn.
