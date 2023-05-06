import streamlit as st
import NaiveBayes

st.title('Formulário')
st.subheader('Entre os dados')

with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter Full name")
    etnia = st.selectbox('Cor de pele', ('Branco', 'Preto'))
    nivel_educacao_pais = st.selectbox('Nivel de educação dos pais', ('bacharel', 'tecnologo','mestre','tecnico', 'ensino médio', 'ensino médio inconpleto'))
    almoco = st.selectbox('almoço', ('padrão', 'gratis'))
    curso_prep = st.selectbox('curso preparatório', ('sem curso', 'curso completo'))
    sexo = st.selectbox('sexo', ('F', 'M'))

    submit = st.form_submit_button('submit')

    if submit:
        dicionario = {
            'Branco': 0,
            'Preto': 1,
            'bacharel': 2,
            'tecnologo': 5,
            'mestre': 3,
            'tecnico': 4,
            'ensino médio': 1,
            'ensino médio inconpleto': 0,
            'padrão': 1,
            'gratis': 0,
            'sem curso': 0,
            'curso completo': 1,
            'F': 1,
            'M': 0
        }

        lista = []
        lista.append(dicionario[etnia])
        lista.append(dicionario[nivel_educacao_pais])
        lista.append(dicionario[almoco])
        lista.append(dicionario[curso_prep])
        lista.append(dicionario[sexo])

        resultado = NaiveBayes.resultado(lista)
        if resultado == 0:
            st.write(f"{name} tem uma chance maior de não passar")
        elif resultado == 1:
            st.write(f'{name} tem Boa chance de passar')
        
