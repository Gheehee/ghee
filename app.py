import streamlit as st
import os

# Streamlit 페이지 설정
st.set_page_config(
    page_title="동물 스트레스 음성 인식 프로젝트",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# HTML 파일 경로 설정
html_file_path = os.path.join(os.path.dirname(__file__), 'htmls', 'index.html')

# HTML 파일이 존재하는지 확인
if os.path.exists(html_file_path):
    # HTML 파일 읽기
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code = f.read()

    # Streamlit에 HTML 코드 렌더링
    st.components.v1.html(html_code, height=1500, scrolling=True)
else:
    st.error(f"HTML 파일을 찾을 수 없습니다: {html_file_path}")
    st.markdown("`htmls` 폴더 안에 `index.html` 파일이 있는지 확인해 주세요.")