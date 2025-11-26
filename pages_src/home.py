import streamlit as st

class HomePage:                                    # Home page
    def render(self):
        st.title("Home")

        # Campo de busca
        busca = st.text_input("Buscar produtos...", "")

        st.divider()
        st.subheader("Categories")
        categories = ["Type1", "Type2", "Type3", "Type4"]
        st.write(" | ".join(categories))

        st.divider()
        st.subheader("Produtos")

        df = st.session_state.db
        
        try:
        # Se quiser filtrar pela busca:
            if busca:
                df = df[df["Nome"].str.contains(busca, case=False, na=False)]
        # Listar produtos
            for i, row in df.iterrows():
                st.write(f"- **{row['Nome']}** | R$ {row['Preço']:.2f} | Qtd: {row['Quantidade']}")
                st.write(f"Descrição: {row['Descrição']}")

        except:
            st.warning('Algo deu errado, talvez algum caracter errado foi inserido.')