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
if hipertension:
    hiper = 1
else:
    hiper = 0

if heart_des:
    heart = 1
else:
    heart = 0
if casado:
    marry = 1
else:
    marry = 0


if st.button('Submit'):
    X = pd.DataFrame([[gender,age,hiper,heart,marry,work,glucosa,imc,smoke]],columns=['gender','age','hypertension','heart_disease','ever_married','work_type','avg_glucose_level','bmi','smoking_status'])
    X = X.replace(['Hombre','Mujer'],[0,1])
    X = X.replace(['Joven', 'Funcionario', 'Desempleado','Privado','Autónomo'],[0,1,2,3,4])
    X = X.replace(['A veces', 'Nunca', 'Habitual','Desconocido'],[0,1,2,3])
    res = clf.predict(X)
    st.write(f'{res} ha sufrido un infarto')