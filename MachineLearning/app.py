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
st.subheader("Esta página tem como objetivo mostrar a análise dos dados do dataset Students Performance in Exams")

st.markdown("<span style='font-size:22px;font-weight:bold'>Dicionário</span>", unsafe_allow_html=True)

st.markdown("<p  style = 'font-size: 20px'>Nível de educação dos pais:</p> ", unsafe_allow_html=True)
st.markdown("Master, Some College, Associate, High School, Some High School") 

st.markdown("<p  style = 'font-size: 20px'>Gênero:</p> ", unsafe_allow_html=True)
st.markdown("M: Masculino")
st.markdown("F: Feminino")

st.markdown("<p  style = 'font-size: 20px'>Notas das Disciplinas:</p> ", unsafe_allow_html=True)
st.markdown("Math percentage : nota Matemática")
st.markdown("Reading score percentage: nota Leitura")
st.markdown("Writing score percentage: nota Escrita")

st.markdown("<p  style = 'font-size: 20px'>Tipo de almoço:</p> ", unsafe_allow_html=True)
st.markdown("Standard: Padrão")
st.markdown("Free/reduced: Gratuito/reduzido")


st.markdown("<p  style = 'font-size: 20px'> Cada grupo de etnia é separado da seguinte forma:</p> ", unsafe_allow_html=True)
st.markdown("Group A: White - British") 
st.markdown("Group B: White - Irish") 
st.markdown("Group C: White - White - Any other white background") 
st.markdown("Group D: Mixed - White and Black Caribbean") 
st.markdown("Group E: Mixed - White and Black African ") 


#SIDEBAR 


# ! mudar o diretorio quando for testar para cloud para  "MachineLearning/dataset/Student_Performance_new.csv" ou ../MachineLearning/dataset/Student_Performance_new.csv
dados = pd.read_csv("MachineLearning/dataset/Student_Performance_new.csv")
dados = dados.drop(columns=['Unnamed: 0'])

dados['nota_matematica'] = (dados['math percentage'] >= 0.5).astype(int)
dados['nota_linguagem'] = dados[['reading score percentage','writing score percentage']].mean(axis=1)
dados['nota_linguagem'] = (dados['nota_linguagem'] >= 0.5).astype(int)


st.markdown(" <p style = 'font-size: 20px' >Dataset: </p> ", unsafe_allow_html=True)
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


##### Matriz de correlacao dos dados numericos
palette = sns.diverging_palette(250, 15, s=75, l=40, n=9, center='light', as_cmap=True)
fig, ax = plt.subplots()
sns.heatmap(dados.corr(), cmap=palette, center=0, annot=True, ax=ax)
ax.set_title('Heatmap de Correlação')
st.pyplot(fig)


### nota de matematica por genero 

st.markdown("<p  style = 'font-size: 20px'> Para relação nota x gênero:</p> ", unsafe_allow_html=True)

### nota de matematica por genero 
fig, ax = plt.subplots(figsize=(10,6))
colors = ['#D2103C', '#00ACEE']
sns.boxplot(x=dados["sex"], y= dados["math percentage"], palette = colors)
plt.title("Distribuição da nota de matemática por gênero", fontsize=18)
st.pyplot(fig)

#### nota leitura por genero 
fig, ax = plt.subplots(figsize=(10,6))
colors = ['#D2103C', '#00ACEE']
sns.boxplot(x=dados["sex"], y= dados["reading score percentage"], palette = colors)
plt.title("Distribuição da nota de leitura por gênero", fontsize=18)
st.pyplot(fig)


#### nota escrita por genero 
fig, ax = plt.subplots(figsize=(10,6))
colors = ['#D2103C', '#00ACEE']
sns.boxplot(x=dados["sex"], y= dados["writing score percentage"], palette = colors)
plt.title("Distribuição da nota de escrita por gênero", fontsize=18)
st.pyplot(fig)



