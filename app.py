import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import pickle

im = Image.open('image/favicon.ico')

st.set_page_config(page_title='Ticket priority Forecasting',
                   page_icon=im,
                   layout='wide',
                   initial_sidebar_state='auto')

st.image('image/logo.png')
st.title("Ticket priority Forecasting")

st.write("""
This app provides 24 hours of future forecast of tickets of varying severity levels using historic data.
""")
st.write('---')

# Loads Dataset
data_df = pd.read_csv('data/sample.csv', index_col = [0])
# Pivot the data
df = data_df.T
data_df = data_df.T.copy().reset_index().rename(mapper={'index':'date','P1':'Priority_1','P2':'Priority_2','P3':'Priority_3'}, axis=1)
st.write(data_df)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Priority_1")
    fig = px.line(data_df, x='date', y='Priority_1')
    fig.update_yaxes(title_text = 'Priority level 1')
    fig.update_xaxes(title_text='Date with Timestamps')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=False)

with col2:
    st.header('Priority_2')
    fig = px.line(data_df, x='date', y='Priority_2')
    fig.update_yaxes(title_text = 'Priority level 2')
    fig.update_xaxes(title_text='Date with Timestamps')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=False)

with col3:
    st.header('Priority_3')
    fig = px.line(data_df, x='date', y='Priority_3')
    fig.update_yaxes(title_text = 'Priority level 3')
    fig.update_xaxes(title_text='Date with Timestamps')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=False)

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'model/finalized_model.sav'

if agree:

    # Create model
    model = VAR(df)
    model = model.fit(10)

    # save the model to disk
    pickle.dump(model, open(filename, 'wb'))
else:
    # load the model from disk
    model = pickle.load(open(filename, 'rb'))

# predict Future datapoints

if st.button('Prediction'):

    lag_order = model.k_ar
    forecast =pd.DataFrame()
    forecast.index = pd.date_range(start ='2018-08-03 0:00',end='2018-08-03 22:00',freq='h')
    forecast[['P1','P2','P3']] = model.forecast(df.values[-lag_order:], 23)
    st.subheader("Forecaster Diagram for future datapoints")
    st.line_chart(forecast)

    result = forecast.to_csv().encode('utf-8')
    st.download_button('📥 Download future datapoints',result,'result.csv')
else:
    st.warning('Please Click on Prediction')

    
        