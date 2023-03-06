import streamlit as st
import pandas as pd
import seaborn as sns
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

# ! mudar o diretorio quando for testar para cloud para  "MachineLearning/dataset/Student_Performance_new.csv"
dados = pd.read_csv("../MachineLearning/dataset/Student_Performance_new.csv")
dados = dados.drop(columns=['Unnamed: 0'])

st.dataframe(dados)  # comando q aparece toda a tabela

st.markdown(" <p style = 'font-size: 20px' >Tipos das colunas: </p> ", unsafe_allow_html=True)
st.table(dados.dtypes)

st.markdown("<p style = 'font-size: 20px' > Verificando se há valores nulos: </p> ", unsafe_allow_html=True)
st.table(dados.isnull().sum())

st.markdown("<p style = 'font-size: 20px' > Verificando se há valores repetidos: </p> ", unsafe_allow_html=True)
duplicatas =  dados.duplicated()
num_duplicatas = duplicatas.sum()
st.table(pd.DataFrame([num_duplicatas]))


### titulo
st.title("Analisando gráficos com apenas uma variável")


##tabela mulher x homem
st.write("<p  style = 'font-size: 20px'> Quantidade de mulheres e homens: </p> ", unsafe_allow_html=True)
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
plt.title("Porcentagem de cada raça/etnia", fontsize = 12)
plt.legend(counts.index, bbox_to_anchor = (1, 1))
st.pyplot(fig)



st.markdown("<p  style = 'font-size: 20px'> Cada grupo de etnia é separado da seguinte forma:</p> ", unsafe_allow_html=True)
st.markdown("Group A: White - British") 
st.markdown("Group B: White - Irish") 
st.markdown("Group C: White - White - Any other white background") 
st.markdown("Group D: Mixed - White and Black Caribbean") 
st.markdown("Group E: Mixed - White and Black African ") 



#Nivel de educacao dos pais

st.markdown("<p style = 'font-size: 20px' > Verificando a quantidade do nivel educacional dos pais dos estudantes: </p> ", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10,6))
sns.countplot(x = "parental level of education", data = dados, ax = ax)
plt.title("Relação quantidade e nivel de educação dos pais", fontsize = 14)
ax.set_xlabel("Educação")
ax.set_ylabel("Quantidade")
st.pyplot(fig)


# Tipo de almoco

counts = dados['lunch'].value_counts(normalize=True)

fig, ax = plt.subplots(figsize =(5,5))
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
plt.title("Porcentagem do tipo de almoço dos estudantes", fontsize = 12)
plt.legend(counts.index, bbox_to_anchor = (1, 1))
st.pyplot(fig)

# teste de preparacao

# boxplot matematica

fig, ax = plt.subplots(figsize=(9,5))
sns.boxplot( x= dados["math percentage"], color = "lightblue", ax = ax)
plt.title("Distribuição da nota de matemática", fontsize=18)
st.pyplot(fig)

#nota leitura
fig, ax = plt.subplots(figsize=(9,5))
sns.boxplot( x= dados["reading score percentage"], color = "lightblue", ax = ax)
plt.title("Distribuição da nota de leitura", fontsize=18)
st.pyplot(fig)

#nota escrita
fig, ax = plt.subplots(figsize=(9,5))
sns.boxplot( x= dados["writing score percentage"], color = "lightblue", ax = ax)
plt.title("Distribuição da nota de escrita", fontsize=18)
st.pyplot(fig)

##ANALISES COM DUAS VARIÁVEIS


st.title("Analisando os dados com gráficos de duas variáveis")


##### Matriz de confusao dos dados numericos

fig, ax = plt.subplots(figsize=(16,9))
sns.heatmap(dados.corr(),annot=True, square=True, ax=ax)
plt.title("Matriz de confusão para as notas", fontsize=20, fontstyle="oblique")
st.pyplot(fig)


