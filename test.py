import streamlit as st
st.title('初めてのStreamlit')
st.write('これから作品を作っていきます')
text = st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は，',text,'です')
condition = st.slider('あなたの今の調子は？',0, 100, 50)