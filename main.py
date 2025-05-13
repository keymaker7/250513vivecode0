import streamlit as st

# 💡 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🔮")

# 🎨 타이틀
st.title("🔮 MBTI로 알아보는 나의 진로")
st.markdown("당신의 MBTI 유형을 선택하면, 잘 어울리는 직업을 추천해드릴게요! 💼✨")

# 🧠 MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 💼 MBTI별 추천 직업 사전
mbti_jobs = {
    "INTJ": ["🔬 과학자", "🧠 전략 컨설턴트", "🧑‍💻 인공지능 개발자"],
    "INTP": ["💡 발명가", "🧪 연구원", "👨‍💻 데이터 분석가"],
    "ENTJ": ["📈 CEO", "🏛️ 변호사", "👩‍💼 프로젝트 매니저"],
    "ENTP": ["🎤 방송인", "💼 창업가", "🤹 기획자"],
    "INFJ": ["🧑‍🏫 교사", "📝 작가", "🧘‍♀️ 상담사"],
    "INFP": ["🎨 예술가", "📖 소설가", "🧑‍🎨 디자이너"],
    "ENFJ": ["👩‍🏫 교육자", "📢 캠페이너", "💖 사회복지사"],
    "ENFP": ["🌍 여행가", "🎭 배우", "🎨 크리에이터"],
    "ISTJ": ["🧾 회계사", "⚖️ 공무원", "📦 물류관리자"],
    "ISFJ": ["🧑‍⚕️ 간호사", "📚 사서", "🏫 교직원"],
    "ESTJ": ["📋 관리자", "🏢 기업인", "🧑‍⚖️ 법무관"],
    "ESFJ": ["👨‍🍳 요리사", "👩‍💻 서비스 매니저", "👨‍👩‍👧‍👦 상담사"],
    "ISTP": ["🛠️ 기술자", "🚗 자동차 정비사", "🏗️ 건축가"],
    "ISFP": ["📷 사진작가", "🎨 플로리스트", "🎼 작곡가"],
    "ESTP": ["📣 마케터", "🎬 프로듀서", "🚀 창업가"],
    "ESFP": ["🎤 연예인", "🕺 댄서", "🎉 이벤트 플래너"]
}

# 🔎 사용자 입력 받기
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요! 🧩", mbti_types)

# ✅ 추천 결과 출력
if selected_mbti:
    st.markdown("---")
    st.subheader(f"✨ {selected_mbti} 유형에게 어울리는 직업은?")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
    st.markdown("---")
    st.success("🎉 진로는 자신만의 색으로 그려가는 여정이에요. 당신만의 길을 응원합니다!")

# 📝 추가 메시지
st.markdown("💬 **MBTI는 참고용일 뿐이에요!** 다양한 경험을 통해 스스로에게 맞는 진로를 찾아가보세요 😊")
