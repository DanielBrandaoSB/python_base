# imports 

import time
import numpy as np
import pandas as pd
import streamlit as st
import sklearn.metrics
import sklearn.datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import pydeck

### Teste
st.title("Teste de Componentes")
st.header("Funcionalidades do streamlit")

### Barra Lateral

#Titulo
st.sidebar.title("Barra Lateral Funcionalidades")
st.sidebar.header("Funcionalidades")
data_inicial = st.sidebar.date_input("Data Inicial", min_value= pd.to_datetime('2024-01-01'))
data_final = st.sidebar.date_input("Data Final",min_value= pd.to_datetime("2024-01-01"))

st.write(data_inicial)
st.write(data_final)
st.metric(label= "Temperatura", value= '70 F', delta="1.2 F")

### Metrics
st.title("Métricas Principais")
col1, col2, col3 = st.columns(3)
var = 1000
delta = 100
col1.metric("Volumetria Média (12 Meses)",f'{var}',f'{delta} pedidos', help=' O indicador leva em consideração o CBK de Jan/23 até Jan/24')
col2.metric("%ChargeBack Médio (12 Meses)", '0.5%', -0.1)
col3.metric("%Bloqueio Médio (12 Meses)", '0.3%', "0.1")
print(data_inicial)
print(data_final)

### Enviar Arquivos 

st.file_uploader("Choose a CSV file")

