import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎮 캐릭터 성장")

df = pd.DataFrame({
    "레벨":[1,1,1,2,2,2,3,3,3,4,4,4],
    "캐릭터":["전사","궁수","마법사"]*4,
    "공격력":[20,18,25,35,30,40,50,45,60,70,62,80],
    "체력":[100,80,60,130,95,75,170,110,90,220,130,110]
})

fig = px.scatter(
    df,
    x="공격력",
    y="체력",
    animation_frame="레벨",
    animation_group="캐릭터",
    text="캐릭터",
    size="체력",
    range_x=[0,90],
    range_y=[0,240]
)

fig.update_traces(textposition="top center")

st.plotly_chart(fig, use_container_width=True)
