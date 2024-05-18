# imports 

import time
import numpy as np
import pandas as pd
import streamlit as st
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Progamando a Barra Superior

#Titulo
st.write("*Formação Engenheriro de Machine Learning*")  
st.write("*Deploy de Modelos de Machine Learning*")
st.write("*Deploy de Aplicações Preditivas com Streamlit*")
st.title("Regressão Logística")

# Programando a Barra lateral

st.sidebar.header("Dataset e Hiperparâmetros")
st.sidebar.markdown("Selecione o Dataset Desejado")
Dataset = st.sidebar.selectbox('Dataset',('Iris','Wine','Breast Cancer')) # Elemento escolhido é armaezando na variável Dataset
Split = st.sidebar.slider("**Escolha o Percentual de Divisão dos Dados em Treino e Teste (Padrão= 70/30)**",0.1,0.9,0.7)
Solver = st.sidebar.selectbox('Algoritmo',('lbfgs','newton-cg','liblinear','sag'))
penality = st.sidebar.radio("Regularização:",('none','l1','l2','elasticnet'))
tol = st.sidebar.text_input("Tolerância para critério de parada (default= 1e-4):",'1e-4') # campo de preenchimento do usuário
max_iteration = st.sidebar.text_input("Número de Iterações (defalt = 5):", '50')

# Dicionário para os hiperparâmetros

parameters = {'Penality': penality, 'Tol':tol, 'Max_iteration': max_iteration, 'Solver': Solver}


#### Funções Para Carregar e Preaprar os Dados ####

# Função para carregar o dataset
def carrega_data(dataset):

    #Carrega o dataset
    if dataset == 'Iris':
        dados = sklearn.datasets.load_iris()
    elif dataset == 'Wine':
        dados = sklearn.datasets.load_wine()
    elif dataset == 'Breast Cancer':
        dados = sklearn.datasets.load_breast_cancer()
    
    return dados

# Função para preparar os dados 

def prepara_dados(dados, split):

    # Divide os dados de acordo com o valor de split definido pelo usuário:
    X_treino, X_teste, y_treino, y_teste = train_test_split(dados.data, dados.target, test_size= float(split), random_state= 42)

    # Prepara o scaler para padronização:
    scaler = MinMaxScaler()

    # Fit e transform nos dados de treino
    X_treino = scaler.fit_transform(X_treino)

    # Apenas transform nos dados de teste
    X_teste = scaler.transform(X_teste)

    return (X_treino, X_teste, y_treino, y_teste)


### Função para o modelo de machine learning ###

def cria_modelo(parameters):

    # Extrai os dados de treino e teste
    X_treino, X_teste, y_treino, y_teste = prepara_dados(Data,Split)

    # cria modelo

    clf = LogisticRegression(penalty= parameters['Penality'],
                             solver= parameters['Solver'],
                             max_iter= int(parameters['Max_iteration']),
                             tol= float(parameters['Tol']))
    
    # Treina o modelo
    clf = clf.fit(X_treino,y_treino)

    # Faz previsões
    prediction = clf.predict(X_teste)

    # Calcula a acurácia
    accuracy = sklearn.metrics.accuracy_score(y_teste,prediction)

    # Calcula a confusion matrix
    cm = confusion_matrix(y_teste, prediction)

    #Dicionatio com os resultados

    dict_value = {"modelo":clf, "acuracia": accuracy, "previsão": prediction, "y_real": y_teste, "Metricas":cm,'X_teste': X_teste}

    return(dict_value)

    return (X_treino, X_teste, y_treino, y_teste)

##### Programando o Corpo da Aplicação Web #####

st.markdown("""Resumo dos Dados""")
st.write("Nome do Dataset:", Dataset)

# Carrega o dataset escolhido pelo usuário

Data = carrega_data(Dataset)

#Extrai a variável alvo

targets = Data.target_names

#Prepara o dataframe com os dados 

Dataframe = pd.DataFrame(Data.data, columns= Data.feature_names)
Dataframe['target'] = pd.Series(Data.target)
Dataframe['target labels'] = pd.Series(targets[i] for i in Data.target)

# Mostra o dataset selecionado para usuário

st.write("visão Geral dos Atributos:")
st.write(Dataframe)


##### Programando o Botão de Ação #####

if(st.sidebar.button("Clique para Treinar o Modelo de Regressão Logística")):

    # Barra de progressão

    with st.spinner("Carregando o Dataset..."):
        time.sleep(1)

    # Info de Sucesso
    st.success("Dataset Carregado!")

    # Cria e treina o modelo
    modelo = cria_modelo(parameters)

    # Barra de progressão
    my_bar = st.progress(0)

    # Mostra a barra de progressão com percentual de conclusão

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    with st.spinner("Treinando o Modelo..."):
        time.sleep(1)

    # Info para o usuário
    st.sucesso("Modelo Treinado")

    # Extrai os labels reais
    labels_reais = [targets[i] for i in modelo['y_real']]

    # Extrai os labels previstos
    labels_previstos = [targets[i] for i in modelo['previsao']]

    st.subheader("Previsão do Modelo nos Dados de Teste")

    st.write(pd.DataFrame({'Valor Real': modelo['y_real'],
                           'Label Real': labels_reais,
                           'Valor Previsto': modelo['previsao'],
                           'Label Previsto': labels_previstos}))
    
    matriz = modelo["metricas"]

    st.subheader("Matriz de Confusão nos Dados de Teste")

    st.write(matriz)

    st.write("Acuracia do Modelo:", modelo["acuracia"])

    st.write("Obrigado por usar esta app!")





    

