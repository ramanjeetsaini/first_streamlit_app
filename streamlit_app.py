import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🐔 Butter Chicken')
streamlit.text('🥣 Dal Tadka')
streamlit.header(' Build your own smoothie')
