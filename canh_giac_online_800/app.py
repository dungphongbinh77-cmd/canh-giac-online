from pathlib import Path
import random
import joblib
import pandas as pd
import streamlit as st

from modules.warning_rules import find_warning_signs, education_advice

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model" / "classifier.joblib"
QUIZ_PATH = ROOT / "data" / "situations.csv"

st.set_page_config(page_title="Cảnh giác Online", page_icon="🛡️", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_quiz():
    return pd.read_csv(QUIZ_PATH)

st.title("🛡️ CẢNH GIÁC ONLINE")
st.caption("Hệ thống hỗ trợ nhận diện và rèn luyện kỹ năng phòng tránh thông điệp lừa đảo trực tuyến")

tab1, tab2, tab3 = st.tabs(["🔎 Kiểm tra", "🎮 Thử thách", "📚 Góc an toàn số"])

with tab1:
    st.subheader("Kiểm tra một thông điệp")
    text = st.text_area(
        "Nhập hoặc dán nội dung tin nhắn:",
        height=150,
        placeholder="Ví dụ: Tài khoản của bạn sẽ bị khóa trong 10 phút..."
    )

    if st.button("PHÂN TÍCH", type="primary"):
        if not text.strip():
            st.warning("Hãy nhập nội dung cần kiểm tra.")
        elif not MODEL_PATH.exists():
            st.error("Chưa có mô hình. Hãy chạy: python model/train.py")
        else:
            model = load_model()
            proba = float(model.predict_proba([text])[0][1])
            score = round(proba * 100, 1)

            if score >= 70:
                level = "🔴 NGUY CƠ CAO"
            elif score >= 40:
                level = "🟡 CẦN THẬN TRỌNG"
            else:
                level = "🟢 NGUY CƠ THẤP"

            signs = find_warning_signs(text)
            advice = education_advice(signs)

            st.metric("Điểm nguy cơ do mô hình ước lượng", f"{score}%")
            st.subheader(level)

            st.markdown("**Dấu hiệu hệ thống phát hiện:**")
            if signs:
                for s in signs:
                    st.write("✓", s)
            else:
                st.write("Chưa phát hiện quy tắc cảnh báo nổi bật.")

            st.markdown("**Khuyến nghị:**")
            for item in advice:
                st.write("•", item)

            st.info(
                "Kết quả chỉ có tính hỗ trợ học tập. Không dùng ứng dụng để thay thế việc xác minh "
                "qua cha mẹ, giáo viên hoặc kênh chính thức."
            )

with tab2:
    st.subheader("Trò chơi: Bạn sẽ làm gì?")
    quiz = load_quiz()

    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = random.randrange(len(quiz))
        st.session_state.quiz_checked = False

    row = quiz.iloc[st.session_state.quiz_index]
    st.write(row["question"])

    choice = st.radio(
        "Chọn phương án:",
        ["A", "B", "C", "D"],
        format_func=lambda x: f"{x}. {row[x]}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Kiểm tra đáp án"):
            st.session_state.quiz_checked = True

    with col2:
        if st.button("Câu khác"):
            st.session_state.quiz_index = random.randrange(len(quiz))
            st.session_state.quiz_checked = False
            st.rerun()

    if st.session_state.quiz_checked:
        if choice == row["answer"]:
            st.success("Chính xác!")
        else:
            st.error(f"Chưa đúng. Đáp án phù hợp là {row['answer']}.")
        st.write("**Giải thích:**", row["explanation"])

with tab3:
    st.subheader("5 nguyên tắc an toàn")
    st.write("1. Không cung cấp OTP, mật khẩu hoặc mã xác thực cho người khác.")
    st.write("2. Không bấm đường link lạ trong các tin nhắn bất ngờ.")
    st.write("3. Không chuyển tiền chỉ vì người nhắn tạo cảm giác khẩn cấp.")
    st.write("4. Kiểm tra thông tin qua website, ứng dụng hoặc số điện thoại chính thức.")
    st.write("5. Khi chưa chắc chắn, hãy hỏi cha mẹ, giáo viên hoặc người lớn đáng tin cậy.")
