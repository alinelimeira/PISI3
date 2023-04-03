import streamlit as st
import seaborn as sns 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
import estudo_dos_dados


dados = estudo_dos_dados.dados


st.markdown ("<p style = 'font-size: 20px'> Iniciando a análise com os algoritmos </p>", unsafe_allow_html=True)
st.write("Variável nota_matematica como target")
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
feature_importances = feature_importances.sort_values("importance", ascending=True)
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
st.write("Matriz de confusão da Árvore de Decisão", matrix)

st.subheader("Para a Árvore de Decisão:")
report = classification_report(y_teste, predito_ArvoreDecisao, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)


###DUMMY CLASSIFIER
SEED = 5
np.random.seed(SEED)
X_treino, X_teste, y_treino, y_teste = train_test_split (X,y,random_state = SEED, test_size = 0.30,stratify = y)

dummy_stratified = DummyClassifier()
dummy_stratified.fit(X_treino, y_treino)
acuracia_dummy = dummy_stratified.score(X_treino, y_treino) * 100

st.markdown(f'  O classificador Dummy resultou numa acurácia de: {acuracia_dummy:.0f}% ', unsafe_allow_html=True)

st.markdown("<p style = 'font-size: 20px'> Após fazer o algoritmo, a variável nota_linguagem mostrou grande importância em relação as outras variáveis. Com isso a variável nota_linguagem foi eliminada e o algoritmo foi refeito. </p>", unsafe_allow_html=True)



#### FAZENDO O SMOTE

df = dados
df = dados.drop(columns=['nota_linguagem'])


X_sem_nota_linguagem = df.drop('nota_matematica', axis=1)
y_sem_nota_linguagem = df['nota_matematica']

smt = SMOTE(random_state=123)  # Instancia um objeto da classe SMOTE
X_sem_nota_linguagem, y_sem_nota_linguagem = smt.fit_resample(X_sem_nota_linguagem, y_sem_nota_linguagem)
df = pd.concat([X_sem_nota_linguagem,y_sem_nota_linguagem], axis = 1)


##### ARVORE DE DECISAO SEM NOTA

X_sem_nota_linguagem = df.drop('nota_matematica', axis = 1)
y_sem_nota_linguagem = df['nota_matematica']



norm = StandardScaler() 
X_normalizado = norm.fit_transform(X_sem_nota_linguagem)

X_treino, X_teste, y_treino, y_teste = train_test_split(X_sem_nota_linguagem, y_sem_nota_linguagem, test_size = 0.3, random_state = 123)
clf = DecisionTreeClassifier(criterion = 'entropy', random_state = 42) #usando a entropia, seleciona o dado mais ordenado
clf.fit(X_treino, y_treino)
prediction_ArvoreDecisao = clf.predict(X_teste)

### calculando o grau de importancia por meio da decision tree sem nota_linguagem e gráfico

importances = clf.feature_importances_
feature_importances = pd.DataFrame({"feature": X_sem_nota_linguagem.columns, "importance": importances})
feature_importances = feature_importances.sort_values("importance", ascending=True)
#st.dataframe(feature_importances)

plt.figure(figsize=(10, 8))
plt.barh(feature_importances["feature"], feature_importances["importance"], height= 0.6)
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importances com a Árvore de Decisão")
plt.grid(True)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)



####### FAZENDO MATRIZ DE  CONFUSÃO E METRICAS DA ARVORE SEM A NOTA_LINGUAGEM####

matriz = confusion_matrix (y_teste, prediction_ArvoreDecisao)
st.write("Matriz de confusão da Árvore de Decisão sem a nota_linguagem", matriz)
st.write("Para a Árvore de Decisão sem a nota_linguagem:")
report = classification_report(y_teste, prediction_ArvoreDecisao, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)



####DUMMMY CLASSIFIER
SEED = 5
np.random.seed(SEED)
X_treino, X_teste, y_treino, y_teste = train_test_split (X_sem_nota_linguagem,y_sem_nota_linguagem,random_state = SEED, test_size = 0.30,stratify = y_sem_nota_linguagem)

dummy_stratified = DummyClassifier()
dummy_stratified.fit(X_treino, y_treino)
acuracia_dummy = dummy_stratified.score(X_treino, y_treino) * 100

st.markdown(f' O classificador Dummy resultou numa acurácia de: {acuracia_dummy:.0f}% ', unsafe_allow_html=True)



####################### LINEAR SVC ######################
st.subheader("Como na Árvore a precisão e a acurácia deu valores baixos, foi necessário analisar com outros algoritmos:")
st.subheader("Utilizando o LinearSVC:")

norm = StandardScaler() 
X_normalizado = norm.fit_transform(X_sem_nota_linguagem)


SEED = 5
np.random.seed(SEED)
treino_x, teste_x, treino_y, teste_y = train_test_split (X_sem_nota_linguagem,y_sem_nota_linguagem, random_state = SEED, test_size = 0.30,stratify = y_sem_nota_linguagem)

model = LinearSVC()
model.fit(treino_x, treino_y)
previsoes = model.predict(teste_x)

###### feature importance da linearsvc
importances = pd.DataFrame({'feature': X_sem_nota_linguagem.columns, 'importance': abs(model.coef_[0])})
importances = importances.sort_values(by='importance', ascending=True)

# Plota o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(importances['feature'], importances['importance'])
ax.set_xlabel('Importância')
ax.set_ylabel('Recurso')
ax.set_title('Importância dos recursos com o LinearSVC')
plt.grid(True)
st.pyplot(fig)

cm = confusion_matrix (teste_y, previsoes)
st.write("Matriz de confusão do LinearSVC", cm)

st.write("Métricas do LinearSVC:")
report = classification_report(teste_y, previsoes, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)



#### XGBOOST SEM A NOTA_LINGUAGEM 
norm = StandardScaler() 
X_normalizado = norm.fit_transform(X_sem_nota_linguagem)

X_train, X_test, y_train, y_test = train_test_split(X_normalizado, y_sem_nota_linguagem, test_size = 0.3, random_state = 1121218)
xgb_cl = xgb.XGBClassifier()

xgb_cl.fit(X_train,y_train)
preds = xgb_cl.predict(X_test)

st.subheader("Para o algoritmo XGBoost sem a nota_linguagem:")



#Matriz de confusao 
matriz_conf = confusion_matrix(y_test, preds)
st.write("Matriz de confusão do XGBoost:", matriz_conf)

st.write("Métricas do XGBoost:")
report = classification_report(y_test, preds, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)