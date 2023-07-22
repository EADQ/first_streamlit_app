import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

# MAKING BASE MENU
st.title("My Mom's New Healthy Diner")
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌 🥭 Build Your Own Fruit Smoothie 🥝 🍇')

# IMPORTING CSV TABLE
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# ADDING INTERACTION WITH THE MENU
# LET'S PUT A PICK LIST HERE SO THE CAN PICK THE FRUIT THEY WANT TO INCLUDE
# st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# LET'S PUT A PICK LIST HER SO THEY CAN PICK THE FRUIT THEY WANT TO INCLUDE
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# DISPLAY THE TABLE ON THE PAGE
st.dataframe(fruits_to_show)

# NEW SECTION TO SHOW ADVICE
st.header("Fruityvice Fruit Advice!")

# ADDING FRUIT CHOICE
try:
    fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
    if not fruit_choice:
        st.error("Please select a fruit to get information.")
    else:
# CALLING RHE FRUITYVICE API'
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# WRITE YOUR OWN COMMENT -WHAT DOES THE NEXT LINE DO? 
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# WRITE YOUR OWN COMMENT - WHAT DOES THIS DO?
        st.dataframe(fruityvice_normalized)

except URLError as e:
    st.error("Error, unable to connect to the API")

# ADDING FRUIT ADVICE
# fruit_advice = st.text_input('What fruit would you like information about?','Kiwi')
fruit_advice = st.text_input('What fruit would you like information about?', 'Kiwi', key='fruit_input')
st.write('The user entered ', fruit_advice)

# DON'T RUN ANYTHING PAST HERE WHILE WE TROUBLESHOOT
st.stop()

# CONNECTING WITH SNOWFLAKE
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

# THIS WILL NOT WORK CORRECTLY, BUT JUST GO WITH IT FOR NOW
# my_cur.execute('insert into fruit_load_list values ("from setreamlite")')
my_cur.execute("insert into fruit_load_list values ('from setreamlite')")