st.markdown("<p  style = 'font-size: 20px'> Para relação nota x etnia:</p> ", unsafe_allow_html=True)


##### nota matematica x etnia 

sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
plt.title("Distribuição das notas de matemática por Raça/Etnia", fontsize=16)
sns.boxplot(data=dados, x="race/ethnicity", y="math percentage", color = (1,1,1,0))
plt.xlabel("Raça/Etnia", fontsize=14)
plt.ylabel("Nota de Matemática", fontsize=14)
st.pyplot()



sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
plt.title("Distribuição das notas de matemática por nível de educação dos pais", fontsize=16)
sns.boxplot(data=dados, x="parental level of education", y="math percentage", color = (0,1,1,1))
plt.xlabel("Nível de Educação dos Pais", fontsize=14)
plt.ylabel("Nota de Matemática", fontsize=14)
st.pyplot()

##Nota por tipo de almoco

fig, ax=plt.subplots(ncols=3,figsize=(22,10))
fig.suptitle('Distribuição das notas baseada no tipo do almoço',size=25)
a=sns.histplot(dados,x='math percentage',ax=ax[0], hue='lunch',element='step')
b=sns.histplot(dados,x='reading score percentage',ax=ax[1],hue='lunch',element='step')
c=sns.histplot(dados,x='writing score percentage',ax=ax[2],hue='lunch',element='step')
sns.move_legend(a, "upper left", bbox_to_anchor=(0, 1))
sns.move_legend(b, "upper left", bbox_to_anchor=(0, 1))
sns.move_legend(c, "upper left", bbox_to_anchor=(0, 1))
st.pyplot(fig)


#Nota x etnia

fig,ax=plt.subplots(ncols=3, figsize=(30,10))
fig.suptitle('Distribuição das notas em relação as Etnias',size=30)
a=sns.kdeplot(data=dados,x='math percentage',ax=ax[0], hue='race/ethnicity')
b= sns.kdeplot(data=dados, x='reading score percentage', ax=ax[1], hue='race/ethnicity')
c= sns.kdeplot(data=dados, x='writing score percentage', ax=ax[2], hue='race/ethnicity')
sns.move_legend(a, "upper left", bbox_to_anchor=(0, 1))
sns.move_legend(b, "upper left", bbox_to_anchor=(0, 1))
sns.move_legend(c, "upper left", bbox_to_anchor=(0, 1))
st.pyplot(fig)


#quantidade de quem tirou >= 5 ou >5 em matematica 

counts = dados['nota_matematica'].value_counts()
colors = ['#4688e3', '#d44242']
labels = [' Maior ou igual a 5', 'Menor que 5']
fig, ax = plt.subplots(figsize =(10,6))
plt.pie(counts, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Porcentagem de alunos que tiraram notas maiores ou iguais 5 ou menores 5 em Matemática', fontsize=12)
plt.legend(title='Notas',loc='upper right' )
st.pyplot(fig)



#quantidade de quem tirou >= 5 ou >5 em nota_linguagem
st.markdown("Para calcular a nota de Linguagem, calculou-se a médias das notas de Leitura e Escrita") 

counts = dados['nota_linguagem'].value_counts()
colors = ['#4688e3', '#d44242']
labels = [' Maior ou igual a 5', 'Menor que 5']
fig, ax = plt.subplots(figsize =(10,6))
plt.pie(counts, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Porcentagem de alunos que tiraram notas maiores ou iguais a 5 ou menores que 5 em Linguagem', fontsize=12)
plt.legend(title='Notas',loc='upper right' )
st.pyplot(fig)



###pairplot das notas
st.write('Gráfico Pairplot das variáveis notas')
colors = ['#D2103C', '#00ACEE']
columns = ["math percentage", "writing score percentage", "reading score percentage", "sex"]
fig = sns.pairplot(data=dados[columns], hue = "sex", palette = colors )
st.pyplot(fig)
