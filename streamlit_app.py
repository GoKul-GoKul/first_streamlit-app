import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#create a funtion for displaying
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information:")
  else:
    streamlit.dataframe(get_fruityvice_data(fruit_choice))

except URLError as e:
  streamlit.error()

streamlit.write('The user entered ', fruit_choice)

streamlit.stop()

# import snowflake.connector
streamlit.header("The fruit load list contains")
#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)


#add a text box challenge lab
#allow the end user to add a fruit to the list

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What Fruit would you like to have?')
if streamlit.button("Add a Fruit to the List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.text(insert_row_snowflake(add_my_fruit))


