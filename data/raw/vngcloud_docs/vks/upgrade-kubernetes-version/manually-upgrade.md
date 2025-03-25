# Manually Upgrade

## Upgrading Control Plane Version

Hiện tại, hệ thống VKS của chúng tôi đã hỗ trợ bạn nâng cấp Control Plane Version, bạn có thể:

* Nâng cấp **Minor Version** mới hơn (ví dụ: 1.24 lên 1.25)
* Nâng cấp **Patch Version** mới hơn (ví dụ: 1.24.2-VKS.100 lên 1.24.5-VKS.200)

**Để thực hiện nâng cấp phiên bản Control Plane, bạn có thể thực hiện theo hướng dẫn sau:**&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn menu **Kubernetes Cluster.**

**Bước 3:** Chọn biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/73762076/image2024-4-16_15-51-55.png?version=1&#x26;modificationDate=1713257518000&#x26;api=v2" alt="" data-size="line">và chọn **Upgrade control plane version** để thực hiện nâng cấp version control plane.

**Bước 4:** Bạn có thể lựa chọn phiên bản mới cho control plane. Phiên bản mới cần hợp lệ và tương thích với phiên bản hiện tại của cluster. Cụ thể: bạn có thể chọn:

* Nâng cấp Minor Version mới hơn (ví dụ: 1.24 lên 1.25)
* Nâng cấp Patch Version mới hơn (ví dụ: 1.24.2-VKS.100 lên 1.24.5-VKS.200)

**Bước 4:** Hệ thống VKS sẽ thực hiện nâng cấp các thành phần Control Plane của Cluster lên phiên bản mới. Sau khi việc nâng cấp hoàn tất, trạng thái (status) Cluster trở về **ACTIVE**.&#x20;

{% hint style="info" %}
**Chú ý:**

* Việc nâng cấp Control Plane Version là không bắt buộc và độc lập với việc nâng cấp Node Group Version. Tuy nhiên Control Plane Version và Node Group Version trong cùng một Cluster không được lệch quá 1 minor version. Bên cạnh đó, hệ thống VKS tự động nâng cấp Control Plane Version khi phiên bản Kubernetes Version hiện tại đang sử dụng cho Cluster của bạn quá thời hạn được nhà cung cấp hỗ trợ.
* Trong quá trình nâng cấp Control Plane Version, bạn không thể thực hiện các hành động khác trên Cluster của bạn.&#x20;
* Bên dưới là một vài lưu ý trước, trong và sau quá trình nâng cấp, vui lòng tham khảo thêm:&#x20;

**Trước khi thực hiện:**

* Sao lưu dữ liệu: Nên sao lưu dữ liệu của cluster trước khi nâng cấp để đảm bảo an toàn trong trường hợp nâng cấp thất bại.
* Kiểm tra phiên bản hiện tại: Truy cập Releases để tham khảo danh sách các phiên bản được hỗ trợ. Chọn phiên bản mới hợp lệ và tương thích với phiên bản hiện tại của cluster.
* Đảm bảo tính sẵn sàng của cluster: Cluster phải đang ở trạng thái (status) hoạt động (ACTIVE) và tất cả các node phải HEALTHY.
* Ngừng các tác vụ đang chạy: Ngừng các tác vụ đang chạy trên cluster để tránh ảnh hưởng đến quá trình nâng cấp.

**Trong khi thực hiện:**

* Theo dõi trạng thái (status) cluster: Theo dõi trạng thái (status) cluster trong quá trình nâng cấp. trạng thái (status) cluster sẽ chuyển sang UPDATING và sau khi hoàn tất sẽ trở về ACTIVE.
* Kiểm tra logs hệ thống: Kiểm tra logs hệ thống để phát hiện bất kỳ lỗi hoặc cảnh báo nào trong quá trình nâng cấp.

**Sau khi thực hiện:**

* Kiểm tra tính sẵn sàng của cluster: Xác nhận rằng cluster đã được nâng cấp thành công và tất cả các node đang hoạt động bình thường.
* Kiểm tra các ứng dụng: Kiểm tra các ứng dụng đang chạy trên cluster để đảm bảo chúng hoạt động bình thường sau khi nâng cấp.

**Lưu ý:**

* Việc nâng cấp Control Plane Version có thể mất một khoảng thời gian tùy thuộc vào kích thước và độ phức tạp của cluster.
* Trong một số trường hợp hiếm gặp, việc nâng cấp Control Plane Version có thể thất bại. Nếu điều này xảy ra, hệ thống VKS sẽ tự động rollback cluster về phiên bản hiện tại.
{% endhint %}

***

## Upgrading Node Group Version

