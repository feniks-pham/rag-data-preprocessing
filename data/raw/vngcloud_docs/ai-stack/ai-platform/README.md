# AI Platform

### **1. AI Platform Là Gì?**

**AI Platform tại VNG Cloud** là một nền tảng điện toán đám mây được thiết kế để hỗ trợ **phát triển, huấn luyện, tối ưu hóa và triển khai mô hình AI** một cách linh hoạt và hiệu quả.

Với **AI Platform**, AI Engineer có thể **xây dựng và quản lý toàn bộ vòng đời của mô hình AI** – từ giai đoạn nghiên cứu, huấn luyện, tinh chỉnh, cho đến triển khai thực tế. AI Platform cung cấp tài nguyên tính toán mạnh mẽ, giúp tối ưu quá trình phát triển AI mà không cần đầu tư hạ tầng phần cứng đắt đỏ.

**AI Platform Giúp Ích Gì?**

* **Tiết kiệm chi phí**: Không cần đầu tư hạ tầng máy chủ mạnh, chỉ trả phí theo mức sử dụng.
* **Tăng tốc phát triển AI**: Cung cấp môi trường làm việc với GPU, khả năng mở rộng linh hoạt.
* **Quản lý hiệu quả mô hình AI**: Hỗ trợ lưu trữ, theo dõi và triển khai mô hình một cách nhất quán.
* **Dễ dàng triển khai AI**: Cho phép triển khai mô hình AI thành API phục vụ ứng dụng thực tế.
* **Bảo mật & tối ưu tài nguyên**: Hỗ trợ kiểm soát truy cập, phân bổ tài nguyên hợp lý theo từng dự án.

***

### **2. Các Tính Năng Chính Của AI Platform**

#### **1. Notebook – Môi trường lập trình AI tương tác**

Notebook là một công cụ quan trọng giúp AI Engineer viết mã, thử nghiệm và huấn luyện mô hình trực tiếp trên cloud.

* **Hỗ trợ Jupyter Notebook:** Môi trường lập trình phổ biến trong cộng đồng AI/ML.
* **Tích hợp GPU:** Cung cấp tài nguyên tính toán mạnh mẽ để huấn luyện mô hình nhanh chóng.
* **Quản lý phiên bản code:** Lưu trữ, theo dõi lịch sử chỉnh sửa và dễ dàng chia sẻ notebook.
* **Ứng dụng**: Viết code AI, thử nghiệm mô hình, tiền xử lý dữ liệu, chạy thử inference.

***

#### **2. Network Volume – Lưu trữ & chia sẻ dữ liệu AI**

Network Volume là **hệ thống lưu trữ phân tán**, giúp AI Engineer có thể **chia sẻ dữ liệu, mô hình và kết quả huấn luyện** giữa các notebook, server mà không cần truyền tải thủ công.

* **Dung lượng mở rộng linh hoạt** – Phù hợp với nhu cầu xử lý dữ liệu lớn.
* **Truy cập nhanh chóng** – Hỗ trợ đọc/ghi dữ liệu tốc độ cao giữa nhiều phiên làm việc.
* **Tích hợp bảo mật** – Kiểm soát quyền truy cập theo từng người dùng hoặc nhóm dự án.
* **Ứng dụng**: Lưu trữ dataset, mô hình AI, kết quả huấn luyện, log file.

***

#### **3. Model Tuning – Tối ưu hóa mô hình AI**

Model Tuning giúp AI Engineer **tinh chỉnh tham số mô hình (hyperparameter tuning)** để đạt hiệu suất cao nhất.

* **Tự động hóa quá trình thử nghiệm tham số** – Chạy nhiều phiên bản huấn luyện song song.
* **Hỗ trợ thuật toán tối ưu**
* **Ghi nhận kết quả & đề xuất mô hình tối ưu** – Giúp chọn mô hình có độ chính xác cao nhất.
* **Ứng dụng**: Tối ưu mô hình AI trong các bài toán nhận diện ảnh, xử lý ngôn ngữ tự nhiên (NLP), dự đoán dữ liệu.

***

#### **4. Inference – Triển khai & chạy mô hình AI**

Inference giúp doanh nghiệp triển khai mô hình AI và **chuyển mô hình thành API** phục vụ ứng dụng thực tế.

