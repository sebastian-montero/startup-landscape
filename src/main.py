from pandas._config.config import describe_option
import requests
import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)


# load data
comps = pd.read_csv("data/comps.csv")
tags = pd.read_csv("data/tags.csv")
countries = pd.read_csv("data/countries.csv")

# NAVBAR

start = st.sidebar.button('Start the app')


with st.sidebar.form(key='filters'):
    # Load country list
    country_selection = st.multiselect('Country', countries['country'])

    # Load tag list
    tag_selection = st.multiselect('Tags', tags['tags'])

    # Submit API
    submitted = st.form_submit_button("Submit")

st.markdown("# Startup Analytics")

# COMPANY LIST
st.markdown("## Companies")
comps_filtered = comps[comps['country'].isin(country_selection)]
st.dataframe(data=comps_filtered.head(50), width=1000)

if len(comps_filtered) != 0:
    with st.sidebar.form(key='comp_sel'):
        comp = st.selectbox('Select Company', comps_filtered['company'])
        hide_df = st.radio("Hide table?", ["Yes", "No"])
        # submitted = True
        submitted2 = st.form_submit_button("Submit")

# Select company
name = comps[comps['company'] == comp]['company'].iloc[0]
desc = comps[comps['company'] == comp]['description'].iloc[0]
founded = comps[comps['company'] == comp]['year founded'].iloc[0]
country = comps[comps['company'] == comp]['country'].iloc[0]

col1, col2 = st.beta_columns(2)
with col1:
    st.markdown(f"""
    ## {name}
    **HQ**: {country}  
    **Founded**: {founded}  
    **Description**: {desc}
    **Website**: xxxx
    """)
with col2:
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    graph = nx.draw(G, with_labels=True)
    st.pyplot(graph)
