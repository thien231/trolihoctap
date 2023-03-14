import config
import requests
import openai
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_chat import message

# Tìm thêm emoji tại: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Trợ lí AI", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

openai.api_key = config.API_KEY

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5,

    )
    message = completions.choices[0].text
    return message
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_itilDAyVNt.json")
left_column, right_column = st.columns(2)
with right_column:
 st_lottie(lottie_coding, height=200 , key="AI")
st.title("Xin chào, tôi là một Trợ lý học tập.")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", "Nhập câu hỏi nào đây.", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
with st.container():
    st.write("---")
    st.header(":pencil: Hãy đưa ra nhận xét hoặc lỗi cho tôi chỉnh sửa lại!")
    st.write("##")
contact_form = """
<form action="https://formsubmit.co/wgjack13@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Tên bạn" required>
     <input type="email" name="email" placeholder="Tên email" required>
     <textarea name="message" placeholder="Tin nhắn bạn cần nhắn"></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
        st.empty()
hide_st_style = """
            <style>
            {visibility: hidden;}
            footer {visibility : hidden;}
            header {visibility : hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.sidebar.success("Select a page above.")
