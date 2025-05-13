import streamlit as st

st.set_page_config(page_title="🌟 MBTI 성향별 진로 탐색기", page_icon="🧭")

st.markdown("""
# 💫 MBTI 성향으로 알아보는 진로 탐색기  
### 내 성향을 이해하고, 나에게 맞는 진로를 찾아보세요! 💼🚀  
""")

st.markdown("---")

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_data = {
    "INTJ": {
        "desc": "🧠 논리적이고 미래지향적인 전략가. 독립성과 분석력으로 장기 목표를 계획하고 성취함.",
        "fields": {
            "과학·기술 분야": ["AI 개발자 🤖", "데이터 과학자 📊", "시스템 엔지니어 🛠️"],
            "경영·전략 분야": ["전략기획자 🧩", "IT 컨설턴트 💼"]
        },
        "reason": "복잡한 문제를 체계적으로 분석하고 해결하는 능력이 뛰어나므로 분석적이고 구조화된 분야가 잘 맞습니다."
    },
    "INFP": {
        "desc": "🌸 감성적이고 창의적인 이상주의자. 개인의 가치와 감정을 중요시하며 타인에 대한 공감력이 뛰어남.",
        "fields": {
            "예술·창작 분야": ["시인 ✍️", "일러스트레이터 🎨", "콘텐츠 크리에이터 🎥"],
            "상담·교육 분야": ["심리상담가 💬", "청소년 지도사 🧒"]
        },
        "reason": "감정을 표현하고 타인을 돕는 일에 보람을 느끼므로 예술적·심리적 활동에서 큰 만족을 얻습니다."
    },
    "ENTP": {
        "desc": "💡 도전적이고 아이디어가 풍부한 혁신가. 변화에 유연하고 다양한 사람들과의 소통을 즐김.",
        "fields": {
            "창업·기획 분야": ["스타트업 CEO 🚀", "제품 매니저 📱", "브랜드 디자이너 🧃"],
            "미디어·커뮤니케이션 분야": ["방송인 🎙️", "광고 기획자 📣"]
        },
        "reason": "창의성과 설득력을 활용하여 새롭고 독창적인 길을 개척하는 데 강점을 가집니다."
    },
    "ISFJ": {
        "desc": "💖 조용하지만 따뜻하고 헌신적인 보호자. 실용적이고 성실하며 다른 사람을 돕는 것을 중요하게 여김.",
        "fields": {
            "복지·보건 분야": ["간호사 👩‍⚕️", "사회복지사 🧓", "재활치료사 🧑‍🦽"],
            "행정·교육 분야": ["교직원 🏫", "학생지도 교사 📘"]
        },
        "reason": "책임감과 배려심이 강하여 안정적이고 봉사적인 역할에서 두각을 나타냅니다."
    },
    "ENFP": {
        "desc": "🌈 활기차고 자유로운 영혼의 소유자. 감성적이면서도 외향적인 에너지로 주변을 밝게 만듦.",
        "fields": {
            "예술·공연 분야": ["배우 🎭", "무용가 💃", "콘서트 기획자 🎤"],
            "디지털 콘텐츠 분야": ["유튜버 🎥", "SNS 마케터 📲"]
        },
        "reason": "창의적 표현과 대인 관계를 즐기며 다양성과 자유를 추구하는 직무에 적합합니다."
    },
    # 💡 필요한 만큼 계속 추가 가능
}

selected_mbti = st.selectbox("🔍 당신의 MBTI 유형을 선택하세요", mbti_types)

if selected_mbti in mbti_data:
    data = mbti_data[selected_mbti]

    st.markdown("---")
    st.subheader(f"🔍 MBTI 해석: {selected_mbti}")
    st.markdown(f"**{data['desc']}**")

    st.markdown("## 💼 추천 진로 분야 및 예시")
    for field, jobs in data["fields"].items():
        st.markdown(f"### 🧭 {field}")
        for job in jobs:
            st.markdown(f"- {job}")
        st.markdown("")

    st.markdown("## 📌 추천 이유")
    st.info(data["reason"])

    st.markdown("---")
    st.success("🎯 성향은 진로를 찾는 강력한 나침반입니다. 다양한 가능성을 열어두고 자신만의 길을 설계해 보세요!")
