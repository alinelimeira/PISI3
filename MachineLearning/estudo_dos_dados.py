import pandas as pd
import numpy as np
import seaborn as seaborn
import streamlit as st


dados = pd.read_csv("MachineLearning/dataset/Student_Performance_new.csv")
st.dataframe(dados)


shape = dados.shape
dados_info = dados.info()




#Excluindo a coluna sem nome Unnamed 0

dados = dados.drop(columns=['Unnamed: 0'])
topo = dados.head()





#transformando o genero em variavel categorica

gender_dict = {'F' : 1,'M' : 0} 
dadosmodificados = dados[['sex']].replace(gender_dict)
dadosmodificados.head()


#transformando as colunas seguintes em variavel categorica por meio do get_dummies

dummie_dados = pd.get_dummies(dados.drop(['sex'], axis = 1))
dados_final = pd.concat([dummie_dados] , axis = 1)
dados_final.head()

dados_final = pd.concat([dadosmodificados, dummie_dados] , axis = 1)
dados_final.head()
topo1 = dados_final.head()

#renomeando as colunas antigas e as novas 

a_renomear = {
    "parental level of education_associate's degree": 'level_associado',
    "parental level of education_bachelor's degree": 'level_bacharel',
    "parental level of education_high school": 'level_high_school',
    "parental level of education_master's degree": 'level_master',
    "parental level of education_some college" : 'level_some_college ',
    "parental level of education_some high school" : 'level_some_high_school',
    "test preparation course_completed" : 'teste_preparation_course_completed',
    "test preparation course_none" : "test_preparation_course_none",
    "math percentage" : "math_percentage",
    "reading score percentage": "reading_score_percentage",
    "writing score percentage" : "writing_score_percentage",
    "race/ethnicity_group A" : "race_ethnicity_group_A",
    "race/ethnicity_group B" : "race_ethnicity_group_B",
    "race/ethnicity_group C" : "race_ethnicity_group_C",
    "race/ethnicity_group D": "race_ethnicity_group_D",
    "race/ethnicity_group E": "race_ethnicity_group_E",
    "lunch_free/reduced" : "lunch_free_reduced"


}


dados_final = dados_final.rename(columns = a_renomear)

#writing_score_percentage e reading_score_percentage estão em valores separados, entao eh necessario fazer uma media das duas notas
#atravez do mean ()
dados_final['average_score_languages'] = dados_final[['reading_score_percentage','writing_score_percentage']].mean(axis=1)

#apos calular eh necessario tirar as casas decimas e deixar duas casas apos a virgula
dados_final['average_score_languages'] = dados_final['average_score_languages'].round(2)


#colocando a math_percentage e average_score_languages em categótica


dados_final['math_percentage_class'] = (dados_final['math_percentage'] > 0.7).astype(int)
dados_final['average_score_languages_class'] = (dados_final['average_score_languages'] > 0.7).astype(int)

#APAGANDO AS COLUNAS QUE RESTARAM COM DADOS DECIMAIS
dados_final = dados_final.drop(['math_percentage','average_score_languages' ,'reading_score_percentage','writing_score_percentage'], axis=1)

#SEPARANDO AS ETNIAS
dados_final['white_people'] = dados_final['race_ethnicity_group_A'] + dados_final['race_ethnicity_group_B'] + dados_final['race_ethnicity_group_C']
dados_final['non_white_people'] = dados_final['race_ethnicity_group_D'] + dados_final['race_ethnicity_group_E']

#APAGANDO COLUNAS ANTIGAS DAS ETNIAS
dados_final = dados_final.drop(['race_ethnicity_group_A','race_ethnicity_group_B' ,'race_ethnicity_group_C','race_ethnicity_group_D', 'race_ethnicity_group_E'], axis=1)


dados = pd.DataFrame(dados_final)


