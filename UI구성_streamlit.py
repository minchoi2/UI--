import streamlit as st
st.set_page_config(layout = 'wide')
# 제목
st.title('KO Chatbot Arena Demo')
# 탭 나누기
tab1, tab2, tab3 = st.tabs(['Chatbot Arena', 'RAG Arena', 'Leaderboard'])
# tab1
with tab1:
    st.title('KO Chatbot Arena Demo')
    st.subheader('안내 사항 보기')
    col1, col2 = st.columns(2)
    with col1:
        st.text('Model A')
    with col2:
        st.text('Model B')
    def main():
        frame = st.text_input('메시지를 입력하세요.')
        st.text(frame)
    col3, col4 = st.columns(2)
    with col3:
        st.button('새 게임')
    with col4:
        st.button('대화 초기화')
    st.text('Use via API - gradio로 제작되었습니다.')
# tab2
with tab2:
    st.title('KO Chatbot Arena Demo')
    st.subheader('안내 사항 보기')
    st.text('Context')
    def main():
        frame2 = st.text_input('Context를 입력하세요.')
        st.text(frame2)
    col5, col6 = st.columns(2)
    with col5:
        st.text('Model A')
    with col6:
        st.text('Model B')
# tab3
import pandas as pd
