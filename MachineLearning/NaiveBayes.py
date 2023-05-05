import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

dados_final = pd.read_csv('MachineLearning/dataset/Student_Performance_new.csv')
dados_final

dados_final = dados_final.drop(columns = ['Unnamed: 0'])

dados_final

dados_final['race/ethnicity'] = dados_final['race/ethnicity'].replace({'group A': 'pessoas_brancas','group B':'pessoas_brancas','group C':'pessoas_brancas','group D':'pessoas_pretas','group E':'pessoas_pretas'})

dados_final['parental level of education'] = dados_final['parental level of education'].replace({"associate's degree":'nivel_tecnico',"bachelor's degree":'nivel_bacharel',"high school":"ensino_medio","master's degree":"nivel_mestre","some college":"nivel_tecnologo","some high school":"algum_ensino_medio"})
dados_final

dados_final['lunch'] = dados_final['lunch'].replace({"standard":"almoco_padrao","free/reduced":"almoco_gratis"})
dados_final['test preparation course'] = dados_final['test preparation course'].replace({"none": "sem_teste_preparacao","completed": "teste_preparacao_completo"})

dados_final = dados_final.rename(columns={"race/ethnicity":"raca/etnia", "parental level of education": "nivel_educacao_parental","lunch":"almoco","test preparation course":"curso_preparatorio"})
dados_final = dados_final.rename(columns={"math percentage":"nota_matematica","sex":"sexo"})

dados_final['nota_escrita_leitura'] = dados_final[['reading score percentage','writing score percentage']].mean(axis=1)

dados_final['nota_escrita_leitura'] = dados_final['nota_escrita_leitura'].round(2)

dados_final = dados_final.drop(["reading score percentage","writing score percentage"], axis=1)

dados_final['nota_escrita_leitura'] = dados_final['nota_escrita_leitura'] * 10
dados_final

dados_final['nota_matematica'], dados_final['nota_escrita_leitura'] = dados_final['nota_escrita_leitura'], dados_final['nota_matematica']
dados_final= dados_final.rename(columns = {'nota_matematica' : 'nota_escrita_leitura','nota_escrita_leitura':'nota_matematica'})
dados_final['nota_escrita_leitura'] = dados_final['nota_escrita_leitura'].round()
dados_final['nota_matematica'] = dados_final['nota_matematica'].round(2)
dados_final['nota_matematica'] = (dados_final['nota_matematica'] >=0.7).astype(int)
dados_final = dados_final.drop(columns=['nota_escrita_leitura'])

dados_final

"""#Naive Bayes"""

x_dados = dados_final.iloc[:, 0:5].values
x_dados

y_dados = dados_final.iloc[:, 5].values
y_dados

label_encoder_etnia = LabelEncoder()
label_encoder_educacao_parental = LabelEncoder()
label_encoder_almoco = LabelEncoder()
label_encoder_curso_prep = LabelEncoder()
label_encoder_sexo = LabelEncoder()

x_dados[:,0] = label_encoder_etnia.fit_transform(x_dados[:,0])
x_dados[:,1] = label_encoder_educacao_parental.fit_transform(x_dados[:,1])
x_dados[:,2] = label_encoder_almoco.fit_transform(x_dados[:,2])
x_dados[:,3] = label_encoder_curso_prep.fit_transform(x_dados[:,3])
x_dados[:,4] = label_encoder_sexo.fit_transform(x_dados[:,4])

x_dados

with open('dados.pkl','wb') as f:
  pickle.dump([x_dados,y_dados],f)

naive_dados = GaussianNB()
naive_dados.fit(x_dados, y_dados)

previsao = naive_dados.predict([[0,2,1,0,0],[0,5,1,1,0]])

def resultado(lista):
  return naive_dados.predict([lista])


previsao

naive_dados.classes_

x_dados_treinamento, x_dados_teste, y_dados_treinamento, y_dados_teste = train_test_split(x_dados, y_dados, test_size= 0.25,random_state=0)

x_dados_treinamento.shape

with open('dados_final.pkl','wb') as f:
  pickle.dump([x_dados_treinamento,y_dados_treinamento,x_dados_teste,y_dados_teste],f)

with open('dados_final.pkl', 'rb') as f:
  x_dados_treinamento, y_dados_treinamento, x_dados_teste, y_dados_teste = pickle.load(f)

naive_dados_final = GaussianNB()
naive_dados_final.fit(x_dados_treinamento,y_dados_treinamento)

previsoes_final = naive_dados_final.predict(x_dados_teste)

previsoes_final

accuracy_score(y_dados_teste,previsoes_final)