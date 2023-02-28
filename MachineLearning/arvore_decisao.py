import streamlit as st
import seaborn as sns 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import estudo_dos_dados

dados = estudo_dos_dados.dados


st.title ("Algoritmo Árvore de Decisão")
st.write("Analisando a variável math_percentage_class ")
fig, ax = plt.subplots()
ax = sns.countplot(x = 'math_percentage_class', data = dados)
ax.figure.set_size_inches(12, 10)
st.pyplot(fig)


st.markdown("<p style = 'font-size: 20px'> As colunas 0 e 1 no gráfico mostram que os dados da variável math_percentage_class não está balanceada em relação ao resto das variáveis.</p>", unsafe_allow_html=True)
st.markdown("<p style = 'font-size: 20px'>Com isso é necessário fazer o SMOTE:</p>", unsafe_allow_html=True)

#fazendo o SMOTE

X = dados.drop('math_percentage_class', axis = 1)
y = dados['math_percentage_class']

smt = SMOTE(random_state=123)  # Instancia um objeto da classe SMOTE
X, y = smt.fit_resample(X, y)
dados = pd.concat([X,y], axis = 1)

fig, ax = plt.subplots()
ax = sns.countplot(x='math_percentage_class', data=dados)
st.pyplot(fig)

st.markdown ('''

## Após fazer o oversampling, tem inicio o Algoritmo Árvore de decisão
''', unsafe_allow_html=True)

########### FAZENDO A ARVORE DE DECISAO #################################

X = dados.drop('math_percentage_class', axis = 1)
y = dados['math_percentage_class']

norm = StandardScaler() 
X_normalizado = norm.fit_transform(X)

X_treino, X_teste, y_treino, y_teste = train_test_split(X_normalizado, y, test_size = 0.3, random_state = 123)




dtc = DecisionTreeClassifier(criterion = 'entropy', random_state = 42) #usando a entropia, seleciona o dado mais ordenado
dtc.fit(X_treino, y_treino)
predito_ArvoreDecisao = dtc.predict(X_teste)

#calculando o grau de importancia por meio da decision tree e gráfico

importances = dtc.feature_importances_
indices = np.argsort(importances) [::1]

plt.bar(range(X_treino.shape[1]), importances[indices])
plt.xticks(range(X_treino.shape[1]), dados.columns[1:][indices], rotation = 90)
plt.xlim([-1, X_treino.shape[1]])
plt.ylim([0, 0.6])

plt.tight_layout()
plt.title("Grau de importância das features pela Árvore de decisão")

# Exibindo gráfico no Streamlit
st.pyplot()


####### FAZENDO MATRIZ DE  CONFUSÃO ####

matrix = confusion_matrix (y_teste, predito_ArvoreDecisao)
plt.figure(figsize=(8,4))
sns.heatmap(matrix, annot=True, fmt="d", cbar=False, cmap="Blues")
plt.title("Matriz de Confusão")

st.pyplot()


################## FAZENDO  PRECISÃO #########

precisao = precision_score(y_teste, predito_ArvoreDecisao) * 100

############## Fazendo acurácia 

acuracia = accuracy_score(y_teste, predito_ArvoreDecisao)*100

st.markdown(f' ## Tendo uma precisão de {precisao:.0f}% e acurácia de {acuracia:.0f}%', unsafe_allow_html=True)



SEED = 5
np.random.seed(SEED)
X_treino, X_teste, y_treino, y_teste = train_test_split (X,y,random_state = SEED, test_size = 0.30,stratify = y)

dummy_stratified = DummyClassifier()
dummy_stratified.fit(X_treino, y_treino)
acuracia_dummy = dummy_stratified.score(X_treino, y_treino) * 100

st.markdown(f' ## O classificador Dummy resultou numa acurácia de: {acuracia_dummy:.0f}% ', unsafe_allow_html=True)
