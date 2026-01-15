import streamlit as st
import random
from datetime import datetime

# --- 1. 페이지 기본 설정 (반드시 맨 위에 와야 합니다) ---
st.set_page_config(
    page_title="인생역전! 행운의 로또",
    page_icon="🍀",
    layout="centered",  # 중앙 정렬 레이아웃
    initial_sidebar_state="collapsed"
)

# --- 2. 로또 번호 생성 함수 (기존 논리 유지) ---
def generate_lotto_numbers():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)
    return sorted(list(lotto))

# --- 3. 로또볼 디자인을 위한 CSS 스타일 ---
# 이 부분은 HTML/CSS를 이용해 숫자를 동그란 공처럼 보이게 만듭니다.
st.markdown("""
<style>
    .lotto-ball {
        display: inline-block;
        width: 45px;
        height: 45px;
        line-height: 45px;
        border-radius: 50%;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        color: white;
        margin: 5px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    /* 로또 번호대별 색상 지정 (실제 로또 색상 참고) */
    .ball-1-10 { background-color: #fbc400; } /* 노랑 */
    .ball-11-20 { background-color: #69c8f2; } /* 파랑 */
    .ball-21-30 { background-color: #ff7272; } /* 빨강 */
    .ball-31-40 { background-color: #aaa; }    /* 회색 */
    .ball-41-45 { background-color: #b0d840; } /* 초록 */
</style>
""", unsafe_allow_html=True)

# 번호에 맞는 색상 클래스를 찾아주는 도우미 함수
def get_ball_class(number):
    if 1 <= number <= 10: return "ball-1-10"
    elif 11 <= number <= 20: return "ball-11-20"
    elif 21 <= number <= 30: return "ball-21-30"
    elif 31 <= number <= 40: return "ball-31-40"
    else: return "ball-41-45"


# --- 4. 메인 화면 구성 ---

# 헤더 영역
st.markdown("<h1 style='text-align: center;'>💎 금주의 행운 번호 추출기</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>정성을 다해 뽑아드립니다! 5세트의 행운을 받아가세요.</p>", unsafe_allow_html=True)
st.divider()

# 버튼 영역 (중앙 정렬을 위해 컬럼 사용)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # type="primary"로 버튼을 강조색으로 변경, use_container_width로 꽉 차게
    generate_btn = st.button("🎲 행운의 번호 생성 시작!", type="primary", use_container_width=True)

# 결과 출력 영역
if generate_btn:
    # 스피너로 로딩 효과 주기
    with st.spinner("행운의 기운을 모으는 중입니다... 💫"):
        
        st.write("") # 약간의 여백
        
        # 5세트 반복
        for i in range(1, 6):
            lotto_numbers = generate_lotto_numbers()
            
            # 컨테이너로 묶어서 세트별 구분감 주기
            with st.container(border=True):
                st.markdown(f"#### ✨ {i}번째 행운 세트")
                
                # 로또볼 HTML 문자열 만들기
                ball_html = ""
                for num in lotto_numbers:
                    ball_class = get_ball_class(num)
                    ball_html += f'<div class="lotto-ball {ball_class}">{num}</div>'
                
                # 화면에 로또볼 출력
                st.markdown(f"<div style='text-align: center;'>{ball_html}</div>", unsafe_allow_html=True)

        # 푸터 영역 (결과가 나왔을 때만 표시)
        st.divider()
        now = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분")
        st.info(f"🕒 생성 완료 시각: {now}")
        st.caption("⚠️ 본 결과는 무작위로 생성되었으며, 실제 당첨을 보장하지 않습니다. 재미로만 즐겨주세요!")