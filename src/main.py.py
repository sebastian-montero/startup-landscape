# %%
import requests
import streamlit as st
import pandas as pd

st.title('Company finder')

with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your search:')
    submit_button = st.form_submit_button(label='Submit')

res = requests.get(f"http://localhost:1919/{text_input}")

if 'sims' in res.json().keys():
    data = res.json()['sims']
    df = pd.DataFrame.from_records(data, columns=[
        "Company", 'Similarity'])
    st.write(df)

# %%
