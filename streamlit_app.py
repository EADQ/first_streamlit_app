import streamlit as st
import pandas as pd
import requests
import snowflake.connector

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
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

# CALLING RHE FRUITYVICE API'
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# WRITE YOUR OWN COMMENT -WHAT DOES THE NEXT LINE DO? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# WRITE YOUR OWN COMMENT - WHAT DOES THIS DO?
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
