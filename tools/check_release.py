from pathlib import Path
import sys
import pandas as pd
import joblib

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / 'app.py',
    ROOT / 'requirements.txt',
    ROOT / 'model' / 'classifier.joblib',
    ROOT / 'data' / 'situations.csv',
    ROOT / 'modules' / 'storage.py',
    ROOT / 'modules' / 'warning_rules.py',
]

errors = []
print('=== KIEM TRA BAN PHAT HANH HOC SINH v1.1 ===')
for path in required:
    ok = path.exists()
    print(('OK   ' if ok else 'THIEU'), path.relative_to(ROOT))
    if not ok:
        errors.append(str(path))

if not errors:
    quiz = pd.read_csv(ROOT / 'data' / 'situations.csv')
    print(f'OK   So cau thu thach: {len(quiz)}')
    if 'question_id' in quiz.columns and quiz['question_id'].duplicated().any():
        errors.append('question_id bi trung')

    app_text = (ROOT / 'app.py').read_text(encoding='utf-8')
    forbidden = ['Nhập mã học sinh do giáo viên cấp', 'student_codes.csv', 'load_allowed_codes']
    for text in forbidden:
        if text in app_text:
            errors.append(f'Con noi dung cu: {text}')

    if 'get_anonymous_session_id' not in app_text or 'ANON-' not in app_text:
        errors.append('Chua co co che ma phien an danh tu dong')

    model = joblib.load(ROOT / 'model' / 'classifier.joblib')
    samples = [
        'Tài khoản của bạn sẽ bị khóa trong 10 phút, hãy bấm link và nhập OTP.',
        'Chiều mai lớp mình học Tin học lúc 14 giờ tại phòng máy.',
        'Thầy nhắc các em không cung cấp mã OTP cho bất kỳ ai.',
    ]
    probs = model.predict_proba(samples)[:,1]
    for s, p in zip(samples, probs):
        print(f'P={p:.3f} | {s}')

if errors:
    print('\nCHUA SAN SANG PHAT HANH')
    for e in errors:
        print('-', e)
    sys.exit(1)

print('\nSAN SANG PHAT HANH')
