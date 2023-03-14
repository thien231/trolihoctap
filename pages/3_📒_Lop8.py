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

if selected == "Văn 8":
 with st.container():
    st.title("Nhấn vào đường link để vào tài liệu môn Văn")
    st.title("[Văn 8](https://tailieu.com/ngu-van-8-c265)")

if selected == "Toán 8":
    st.title("Nhấn vào đường link để vào tài liệu môn Toán")
    st.title("[Toán 8](https://vietjack.com/giai-toan-lop-8/index.jsp)")

if selected == "Anh Văn 8":
    st.title("Nhấn vào đường link để vào tài liệu môn Toán")
    st.title("[Anh Văn 8](https://vietjack.com/tieng-anh-8/index.jsp)")

if selected == "Địa lý 8":
 with st.container():
    st.title("Nhấn vào đường link để vào tài liệu môn Địa lý")
    st.title("[Địa lý 8](https://vietjack.com/giai-bai-tap-dia-li-8/index.jsp)")