import streamlit as st
from multiapp import MultiApp
from apps import dashboard, model  # import your app modules here

app = MultiApp()

st.set_page_config(layout="wide")
st.sidebar.markdown("""
# Projeto  Predição de diabetes 
## Time Jupyter 🚀

""")

# Add all your application here
app.add_app("Dashboard", dashboard.app)
app.add_app("Modelo", model.app)
# The main app
app.run()
