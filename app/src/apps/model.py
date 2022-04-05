import streamlit as st
import pandas as pd
import requests
import os
import json


def app():
    api_ml_url = os.environ.get('API_ML_SERVICE_SERVICE_HOST')
    api_ml_port = os.environ.get('API_ML_SERVICE_SERVICE_PORT')

    age_list = ('18 a 24 anos',
                '25 a 29 anos',
                '30 a 34 anos',
                '35 a 39 anos',
                '40 a 44 anos',
                '45 a 49 anos',
                '50 a 54 anos',
                '55 a 59 anos',
                '60 a 64 anos',
                '65 a 69 anos',
                '70 a 74 anos',
                '75 a 79 anos',
                '80 anos ou mais')

    education_list = ('Não frequentou ou apenas o jardim',
                      'Ensino Fundamental',
                      'Ensino Medio Incompleto',
                      'Ensino Medio Completo',
                      'Ensino Superior Incompleto',
                      'Ensino Superior Completo')

    income_list = ('Até $ 10.000,00',
                   'De $ 10.000,01 a $ 15.000,00',
                   'De $ 15.000,01 a $ 20.000,00',
                   'De $ 20.000,01 a $ 25.000,00',
                   'De $ 25.000,01 a $ 35.000,00',
                   'De $ 35.000,01 a $ 50.000,00',
                   'De $ 50.000,01 a $ 75.000,00',
                   'Mais que $ 75.000,00 ')

    genhlt_list = ('Ruim', 'Regular', 'Bom', 'Muito Bom', 'Excelente')

    yes_or_no = ('Não', 'Sim')

    st.title(":bar_chart: Formulário")

    with st.form("my_form"):

        left_column, right_column = st.columns(2)

        with left_column:
            weight = st.number_input('Peso', value=1.0)
            smoker = st.selectbox('Fumante', yes_or_no)
            age = st.selectbox('Qual a sua faixa de idade?', age_list)
            education = st.selectbox(
                'Qual o seu nivel de escolaridade?', education_list)
            physhlt = st.slider(
                'Em quantos dias a sua saúde física não foi boa', 0, 30, 1)
            submitted = st.form_submit_button("Enviar")

        with right_column:
            height = st.number_input('Altura', value=1.00)
            highbp = st.selectbox('Pressão Alta', yes_or_no)
            fruits = st.selectbox('Come fruta regularmente?', yes_or_no)
            income = st.selectbox(
                'Qual a sua renda familiar anual bruta?', income_list)
            genhlt = st.selectbox(
                'Como você avalia sua saúde geral?', genhlt_list)
            menthlt = st.slider(
                'Em quantos dias a sua saúde mental não foi boa', 0, 30, 1)

    # Tratamento das variáveis
    def return_dict(list_elements):
        return {item: i+1 for i, item in enumerate(list_elements)}

    dict_yes_or_no = return_dict(yes_or_no)
    dict_age = return_dict(age_list[::1])
    dict_education = return_dict(education_list[::1])
    dict_income = return_dict(income_list[::1])
    dict_genhlt = return_dict(genhlt_list[::-1])

    # Tratamento dos dados recebidos
    bmi = round(weight / (height ** 2))

    # Pelo laço começar pelo 1
    smoker = dict_yes_or_no[smoker] - 1
    highbp = dict_yes_or_no[highbp] - 1
    fruits = dict_yes_or_no[fruits] - 1

    age = dict_age[age]
    education = dict_education[education]
    income = dict_income[income]
    genhlt = dict_genhlt[genhlt]

    if submitted:
        with st.spinner('Modelando seus dados...'):
            url = 'http://{}:{}/predict'.format(api_ml_url, api_ml_port)
            data_ml = {
                "BMI": bmi,
                "Age": age,
                "Income": income,
                "PhysHlth": physhlt,
                "Education": education,
                "GenHlth": genhlt,
                "MentHlth": menthlt,
                "HighBP": highbp,
                "Fruits": fruits,
                "Smoker": smoker
            }
            predict_values = requests.post(url, json=data_ml)

            predict_response = json.loads(predict_values.text)

            score_percent = round(predict_response['score'] * 100)
            predict_int = int(predict_response['predict'])

            if predict_int == 0:
                st.info('Você **NÃO POSSUI** risco de ter diabetes')
            elif predict_int == 1:
                st.info('Você **POSSUI** risco de ter prediabetes')
            else:
                st.info('Você **POSSUI** risco de ter diabetes')

            st.info(
                'Sua conformidade com o modelo é de **{}%**'.format(score_percent))
