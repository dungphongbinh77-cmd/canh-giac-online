# RELEASE NOTES - STUDENT v1.1 DÙNG NGAY

## Thay đổi chính so với v1.0

- Bỏ hoàn toàn màn hình nhập mã học sinh.
- Không cần giáo viên cấp mã trước khi sử dụng.
- App tự tạo mã phiên ẩn danh dạng `ANON-XXXXXXXXXX`.
- Mã phiên chỉ dùng để liên kết dữ liệu luyện tập và tiến bộ; không chứa thông tin cá nhân.
- Giữ đầy đủ 4 chức năng chính: Kiểm tra thông điệp, Thử thách, Tiến bộ, An toàn số.
- Bỏ `data/student_codes.csv` và công cụ tạo mã học sinh.
- Cập nhật hướng dẫn triển khai, hướng dẫn học sinh và checklist phát hành.

## Lưu ý triển khai

Khi tạo QR hoặc gửi link cho học sinh, luôn dùng link gốc của app, ví dụ:

`https://canh-giac-online.streamlit.app`

Không dùng link sau khi đã mở app có dạng:

`https://canh-giac-online.streamlit.app/?u=ANON-...`

vì phần `u=ANON-...` là mã phiên riêng được tạo tự động.
