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

# CALLING THE DATAFRAME WITH STREAMLIT
# streamlit.dataframe(my_fruit_list)


