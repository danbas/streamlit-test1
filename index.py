import streamlit as st
import pandas as pd

df = pd.DataFrame({
    
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
    
    
})

#df

st.line_chart(df)
st.dataframe(df.style.highlight_max(axis=0))
