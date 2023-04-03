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

X = dados.drop('nota_linguagem', axis = 1)
y = dados['nota_linguagem']
smote = SMOTE(random_state=123)  # Instancia um objeto da classe SMOTE
X, y = smote.fit_resample(X, y)
dados = pd.concat([X,y], axis = 1)


norm = StandardScaler() 
X_normalizado = norm.fit_transform(X)


st.title('Analisando as variáveis tendo como target a nota_linguagem')

### Arvore de decisao com target nota_linguagem
X_treino, X_teste, y_treino, y_teste = train_test_split(X_normalizado, y, test_size = 0.3, random_state = 123)
dtc = DecisionTreeClassifier(criterion = 'entropy', random_state = 42) #usando a entropia, seleciona o dado mais ordenado
dtc.fit(X_treino, y_treino)
pred_arvore = dtc.predict(X_teste)

st.subheader("Feature Importance de acordo com a Árvore de decisão")
importances = dtc.feature_importances_
feature_importances = pd.DataFrame({"feature": X.columns, "importance": importances})
feature_importances = feature_importances.sort_values("importance", ascending=True)
fig, ax = plt.subplots(figsize=(10, 6))
plt.barh(feature_importances["feature"], feature_importances["importance"], height= 0.6)
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importances")
plt.grid(True)
st.pyplot(fig)
st.set_option('deprecation.showPyplotGlobalUse', False)

mt = confusion_matrix(y_teste, pred_arvore)
st.write("Matriz de Confusão da Árvore de Decisão",mt)

st.write("Para a Árvore de Decisão com a nota_matematica:")
report = classification_report(y_teste, pred_arvore, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)


#### ANALISE SEM NOTA_MATEMATICA

dataf= dados
dataf = dados.drop(columns=['nota_matematica'])

X_sem_nota_mat = dataf.drop('nota_linguagem', axis = 1)
y_sem_nota_mat = dataf['nota_linguagem']

smt = SMOTE(random_state=123)  # Instancia um objeto da classe SMOTE
X_sem_nota_mat, y_sem_nota_mat = smt.fit_resample(X_sem_nota_mat, y_sem_nota_mat)
dataf = pd.concat([X_sem_nota_mat,y_sem_nota_mat], axis = 1)


X_sem_nota_mat = dataf.drop('nota_linguagem', axis = 1)
y_sem_nota_mat = dataf['nota_linguagem']
normalizado = StandardScaler() 
X_norm = normalizado.fit_transform(X_sem_nota_mat)

### ARVORE DE DECISAO REMOVENDO NOTA_MATEMATICA

X_trn, X_tst, y_trn, y_tst = train_test_split(X_norm,y_sem_nota_mat, test_size = 0.3, random_state = 123)
clt = DecisionTreeClassifier(criterion = 'entropy', random_state = 42)
clt.fit(X_trn,y_trn)
predic_arv= clt.predict(X_tst)

st.write("Feature Importance de acordo com a Árvore de decisão")
importances = clt.feature_importances_
feature_importances = pd.DataFrame({"feature": X_sem_nota_mat.columns, "importance": importances})
feature_importances = feature_importances.sort_values("importance", ascending=True)
fig, ax = plt.subplots(figsize=(10, 6))
plt.barh(feature_importances["feature"], feature_importances["importance"], height= 0.6)
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importances")
plt.grid(True)
st.pyplot(fig)

mtx = confusion_matrix (y_tst, predic_arv)
st.write("Matriz de confusão da Árvore de Decisão sem a nota_matematica", mtx)

st.write("Métricas da Árvore de Decisão sem a nota_matematica:")
report = classification_report(y_tst, predic_arv, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)



#######LINEARSVC

st.subheader("Utilizando o LinearSVC:")

norm = StandardScaler() 
X_normalizado = norm.fit_transform(X_sem_nota_mat)


SEED = 5
np.random.seed(SEED)
treino_x, teste_x, treino_y, teste_y = train_test_split (X_sem_nota_mat,y_sem_nota_mat, random_state = SEED, test_size = 0.30,stratify = y_sem_nota_mat)

model = LinearSVC()
model.fit(treino_x, treino_y)
prev_linear = model.predict(teste_x)

cm = confusion_matrix (teste_y, prev_linear)
st.write("Matriz de confusão do LinearSVC", cm)

st.write("Métricas do LinearSVC:")
report = classification_report(teste_y, prev_linear, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)

importances = pd.DataFrame({'feature': X_sem_nota_mat.columns, 'importance': abs(model.coef_[0])})
importances = importances.sort_values(by='importance', ascending=True)

# Plota o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(importances['feature'], importances['importance'])
ax.set_xlabel('Importância')
ax.set_ylabel('Recurso')
ax.set_title('Importância dos recursos com o LinearSVC')
plt.grid(True)
st.pyplot(fig)





#### XGBoost sem a nota_matematica
st.subheader("Utilizando o XGBoost sem a nota_matematica:")

nrml = StandardScaler() 
X_nrml = nrml.fit_transform(X_sem_nota_mat)

X_train, X_test, y_train, y_test = train_test_split(X_nrml, y_sem_nota_mat, test_size = 0.3, random_state = 1121218)
xgb_clf = xgb.XGBClassifier()

xgb_clf.fit(X_train,y_train)
pred_xgb = xgb_clf.predict(X_test)

#Matriz de confusao 
matriz_conf = confusion_matrix(y_test, pred_xgb)
st.write("Matriz de confusão do XGBoost", matriz_conf)

st.write("Métricas do XGBoost")
report = classification_report(y_test, pred_xgb, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)
