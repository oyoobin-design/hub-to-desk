import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime as dt
import datetime

# --- 0. 페이지 설정 (가장 먼저 실행되어야 함) ---
st.set_page_config(
    page_title="스트림릿 통합 연습장",
    page_icon="🚀",
    layout="wide"
)

# --- 1. 타이틀 및 헤더 영역 ---
st.title("이게 타이틀이다! 😊")
st.header("이게 헤더다! 🌞")
st.subheader("이게 서브헤더다! ❤️")

# 이모지 연습
col_emoji1, col_emoji2 = st.columns(2)
with col_emoji1:
    st.text("별 : ⭐")
    st.text("음표 : 🎵")
with col_emoji2:
    st.text("체크 : ✅")
    st.text("불꽃 : 🔥")

st.divider() # 구분선

# --- 2. 텍스트 요소 ---
st.text("이게 일반 텍스트다!")
st.caption("이게 캡션(설명문)이다!")
st.markdown("마크다운 문법도 지원합니다! **굵게**, *기울임*, ~~취소선~~, `코드` 가능")

# 코드 표시
sample_code = '''def hello_world():
    print("Hello, World!")'''
st.code(sample_code, language='python')

# 색상 텍스트 및 수식
st.markdown("텍스트 색상 변경: :green[초록], :red[빨강], :blue[파란색]")
st.markdown(":green[$\sqrt{x^2 + y^2} = 1$] (LaTeX 수식 지원)")
st.latex(r'\sqrt{x^2 + y^2} = 1')

st.divider()

# --- 3. 데이터 출력 영역 ---
st.title("데이터 출력하기")
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

col_df1, col_df2 = st.columns(2)
with col_df1:
    st.subheader("데이터프레임 (대화형)")
    st.dataframe(df)
with col_df2:
    st.subheader("테이블 (정적)")
    st.table(df)

st.divider()

# --- 4. 메트릭(지표) 영역 ---
st.title("실시간 지표(Metric)")
st.metric(label="현재 온도", value="25 °C", delta="1.2 °C")

# 컬럼으로 나누어 표기 (무역/금융 예시)
m1, m2, m3 = st.columns(3)
m1.metric(label="달러 USD", value="1,471원", delta="+30원")
m2.metric(label="유로 EUR", value="1,590원", delta="+20원")
m3.metric(label="엔 JPY", value="1,123원", delta="-5원")

st.divider()

# --- 5. 입력 위젯 영역 ---
st.title("다양한 입력 도구")

# 버튼과 체크박스
if st.button("클릭 시 효과 발생"):
    st.balloons() # 풍선 효과
    st.success("버튼이 눌렸습니다!")

if st.checkbox("체크박스를 선택하면 눈이 내려요"):
    st.snow()

# 라디오 버튼 (MBTI)
mbti = st.radio("당신의 MBTI는?", ("ENFP", "INTJ", "ISTP"))
if mbti == "ENFP":
    st.write("당신은 :red[열정적인 활동가]입니다!")
elif mbti == "INTJ":
    st.write("당신은 :blue[전략적인 사색가]입니다!")
else:
    st.write("당신은 :green[논리적인 분석가]입니다!")

# 셀렉트박스 (오류 수정 완료)
favorite_color = st.selectbox("가장 좋아하는 색깔은?", 
                              ("빨강", "파랑", "초록", "노랑", "보라"))
color_map = {
    "빨강": "red", "파랑": "blue", "초록": "green", 
    "노랑": "orange", "보라": "purple" # 노랑은 orange가 가독성이 좋습니다.
}
st.write(f"선택한 색깔: :{color_map[favorite_color]}[{favorite_color}]")

# 멀티셀렉트
hobbies = st.multiselect("취미를 모두 골라주세요", ["독서", "여행", "운동", "요리", "게임"])
if hobbies:
    st.write(f"당신의 취미는 :blue[{', '.join(hobbies)}] 이군요!")

# 슬라이더 (숫자 및 범위)
age = st.slider("나이", 0, 100, 25)
st.write(f"나이는 :blue[{age}살]입니다.")

val_range = st.slider("범위 선택", 0.0, 100.0, (25.0, 75.0))
st.write(f"범위: :green[{val_range[0]}] ~ :green[{val_range[1]}]")

# 날짜/시간 슬라이더
target_date = st.slider(
    "약속 날짜",
    min_value=dt(2026, 1, 1),
    max_value=dt(2026, 12, 31),
    value=dt(2026, 1, 15),
    step=datetime.timedelta(days=1),
    format="YYYY-MM-DD"
)
st.write(f"선택일: :red[{target_date.date()}]")

st.divider()

# --- 6. 입력 및 다운로드 ---
# 텍스트 입력 (콤마 오류 수정 완료)
destination = st.text_input(
    label="가고 싶은 여행지",
    value="제주도",
    placeholder="예: 파리, 뉴욕, 도쿄"
)
st.write(f"목적지: :green[{destination}]")

# 숫자 입력
fav_num = st.number_input("좋아하는 숫자 (0~100)", 0, 100, 7)

# 파일 다운로드 버튼
st.download_button(
    label="데이터 CSV 다운로드",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="my_data.csv",
    mime="text/csv"
)