# Bắt đầu với Kafka Cluster

Với vDB Kafka Cluster, bạn có thể nhanh chóng triển khai và quản lý cụm Kafka một cách hiệu quả, tập trung vào phát triển ứng dụng và khai thác sức mạnh của xử lý luồng sự kiện theo thời gian thực. Làm theo hướng dẫn dưới đây để bắt đầu sử dụng dịch vụ Kafka Cluster.

## Bước 1: Truy cập và Đăng nhập

1. Mở trình duyệt web và truy cập vào giao diện vDB Kafka Cluster theo đường dẫn tại đây: [https://vdb.console.vngcloud.vn/kafka/cluster](https://vdb.console.vngcloud.vn/kafka/cluster)
2. Nếu bạn đã có tài khoản, hãy nhập thông tin đăng nhập của bạn.

Tham khảo hướng dẫn đăng nhập vào VNG Cloud [tại đây](../../identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md).

## Bước 2: Tạo Cụm Kafka

1.  Nhấp vào nút "Tạo Cụm Kafka".&#x20;

    <figure><img src="../../.gitbook/assets/image%20(744).png" alt="" width="228"><figcaption></figcaption></figure>
2. Điền thông tin sau:
   * **Tên:** Đặt tên cho cụm Kafka của bạn để dễ nhận biết và quản lý.
   * **Kafka Version:** Chọn phiên bản Kafka phù hợp với nhu cầu của bạn. Các phiên bản khác nhau có thể có tính năng và hiệu suất khác nhau.
   * **Flavor (CPU, RAM):** Chọn cấu hình phần cứng (CPU và RAM) cho các broker trong cụm Kafka. Cấu hình này ảnh hưởng đến khả năng xử lý và hiệu suất của cụm.
   * **Số lượng Broker:** Xác định số lượng broker trong cụm Kafka. Số lượng broker ảnh hưởng đến khả năng chịu lỗi và khả năng mở rộng của cụm.
   * **Storage từng Broker (IOPS và Dung lượng):** Chọn dung lượng lưu trữ và IOPS (Số lượng hoạt động nhập/xuất mỗi giây) cho mỗi broker. Điều này ảnh hưởng đến khả năng lưu trữ dữ liệu và hiệu suất đọc/ghi của cụm.
   * **Network (VPC, Subnet):** Chọn mạng ảo (VPC) và subnet mà cụm Kafka sẽ được triển khai. Khi khởi tạo, cụm Kafka sẽ ở chế độ private (chỉ truy cập được từ trong VPC). Sau khi khởi tạo thành công, bạn có thể mở truy cập public nếu cần.
   * **Access Method Control (mTLS, SASL):** Chọn phương thức xác thực và ủy quyền cho client kết nối đến cụm Kafka. mTLS sử dụng chứng chỉ client và server, SASL sử dụng tên người dùng và mật khẩu.
   * **Encryption Mode:** Chọn chế độ mã hóa dữ liệu. Mặc định, mã hóa in transit (dữ liệu được mã hóa khi truyền giữa client và broker) và within cluster (dữ liệu được mã hóa khi lưu trữ trên các broker) được bật.
   * **Config Group:** Chọn nhóm cấu hình áp dụng cho cụm Kafka. Nhóm cấu hình chứa các thiết lập chi tiết về hoạt động của Kafka.
3.  Nhấp vào nút "Tạo" để bắt đầu quá trình tạo cụm Kafka.&#x20;

    <figure><img src="../../.gitbook/assets/image%20(745).png" alt=""><figcaption></figcaption></figure>

## Bước 3: Tạo Topic

1. Sau khi cụm Kafka được tạo thành công, truy cập vào trang quản lý cụm Kafka đó.
2. Tìm và nhấp vào phần "Tạo Topic".

<figure><img src="../../.gitbook/assets/image%20(748).png" alt=""><figcaption></figcaption></figure>

3. Điền thông tin sau:

* **Tên:** Đặt tên cho topic. Lưu ý rằng tên này sẽ không thể thay đổi sau khi khởi tạo.
* **Partition Count:** Xác định số lượng phân vùng cho topic. Số lượng phân vùng ảnh hưởng đến khả năng mở rộng và song song của topic.
* **Replication Factor:** Xác định số lượng bản sao của mỗi phân vùng. Điều này ảnh hưởng đến khả năng chịu lỗi của topic.
* **Retention Hour/Byte:** Xác định thời gian hoặc dung lượng lưu trữ tối đa cho dữ liệu trong topic.

4. Nhấp vào nút "Tạo" để tạo topic.

## Bước 4: Tạo Kafka User và Phân Quyền

1. Trong trang quản lý cụm Kafka, tìm và nhấp vào phần "Tạo Kafka User".

<figure><img src="../../.gitbook/assets/image%20(749).png" alt=""><figcaption></figcaption></figure>

2. Điền thông tin sau:

* **Tên:** Đặt tên cho Kafka user.
* **Phân quyền:** Tại phần permission, nhấn "Add Permission" để chọn các quyền Produce (ghi dữ liệu vào topic) và Consume (đọc dữ liệu từ topic) cho từng topic mà user này cần truy cập.

<figure><img src="../../.gitbook/assets/image%20(750).png" alt=""><figcaption></figcaption></figure>

* **Phương thức Truy cập:** Chọn phương thức truy cập cho Kafka user (mTLS hoặc SASL) tùy thuộc vào phương thức được bật cho cụm Kafka.

3. Nhấp vào nút "Tạo" để tạo Kafka user.

## Bước 5: Kết nối tới cụm Kafka

Có nhiều cách kết nối tới cụm Kafka, hướng dẫn sau sẽ giới thiệu bạn cách kết nối đến cụm kafka thông qua private client.

Lưu ý: Hướng dẫn cài đặt dưới đây được thực hiện trên server client unbuntu 22.04.

1. Khởi tạo Server. Xem hướng dẫn chi tiết khởi tạo server [tại đây](../../vserver/compute-hcm03-1a/server/tao-may-chu-bang-bang-dieu-khien.md).
2. Kết nối đến server vừa khởi tạo. Xem hướng dẫn chi tiết [tại đây.](../../vserver/compute-hcm03-1a/server/ket-noi-vao-may-chu-ao/)
3. Cài đặt Java và các package cần thiết trên server với lệnh sau:

```bash
sudo apt-get update && sudo apt-get install default-jre tar unzip -y
```

4. Tiếp theo, tải Apache Kafka với lệnh sau:

```bash
wget https://archive.apache.org/dist/kafka/{Your Kafka Cluster Version}/kafka_2.13-{Your Kafka Cluster Version}.tgz
tar -xzf kafka_2.13-{YOUR MSK VERSION}.tgz
```

Example

```bash
wget https://archive.apache.org/dist/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xzf kafka_2.13-3.7.0.tgz
```

5.  Tiếp theo, tải về các chứng chỉ TLS để truy cập đến cụm Kafka.&#x20;

    <figure><img src="../../.gitbook/assets/image%20(746).png" alt=""><figcaption></figcaption></figure>
6. Tại server vừa khởi tạo, tải lên và giải nén các chứng chỉ TLS và unzip theo lệnh bên dưới:

Lưu ý: User ID sẽ là tên thư mục sau khi giải nén chứng chỉ vừa tải về

```bash
unzip vng-manage-key.zip 
cd {User ID}/mtls
```

Example

```bash
unzip vng-manage-key.zip
cd user-4436a54a-feaa-4afd-bfe7-4bd3d2cae33a/mtls/
```

7. Cho phép truy cập đến cụm Kafka

Bạn cần cho phép server này truy cập đến cụm kafka như là một private client, bằng cách allow IP, làm theo hướng dẫn dưới đây:

* 7.1 Xem thông tin Private IP của server vừa khởi tạo, ví dụ server có private IP là 10.255.0.5
* 7.2 Cho phép IP này truy cập đến cụm Kafka:
  * 7.2.1 Truy cập vào giao diện quản lý cụm Kafka
  * 7.2.2 Tìm đến mục **Conectivity & Security**, thêm rule như hình bên dưới

Lưu ý: Port 9094 với mTLS và 9096 với SASL

<figure><img src="../../.gitbook/assets/image%20(751).png" alt=""><figcaption></figcaption></figure>

8. Produce message đến Kafka topic

Sau khi cho phép truy cập từ máy khách đến cụm Kafka, kết nối tới máy khách đã khởi tạo trước đó, và thực hiện lệnh sau:

```bash
{Path To Your Kafka Installation}/bin/kafka-console-producer.sh --bootstrap-server {Your Kafka Cluster Private endpoint}  --producer.config config.properties  --topic {Your Kafka Topic}
```

Example

```bash
/home/stackops/kafka_2.13-3.7.0/bin/kafka-console-producer.sh --bootstrap-server 10.5.0.6:9094,10.5.0.3:9094,10.5.0.5:9094 --producer.config config.properties --topic kafka-cluster-tutorial
```

9. Consume message từ Kafka topic

Sau khi cho phép truy cập từ máy khách đến cụm Kafka, kết nối tới máy khách đã khởi tạo trước đó, và thực hiện lệnh sau:

```bash
{Path To Your Kafka Installation}/bin/kafka-console-consumer.sh --bootstrap-server {Your Kafka Cluster Private endpoint} --consumer.config config.properties  --topic {Your Kafka Topic}  --from-beginning
```

Example

```bash
/home/stackops/kafka_2.13-3.7.0/bin/kafka-console-consumer.sh --bootstrap-server 10.5.0.6:9094,10.5.0.3:9094,10.5.0.5:9094 --consumer.config  config.properties   --topic kafka-cluster-tutorial    --from-beginning
```

## Bước 6: Xóa Cụm Kafka

1. Khi bạn không còn nhu cầu sử dụng cụm Kafka, hãy truy cập vào trang quản lý cụm Kafka.
2. Tìm và nhấp vào nút "Xóa Cụm Kafka".
3. Xác nhận việc xóa cụm Kafka để tránh mất dữ liệu và chi phí không cần thiết.

