from re import template
import streamlit as st
import plotly.express as px
import pandas as pd


def app():
    df = pd.read_parquet(
        "datasets/diabetes_012_health_indicators_BRFSS2015.parquet")

    # Utilitarios
    dicionario_labels = {
        "HighBP": ['Pressao Normal', 'Pressao Alta'],
        "HighChol": ['Colesterol Normal', 'Colesterol Alto'],
        "Smoker": ['Não Fumante', 'Fumante'],
        "Stroke": ['Não teve AVC', 'Teve AVC'],
        "DiffWalk": ['Normal', 'Dificuldade de Andar'],
        "GenHlth": ['Excelente', 'Muito Bom', 'Bom', 'Regular', 'Ruim']
    }

    tipos = ['Sem Diabetes', 'Pre Diabetes', 'Com Diabetes']
    tipos_dict = {item: i for i, item in enumerate(tipos)}

    st.title(":bar_chart: Dashboard de Análise")

    def graficos_categoricos(df, variavel, labels, tipos):
        df_categorico = df.groupby("Diabetes_012")[variavel]\
            .value_counts(normalize=True)\
            .unstack()\
            .mul(100)\
            .round(2)

        if len(labels) == 2:
            df_categorico["Tipo"] = tipos
            rename_dict = {i: item for i, item in enumerate(labels)}
        else:
            df_categorico = df_categorico.T
            df_categorico["Tipo"] = labels
            rename_dict = {i: item for i, item in enumerate(tipos)}

        df_categorico.rename(columns=rename_dict, inplace=True)
        return df_categorico

    def retorna_histograma(df, tipo, width=600):
        histograma = px.histogram(
            df,
            x=tipo,
            color_discrete_sequence=["darkblue", "purple", "blue"],
            width=width,
            height=400,
            histnorm='probability',
            title=f"Gráfico {tipo}",
            template="simple_white"
        )
        return histograma

    # Menu Lateral
    st.sidebar.markdown("## Escolha o Tipo")
    fator_inicial = st.sidebar.selectbox("Filtro", tipos)

    st.sidebar.markdown("## :pill: Fatores de Risco")
    fator_cat = st.sidebar.selectbox("Variáveis Categóricas",
                                     ("HighBP", "HighChol", "Smoker", "Stroke", "DiffWalk"))

    fator_num = st.sidebar.selectbox("Variáveis Numéricas",
                                     ("Age", "Income", "Education"))

    # Containers
    container_inicial = st.container()
    col1, col2, col3 = st.columns(3)

    with container_inicial:
        col1.metric("Quantidade de Dados", df.shape[0])
        col2.metric("Porcentagem de Diabeticos", "17,28%")
        col3.metric("Pessoas com plano de saude", "94,46%")

    container_graficos1 = st.container()
    col4, col5 = st.columns(2)

    container_graficos2 = st.container()
    col6, col7 = st.columns(2)

    # Dashboard
    df_categorico = graficos_categoricos(
        df, fator_cat, dicionario_labels[fator_cat], tipos)
    df_filtro = df[df['Diabetes_012'] == tipos_dict[fator_inicial]]
    df_barras = graficos_categoricos(
        df, 'GenHlth', dicionario_labels['GenHlth'], tipos)

    figure1 = px.bar(
        df_categorico,
        x='Tipo',
        y=df_categorico.columns[:-1],
        color_discrete_sequence=["darkblue", "blue"],
        template="simple_white",
        width=600,
        height=400,
        title=fator_cat
    )

    figure2 = px.bar(
        df_barras,
        x="Tipo",
        y=df_barras.columns[:-1],
        color_discrete_sequence=["blue", "purple", "darkblue"],
        barmode='group',
        template="simple_white",
        width=600,
        height=400,
        title="Saúde Geral"
    )

    histogram1 = retorna_histograma(df_filtro, "BMI", 1200)
    histogram2 = retorna_histograma(df_filtro, fator_num)

    with container_graficos1:
        with col4:
            st.plotly_chart(figure1)
        with col5:
            st.plotly_chart(histogram2)

    with container_graficos2:
        with col6:
            st.plotly_chart(figure2)
        with col7:
            figure_pie = px.pie(df_filtro, names='Sex', color_discrete_sequence=["darkblue", "blue"],
                template="simple_white", width=600, height=400, title="Distribuição Por Sexo")
            st.plotly_chart(figure_pie)

    st.plotly_chart(histogram1)
