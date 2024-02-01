import streamlit as st 
import pandas as pd 
import joblib

clf = joblib.load('model/stroke_model.pkl') # importamos el modelo

st.title('Rellena estos campos, para saber si un paciente ha sufrido un infarto cerebral')

col1, col2 = st.columns(2)  # con las columnas haremos más agradable el cuestionario

with col1:
    gender = st.selectbox('Genero: ',('Hombre', 'Mujer'))
    age = st.number_input('Edad: ',step=1, min_value=0, max_value=120)
    hipertension = st.checkbox('Padece de Hipertensión')
    heart_des = st.checkbox('Padece de alguna enfermedad cardiaca')
    casado = st.checkbox('Está casad@')

with col2:
    work = st.selectbox('Tipo de trabajo: ',('Joven', 'Funcionario', 'Desempleado','Privado','Autónomo'))
    glucosa = st.number_input('Nivel de glucosa en sangre: ',step=1, min_value=50, max_value=299)
    imc = st.number_input('Indice de masa corporal: ',step=1, min_value=12, max_value=49)
    smoke = st.selectbox('Fumador: ',('A veces', 'Nunca', 'Habitual','Desconocido'))

# Los checkboxs devuelven booleano, haciendo esto funcionará
hiper = 1 if hipertension else 0
heart = 1 if heart_des else 0
marry = 1 if casado else 0

if st.button('Submit'):
    st.write('Realizando la predicción...')
    
    X = pd.DataFrame([[gender, age, hiper, heart, marry, work, glucosa, imc, smoke]],
                     columns=['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'avg_glucose_level', 'bmi', 'smoking_status'])
    
    gender_mapping = {'Hombre': 0, 'Mujer': 1}
    work_mapping = {'Joven': 0, 'Funcionario': 1, 'Desempleado': 2, 'Privado': 3, 'Autónomo': 4}
    smoke_mapping = {'A veces': 0, 'Nunca': 1, 'Habitual': 2, 'Desconocido': 3}
    
    X['gender'] = X['gender'].map(gender_mapping)
    X['work_type'] = X['work_type'].map(work_mapping)
    X['smoking_status'] = X['smoking_status'].map(smoke_mapping)

    res = clf.predict(X)
    if res == 0:
        st.write('No ha sufrido un infarto antes')
    elif res == 1:
        st.write('SI ha sufrido un infarto anteriormente')