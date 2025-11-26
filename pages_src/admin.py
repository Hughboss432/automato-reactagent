import streamlit as st
import pandas as pd

class AdminPage:                                     # Super user page
    def render(self):
        st.title("Administração do Sistema")
        user = st.session_state.get("user", "Desconhecido") 
        st.caption(f"👤 Usuário logado: **{user}**")
        st.divider()

        st.subheader("Funções disponíveis")          # CRUD Menu
        prod = st.session_state.db                   # Save Database
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            create_btn = st.button("➕ Create", use_container_width=True)
        with col2:
            view_btn   = st.button("📄 View", use_container_width=True)
        with col3:
            update_btn = st.button("✏️ Update", use_container_width=True)
        with col4:
            delete_btn = st.button("🗑️ Delete", use_container_width=True)
        st.divider()

        if create_btn:
            st.session_state.btn_adm = "create_btn"
        elif view_btn:
            st.session_state.btn_adm = "view_btn"
        elif update_btn:
            st.session_state.btn_adm = "update_btn"
        elif delete_btn:
            st.session_state.btn_adm = "delete_btn"

        if st.session_state.btn_adm == "create_btn":
            st.markdown("### ➕ Criar novo produto")
            pdt_name = st.text_input("Nome do produto")
            pdt_price = st.number_input("Preço", min_value=0.0)
            pdt_num = st.number_input("Quantidade", min_value=1)
            pdt_desc = st.text_input("Descrição do produto")
            if st.button("Salvar"):
                new_pdt = novo_produto = pd.DataFrame(
                    {"Nome": [pdt_name], "Preço": [pdt_price], "Quantidade": [pdt_num], "Descrição": [pdt_desc]}
                )
                st.session_state.db = pd.concat(
                    [st.session_state.db, new_pdt],
                    ignore_index=True
                )
                st.success(f"Produto '{pdt_name}' cadastrado com sucesso!")
        elif st.session_state.btn_adm == "view_btn":
            st.markdown("### 📄 Produtos cadastrados")
            st.dataframe(st.session_state.db)
        elif st.session_state.btn_adm == "update_btn":
            st.markdown("### ✏️ Atualizar produto")
            produto = st.selectbox(
                "Escolha o produto",
                prod["Nome"].tolist()  
            )
            new_pdt_name = st.text_input("Novo nome", value=produto)
            new_pdt_price = st.number_input("Novo preço", min_value=0.0)
            new_pdt_num = st.number_input("Nova quantidade", min_value=1)
            new_pdt_desc = st.text_input("Nova descrição")
            if st.button("Atualizar"):
                idx = prod.index[prod["Nome"] == produto][0]
                st.session_state.db.loc[idx, "Nome"] = new_pdt_name
                st.session_state.db.loc[idx, "Preço"] = new_pdt_price
                st.session_state.db.loc[idx, "Quantidade"] = new_pdt_num
                st.session_state.db.loc[idx, "Descrição"] = new_pdt_desc
                st.success(f"Produto '{new_pdt_name}' atualizado com sucesso!")
        elif st.session_state.btn_adm == "delete_btn":
            st.markdown("### 🗑️ Excluir produto")
            del_prod = st.selectbox(
                "Escolha o produto para excluir",
                prod["Nome"].tolist()
            )
            if st.button("Excluir"):
                idx = prod.index[prod["Nome"] == del_prod][0]
                st.session_state.db = prod.drop(idx).reset_index(drop=True)
                st.success(f"Produto '{del_prod}' excluído com sucesso!")
        else:
            st.info("Selecione uma opção de CRUD acima.")