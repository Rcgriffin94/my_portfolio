import streamlit as st
import get_nfl_data 
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.header('NFL Trends')

all_games = get_nfl_data.get_all_games()

teams = get_nfl_data.teams
team_names = sorted(teams.keys())
team_selection = st.selectbox(options=teams, label='Team Name', placeholder='Select a team', index=None) 
st.divider()

if team_selection is not None:

    team_games = all_games[team_selection]
    team_games = team_games.sort_values('gameday', ascending = False).reset_index(drop=True)

    team_color = teams[team_selection]['color']
    fig1 = px.line(team_games, x='gameday', y='home_score', color_discrete_sequence=[team_color], title='Placeholder 1')
    fig2 = px.line(team_games, x='gameday', y='home_score', color_discrete_sequence=[team_color], title='Placeholder 2')
    fig3 = px.line(team_games, x='gameday', y='home_score', color_discrete_sequence=[team_color], title='Placeholder 3')
    fig4 = px.line(team_games, x='gameday', y='home_score', color_discrete_sequence=[team_color], title='Placeholder 4')

    st.header(f'Analyzing the {team_selection}')

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(fig3, use_container_width=True)
    with col4:
        st.plotly_chart(fig4, use_container_width=True)

    st.dataframe(data=team_games, use_container_width=True)