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


st.markdown ("<p style = 'font-size: 20px'> Iniciando o algoritmo Árvore de Decisão </p>", unsafe_allow_html=True)
st.write("Analisando a variável nota_matematica ")
fig, ax = plt.subplots()
ax = sns.countplot(x = 'nota_matematica', data = dados)
#ax.figure.set_size_inches(12, 10)
plt.figure(figsize=(10, 8))
st.pyplot(fig)


st.markdown("<p style = 'font-size: 20px'> As colunas 0 e 1 no gráfico mostram que os dados da variável nota_matematica não está balanceada em relação ao resto das variáveis.</p>", unsafe_allow_html=True)
st.markdown("<p style = 'font-size: 20px'>Com isso é necessário fazer o SMOTE:</p>", unsafe_allow_html=True)

#fazendo o SMOTE

X = dados.drop('nota_matematica', axis = 1)
y = dados['nota_matematica']

smt = SMOTE(random_state=123)  # Instancia um objeto da classe SMOTE
X, y = smt.fit_resample(X, y)
dados = pd.concat([X,y], axis = 1)

fig, ax = plt.subplots()
ax = sns.countplot(x='nota_matematica', data=dados)
plt.figure(figsize=(10, 8))
st.pyplot(fig)

st.markdown ("<p style = 'font-size: 20px'>Após fazer o oversampling, tem inicio o Algoritmo Árvore de decisão: </p>", unsafe_allow_html=True)

########### FAZENDO A ARVORE DE DECISAO #################################

X = dados.drop('nota_matematica', axis = 1)
y = dados['nota_matematica']

norm = StandardScaler() 
X_normalizado = norm.fit_transform(X)

X_treino, X_teste, y_treino, y_teste = train_test_split(X_normalizado, y, test_size = 0.3, random_state = 123)




dtc = DecisionTreeClassifier(criterion = 'entropy', random_state = 42) #usando a entropia, seleciona o dado mais ordenado
dtc.fit(X_treino, y_treino)
predito_ArvoreDecisao = dtc.predict(X_teste)


### calculando o grau de importancia por meio da decision tree e gráfico

importances = dtc.feature_importances_
feature_importances = pd.DataFrame({"feature": X.columns, "importance": importances})
feature_importances = feature_importances.sort_values("importance", ascending=False)
#st.dataframe(feature_importances)

plt.figure(figsize=(10, 8))
plt.barh(feature_importances["feature"], feature_importances["importance"], height= 0.6)
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importances")
plt.grid(True)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
####### FAZENDO MATRIZ DE  CONFUSÃO ####

matrix = confusion_matrix (y_teste, predito_ArvoreDecisao)
plt.figure(figsize=(8,4))
sns.heatmap(matrix, annot=True, fmt="d", cbar=False, cmap="Blues")
plt.title("Matriz de Confusão")

st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

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
