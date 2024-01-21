import streamlit as st
import pandas as pd
import preprocessor, helper

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)
st.sidebar.title('Olympic Analysis')


user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)
# st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years,country = helper.year_country_list(df)

    selected_year = st.sidebar.selectbox('Select Years',years)
    selected_country = st.sidebar.selectbox('Select Country',country)


    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year=='overall' and selected_country == 'overall':
        st.title('Overall Tally')
    if selected_year == 'overall' and selected_country != 'overall':
        st.title(f'Overall Tally for {selected_country}')
    if selected_year != 'overall' and selected_country == 'overall':
        st.title(f'Overall Tally in {selected_year}')
    if selected_year != 'overall' and selected_country != 'overall':
        st.title(f'Record medal for {selected_country} in {selected_year}')

    st.table(medal_tally)
