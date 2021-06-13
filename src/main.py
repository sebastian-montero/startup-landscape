from pandas._config.config import describe_option
import requests
import streamlit as st
import pandas as pd


st.set_option('deprecation.showPyplotGlobalUse', False)

# NAVBAR

# start = st.sidebar.button('Start the app')

with st.sidebar.form(key='filters'):
    # Load country list
    countries = requests.get("https://limitless-coast-08153.herokuapp.com/variables/countries")
    countries =countries.json()['data']

    country_selection = st.multiselect('Country', countries)

    # Load tag list
    tags = requests.get("https://limitless-coast-08153.herokuapp.com/variables/tags")
    tags =tags.json()['data']
    tag_selection = st.multiselect('Tags', tags)

    # Submit API
    submitted = st.form_submit_button("Submit")

st.markdown("# Startup Analytics")
st.markdown("The Startup Analytics website is a data web app that allows anyone to find European startups. This app relies in the data of the [EU-Startups](https://www.eu-startups.com/directory/) website and makes it easier to find startups in the hottest topics across different European countries.")
st.markdown("To start, just filter for the topic of interest and for the country. Either of these search fields can be left blank so show all companies.")
# COMPANY LIST
data = {'countries': country_selection, "tags":tag_selection}
comps = requests.post("https://limitless-coast-08153.herokuapp.com/companies", json = data)
comps_filtered = pd.DataFrame(eval(comps.json()))


if len(comps_filtered) != 0:
    st.markdown("## Companies")
    st.dataframe(data=comps_filtered.drop(['website','tags'],axis=1))
    st.markdown(f"#### Total number of results: {len(comps_filtered)}")

    with st.sidebar.form(key='comp_sel'):
        comp = st.selectbox('Select Company', comps_filtered['name'])
        submitted2 = st.form_submit_button("Submit")


    comp = requests.get(f"https://limitless-coast-08153.herokuapp.com/companies/{comp}")
    comp = comp.json()['data']
    st.markdown(f"## Company Profile")
    st.markdown(f"### {comp['name']}")
    st.markdown(f"**HQ**: {comp['category']}  ")
    st.markdown(f"**Founded**: {comp['founded']}  ")
    st.markdown(f"**Funding**: {comp['funding']}  ")
    st.markdown(f"**Description**: {comp['description']} ")
    st.markdown(f"**Website**: {comp['website']}")
