# DEPLOY BẢN HỌC SINH - KHÔNG CẦN MÃ

## 1. Upload lên GitHub

Tạo repository mới, ví dụ `canh-giac-online-student`.
Upload toàn bộ nội dung dự án, không upload file ZIP.

## 2. Streamlit Secrets

Dùng cùng `spreadsheet_id` và Service Account đã thử nghiệm thành công.
Dán nội dung Secrets vào:

`Streamlit Community Cloud > App > Settings > Secrets`

Không cần danh sách mã học sinh và không cần `admin_pin` cho bản học sinh.

## 3. Deploy

- Repository: repository bản học sinh.
- Branch: `main`.
- Main file: `app.py`.

## 4. Kiểm tra trước khi phát link

1. Mở app bằng đường link gốc, không thêm tham số.
2. App phải vào thẳng Trang chủ, không hỏi mã học sinh.
3. Vào Kiểm tra thông điệp và phân tích một tin nhắn mẫu.
4. Làm ít nhất 2 câu Thử thách.
5. Vào Tiến bộ của tôi và kiểm tra số lượt đã ghi nhận.
6. Tải lại trang: tiến độ của cùng phiên phải vẫn truy xuất được nếu tham số phiên còn trong URL.
7. Mở Google Sheet và kiểm tra `quiz_attempts` và `message_checks` có thêm dữ liệu với mã dạng `ANON-...`.

Chỉ phát link sau khi cả 7 bước đều đạt.

## 5. Lưu ý khi phát link

Hãy phát **đường link gốc của app**, ví dụ:

`https://ten-app.streamlit.app`

Không phát đường link có `?u=ANON-...` vì đó là mã phiên riêng của một người dùng.
