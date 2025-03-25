---
hidden: true
---

# Cách tính phí

Tại VNG Cloud, với sản phẩm vCloudStack mang đến cho khách hàng hai (02) gói mô hình sử dụng dịch vụ, tùy vào nhu cầu sử dụng và định hướng phát triển hệ thống mà khách hàng có thể cân nhắc quyết định nên sử dụng gói mô hình dịch vụ nào:

* Mô hình High Scale
* Mô hình HCI

***

### 1/ Mô hình High Scale <a href="#id-1-mo-hinh-high-scale" id="id-1-mo-hinh-high-scale"></a>

Mô hình cung cấp cố định phần mềm hỗ trợ quản lý vận hành theo cơ sở hạ tầng (vật lý) gồm:

<table><thead><tr><th width="86">STT</th><th width="424">Danh mục</th><th width="141">Đơn vị</th><th>Số lượng</th></tr></thead><tbody><tr><td>1</td><td><p>Cụm máy chủ (Compute cluster) gồm 6 nodes:</p><p>+ Bộ xử lý: 02 x 16 lõi cores</p><p>+ Ram: 512 GB</p><p>+ Ổ đĩa (Disk): 02 x 480 GB SSD/VNME</p><p>+ NIC: 04 x10G SFP + Bộ thu phát</p><p> </p></td><td>Cụm (Cluster)</td><td>1</td></tr><tr><td>2</td><td><p>Cụm lưu trữ (Storage cluster) gồm 4 nodes:</p><p>+ Bộ xử lý: 02 x 16 lõi cores</p><p>+ RAM: 128 GB</p><p>+ Ổ đĩa (Disk): 09 x 1.92 TB SSD/NVEME</p><p>+ NIC: 04 x10G SFP + Bộ thu phát</p></td><td>Cụm (Cluster)</td><td>1</td></tr><tr><td>3</td><td><p>Cụm Backup (Backup Cluster) gồm 1 node:</p><p>+ Bộ xử lý: 02 x 8 lõi cores</p><p>+ RAM: 128 GB</p><p>+ Ổ đĩa (Disk): 10 x 7.6 TB SSD hoặc 10 x 8TB HDD</p><p>+ NIC: 04 x10G SFP + Bộ thu phát</p></td><td>Cụm (Cluster)</td><td>1</td></tr><tr><td>4</td><td>Thiết bị Firewall</td><td>Thiết bị</td><td>2</td></tr><tr><td>5</td><td>Thiết bị định tuyến : 48 x 10 G SFP + bộ thu phát</td><td>Thiết bị</td><td>2</td></tr><tr><td>6</td><td><p>Đường truyền kết nối:</p><p>+ Tuyến chính (Main line): DarkFiber/MPLS</p><p>+ Tuyến phụ (Seconda line): MPLS/VPN</p></td><td>Đường truyền (line)</td><td>2</td></tr><tr><td>7</td><td>Dịch vụ triển khai</td><td>Gói</td><td>1</td></tr></tbody></table>

### 2/ Mô hình HCI <a href="#id-2-mo-hinh-hci" id="id-2-mo-hinh-hci"></a>

Mô hình cung cấp cố định phần mềm hỗ trợ quản lý vận hành theo cơ sở hạ tầng (vật lý) gồm:

<table><thead><tr><th width="85">STT</th><th width="428">Danh mục</th><th width="141">Đơn vị</th><th>Số lượng</th></tr></thead><tbody><tr><td>1</td><td><p>Cụm máy chủ và lưu trữ (Compute và Storage Cluster) gồm 6 nodes:</p><p>+ Bộ xử lý: 02 x 16 lõi cores</p><p>+ Ram: 768 GB</p><p>+ Ổ đĩa OS (Disk): 02 x 480 GB SSD/VNME</p><p>+ Ổ đĩa data (Disk): 08 x 1.92 TB SSD/NVME</p><p>+ NIC: 04 x10G SFP + Bộ thu phát</p><p> </p></td><td>Cụm (Cluster)</td><td>1</td></tr><tr><td>2</td><td><p>Cụm Backup (Backup Cluster) gồm 1 node:</p><p>+ Bộ xử lý: 02 x 8 lõi cores</p><p>+ RAM: 128 GB</p><p>+ Ổ đĩa (Disk): 10 x 7.6 TB SSD hoặc 10 x 8TB HDD</p><p>+ NIC: 04 x10G SFP + Bộ thu phát</p></td><td>Cụm (Cluster)</td><td>1</td></tr><tr><td>3</td><td>Thiết bị Firewall</td><td>Thiết bị</td><td>2</td></tr><tr><td>4</td><td>Thiết bị định tuyến : 48 x 10 G SFP + bộ thu phát</td><td>Thiết bị</td><td>2</td></tr><tr><td>5</td><td><p>Đường truyền kết nối:</p><p>+ Tuyến chính (Main line): DarkFiber/MPLS</p><p>+ Tuyến phụ (Seconda line): MPLS/VPN</p></td><td>Đường truyền (line)</td><td>2</td></tr><tr><td>6</td><td>Dịch vụ triển khai</td><td>Gói</td><td>1</td></tr></tbody></table>