* **Triển khai mô hình AI dưới dạng API RESTful** – Dễ dàng tích hợp vào ứng dụng web, mobile, chatbot.
* **Tối ưu tốc độ suy luận (low-latency inference)** – Giúp AI chạy nhanh với thời gian phản hồi thấp.
* **Quản lý phiên bản mô hình** – Dễ dàng nâng cấp và kiểm soát hiệu suất mô hình.
* **Ứng dụng**: Chatbot AI, phân tích hình ảnh/video, hệ thống gợi ý sản phẩm.

***

### **3. Cách AI Platform Hoạt Động**

AI Engineer sử dụng **Notebook** để lập trình và chạy thử nghiệm AI. Dữ liệu, mô hình AI được lưu trên **Network Volume**. Khi đã có mô hình ban đầu, AI Engineer sử dụng **Model Tuning** để tối ưu hiệu suất mô hình. Mô hình AI sau khi huấn luyện sẽ được lưu trữ trong **Model Registry** để dễ dàng kiểm soát phiên bản. Khi mô hình sẵn sàng, AI Engineer triển khai nó trên **Inference**, giúp tạo API AI. Ứng dụng (web, mobile, chatbot) có thể gọi API từ Inference để sử dụng AI.

#### **Quy Trình Tổng Quan**

* **Bước 1: Chuẩn bị dữ liệu** – Dữ liệu AI được tải lên **Network Volume**.
  * AI Engineer tải dữ liệu huấn luyện lên **Network Volume** – nơi lưu trữ và chia sẻ dữ liệu giữa các phiên làm việc.
  * Dữ liệu có thể bao gồm **hình ảnh, văn bản, video, dữ liệu số, log file, v.v.**
  * AI Engineer chọn môi trường Notebook phù hợp (Python, TensorFlow, PyTorch, v.v.) để lập trình AI.
* **Bước 2: Huấn luyện mô hình** – AI Engineer lập trình trong **Notebook**, sử dụng tài nguyên tính toán trên cloud.
  * AI Engineer viết mã huấn luyện mô hình trên **Notebook**, sử dụng tài nguyên tính toán GPU.
  * Trong quá trình huấn luyện, mô hình sẽ học từ dữ liệu, tối ưu hóa tham số và lưu lại trạng thái.
  * Kết quả huấn luyện (mô hình, logs, checkpoints) được lưu vào **Network Volume**.
* **Bước 3: Tinh chỉnh mô hình** – Chạy **Model Tuning** để tìm tham số tối ưu.
  * AI Engineer sử dụng **Model Tuning** để tự động tối ưu hóa mô hình AI.
  * Hệ thống chạy nhiều phiên bản mô hình với các tham số khác nhau để tìm ra cấu hình tối ưu.
  * Kết quả của mỗi lần thử nghiệm được ghi nhận để phân tích.
* **Bước 4: Lưu trữ mô hình** – Mô hình đã huấn luyện được lưu vào **Model Registry**.
  * Khi mô hình đã đạt hiệu suất mong muốn, AI Engineer lưu nó vào **Model Registry**.
  * Model Registry giúp **quản lý phiên bản mô hình**, đảm bảo sự nhất quán khi triển khai.
* **Bước 5: Triển khai mô hình** – Mô hình được đưa vào **Inference** để tạo API AI.
  * AI Engineer chọn mô hình phù hợp từ **Model Registry** và triển khai trên **Inference**.
  * Mô hình được chuyển đổi thành API RESTful, có thể được gọi từ ứng dụng bên ngoài.
  * Inference hỗ trợ **tối ưu tốc độ suy luận (low-latency inference)** để đảm bảo phản hồi nhanh.
* **Bước 6: Sử dụng AI trong ứng dụng** – Ứng dụng gọi API từ **Inference** để chạy AI trên dữ liệu thực tế.
  * Ứng dụng web, mobile, chatbot hoặc hệ thống doanh nghiệp có thể gọi API từ **Inference Service**.
  * Dữ liệu đầu vào được gửi đến mô hình AI để suy luận.
  * Kết quả AI được trả về ứng dụng để hiển thị hoặc xử lý tiếp.