Hiện tại, hệ thống VKS của chúng tôi đã hỗ trợ bạn nâng cấp Node Group Version, bạn có thể nâng cấp Node Group Version lên:

* **Control Plane Version** (Ví dụ nâng cấp từ 1.24 (Node Group version hiện tại) lên 1.25 (Control Plane Version hiện tại), nhưng không thể nâng cấp lên các phiên bản khác.

**Để thực hiện nâng cấp phiên bản Node Group Version, bạn có thể thực hiện theo hướng dẫn sau:**&#x20;

**Bước 1:** Truy cập vào [https://vks.console.vngcloud.vn/overview](https://vks.console-dev.vngcloud.tech/overview)

**Bước 2:** Tại màn hình **Overview**, chọn menu **Kubernetes Cluster.** Chọn vào một **Cluster** mà bạn muốn nâng cấp **Node Group Version**.

**Bước 3:** Chọn biểu tượng <img src="https://docs-admin.vngcloud.vn/download/thumbnails/73762196/image2024-4-16_15-51-55.png?version=1&#x26;modificationDate=1713258271000&#x26;api=v2" alt="" data-size="line">và chọn **Upgrade Node Group Version** để thực hiện nâng cấp version node group.

**Bước 4:** Bạn có thể lựa chọn phiên bản mới cho tất cả các Node Group. Phiên bản mới cần hợp lệ và tương thích với phiên bản hiện tại của cluster. Cụ thể: bạn có thể chọn:

* Nâng cấp Node Group sao cho về cùng version với Control Plane Version (ví dụ: 1.24 lên 1.25)

**Bước 5:** Hệ thống VKS sẽ thực hiện nâng cấp tất cả các Node Group lên version của Control Plane. Sau khi việc nâng cấp hoàn tất, trạng thái (status) Node Group trở về **ACTIVE**.&#x20;

{% hint style="info" %}
**Chú ý:**

* Việc nâng cấp Node Group Version là không bắt buộc và độc lập với việc nâng cấp Control Plane Version. Tuy nhiên tất cả các Node Group trong một Cluster sẽ được nâng cấp trong cùng một lần, cũng như Control Plane Version và Node Group Version trong cùng một Cluster không được lệch quá 1 minor version. Bên cạnh đó, hệ thống VKS tự động nâng cấp Node Group Version khi phiên bản Kubernetes Version hiện tại đang sử dụng cho Cluster của bạn quá thời hạn được nhà cung cấp hỗ trợ.
* Trong quá trình nâng cấp Node Group Version, bạn không thể thực hiện các hành động khác trên Node Group của bạn.&#x20;
* Bên dưới là một vài lưu ý trước, trong và sau quá trình nâng cấp, vui lòng tham khảo thêm:&#x20;

**Trước khi thực hiện:**

* Kiểm tra phiên bản hiện tại: Truy cập Releases để tham khảo danh sách các phiên bản được hỗ trợ. Chọn phiên bản mới hợp lệ và tương thích với phiên bản hiện tại của cluster.
* Đảm bảo tính sẵn sàng của Node Group: Node Group phải đang ở trạng thái (status) hoạt động (ACTIVE) và tất cả các node phải HEALTHY.
* Ngừng các tác vụ đang chạy: Ngừng các tác vụ đang chạy trên cluster để tránh ảnh hưởng đến quá trình nâng cấp.

**Trong khi thực hiện:**

* Theo dõi trạng thái (status) Node Group: Theo dõi trạng thái (status) Node Group trong quá trình nâng cấp. trạng thái (status) Node Group sẽ chuyển sang UPDATING và sau khi hoàn tất sẽ trở về ACTIVE.
* Kiểm tra logs hệ thống: Kiểm tra logs hệ thống để phát hiện bất kỳ lỗi hoặc cảnh báo nào trong quá trình nâng cấp.

**Sau khi thực hiện:**

* Kiểm tra tính sẵn sàng của Node Group: Xác nhận rằng Node Group đã được nâng cấp thành công và tất cả các node đang hoạt động bình thường.
* Kiểm tra các ứng dụng: Kiểm tra các ứng dụng đang chạy trên cluster để đảm bảo chúng hoạt động bình thường sau khi nâng cấp.

**Lưu ý:**

* Việc nâng cấp Node Group Version có thể mất một khoảng thời gian tùy thuộc vào kích thước và độ phức tạp của Node Group.
* Trong một số trường hợp hiếm gặp, việc nâng cấp Node Group Version có thể thất bại. Nếu điều này xảy ra, hệ thống VKS sẽ tự động rollback cluster về phiên bản hiện tại.
{% endhint %}
