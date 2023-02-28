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


dados = pd.read_csv("MachineLearning/dataset/Student_Performance_new.csv")


st.dataframe(dados)  # comando q aparece toda a tabela

st.write("Tipos das colunas: ")
st.table(dados.dtypes)

st.write("Verificando se há valores nulos: ")
st.table(dados.isnull().sum())

##tabela mulher x homem
plt.title("Analisando a quantidade de mulheres e homens: ")
counts = dados['sex'].value_counts()
colors = ['#D2103C', '#00ACEE']

plt.xlabel('Sexo')
plt.ylabel('Quantidade')

plt.bar(counts.index, counts.values, color = colors, width = 0.6)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()



##grafico com as etnias 

counts = dados['race/ethnicity'].value_counts(normalize=True)

fig, ax = plt.subplots(figsize =(5,5))
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
plt.title("Porcentagem de cada raça/etnia")
plt.legend(counts.index, bbox_to_anchor = (1, 1))
st.pyplot(fig)


## nivel de educacao dos pais
plt.title("Nivel de education dos pais")
counts = dados ['parental level of education']. value_counts()
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']


fig, ax = plt.subplots(figsize =(12,7),layout='constrained')
plt.xlabel("Nivel de educação dos pais")
plt.ylabel("Quantidade")
plt.bar(counts.index, counts.values, color=colors[:len(counts.index)])


plt.legend()
st.pyplot(fig)
