# KHẮC PHỤC LỆCH THỜI GIAN - CẢNH GIÁC ONLINE v1.2

## 1. Mã nguồn đã sửa
App ghi `created_at` bằng múi giờ IANA `Asia/Ho_Chi_Minh` và lưu rõ offset `+07:00`. Vì vậy giờ ghi không phụ thuộc múi giờ của máy chủ Streamlit, máy tính hay điện thoại.

Ví dụ mới: `2026-09-22 06:25:30+07:00`.

## 2. Đặt múi giờ Google Sheet
Trên MÁY TÍNH mở Google Sheet -> File -> Settings -> General:
- Locale: Vietnam
- Time zone: (GMT+07:00) Ho Chi Minh / Bangkok / Jakarta (chọn mục GMT+07 phù hợp hiển thị)
- Save settings

App dùng `RAW` khi ghi thời gian nên chuỗi `+07:00` vẫn được giữ nguyên; cài đặt của Sheet giúp các công thức/ngày giờ khác đồng nhất.

## 3. Kiểm tra trước khi deploy
Chạy:
```bash
python tools/check_time.py
```
Dòng `Viet Nam` phải kết thúc bằng `+07:00`.

## 4. Sửa các dòng cũ đã bị lệch 7 giờ (TÙY CHỌN)
Trước hết SAO LƯU Google Sheet. Sau đó chạy thử (không ghi):
```bash
python tools/fix_legacy_timestamps.py --json "C:\duongdan\service-account.json" --spreadsheet-id "ID_GOOGLE_SHEET"
```
Kiểm tra 5 dòng preview. Nếu đúng là dữ liệu cũ đang chậm 7 giờ, mới chạy:
```bash
python tools/fix_legacy_timestamps.py --json "C:\duongdan\service-account.json" --spreadsheet-id "ID_GOOGLE_SHEET" --apply
```
Script bỏ qua các dòng mới đã có `+07:00`, nên không cộng giờ lần thứ hai cho dữ liệu mới.

## 5. Deploy lại Streamlit
Upload/commit bản v1.2 lên GitHub. Streamlit sẽ cập nhật từ repository; nếu chưa thấy bản mới, vào Manage app -> Reboot app.

## 6. Kiểm tra cuối
1. Nhìn giờ hiện tại trên điện thoại/máy tính.
2. Làm 1 câu Thử thách.
3. Mở `quiz_attempts` trên Google Sheet.
4. Cột `created_at` phải cùng giờ Việt Nam và có `+07:00`.
5. Thử 1 lần Kiểm tra thông điệp và kiểm tra `message_checks`.
