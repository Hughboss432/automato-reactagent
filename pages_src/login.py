import streamlit as st

class LoginPage:                                    # Login page
    def render(self):
        st.title("Log-in")

        user = st.text_input("Usuário")
        pwd = st.text_input("Senha", type="password")

        if st.button("Log-in"):
            if user == "admin" and pwd == "admin":
                st.session_state.user = "Admin"
                st.session_state.page = "admin"
                st.rerun()
            else:
                st.error('Usuário ou senha incorreto.')
                #st.session_state.user = "User"
                #st.session_state.page = "home"
                #st.rerun()