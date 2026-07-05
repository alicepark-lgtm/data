import streamlit as st
import pandas as pd

st.title("📈 두 개의 라인 비교")

df = pd.DataFrame({
    "월":["1월","2월","3월","4월","5월","6월"],
    "서울":[3,5,10,16,22,27],
    "부산":[5,7,12,17,21,25]
})

st.dataframe(df)

st.line_chart(df.set_index("월"))
