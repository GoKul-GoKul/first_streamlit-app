import streamlit

import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

myfruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#multilist in streamlist to select the meal
streamlit.multiselect("Pick Any fruits:", myfruits_list)

#streamlit dataframe
streamlit.dataframe(myfruits_list)
