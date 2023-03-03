import streamlit as st
import pandas as pd
import seaborn as seaborn
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm



#informacoes no head da pagina
st.set_page_config(page_title='Analise de dados', page_icon=':bar_chart')
st.title("Análise de dados")
st.subheader("Esta página tem como objetivo mostrar a analise dos dados do dataset Students Performance in Exams")

#SIDEBAR 
classifier_name = st.sidebar.selectbox("Selecione um classificador", ("Árvore de decisão", "Bernoulli","KNN"))


dados = pd.read_csv("../MachineLearning/dataset/Student_Performance_new.csv")


st.dataframe(dados)  # comando q aparece toda a tabela

st.markdown(" <p style = 'font-size: 20px' >Tipos das colunas: </p> ", unsafe_allow_html=True)
st.table(dados.dtypes)

st.markdown("<p style = 'font-size: 20px' > Verificando se há valores nulos: </p> ", unsafe_allow_html=True)
st.table(dados.isnull().sum())

st.markdown("<p style = 'font-size: 20px' > Verificando se há valores repetidos: </p> ", unsafe_allow_html=True)
duplicatas =  dados.duplicated()
num_duplicatas = duplicatas.sum()
st.table(pd.DataFrame([num_duplicatas]))

##tabela mulher x homem
st.write("<p  style = 'font-size: 20px'> Analisando a quantidade de mulheres e homens: </p> ", unsafe_allow_html=True)
counts = dados['sex'].value_counts()
colors = ['#D2103C', '#00ACEE']

plt.xlabel('Sexo')
plt.ylabel('Quantidade')

plt.bar(counts.index, counts.values, color = colors, width = 0.7)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()



##grafico com as etnias 

counts = dados['race/ethnicity'].value_counts(normalize=True)

fig, ax = plt.subplots(figsize =(5,5))
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
plt.title("Porcentagem de cada raça/etnia")
plt.legend(counts.index, bbox_to_anchor = (1, 1))
st.pyplot(fig)



st.markdown("<p  style = 'font-size: 20px'> Cada grupo de etnia é separado da seguinte forma:</p> ", unsafe_allow_html=True)
st.markdown("Group A: White - British") 
st.markdown("Group B: White - Irish") 
st.markdown("Group C: White - White - Any other white background") 
st.markdown("Group D: Mixed - White and Black Caribbean") 
st.markdown("Group E: Mixed - White and Black African ") 



## nivel de educacao dos pais

st.markdown("<p  style = 'font-size: 20px'> Nível de educação dos pais:</p> ", unsafe_allow_html=True)
plt.title("Nivel de education dos pais")
counts = dados ['parental level of education']. value_counts()
colors = ['#9e4a49', '#9e4a49', '#9e4a49', '#9e4a49', '#9e4a49', '#9e4a49']


fig, ax = plt.subplots(figsize =(12,7),layout='constrained')
plt.xlabel("Nivel de educação dos pais")
plt.ylabel("Quantidade")
plt.bar(counts.index, counts.values, color=colors[:len(counts.index)])


plt.legend()
st.pyplot(fig)
