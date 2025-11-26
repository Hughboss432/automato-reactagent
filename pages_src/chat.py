import streamlit as st
import asyncio
from ai_core.mcp_tools import connect_to_server
from langchain_core.messages import AIMessage, HumanMessage

class AIChatPage:                                   # AI Chat page
    def render(self):
        st.title("AI Chat")
        st.caption(f"👤 User: {st.session_state.get('user', 'Unknown')}")
        st.divider()

        if "chat" not in st.session_state:
            st.session_state.chat = []

        for message in st.session_state.chat:
            st.write(message.content)

        user_input = st.text_input("Mensagem:", "")
        if st.button("Enviar"):
            if user_input.strip() != "":
                try:
                    st.session_state.chat.append(HumanMessage(content=f"👤 Usuário: {user_input}"))
                    response = asyncio.run(connect_to_server(st.session_state.chat[-5:]))
                    st.session_state.chat.append(AIMessage(content=f"🤖 AI: {response}"))
                    st.rerun()
                except Exception as e:
                    st.error(f'Algo deu errado com o agente: {e}')

