# Cách tính giá

Đối với VKS chi phí **Managed Control Plane là hoàn toàn miễn phí.** Bạn chỉ cần chi trả cho các resource khác mà thực tế bạn sử dụng bao gồm:

* Đối với **Public Cluster**, bạn cần chi trả cho:&#x20;
  * Tất cả các node có trong Cluster (VM). Chi tiết cách tính giá của vServer bạn có thể tham khảo thêm tại [đây](../vserver/compute-hcm03-1a/cach-tinh-gia-vserver.md).
  * Load Balancer được integrated vào Cluster của bạn. Chi tiết cách tính giá của Load Balancer bạn có thể tham khảo thêm tại [đây](../vserver/compute-hcm03-1a/cach-tinh-gia-vserver.md).
  * Persistent Volume, Snapshot được integrated vào Cluster của bạn. Chi tiết cách tính giá của Volume bạn có thể tham khảo tại [đây](../vserver/compute-hcm03-1a/cach-tinh-gia-vserver.md).
* Đối với **Private Cluster**, bạn cần chi trả cho:&#x20;
  * Tất cả các node có trong Cluster (VM). Chi tiết cách tính giá của vServer bạn có thể tham khảo thêm tại [đây](../vserver/compute-hcm03-1a/cach-tinh-gia-vserver.md).
  * Load Balancer được integrated vào Cluster của bạn. Chi tiết cách tính giá của Load Balancer bạn có thể tham khảo thêm tại [đây](../vserver/compute-hcm03-1a/cach-tinh-gia-vserver.md).
  * Persistent Volume, Snapshot được integrated vào Cluster của bạn. Chi tiết cách tính giá của Volume bạn có thể tham khảo tại [đây](../vserver/compute-hcm03-1a/cach-tinh-gia-vserver.md).
  *   Ngoài ra, khi bạn tạo một private cluster, hệ thống tự động tạo 4 endpoints giúp kết nối với các dịch vụ khác trên VNG Cloud bao gồm:

      * **Endpoint** để kết nối tới dịch vụ **IAM** (Endpoint Name: vks-iam-endpoint-...)
      * **Endpoint** để kết nối tới dịch vụ **vCR** (Endpoint Name: vks-vcr-endpoint-...)
      * **Endpoint** để kết nối tới dịch vụ **vServer** (Endpoint Name: vks-vserver-endpoint-...)
      * **Endpoint** để kết nối tới dịch vụ **vStorage** (Endpoint Name: vks-vstorage-endpoint-...)

      Việc sử dụng private cluster sẽ phát sinh thêm chi phí cho 4 private service endpoint này, nhưng nó mang lại nhiều lợi ích về bảo mật cho dự án của bạn. Bạn hãy cân nhắc kỹ lưỡng các yếu tố để đưa ra quyết định sử dụng public hay private cho cluster của mình.

{% hint style="info" %}
**Chú ý:**

* Để đảm bảo Cluster của bạn hoạt động ổn định, chúng tôi đã tự động thiết lập Auto-renew cho tất cả các resource trên Cluster của bạn. Trước ngày hết hạn của các resource, hãy đảm bảo số dư credit của bạn đủ để hệ thống có thể thực hiện Auto-renew thành công.
{% endhint %}
