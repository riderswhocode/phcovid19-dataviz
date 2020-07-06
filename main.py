import pandas as pd
import numpy as np
import streamlit as st
from bokeh.plotting import figure
import matplotlib.pyplot as plt

st.title('PH Covid19 - Historical Data')
st.markdown('CHEER ME UP PLEASE :(')
st.write("""
    Interactive Graph for
    Philippines Covid19 Historical Data
""")

st.sidebar.header('Users Input')

csv_file = st.sidebar.file_uploader("Upload the CSV File here", type=["csv"])
view_set = st.sidebar.selectbox('Select History Data view',('Daily Case Recorded','Daily Deaths Recorded','Daily Recoveries Recorded'))

date_label = []
daily_case = []
daily_death = []
daily_recovery = []

if csv_file is not None:
    pdf = pd.read_csv(csv_file)
    date = pdf['Date']
    daily_case_data = pdf['Daily Case Increase']
    daily_death_data = pdf['Daily Death']
    daily_recovery_data = pdf['Daily Recovery']
    
    print('Start loading data!')
    def loadData(date_var, daily_case_var, daily_death_var, daily_recovery_var):
        for data in date_var.items():
            if str(data[1]):
                date_label.append(str(data[1]))
                
        for daily_case_data in daily_case_var.items():
            if str(daily_case_data[1]):
                daily_case.append(str(daily_case_data[1]))

        for daily_death_data in daily_death_var.items():
            if str(daily_death_data[1]):
                daily_death.append(str(daily_death_data[1]))

        for daily_recovery_data in daily_recovery_var.items():
            if str(daily_death_data[1]):
                daily_recovery.append(str(daily_recovery_data[1]))
                print(daily_recovery_data[1])

    loadData(date,daily_case_data,daily_death_data,daily_recovery_data)

    daily_case_chart = figure(
        title = 'Daily Case Increase',
        x_axis_label = 'Date',
        y_axis_label = 'Daily Case Increase'
    )

    daily_death_chart = figure(
        title = 'Daily Death',
        x_axis_label = 'Date',
        y_axis_label = 'Daily Deaths'
    )

    daily_recovery_chart = figure(
        title = 'Daily Recovery',
        x_axis_label = 'Date',
        y_axis_label = 'Daily Recovery'
    )

    new_df_case = pd.DataFrame({
        'date' : date,
        'new_case_daily' : daily_case_data,
        'new_death_daily' : daily_death_data,
        'new_recovery_daily' : daily_recovery_data
    })


    ax = plt.gca()

    pdf['Daily Case Increase'] = pd.to_numeric(pdf['Daily Case Increase'], errors='coerce')
    pdf['Daily Death'] = pd.to_numeric(pdf['Daily Death'], errors='coerce')
    pdf['Daily Recovery'] = pd.to_numeric(pdf['Daily Recovery'], errors='coerce')

    new_df_case = new_df_case.set_index('date')

    new_df_case

    st.line_chart(new_df_case, use_container_width=True)

    daily_case_chart.line(date_label, daily_case_data, legend_label='Daily Case', line_width=2, color='red')
    daily_death_chart.line(date_label, daily_death_data, legend_label='Daily Deaths', line_width=2, color='blue')
    daily_recovery_chart.line(date_label, daily_recovery_data, legend_label='Daily Recovery', line_width=2, color='green')
   
    st.header("Historical Data")
    if view_set == 'Daily Case Recorded':
        st.subheader("Daily Case Recorded")
        st.bokeh_chart(daily_case_chart, use_container_width=True)
    elif view_set == 'Daily Deaths Recorded':
        st.subheader("Daily Death Recorded")
        st.bokeh_chart(daily_death_chart, use_container_width=True)
    else:
        st.subheader("Daily Recovery Recorded")
        st.bokeh_chart(daily_recovery_chart, use_container_width=True)


