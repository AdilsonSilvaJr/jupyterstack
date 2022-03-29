import streamlit as st
import pandas as pd

st.set_page_config(page_title="Formulário de Diagnóstico",
                   page_icon=":bar_chart:")#, layout='wide')

education_list = ('Não frequentou ou apenas o jardim', 
        'Ensino Fundamental', 
        'Ensino Medio Incompleto',
        'Ensino Medio Completo',
        'Ensino Superior Incompleto',
        'Ensino Superior Completo')

genhlt_list = ('Excelente', 'Muito Bom', 'Bom', 'Regular', 'Ruim')

yes_or_no =  ('Não', 'Sim')

st.title(":bar_chart: Formulário")

with st.form("my_form"):

    name_val = st.text_input('Seu Nome')
    left_column, right_column = st.columns(2)

    with left_column:
        weight = st.number_input('Peso', value=1)
        smoker = st.selectbox('Fumante', yes_or_no)
        age = st.number_input('Idade')
        education = st.selectbox('Qual o seu nivel de escolaridade?', education_list)
        physhlt = st.slider('Em quantos dias a sua saúde física não foi boa', 0, 30, 1)
        submitted = st.form_submit_button("Enviar")

    with right_column:
        height = st.number_input('Altura', value=1)
        highbp = st.selectbox('Pressão Alta', yes_or_no)
        fruits = st.selectbox('Come fruta regularmente?', yes_or_no)
        income = st.number_input('Salario (Bruto em conjunto)')
        genhlt = st.selectbox('Como você avalia sua saúde geral?', genhlt_list)
        menthlt = st.slider('Em quantos dias a sua saúde mental não foi boa', 0, 30, 1)

#Tratamento das variáveis
def return_dict(list_elements):
    return {item: i+1 for i, item in enumerate(list_elements)}

dict_yes_or_no = return_dict(yes_or_no)
dict_education = return_dict(education_list[::-1])
dict_genhlt    = return_dict(genhlt_list[::-1])

#Tratamento dos dados recebidos
bmi = round(weight / (height ** 2))

#Pelo laço começar pelo 1
smoker = dict_yes_or_no[smoker] - 1
highbp = dict_yes_or_no[highbp] - 1
fruits = dict_yes_or_no[fruits] - 1

education = dict_education[education]
genhlt = dict_genhlt[genhlt]

if submitted:
    columns = ['BMI','Age','Income','PhysHlth', 'Education', 'GenHlth', 'MentHlth', 'HighBP', 'Fruits', 'Smoker']
    input = [[bmi, int(age), income, physhlt, education, genhlt, menthlt, highbp, fruits, smoker]]
    data = pd.DataFrame(data=input, columns=columns)
    st.write(data.head())