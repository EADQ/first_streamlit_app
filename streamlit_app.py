import streamlit as st
import pandas as pd

# MAKING BASE MENU
st.title('My Parents New Healthy Diner')
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
st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# DISPLAY THE TABLE ON THE PAGE
st.dataframe(my_fruit_list)
