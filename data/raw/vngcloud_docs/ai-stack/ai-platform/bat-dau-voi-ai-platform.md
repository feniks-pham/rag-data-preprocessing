# Bắt đầu với AI Platform

### Trước khi bắt đầu <a href="#gettingstarted-vcr-truockhibatdau" id="gettingstarted-vcr-truockhibatdau"></a>

Để bắt đầu sử dụng AI Platform, bạn cần tìm hiểu trước các hướng dẫn sau:

* Nếu chưa có tài khoản VNG Cloud, người dùng cần đăng ký tài khoản để có thể sử dụng dịch vụ. Tham khảo hướng dẫn [Đăng ký tài khoản](../../huong-dan-su-dung-tai-khoan/dang-ky-tai-khoan.md)
* Tìm hiểu cách **truy cập VNG Cloud Portal** với Root User Account hoặc IAM User Account, tham khảo hướng dẫn [Cách đăng nhập vào VNG Cloud](../../identity-and-access-management-iam/cac-loai-dinh-danh-iam/tai-khoan-user-accounts/cach-dang-nhap-vao-vng-cloud.md).

### 1. Truy cập AI Platform

* Truy cập AI Platform theo đường dẫn tại đây: [https://aiplatform.console.vngcloud.vn/](https://aiplatform.console.vngcloud.vn/)
* Nhập **tài khoản và mật khẩu** của bạn tại bước đăng nhập.

### **2. Khởi tạo Network Volume**

Network Volume là nơi **lưu trữ dữ liệu, mô hình AI, và kết quả huấn luyện** để sử dụng trên AI Platform.

#### **Tạo Network Volume**

1.  Trong giao diện **AI Platform**, tại mục Storage management, chọn **Network Volume**.&#x20;

    <figure><img src="../../.gitbook/assets/image (947).png" alt="" width="166"><figcaption></figcaption></figure>
2. Nhấn **Create a network volume**.
3. Điền thông tin cần thiết:
   * **Tên Volume**: Ví dụ `ai-storage`
   * **Region**: HCM.
4. Nhấn **Create volume** để hoàn tất.

Lưu ý: Dung lượng volume sẽ dựa vào usage sử dụng thực tế, người dùng không cần chỉ định dung lượng khi khởi tạo.

#### **Tải lên Model lưu trữ tại Network Volume bằng S3**



### **3. Khởi Tạo Model Registry với Model từ Network Volume**

Model Registry giúp bạn **quản lý phiên bản mô hình**, lưu trữ metadata và đảm bảo tính nhất quán khi triển khai.

#### **Import Model vào Model Registry**

1. Truy cập **AI Platform > Model Registry** tại đây: [https://aiplatform.console.vngcloud.vn/registry](https://aiplatform.console.vngcloud.vn/registry)
2. Nhấn **Import a model registry**.
3. Điền thông tin:
   * **Region:** `e.g. HCM`
     * Xác định **vị trí trung tâm dữ liệu** nơi model được lưu trữ và triển khai inference.
     * Lựa chọn đúng region giúp tối ưu tốc độ truy cập và độ trễ thấp hơn.
     * Hiện tại, AI Platform tại VNG Cloud hỗ trợ triển khai tại **HCM (TP. Hồ Chí Minh)**.
   * **Tên Model**: e.g.`face-recognition-v1`
     * Đặt tên cho mô hình AI để dễ dàng quản lý.
     * Có thể bao gồm **số phiên bản (v1, v2, v3, …)** để theo dõi quá trình cải tiến model.
     * Tên này sẽ được sử dụng khi triển khai **Inference Service**.
   * **Container**: Pre-built container/Custom container
     * **Pre-built container**:
       * Hệ thống đã cài sẵn **runtime, thư viện AI** (PyTorch, TensorFlow, ONNX…).
       * Hỗ trợ **Inference Engine** như Triton, vLLM để chạy model. Phù hợp nếu model được huấn luyện bằng framework phổ biến.
     * **Custom image**: Bạn có thể sử dụng **container riêng** để chạy mô hình AI. Cần đảm bảo ảnh container có đầy đủ thư viện, mã nguồn cần thiết.
   * **Model framework:** Triton 24.12/Triton 24.12-vLLM
     * **Triton 24.12** – NVIDIA Triton Inference Server (Phiên bản chuẩn).
     * **Triton 24.12-vLLM** – NVIDIA Triton với hỗ trợ **vLLM** (tối ưu cho LLM - Large Language Model).
   * **Data mount:** Chỉ định nơi chứa dữ liệu và model để **Inference Service** có thể truy cập.
     * Hiện chỉ hỗ trợ **Network Volume**&#x20;
   * **Network volume:** e.g.`ai-storage`
     * Chỉ định Network Volume **chứa model AI** để hệ thống có thể truy cập khi chạy inference.
     * Model phải được lưu trong thư mục `/models/your-model-folder/`.
4. Nhấn **Import** để lưu mô hình.

### **4. Khởi Tạo Inference với Model Registry Vừa Import**

Inference giúp bạn **triển khai mô hình AI** dưới dạng **API RESTful**, có thể được gọi từ ứng dụng web, mobile hoặc hệ thống backend.

1. Endpoint Name

* **Tên endpoint** là định danh cho inference service.
* Đây là phần cuối trong URL API mà bạn sẽ gọi từ ứng dụng.
* **Giới hạn độ dài:** **Tối thiểu 1 ký tự, tối đa 50 ký tự**.

2\. Region (Khu Vực)

* Chọn **khu vực** để triển khai inference service.
* Hiện tại, VNG Cloud hỗ trợ **HCM (TP. Hồ Chí Minh)**.

3\. Model

* Chọn **mô hình AI** từ **Model Registry** để triển khai inference.
* Chỉ các model đã được import vào **Model Registry** mới xuất hiện trong danh sách này.

4\. Resource Configuration (Cấu Hình Tài Nguyên)

* Cấu hình tài nguyên phần cứng (CPU, RAM, GPU) để chạy inference service.
* Cấu hình này ảnh hưởng đến **hiệu suất và chi phí**.
* Chọn **GPU nếu model cần tăng tốc xử lý**, đặc biệt với Computer Vision & LLM.
* Nếu model **nhẹ (XGBoost, Scikit-Learn, ONNX)**, có thể chọn instance **chỉ CPU** để tiết kiệm chi phí.

5\. Replica Configuration (Cấu Hình Replica - Tự Động Mở Rộng)

* Xác định **số lượng bản sao (replica)** của inference service.
* Hệ thống có thể **tự động scale up/down** theo nhu cầu.
* **Minimum Replica Count**
  * **Số lượng instance tối thiểu** chạy inference.
  * Nếu giá trị là `1`, inference service **luôn có ít nhất 1 instance** hoạt động.
* **Maximum Replica Count**
  * **Số lượng instance tối đa** mà hệ thống có thể mở rộng.
  * Nếu traffic tăng cao, hệ thống sẽ scale lên tối đa `10` instance.
* **Auto-Scaling Settings (Cấu Hình Tự Động Mở Rộng)**
  * Cấu hình **khi nào hệ thống cần scale up/down** dựa trên tài nguyên sử dụng.
  * Một số **chỉ số quan trọng** có thể dùng để auto-scale:
    * **CPU & RAM Usage (%)**: Nếu CPU & RAM vượt \[n]`%`, hệ thống scale lên.
    * **GPU Utilization (%)**: Nếu GPU vượt \[n]`%`, scale thêm instance.
    * **Response latency (milisecond)**: Nếu số latency vượt \[n]milisecond, scale lên.

