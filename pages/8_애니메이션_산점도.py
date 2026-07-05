import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎬 애니메이션 산점도")

# 데이터 만들기
df = pd.DataFrame({
    "학년":[1,1,1,2,2,2,3,3,3],
    "반":["1반","2반","3반"]*3,
    "평균키":[160,162,161,166,167,165,170,171,169],
    "평균몸무게":[52,54,53,57,58,56,61,63,60]
})

# 애니메이션 산점도
fig = px.scatter(
    df,
    x="평균키",
    y="평균몸무게",
    animation_frame="학년",     # 시간 역할
    animation_group="반",       # 같은 반이 계속 움직임
    text="반",
    range_x=[155,175],
    range_y=[45,70],
    size_max=20,
    title="학년이 올라갈수록 평균 키와 몸무게 변화"
)

fig.update_traces(textposition="top center")

st.plotly_chart(fig, use_container_width=True)
