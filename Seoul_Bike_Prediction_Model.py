import numpy as np
import pickle
import pandas as pd
import streamlit as st



pickle_in = open("rf_model", "rb")
model = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def seoulbikedemand_prediction(hour,temperature, wind_speed, visibility, rainfall,snowfall, C_Autumn, C_Spring, C_Summer, C_Winter):
    predictionn = model.predict([[hour, temperature, wind_speed, visibility, rainfall,
       snowfall, C_Autumn, C_Spring, C_Summer, C_Winter]])
    print(predictionn)
    return predictionn


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>SEOUL Total Bike Count Predictor</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Drop in the required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)
  st.image('./seoulbike.jpg')
  st.sidebar.header("What is this Project about?")
  st.sidebar.markdown("It a Web app that would help the user to predict the total bike count in a season.")
  st.sidebar.header("What tools where used to make this?")
  st.sidebar.markdown("The Model was made using a dataset from UCI Machine Learning Repository. I have utilized Linear Regression, LASSO, Ridge and Random Forest in our model.")
  
  
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
  </div>
  """
  temperature = st.slider("Select Temperature in celsius",min_value=-10.0,max_value=39.0,step = 1.0) 
  hour = st.slider("Hour: ", 0, 23, value=0, format="%d")
  wind_speed = st.slider("Select expected wind speed in m/s",min_value = 0.0,max_value = 7.40,step = 0.10)
  visibility = st.slider("Select Visbility in m",min_value=0.0,max_value=8.8,step = 0.10) 
  rainfall = st.slider("Select expected rainfall in mm",min_value=0.0,max_value=8.8,step = 0.10) 
  snowfall = st.slider("Select expected snowfall in cm",min_value=0.0,max_value=8.8,step = 0.10) 



  # for season
  season_list = ['C_Spring', 'C_Autumn', 'C_Summer', 'C_Winter']
  season = st.selectbox('which season', season_list)

  if season == 'C_Autumn':
      C_Spring = 0
      C_Summer = 0
      C_Winter = 0
      C_Autumn = 1
  elif season == 'C_Spring':
      C_Spring = 1
      C_Summer = 0
      C_Winter = 0
      C_Autumn=0
  elif season == 'C_Summer':
      C_Spring = 0
      C_Summer = 1
      C_Winter = 0
      C_Autumn =0
  elif season == 'C_Winter':
      C_Spring = 0
      C_Summer = 0
      C_Winter = 1
      C_Autumn =0
 
  
  result = ""
  if st.button("Predict"):
      result = seoulbikedemand_prediction(hour,temperature, wind_speed, visibility, rainfall,snowfall, C_Autumn, C_Spring, C_Summer, C_Winter)
  st.success('The predicted bike count is {}'.format(result))

if __name__ == '__main__':
    main()