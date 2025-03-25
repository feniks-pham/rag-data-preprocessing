# Upgrading Control Plane Version

Hiện tại, hệ thống VKS của chúng tôi đã hỗ trợ bạn nâng cấp Control Plane Version, bạn có thể:

* Nâng cấp **Minor Version** mới hơn (ví dụ: 1.24 lên 1.25)
* Nâng cấp **Patch Version** mới hơn (ví dụ: 1.24.2-VKS.100 lên 1.24.5-VKS.200)

**Để thực hiện nâng cấp phiên bản Control Plane, bạn có thể thực hiện theo hướng dẫn sau:**&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn menu **Kubernetes Cluster.**

**Bước 3:** Chọn biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/73762015/image2024-4-16_15-51-55.png?version=1&#x26;modificationDate=1713262579000&#x26;api=v2" alt="" data-size="line">và chọn **Upgrade control plane version** để thực hiện nâng cấp version control plane.

**Bước 4:** Bạn có thể lựa chọn phiên bản mới cho control plane. Phiên bản mới cần hợp lệ và tương thích với phiên bản hiện tại của cluster. Cụ thể: bạn có thể chọn:

* Nâng cấp **Minor Version** mới hơn (ví dụ: 1.24 lên 1.25)
* Nâng cấp **Patch Version** mới hơn (ví dụ: 1.24.2-VKS.100 lên 1.24.5-VKS.200)

**Bước 4:** Hệ thống VKS sẽ thực hiện nâng cấp các thành phần **Control Plane** của **Cluster** lên phiên bản mới. Sau khi việc nâng cấp hoàn tất, trạng thái Cluster trở về **ACTIVE**.&#x20;

{% hint style="info" %}
**Chú ý:**

* Việc nâng cấp Control Plane Version là không bắt buộc và độc lập với việc nâng cấp Node Group Version. Tuy nhiên Control Plane Version và Node Group Version trong cùng một Cluster không được lệch quá 1 minor version. Bên cạnh đó, hệ thống VKS tự động nâng cấp Control Plane Version khi phiên bản K8S Version hiện tại đang sử dụng cho Cluster của bạn quá thời hạn được nhà cung cấp hỗ trợ.
* Trong quá trình nâng cấp Control Plane Version, bạn không thể thực hiện các hành động khác trên Cluster của bạn.&#x20;
* Bên dưới là một vài lưu ý trước, trong và sau quá trình nâng cấp, vui lòng tham khảo thêm:&#x20;

**Trước khi thực hiện:**

* Sao lưu dữ liệu: Nên sao lưu dữ liệu của cluster trước khi nâng cấp để đảm bảo an toàn trong trường hợp nâng cấp thất bại.
* Kiểm tra phiên bản hiện tại: Truy cập Releases để tham khảo danh sách các phiên bản được hỗ trợ. Chọn phiên bản mới hợp lệ và tương thích với phiên bản hiện tại của cluster.
* Đảm bảo tính sẵn sàng của cluster: Cluster phải đang ở trạng thái hoạt động (ACTIVE) và tất cả các node phải HEALTHY.
* Ngừng các tác vụ đang chạy: Ngừng các tác vụ đang chạy trên cluster để tránh ảnh hưởng đến quá trình nâng cấp.

**Trong khi thực hiện:**

* Theo dõi trạng thái cluster: Theo dõi trạng thái cluster trong quá trình nâng cấp. Trạng thái cluster sẽ chuyển sang UPDATING và sau khi hoàn tất sẽ trở về ACTIVE.
* Kiểm tra nhật ký hệ thống: Kiểm tra nhật ký hệ thống để phát hiện bất kỳ lỗi hoặc cảnh báo nào trong quá trình nâng cấp.

**Sau khi thực hiện:**

* Kiểm tra tính sẵn sàng của cluster: Xác nhận rằng cluster đã được nâng cấp thành công và tất cả các node đang hoạt động bình thường.
* Kiểm tra các ứng dụng: Kiểm tra các ứng dụng đang chạy trên cluster để đảm bảo chúng hoạt động bình thường sau khi nâng cấp.

**Lưu ý:**

* Việc nâng cấp Control Plane Version có thể mất một khoảng thời gian tùy thuộc vào kích thước và độ phức tạp của cluster.
* Trong một số trường hợp hiếm gặp, việc nâng cấp Control Plane Version có thể thất bại. Nếu điều này xảy ra, hệ thống VKS sẽ tự động rollback cluster về phiên bản hiện tại.
{% endhint %}
