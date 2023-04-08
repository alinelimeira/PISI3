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
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

dados = pd.read_csv("MachineLearning/dataset/Student_Performance_new.csv")
dados = dados.drop(columns=['Unnamed: 0'])
gender_dict = {'F' : 1,'M' : 0} 
dadosmodificados = dados[['sex']].replace(gender_dict)


dummie_dados = pd.get_dummies(dados.drop(['sex'], axis = 1))
dados_final = pd.concat([dummie_dados] , axis = 1)
dados_final = pd.concat([dadosmodificados, dummie_dados] , axis = 1)


a_renomear = {
      "parental level of education_associate's degree": 'nivel_tecnico',
      "parental level of education_bachelor's degree": 'nivel_bacharel',
      "parental level of education_high school": 'ensino_medio',
      "parental level of education_master's degree": 'nivel_mestre',
      "parental level of education_some college" : 'nivel_tecnologo ',
      "parental level of education_some high school" : 'algum_ensino_medio',
      "test preparation course_completed" : 'teste_preparacao_completo',
      "test preparation course_none" : "sem_teste_preparacao",
      "math percentage" : "math_percentage",
      "reading score percentage": "reading_score_percentage",
      "writing score percentage" : "writing_score_percentage",
      "race/ethnicity_group A" : "race_ethnicity_group_A",
      "race/ethnicity_group B" : "race_ethnicity_group_B",
      "race/ethnicity_group C" : "race_ethnicity_group_C",
      "race/ethnicity_group D": "race_ethnicity_group_D",
      "race/ethnicity_group E": "race_ethnicity_group_E",
      "lunch_free/reduced" : "almoco_gratis",
      "lunch_standard": "almoco_padrao"


}

dados_final = dados_final.rename(columns = a_renomear)
dados_final['nota_escrita_leitura'] = dados_final[['reading_score_percentage','writing_score_percentage']].mean(axis=1)

dados_final['nota_matematica'] = (dados_final['math_percentage'] >= 0.5).astype(int)
dados_final['nota_linguagem'] = (dados_final['nota_escrita_leitura'] >= 0.5).astype(int)
dados_final = dados_final.drop(['math_percentage','nota_escrita_leitura' ,'reading_score_percentage','writing_score_percentage'], axis=1)

dados_final['pessoas_brancas'] = dados_final['race_ethnicity_group_A'] + dados_final['race_ethnicity_group_B'] + dados_final['race_ethnicity_group_C']
dados_final['pessoas_pardas_pretas'] = dados_final['race_ethnicity_group_D'] + dados_final['race_ethnicity_group_E']

dados_final = dados_final.drop(['race_ethnicity_group_A','race_ethnicity_group_B' ,'race_ethnicity_group_C','race_ethnicity_group_D', 'race_ethnicity_group_E'], axis=1)
dados_final['nivel_ensino_medio'] = dados_final['ensino_medio'] + dados_final['algum_ensino_medio']

dados_final = dados_final.drop(['ensino_medio','algum_ensino_medio'], axis=1)

dados = dados_final


##################### SMOTE
dados_final = dados_final.drop(columns=['nota_linguagem'])

X = dados_final.drop('nota_matematica', axis = 1)
y = dados_final['nota_matematica']

smt = SMOTE(random_state=123)  
X, y = smt.fit_resample(X, y)  
dados_final = pd.concat([X, y], axis=1) 


################# LINEAR SVC COM Y = NOTA_MATEMATICA

X= dados_final.drop('nota_matematica', axis = 1) 
y= dados_final['nota_matematica']

norm = StandardScaler()
X_normalizado = norm.fit_transform(X)

SEED = 5
np.random.seed(SEED)
X_treino, X_teste, y_treino, y_teste = train_test_split(X_normalizado, y, test_size = 0.3, random_state = 123)

model = LinearSVC()
model.fit(X_treino,y_treino)
previsoes_linear = model.predict(X_teste)

importances = pd.DataFrame({'feature': X.columns, 'importance': abs(model.coef_[0])})
importances = importances.sort_values(by='importance', ascending=True)


st.subheader('LinearSVC com y = nota_matematica, em relação a nota 5')

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(importances['feature'], importances['importance'])
ax.set_xlabel('Importância')
ax.set_ylabel('Recurso')
ax.set_title('Importância dos recursos com o LinearSVC, target nota_matematica')
plt.grid(True)
st.pyplot(fig)

cm = confusion_matrix (y_teste, previsoes_linear)
st.write("Matriz  de Confusão do LinearSVC em relação a nota 5, target nota_matematica",cm)

st.write("Para o LinearSVC, target nota_matematica:")
report = classification_report(y_teste, previsoes_linear, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)





############################FAZENDO EM RELAÇÃO A NOTA_LINGUAGEM

dados = dados.drop(columns=['nota_matematica'])

X = dados.drop('nota_linguagem', axis = 1)
y = dados['nota_linguagem']

smt = SMOTE(random_state=123)  
X, y = smt.fit_resample(X, y)  
dados = pd.concat([X, y], axis=1)

X= dados.drop('nota_linguagem', axis = 1) #pega todas as colunas menos a nota_linguagem
y= dados['nota_linguagem']

norm = StandardScaler()
X_norm = norm.fit_transform(X)

################## algortimo 
SEED = 5
np.random.seed(SEED)
X_treino, X_teste, y_treino, y_teste = train_test_split(X_norm, y, test_size = 0.3, random_state = 123)

modelo = LinearSVC()
modelo.fit(X_treino,y_treino)
prev_linear = modelo.predict(X_teste)

imptc = pd.DataFrame({'feature': X.columns, 'importance': abs(modelo.coef_[0])})
imptc = imptc.sort_values(by='importance', ascending=True)

st.subheader('LinearSVC com y = nota_linguagem em relação a nota 5')

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(imptc['feature'], imptc['importance'])
ax.set_xlabel('Importância')
ax.set_ylabel('Recurso')
ax.set_title('Importância dos recursos com o LinearSVC, target nota_linguagem')
plt.grid(True)
st.pyplot(fig)


mtx = confusion_matrix (y_teste, prev_linear)
st.write("Matriz  de Confusão do LinearSVC em relação a nota 5, target nota_linguagem",mtx)

st.write("Para o LinearSVC, target nota_linguagem:")
report = classification_report(y_teste, prev_linear, output_dict = True)
df_metrics = pd.DataFrame(report).transpose()
st.table(df_metrics)
