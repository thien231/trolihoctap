import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
            menu_title=None,  # required
            options=["Văn 9", "Toán 9", "Anh Văn 9", "Địa lý 9"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )   

if selected == "Văn 7":
 with st.container():
    st.title("Nhấn vào đường link để vào tài liệu môn Văn")
    st.title("[Văn 7](https://tailieu.com/ngu-van-7-c265)")

if selected == "Toán 7":
    st.title("Nhấn vào đường link để vào tài liệu môn Toán")
    st.title("[Toán 7](https://vietjack.com/giai-toan-lop-7/index.jsp)")

if selected == "Anh Văn 7":
    st.title("Nhấn vào đường link để vào tài liệu môn Toán")
    st.title("[Anh Văn 7](https://vietjack.com/tieng-anh-7/index.jsp)")

if selected == "Địa lý 7":
 with st.container():
    st.title("Nhấn vào đường link để vào tài liệu môn Địa lý")
    st.title("[Địa lý 7](https://vietjack.com/giai-bai-tap-dia-li-7/index.jsp)")