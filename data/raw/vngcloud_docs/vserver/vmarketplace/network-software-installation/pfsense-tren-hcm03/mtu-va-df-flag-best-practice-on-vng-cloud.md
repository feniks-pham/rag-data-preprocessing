# MTU và “DF flag” best practice on VNG Cloud

Default MTU trên môi trường Internet là 1500 bytes, tuy nhiên công nghệ ảo hóa yêu cầu đóng gói thêm một số Extended Headers, điều này làm cho giá trị thực tế sẽ < 1500 bytes.

Hiện tại hạ tầng VNG Cloud đang hỗ trợ tốt ở giá trị Interface MTU 1450 bytes, do đó sau quá trình đóng gói các protocol/application headers, gói tin được gửi ra khỏi VM được khuyến cáo nên ≤ 1450 bytes (1).

Việc VM gửi ra các gói có MTU lớn hơn giá trị MTU đang hỗ trợ dẫn đến hiện tượng “packet fragmentation”, gói tin gốc sẽ được chia thành nhiều gói nhỏ hơn truyền đi và ghép lại khi đến đích, đây là một quá trình hoàn toàn bình thường xảy ra khi dữ liệu được truyền trên môi trường Internet. “Packet fragmentation” sẽ đáp ứng phần lớn nhu cầu của khách hàng.

Tuy nhiên, đối với một số dịch vụ đặc thù như Voice SIP(UDP), VPN Tunnel (IPSec/GRE), có 2 vấn đề thường xuyên dẫn đến issues:

1. Các gói tin được truyền đi với cờ "Do Not Fragment" (DF flag) (2).
2. Custom SIP Headers hoặc IPSec/GRE Headers được thêm vào gói tin gốc, làm cho kích thước gói tin lớn hơn 1450 Bytes.

Khi cả hai điều kiện trên xảy ra đồng thời, hạ tầng có thể bỏ qua gói tin ra khỏi máy ảo.

Vì thế VNG Cloud khuyến khích khách hàng chủ động giảm giá trị MTU khi khởi tạo, nếu có sử dụng các “dịch vụ nhạy cảm về MTU và yêu cầu “DF flag”” theo một trong các cách như sau để hạn chế rủi ro khi sử dụng dịch vụ:

1. Thay đổi cấu hình Application/Service để loại bỏ các Headers không cần thiết (ví dụ custom SIP Headers, IPSec Authentication and Encryption Algorithm).
2.  Thay đổi MTU của VM (đối với các VM sử dụng custom flavor của KH không theo chuẩn chung VNG Cloud) về 1450 (hoặc nhỏ hơn nếu cần).

    **PFSense: WEB UI - Interfaces - WAN - MTU = 1450**

    <figure><img src="https://docs.vngcloud.vn/download/attachments/64554291/image2023-10-11_10-15-3.png?version=1&#x26;modificationDate=1696994104000&#x26;api=v2" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (686).png" alt=""><figcaption></figcaption></figure>

    **FortiGate CLI:**

    ```
    FTG_GW #

    config system interface

        edit <interface-name>

            set mtu-override enable

            set mtu <1450>

        next

    end
    ```

    \
    ![](<../../../../.gitbook/assets/image (687).png>)\


    **Ubuntu/Linux**

```
$ ifconfig <interface_name> mtu <mtu_size> up

Hoặc thêm vào file cấu hình interfaces

post-up /sbin/ifconfig <interface-name> mtu <mtu_size>
```

3. Liên hệ đội ngũ support qua Portal\
   **Lưu ý:**\
   (1) đối với các IPSec Tunnel yêu cầu xác thực và mã hóa cao, giá trị Headers có thể lên đến hơn 100 bytes, do đó tùy theo nhu cầu sử dụng, khách hàng nên lựa chọn giá trị MTU phù hợp 1200 – 1300 – 1450 bytes. Bảng dưới mô tả ví dụ IPSec Headers Size được thêm vào làm ảnh hưởng đến giá trị MTU thực tế đối với gói tin có Payload ban đầu 1340 bytes.

| **Payload**                                 | **Size** |
| ------------------------------------------- | -------- |
| New IPv4 Header for IPsec                   | 20       |
| AH Header                                   | 12       |
| Next Header - 1                             |          |
| Payload - 1                                 |          |
| Reserved - 2                                |          |
| SPI - 4                                     |          |
| Sequence - 4                                |          |
| AH Digest                                   | 12       |
| ESP Header                                  | 8        |
| SPI - 4                                     |          |
| Sequence - 4                                |          |
| ESP IV                                      | 16       |
| **Original IPv4 Header**                    | **20**   |
| **Original IPv4 Payload**                   | **1320** |
| ESP Trailer                                 | 36       |
| ESP Pad - 2                                 |          |
| Pad Length - 1                              |          |
| Next Header - 1                             |          |
| ESP ICV - 32                                |          |
| Total IPsec Packet Size sending out from VM | 1444     |

&#x20; **Bảng 1: Không enable NAT-T và không enable GRE**

| **Payload**                                 | **Size** |
| ------------------------------------------- | -------- |
| New IPv4 Header for IPsec                   | 20       |
| UDP Header (NAT-T)                          | 8        |
| AH Header                                   | 12       |
| Next Header - 1                             |          |
| Payload - 1                                 |          |
| Reserved - 2                                |          |
| SPI - 4                                     |          |
| Sequence - 4                                |          |
| AH Digest                                   | 12       |
| ESP Header                                  | 8        |
| SPI - 4                                     |          |
| Sequence - 4                                |          |
| ESP IV                                      | 16       |
| **Original IPv4 Header**                    | **20**   |
| **Original IPv4 Payload**                   | **1320** |
| ESP Trailer                                 | 36       |
| ESP Pad - 2                                 |          |
| Pad Length - 1                              |          |
| Next Header - 1                             |          |
| ESP ICV - 32                                |          |
| Total IPsec Packet Size sending out from VM | **1452** |

&#x20;     **Bảng 2: Enable NAT-T và không enable GRE**

| **Payload**                                 | **Size** |
| ------------------------------------------- | -------- |
| New IPv4 Header for IPsec                   | 20       |
| UDP Header (NAT-T)                          | 8        |
| AH Header                                   | 12       |
| Next Header - 1                             |          |
| Payload - 1                                 |          |
| Reserved - 2                                |          |
| SPI - 4                                     |          |
| Sequence - 4                                |          |
| AH Digest                                   | 12       |
| ESP Header                                  | 8        |
| SPI - 4                                     |          |
| Sequence - 4                                |          |
| ESP IV                                      | 16       |
| New IPv4 Header for GRE                     | 20       |
| GRE Header + Tunnel Key                     | 8        |
| **Original IPv4 Header**                    | **20**   |
| **Original IPv4 Payload**                   | **1320** |
| ESP Trailer                                 | 40       |
| ESP Pad - 6                                 |          |
| Pad Length - 1                              |          |
| Next Header - 1                             |          |
| ESP ICV - 32                                |          |
| Total IPsec Packet Size sending out from VM | **1484** |

&#x20;                   **Bảng 3: Enable NAT-T và GRE**
