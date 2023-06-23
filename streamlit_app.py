import streamlit

import pandas

streamlit.title('New Healthy Diner for Restaurant')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

myfruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruits_list = myfruits_list.set_index('Fruit')

#multilist in streamlist to select the meal
fruits_selected = streamlit.multiselect("Pick Any fruits:", list(myfruits_list.index),['Avocado','Strawberries'])
fruits_to_show = myfruits_list.loc[fruits_selected]

#streamlit dataframe
streamlit.dataframe(fruits_to_show)

#requests
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
