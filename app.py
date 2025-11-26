import streamlit as st
import pandas as pd
from pages_src.home import HomePage
from pages_src.chat import AIChatPage
from pages_src.login import LoginPage
from pages_src.admin import AdminPage

class AppController:                                  # Side bar Menu
    def render_menu(self):
        menu = st.sidebar.radio("Menu", ["Home", "AI Chat", "Account"])

        if menu == "Home":
            st.session_state.page = "home"
        elif menu == "AI Chat":
            st.session_state.page = "chat"
        elif menu == "Account":
            st.session_state.page = "login"

class App:                                            # Class page controller
    def __init__(self):
        if "page" not in st.session_state:            # Page state
            st.session_state.page = "home"
        if "user" not in st.session_state:            # User state
            st.session_state.user = "Unknown"
        if "btn_adm" not in st.session_state:         # bnt state
            st.session_state.btn_adm = "None"
        if "db" not in st.session_state:
            st.session_state.db = pd.DataFrame(columns=["Nome", "Preço", "Quantidade", "Descrição"])

        self.home = HomePage()
        self.chat = AIChatPage()
        self.login = LoginPage()
        self.admin = AdminPage()
        self.controller = AppController()

    def run(self):
        self.controller.render_menu()

        if st.session_state.page == "home":
            self.home.render()

        elif st.session_state.page == "chat":
            self.chat.render()

        elif st.session_state.page == "login":
            if st.session_state.get("user") == "Admin":
                self.admin.render()
            else:
                self.login.render()

        elif st.session_state.page == "admin":
            self.admin.render()

if __name__ == "__main__":
    app = App()
    app.run()
