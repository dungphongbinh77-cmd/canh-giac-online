# CẢNH GIÁC ONLINE - MVP

## 1. Mục tiêu
Sản phẩm mẫu cho dự án KHKT lớp 9:
- Phân loại thông điệp có nguy cơ lừa đảo.
- Giải thích các dấu hiệu đáng ngờ.
- Đưa ra khuyến nghị an toàn.
- Luyện tập qua tình huống.

## 2. Cài đặt
Mở Terminal/Command Prompt tại thư mục dự án:

```bash
pip install -r requirements.txt
```

## 3. Huấn luyện mô hình
```bash
python model/train.py
```

Sau khi chạy sẽ tạo:
`model/classifier.joblib`

## 4. Chạy ứng dụng
```bash
streamlit run app.py
```

## 5. Lưu ý khoa học
Bộ dữ liệu 100 mẫu trong bản MVP chỉ để minh họa kỹ thuật.
Khi làm đề tài chính thức nên:
- tăng lên khoảng 600-1000 mẫu;
- xây tiêu chí gán nhãn rõ ràng;
- có ít nhất 2 người gán nhãn độc lập;
- tách train/test hợp lý;
- báo cáo Accuracy, Precision, Recall, F1 và Confusion Matrix;
- thử nghiệm pre-test/post-test với học sinh.

## 6. Bộ dữ liệu 800 mẫu
Phiên bản này thay `data/messages.csv` bằng 800 mẫu mô phỏng có cấu trúc:
`id, message, label, category, red_flags, source_type, difficulty, template_id, split`.

Phân bố:
- 400 mẫu nguy cơ, 8 nhóm x 50 mẫu.
- 400 mẫu bình thường, 8 nhóm x 50 mẫu.
- train: 560; validation: 120; test: 120.
- Hai nhãn cân bằng trong từng split: train 280/280, validation 60/60, test 60/60.

Bản 100 mẫu ban đầu được giữ tại `data/messages_100_mvp_backup.csv`.

**Lưu ý:** dữ liệu là dữ liệu mô phỏng phục vụ nghiên cứu/giảng dạy, không phải tập dữ liệu đại diện cho toàn bộ lừa đảo ngoài đời. Trước khi dùng cho báo cáo chính thức, học sinh nên rà soát, gán nhãn độc lập và bổ sung mẫu thực tế đã ẩn danh theo quy trình đạo đức dữ liệu.


## 7. Lưu ý khi đánh giá mô hình
Phiên bản 800 mẫu đã có cột `split` cố định và `model/train.py` sử dụng trực tiếp train/validation/test. Các họ câu chữ (`template_id`) được giữ trong cùng một split để giảm việc mô hình nhìn thấy cùng một mẫu câu ở cả train và test. Dù vậy, đây vẫn là dữ liệu mô phỏng nên kết quả cao không được xem là bằng chứng mô hình sẽ đạt hiệu quả tương tự ngoài thực tế.
