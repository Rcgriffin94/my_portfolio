import streamlit as st
import get_nfl_data 

st.set_page_config(layout='wide')
st.header('NFL Trends')

all_games = get_nfl_data.get_games()

teams = sorted(get_nfl_data.teams.keys())
team_selection = st.selectbox(options=teams, label='Team Name', placeholder='Select a team', index=None) 

if team_selection is not None:

    st.dataframe(data=all_games[team_selection], use_container_width=True)