# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns


# Set plot styl
sns.set_style("dark")

# Remove Warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Deaths of Breaking Bad - Stats")

# import dataset
deaths = pd.read_csv('deaths.csv')


# Selection of method of visualization
options = ['Season wise deaths', 'Cause of deaths',
           'Kill count of characters', 'Raw data']
option = st.selectbox('Display Data', options)


# Function to display data according to selection
def death_table_plot(parameter, sort_parameter, is_ascending, graph_title, graph_x, graph_y):
    condition_death = deaths[[parameter, 'number_of_deaths']]
    group_cd = condition_death.groupby(
        [parameter]).sum().sort_values(by=sort_parameter, ascending=is_ascending)
    st.table(group_cd)

    st.header(graph_title)
    death_plot = sns.barplot(x='number_of_deaths', y=group_cd.head().index,
                             data=group_cd.head(), ci=None, palette="muted", orient='h')
    death_plot.set_xlabel(graph_x)
    death_plot.set_ylabel(graph_y)
    st.pyplot()


# Season wise deaths
if option == options[0]:
    death_table_plot('season', 'season', True,
                     "Visualization", "Death Count", "Season")

# Cause of deaths
if option == options[1]:
    death_table_plot('cause', 'number_of_deaths', False,
                     "Top Causes of Death", "Death Count", "Cause")

# Kill count of characters
if option == options[2]:
    death_table_plot('responsible', 'number_of_deaths',
                     False, "Top Perpetrator", "Kill Count", "Perpetrator")

# Raw data
if option == options[3]:
    st.table(deaths)
    st.header("Incidents of deaths over the show")
    death_arr = np.array(deaths.number_of_deaths)
    plt.plot(death_arr)
    plt.xlabel("Incidents")
    plt.ylabel("Death Count")
    st.pyplot()