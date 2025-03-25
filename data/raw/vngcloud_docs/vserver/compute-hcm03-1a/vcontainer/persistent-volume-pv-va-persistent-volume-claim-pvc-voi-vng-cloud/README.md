# Persistent Volume (PV) và Persistent Volume Claim(PVC) với VNG Cloud

**PersistentVolume** (PV) là một phần không gian lưu trữ dữ liệu trong cluster, các PersistentVolume giống với Volume bình thường tuy nhiên nó tồn tại độc lập với POD (pod bị xóa PV vẫn tồn tại), có nhiều loại PersistentVolume có thể triển khai như NFS, Clusterfs...&#x20;

**PersistentVolumeClaim** (PVC) là yêu cầu sử dụng không gian lưu trữ (sử dụng PV). Hình dung PV giống như Node, PVC giống như POD. POD chạy sẽ sử dụng các tài nguyên của NODE, PVC hoạt động nó sử dụng tài nguyên của PV.&#x20;

<figure><img src="https://docs.vngcloud.vn/download/attachments/59801643/image2023-4-26_13-12-34.png?version=1&#x26;modificationDate=1682489555000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

### **Vì sao nên sử dụng Persistent Volume (PV) và Persistent Volume Claim(PVC)** <a href="#persistentvolume-pv-vapersistentvolumeclaim-pvc-voivngcloud-visaonensudungpersistentvolume-pv-vapers" id="persistentvolume-pv-vapersistentvolumeclaim-pvc-voivngcloud-visaonensudungpersistentvolume-pv-vapers"></a>

**Dưới đây là một số lý do quan trọng để sử dụng Persistent Volume (PV) và Persistent Volume Claim (PVC) trong môi trường Kubernetes:**

1. **Tách biệt dữ liệu và ứng dụng**: PV và PVC cho phép tách biệt giữa dữ liệu và ứng dụng. Khi triển khai một ứng dụng, chúng ta muốn dữ liệu lưu trữ được duy trì ngay cả khi các container hoặc Pod bị xóa hoặc triển khai lại. PV và PVC giúp đảm bảo rằng dữ liệu lưu trữ không bị mất khi các container hoặc Pod được tạo hoặc xóa.
2. **Quản lý lưu trữ dễ dàng**: PV và PVC cung cấp một cách thức dễ dàng để quản lý và triển khai lưu trữ trong môi trường Kubernetes. Chúng cho phép bạn xác định loại lưu trữ mong muốn (ví dụ: Ceph, NFS, iSCSI) và các yêu cầu khác như dung lượng, chia sẻ dữ liệu giữa các Pod, chế độ truy cập, v.v. PV và PVC tách biệt khỏi các Pod, giúp quản lý lưu trữ trở nên linh hoạt và dễ dàng.
3. **Đảm bảo tính nhất quán và độ tin cậ**y: PV và PVC cho phép đảm bảo tính nhất quán và độ tin cậy cho dữ liệu lưu trữ. PVC định nghĩa yêu cầu lưu trữ và PV đại diện cho một tài nguyên lưu trữ thực tế. Khi PVC được tạo, Kubernetes sẽ cố gắng tìm và gắn kết PV phù hợp. Điều này đảm bảo rằng mỗi PVC sẽ có một PV duy nhất và giúp đảm bảo tính nhất quán khi triển khai các ứng dụng sử dụng dữ liệu lưu trữ.
4. **Chia sẻ lưu trữ giữa nhiều Pod**: PV và PVC cũng hỗ trợ chia sẻ dữ liệu lưu trữ giữa nhiều Pod. Khi một PVC được gắn kết với một PV, nó có thể được sử dụng bởi nhiều Pod. Điều này cho phép các Pod khác nhau trong cùng một nhóm ứng dụng truy cập và sử dụng cùng một dữ liệu lưu trữ.

Tóm lại, việc sử dụng PV và PVC trong Kubernetes giúp tách biệt dữ liệu và ứng dụng, quản lý lưu trữ dễ dàng, đảm bảo tính nhất quán và độ tin cậy cho dữ liệu, cũng như hỗ trợ chia sẻ lưu trữ giữa nhiều Pod. Điều này giúp tăng tính ổn định và linh hoạt trong quản lý lưu trữ trong môi trường containerized.

***

#### Chủ đề <a href="#persistentvolume-pv-vapersistentvolumeclaim-pvc-voivngcloud-chude" id="persistentvolume-pv-vapersistentvolumeclaim-pvc-voivngcloud-chude"></a>

* [Tạo PersistentVolume(PV) và PersistentVolumeClaim(PVC)](tao-persistentvolume-pv-va-persistentvolumeclaim-pvc.md)
* [Sử dụng PersistentVolumeClaim](su-dung-persistentvolumeclaim.md)
* [Xóa PersistentVolume và PersistentVolumeClaim](xoa-persistentvolume-va-persistentvolumeclaim.md)

\
